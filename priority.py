def apply_priority_aging(queue, aging_interval):
    for job in queue:
        job['waiting_time'] += 1

        if job['waiting_time'] >= aging_interval:
            if job['priority'] > 1:
                job['priority'] -= 1
            job['waiting_time'] = 0

    queue.sort(key=lambda job: (job['priority'], job['waiting_time']))
    return queue
