
"""class LibraryBook:
    def __init__(self, title: str, author : str, ISBN,  DateAcquired: str):
        self._title = title
        self._author = author
        self._ISBN = ISBN
        self._OnLoan = False
        self._DateAcquired = DateAcquired
    def SetLoan(self):
        self._OnLoan = True
    def ReturnLoan(self):
        self._OnLaon = False
    def DisplayDetails(self):
        print(f'Title: {self._title}, Author: {self._author}')

book = LibraryBook("Hi", 'hello', '12345', '10-10-2023')
book.DisplayDetails()"""

class StockItem:
    def __init__(self, title, DateAcquired):
        self._title = title
        self._OnLoan = False
        self._DateAcquired = DateAcquired
    def SetLoan(self):
        self._OnLoan = True
    def ReturnLoan(self):
        self._OnLaon = False
class CD(StockItem):
    def __init__(self, title, DateAcquired, Artist, PlayTime):
        super().__init__(title, DateAcquired)
        self._Artist = Artist
        self._PlayTime = PlayTime
        self._OnLoan = False
    def DisplayDetails(self):
        print(f'Title: {self._title} \nArtist: {self._Artist} \nPlaytime: {self._PlayTime}')
        if self._OnLoan == False:
            print("This cd is currently not on loan")
        else:
            print("This cd is currently on loan")
    
class LibraryBook(StockItem):
    def __init__(self, title, DateAcquired, Author, ISBN):
        super().__init__(title, DateAcquired)
        self._author = Author
        self._ISBN = ISBN
        self._OnLoan = False
    def DisplayDetails(self):
        print(f'Title: {self._title} \nAuthor: {self._author} \nISBN: {self._ISBN}')
        if self._OnLoan == False:
            print("This book is currently not on loan")
        else:
            print("This book is currently on loan")



book = LibraryBook("Hi", '10-10-2023', 'Hello', "12344134")
book.DisplayDetails()
book.SetLoan()
book.DisplayDetails()

cd = CD("Hi","10-10-2023","Hello","1m23s")
cd.DisplayDetails()
cd.SetLoan()
cd.DisplayDetails()