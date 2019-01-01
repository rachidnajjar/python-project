'''
Created on 29 déc. 2018

@author: rachid
'''
import unittest
from models import Personne
import datetime


class PersonneTest(unittest.TestCase):


    def test_obtenirAge(self):
        dateReference = datetime.date(2019, 1, 1)
        expected = 11

        p = Personne("NAJJAR", "Amine", datetime.date(2008, 6, 14))
        actual = p.obtenirAge(dateReference)

        self.assertEqual(actual, expected)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testObtenirAge']
    unittest.main()