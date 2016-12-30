import unittest

import controller, app


class TestTudoMethods(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        app.init("test_db.db")

    def setUp(self):
        app.task_db.reset()

    def test_add(self):
        controller.add(["Do Homework"])
        # self.assertEqual(main.list_tasks()[-1], "Do Homework")
        self.assertTrue(len(controller.list_tasks()) == 1)

    def test_list(self):
        self.assertTrue(len(controller.list_tasks()) == 0)

    @classmethod
    def tearDownClass(cls):
        return
        # TODO: Delete database file after completing all tests


if __name__ == "__main__":
    unittest.main()
