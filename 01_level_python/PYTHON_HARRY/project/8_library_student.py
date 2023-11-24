class Library:
    def __init__(self,Listofbooks):
        self.books=Listofbooks
    def displayAvailableBooks(self):
        print("Books present in the library are:")
        for book in self.books:
            print(" *"+book)
    def borrowBook(self,bookname):
        if bookname in self.books:
            print("You have been issued {bookname}.please keep it safe and return it within 30 days ") 
            self.books.remove(bookname)
            return True
        else:
            print("Sorry,This book has already been issued to someone else.please wait until the book is returned")
            return False    
    def returnBook(self,bookname): 
        self.books.append(bookname)
        print("Thanks for returning this book  i hope you enjoyed reading it.")
class Student:
    def requestBooks(self):
        self.book=input("Enter the name of the book you want to borrow: ")
        return self.book
    def returnBooks(self):
        self.book=input("Enter the name of the book you want to return: ")
        return self.book
if __name__=="__main__":
    centralLibrary=Library(["Maths","Algorithm","Django","Philosophy","psychology"])
    student=Student()
    #centralLibrary.displayAvailableBooks()
    while(True):
        welcomeMssg ='''===Welcome to central library === please choose an option 
        1. Listing  all the books
        2.Request a book 
        3.Return a book 
        4.Exit the library
        '''
        print(welcomeMssg)
        a=int(input("Enter the choice:"))
        if a==1:
            centralLibrary.displayAvailableBooks()
        elif a==2:
            centralLibrary.borrowBook(student.requestBooks())
        elif a==3:
            centralLibrary.returnBook(student.returnBooks())
        else:
            print("Thanks for using this library ")
            exit()