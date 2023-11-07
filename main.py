"""This file will run to execute all the logics and commands"""

# Import required modules
import csv
from pathlib import Path
from datetime import datetime
from drivers.driver import get_undetected_chrome_browser
from pages.profile_page import ProfilePage, make_csv

BASE_DIR = Path(__file__).resolve().parent
input_file = BASE_DIR / "input.csv"
output_file = BASE_DIR / "output.csv"


def main():
    # Get a new undetected Chrome browser instance for the user
    
    USERNAME = "linkedint31@gmail.com"
    PASSWORD = "Usman@112"
    

    driver = get_undetected_chrome_browser('christoph')
    
    with open(input_file, "r") as file:
        reader = csv.reader(file)
        make_csv("linkidin_experience.csv", "Role; Organization; Start date; End date; People ID\n", new=True)
        make_csv("linkidin_education.csv", "Degree; Start date; End date; Institute; People ID\n", new=True)
        for row in reader:
            url = row[0]
            people_id = row[1]
            F_company = row[2]
            
            # try:
            #     profile = ProfilePage(url, people_id, F_company, driver).get_experience()\
            #         .export_experience()
            # except:
            #     pass
            try:
                profile = ProfilePage(url, people_id, F_company, driver).get_experience()\
                    .get_education()\
                    .export_education()\
                    .export_experience()
            except:
                pass
            # try:
            #     profile = ProfilePage(url, people_id, driver).get_experience()\
            #         .get_education()\
            #         .export_education()\
            #         .export_experience()
            # except:
            #     pass
            

if __name__ == '__main__':
    main()
