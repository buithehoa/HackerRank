#!/bin/python3

from book import Book

class MyBook(Book):
    def __init__(self, title, author, price):
        self.price = price
        super().__init__(title, author)

    def display(self):
        print("Title: %s" % self.title)
        print("Author: %s" % self.author)
        print("Price: %d" % self.price)
