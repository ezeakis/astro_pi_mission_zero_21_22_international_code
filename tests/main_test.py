import unittest


class testTests(unittest.TestCase):

    def test_1(self):
        self.assertIs("a", "a")
    
    
if __name__ == '__main__':
    unittest.main()
