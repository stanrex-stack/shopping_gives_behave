from selenium import webdriver
from app.application import Application


def browser_init(context):
    """
    :param context: Behave context
    """
    # BROWSERSTACK_URL = 'https://stanrekhletskyy1:8y54oxR2pdxrcpDWxxQY@hub-cloud.browserstack.com/wd/hub'
    # desired_cap = {
    #     'bstack:options': {
    #         "os": "OS X",
    #         "osVersion": "Catalina",
    #         "local": "false",
    #         "seleniumVersion": "3.5.2",
    #     },
    #     "browserName": "Edge",
    #     "browserVersion": "latest",
    # }


    executable_path = 'drivers/chromedriver'
    context.driver = webdriver.Chrome()
    # context.driver = webdriver.Remote(command_executor=BROWSERSTACK_URL, desired_capabilities=desired_cap)
    context.driver.maximize_window()
    context.driver.implicitly_wait(5)
    context.app = Application(context.driver)


def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    browser_init(context)


def before_step(context, step):
    print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)


def after_scenario(context, feature):
    context.driver.delete_all_cookies()
    context.driver.quit()
