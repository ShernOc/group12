# 1. 1-to-1 Relationship: Author and Book
# Scenario: Each book has a unique author, and an author writes only one book.
# Implement two classes: Author and Book.
# Define attributes like name for Author and title for Book.
# Ensure that a Book object is always associated with an Author object.
# Add a method to display the author’s name and their book title.


#Creating a class Author taking in name as arguments
class Author:
    def __init__(self,name):
        self.name = name 

    
#Class book that takes title and author  as arguments 
#We are also passing the author, as 
class Book:
    def __init__(self,title, author):
        self. title = title
        self.author = author 
    
    
 #create an Author object 
author3 = Author("Collins")
author2 = Author ("Abdi")
author5 = Author("Marion")


#A book association with an Author. 
#create Book object that is going to associate or relate to the author
# here book2 is in relationship with author3 = "collins"
book2 = Book("One to One Relationship",author3)
book5 = Book("Things Fall Apart", author2) 
book10= Book("Inheritance Book", author5)

#Method/function to display/call the author's name and book title. 

def display_name():
    print(f"The book title is :{book2.title} and the author of the book is: {book2.author.name}")
  
display_name()

author3.name # output = Collins 
book2.title # output = One to One Relationship 










        
        
        
        