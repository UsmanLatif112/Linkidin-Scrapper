"""This file contains all the logic of how the driver or browser will react
"""

# ===================

import time
import pyautogui
from typing import List
from datetime import date
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from undetected_chromedriver import Chrome, ChromeOptions
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService

# =================
from pathlib import Path
import undetected_chromedriver as uc
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

BASE_DIR = Path(__file__).resolve().parent


"""This file contains all the logic of how the driver or browser will react"""

from pathlib import Path
import undetected_chromedriver as uc
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

BASE_DIR = Path(__file__).resolve().parent

# def get_undetected_chrome_browser(profile=None):
#     """Returns an instance of an undetected Chrome browser with added features to make it more undetectable and secure.
#     The browser will save the profile and cookies to the specified folder so that you don't have to log in every time.

#     Returns:
#         uc.Chrome: An instance of the Chrome class from the undetected_chromedriver library.
#     """
#     options = uc.ChromeOptions()
#     options.headless = True  # Add this line
#     if profile:
#         options.user_data_dir = f"{BASE_DIR}/profile/{profile}"
#     driver_version = "114.0.5735.90"  # You can also specify a specific version here
#     return uc.Chrome(options=options)

def get_undetected_chrome_browser(profile=None):
    """Returns an instance of a Chrome browser with specified user profile."""

    options = webdriver.ChromeOptions()
    if profile:
        options.add_argument(f"user-data-dir={BASE_DIR}/profile/{profile}")
        
    return webdriver.Chrome(options=options)