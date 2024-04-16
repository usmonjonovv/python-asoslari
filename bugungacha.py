import datetime as dt
bugun = dt.date.today()
tkun = dt.date(2009, 1, 13)
farq = bugun - tkun
oy = farq/30
soat = farq*24
print(farq)
print(f"Bugungacha {oy.days} oy yashadim")
print(f"Bugungacha {farq.days} kun yashadim")
print(f"Bugungacha {soat.days} oy yashadim")