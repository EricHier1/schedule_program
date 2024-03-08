from schedule_model import DailySchedule
from schedule_view import ScheduleView

class ScheduleController:
    def __init__(self):
        self.model = DailySchedule()
        self.view = ScheduleView()

    def add_task_from_input(self):
        task_name, start_time, end_time, priority = self.view.get_task_details()
        self.model.add_task(task_name, start_time, end_time, priority)

    def display_schedule(self):
        schedule = self.model.get_sorted_schedule()
        self.view.display_schedule(schedule)
