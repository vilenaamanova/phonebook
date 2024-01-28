from phonebook.User import User
from phonebook.Phonebook import Phonebook
from phonebook.Contact import Contact

if __name__ == "__main__":

    user = User("abc", "Ivan", "Ivanov")
    friend1 = User("qwe", "Anna", "Semenova")
    friend2 = User("xyz", "Ilya", "Ilyich")

    c1 = Contact(friend1, '+7', '9991002233')
    c2 = Contact(friend2, '+7', '9882346677')

    user.create_phonebook('friends')
    user.phonebooks['friends'].create_contact(c1)
    user.phonebooks['friends'].create_contact(c2)
    user.create_phonebook('family')
    user.phonebooks['family'].create_contact(c2)

    user.add_friend(friend1)
    user.add_friend(friend2)
    user.delete_friend(friend1)

    print("----- Выводим логины всех друзей пользователя -----")
    for i in range(len(user.friends)):
        print(user.friends[i].login)
    print("\n")

    print("----- Выводим те контакты, из телефонной книжки с тегом friends, чей код страны равен \"+7\" -----")
    user.phonebooks['friends'].show_contacts_country('+7')
    print("\n")

    print("----- Выводим контакты определенного пользователя -----")
    user.phonebooks['friends'].show_contacts_user('qwe')

