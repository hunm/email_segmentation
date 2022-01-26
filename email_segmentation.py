import re


def valid_email(email):
    return bool(re.search(r"^[\w\.\+\-]+\@[\w]+\.[a-z]{2,3}$", email))


def segment_email(email):
    print("Email:", email)
    print("Username:", email[0:email.find('@')])
    print("Domen:", email[email.find('@')+1:email[email.find('@')].find('.')-2])


def main():
    print("Input your email:")
    email = input()
    if valid_email(email):
        segment_email(email)
    else:
        print("Invalid email")


if __name__ == "__main__":
    main()