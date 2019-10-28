import time

from selenium import webdriver
from features.pages.login_page import LoginPage
from features.pages.main_page import MainPage
from features.pages.search_results_page import SearchResultsPage

driver = webdriver.Chrome("D:/Tools/chromedriver.exe")
driver.implicitly_wait(5)

driver.get("https://www.instagram.com/accounts/login/")

login_page = LoginPage(driver)
login_page.enter_username("pyautomation")
login_page.enter_password("Ab123456789!")
login_page.click_login()

main_page = MainPage(driver)
main_page.click_not_now_button()
main_page.type_in_search_field("#fitness")
main_page.click_result_with_text("#fitness")
time.sleep(3)
search_results_page = SearchResultsPage(driver)
# assert "Follow" in search_results_page.get_follow_button_text()
search_results_page.get_button_text("Follow")

driver.quit()
