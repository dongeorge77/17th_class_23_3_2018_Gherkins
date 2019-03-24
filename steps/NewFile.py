from behave import *
from selenium import webdriver

use_step_matcher("re")


@given("User present with loginpage")
def launch_browser(context):
    global driver
    driver=webdriver.Chrome()
    driver.maximize_window()
    driver.get("http://localhost/login.do")

@when("Enter username")
def enter_un(context):
    driver.find_element_by_id("username").send_keys("admin")

@when("Enter password")
def enter_pw(context):
    driver.find_element_by_name("pwd").send_keys("manager")

@when("Click on login")
def login_btn(context):
    driver.find_element_by_xpath("//*[text()='Login ']").click()

@then("Validate homepage")
def validate_hmpg(context):
