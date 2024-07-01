import pandas as pd

class BookLover():
    def __init__(
        self, name, email, fav_genre,
        num_books = 0,
        book_list = pd.DataFrame({'book_name':[], 'book_rating':[]})):
        """
        Initializes the BookLover with the given name, email, favorite genre, number of books read, and book list.

        INPUTS:
        name : str
            The name of the book lover.
        email : str
            The email of the book lover.
        fav_genre : str
            The favorite genre of the book lover.
        num_books : int, optional, default = 0
            The number of books the book lover has read.
        book_list : pandas.DataFrame, optional
            A DataFrame containing the names and ratings of the books read (default is an empty DataFrame).
        """
        self.name = name
        self.email = email
        self.fav_genre = fav_genre
        if num_books != book_list.shape[0]:
            self.num_books = book_list.shape[0]
        else:
            self.num_books = num_books
        if book_list.shape[0] == book_list.drop_duplicates(['book_name']).shape[0]:
            self.book_list = book_list
        else:
            raise ValueError("book_list must contain unique books")

    def add_book(self, book_name, book_rating):
        """
        Adds a book to the book list if it hasn't been read yet.

        INPUTS:
        book_name : str
            The name of the book to add.
        book_rating : int
            The rating of the book to add.
        """
        if self.has_read(book_name) == False:
            new_book = pd.DataFrame({
                'book_name': [book_name], 
                'book_rating': [book_rating]
            })

            self.book_list = pd.concat([self.book_list, new_book], ignore_index=True)
            self.num_books += 1


    def has_read(self, book_name):
        """
        Check if book has already been read.

        INPUT:
        book_name : str
            The name of the book to check.

        OUTPUT:
        bool
            True if book has been read, else False.
        """
        if book_name in self.book_list['book_name'].values:
            print(f"{self.name}, This Book, '{book_name}' Already Exists in Your Book List")
            return True
        else: 
            return False
    
    def num_books_read(self):
        """
        Returns the number of books read.

        OUTPUT:
        int
            The number of books read.
        """
        return self.num_books
    
    def fav_books(self):
        """
        Returns a DataFrame of books with a rating greater than 3.

        OUTPUT:
        pandas.DataFrame
            A DataFrame with the favorite books.
        """
        return self.book_list.loc[self.book_list['book_rating']>3,:]