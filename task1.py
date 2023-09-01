from tel_book import add_new_data, find_data, print_data, delete_data, change_data

print ("Добро пожаловать в телефонный справочник")

while True:
    print ()
    print ("Чтобы добавить запись - нажмите 1")
    print ("чтобы найти запись - нажмите 2")
    print ("чтобы вывести все данные на экран - нажмите 3")
    print ("чтобы изменить строку из записей - нажмите 4")
    print ("чтобы удалить строку из записей - нажмите 5")
    string = int (input ("чтобы окончить работу с программой - нажмите 6: "))
    print ()
    list1 = new_data = []
    if string == 1:
        flag = True
        string1 = 0
        while flag == True:
            line = input ("Ведите Фамилию Имя Отчество и Телефон абонента через пробел: ")
            print (list1)
            new_data.append (line)
            print (new_data)
            string1 = int (input("Если желаете добавить еще запись нажмите 1, иначе 0:"))
            if string1 == 0:
                flag = False
                print (add_new_data(new_data))
    elif string == 2:
        print ("ищем")
        string1 = (input("Введите данные для поиска:"))
        find_data (string1)
    elif string == 3:
        print ("")
        print_data()
    elif string == 4:
        print ("")
        line_for_change = int(input("Введите номер строки записи для изменения: "))
        new_data = input("Введите новую строку: ")
        change_data (line_for_change, new_data)
    elif string == 5:
        print ("")
        line_for_delete = int(input("Введите номер строки записи для удаления: "))
        delete_data (line_for_delete)
    elif string == 6:
        break
    else:
        print ("Такой команды не существует")