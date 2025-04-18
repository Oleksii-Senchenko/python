# import time
#
#
# class Profile:
#     def get_subsribers(self):
#         return []
#
#     def set_on_susubscribe(self, func):
#         self._on_susubscribe = func
#
#     def set_on_unsusubscribe(self, func):
#         self._unsusubscribe = func
#
#
# profile = Profile()
#
# def on_subscribe(users):
#     print(users)
#
# def on_unsubscribe(users):
#     ...
#     print(users)
#
#
# profile.set_on_susubscribe(on_subscribe)
# profile.set_on_unsusubscribe(on_unsubscribe)
#
# class User:
#     def check_subscribers(self, subscribers):
#         while True:
#             cur_subscribers = profile.get_subsribers()
#             if subscribers == cur_subscribers:
#                 pass
#             else:
#                 ...
#                 print()
#             time.sleep(10)
from enum import Enum, auto


class BookState(Enum):
    AVAILABLE = auto()
    UNAVAILABLE = auto()
    NOT_FOUND = auto()


class Library:

    books = {'aaa': BookState.AVAILABLE, 'bbb': BookState.AVAILABLE, "ccc": BookState.AVAILABLE, 'ddd': BookState.AVAILABLE}

    waiters = []

    def get_all_books(self):
        return self.books

    def get_book_status(self, title):
        return self.books.get(title, BookState.NOT_FOUND)


    def get_book(self, title):
        status = self.get_book_status(title)
        if status is BookState.AVAILABLE:
            self.books[title] = BookState.UNAVAILABLE
            return f'Book {title}'
        return status

    def return_book(self, title):
        self.books[title] = BookState.AVAILABLE
        for waiter in self.waiters:
            if waiter['book_title'] == title:
                waiter['callback'](title)

    def get_when_available(self, title, func):
        self.waiters.append({'book_title':title, 'callback': func})

library = Library()


print(library.get_book('aaa'))
print(library.get_book('aaa'))
print(library.get_book('sahj'))


