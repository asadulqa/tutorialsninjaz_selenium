from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def before_scenario(context, scenario):
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--disable-background-timer-throttling")
    chrome_options.add_argument("--disable-backgrounding-occluded-windows")


    context.driver = webdriver.Chrome(options=chrome_options)

def after_scenario(context, scenario):
    if hasattr(context, 'driver'):
        context. driver.quit()
