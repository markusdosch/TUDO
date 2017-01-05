import sys
import argparse

import tudo.controller as controller
import tudo.store as store

parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers()

add_parser = subparsers.add_parser('add')
list_parser = subparsers.add_parser('list')
rm_parser = subparsers.add_parser('rm')
done_parser = subparsers.add_parser('done')
stats_parser = subparsers.add_parser('stats')
eisenhower_parser = subparsers.add_parser('eisenhower')

add_parser.add_argument('task_descriptions', metavar='task_description', nargs='+')  # There has to at least one task_description, there can be multiple task_descriptions
# TODO: With this solution, the tasks can not have individual priorities, but have all the same which were specified with --prio (add needs to be called again for that)
# This is different from the previous behaviour -> it would be better to get back to the previous behaviour
# TODO: Maybe change variable type to bool? (but probably needs to be done in the DB, too
add_parser.add_argument('--prio', nargs=2, type=int, help='<important_val> <urgent_val>')
add_parser.set_defaults(func=controller.add)  # set the default function to controller.add

list_parser.add_argument('all', action='store_true') # false by default
list_parser.add_argument('--prio', nargs=2, type=int, help='<important_val> <urgent_val>')
list_parser.set_defaults(func=controller.list_tasks)

rm_parser.add_argument('task_ids', nargs='+')
rm_parser.set_defaults(func=controller.remove_tasks)

done_parser.add_argument('task_ids', nargs='+')
done_parser.set_defaults(func=controller.finish_tasks)

stats_parser.set_defaults(func=controller.group_tasks_archived)
eisenhower_parser.set_defaults(func=controller.eisenhower_matrix)


def tudo():
    init()
    args = parser.parse_args()
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(1)
    args.func(args)


def init(database_name = "database.db"):
    store.TasksStore(database_name)

if __name__ == '__main__':
    tudo()