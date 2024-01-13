import json

user_name = input("Enter your name: ")
user_age = input("Enter your age: ")
user_food = input("Enter your favorite food: ")

user_data = {
    "name" : user_name,
    "age" : user_age,
    "favorite_food" : user_food
}

data = json.dumps(user_data, indent = 2)

print(data)

with open('output.json', 'w') as file:
    file.write(data)