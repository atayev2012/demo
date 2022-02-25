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


def list_all(data_list):
    for data in data_list:
        print(f'First name: {data["name"]:10} Last name: {data["surname"]:10} Date of birth: {data["birthday"]}')

print('''Please, choose from commands below: 
1 - add data
2 - list data''')
command_ = input('Please enter your command No.: ')

if command_ == '1':
    add_data(data_container)
elif command_ == '2':
    list_all(data_container)
else:
    print('Program was terminated by an unknown command')
