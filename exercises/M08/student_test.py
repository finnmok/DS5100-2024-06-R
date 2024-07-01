import unittest
import student as st

class TestStringMethods(unittest.TestCase):

    # test function
    def test_01(self):

        finn = st.Student("Finn",["course1","course2"])
        orig_n = finn.num_courses

        finn.enroll_in_course("course3")
        updated_n = finn.num_courses

        self.assertTrue(orig_n - 1, updated_n)

    def test_02(self):

        orig = ["course1","course2"]
        finn = st.Student("Finn",orig)

        finn.unenroll_in_course('course1')

        self.assertTrue(orig, ["course2"])

    def test_03(self):

            orig = ["course1","course2"]
            finn = st.Student("Finn",orig)
            orig_n = finn.num_courses

            with self.assertRaises(ValueError):
                 finn.unenroll_in_course('course3')
            updated_n = finn.num_courses

            self.assertTrue(orig_n, updated_n)
            
if __name__ == '__main__':
    unittest.main(verbosity=2)