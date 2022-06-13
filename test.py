import csv
from random_uk_bank_account import GenerateUkBankAccount


sort_code = '040004'

f = open('test.csv', 'w')
writer = csv.writer(f)
writer.writerow(['sortCode', 'accountNumber'])


for _ in range(1000):
    print(_)
    account = GenerateUkBankAccount().generate_for_sort_code(sort_code)
    writer.writerow([account.sort_code, account.account_numbers[0]])


f.close()