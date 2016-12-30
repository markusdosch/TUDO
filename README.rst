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
4. To uninstall, use ``pip uninstall tudo``

How to publish to PyPi (already done)
-------------------------------------
1. Register on PyPi (or, for tests, on TestPyPi) the  and create a personal ``.pypirc`` file in your HOME directory (see https://packaging.python.org/distributing/#create-an-account)
2. Register the package with ``python setup.py register <testpypi|pypi>`` (see https://packaging.python.org/distributing/#register-your-project)
3. Upload the package with ``twine upload dist/* -r <testpypi|pipy>`` (see https://wiki.python.org/moin/TestPyPI)
4. Install the package with ``pip install [-i https://testpypi.python.org/pypi] tudo``
5. To uninstall, use ``pip uninstall tudo``

Open issues
-----------
- ``database.db`` is currently created & saved in the same directory from where the ``tudo`` command was executed (leads to multiple ``database.db`` files). But our app should always use the same database location! (What is a good location? The user directory?)
- Editing tasks