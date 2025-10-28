# subscription.py

class Subscription:
    def __init__(self, member_id, amount, date, status):
        self.member_id = member_id
        self.amount = amount
        self.date = date
        self.status = status

    def display_info(self):
        return f"<tr><td>{self.member_id}</td><td>{self.amount}</td><td>{self.date}</td><td>{self.status}</td></tr>"
