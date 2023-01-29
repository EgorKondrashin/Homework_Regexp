import re
import csv

with open('phonebook_raw.csv', encoding='utf-8') as f:
    rows = csv.reader(f, delimiter=',')
    contacts_list = list(rows)
    contacts_list.pop()

for contacts in contacts_list:
    if len(contacts[0].split()) > 2:
        contacts[1] = contacts[0].split()[1]
        contacts[2] = contacts[0].split()[2]
        contacts[0] = contacts[0].split()[0]
    elif len(contacts[1].split()) > 1:
        contacts[2] = contacts[1].split()[1]
        contacts[1] = contacts[1].split()[0]
    elif len(contacts[0].split()) == 2:
        contacts[1] = contacts[0].split()[1]
        contacts[0] = contacts[0].split()[0]

for contact_1 in contacts_list:
    for contact_2 in contacts_list[1:]:
        if contact_1[4] == '':
            if contact_1[0] == contact_2[0] and contact_1[1] == contact_2[1] and contact_2[4] != '':
                contact_1[4] = contact_2[4]
                contacts_list.remove(contact_2)
        if contact_1[6] == '':
            if contact_1[0] == contact_2[0] and contact_1[1] == contact_2[1] and contact_2[6] != '':
                contact_1[6] = contact_2[6]
                contacts_list.remove(contact_2)

new_contacts_list = []

pattern = re.compile(r'([А-Я]\w+)\,([А-Я]\w+)\,([А-Я]\w+)\,([А-Я]\w+)\,?(\D+)?\,\+?(\d{1})\s?\W?(\d{3})'
                     r'\W*(\d{3})\W?(\d{2})\W?(\d{2})\W*([а-я.]+)?\W?(\d{4})?\)?\,(\S+)?')

for contact in contacts_list:
    result = pattern.sub(r'\1,\2,\3,\4,\5,+7(\7)\8-\9-\10 \11\12,\13', str(','.join(contact)))
    new_contacts_list.append(result)

with open('phonebook.csv', 'w', newline='') as f:
    datawriter = csv.writer(f, delimiter='\n')
    datawriter.writerows([new_contacts_list])
