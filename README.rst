====
TUDO
====

A simple command-line based TODO-app in Python
==============================================

Commands
--------
- ``main.py add <task_description> <...>``: Add new tasks. Default priorities: Important = No/0, Urgent = No/0
- ``main.py add --prio <task_description> <important_val> <urgent_val> <...>``: Add new tasks with non-default priorities (possible priority values: 0 => No, 1 => Yes)
- ``main.py list``: List all non-finished tasks
- ``main.py list all``: List all tasks including the finished ones
- ``main.py list --prio [all] <important_val> <urgent_val>``: List tasks, filter for specific important/urgent values
- ``main.py rm <task_id> <...>``: Delete tasks
- ``main.py done <task_id> <...>``: Set a task as done/finished
- ``main.py stats``: Display number of finished tasks per day
- ``main.py eisenhower``: Display open tasks in an Eisenhower matrix according to set priorities (see https://en.wikipedia.org/wiki/Time_management#The_Eisenhower_Method)

How to continue development (tested on Windows)
-----------------------------------------------
1. Navigate to the root directory of this repository
2. ``pip install -e .``
3. Now, you can use ``tudo list`` etc. while still applying changes to the underlaying source code
4. To uninstall, use `pip uninstall tudo`

Open issues
-----------
- Where is & where should the ``database.db`` be saved?
- Editing tasks