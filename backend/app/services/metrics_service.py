import time
import psutil
import os


class MetricsTracker:
    def __init__(self):
        self.start_time = None

    def start(self):
        self.start_time = time.time()

    def end(self):
        return time.time() - self.start_time


def get_memory_usage_mb():
    process = psutil.Process(os.getpid())
    return round(process.memory_info().rss / 1024 / 1024, 2)
