
all_ok = False
name, surname = "", ""
age = -1

def name_is_ok(name):
    return len(name) > 1

def surname_is_ok(surname):
    return len(surname) > 1

def age_is_ok(age):
    return age >= 18

while not all_ok:
    name = input("Insert your name: ")
    if not name_is_ok(name):
        print("Inserted name isn't valid, it must be longer than 1 character!")
        continue
    surname = input("Insert your surname: ")
    if not surname_is_ok(surname):
        print("Inserted surname isn't valid, it must be longer than 1 character!")
        continue
    age = int(input("Insert your age: "))
    if not age_is_ok(age):
        print("Inserted age isn't valid, it must be higher than 18!")
        continue
    all_ok = True

print("Login completed!")
print(f"Welcome back {name.capitalize()} {surname.capitalize()} ({age} years old)")