
l1 = [1, 2, 3, 4, 5]
print(f"l1 = {l1}")

l2 = [6, 7, 8, 9, 10]
print(f"l2 = {l2}")

l3 = l1 + l2
print(f"l1 + l2 = {l3}")

def choose_length():
    length = 0
    while length <= 0:
        try:
            length = int(input("Insert how many elements you want to insert in the first list: "))
        except ValueError:
            print("Please insert a number")
    return length

def insert_elements(length):
    count = 0
    l = []
    while count < length:
        l.append(int(input(f"Insert {count + 1}° element: ")))
        count += 1
    return l

n_elem = choose_length()
l1 = insert_elements(n_elem)
print(f"l1 = {l1}")

n_elem = choose_length()
l2 = insert_elements(n_elem)
print(f"l2 = {l2}")

l3 = l1 + l2
print(f"l1 + l2 = {l3}")