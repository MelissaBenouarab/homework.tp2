from member import member

class teacher(member):
    def __init__(self, teacher_id, full_name, email, phone, address, join_date, skills, interests):
        super().__init__(full_name, email, phone, address, join_date, skills, interests)
        self.teacher_id = teacher_id
