import csv


def main():
    count = 0

    with open("books.csv", encoding="windows-1251") as file:
        reader = csv.DictReader(file, delimiter=";")
        for row in reader:
            title = row.get("Название", "")
            if len(title) > 30:
                count += 1

    print("Количество записей с названием длиннее 30 символов: ", count)


if __name__ == "__main__":
    main()