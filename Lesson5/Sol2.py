
n = 0
while n <= 10:
    try:
        n = int(input("Insert a number bigger than 10: "))
        if n <= 10:
            raise ValueError()
    except ValueError as e:
        print("Please insert a valid value!")

print(f"You have inserted {n}")