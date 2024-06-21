import random
import string


def generate_password(length=8):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password


length = int(input("Введите длину пароля: "))
password = generate_password(length)
print("Сгенерированный пароль:", password)
