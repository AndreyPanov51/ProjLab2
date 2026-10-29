import csv
import random


def main():
    all_books = []

    with open("books.csv", encoding="windows-1251") as file:
        reader = csv.DictReader(file, delimiter=";")
        for row in reader:
            author = row.get("Автор (ФИО)")
            title = row.get("Название")
            date_str = row.get("Дата поступления", "")

            if date_str != "":
                year = date_str.split()[0].split(".")[2]
                all_books.append(
                    {"author": author, "title": title, "year": year}
                )

    random_books = random.sample(all_books, 20)

    with open("bibliography.txt", "w", encoding="utf-8") as out_file:
        for i, book in enumerate(random_books, start=1):
            out_file.write(
                f"{i}. {book['author']}. {book['title']} - {book['year']}\n"
            )


if __name__ == "__main__":
    main()

