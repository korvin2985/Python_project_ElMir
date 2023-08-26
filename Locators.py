from selenium.webdriver.common.by import By


#Форма регистрации
class Registration():
    button_registration_locator = (By.CLASS_NAME, "lf-a.open-reg")
    button_enter_locator = (By.ID, "autho")
    button_registration_input_data_locator = (By.CSS_SELECTOR, "#reg-form > form > button")

    name_error_message_locator = (By.ID, 'rf-err-name')
    surname_error_message_locator = (By.ID, 'rf-err-surname')
    email_error_message_locator = (By.ID, 'rf-err-email')
    phone_error_message_locator = (By.ID, 'rf-err-phone')
    password_error_message_locator = (By.ID, 'rf-err-password')

    field_name_registration_locator = (By.ID, "rf-name")
    field_last_name_registration_locator = (By.ID, "rf-surname")
    field_phone_registration_locator = (By.ID, "rf-phone")
    field_email_registration_locator = (By.ID, "rf-email")
    field_psw_registration_locator = (By.ID, "rf-password")

    button_registration_submit_locator = (By.CLASS_NAME, "mw-submit")


#Форма логина
class FormLogin():
    field_phone_email_locator = (By.ID, "lf-login")
    field_psw_locator = (By.ID, "lf-password")
    hover_locator = (By.CLASS_NAME, "user-name")
    logout_button_from_dropdown_locator = (By.CSS_SELECTOR, "#autho > ul > li > ul > li:nth-child(9) > form > button")
    field_incorrect_psw_locator = (By.CLASS_NAME, "mw_error_text")
    field_incorrect_phone_email_locator = (By.CLASS_NAME, "mw_error_text")


#Модули интернет магазина
class Modules():
    superciny_locator = (By.ID, 'out-link-4')
    configurator_locator = (By.ID, 'out-link-5')
    energy_locator = (By.ID, 'tab-21')
    kompyterna_tehnika_komplectyuchi_locator = (By.ID, 'tab-1')
    pobytova_tehnica_locator = (By.ID, 'tab-6')
    mobilnuy_zviazok_locator = (By.ID, 'tab-5')
    portatuvna_tehnika_locator = (By.ID, 'tab-2')
    tovary_dliy_geymerov_locator = (By.ID, 'tab-20')
    televizory_ta_rozvagy_locator = (By.ID, 'tab-4')
    audio_locator = (By.ID, 'tab-22')
    foto_i_videotehnika_locator = (By.ID, 'tab-16')
    vse_dliy_oficy_locator = (By.ID, 'tab-3')
    avto_locator = (By.ID, 'tab-7')
    dutyachiy_svit_locator = (By.ID, 'tab-8')
    santechnika_ta_remont_locator = (By.ID, 'tab-9')
    vse_dliy_domy_locator = (By.ID, 'tab-14')
    dacha_sad_ogorod_locator = (By.ID, 'tab-19')
    sport_vidpochinok_ta_turizm_locator = (By.ID, 'tab-11')
    suveniry_chasy_symki_locator = (By.ID, 'tab-18')
    krasota_ta_zdorovie_locator = (By.ID, 'tab-17')
    zootovary_locator = (By.ID, 'tab-13')
    apple_locator = (By.ID, 'tab-12')
    poslygu_locator = (By.ID, 'tab-15')
    ychinka_locator = (By.ID, 'out-link-3')

    catalog_items_locator = (By.CLASS_NAME, 'tab')


#Добавление в корзину
class TheBasket():
    search_field_locator = (By.ID, "q")
    find_button_locator = (By.ID, "find")
    item_name_locator = (By.CLASS_NAME, "vit-name")
    basket_button_locator = (By.CLASS_NAME, "no-print.ready.btn")
    create_order_locator = (By.CSS_SELECTOR, "#basket-popup > form > div.b_side > div > div.buttons > a:nth-child(3)")
    item_name_basket_locator = (By.CLASS_NAME, "item-name")