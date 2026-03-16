from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from config.settings import Config


def get_driver():

    options = Options()

    # Headless mode (used in Jenkins / CI)
    if Config.HEADLESS:
        options.add_argument("--headless=new")

    # Required for Jenkins / Docker environments
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-extensions")

    # Browser window size
    options.add_argument("--window-size=1920,1080")

    # Recommended stability flags
    options.add_argument("--remote-allow-origins=*")
    options.add_argument("--disable-infobars")

    if Config.GRID_URL:

        driver = webdriver.Remote(
            command_executor=Config.GRID_URL,
            options=options
        )

    else:

        driver = webdriver.Chrome(options=options)

    return driver