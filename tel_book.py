def add_new_data (recs):
    with open ('base.txt', 'a', encoding = 'utf-8') as data:
        for i, item in enumerate (recs):
            data.write (item + '\n')
    message = "запись создана"
    return message


def find_data (key_str):
    flag = False
    with open ('base.txt', 'r', encoding = 'utf-8') as data:
        for line in data:
            if key_str in line:
                print(line)
                flag = True
    if not flag:
        print ("Данные по Вашим параметрам не найдены")


def print_data ():
    id = 0
    with open ('base.txt', 'r', encoding = 'utf-8') as data:
        for line in data:
            id += 1
            print(id, line)
    message = "Данные выведены на экран"
    return message


def delete_data (num_of_line_for_del):
    temp_data = []
    with open ('base.txt', 'r', encoding = 'utf-8') as data:
        temp_data = data.readlines()
    temp_data.pop(num_of_line_for_del - 1)
    with open ('base.txt', 'w', encoding = 'utf-8') as data:
        for i, item in enumerate (temp_data):
            data.write (item)
    with open ('base.txt', 'r', encoding = 'utf-8') as data:
        for line in data:
            print(line)
    message = "запись создана"
    return message