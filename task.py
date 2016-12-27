class Task:
    # TODO import Counter number?
    counter = 0

    # Creates a Task
    def __init__(self, description, started, finished=None):
        Task.counter += 1
        self.number = Task.counter
        self.description = description
        self.started = started
        self.finished = finished

    def is_finished(self):
        return True if not self.finished else False
