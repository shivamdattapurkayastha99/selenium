from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
# driver.get("https://www.google.com")
# print(driver.title)
# print(driver.current_url)
# print(driver.page_source)
# driver.fullscreen_window()
# driver.maximize_window()
# driver.set_window_size(100,400)
# driver.set_window_rect(x=200,y=200,width=200,height=200)
# driver.close()
# ===========================================================
# search_box=driver.find_element_by_name('q')
# search_box.send_keys('made easy test series')
# search_box.submit()
# ============================================================
# driver.get("https://demoqa.com/text-box")
# input_field1=driver.find_element_by_id('userName')
# input_field2=driver.find_element_by_id('userEmail')
# input_field3=driver.find_element_by_id('currentAddress')
# input_field4=driver.find_element_by_id('permanentAddress')
# input_field1.send_keys("Shivam Datta")
# input_field2.send_keys("x@gmail.com")
# input_field3.send_keys("xyz")
# input_field4.send_keys("xyz")
# btn_submit=driver.find_element_by_id('submit')
# btn_submit.click()
# ========================================================================
# driver.get("https://www.google.com")
# search_box=driver.find_element_by_name('q')
# search_box.send_keys('selenium web driver')
# search_box.submit()
# driver.back()
# print(driver.title)
# driver.forward()
# driver.refresh()
# ============================================================================
# driver.get("https://www.google.com")
# search_box=driver.find_element_by_name('q')
# print(search_box.is_displayed())
# print(search_box.is_enabled())
# print(search_box.is_selected())
# =====================================================================
# driver.get("https://demoqa.com/selectable")
# one=driver.find_element_by_xpath('//*[@id="verticalListContainer"]/li[1]')
# two=driver.find_element_by_xpath('//*[@id="verticalListContainer"]/li[2]')
# actions=ActionChains(driver)
# actions.click(one)
# actions.click(two)
# =================================
# driver.get("F:/selenium full/index.html")
# three=driver.find_element_by_name("three")
# l=three.location
# s=three.size
# print(f"Coordinates are {l} and size is {s}")
# actions=ActionChains(driver)
# actions.move_by_offset(200,200)
# actions.click().perform()
# ========================================
# driver.get("F:/selenium full/index.html")
# three=driver.find_element_by_name('three')
# one=driver.find_element_by_name('one')
# two=driver.find_element_by_name('two')
# actions=ActionChains(driver)
# actions.click(one)
# actions.click(two)
# actions.click(three)
# ============================================
# driver.get("F:/selenium full/2.html")
# three=driver.find_element_by_name('three')
# one=driver.find_element_by_name('one')
# two=driver.find_element_by_name('two')
# actions=ActionChains(driver)
# actions.click_and_hold(one)
# actions.release(two)
# actions.perform()
# ==================================
# driver.get("https://demoqa.com/droppable")
# dragged=driver.find_element_by_id('draggable')
# dropped=driver.find_element_by_id('droppable')

# actions=ActionChains(driver)
# actions.click_and_hold(dragged)
# actions.release(dropped)
# actions.perform()
# ================================
# driver.get("https://demoqa.com/droppable")
# src=driver.find_element_by_id('draggable')
# target=driver.find_element_by_id('droppable')

# actions=ActionChains(driver)
# actions.drag_and_drop(src,target)
# actions.perform()
# ===================================
# driver.implicitly_wait(10)
# driver.get("https://demoqa.com/login")
# u_name=driver.find_element_by_id('userName')
# password=driver.find_element_by_id('password')
# btn_login=driver.find_element_by_id('login')
# u_name.send_keys('shivam')
# password.send_keys('password')
# btn_login.click()
# try:
#     element=WebDriverWait(driver,10).until(EC.presence_of_element_located((By.ID,"searchBox")))
#     element.send_keys('Learn Python')
# finally:
#     driver.close()
# ==========================================
driver.get("https://www.google.com")
mycookies=driver.get_cookies()
print(len(mycookies))
cookie={'name':'cookiename','value':'cookievalue'}
driver.add_cookie(cookie)
mycookies=driver.get_cookies()
print(len(mycookies))
print(mycookies)
driver.delete_cookie('cookiename')
mycookies=driver.get_cookies()
print(len(mycookies))
print(mycookies)