# Класс контакта, который поддерживает:
# а. юзера, которому принадлежит контакт
# б. код страны
# в. номер телефона без кода страны

class Contact:
    def __init__(self, user, country_code, phone_num):
        self.user = user
        self.country_code = country_code
        self.phone_num = phone_num
