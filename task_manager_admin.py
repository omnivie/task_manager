# Reading user.txt, reading lines and splitting by comma
with open('user.txt', 'r', encoding='utf-8') as users:
    user_data = users.read()
    user_list = user_data.replace('\n', ",").split(',')

# creating separate lists of usernames and passwords
    users = []
    passes = []
    for i in range(0, len(user_list)):
        if i % 2:
            passes.append(user_list[i])
        else:
            users.append(user_list[i])

# using comprehension strip of spaces
users_clean = [x.strip(' ') for x in users]
passes_clean = [x.strip(' ') for x in passes]

# Creating a dictionary from usernames and passwords
users_dict = {}

for key in users_clean:
    for value in passes_clean:
        users_dict[key] = value
        passes_clean.remove(value)
        break

# Authenticating a user using while loop
while True:
    username = input("Please enter your username: ")
    if username in users_clean:
        break
    else:
        print("You have entered a wrong username, please try again.")

while True:
    password = input("Please enter your password: ")
    if password == users_dict[username]:
        break
    else:
        print("You have entered a wrong password, please try again")

# Bringing menu of options available for admin only
if username == "admin":
    while True:
        menu = input('''Select one of the following Options below:
        r - Registering a user
        a - Adding a task
        va - View all tasks
        vm - View my tasks
        s  - View statistics
        e - Exit
        : ''').lower()

# Taking data from user and  writing data to the file. Using while True loop to confirm the password
        if menu == 'r':
            new_user = input("Please enter a username for a new user: ")
            new_user_pass = input("Please enter a password for a new user: ")
            while True:
                pass_confirm = input("Please confirm the password: ")
                if new_user_pass == pass_confirm:
                    with open('user.txt', 'a', encoding='utf-8') as users:
                        users.write(f" \n {new_user}, {new_user_pass}")
                        break
                else:
                    print("Tha passwords don't match, please try again")

# Taking data from a user and adding a task using write method
        elif menu == 'a':
            pass
            new_user = input("Who is this task for (username): ")
            task_title = input("What is the task title: ")
            task_descrip = input("What is the task description? ")
            due_date = (input("What is the task due date: "))
            from datetime import date

            current = date.today()
            current_d = current.strftime("%d %B %y")
            with open('tasks.txt', 'a', encoding='utf-8') as tasks:
                tasks.write(f" \n {new_user}, {task_title}, {task_descrip}, {due_date}, {current_d}, No ")

# Reading tasks.txt, splitting in lines and then words into list using nested for loop
# and printing formatted result of all tasks
        elif menu == 'va':
            with open('tasks.txt', 'r', encoding='utf-8') as tasks:
                for line in tasks:
                    task_list = tasks.readlines()
                    for i in task_list:
                        items = i.split(',')
                        print(f'''
    User - {items[0]}     Task - {items[1]}
    Task Description - {items[2]}
    Date Assigned: {items[3]}
    Date Due: {items[4]}
    Completed: {items[5]} 
    ''')
                    print('')

# Using for loop to read the lines and printing the list where username of registered user is present
        elif menu == 'vm':
            with open('tasks.txt', 'r', encoding='utf-8') as tasks:
                for line in tasks:
                    items = line.split(', ')
                    if username in line:
                        printout = "=====================================\n"
                        printout += "\n"
                        printout += f'User -\t\t\t{items[0]}\n'
                        printout += f'Task -\t\t\t{items[1]}\n'
                        printout += f'Task Description -\t{items[2]}\n'
                        printout += f'Date Assigned -\t\t{items[3]}\n'
                        printout += f'Date Due -\t\t{items[4]}\n'
                        printout += f'Completed -\t\t{items[5]}\n'
                        printout += "\n"
                        printout += "=====================================\n"
                        print(printout)

# Reading and counting lines in files in order to print statistics for the admin
        elif menu == 's':
            with open("user.txt", "r", encoding='utf-8') as users:
                nu = len(users.readlines())
                print(f"There are total of {nu} users in the system.")
            with open("tasks.txt", "r", encoding='utf-8') as tasks:
                nt = len(tasks.readlines())
                print(f"There are total of {nt} tasks in the system.")
            print("")

        elif menu == 'e':
            print('Goodbye!!!')
            exit()
        else:
            print("You have made a wrong choice, Please Try again")

# Bringing menu for users without admin rights
else:
    while True:
        menu = input('''Select one of the following Options below:
        a - Adding a task
        va - View all tasks
        vm - View my tasks
        e - Exit
        : ''').lower()

# Taking data from a user and adding a task to tasks.txt using write method
        if menu == 'a':
            pass
            new_user = input("Who is this task for (username): ")
            task_title = input("What is the task title: ")
            task_descrip = input("What is the task description? ")
            due_date = (input("What is the task due date: "))
            from datetime import date
            current = date.today()
            current_d = current.strftime("%d %B %y")
            with open('tasks.txt', 'a', encoding='utf-8') as tasks:
                tasks.write(f" \n {new_user}, {task_title}, {task_descrip}, {due_date}, {current_d}, No ")

# Reading tasks.txt, splitting in lines and then words into list using nested for loop
# and printing formatted result of all tasks
        elif menu == 'va':
            with open('tasks.txt', 'r', encoding='utf-8') as tasks:
                for line in tasks:
                    task_list = tasks.readlines()
                    for i in task_list:
                        items = i.split(',')
                        print(f'''
    User - {items[0]}     Task - {items[1]}
    Task Description - {items[2]}
    Date Assigned: {items[3]}
    Date Due: {items[4]}
    Completed: {items[5]} 
    ''')
                    print('')

# Using for loop to read the lines and printing the list where username of registered user is present
        elif menu == 'vm':
            with open('tasks.txt', 'r', encoding='utf-8') as tasks:
                for line in tasks:
                    items = line.split(', ')
                    if username in line:
                        printout = "====================================\n"
                        printout += "\n"
                        printout += f'User -\t\t\t{items[0]}\n'
                        printout += f'Task -\t\t\t{items[1]}\n'
                        printout += f'Task Description -\t{items[2]}\n'
                        printout += f'Date Assigned -\t\t{items[3]}\n'
                        printout += f'Date Due -\t\t{items[4]}\n'
                        printout += f'Completed -\t\t{items[5]}\n'
                        printout += "\n"
                        printout += "=====================================\n"
                        print(printout)

        elif menu == 'e':
            print('Goodbye!!!')
            exit()
        else:
            print("You have made a wrong choice, Please Try again")