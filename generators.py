import random


class BadPasswordGenerator:
    """
    Генератор плохих=небезопасных паролей
    """
    def __init__(self):
        """Инициализация генератора"""
        self.i = 0
        with open('passwords.txt') as f:
            passwords_data = f.read()
        self.passwords = passwords_data.split('\n')

    def next(self):
        """Получение следущего пароля"""
        password = self.passwords[self.i]
        self.i += 1
        return password


# пример использования класса
# generator = BadPasswordGenerator()
# print(generator.next())
# print(generator.next())


class GoodPasswordGenerator:
    """
    Генератор безопасных паролей
    """
    def __init__(self):
        """Инициализация генератора"""
        self.alphabet = '1234567890' \
                        'qwertyuiopasdfghjklzxcvbnm' \
                        'QWERTYUIOPASDFGHJKLZXCVBNM' \
                        '!@#$%^&*()_+'

    def next(self, length=10):
        """Получение следущего пароля"""
        password = ''
        for i in range(length):
            c = random.choice(self.alphabet)
            password += c
        return password


# generator2 = GoodPasswordGenerator()
# print(generator2.next())
# print(generator2.next())
