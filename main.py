import sys

tasks = []


def main(argv=sys.argv):
    print(str(argv))

    if argv[1] == "add":
        add(argv[1:])
    if argv[1] == "list":
        list()
    return 0


def add(*string):
    # TODO Behaviour for no Tasks to add
    global tasks
    tasks.extend(string)
    return


def list():
    return tasks


def init():
    global tasks
    tasks = []


if __name__ == "__main__":
    SystemExit(main(['', '-o']))
