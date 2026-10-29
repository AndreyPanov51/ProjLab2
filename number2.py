import csv


def main():
    search_author = "Петрановская"

    print(
        f"Результаты поиска по автору '{search_author}' "
        f"за 2015 и 2018 годы:"
    )

    search_author = search_author.lower()

    with open("books.csv", encoding="windows-1251") as file:
        reader = csv.DictReader(file, delimiter=";")
        for row in reader:
            date_str = row.get("Дата поступления", "")
            if date_str != "":
                year = int(date_str.split()[0].split(".")[2])
                if year in (2015, 2018):
                    author = row.get("Автор", "").lower()
                    author_full = row.get("Автор (ФИО)", "").lower()
                    if (
                        search_author in author
                        or search_author in author_full
                    ):
                        print(
                            f"[{year}] {row.get('Автор (ФИО)')} - "
                            f"{row.get('Название')}"
                        )


if __name__ == "__main__":
    main()