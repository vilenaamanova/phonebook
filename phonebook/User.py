# Класс пользователя, который поддерживает:
# а. список друзей
# б. словарь из телефонных книжек ({'family': phoneBook1, ...} -- размер словаря неограничен)
# в. user.add(contact, 'work'). возможность добавить новый контакт с учетом его тега.
# г. user1.share(user2, 'family'). возможность поделиться какой-либо телефонной книжкой с другом.
# Важно, что делиться книжками можно только с друзьями!
# Если юзер вам не друг -- напишите об этом. Если необходимого типа книжки нет -- напишите об этом.
# д. возможность добавлять и удалять друзей

from phonebook.Phonebook import Phonebook

class User:
    def __init__(self, login, first_name, last_name):
        self.login = login
        self.first_name = first_name
        self.last_name = last_name
        self.friends = []
        self.phonebooks = {}

    def add_contact(self, tag, pb_name, new_contact):
        if not isinstance(new_contact, User):
            raise ValueError("new_contact is not of class User")
        if tag in self.phonebooks:
            pb_name.create_contact(new_contact)
        else:
            print("Такой телефонной книжки не существует")

    def delete_contact(self, tag, pb_name, contact):
        if not isinstance(contact, User):
            raise ValueError("contact is not of class User")
        if tag in self.phonebooks:
            pb_name.delete_contact(contact)
        else:
            print("Такой телефонной книжки не существует")

    def add_friend(self, friend):
        if not isinstance(friend, User):
            raise ValueError("friend is not of class User")
        self.friends.append(friend)

    def delete_friend(self, friend):
        if not isinstance(friend, User):
            raise ValueError("friend is not of class User")
        self.friends.remove(friend)

    def create_phonebook(self, tag, pb_name):
        self.phonebooks[tag] = pb_name

    def share_phonebook(self, friend, tag):
        if not isinstance(friend, User):
            raise ValueError("friend is not of class User")
        if friend in self.friends:
            for i in range(len(self.phonebooks.get(tag).contacts)):
                print(self.phonebooks.get(tag).contacts[i].user.login)
                print(self.phonebooks.get(tag).contacts[i].country_code + self.phonebooks.get(tag).contacts[i].phone_num)
        else:
            print(f"Добавьте {friend.last_name} {friend.first_name} в друзья, чтобы поделится своей телефонной книжкой")
