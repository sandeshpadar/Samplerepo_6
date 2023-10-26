# how to calculate your age

from datetime import datetime
birthdate_str = input('Enter your birthdate(YYYY/MM/DD):- ')
birthdate = datetime.strptime(birthdate_str, '%Y/%m/%d')
current_date = datetime.today()
age = current_date.year - birthdate.year
print(f'The age is {age} years old')
