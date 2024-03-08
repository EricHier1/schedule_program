class DailySchedule:
    def __init__(self):
        self.schedule = []

    def add_task(self, task_name, start_time, end_time, priority):
        self.schedule.append({
            "task_name": task_name,
            "start_time": start_time,
            "end_time": end_time,
            "priority": priority
        })

    def get_sorted_schedule(self):
        return sorted(self.schedule, key=lambda x: x['priority'])
