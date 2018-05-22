import unittest
import Calculator


class TestCalc(unittest.TestCase):
    def test_add(self):
        result = Calculator.add(10, 5)
        self.assertEqual(result, 15)

        self.assertEqual(Calculator.add(-1, 1), 0)
        self.assertEqual(Calculator.add(-1, -1), -2)

    # def test_subtract(self):
    #     self.assertEqual(Calculator.subtract(10, 8), 2)
    #     self.assertEqual(Calculator.subtract(-5, 1), -6)
    #     self.assertEqual(Calculator.subtract(-1, -10), 9)
    #
    # def test_multiply(self):
    #     self.assertEqual(myCode.multiply(10, 8), 80)
    #     self.assertEqual(myCode.multiply(-5, 1), -5)
    #     self.assertEqual(myCode.multiply(-10, -12), 120)

    # def test_divide(self):
    #     self.assertEqual(myCode.divide(10, 5), 2)
    #     self.assertEqual(myCode.divide(5, 3), 1.6666666666666667)
    #     self.assertEqual(myCode.divide(-10, 5), -2)
    #     self.assertEqual(myCode.divide(-1, -1), 1)

        #self.assertRaises(ValueError, myCode.divide, 10, 0)    # Mozhno i tak

        # with self.assertRaises(ValueError):
        #     myCode.divide(10, 0)






if __name__ == '__main__':
    unittest.main()
