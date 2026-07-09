from piccolo.apps.migrations.auto.migration_manager import MigrationManager
from piccolo.table import Table


# Dummy table we use to execute raw SQL with
class RawTable(Table):
    pass


def postgresql_code_block(sql: str) -> str:
    """
    Wrap the given SQL in a PostgreSQL DO block, allowing multiple SQL
    statements to be executed in a single RawTable.raw() call.
    """

    sql = sql.strip()

    # Ensure the SQL ends with a semicolon
    if sql and not sql.endswith(";"):
        sql += ";"

    return f"""
DO $nephthys_migration_block$
BEGIN
{sql}
END;
$nephthys_migration_block$
LANGUAGE plpgsql;
"""


def raw_migration(
    migration_id: str,
    app_name: str,
    description: str,
    forwards: str,
    backwards: str | None = None,
):
    manager = MigrationManager(
        migration_id=migration_id,
        app_name=app_name,
        description=description,
    )

    async def run():
        await RawTable.raw(postgresql_code_block(forwards))

    manager.add_raw(run)

    if backwards:

        async def run_backwards():
            await RawTable.raw(postgresql_code_block(backwards))

        manager.add_raw_backwards(run_backwards)

    return manager
