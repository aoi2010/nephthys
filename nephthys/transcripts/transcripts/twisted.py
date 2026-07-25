from nephthys.transcripts.transcript import Transcript


class Twisted(Transcript):
    """Transcript for Twisted YSWS"""

    program_name: str = "Twisted"
    program_owner: str = "U0A5NKH93BJ"  # @aoishik

    help_channel: str = "C0BKH9PQLPP"  # #Twisted-help
    ticket_channel: str = "C0BKG9RBZRR"
    team_channel: str = "C0AD3HRV4F8"

    faq_link: str = "https://hackclub.enterprise.slack.com/docs/T0266FRGM/F0ASVGKKBRD"
    first_ticket_create: str = f"""
Heya (user)! Welcome to the Twisted help channel! Someone from our team will be here to help you out soon.
If you haven't already, have a read through <{faq_link}|*the FAQ*> – it will likely contain the answer you're looking for!
If your question has been answered, please hit the button below to mark it as resolved!
    """
    ticket_create: str = f"""
Hi (user), welcome back to the Twisted help channel! Someone should be along to help you soon.
As a reminder, you can take a look at <{faq_link}|*the FAQ*> while you wait – it might contain the answer to your question! :D
"""
    resolve_ticket_button: str = "Mark As Resolved"
    ticket_resolve: str = f"<@{{user_id}}> has marked this as resolved. If you think this was a mistake, you may reopen this ticket. More questions? Feel free to send another message in <#{help_channel}> and we'll be there to help too!"

    not_allowed_channel: str = f"Heya, it looks like you're not supposed to be in that channel, pls talk to <@{program_owner}> If that's wrong."
    faq_macro: str = f"""
Hi (user), this question is already answered in our FAQ!

Here's the link again: <{faq_link}|*Twisted FAQ*>.

_I've marked this question as resolved, so please start a new thread if you need more help_
    """
