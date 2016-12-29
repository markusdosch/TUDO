from itertools import zip_longest
from tabulate import tabulate
from store import TasksStore


def finish_tasks(numbers):
    TasksStore.active_db.set_done(numbers)
    return


def remove_tasks(numbers):
    TasksStore.active_db.remove(numbers)
    return


def add(args):
    if args[0] == "--prio" and len(args[1:]) % 3 == 0:
        tasks = args[1:]
        for i in range(0, len(tasks) // 3):
            TasksStore.active_db.add_task_p([tasks[i * 3], tasks[i * 3 + 1], tasks[i * 3 + 2]])
    else:
        # TODO Behaviour for no Tasks to add
        for description in args:
            TasksStore.active_db.add_task(description)
    return


def list_tasks(show_completed=False, important = None, urgent = None):
    if important and urgent:
        tasks = TasksStore.active_db.list_tasks_p(important, urgent)
    else:
        tasks = TasksStore.active_db.list_tasks()

    if show_completed:
        print(tabulate([[
                            task.number,
                            task.description,
                            task.started.strftime("%Y-%m-%d %H:%M"),
                            "No" if task.important == 0 else "Yes",
                            "No" if task.urgent == 0 else "Yes",
                            task.finished.strftime("%Y-%m-%d %H:%M") if task.finished else "No"
                         ] for task in tasks],
                       headers=["#", "Description", "Started", "Important", "Urgent", "Finished"]))
    else:
        print(tabulate([[
                            task.number,
                            task.description,
                            task.started.strftime("%Y-%m-%d %H:%M"),
                            "No" if task.important == 0 else "Yes",
                            "No" if task.urgent == 0 else "Yes",
                        ] for task in tasks if not task.is_finished()],
                       headers=["#", "Description", "Started", "Important", "Urgent"]))
    return tasks


# TODO: Be able to set time range for grouping
def group_tasks_archived(*args):
    dates_and_nums = TasksStore.active_db.group_tasks_archived()
    print(tabulate(dates_and_nums,
                   headers=["Date", "Tasks finished"]))
    return dates_and_nums


def eisenhower_matrix(*args):
    col0 = col1 = col2 = col3 = []

    imp_urg = list(map(lambda task: str(task.number) + ": "+task.description, TasksStore.active_db.list_tasks_p(1, 1)))
    imp_not_urg = list(map(lambda task: str(task.number) + ": "+task.description, TasksStore.active_db.list_tasks_p(1, 0)))
    not_imp_urg = list(map(lambda task: str(task.number) + ": "+task.description, TasksStore.active_db.list_tasks_p(0, 1)))
    not_imp_not_urg = list(map(lambda task: str(task.number) + ": "+task.description, TasksStore.active_db.list_tasks_p(0, 0)))

    if len(imp_urg) < len(imp_not_urg):
        diff = len(imp_not_urg) - len(imp_urg)
        imp_urg.extend([" "] * diff)
    elif len(imp_not_urg) < len(imp_urg):
        diff = len(imp_urg) - len(imp_not_urg)
        imp_not_urg.extend([" "] * diff)

    col0 = ["Important"] + [" "] * (len(imp_urg) - 1) + ["---", "Not Important"]
    col1 = imp_urg + ["---"] + not_imp_urg
    col2 = ["---"] * (len(imp_urg) + 1 + max(len(not_imp_urg), len(not_imp_not_urg)))
    col3 = imp_not_urg + ["---"] + not_imp_not_urg

    zipped = zip_longest(col0, col1, col2, col3, fillvalue=" ")
    print(tabulate(list(zipped),
                   headers=[" ", "Urgent", "---", "Not Urgent"]))