import sys

from tabulate import tabulate

import tasks_store

task_db = tasks_store.TasksStore()

def main(argv=sys.argv):
    print(str(argv))
    if len(argv) == 1:
        # TODO print help
        return 1
    if argv[1] == "add":
        add(argv[2:])
    if argv[1] == "list":
        list_tasks()
    if argv[1] == "stats":
        group_tasks_archived()
    return 0


# Adds Tasks to the list of tasks
def add(descriptions):
    # TODO Behaviour for no Tasks to add
    for description in descriptions:
        task_db.add_task(description)
    return


# Returns the full list of tasks
def list_tasks():
    tasks = task_db.list_tasks()
    print(tabulate([[task.number, task.description, task.started.strftime("%Y-%m-%d %H:%M")] for task in tasks],
                   headers=["#", "Description", "Started"]))
    return tasks


# Returns the number of archived tasks grouped by "finished" date
def group_tasks_archived():
    dates_and_nums = task_db.group_tasks_archived()
    print(tabulate(dates_and_nums,
                   headers=["Date", "Tasks finished"]))
    return dates_and_nums


def init():
    return


if __name__ == "__main__":
    SystemExit(main())
