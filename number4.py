import xml.etree.ElementTree as ET


def main():
    tree = ET.parse("currency.xml")
    root = tree.getroot()
    currency_dict = {}

    for valute in root.iter("Valute"):
        code_el = valute.find("CharCode")
        nominal_el = valute.find("Nominal")

        if code_el is not None and nominal_el is not None:
            char_code = code_el.text
            nominal = int(nominal_el.text)
            currency_dict[char_code] = nominal

    print("Словарь 'CharCode - Nominal':")
    for code, nominal in currency_dict.items():
        print(f"{code} - {nominal}")
    


if __name__ == "__main__":
    main()