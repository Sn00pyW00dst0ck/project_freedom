"""Hello World Unit Test"""

import unittest

class HelloWorldTest(unittest.TestCase):
    """A 'Hello World' test case to ensure the system is setup properly."""
    def test_hello_world(self):
        """This dummy test should always pass. If it doesn't, then something is really wrong!"""
        self.assertEqual('Hello world!', 'Hello world!')

if __name__ == '__main__':
    unittest.main()
