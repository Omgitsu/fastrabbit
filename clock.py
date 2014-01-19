from rq import Queue
from worker import conn
from fastrabbit import fetch_tasks
from apscheduler.scheduler import Scheduler

sched = Scheduler()
q = Queue(connection=conn)

@sched.interval_schedule(seconds=30)
def fast_job():
    print 'This job is run every thirty seconds.'
    result = q.enqueue(fetch_tasks)

sched.start()

while True:
    pass






