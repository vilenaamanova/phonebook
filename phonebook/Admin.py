# В записную книжку добавить админов, которые могут добавлять и удалять контакты из любых записных книжек

from phonebook.User import User
from phonebook.Phonebook import Phonebook

class Admin(User):
    def add_contact_to_phonebook(self, contact, phonebook):
        phonebook.contacts.append(contact)

    def remove_contact_from_phonebook(self, contact, phonebook):
        phonebook.contacts.remove(contact)
