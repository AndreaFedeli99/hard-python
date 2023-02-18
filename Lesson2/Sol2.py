
def insert_users():
    user_to_insert = int(input("Insert the number of users to insert: "))
    users = []
    for i in range(1, user_to_insert + 1):
        nickname = input(f"Insert the {i}° user's nickname: ")
        age = int(input(f"Insert the {i}° user's age: "))
        gender = input(f"Insert the {i}° user's gender (M/F): ")

        for usr in users:
            if nickname == usr['nickname']:
                raise ValueError("User already inserted!")
        users.append({'nickname': nickname, 'age': age, 'gender': gender})
        print(f"{i}° user inserted!")
    return users

def get_number_of_male_users(users):
    male_count = 0
    for usr in users:
        if usr['gender'] == 'M':
            male_count += 1
    return male_count

def get_number_of_female_users(users):
    female_count = 0
    for usr in users:
        if usr['gender'] == 'F':
            female_count += 1
    return female_count

def get_max_age(users):
    max_age = users[0]['age']
    for usr in users[1:]:
        if usr['age'] > max_age:
            max_age = usr['age']
    return max_age

def get_avg_age(users):
    age_sum = 0
    for usr in users:
        age_sum += usr['age']
    return age_sum / len(users)

def get_min_age(users):
    min_age = users[0]['age']
    for usr in users[1:]:
        if usr['age'] < min_age:
            min_age = usr['age']
    return min_age

def get_avg_nickname_length(users):
    tot_nick_length = 0
    for usr in users:
        tot_nick_length += len(usr['nickname'])
    return tot_nick_length / len(users)

print("**********Welcome to Casino**********")
try:
    users = insert_users()
    print(f"The number of male users is {get_number_of_male_users(users)}")
    print(f"The number of female users is {get_number_of_female_users(users)}")
    print(f"The max users' age is {get_max_age(users)}")
    print(f"The average users' age is {get_avg_age(users):.2f}")
    print(f"The minimum users' age is {get_min_age(users)}")
    print(f"The average length of users' nickname is {get_avg_nickname_length(users):.2f}")
except ValueError as exc:
    print(exc)
