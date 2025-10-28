# -*- coding: utf-8 -*-
# member.py

class Member:
    def __init__(self, full_name, email, phone, address, join_date, skills, interests, subscription_status):
        self.full_name = full_name
        self.email = email
        self.phone = phone
        self.address = address
        self.join_date = join_date
        self.skills = skills  # list of strings
        self.interests = interests  # list of strings
        self.subscription_status = subscription_status

    def display_info(self):
        return f"<tr><td>{self.full_name}</td><td>{self.email}</td><td>{self.phone}</td><td>{self.address}</td>" \
               f"<td>{self.join_date}</td><td>{', '.join(self.skills)}</td><td>{', '.join(self.interests)}</td>" \
               f"<td>{self.subscription_status}</td></tr>"
