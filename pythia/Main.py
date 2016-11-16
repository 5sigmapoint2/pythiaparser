import time
import unittest

from pythia.Adapter import python_adapter


class TestAdapter(unittest.TestCase):
    def testPingFunction(self):
        self.assertEqual(
            "['r', [3, 'long string', [5, 67, 8], -9.0]]",
            python_adapter("['Pythia.ping', 3, 'long string', [5,67,8], -9.0]")
        )

    def testTestFunction(self):
        self.assertEqual(
            "['r', 'OK']",
            python_adapter("['Pythia.test', 3, 'long string', [5,67,8], -9.0]")
        )

    def testPerformance(self):
        command = "['Pythia.test', 3, 'long string', [5,67,8], -9.0]"
        iterations = 10000

        print("Calling", iterations, "times:", command)
        start = time.time()

        for _ in range(iterations):
            python_adapter(command)

        end = time.time()
        print("Total time:", end - start)


if __name__ == '__main__':
    unittest.main()
