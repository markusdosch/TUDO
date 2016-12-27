import sys

from tabulate import tabulate

import tasks_store

task_db = tasks_store.TasksStore()

def main(argv=sys.argv):
    if len(argv) == 1:
        # TODO print help
        return 1

    if argv[1] == "add":
        add(argv[2:])
    if argv[1] == "del":
        delete_tasks(argv[2:])
    if argv[1] == "fin":
        finish_tasks(argv[2:])

    if argv[1] == "list":
        if len(argv) > 2 and argv[2] == "all":
            list_tasks(True)
        else:
            list_tasks()
    return 0


def finish_tasks(numbers):
    task_db.set_done(numbers)
    return


def delete_tasks(numbers):
    task_db.delete(numbers)
    return

# Adds Tasks to the list of tasks
def add(descriptions):
    # TODO Behaviour for no Tasks to add
    for description in descriptions:
        task_db.add_task(description)
    return


# Returns the full list of tasks
def list_tasks(show_completed=False):
    tasks = task_db.list_tasks()
    if show_completed:
        print(tabulate([[task.number, task.description, task.started.strftime("%Y-%m-%d %H:%M"),
                         task.finished.strftime("%Y-%m-%d %H:%M") if task.finished else "Not Yet"] for task in tasks],
                       headers=["#", "Description", "Started", "Finished"]))
    else:
        print(tabulate([[task.number, task.description, task.started.strftime("%Y-%m-%d %H:%M")] for task in tasks if
                        not task.is_finished()],
                       headers=["#", "Description", "Started"]))
    return tasks

def init():
    return


if __name__ == "__main__":
    SystemExit(main())
