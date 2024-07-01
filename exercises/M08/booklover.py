import pandas as pd

class BookLover():
    def __init__(
        self, name, email, fav_genre,
        num_books = 0,
        book_list = pd.DataFrame({'book_name':[], 'book_rating':[]})):

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
        
        if self.has_read(book_name) == False:
            new_book = pd.DataFrame({
                'book_name': [book_name], 
                'book_rating': [book_rating]
            })

            self.book_list = pd.concat([self.book_list, new_book], ignore_index=True)
            self.num_books += 1


    def has_read(self, book_name):
        if book_name in self.book_list['book_name'].values:
            print(f"{self.name}, This Book, '{book_name}' Already Exists in Your Book List")
            return True
        else: 
            return False
    
    def num_books_read(self):
        return self.num_books
    
    def fav_books(self):
        return self.book_list.loc[self.book_list['book_rating']>3,:]