import unittest

import controller, main


class TestTudoMethods(unittest.TestCase):
    def setUp(self):
        main.init()
        main.task_db.reset()

    def test_add(self):
        controller.add(["Do Homework"])
        # self.assertEqual(main.list_tasks()[-1], "Do Homework")
        self.assertTrue(len(controller.list_tasks()) == 1)

    def test_list(self):
        self.assertTrue(len(controller.list_tasks()) == 0)


if __name__ == "__main__":
    unittest.main()
