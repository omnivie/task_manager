# Importing datetime for calculation with dates below in the code
from _datetime import datetime


# Defining a function to register new users
def register():
    new_user = input("Please enter a username for a new user: ")
    new_user_pass = input("Please enter a password for a new user: ")
    while True:
        pass_confirm = input("Please confirm the password: ")
        if new_user_pass == pass_confirm:
            with open('user.txt', 'a', encoding='utf-8') as users:
                users.write(f"\n{new_user}, {new_user_pass}")
                break
        else:
            print("Tha passwords don't match, please try again")


# Defining a function for adding new task
def add_task():
    while True:
        new_user = input("Who is this task for (username): ")
        if new_user not in users_clean:
            print("That username is not available. Please choose another one.")
        else:
            break
    task_title = input("What is the task title: ")
    task_descrip = input("What is the task description? ")
    due_date = (input("What is the task due date: "))
    from datetime import date
    current = date.today()
    current_d = current.strftime("%d %B %Y")
    with open('tasks.txt', 'a', encoding='utf-8') as tasks:
        tasks.write(f"\n{new_user}, {task_title}, {task_descrip}, {due_date}, {current_d}, No ")


# Defining a function for displaying all the tasks
def view_all():
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


# Defining a function to view and edit user's tasks
def view_mine():
# Using for loop to print out all the task with a number next to it
    user_tasks = []
    j = -1
    with open('tasks.txt', 'r', encoding='utf-8') as tasks:
        for line in tasks:
            items = line.split(', ')
            if username in line:
                j += 1
                user_tasks.append(line)
                printout = "=====================================\n"
                printout += "\n"
                printout += f'Task No {j}     '
                printout += f'User -\t\t\t{items[0]}\n'
                printout += f'Task -\t\t\t{items[1]}\n'
                printout += f'Task Description -\t{items[2]}\n'
                printout += f'Date Assigned -\t\t{items[3]}\n'
                printout += f'Date Due -\t\t{items[4]}\n'
                printout += f'Completed -\t\t{items[5]}\n'
                printout += "\n"
                printout += "=====================================\n"
                print(printout)


