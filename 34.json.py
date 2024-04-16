import json
data = {"Model" : "Malibu", "Rang" : "Qora", "Yil":2020, "Narh":40000}
data_json = json.dumps(data)
print(data_json)
print(type(data_json))
with open('data.json','w') as d:
    json.dump(data,d)


talaba_json = """{"ism":"Hasan","familiya":"Husanov","tyil":2000}"""
talaba = json.loads(talaba_json)
talaba = dict(talaba)
print(type(talaba))
ism = talaba["ism"]
familiya = talaba["familiya"]
print(f"{ism} {familiya}")
with open('talaba.json','w') as tj:
    json.dump(talaba,tj)
#talaba_json1 = json.dumps(talaba_json) == talaba_json = """{"ism":"Hasan","familiya":"Husanov","tyil":2000}"""