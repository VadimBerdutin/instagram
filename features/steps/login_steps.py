import time

from behave import *

from features.pages.login_page import LoginPage


@given('I open login page')
def step_impl(context):
    context.driver.get("https://www.instagram.com/accounts/login/")


@when('I type "{username}" in username field')
def step_impl(context, username):
    login_page = LoginPage(context.driver)
    login_page.enter_username(username)


@when('I type "{password}" in password field')
def step_impl(context, password):
    login_page = LoginPage(context.driver)
    login_page.enter_password(password)


@when('I click login button')
def step_impl(context):
    login_page = LoginPage(context.driver)
    login_page.click_login()
    time.sleep(5)


@given('I log in')
def step_impl(context):
    context.driver.get("https://www.instagram.com/accounts/login/")
    login_page = LoginPage(context.driver)
    login_page.enter_username(context.config.get("user", "username"))
    login_page.enter_password(context.config.get("user", "password"))
    login_page.click_login()
