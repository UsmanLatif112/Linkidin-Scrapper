"""This File contains all the locators all the elements of different pages
If in futur the UI of the website will change we can change the locators from here
"""
from selenium.webdriver.common.by import By
from dataclasses import dataclass

@dataclass
class Selector:
    """class to create objects for selecting or targetting a certain element
        on the page

        Args:
            ST (str): Selector Type: ie XPATH or CSSSelector
            SP (str): Path of the element according to selector type
    """
    ST: str
    SP: str

class ProfileResources:
    
    date = Selector(By.XPATH, './/span[@class="t-14 t-normal t-black--light"][1]/span[@aria-hidden="true"]')

    # Experience History
    company_containers = Selector(By.XPATH, "//main[@class='scaffold-layout__main']/section/div/div/div/ul/li/div/div/div[position() > 1]")
    company = Selector(By.XPATH, './div/a/div/div/div//span[@aria-hidden="true"]')
    multi_experience_container = Selector(By.XPATH, './/div[@class="scaffold-finite-scroll__content"]/ul/li')
    experience = Selector(By.XPATH, ".//*[@class='display-flex flex-wrap align-items-center full-height']/div/div/div/span[@aria-hidden='true']")
    company_without_link = Selector(By.XPATH, './div/div/div/div/div/div/span[@aria-hidden="true"]')
    experience_without_link = Selector(By.XPATH, './div/div/span[position() < 3]/span[@aria-hidden="true"]')

    # Educational History
    education_containers = Selector(By.XPATH, "//main[@class='scaffold-layout__main']/section/div/div/div/ul/li/div/div/div[position() > 1]")
    institude = Selector(By.XPATH, './div/a/div//span[@aria-hidden="true"]')
    degree = Selector(By.XPATH, './/span[@class="t-14 t-normal"]/span[@aria-hidden="true"]')


class CookieBotResources:
    """This class contains all the locators and urls for cookie bot"""

    # URLs for YouTube and Google
    YoutubeURL = "https://youtube.com/"
    GoogleURL = "https://google.com/"

    # Locators for YouTube search field and video elements
    YoutubeSearchField = Selector(By.XPATH, "//input[@id='search']")
    YoutubeVideo = Selector(By.XPATH, "//a[@id='video-title']")

    # Locators for Google search field and link elements
    GoogleSearchField = Selector(By.XPATH, "//*[@name='q']")
    Googlelink = Selector(By.XPATH, '//a[./h3[contains(@class,"DKV0Md")]]')

