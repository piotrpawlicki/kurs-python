
email_list = [
    "example1@example.com",
    "example2@example.com",
    "example3@example.com",
    "example4@example.com",
    "example5@example.com",
    "example6@example.com",
    "example7@example.com",
    "example8@example.com",
    "example9@example.com",
    "example10@example.com",
    "example11@example.com",
    "example12@example.com",
    "example13@example.com",
    "example14@example.com",
    "example15@example.com",
    "example16@example.com",
    "example17@example.com",
    "example18@example.com",
    "example19@example.com",
    "example20@example.com"
]

def get_email():
    email = ''
    while True:
        email = input('Podaj email: ')
        if '@' in email:
            break
    return email

user_email = get_email()

def check_email(user_email, email_list):
    if user_email in email_list:
        return True
    return False

def main():
    print(check_email(user_email, email_list))

if __name__== '__main__':
    main()

