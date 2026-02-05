# Simple scribe-student matching logic

student = {
    "name": "Student A",
    "subject": "Computer Science"
}

scribes = [
    {"name": "Scribe 1", "subject": "Computer Science"},
    {"name": "Scribe 2", "subject": "Mathematics"}
]

for scribe in scribes:
    if scribe["subject"] == student["subject"]:
        print("Assigned Scribe:", scribe["name"])
        break
