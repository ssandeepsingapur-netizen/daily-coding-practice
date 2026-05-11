class book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def display(self):
        print(f"Title: {self.title}, Author: {self.author}")
title = input("Enter the book title: ")
author = input("Enter the book author: ")
my_book = book(title, author)
my_book.display()