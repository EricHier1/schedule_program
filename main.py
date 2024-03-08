from schedule_controller import ScheduleController
from schedule_view import ScheduleView

def main():
    controller = ScheduleController()

    while True:
        ScheduleView.display_message("\nAdd a new task to your daily schedule. Enter 'done' when you are finished.")
        task_name = input("Task Name: ")
        if task_name.lower() == 'done':
            break
        controller.add_task_from_input()
    
    controller.display_schedule()

if __name__ == "__main__":
    main()
