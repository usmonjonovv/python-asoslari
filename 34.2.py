import json
with open("students.json") as f:
    data = json.load(f)

for item in data["student"]:
    print(f"{item['name']} {item['lastname']}." f" Faculty of {item['faculty']} ")