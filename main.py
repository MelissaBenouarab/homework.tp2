from teacher import teacher
from student import student
from subscription import subscription
from event import event
import webbrowser

# ---------- DATA CREATION ----------

teachers = [
    teacher(1, "Ahmed Ben Ali", "ahmed@example.com", "0550-123456", "Algiers", "2022-01-15", ["Tajwid"], ["Teaching Quran"]),
    teacher(2, "Fatima Bensalem", "fatima@example.com", "0551-987654", "Oran", "2021-03-22", ["Arabic"], ["Quranic Studies"]),
    teacher(3, "Youssef Amrani", "youssef@example.com", "0552-765432", "Constantine", "2023-05-10", ["Tafsir"], ["Islamic Education"]),
    teacher(4, "Sara Khaled", "sara@example.com", "0553-222333", "Blida", "2022-09-01", ["Recitation"], ["Community Work"])
]

groups = {
    "Group 1": {"teacher": teachers[0], "students": []},
    "Group 2": {"teacher": teachers[1], "students": []},
    "Group 3": {"teacher": teachers[2], "students": []},
    "Group 4": {"teacher": teachers[3], "students": []}
}

group_skills_interests = {
    "Group 1": (["Tajwid", "Memorization"], ["Quran Reading", "Recitation"]),
    "Group 2": (["Tafsir", "Recitation"], ["Quran Memorization", "Arabic"]),
    "Group 3": (["Arabic", "Quran Reading"], ["Tafsir", "Memorization"]),
    "Group 4": (["Islamic Studies", "Community Work"], ["Recitation", "Quran Study"])
}

first_names = ["Amir", "Sara", "Youssef", "Leila", "Omar", "Meryem", "Ali", "Nadia", "Hassan", "Fatima"]
last_names = ["Ben Ali", "Bensalem", "Amrani", "Khaled", "Mansouri", "Bouaziz"]

all_subscriptions = []

for i in range(60):
    group_name = f"Group {(i)//15 + 1}"
    skills, interests = group_skills_interests[group_name]
    sub = subscription(i+1, 5000, "2025-01-10", "paid" if i % 2 == 0 else "unpaid")
    full_name = f"{first_names[i % len(first_names)]} {last_names[i % len(last_names)]}"
    s = student(i+1, full_name, f"student{i+1}@example.com", f"0550-{100000+i+1}", "Algeria", "2024-09-10",
                skills, interests, group_name, sub.status)
    groups[group_name]["students"].append(s)
    all_subscriptions.append(sub)

events = [
    event("Quran Recitation Contest", "A competition for best recitation.", "2025-11-15", "Ahmed Ben Ali",
          [s.full_name for s in groups["Group 1"]["students"][:5]]),
    event("Ramadan Charity", "Community charity during Ramadan.", "2025-03-10", "Sara Khaled",
          [s.full_name for s in groups["Group 2"]["students"][:5]])
]

# ---------- HTML GENERATION ----------

def generate_table_students():
    rows = ""
    for group_name, data in groups.items():
        for s in data["students"]:
            rows += f"<tr><td>{s.student_id}</td><td>{s.full_name}</td><td>{s.group}</td><td>{s.subscription_status}</td><td>{s.email}</td><td>{s.phone}</td><td>{', '.join(s.skills)}</td><td>{', '.join(s.interests)}</td></tr>"
    return f"""
    <h2>Students</h2>
    <table>
        <tr><th>Student ID</th><th>Full Name</th><th>Group</th><th>Subscription</th><th>Email</th><th>Phone</th><th>Skills</th><th>Interests</th></tr>
        {rows}
    </table>
    """

def generate_table_subscriptions():
    rows = ""
    for sub in all_subscriptions:
        rows += f"<tr><td>{sub.student_id}</td><td>{sub.amount}</td><td>{sub.date}</td><td>{sub.status}</td></tr>"
    return f"""
    <h2>Subscriptions</h2>
    <table>
        <tr><th>Student ID</th><th>Amount</th><th>Date</th><th>Status</th></tr>
        {rows}
    </table>
    """

