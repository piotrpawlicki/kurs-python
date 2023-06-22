import unittest
import unittest as ut
from student import Student

class TestStudent(unittest.TestCase):

    def test_email(self):
        anna = Student('anna', 'snow', 4.6)
        expected = 'anna.snow@uam.com'
        self.assertEqual(anna.email, expected)

        anna.last = 'summer'
        new_email = 'anna.summer@uam.com'
        self.assertEqual(anna.email, new_email)


    def test_fullname(self):
        anna = Student('anna', 'snow', 4.6)
        expected = 'Anna Snow'
        self.assertEqual(anna.fullname, expected)

        anna.last = 'summer'
        new_fullname = 'Anna Summer'
        self.assertEqual(anna.fullname, new_fullname)

    def test_grant_scholarship(self):
        anna = Student('anna', 'snow', 4.6)
        adam = Student('adam', 'kowalski', 3.5)

        anna.grant_scholarship()
        self.assertTrue(anna.scholarship)
        adam.grant_scholarship()
        self.assertFalse(adam.scholarship)

if __name__ == '__main__':
    unittest.main()