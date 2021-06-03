from selenium.webdriver.common.by import By


class HomePage():
    MY_ACCOUNT_BTN_PL =(By.ID, 'menu-item-290299')

    MY_ACCOUNT_BTN_DE = (By.ID, 'menu-item-279154')
    MY_ACCOUNT_BTN_SK = (By.ID, 'menu-item-279021')
    MY_ACCOUNT_BTN_CS = (By.ID, 'menu-item-284071')
    MY_ACCOUNT_BTN_IT = (By.ID, 'menu-item-278684')

    SIGN_IN_BTN_PL = (By.XPATH, '//p//a[@href="https://vapefully.com/pl/moje-konto/"]')

    SIGN_IN_BTN_DE = (By.XPATH, '//p//a[@hhref="https://woocommerce-button button woocommerce-form-login__submitvapefully.com/de/mein-konto/"]')
    SIGN_IN_BTN_SK = (By.XPATH, '//p//a[@href="https://vapefully.com/sk/moj-ucet/"]')
    SIGN_IN_BTN_CS = (By.XPATH, '//p//a[@href="https://vapefully.com/cs/muj-ucet/"]')
    SIGN_IN_BTN_IT = (By.XPATH, '//p//a[@href="https://vapefully.com/it/il-mio-profilo/"]')



    # COM
    VAPORYZATORY_BTM = (By.XPATH, '//body/div[@id="page"]/div[3]/div[1]/nav[1]/div[1]/div[2]/ul[1]/li[1]/a[1]')
    INPUT_NAME_BP = (By.ID, 'username')
    CART_IN = (By.XPATH, '//div[@class="cart-click"]')
    IMPUT_PASS_BP = (By.ID, 'password')
    ERROR_MESSAGES_SPAN = (By.CSS_SELECTOR,"div.col-full div.woocommerce ul.woocommerce-error > li:nth-child(1)")
    SIGN_IN_BTN_COM = (By.XPATH, '//button[contains(text(),"Login")]')
    MY_ACCOUNT_BTN_COM = (By.XPATH, '//li[@id="menu-item-285005"]')
    LOGIN_BLOCK = (By.LINK_TEXT, "My account")
    SIGN_UP_BTN_COM = (By.LINK_TEXT, "sign up")



class LoginPageLocators():

    LOGIN_BTN= (By.XPATH, '//button[@class="woocommerce-button button woocommerce-form-login__submit"]')
    NAME_INPUT = (By.ID, 'reg_email')
    PASSWORD_INPUT = (By.ID, 'password')

class RegistrationPageLocators():
    REG_EMAIL = (By.ID, 'reg_email')
    REG_PASS = (By.ID, 'reg_password')
    REG_LOG_IN = (By.XPATH, '//button[@class="woocommerce-Button woocommerce-button button woocommerce-form-register__submit"]')
class SignUpPage():



    # COM
    SIGN_UP_CHECK= (By.CLASS_NAME, "entry-title")
    SUP_EMAIL = (By.NAME, "email")
    SUP_PASS = (By.CSS_SELECTOR, "#reg_password")
    SUP_REG_BTN =(By.NAME, "register")
    SUP_REG_BTN_DISABLED =(By.CSS_SELECTOR, 'p.woocommerce-form-row.form-row:nth-child(4) > button.woocommerce-Button.woocommerce-button.button.woocommerce-form-register__submit.disabled:nth-child(3)')
    PASSWORD_STRENGHT = (By.XPATH,"//span[@class='password-input']//div")
    ERROR_ALREADY_EXIST =(By.CSS_SELECTOR, "div.woocommerce ul.woocommerce-error > li:nth-child(1)")

class PopUp():
    POP_UP_CLOSE = (By.XPATH, '//div//button[@class="needsclick DismissButton__closeButtonImage-spg526-0 fMcTYf kl-private-reset-css-Xuajs1"]')

class ProductPages():
    SEARSH_FIELD = (By.CSS_SELECTOR, "#woocommerce-product-search-field-0")
    AUTOSUGGESTION_FIELD = (By.CLASS_NAME, "autocomplete-suggestion")
    VARIANTS_OPEN = (By.CSS_SELECTOR, "#variant")
    VARIANTS_SELLECT =("//option[@class='attached enabled']")
    AVAILABILITY = (By.CSS_SELECTOR, "div.woocommerce-variation.single_variation div.woocommerce-variation-availability > p")
    ADD_TO_CART = (By.CSS_SELECTOR, ".woocommerce-variation-add-to-cart-enabled > button.single_add_to_cart_button.button.alt:nth-child(3)")
    ADD_TO_CARTV = ( By.XPATH, "//button[contains(text(),'Add to basket')]")
    CART_BTN = (By.LINK_TEXT, "View Cart")
class CartPages():
    PRODUCT_NAME = (By.CSS_SELECTOR, ".woocommerce-cart-form__cart-item.cart_item:nth-child(1) td.product-name > a:nth-child(1)")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "tr.cart-subtotal > td:nth-child(2)")
    SHIPPING_METHOD = (By.CSS_SELECTOR, ".woocommerce-shipping-methods li:nth-child(1) > label:nth-child(2)")
    TOTAL_PRICE =(By.CSS_SELECTOR, ".order-total td:nth-child(2) strong:nth-child(1) > span.woocommerce-Price-amount.amount")
    CHECKOUT_BTN = (By.LINK_TEXT, "Proceed to checkout")
class CheckOutPages():
    EMAIL_FIELD = (By.ID, "billing_email")
    NAME_FIELD = (By.ID, "billing_first_name")
    LASTNAME_FIELD =(By.ID, "billing_last_name")
    COUNTRY_FIELD = (By.ID, "select2-billing_country-container")
    COUNTRY_SEARCH =(By.CLASS_NAME,"select2-search__field")
    ADDRESS_FIELD = (By.ID, "billing_address_1")
    POSTCODE_FIELD =(By.ID, "billing_postcode")
    CITY_FIELD = (By.ID, "billing_city")
    PHONE_FIELD = (By.ID, "billing_phone")
    IHAVER_BOX = (By.CSS_SELECTOR, ".woocommerce-form__label-for-checkbox.checkbox:nth-child(1) > span.woocommerce-terms-and-conditions-checkbox-text")
    PLACE_ORDER_BTN =(By.ID, "place_order")
    OUTSIDE = (By.XPATH,"//h3[contains(text(),'Billing details')]")
