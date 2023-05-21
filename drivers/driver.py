"""This file contains all the logic of how the driver or browser will react
"""
from pathlib import Path
import undetected_chromedriver as uc
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

BASE_DIR = Path(__file__).resolve().parent

def get_undetected_chrome_browser(profile):
    """Returns an instance of an undetected Chrome browser with added features to make it more undetectable and secure.
    The browser will save the profile and cookies to the specified folder so that you don't have to log in every time.

    Returns:
        uc.Chrome: An instance of the Chrome class from the undetected_chromedriver library.
    """
    if profile:
        options = uc.ChromeOptions()
        options.user_data_dir = f"{BASE_DIR}/peofile/{profile}"
        options.add_argument("--profile-directory=Default")
        return uc.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
    return uc.Chrome(service=ChromeService(ChromeDriverManager().install()))
