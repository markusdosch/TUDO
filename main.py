import sys

from tabulate import tabulate
from itertools import repeat, zip_longest

import tasks_store

task_db = tasks_store.TasksStore()

def main(argv=sys.argv):
    if len(argv) == 1:
        # TODO print help
        return 1

    if argv[1] == "addp":
        add_prioritised(argv[2:])
    if argv[1] == "listp":
        if len(argv) > 2 and argv[2] == "val":
            list_priorities(int(argv[3]), int(argv[4]))
        else:
            list_priorities()
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
    if argv[1] == "stats":
        group_tasks_archived()
    if argv[1] == "eisenhower":
        eisenhower_matrix()
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


def add_prioritised(args):
    for i in range(0, len(args) // 3):
        task_db.add_task_p([args[i * 3], args[i * 3 + 1], args[i * 3 + 2]])


def list_priorities():
    tasks = task_db.list_tasks()
    print(tabulate([[task.number, task.description, task.started.strftime("%Y-%m-%d %H:%M"),
                     task.finished.strftime("%Y-%m-%d %H:%M") if task.finished else "Not Yet", task.important,
                     task.urgent] for task in tasks],
                   headers=["#", "Description", "Started", "Finished", "important", "urgent"]))


def list_priorities(important, urgent):
    tasks = task_db.list_tasks_p(important, urgent)
    print(tabulate([[task.number, task.description, task.started.strftime("%Y-%m-%d %H:%M"),
                     task.finished.strftime("%Y-%m-%d %H:%M") if task.finished else "Not Yet", task.important,
                     task.urgent] for task in tasks],
                   headers=["#", "Description", "Started", "Finished", "important", "urgent"]))

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


# Returns the number of archived tasks grouped by "finished" date
def group_tasks_archived():
    dates_and_nums = task_db.group_tasks_archived()
    print(tabulate(dates_and_nums,
                   headers=["Date", "Tasks finished"]))
    return dates_and_nums

def eisenhower_matrix():
    col0 = col1 = col2 = col3 = []

    imp_urg = ["Imp", "Urg"]
    imp_not_urg = ["Imp", "Not", "Urg"]
    not_imp_urg = ["Not", "Imp", "Urg"]
    not_imp_not_urg = ["Not", "Imp", "Not", "Urg"]

    if len(imp_urg) < len(imp_not_urg):
        diff = len(imp_not_urg) - len(imp_urg)
        imp_urg.extend([" "] * diff)
    elif len(imp_not_urg) < len(imp_urg):
        diff = len(imp_urg) - len(imp_not_urg)
        imp_urg.extend([" "] * diff)

    col0 = ["Important"] + [" "] * (len(imp_urg) - 1) + ["---", "Not Important"]
    col1 = imp_urg + ["---"] + not_imp_urg
    col2 = ["---"] * (len(imp_urg) + 1 + max(len(not_imp_urg), len(not_imp_not_urg)))
    col3 = imp_not_urg + ["---"] + not_imp_not_urg

    zipped = zip_longest(col0, col1, col2, col3, fillvalue=" ")
    print(tabulate(list(zipped),
                   headers=[" ", "Urgent", "---", "Not Urgent"]))


def init():
    return


if __name__ == "__main__":
    SystemExit(main())
