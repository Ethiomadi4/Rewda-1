import time

from selenium import webdriver

from src.pages.landingpage import LandingPage
from src.pages.registrationpage import RegPage
from src.pages.logingpage import LoginPage
from src.pages.product import ProductPage
from src.pages.cartpage import CartPage
from src.pages.orderpage import OrderPage

driver = webdriver.Firefox()
driver.get("http://shop.icraftsoft.net:8095/")
driver.maximize_window()

#landingpage
lp = LandingPage(driver)
lp.click_login()
time.sleep(3)


# registration
Reg = RegPage(driver)
Reg.getUsername()
time.sleep(3)
Reg.getEmail()
time.sleep(3)
Reg.getButton()
time.sleep(5)
Reg.get_login()
time.sleep(3)

#Login page
driver.get("http://shop.icraftsoft.net:8095/")
lg = LoginPage(driver)
lg.login_textbox()
time.sleep(2)
lg.click_login()
time.sleep(2)
lg.click_logout()
time.sleep(2)
lg.click_home()
time.sleep(2)
lg.login_textbox2()
time.sleep(2)
lg.login_again()
time.sleep(2)

#productpage
pro = ProductPage(driver)
pro.search_box()
time.sleep(4)
pro.Quick_view_product()
time.sleep(4)
pro.select_Product1()
time.sleep(4)
pro.Add_to_Cart()
time.sleep(4)
pro.second_cart()
time.sleep(4)

#cartpage
cr = CartPage(driver)
time.sleep(5)
cr.click_on_cart()
time.sleep(5)

#orderpage
A = OrderPage(driver)
time.sleep(3)
A.remove_items()
time.sleep(3)
A.continue_shop()
time.sleep(3)
A.click_on_cart()
time.sleep(3)
A.click_on_Buy_now()
time.sleep(3)
A.click_on_home()
time.sleep(3)

