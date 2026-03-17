if __name__ == "__main__":
    email = input("Enter your email: ")
    index = email.index("@")

    username = email[0:index]
    domain = email[index + 1:]

    print(f"Your email is {username} and domain is {domain}")