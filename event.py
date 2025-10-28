class event:
    def __init__(self, event_name, description, event_date, organizer, participants):
        self.event_name = event_name
        self.description = description
        self.event_date = event_date
        self.organizer = organizer
        self.participants = participants  # list of student names
