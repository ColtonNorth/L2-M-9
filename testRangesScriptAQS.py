import unittest
from random import randint

class test_ranges(unittest.TestCase):

    def test_ranges(self):
        #Initialize random values within range
        carbonVal = randint(0,2000)
        nitrogenVal = randint(0,100)
        vocVal = randint(0,750)

        #Maximum values for given ranges
        carbonMaxVal = 2000
        carbonMinVal = 0

        nitrogenMaxVal = 100
        nitrogenMinVal = 0

        vocMaxVal = 750
        vocMinVal = 0

        #Test if the values are within the given range
        self.assertTrue(carbonVal <=  carbonMaxVal, msg= "carbon Level out of range")
        self.assertTrue(carbonVal >=  carbonMinVal, msg= "carbon Level out of range")

        self.assertTrue(nitrogenVal <=  nitrogenMaxVal, msg= "nitrogen Level out of range")
        self.assertTrue(nitrogenVal >=  nitrogenMinVal, msg= "nitrogen Level out of range")

        self.assertTrue(vocVal <=  vocMaxVal, msg= "voc Level out of range")
        self.assertTrue(vocVal >=  vocMinVal, msg= "voc Level out of range")

if __name__ == '__main__':
    unittest.main()

