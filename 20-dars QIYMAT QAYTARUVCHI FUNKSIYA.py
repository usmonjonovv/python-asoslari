#1,2-mashq
def new_students(name, fname,age,level,city,email = "",number = None):
    """Information about new studenets"""
    student = {
        "name" : name,
        "fname" : fname,
        "age" : age,
        "level" : level,
        "city" : city,
        "email" : email,
        "number" : number
        }
    return student

print("Enter data about new student.")
students = []
while True:
    name = input("Name: ")
    fname = input("Family name: ")
    age = input("Age: ")
    level = input("Level: ")
    city = input("Living city: ")
    email = input("Email: ")
    number = input("Number: ")
    students.append(new_students(name, fname, age, level, city))
    question = input("Is there any other new students? yes/no: ")
    if question != "yes":
        break
print("New students:")
for s in students:
    print(
        f"Name:{s['name'].title()} {s['fname'].title()} \nAge:{s['age']} \nLevel:{s['level'].upper()} \nLiving city:{s['city'].title()} \nContact info:{s['email']},{s['number']}"
        )
#3-mashq
def highest(x,y,z):
    """Show the highest number among 3"""
    x = max()
    if y>=max():
        y = max()
    if z>=max(x, y, z):
        z=max()
print("Enter 3 numbers:")
while True:
    x = input("1-number: ")
    y = input("2-number: ")
    z = input("3-number: ")
    number = input("Do you want to add new number? (yes/no): ")
    if number != 'yes':
        break
print(f"Highest number among them is:{max(x, y, z)}")
#4-mashq
def circle_info(radius, p=3.14159):
    circle = {
        "radius": radius,
        "diametr": 2 * radius,
        "perimetr": 2 * radius * p,
        "yuza": p * radius ** 2,
    }
    return circle
#5-mashq
def tub_sonlar_top(min, max):
    tub_sonlar = []
    for n in range(min, max + 1):
        tub = True
        if n == 1:
            tub = False
        elif n == 2:
            tub = True
        else:
            for x in range(2, n):
                if n % x == 0:
                    tub = False
        if tub:
            tub_sonlar.append(n)

    return tub_sonlar
#6-mashq
def fibonacci(n):
    sonlar = []
    for x in range(n):
        if x == 0 or x == 1:
            sonlar.append(1)
        else:
            sonlar.append(sonlar[x - 1] + sonlar[x - 2])
    return sonlar


print(fibonacci(10))