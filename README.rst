TUDO
====

A simple command-line based TODO-app in Python. Install with ``pip install tudo``.

.. image:: https://cl.ly/0u1D1j2m3X2C/Screen%20recording%202017-01-02%20at%2012.26.51%20PM.gif
   :alt: Screenshot.gif

Commands
--------

- ``tudo add <task_description> <...>``: Add new tasks. Default priorities: Important = No/0, Urgent = No/0
- ``tudo add --prio <important_val> <urgent_val> <task_description> <task_description> ...``: Add new tasks with non-default priorities (possible priority values: 0 => No, 1 => Yes)
- ``tudo list``: List all non-finished tasks
- ``tudo list all``: List all tasks including the finished ones
- ``tudo list [all] --prio <important_val> <urgent_val>``: List tasks, filter for specific important/urgent values
- ``tudo rm <task_id> <...>``: Delete tasks
- ``tudo done <task_id> <...>``: Set a task as done/finished
- ``tudo stats``: Display number of finished tasks per day
- ``tudo eisenhower``: Display open tasks in an Eisenhower matrix according to set priorities (see https://en.wikipedia.org/wiki/Time_management#The_Eisenhower_Method)

How to continue development (tested on Windows)
-----------------------------------------------

1. Navigate to the root directory of this repository
2. ``pip install -e .``
3. Now, you can use ``tudo list`` etc. while still applying changes to the underlaying source code
4. To uninstall, use ``pip uninstall tudo``

How to publish to PyPi (already done)
-------------------------------------

#. Register on PyPi (or, for tests, on TestPyPi) the  and create a personal ``.pypirc`` file in your HOME directory (see https://packaging.python.org/distributing/#create-an-account)
#. Register the package with ``python setup.py register -r <testpypi|pypi>`` (see https://packaging.python.org/distributing/#register-your-project)

  a. **Attention**: This does not work with the live PyPi version (``Server response (410): This API is no longer supported, instead simply upload the file.``). Using the register form (https://pypi.python.org/pypi?%3Aaction=submit_form) works.

#. Upload the package with ``twine upload dist/* -r <testpypi|pipy>`` (see https://wiki.python.org/moin/TestPyPI)
#. Install the package with ``pip install [-i https://testpypi.python.org/pypi] tudo``
#. To uninstall, use ``pip uninstall tudo``

Also probably a good guide: http://peterdowns.com/posts/first-time-with-pypi.html

Open issues
-----------

- ``database.db`` is currently created & saved in the same directory from where the ``tudo`` command was executed (leads to multiple ``database.db`` files). But our app should always use the same database location! (What is a good location? The user directory?)
- Editing tasks
