import random
import string


if __name__ == "__main__":
    chars = string.punctuation + string.digits + string.ascii_letters
    chars = list(chars)
    key = chars.copy()
    random.shuffle(key)

    message = input("Enter a message to encrypt: ")
    crypted_message = ""

    for letter in message:
        index = chars.index(letter)
        crypted_message += key[index]

    print(crypted_message)
