import csv
import random
import string
import ccard
from random_uk_bank_account import GenerateUkBankAccount


sort_code = '040004'

f = open('test.csv', 'w', newline='')
writer = csv.writer(f)
writer.writerow(['sortCode', 'accountNumber', 'email', 'phone', 'ccard'])


for _ in range(377125):
    print(_)
    account = GenerateUkBankAccount().generate_for_sort_code(sort_code)
    letters = string.ascii_lowercase
    start = ''.join(random.choice(letters) for i in range(10))
    
    phone = '44075' + str(_).zfill(6) + '22'
    if (_ % 5) == 0:
        phone = '44020' + str(_).zfill(6) + '22'
        
    writer.writerow([account.sort_code, account.account_numbers[0], start + '@legatio.test', phone, ccard.visa()])


f.close()