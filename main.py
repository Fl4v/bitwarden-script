import csv
import re


def main():
    url_rejex = '[-a-zA-Z0-9@:%._\\+~#=]{1,256}\\.[a-zA-Z0-9()]{1,6}\\b([-a-zA-Z0-9()@:%_\\+.~#?&//=]*)'
    new_passwords = []

    with open('passwords.csv', 'r') as csv_file:
        passwords = csv.DictReader(csv_file)

        for password in passwords:
            if re.fullmatch(url_rejex, password['name']):
                password['login_uri'] = password['name'].lower()  # Copy name to uri
                name = password['name'].split('.')[0]  # Extract name
                password['name'] = name.lower()
                new_passwords.append(password)
            else:
                password['name'] = password['name'].lower()
                new_passwords.append(password)

    with open('passwords_new.csv', 'w') as csv_file:
        fieldnames = new_passwords[0].keys()
        writer = csv.DictWriter(csv_file, fieldnames)

        writer.writeheader()
        writer.writerows(new_passwords)


if __name__ == '__main__':
    main()
