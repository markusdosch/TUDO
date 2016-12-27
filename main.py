import datetime
import sys

from pytz import timezone

from task import Task

tz_germany = timezone("Europe/Berlin")
tasks = []


def main(argv=sys.argv):
    print(str(argv))
    if len(argv) == 1:
        # TODO print help
        return 1
    if argv[1] == "add":
        add(argv[1:])
    if argv[1] == "list":
        list_tasks()
    return 0


# Adds Tasks to the list of tasks
def add(*descriptions):
    # TODO Behaviour for no Tasks to add
    global tasks
    for description in descriptions:
        tasks.append(Task(description, datetime.now(tz_germany)))
    return


# Returns the full list of tasks
def list_tasks():
    return tasks


def init():
    global tasks
    tasks = []


if __name__ == "__main__":
    SystemExit(main())
