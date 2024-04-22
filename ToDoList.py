class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({"task": task, "completed": False})

    def complete_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index]["completed"] = True
        else:
            print("Invalid task number.")

    def display_tasks(self):
        for index, task in enumerate(self.tasks):
            status = "Done" if task["completed"] else "Pending"
            print(f"{index + 1}: {task['task']} [{status}]")

def main():
    todo_list = ToDoList()
    while True:
        print("\nTo-Do List")
        print("1. Add Task")
        print("2. Complete Task")
        print("3. Show Tasks")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            task = input("Enter a task: ")
            todo_list.add_task(task)
        elif choice == "2":
            index = int(input("Enter task number to mark as completed: ")) - 1
            todo_list.complete_task(index)
        elif choice == "3":
            todo_list.display_tasks()
        elif choice == "4":
            break
        else:
            print("Invalid option. Please choose a valid number.")

if __name__ == "__main__":
    main()
