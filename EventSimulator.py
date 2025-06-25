# Event Simulation & Time Management Module

class EventSimulator:
    def __init__(self, queue, aging_interval, expiry_time, priority_handler, expiry_handler, visualizer):
        """
        queue: reference to the core queue data structure
        aging_interval: int, time interval after which priority should be increased
        expiry_time: int, max allowed waiting time before a job expires
        priority_handler: function/module to handle priority aging
        expiry_handler: function/module to remove expired jobs
        visualizer: function/module to display the current state
        """
        self.queue = queue
        self.aging_interval = aging_interval
        self.expiry_time = expiry_time
        self.priority_handler = priority_handler
        self.expiry_handler = expiry_handler
        self.visualizer = visualizer
        self.current_time = 0  # system time

    def tick(self):
        """Simulates the passage of 1 time unit."""
        print(f"\n--- Tick {self.current_time + 1} ---")
        self.current_time += 1

        self.update_waiting_times()
        self.apply_priority_aging()
        self.handle_expiry()
        self.visualizer.display(self.queue, self.current_time)

    def update_waiting_times(self):
        """Increases waiting time of each job."""
        for job in self.queue.jobs:
            job.waiting_time += 1

    def apply_priority_aging(self):
        """Calls priority handler for jobs that meet aging threshold."""
        for job in self.queue.jobs:
            if job.waiting_time > 0 and job.waiting_time % self.aging_interval == 0:
                self.priority_handler.age_job(job)

    def handle_expiry(self):
        """Remove jobs that exceed expiry time."""
        expired_jobs = [job for job in self.queue.jobs if job.waiting_time >= self.expiry_time]
        for job in expired_jobs:
            self.expiry_handler.expire_job(job)
            self.queue.remove(job)  # Actual removal

    def run_simulation(self, ticks=10):
        """Run multiple ticks."""
        for _ in range(ticks):
            self.tick()
