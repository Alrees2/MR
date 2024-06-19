# MR/core.py

import time
from datetime import datetime, timedelta

class TimedExecutor:
    def __init__(self, timeout, unit='seconds'):
        self.start_time = datetime.now()
        self.timeout = timeout
        self.unit = unit
        self.end_time = self.calculate_end_time()

    def calculate_end_time(self):
        if self.unit == 'seconds':
            return self.start_time + timedelta(seconds=self.timeout)
        elif self.unit == 'minutes':
            return self.start_time + timedelta(minutes=self.timeout)
        elif self.unit == 'hours':
            return self.start_time + timedelta(hours=self.timeout)
        elif self.unit == 'days':
            return self.start_time + timedelta(days=self.timeout)
        else:
            raise ValueError("Invalid time unit")

    def check_time(self):
        current_time = datetime.now()
        if current_time >= self.end_time:
            self.delete_date()
            raise TimeoutError("Code execution time has expired")

    def delete_date(self):
        if self.unit == 'seconds':
            print(f"Deleting data for {self.start_time.second} seconds")
        elif self.unit == 'minutes':
            print(f"Deleting data for {self.start_time.minute} minutes")
        elif self.unit == 'hours':
            print(f"Deleting data for {self.start_time.hour} hours")
        elif self.unit == 'days':
            print(f"Deleting data for {self.start_time.date()}")

def run_with_timeout(timeout, unit='seconds'):
    def decorator(func):
        def wrapper(*args, **kwargs):
            executor = TimedExecutor(timeout, unit)
            result = func(*args, **kwargs)
            executor.check_time()
            return result
        return wrapper
    return decorator
