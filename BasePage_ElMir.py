import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import message_errors
import create_data_list
import random


options = webdriver.ChromeOptions()
options.add_argument('lang=ukr')
options.add_argument("start-maximized")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.implicitly_wait(10)
#driver.maximize_window()

driver.get("https://elmir.ua")


#Регистрация - проверка валидации полей
#Заходит на форму регистрации
def reg_button():
    button_enter = driver.find_element(By.ID, "autho")
    button_enter.click()
    time.sleep(1)
    button_registration = driver.find_element(By.CLASS_NAME, "lf-a.open-reg")
    time.sleep(1)
    button_registration.click()


def registration_account():
    field_name_registration = driver.find_element(By.ID, "rf-name")
    field_last_name_registration = driver.find_element(By.ID, "rf-surname")
    field_phone_registration = driver.find_element(By.ID, "rf-phone")
    field_email_registration = driver.find_element(By.ID, "rf-email")
    field_psw_registration = driver.find_element(By.ID, "rf-password")
    button_registration_submit = driver.find_element(By.CLASS_NAME, "mw-submit")


#В поле формы Y вводим значение Х, кликаем Зарегистрироваться и стираем Х
def reg_general_fields(x,y):
    field_name_registration = driver.find_element(By.ID, y)
    if x != None:
        field_name_registration.send_keys(x)
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, "#reg-form > form > button").click()
    try:
        field_name_clear = driver.find_element(By.ID, y)
        field_name_clear.clear()
    except:
        assert True


#Проверяем сообщение в попапе при некорректных данных
def reg_general_validation_incorrect(x,y,z):
    try:
        field_incorrect = driver.find_element(By.ID, y)
        error_message = field_incorrect.text
        if error_message in x:
            print(f"Test invalid {z} is PASSED")
            print(error_message)
        else:
            print(f"Test invalid {z} is FAILED")
            print(error_message)

    except:
        print("User has been FAILED")


def login_button():
    button_enter = driver.find_element(By.ID, "autho")
    time.sleep(1)
    button_enter.click()


def login_popup_email(x):
    field_phone_email = driver.find_element(By.ID, "lf-login")
    field_psw = driver.find_element(By.ID, "lf-password")
    field_phone_email.send_keys(x)
    time.sleep(1)
    field_psw.send_keys("29852985Kk")
    time.sleep(2)
    button_submit = driver.find_elements(By.CLASS_NAME, "mw-submit")
    for i in button_submit:
       if i.text == 'Войти' or i.text == 'Увійти':
            i.click()
    time.sleep(2)
    try:
        field_phone_email_clear = driver.find_element(By.ID, "lf-login")
        field_phone_email_clear.clear()
    except:
        assert True


def login_popup_psw(x):
    field_phone_email = driver.find_element(By.ID, "lf-login")
    field_psw = driver.find_element(By.ID, "lf-password")
    field_phone_email.send_keys("claudiajenrpm365@gmail.com")
    field_psw.send_keys(x)
    time.sleep(2)
    button_submit = driver.find_elements(By.CLASS_NAME, "mw-submit")
    for i in button_submit:
        if i.text == 'Войти' or i.text == 'Увійти':
            i.click()
    time.sleep(2)
    try:
        field_phone_email_clear = driver.find_element(By.ID, "lf-login")
        field_phone_email_clear.clear()
        field_psw_clear = driver.find_element(By.ID, "lf-password")
        field_psw_clear.clear()
    except:
        assert True


def logout_button():
    actions = webdriver.ActionChains(driver)
    hover = driver.find_element(By.CLASS_NAME, "user-name")
    actions.click(hover).perform()
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, "#autho > ul > li > ul > li:nth-child(9) > form > button").click()
    time.sleep(2)
    login_button()
    time.sleep(1)


def login_email_validation_incorrect():
    try:
        field_incorrect_phone_email = driver.find_element(By.CLASS_NAME, "mw_error_text")
        if field_incorrect_phone_email.text == "Укажите телефон или email" or "Вкажіть телефон або email":
            print("Test invalid email/phone is PASSED")
        else:
            print("Test invalid email/phone is FAILED")
    except:
        print("User has been FAILED")
        logout_button()


def login_psw_validation_incorrect():
    try:
        field_incorrect_psw = driver.find_element(By.CLASS_NAME, "mw_error_text")
        if field_incorrect_psw.text == "Неверные данные входа" or "Невірні дані входу":
            print("Test invalid psw is PASSED")
        else:
            print("Test invalid psw is FAILED")
    except:
        print("User has been FAILED")
        logout_button()




def basket(x):
    search_field = driver.find_element(By.ID, "q")
    search_field.send_keys(x)
    time.sleep(2)
    find_button = driver.find_element(By.ID, "find")
    find_button.click()
    time.sleep(2)
    item_name = driver.find_element(By.CLASS_NAME, "vit-name")
    text_item = item_name.text
    time.sleep(1)
    basket_button = driver.find_element(By.CLASS_NAME, "no-print.ready.btn")
    basket_button.click()
    time.sleep(1)
    create_order = driver.find_element(By.CSS_SELECTOR, "#basket-popup > form > div.b_side > div > div.buttons > a:nth-child(3)")
    create_order.click()
    time.sleep(1)
    item_name_basket = driver.find_elements(By.CLASS_NAME, "item-name")
    text_list = []
    for i in item_name_basket:
        text_list.append(i.get_attribute("text"))
    if text_item in text_list:
        print("Test add to the basket is PASSED")
        print(text_item)
    else:
        print("Test add to the basket is FAILED")






#login_button()
#login_popup_psw("29852985Kk")
basket("Poco")













#reg_button()    #Заходим на форму регистрации и запускаем валидацию полей (данные из эксель файла)
#for from_list in create_data_list.name_reg:
#    print(from_list)
#    reg_general_fields(from_list, "rf-name")
#    time.sleep(2)
#    reg_general_validation_incorrect(message_errors.name_error_messages, 'rf-err-name', "Name")

#for from_list in create_data_list.last_name_reg:
#    print(from_list)
#    reg_general_fields(from_list, "rf-surname")
#    time.sleep(2)
#    reg_general_validation_incorrect(message_errors.last_name_error_messages, 'rf-err-surname', "Last Name")

#for from_list in create_data_list.email_reg:
#    print(from_list)
#    reg_general_fields(from_list, "rf-email")
#    time.sleep(2)
#    reg_general_validation_incorrect(message_errors.email_error_messages, 'rf-err-email', "Email")

#for from_list in create_data_list.phone_reg:
#    print(from_list)
#    reg_general_fields(from_list, "rf-phone")
#    time.sleep(3)
#    reg_general_validation_incorrect(message_errors.phone_error_messages, 'rf-err-phone', "Phone")

#for from_list in create_data_list.psw_reg:
#    print(from_list)
#    reg_general_fields(from_list, "rf-password")
#    time.sleep(3)
#    reg_general_validation_incorrect(message_errors.psw_error_messages, 'rf-err-password', "Password")

#time.sleep(1)
#driver.find_element(By.CLASS_NAME, "mw-close.close-dialog").click()


#login_button()


#for log1 in create_data_list.log_incorrect_email:
#    login_popup_email(log1)
#    login_email_validation_incorrect()
#    time.sleep(2)

#for log1 in create_data_list.log_incorrect_psw:
#    login_popup_psw(log1)
#    login_psw_validation_incorrect()
#    time.sleep(2)







driver.quit()

