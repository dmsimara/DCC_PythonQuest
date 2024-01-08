file = open('user_info.txt', 'a')

name = input("Enter your name: ")

file.write(name + '\n')

file.close()