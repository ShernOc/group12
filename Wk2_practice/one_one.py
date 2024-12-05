# 1. 1-to-1 Relationship: Author and Book
# Scenario: Each book has a unique author, and an author writes only one book.
# Implement two classes: Author and Book.
# Define attributes like name for Author and title for Book.
# Ensure that a Book object is always associated with an Author object.
# Add a method to display the author’s name and their book title.


#Calling an Author in relation to their book 
class Author:
    def __init__(self,name):
        self.name = name 
    
class Book:
    def __init__(self, title,author):
        self. title = title
        self.author = author
        # self.author = author 
        
#Calling the Class 
#Object of the Author
a2= Author("Collins")
# a1 = Author("Marion")


#Object of the Book 
b1 = Book("Things Fall Apart",a2)
# b2 = Book("Inheritance Book")

a2.name # Collins 
b1.title # Things Falls apart 
#creating a relationship 
# print(f"The Author is {a2.name}: {b1.author.name}")
# print(f"The title is {b1.title}: ")

#calling the name of author and book title
def display_name():
    print(f"The author is: {b1.author.name} and the title is: {b1.title}")
    
display_name()







        
        
        
        