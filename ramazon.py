import datetime as dt
bugun = dt.date.today()
ramazon = dt.date(2025, 3, 1)
eid = dt.date(2024, 6, 16)
farq = ramazon-bugun
farq1 = eid - bugun
print(farq1)
print(farq)
print(f"Ramazonga {farq.days} kun qoldi")
print(f"Qurbon Hayitiga {farq1.days} kun qoldi")