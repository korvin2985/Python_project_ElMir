from selenium.webdriver.common.by import By



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