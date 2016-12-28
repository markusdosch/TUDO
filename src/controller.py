from itertools import zip_longest

from tabulate import tabulate

from main import task_db


def finish_tasks(numbers):
    task_db.set_done(numbers)
    return


def delete_tasks(numbers):
    task_db.delete(numbers)
    return


def add(descriptions):
    # TODO Behaviour for no Tasks to add
    for description in descriptions:
        task_db.add_task(description)
    return


def add_prioritised(args):
    for i in range(0, len(args) // 3):
        task_db.add_task_p([args[i * 3], args[i * 3 + 1], args[i * 3 + 2]])


def list_priorities(important = None, urgent = None):
    if important and urgent:
        tasks = task_db.list_tasks_p(important, urgent)
    else:
        tasks = task_db.list_tasks()

    print(tabulate([[task.number, task.description, task.started.strftime("%Y-%m-%d %H:%M"),
                     task.finished.strftime("%Y-%m-%d %H:%M") if task.finished else "Not Yet", task.important,
                     task.urgent] for task in tasks],
                   headers=["#", "Description", "Started", "Finished", "important", "urgent"]))

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


def group_tasks_archived(*args):
    dates_and_nums = task_db.group_tasks_archived()
    print(tabulate(dates_and_nums,
                   headers=["Date", "Tasks finished"]))
    return dates_and_nums


def eisenhower_matrix(*args):
    col0 = col1 = col2 = col3 = []

    imp_urg = list(map(lambda task: str(task.number) + ": "+task.description, task_db.list_tasks_p(1, 1)))
    imp_not_urg = list(map(lambda task: str(task.number) + ": "+task.description, task_db.list_tasks_p(1, 0)))
    not_imp_urg = list(map(lambda task: str(task.number) + ": "+task.description, task_db.list_tasks_p(0, 1)))
    not_imp_not_urg = list(map(lambda task: str(task.number) + ": "+task.description, task_db.list_tasks_p(0, 0)))

    if len(imp_urg) < len(imp_not_urg):
        diff = len(imp_not_urg) - len(imp_urg)
        imp_urg.extend([" "] * diff)
    elif len(imp_not_urg) < len(imp_urg):
        diff = len(imp_urg) - len(imp_not_urg)
        imp_not_urg.extend([" "] * diff)

    col0 = ["Important (1)"] + [" "] * (len(imp_urg) - 1) + ["---", "Not Important (0)"]
    col1 = imp_urg + ["---"] + not_imp_urg
    col2 = ["---"] * (len(imp_urg) + 1 + max(len(not_imp_urg), len(not_imp_not_urg)))
    col3 = imp_not_urg + ["---"] + not_imp_not_urg

    zipped = zip_longest(col0, col1, col2, col3, fillvalue=" ")
    print(tabulate(list(zipped),
                   headers=[" ", "Urgent (1)", "---", "Not Urgent (0)"]))