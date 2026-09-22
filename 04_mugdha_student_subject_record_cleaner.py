student_data = {
    "id1": {"name": "Sahra", "class": "V", "subject": "english, math, science"},
    "id2": {"name": "David", "class": "V", "subject": "english, math, science"},
    "id3": {"name": "Sahra", "class": "V", "subject": "english, math, science"},
    "id4": {"name": "Surya", "class": "V", "subject": "english, coding, math"},
}

print("Original Student Records:")
print(student_data)

print("Details of id1:")
print(student_data.get("id1", "Not Found"))

print("Details of id5:")
print(student_data.get("id5", "Not Found"))

student_data["id5"] = {
    "name": "Anaya",
    "class": "V",
    "subject": "english, art, science"
}

print("After adding id5:")
print(student_data)
student_data["id2"]["subject"] = "english, math, coding"
print(student_data["id2"])

cleaned_data = {}
seen_records = []

for student_id, details in student_data.items():
    unique_key = (details["name"], details["class"], details["subject"])    
    if unique_key not in seen_records:
        seen_records.append(unique_key)
        cleaned_data[student_id] = details

student_data = cleaned_data

print(student_data)

removed_student = student_data.pop("id4", "Student not found")

print("Removed student:")
print(removed_student)


for student_id, details in student_data.items():
    print(student_id, ":", details)
