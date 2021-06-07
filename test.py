import unnittest
import example

    class TestCase(unnittest.TestCase):

        deg test_add_1(self):
            self.assertEqual(example.add(1, 2), 3)

if __name__ == '__main__':
    unittest.main()