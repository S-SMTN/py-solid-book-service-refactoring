from app.book.book_services.method_interface import IBookAction
from app.book.book import Book


class BookPrinterConsole(IBookAction):
    @staticmethod
    def method(book: Book) -> None:
        print(book.content)


class BookPrinterReverse(IBookAction):
    @staticmethod
    def method(book: Book) -> None:
        print(book.content[::-1])
