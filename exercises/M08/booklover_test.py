import unittest
import numpy as np
import pandas as pd
from booklover import BookLover
import booklover as bl

class BookLoverTestSuite(unittest.TestCase):
   
    def test_1_add_book(self):
        """
        add a book and test if it is in `book_list`.
        """
        book = BookLover("Name","Email","NA")      
        book.add_book("Travels with Charley",5)
        self.assertTrue("Travels with Charley" in book.book_list['book_name'].values)

    def test_2_add_book(self):
        """ 
        add the same book twice. Test if it's in `book_list` only once.
        """
        book = BookLover("Dude","Email","NA")
        book.add_book("Travels with Charley",5)
        book.add_book("Travels with Charley",5)
        self.assertEqual(book.book_list[book.book_list['book_name'] == "Travels with Charley"].shape[0],1)

    def test_3_has_read(self):
        """
        pass a book in the list and test if the answer is `True`.
        """
        book = BookLover(
         "Dude","Email","NA",1,
         pd.DataFrame({'book_name':["Travels with Charley"], 'book_rating':[5]}))

        self.assertTrue(book.has_read("Travels with Charley"))

    def test_4_has_read(self):
        """
        pass a book NOT in the list and use `assert False` to test the answer is `True`
        """
        book = BookLover(
         "Dude","Email","NA",1,
         pd.DataFrame({'book_name':["Travels with Charley"], 'book_rating':[5]}))

        self.assertFalse(book.has_read("Travels without Charley"))

    def test_5_num_books_read(self):
        """ 
        add some books to the list, and test num_books matches expected.
        """
        book = BookLover("Dude","Email","NA")
        book.add_book("Traveled with Charley",5)
        book.add_book("Travels with Charley",5)
        book.add_book("Travels with Charley",5) #DUP
        book.add_book("Traveling with Charley",5)
        book.add_book("Travel with Charley",5)
        book.add_book("Will Travel with Charley",5)
        self.assertEqual(book.num_books,5)


    def test_6_fav_books(self):
        """ 
        add some books with ratings to the list, making sure some of them have rating > 3. 

        Your test should check that the returned books have rating  > 3
        """
        book = BookLover("Dude","Email","NA")
        book.add_book("Traveled with Charley",1)
        book.add_book("Travels with Charley",4)
        book.add_book("Travels with Charley",5) #DUP
        book.add_book("Traveling with Charley",3)
        book.add_book("Travel with Charley",2)
        book.add_book("Will Travel with Charley",5)
        self.assertTrue(all(book.fav_books()['book_rating'].values > 3))

if __name__ == '__main__':
    unittest.main(verbosity=3)