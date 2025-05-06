#PROJECT: Task Manager with Priority

tasks = []

def show_menu():
    print("\n--- Task Manager Menu ---")
    print("1. Add a new Task")
    print("2. View all Tasks")
    print("3. Filter tasks by priority")
    print("4. Mark taks as completed")
    print("5. View tasks by status(Pending/Completed)")
    print("6. Exit")
    
while True:
    show_menu()
    option = input("Choose an option: ")
    if option == '1':
        title = input("Task title: ")
        description = input("Task description (optional): ")
        priority = input ("Priority (High/Medium/Low): ").capitalize()
            
        if priority not in ['High', 'Medium', 'Low']:
            print("Invalid Priority. Defaulting to 'Low'.")
            priority = 'Low'
                
        task = {
            'title' : title, 
            'description' : description,
            'priority' : priority,
            'status' : 'Pending'
        }
            
        tasks.append(task)
        print(f"Task'{title}' added successfully!")
        
    elif option == '2':
        if not tasks:
            print("No tasks found.")
        else:
            print("\n--- All Tasks ---")
            for i, task in enumerate(tasks, start =1):
                print(f"{i}. Title: {task['title']}")
                print(f" Description: {task['description']}")
                print(f" Priority: {task['priority']}")
                print(f" Status: {task['status']}")
                print("-" * 30)
        
    elif option == '3':
        desired_priority = input("Enter the priority to filter (High, Medium, Low):").capitalize()
        filtered_tasks = [task for task in tasks if task['priority'] == desired_priority]
            
        if not filtered_tasks:
            print(f"No tasks found with priority: {desired_priority}")
        else:
            print(f"\n--- Tasks with{desired_priority} Priority ---")
            for i, task in enumerate(filtered_tasks, start=1):
                print(f"{i}. Title: {task['title']}")
                print(f" Description: {task['description']}")
                print(f" Status: {task['status']}")
                print("-" * 30)
                    
    elif option == '4':
        if not task:
            print("No tasks available to update.")
        else:
            print("\n--- Tasks ---")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}.{task['title']} - Status: {task['status']}") 
                      
            try:
                task_number = int(input("Enter the task number to update: "))
                if 1 <= task_number <= len(tasks):
                    new_status = input("Enter the new status(Pending, In Progress, Completed): ").capitalize()
                    tasks[task_number - 1]['status'] = new_status
                    print("Task status updated succesfully!")
                else:
                        print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")
        
    elif option == '5':
        print("\n View tasks by status")
        print("Available statuses: Pending, in Progress, Completed")
        chosen_status = input("Enter the status to filter: ").capitalize()
            
        matching_tasks = [task for task in tasks if task['status'] == chosen_status]
            
        if not matching_tasks:
            print(f"No tasks found with status: {chosen_status}")
        else:
            print(f"\nTasks with status '{chosen_status}': ")
            for i, task in enumerate(matching_tasks, start=1):
                print(f"{i}. Title: {task['title']} - Status: {task['status']}")
        
    elif option == '6':
        print('Exiting the system... 👋')
        print('Thank you for using our Task Manager!')
        break
        
    else:
        print("Invalid option. Please try again.")
        
                    