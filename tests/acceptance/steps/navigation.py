from behave import *
from selenium import webdriver
from tests.acceptance import steps


use_step_matcher('re')


@given('I am on the homepage')
def step_impl(context):
    context.driver = webdriver.Chrome(chrome_options=webdriver.ChromeOptions(), executable_path=r"C:\Users\isaia\PycharmProjects\acceptance_testing\chromedriver.exe")
    context.driver.get('http://127.0.0.1:5000')

@given('I am on the blog page')
def step_impl(context):
    context.driver = webdriver.Chrome(chrome_options=webdriver.ChromeOptions(), executable_path=r"C:\Users\isaia\PycharmProjects\acceptance_testing\chromedriver.exe")
    context.driver.get('http://127.0.0.1:5000/blog')

@then('I am on the blog page')
def step_impl(context):
    expected_url = 'http://127.0.0.1:5000/blog'
    assert context.driver.current_url == expected_url

@then('I am on the homepage')
def step_impl(context):
    expected_url = 'http://127.0.0.1:5000/'
    assert context.driver.current_url == expected_url