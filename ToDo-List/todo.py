import json
class Task:
    def __init__(self, title, description, category):
        self.title = title
        self.description = description
        self.category = category
        self.completed = False
    def mark_completed(self):
        self.completed = True
    def to_dict(self):
        return {
            'title': self.title,
            'description': self.description,
            'category': self.category,
            'completed': self.completed 
        }
    @classmethod
    def from_dict(cls, data):
        task = cls(data['title'], data['description'], data['category'])
        task.completed = data.get('completed', False)
        return task
class TaskManager:
    def __init__(self, filename='tasks.json'):
        self.filename = filename
        self.tasks = self.load_tasks()
    def save_tasks(self):
        with open(self.filename, 'w') as file:
            json.dump([task.to_dict() for task in self.tasks], file, indent=4)
    def load_tasks(self):
        try:
            with open(self.filename, 'r') as file:
                return [Task.from_dict(data) for data in json.load(file)]
        except FileNotFoundError:
            return []
    def add_task(self, title, description, category):
        self.tasks.append(Task(title, description, category))
    def view_tasks(self):
        return self.tasks
    def mark_task_completed(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].mark_completed()
    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks.pop(index)
    
def display_tasks(tasks):
    if not tasks:
        print("No tasks available.")
        return
    print("\nYour Tasks:")
    for i, task in enumerate(tasks):
        status = "Completed" if task.completed else "Pending"
        print(f"{i + 1}. {task.title} ({task.category}) - {status}")
        print(f"   Description: {task.description}")
def main():
    task_manager = TaskManager()
    while True:
        print("\nPersonal To-Do List")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. Exit")
         
        choice = input("Choose an option: ")
        if choice == '1':
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            category = input("Enter task category (e.g., Work, Personal, Urgent): ")
            task_manager.add_task(title, description, category)
            print("Task added successfully!")
        elif choice == '2':
            display_tasks(task_manager.view_tasks())
        elif choice == '3':
            task_num = int(input("Enter the task number to mark as completed: ")) - 1
            task_manager.mark_task_completed(task_num)
            print("Task marked as completed!")
        elif choice == '4':
            task_num = int(input("Enter the task number to delete: ")) - 1
            task_manager.delete_task(task_num)
            print("Task deleted successfully!")
        
        elif choice == '5':
            task_manager.save_tasks()
            print("Tasks saved. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == '__main__':
    main()

