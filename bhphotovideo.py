from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from time import sleep

driver = Chrome(executable_path='/opt/WebDriver/bin/chromedriver')
# test link
driver.get("https://www.bhphotovideo.com/c/product/1561250-REG/fractal_design_fd_ca_mesh_c_bko_meshify_c_atx_matx_itx_blackout.html")
sleep(2)
driver.find_element_by_xpath("//button[@data-selenium = 'addToCartButton']").click()
sleep(2)
viewCartBtn = None
while viewCartBtn is None:
    try:
        viewCartBtn = driver.find_element_by_xpath("//a[@data-selenium = 'itemLayerViewCartBtn']")
    except:
        pass
viewCartBtn.click()
# driver.execute_script("window.open('');")
# sleep(0.5)
# # Switch to the new window
# driver.switch_to.window(driver.window_handles[1])
# driver.get("https://www.bhphotovideo.com/find/cart.jsp")
sleep(2)
checkoutBtn = None
while checkoutBtn is None:
    try:
        checkoutBtn = driver.find_element_by_xpath("//input[@data-selenium = 'checkoutLogin']")
    except:
        pass
checkoutBtn.click()

sleep(5)

checkoutNoLoginBtn = None
while checkoutNoLoginBtn is None:
    try:
        checkoutNoLoginBtn = driver.find_element_by_xpath("//input[@data-selenium = 'checkoutNoLogin']")
    except:
        pass

driver.find_element_by_xpath("//input[@data-selenium = 'emailAddress']").send_keys()
driver.find_element_by_xpath("//input[@data-selenium = 'password']").send_keys()
sleep(0.5)
checkoutNoLoginBtn.click()
