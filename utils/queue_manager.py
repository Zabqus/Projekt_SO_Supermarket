from multiprocessing import Queue


class QueueManager:
    def __init__(self, num_queues):
        self.queues = [Queue() for _ in range(num_queues)]
        self.active_queues = [0, 1]

    def get_shortest_queue(self):
        shortest = self.active_queues[0]
        min_length = self.queues[shortest].qsize()

        for queue_id in self.active_queues:
            current_length = self.queues[queue_id].qsize()
            if current_length < min_length:
                min_length = current_length
                shortest = queue_id

        return shortest