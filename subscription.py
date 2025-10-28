class subscription:
    def __init__(self, student_id, amount, date, status):
        self.student_id = student_id
        self.amount = amount
        self.date = date
        self.status = status  # paid / unpaid
