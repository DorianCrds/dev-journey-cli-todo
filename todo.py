from json_operations import init_json_file, save_task_into_json
from options_controller import show_menu, show_tasks_list, mark_task_done, delete_task

init_json_file()
run = True
print("Welcome to your command-line ToDoList Application !")
while run:
    choice = show_menu()
    if choice == 1:
        save_task_into_json(input("Enter the new task title >> ").strip())
    elif choice == 2:
        show_tasks_list()
    elif choice == 3:
        mark_task_done()
    elif choice == 4:
        delete_task()
    elif choice == 5:
        run = False
        print("Exitting the CLI ToDoList Application.")
        print("See you soon !")
