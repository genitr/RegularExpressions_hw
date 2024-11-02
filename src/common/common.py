""""""
import re
from enum import IntEnum


class Title(IntEnum):
    LASTNAME = 0
    FIRSTNAME = 1
    SURNAME = 2
    ORGANISATION = 3
    POSITION = 4
    PHONE = 5
    EMAIL = 6


search_pattern = r'(\+7|8)\s?\(?(\d{3})\)?\s?\-?(\d{3})\s?\-?(\d{2})\s?\-?(\d{2})(\s)?(\(?)?(доб.\)?\s\d*)?(\)?)?'
replace_pattern = r'+7(\2)\3-\4-\5\6\8'


def contact_normalization(contacts: list[list]):
    """Приведение контактов к нормальному состоянию"""
    for row in contacts[1:]:
        combined_list = ' '.join(row[:3]).strip().replace('  ', ' ').split(' ')

        for ids, i in enumerate(combined_list):
            row[ids] = combined_list[ids]

        result = re.sub(search_pattern, replace_pattern, row[Title.PHONE])
        row[Title.PHONE] = result


def merging_identical_contacts(phone_book: dict, unique_key: str, contacts_list, contact, index: int):
    """Объединение идентичных контактов"""
    for k in list(phone_book.keys()):
        if k == unique_key:
            update_list = phone_book[k]
            second_list = contacts_list[index]

            for i in range(len(update_list)):
                if not update_list[i]:
                    update_list[i] = second_list[i]

            phone_book[unique_key] = update_list
        else:
            phone_book[unique_key] = contact


def refactoring_phone_book(contacts_list):
    """Поиск похожих контактов и их слияние в один контакт"""
    phone_book = {}
    keys = list(phone_book.keys())

    for ids, contact in enumerate(contacts_list[1:]):
        unique_key = f'{contact[Title.LASTNAME]} {contact[Title.FIRSTNAME]}'
        if not keys:
            phone_book[unique_key] = contact
            keys = list(phone_book.keys())
        else:
            merging_identical_contacts(phone_book, unique_key, contacts_list, contact, ids)

    return phone_book
