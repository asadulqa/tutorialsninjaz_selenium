from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def before_scenario(context, scenario):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    
    context.driver = webdriver.Chrome(options=chrome_options)

def after_scenario(context, scenario):
    if hasattr(context, 'driver'):
        context.driver.quit()
