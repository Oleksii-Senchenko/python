# import copy
# from dataclasses import dataclass
#
#
# @dataclass
# class Book:
#     title: str
#     author: str
#     year: str
#     pages: int
#
#     def __copy__(self):
#         return self.title, self.author, self.year, self.pages
#
#
# book1 = Book('asda', "asdas", '123', 123)
#
# book2 = copy.copy(book1)
# print(book2)
#

def foo(b, a:list = None):
    if a is None:
        a = []
    a.append(b)
    print(a)


foo(3)
foo(4)
foo(5)