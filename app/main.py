import json
import xml.etree.ElementTree as ET


class DisplayBook:
    def __init__(self, content: str) -> None:
        self.content = content

    def console(self) -> None:
        print(self.content)

    def reverse(self) -> None:
        print(self.content[::-1])


class PrintBook:
    def __init__(self, title: str, content: str) -> None:
        self.title = title
        self.content = content

    def console(self) -> None:
        print(f"Printing the book: {self.title}...")
        print(self.content)

    def reverse(self) -> None:
        print(f"Printing the book in reverse: {self.title}...")
        print(self.content[::-1])


class SerializeBook:
    def __init__(self, title: str, content: str) -> None:
        self.title = title
        self.content = content

    def json(self) -> str:
        return json.dumps({"title": self.title, "content": self.content})

    def xml(self) -> str:
        root = ET.Element("book")
        title = ET.SubElement(root, "title")
        title.text = self.title
        content = ET.SubElement(root, "content")
        content.text = self.content
        return ET.tostring(root, encoding="unicode")


class Book:
    def __init__(self, title: str, content: str) -> None:
        self.title = title
        self.content = content
        self.display = DisplayBook(content)
        self.print = PrintBook(title, content)
        self.serialize = SerializeBook(title, content)


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        command = getattr(book, cmd)
        command_attr = getattr(command, method_type)
        data = command_attr()
        if data:
            return data


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
