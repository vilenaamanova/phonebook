from phonebook.User import User
from phonebook.Phonebook import Phonebook
from phonebook.Contact import Contact

if __name__ == "__main__":
    user = User("abc", "Ivan", "Ivanov")
    friend1 = User("qwe", "Anna", "Semenova")
    friend2 = User("xyz", "Ilya", "Ilyich")
    c1 = Contact(friend1, '+7', '9991002233')
    c2 = Contact(friend2, '+7', '9882346677')
    friends_pb = Phonebook()
    friends_pb.create_contact(c1)
    friends_pb.create_contact(c2)
    user.create_phonebook('friends', friends_pb)
    user.add_friend(friend1)
    user.add_friend(friend2)
    user.delete_friend(friend1)
    print("----- Выводим логины всех друзей пользователя -----")
    for i in range(len(user.friends)):
        print(user.friends[i].login)
    print("----- Выводим все контакты пользователя -----")
    for i in range(len(user.phonebooks.get('friends').contacts)):
        print(user.phonebooks.get('friends').contacts[i].user.login)
    print("----- Выводим те контакты, чей код страны равен \"+7\" -----")
    friends_pb.show_contacts_country('+7')
    print("----- Выводим контакты определенного пользователя -----")
    friends_pb.show_contacts_user('qwe')
