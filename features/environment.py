import configparser

import allure
from selenium import webdriver


def before_all(context):
    parser = configparser.ConfigParser()
    parser.read('./features/config/behave.ini')
    parser.read("behave.ini")
    context.config = parser

    context.driver = webdriver.Chrome("D:/Tools/chromedriver.exe")
    context.driver.implicitly_wait(context.config.get("settings", "wait"))


def before_scenario(context, scenario):
    context.driver.delete_all_cookies()


def after_step(context, step):
    if step.status == "failed":
        allure.attach(context.driver.get_screenshot_as_png(),
                      name="screenshot",
                      attachment_type=allure.attachment_type.PNG)


def after_all(context):
    context.driver.quit()
