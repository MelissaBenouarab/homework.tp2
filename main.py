# -*- coding: utf-8 -*-
import csv
from member import Member

def read_members_from_file(filename):
    members = []
    with open(filename, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f, delimiter='\t')
        for row in reader:
            skills = row["skills"].split(",")
            interests = row["interests"].split(",")
            member = Member(
                full_name=row["full_name"],
                email=row["email"],
                phone=row["phone"],
                address=row["address"],
                join_date=row["join_date"],
                skills=skills,
                interests=interests,
                subscription_status=row["subscription_status"]
            )
            members.append(member)
    return members


def generate_html(members):
    html = """
    <html>
    <head>
        <meta charset="utf-8">
        <title>Liste des Membres - Association Quranic</title>
        <style>
            body { font-family: Arial; background: #f8f8f8; color: #333; }
            h1 { text-align: center; }
            table { width: 90%; margin: auto; border-collapse: collapse; }
            th, td { border: 1px solid #ccc; padding: 8px; text-align: center; }
            th { background: #d8e8d8; }
        </style>
    </head>
    <body>
        <h1>Liste des Membres de l’Association Quranic</h1>
        <table>
            <tr>
                <th>Nom Complet</th><th>Email</th><th>Téléphone</th><th>Adresse</th>
                <th>Date d’adhésion</th><th>Compétences</th><th>Centres d’intérêt</th><th>Statut</th>
            </tr>
    """

    for member in members:
        html += member.display_info()

    html += """
        </table>
    </body>
    </html>
    """

    with open("members.html", "w", encoding="utf-8") as f:
        f.write(html)
    print("✅ Fichier HTML généré : members.html")


# ---------- EXÉCUTION ----------
if __name__ == "__main__":
    members = read_members_from_file("members.tsv")
    generate_html(members)
