"""This file will run to execute all the logics and commands"""

# Import required modules
from datetime import datetime
from drivers.driver import get_undetected_chrome_browser

def main():
    # Get a new undetected Chrome browser instance for the user
    driver = get_undetected_chrome_browser()
    

if __name__ == '__main__':
    main()
