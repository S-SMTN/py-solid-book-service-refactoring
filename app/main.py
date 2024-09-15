from app.book.factories.action_factory import BookActionFactory
from app.book.book import Book


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for action_type, method_type in commands:
        action_factory = BookActionFactory.get_action_factory(action_type)
        method = action_factory.get_book_method(method_type)
        data = method.method(book)
        if data:
            return data


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
