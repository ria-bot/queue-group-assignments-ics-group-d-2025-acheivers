import threading

def handle_simultaneous_submissions(self, jobs):
    threads = []

    def submit(job):
        self.enqueue_job(job["user_id"], job["job_id"], job["priority"])

    for job in jobs:
        t = threading.Thread(target=submit, args=(job,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()
