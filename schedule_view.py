class ScheduleView:
    @staticmethod
    def display_schedule(schedule):
        print("Your Daily Schedule:")
        for task in schedule:
            print(f"{task['start_time']} - {task['end_time']} | Priority {task['priority']} | Task: {task['task_name']}")

    @staticmethod
    def get_task_details():
        task_name = input("Task Name: ")
        start_time = input("Start Time (HH:MM): ")
        end_time = input("End Time (HH:MM): ")
        priority = int(input("Priority (1-5, 1 being highest): "))
        return task_name, start_time, end_time, priority

    @staticmethod
    def display_message(message):
        print(message)
