class Task:
    def __init__(self, title):
        self.title = title
        self.is_complete = False

    def mark_complete(self):
        self.is_complete = True
        print("Task marked as complete.")


class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        for existing_task in self.tasks:
            if existing_task.title == task.title:
                print("Task already exists in the to-do list.")
                return
        self.tasks.append(task)
        print("Task added successfully.")

    def remove_task(self, title):
        for task in self.tasks:
            if task.title == title:
                self.tasks.remove(task)
                print("Task removed.")
                return
        print("Task not found'.")

    def mark_task_complete(self, title):
        for task in self.tasks:
            if task.title == title:
                task.mark_complete()
                return
        print("Task not found'.")


    def view_tasks(self, choice):
        if choice == 1:
            print("\nAll Tasks:")
            for task in self.tasks:
                status = "Complete" if task.is_complete else "Incomplete"
                print(f"Title: {task.title}, Status: {status}")
        elif choice == 2:
            print("\nCompleted Tasks:")
            for task in self.tasks:
                if task.is_complete:
                    print(f"Title: {task.title}")
        elif choice == 3:
            print("\nIncomplete Tasks:")
            for task in self.tasks:
                if not task.is_complete:
                    print(f"Title: {task.title}")


class User:
    def __init__(self, uname, passwd):
        self.username = uname
        self.password = passwd
        self.todo_list = ToDoList()

    def authenticate(self, passwd):
        return self.password == passwd


class ToDoApp:
    def __init__(self):
        self.users = {}

    def signup(self, uname, passwd):
        if uname not in self.users:
            self.users[uname] = User(uname, passwd)
            print("User signed up successfully.")
        else:
            print("Username already taken. Try something unique.")

    def login(self, uname, passwd):
        user = self.users.get(uname)
        if user and user.authenticate(passwd):
            print(f"Hello, {uname}!")
            return user
        else:
            print("Invalid credentials.")
            return None


def start():
    app = ToDoApp()
    current_user = None

    while not current_user:
        print("\nUser Authentication")
        print("1. Sign Up")
        print("2. Log In")
        choice = input("Do you want to Log In or Sign Up? (Enter 1 or 2): ")

        if choice == "1":
            uname = input("Choose a username: ")
            passwd = input("Choose a password: ")
            app.signup(uname, passwd)
        elif choice == "2":
            uname = input("Enter your username: ")
            passwd = input("Enter your password: ")
            current_user = app.login(uname, passwd)

    while True:
        print("\nTo-Do List")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Mark a Task as Complete")
        print("4. View Tasks")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            title = input("Entertitle: ")
            task = Task(title)
            current_user.todo_list.add_task(task)

        elif choice == "2":
            title = input("Enter title to remove: ")
            current_user.todo_list.remove_task(title)

        elif choice == "3":
            title = input("Enter task title to mark as complete: ")
            current_user.todo_list.mark_task_complete(title)

        elif choice == "4":
            print("\nView Tasks")
            print("1. All Tasks")
            print("2. Completed Tasks")
            print("3. Incomplete Tasks")
            view_choice = input("Choose an option: ")
            if view_choice in ("1", "2", "3"):
                current_user.todo_list.view_tasks(int(view_choice))
            else:
                print("Wrong Option.")

        elif choice == "5":
            print("End of Program")
            break
        else:
            print("Wrong Option")


start()
