# CareConnect: A Mental Health Support App
# Author: Elisee Kaneza
# Course: CIS129 - Final Project

class CareConnect:
    def __init__(self):
        self.mood_log = []
        self.journal_entries = []

    def log_mood(self, mood):
        """Track how the user is feeling with emoji-based input."""
        self.mood_log.append(mood)
        print(f"Mood '{mood}' logged.")

    def write_journal(self, entry):
        """Capture thoughts or reflections in a quick journal entry."""
        self.journal_entries.append(entry)
        print("Journal entry saved.")

    def send_motivational_message(self):
        """Deliver a daily motivational message to uplift the user."""
        message = "Every day is a new beginning. You’ve got this!"
        print(f"Motivational Message: {message}")
        return message

    def show_help_links(self):
        """Display support resources for when extra help is needed."""
        links = [
            "https://suicidepreventionlifeline.org",
            "https://www.mentalhealth.gov",
            "Call 988 for urgent mental health support"
        ]
        print("Support Resources:")
        for link in links:
            print(link)
        return links

# Conceptual demonstration of app usage
app = CareConnect()
app.log_mood("🙂")
app.write_journal("Felt a bit anxious this morning but better after class.")
app.send_motivational_message()
app.show_help_links()
