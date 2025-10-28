# event.py

class Event:
    def __init__(self, event_name, description, event_date, organizer):
        self.event_name = event_name
        self.description = description
        self.event_date = event_date
        self.organizer = organizer
        self.participants = []

    def add_participant(self, member):
        self.participants.append(member)

    def display_info(self):
        participants_list = ", ".join([m.full_name for m in self.participants])
        return f"<tr><td>{self.event_name}</td><td>{self.description}</td><td>{self.event_date}</td>" \
               f"<td>{self.organizer}</td><td>{participants_list}</td></tr>"
