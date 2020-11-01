"""
Implement a job scheduler which takes in a function f and an integer n, and calls f after n milliseconds.
"""

import datetime

class JobScheduler:

    def __init__(self):
        pass


    def delay(self, f, n):
        t = datetime.datetime.now()
        task = f
        print(t)
        target_t = t + datetime.timedelta(milliseconds=n)
        while datetime.datetime.now() < target_t:
            pass
        print(datetime.datetime.now())
        task()


def flag():
    thingy = datetime.datetime.now()
    print(f'this is the flag at {thingy}')


#js = JobScheduler()
#js.delay(flag, 45)


import threading
from time import time


class Scheduler:
    def __init__(self):
        self.fns = []

        self.lock = threading.RLock()

        self.condition = threading.Condition(self.lock)

        t = threading.Thread(target=self.poll)
        t.start()

    def poll(self):
        while True:
            now = time() * 1000

            with self.lock:
                to_run = [fn for fn, due in self.fns if due <= now]
                self.fns = [(fn, due) for (fn, due) in self.fns if due > now]

            for fn in to_run:
                fn()

            with self.lock:
                if not self.fns:
                    self.condition.wait()
                else:
                    ms_remaining = min(due for fn, due in self.fns) - time()*1000
                    if ms_remaining > 0:
                        self.condition.wait(ms_remaining / 1000)

    def delay(self, f, n):
        with self.lock:
            self.fns.append((f, time() * 1000 + n))

            self.condition.notify_all()


s = Scheduler()
print(datetime.datetime.now())
s.delay(flag, 45)
print(time())
print(f"hi at {datetime.datetime.now()}")