import requests
from prettytable import PrettyTable

todos_URL = "https://jsonplaceholder.typicode.com/todos"
users_URL = "https://jsonplaceholder.typicode.com/users"

def get_users():
    users_json = requests.get(users_URL).json()
    return {user['id']: user['username'] for user in users_json}

def get_per_user_todos():
    todos = {}
    todos_json = requests.get(todos_URL).json()
    for todo in todos_json:
        try:
            todos[todo['userId']].append((todo['title'], todo['completed']))
        except:
            todos.update({todo['userId']: [(todo['title'], todo['completed'])]})
    return todos

def print_users_todos(users):
    per_users_todos = get_per_user_todos()
    for id,username in users.items():
        user_table = PrettyTable()
        
        try:
            user_table.field_names = [username, "TODO"]
            user_table.add_rows([[todo[0], f"{'✓' if todo[1] else 'X'}"] for todo in per_users_todos[id]])

            print(user_table)
        except:
            continue

users = get_users()
print_users_todos(users)