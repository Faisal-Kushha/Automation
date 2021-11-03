import re

phone_numbers = []
numbers_pattern = re.compile(
    r'(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})')
# (\d{3}) \W* (\d{3}) \W* (\d{4}) \W* (\d*)
# (\w{3})\w{3}-\w{4}
with open('assets/potential-contacts.txt', 'r') as file:
    files = file.readlines()
    for i in files:
        if numbers_pattern.search(i):
            number = numbers_pattern.search(i).group()
            if '+' in number:
                number = number.replace('+', '00')
            if '(' in number:
                number = number.strip('(')
            if ')' in number:
                number = number.replace(')', '-')
            if '.' in number:
                number = number.replace('.', '-')
            if len(number) == 10:
                number = f'{number[:3]}-{number[3:5]}-{number[5:]}'
            if len(number) == 8:
                number = number.strip('-')
                number = '206' + '-'+number
            # if len(number) == 7:
            #     number = f'206-{number}'
            # if '-' in number and len(number) == 10:
            #     number = number.strip('-')
            #     number = f'{number[:3]}-{number[3:5]}-{number[5:]}'

            phone_numbers.append(number)
            phone_numbers = sorted(phone_numbers)
print(len(phone_numbers))
with open('assets/phone_numbers.txt', 'w+') as file:
    files = file.readlines()
    for i in phone_numbers:
        file.write(f'{i}\n')


emails_list = []
email_pattern = re.compile(r"\w+.\w+@\w+.\w+.(com|net|org|info|biz)")
with open('assets/potential-contacts.txt', 'r') as file:
    files = file.readlines()
    for i in files:
        if email_pattern.search(i):
            email = email_pattern.search(i).group()
            emails_list.append(email)
            emails_list = sorted(emails_list)
print(len(emails_list))
with open('assets/emails.txt', 'w+') as file:
    files = file.readlines()
    for i in emails_list:
        file.write(f'{str(i)}\n')
