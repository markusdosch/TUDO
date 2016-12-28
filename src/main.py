import sys

import store as store
import controller as controller

task_db = store.TasksStore()


def main(argv=sys.argv):
    if len(argv) == 1:
        # TODO print help
        return 1


    Switch = {
        "addp": controller.add_prioritised,
        "listp": listp,
        "add": controller.add,
        "del": controller.delete_tasks,
        "fin": controller.finish_tasks,
        "list": controller.list_tasks,
        "stats": controller.group_tasks_archived,
        "eisenhower": controller.eisenhower_matrix
    }

    Switch[argv[1]](argv[2:])
    return 0


def listp(args):
    if args[0] == "val" and len(args) == 3:
        controller.list_priorities(important=int(args[1]), urgent=int(args[3]))
    else:
        controller.list_priorities()
    return


def list(args):
    if args[0] == "all" and len(args) == 1:
        controller.list_tasks(show_completed=True)
    else:
        controller.list_tasks()


def init():
    return

if __name__ == "__main__":
    SystemExit(main())