def generate_table_teachers():
    rows = ""
    for t in teachers:
        rows += f"<tr><td>{t.teacher_id}</td><td>{t.full_name}</td><td>{t.email}</td><td>{t.phone}</td><td>{t.address}</td><td>{t.join_date}</td><td>{', '.join(t.skills)}</td><td>{', '.join(t.interests)}</td></tr>"
    return f"""
    <h2>Teachers</h2>
    <table>
        <tr><th>Teacher ID</th><th>Full Name</th><th>Email</th><th>Phone</th><th>Address</th><th>Join Date</th><th>Skills</th><th>Interests</th></tr>
        {rows}
    </table>
    """

def generate_table_groups():
    rows = ""
    for name, data in groups.items():
        t = data["teacher"]
        rows += f"<tr><td>{name}</td><td>{t.full_name}</td><td>{', '.join(t.skills)}</td><td>{len(data['students'])} students</td></tr>"
    return f"""
    <h2>Groups</h2>
    <table>
        <tr><th>Group</th><th>Teacher</th><th>Teaching</th><th>Number of Students</th></tr>
        {rows}
    </table>
    """

def generate_table_events():
    rows = ""
    for e in events:
        participants = ", ".join(e.participants)
        rows += f"<tr><td>{e.event_name}</td><td>{e.description}</td><td>{e.event_date}</td><td>{e.organizer}</td><td>{participants}</td></tr>"
    return f"""
    <h2>Events</h2>
    <table>
        <tr><th>Name</th><th>Description</th><th>Date</th><th>Organizer</th><th>Participants</th></tr>
        {rows}
    </table>
    """

# ---------- HTML TEMPLATE ----------
html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Quranic School</title>
<style>
body {{ margin:0; font-family:Poppins,sans-serif; display:flex; flex-direction:column; height:100vh; }}
.sidebar {{ width:100%; background:#c7f0c2; padding:10px; display:flex; flex-wrap:wrap; justify-content:center; }}
.sidebar button {{ padding:10px 15px; margin:5px; border:none; border-radius:8px; cursor:pointer; font-size:16px; background:#a4e1a1; }}
.sidebar button:hover {{ background:#90d48c; }}
.content {{ flex:1; padding:20px; overflow-y:auto; text-align:center; }}
table {{ width:100%; border-collapse: collapse; margin-top:10px; }}
th, td {{ border:1px solid #ccc; padding:8px; }}
th {{ background-color:#d9f8c4; }}
tr:nth-child(even){{ background:#f6fff6; }}
img {{ width:80%; border-radius:20px; margin-top:20px; }}
.bottombar {{ width:100%; background:#f5fff5; padding:20px; border-top:1px solid #d0e8d0; text-align:center; font-size:15px; }}
</style>
</head>
<body>

<div class="sidebar">
<button onclick="showSection('home')">🏠 Home</button>
<button onclick="showSection('students')">👨‍🎓 Students</button>
<button onclick="showSection('teachers')">👩‍🏫 Teachers</button>
<button onclick="showSection('groups')">📚 Groups</button>
<button onclick="showSection('events')">🕌 Events</button>
<button onclick="showSection('subscriptions')">💳 Subscriptions</button>
</div>

<div class="content" id="content">
<div id="home">
<h2>Welcome to Quranic School</h2>
<p>“And We have certainly made the Quran easy for remembrance, so is there any who will remember?” (Al-Qamar 54:17)</p>
<img src="img/pic.jpg" alt="Quranic Image">
<div class="bottombar">
<h3>📅 Opening Hours</h3>
<p>Sunday to Thursday | 8:00 AM - 4:00 PM</p>
<h3>📞 Contact</h3>
<p>Email: contact@quranicschool.com | Phone: 0550-000000</p>
</div>
</div>
<div id="students" style="display:none;">{generate_table_students()}</div>
<div id="teachers" style="display:none;">{generate_table_teachers()}</div>
<div id="groups" style="display:none;">{generate_table_groups()}</div>
<div id="events" style="display:none;">{generate_table_events()}</div>
<div id="subscriptions" style="display:none;">{generate_table_subscriptions()}</div>
</div>

<script>
function showSection(id){{
    const sections = ['home','students','teachers','groups','events','subscriptions'];
    sections.forEach(s => document.getElementById(s).style.display = 'none');
    document.getElementById(id).style.display = 'block';
}}
</script>

</body>
</html>"""

with open("quranic_school.html", "w", encoding="utf-8") as f:
    f.write(html_content)

webbrowser.open("quranic_school.html")
print("✅ Quranic School interactive page generated successfully!")
