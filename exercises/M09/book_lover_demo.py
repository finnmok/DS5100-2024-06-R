from modulehw09.booklover import BookLover


bl = BookLover("Name","Email","NA")
bl.add_book("Travels with Charley",5)
bl.add_book("A Streetcare Named Desire",5)
bl.add_book("Where the Crawdads Sing",4)
bl.add_book("Catch-22",3)
print(bl.fav_books())