import sys

import controller
import store

task_db = None


def get_task_db():
    return task_db

# TODO: Call our app via "tudo <command>", not with "main.py"
def main(argv=sys.argv):
    if len(argv) == 1:
        # TODO print help
        return 1

    switch = {
        "add": controller.add,
        "list": controller.list_tasks,
        "rm": controller.remove_tasks,
        "done": controller.finish_tasks,
        "stats": controller.group_tasks_archived,
        "eisenhower": controller.eisenhower_matrix
    }

    switch[argv[1]](argv[2:])
    return 0


def list(args):
    if args[0] == "all":
        if len(args) > 1:
            if len(args) == 4 and args[1] == "--prio":
                controller.list_tasks(show_completed=True, important=int(args[2]), urgent=int(args[3]))
            else:
                controller.list_tasks(show_completed=True)
        else:
            controller.list_tasks(show_completed=True)
    else:
        if len(args) > 0:
            if len(args) == 3 and args[0] == "--prio":
                controller.list_tasks(important=int(args[1]), urgent=int(args[2]))
            else:
                controller.list_tasks()
        else:
            controller.list_tasks()


def init(database_name = "database.db"):
    global task_db
    task_db = store.TasksStore(database_name)


if __name__ == "__main__":
    init()
    SystemExit(main())
