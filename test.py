#test file

data_container = []

def add_data(data_list):
    name = input('Enter your first name: ')
    surname = input('Enter your last name: ')
    birth_date = input('Enter your date of birth: ')

    data_dict = dict()
    data_dict.setdefault('name',name)
    data_dict.setdefault('surname',surname)
    data_dict.setdefault('birthday',birth_date)

    data_list.append(data_dict)



print('''Please, choose from commands below: 
1 - add data
2 - list data''')
command_ = input('Please enter your command No.: ')

if command_ == '1':
    add_data(data_container)