# Bringing a menu to allow a user to edit a specific task. Using for loop and splitting and joining back
# to make appropriate changes by user and write it back to the file.
    which_task = int(input("Which task you would like to update? "))
    while True:
        chosen_task = user_tasks[which_task]
        options_choice = int(input('''
1. Mark  task as complete
2. Edit task 
-1. Exit to menu
:  '''))
        if options_choice == 1:
            with open('tasks.txt', 'r') as alltasks:
                the_tasks = alltasks.readlines()
            for index, value in enumerate(the_tasks):
                if chosen_task in value:
                    items = chosen_task.split(', ')
                    items[-1] = 'Yes'
                    details_text = ', '.join(items)
                    the_tasks[index] = details_text
            with open('tasks.txt', 'w+') as updated_tasks:
                updated_tasks.write('\n'.join(str(line.strip('\n')) for line in the_tasks))
            print("\nThe task has been updated.")

        elif options_choice == 2:
            while True:
                actions = int(input('''
Please choose an action below:

1. To allocate the task to a different person
2. To update a due date for this task
-1. Exit
: '''))
                if actions == 1:
                    new_user = input("Please enter a username of a new person for this task: ")
                    with open('tasks.txt', 'r') as alltasks:
                        the_tasks = alltasks.readlines()
                    for index, value in enumerate(the_tasks):
                        if chosen_task in value:
                            items = chosen_task.split(', ')
                            items[0] = new_user
                            details_text = ', '.join(items)
                            the_tasks[index] = details_text
                    with open('tasks.txt', 'w+') as updated_tasks:
                        updated_tasks.write('\n'.join(str(line.strip('\n')) for line in the_tasks))
                    print("\nThe task has been updated.")

                elif actions == 2:
                    new_due_date = input("Please enter a new due date for this task(dd MMM yyyy): ")
                    with open('tasks.txt', 'r') as alltasks:
                        the_tasks = alltasks.readlines()
                    for index, value in enumerate(the_tasks):
                        if chosen_task in value:
                            items = chosen_task.split(', ')
                            items[-2] = new_due_date
                            details_text = ', '.join(items)
                            the_tasks[index] = details_text
                    with open('tasks.txt', 'w+') as updated_tasks:
                        updated_tasks.write('\n'.join(str(line.strip('\n')) for line in the_tasks))
                    print("\nThe task has been updated.")

                elif actions == -1:
                    break

                else:
                    print("You have made a wrong choice, Please Try again")

        elif options_choice == -1:
            break

        else:
            print("You have made a wrong choice, Please Try again")


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
gr - Generate reports
ds  - Display statistics
e - Exit
: ''').lower()

# Using functions defined above to perform menu options below
        if menu == 'r':
            register()

        elif menu == 'a':
            add_task()

        elif menu == 'va':
            view_all()

        elif menu == 'vm':
            view_mine()

# Executing generate report option using dictionary and using counters to add keys and values to that dictionary.
        elif menu == 'gr':
            total_tasks = {}
            total_tasks['counter'] = 0
            total_tasks['completed'] = 0
            total_tasks['overdue'] = 0
            from datetime import date
            current = date.today()
            current_d = current.strftime("%d %B %Y")

            with open('tasks.txt', 'r', encoding='utf-8') as tasks:
                task_list = tasks.readlines()
                for line in task_list:
                    current_tasks = line.split(", ")
                    total_tasks['counter'] += 1
                    if current_tasks[-1].strip('\n') == "Yes":
                        total_tasks['completed'] += 1
                    due_date = current_tasks[-2]
                    if due_date < current_d:
                        total_tasks['overdue'] += 1

# Using results from the dictionary and previous code to calculate required percentages
            uncompl_tasks = len(task_list) - total_tasks['completed']
            pct_uncompl = (uncompl_tasks/len(task_list))*100
            pct_over = (total_tasks['overdue']/len(task_list))*100

# Creating a task_overview.txt file and wrting int task related information determined above
            with open('task_overview.txt', 'a+') as abc:
                abc.write(f"\nTotal number of tasks is {total_tasks['counter']}")
                abc.write(f"\nTotal number of completed tasks is {total_tasks['completed']}")
                abc.write(f"\nTotal number of uncompleted tasks is {uncompl_tasks}")
                abc.write(f"\nTotal number of overdue tasks is {total_tasks['overdue']}")
                abc.write(f"\nUncompleted tasks are {pct_uncompl}% of total tasks")
                abc.write(f"\nOverdue tasks are {pct_over}% of total tasks")

# Creating user_overview.txt and adding initial user and task data
            with open('user_overview.txt', 'a+') as xyz:
                xyz.write(f'\nTotal number of users is {len(users)}')
                xyz.write(f'\nTotal number of tasks in the system is {len(task_list)}')

# Using for loop and if statements and list split method to assign new values as per user input
# and writing to the file

            with open('user_overview.txt', 'a+') as overview:
                for user in users:
                    user_completed = 0
                    user_overdue = 0
                    user_incomplete = 0
                    user_count = 0
                    for task in task_list:
                        if user in task:
                            user_count += 1
                            details = task.split(', ')
                            if details[-1] == 'Yes':
                                user_completed += 1
                            else:
                                user_incomplete += 1

                            date_check = details[-2].strip()
                            date_check = datetime.strptime(date_check, '%d %b %Y')
                            current_date = datetime.today()
                            if (current_date > date_check) and (details == 'No'):
                                user_overdue += 1

                    with open('user_overview.txt', 'a+') as mnu:
                        total_user_tasks = user_count
                        mnu.write(f'\nTotal number of tasks for {user} is {total_user_tasks}')

                        percent_of_total = (total_user_tasks/len(task_list))*100
                        mnu.write(f'\nTasks for {user} represent {percent_of_total}% of the tasks in the system')

                        if user_count == 0:
                            percent_complete = 0
                        else:
                            percent_complete = (user_completed/user_count)*100
                            mnu.write(f'\nThe user {user} has completed {percent_complete}% of his/her tasks')

                            percent_still_completed = (user_incomplete/user_count)*100
                            mnu.write(f'\nThe user {user} has  {percent_still_completed}% of his/her '
                                      f'tasks still to be completed')

                            percent_overdue = (user_overdue/user_count)*100
                            mnu.write(f'\nPercentage of overdue tasks for {user} is {percent_overdue}% ')

# Displaying results of report contained in the files using for loop and readlines method
        elif menu == 'ds':
            with open('task_overview.txt', 'r') as to:
                top = to.readlines()
                print("\nBelow is an overview of the tasks:\n")
                for lines in top:
                    print(lines)

            with open('user_overview.txt', 'r') as uo:
                uop = uo.readlines()
                print("\nBelow is an overview of the users:\n")
                for lines in uop:
                    print(lines)

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

# Using functions defined above to perform options selected by the user
        if menu == 'a':
            add_task()

        elif menu == 'va':
            view_all()

        elif menu == 'vm':
            view_mine()

        elif menu == 'e':
            print('Goodbye!!!')
            exit()

        else:
            print("You have made a wrong choice, Please Try again")