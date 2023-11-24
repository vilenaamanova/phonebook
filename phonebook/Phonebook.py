# Класс телефонной книжки, который поддерживает:
# а. список контактов
# б. возможность добавить/удалить контакт
# в. тег книжки
# г. возможность отобрать из книжки те контакты, которые принадлежат какой-то стране по коду страны
# д. возможность отобрать контакты, которые принадлежат какому-то юзеру

from phonebook.Contact import Contact

class Phonebook:
    def __init__(self):
        self.contacts = []

    def create_contact(self, contact):
        self.contacts.append(contact)

    def delete_contact(self, contact):
        self.contacts.remove(contact)

    def show_contacts_country(self, country_code):
        for i in range(len(self.contacts)):
            if country_code == self.contacts[i].country_code:
                print(f"{self.contacts[i].user.first_name} {self.contacts[i].user.last_name}\n"
                      f"Телефон: {self.contacts[i].country_code}{self.contacts[i].phone_num}")

    def show_contacts_user(self, login):
        for i in range(len(self.contacts)):
            if login == self.contacts[i].user.login:
                print(f"{self.contacts[i].user.first_name} {self.contacts[i].user.last_name}\n"
                      f"Телефон: {self.contacts[i].country_code}{self.contacts[i].phone_num}")