import json
import xml.etree.ElementTree as ElementTree


class DisplayBook:

    @staticmethod
    def console(content: str, *_) -> None:
        print(content)

    @staticmethod
    def reverse(content: str, *_) -> None:
        print(content[::-1])


class PrintBook:

    @staticmethod
    def console(content: str, title: str) -> None:
        print(f"Printing the book: {title}...")
        print(content)

    @staticmethod
    def reverse(content: str, title: str) -> None:
        print(f"Printing the book in reverse: {title}...")
        print(content[::-1])


class SerializeBook:

    @staticmethod
    def json(content: str, title: str) -> str:
        return json.dumps({"title": title, "content": content})

    @staticmethod
    def xml(content: str, title: str) -> str:
        root = ElementTree.Element("book")
        xml_title = ElementTree.SubElement(root, "title")
        xml_title.text = title
        xml_content = ElementTree.SubElement(root, "content")
        xml_content.text = content
        return ElementTree.tostring(root, encoding="unicode")


class Book:
    def __init__(self, title: str, content: str) -> None:
        self.title = title
        self.content = content
        self.display = DisplayBook()
        self.print = PrintBook()
        self.serialize = SerializeBook()


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        command = getattr(book, cmd)
        command_attr = getattr(command, method_type)
        data = command_attr(book.content, book.title)
        if data:
            return data


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
