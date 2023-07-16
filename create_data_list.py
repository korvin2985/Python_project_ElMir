import openpyxl


#Открытие эксель файла и задание текущей страницы
_xlsx_book = openpyxl.load_workbook("TestData.xlsx")
my_profile_data = _xlsx_book.active

start = ord('A')
i = 0
letter_symbol = chr(start) + '1'

#Создание списков данных из эксель файла
name_reg = []
last_name_reg = []
phone_reg = []
email_reg = []
psw_reg = []
log_incorrect_email = []
log_incorrect_psw = []

#Проход по всем столбцам и считывание названия столбца
while my_profile_data[letter_symbol].value != None:
    a = my_profile_data[letter_symbol].value

#Наполнение массива данными из эксель файла
    if a == "Name_Registration":
        row = 2
        name_reg.append(my_profile_data[chr(start+i) + str(row)].value)
        from_list = name_reg[0]
        while from_list != "***":
            row = row + 1
            if my_profile_data[chr(start+i) + str(row)].value != "***":
                name_reg.append(my_profile_data[chr(start+i) + str(row)].value)
            else:
                from_list = "***"

    if a == "Last_Name_Registration":
        row = 2
        last_name_reg.append(my_profile_data[chr(start+i) + str(row)].value)
        from_list = last_name_reg[0]
        while from_list != "***":
            row = row + 1
            if my_profile_data[chr(start+i) + str(row)].value != "***":
                last_name_reg.append(my_profile_data[chr(start+i) + str(row)].value)
            else:
                from_list = "***"

    if a == "Phone_Registration":
        row = 2
        phone_reg.append(my_profile_data[chr(start+i) + str(row)].value)
        from_list = phone_reg[0]
        while from_list != "***":
            row = row + 1
            if my_profile_data[chr(start+i) + str(row)].value != "***":
                phone_reg.append(my_profile_data[chr(start+i) + str(row)].value)
            else:
                from_list = "***"

    if a == "Email_Registration":
        row = 2
        email_reg.append(my_profile_data[chr(start+i) + str(row)].value)
        from_list = email_reg[0]
        while from_list != "***":
            row = row + 1
            if my_profile_data[chr(start+i) + str(row)].value != "***":
                email_reg.append(my_profile_data[chr(start+i) + str(row)].value)
            else:
                from_list = "***"

    if a == "PSW_Registration":
        row = 2
        psw_reg.append(my_profile_data[chr(start+i) + str(row)].value)
        from_list = psw_reg[0]
        while from_list != "***":
            row = row + 1
            if my_profile_data[chr(start+i) + str(row)].value != "***":
                psw_reg.append(my_profile_data[chr(start+i) + str(row)].value)
            else:
                from_list = "***"

    if a == "Email/Phone":
        row = 2
        log_incorrect_email.append(my_profile_data[chr(start+i) + str(row)].value)
        from_list = log_incorrect_email[0]
        while from_list != "***":
            row = row + 1
            if my_profile_data[chr(start+i) + str(row)].value != "***":
                log_incorrect_email.append(my_profile_data[chr(start+i) + str(row)].value)
            else:
                from_list = "***"

    if a == "PSW":
        row = 2
        log_incorrect_psw.append(my_profile_data[chr(start+i) + str(row)].value)
        from_list = log_incorrect_psw[0]
        while from_list != "***":
            row = row + 1
            if my_profile_data[chr(start+i) + str(row)].value != "***":
                log_incorrect_psw.append(my_profile_data[chr(start+i) + str(row)].value)
            else:
                from_list = "***"

    i = i + 1
    letter_symbol = chr(start + i) + '1'

