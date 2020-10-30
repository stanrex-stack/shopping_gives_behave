from behave import given, when, then
from time import sleep


@given('Open Main Page')
def open_main_page(context):
        context.app.main_page.main_open()

@when('On main page click on {network_name} link')
def main_page_click_on_social_network(context, network_name):
        context.app.main_page.view_and_click_network_link(network_name)

@then('Verify the network page title is {title_text}')
def pass_method(context, title_text):
        context.app.main_page.verify_title_text(title_text)


