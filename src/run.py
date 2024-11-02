"""Исполняемый файл программы"""

from pprint import pprint
import csv

from src.common.common import contact_normalization, refactoring_phone_book


with open("documents/phonebook_raw.csv", encoding="utf-8") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)
    contact_normalization(contacts_list)

phone_book = refactoring_phone_book(contacts_list)

new_contacts_list = [contacts_list[0]]

for v in phone_book.values():
    new_contacts_list.append(v)

with open("documents/phonebook.csv", "w", encoding="utf-8") as f:
    datawriter = csv.writer(f, delimiter=',')
    datawriter.writerows(new_contacts_list)

if __name__ == '__main__':
    pprint(new_contacts_list)
