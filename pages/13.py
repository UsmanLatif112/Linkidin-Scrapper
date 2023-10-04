import contextlib
import time
from .page import BasePage
from datetime import datetime
from resources.resourcces import ProfileResources


def make_csv(filename: str, data, new=True):
    """make a csv file with the given filename
    and enter the data
    """
    mode = "w" if new else "a"
    with open(filename, mode, newline="", encoding='utf-8') as f:
        f.writelines(data)

def format_date(date_str):
    try:
        # Try to parse the date string as 'Mon YYYY' format
        date = datetime.strptime(date_str, '%b %Y')
        return date.strftime('%b %Y')  # Format it as 'Mon YYYY'
    except ValueError:
        # If parsing fails, assume it's just a year and add 'JAN' to it
        return 'Jan ' + date_str if date_str.isdigit() else date_str
    
    
    
    
class ProfilePage(BasePage):
    experience_list = []
    education_list = []
    def __init__(self, url: str, people_id: str, F_company: str,  *args, **kwargs) -> None:
        self.url = url
        self.people_id = people_id
        self.founder_company = F_company
        super().__init__(*args, **kwargs)

    def get_experience(self):
        try:
            experience_url = f"{self.url}details/experience/"
            self.driver.get(experience_url)
            if 'This page doesn’t exist' not in self.driver.page_source:
                containers = self.wait_until_find_all(ProfileResources.company_containers)
                for container in containers:
                    designation = ''
                    company_name = ''
                    date = ''
                    from_date = ''
                    to_date = ''
                    
                    try:
                        designation = self.find_from_element(container, ProfileResources.company_without_link).text
                        with contextlib.suppress(Exception):
                            company_name = self.find_from_element(container, ProfileResources.experience_without_link).text.split(' · ')[0]
                        with contextlib.suppress(Exception):
                            date = self.find_from_element(container, ProfileResources.date).text.split(' · ')[0]
                            from_date = date.split(' - ')[0]
                            with contextlib.suppress(Exception):
                                to_date = date.split(' - ')[1]
                            formatted_from_date = format_date(from_date)  # Format the from_date
                            formatted_to_date = format_date(to_date)  # Format the to_date
                        temp_dict = {
                            "designation": designation,
                            "company": company_name,
                            "from_date": formatted_from_date,
                            "to_date": formatted_to_date,
                            
                        }
                        self.experience_list.append(temp_dict.copy())
                    except:
                        company_name = self.find_from_element(container, ProfileResources.company).text
                        experience_containers = self.find_all_from_element(container, ProfileResources.multi_experience_container)
                        for experience_container in experience_containers:
                            designation = self.find_from_element(experience_container, ProfileResources.experience).text
                            date = self.find_from_element(experience_container, ProfileResources.date).text.split(' · ')[0]
                            from_date = date.split(' - ')[0]
                            with contextlib.suppress(Exception):
                                to_date = date.split(' - ')[1]
                            formatted_from_date = format_date(from_date)  # Format the from_date
                            formatted_to_date = format_date(to_date) 
                            temp_dict = {
                                "designation": designation,
                                "company": company_name,
                                "from_date": formatted_from_date,
                                "to_date": formatted_to_date,
                            }
                            self.experience_list.append(temp_dict.copy())
        except Exception as e:
            print(e)
        return self
    
    # =============================================================
    
    def get_education(self):
        try:
            time.sleep(3)
            education_url = f"{self.url}details/education/"
            time.sleep(3)
            self.driver.get(education_url)
            if 'This page doesn’t exist' not in self.driver.page_source:
                degree = ''
                from_date = ''
                to_date = ''
                institude = ''
                try:
                    education_containers = self.wait_until_find_all(ProfileResources.education_containers)
                    for container in education_containers:
                        degree = ''
                        from_date = ''
                        to_date = ''
                        institude = ''
                        with contextlib.suppress(Exception):
                            degree = self.find_from_element(container, ProfileResources.degree).text
                        with contextlib.suppress(Exception):
                            institude = self.find_from_element(container, ProfileResources.institude).text
                        with contextlib.suppress(Exception):
                            date = self.find_from_element(container, ProfileResources.date).text.split(' · ')[0]
                            from_date = date.split(' - ')[0]
                            with contextlib.suppress(Exception):
                                to_date = date.split(' - ')[1]
                            formatted_from_date = format_date(from_date)  # Format the from_date
                            formatted_to_date = format_date(to_date)  # Format the to_date
                        temp_dict = {
                            "degree": degree,
                            "from_date": formatted_from_date,
                            "to_date": formatted_to_date,
                            "institude": institude,
                        }
                        self.education_list.append(temp_dict.copy())
                except:
                    pass
        except Exception as e:
            print(e)
        return self
    # =============================================================
    
    def export_experience(self):
        max_lines = 7  # Maximum number of lines to print initially
        company_match = False  # Flag to indicate if Fcompany is found in experience list
        make_csv("linkidin_experience.csv", f"{self.people_id};\n", new=False)
        
        # Separate experiences into founder company lines and other lines
        founder_company_lines = []
        other_lines = []
        
        for idx, experience in enumerate(self.experience_list):
            if idx >= max_lines:  # Print only up to max_lines
                break
                
            if experience["company"] == experience["from_date"]:
                experience["company"] = ""
                
            if self.founder_company in experience["company"]:
                company_match = True
                max_lines = 8  # Change the max_lines to 8 if there's a match
                
                is_founder_flag = "1"
                formatted_line = f"{experience['company']};{is_founder_flag};{experience['designation']};{experience['from_date']};{experience['to_date']};"
                founder_company_lines.append(formatted_line)
            else:
                is_founder_flag = "0"
                formatted_line = f"{experience['company']};{is_founder_flag};{experience['designation']};{experience['from_date']};{experience['to_date']};"
                other_lines.append(formatted_line)
        
        # Print founder company lines first, then other lines
        for line in founder_company_lines:
            make_csv("linkidin_experience.csv", line, new=False)
        
        for line in other_lines:
            make_csv("linkidin_experience.csv", line, new=False)
        
        make_csv("linkidin_experience.csv", "\n\n", new=False)
        self.experience_list.clear()
        time.sleep(3)
        return self


    # =============================================================

    def export_education(self):
        max_lines = 6  # Maximum number of lines to print
        make_csv("linkidin_education.csv", f"""{self.people_id};\n""", new=False)
        for idx, education in enumerate(self.education_list):
            if idx >= max_lines:  # Print only up to max_lines
                break
            if education["degree"] == education["from_date"]:
                education["degree"] = ""
            make_csv("linkidin_education.csv", f"""{education["institude"]};{education["degree"]};{education["from_date"]};{education["to_date"]};""", new=False)
        
        make_csv("linkidin_education.csv", "\n\n", new=False)
        self.education_list.clear()
        time.sleep(3)
        return self

   
    # =============================================================
    # =============================================================
    
    
    
    # def export_experience(self):
    #     for experience in self.experience_list:
    #         if experience["company"] == experience["from_date"]:
    #             experience["company"] = ""
    #         make_csv("linkidin_experience.csv", f'''{self.people_id};{self.founder_company};{experience["company"]};{experience["designation"]};{experience["from_date"]};{experience["to_date"]};{experience["duration"]}\n''', new=False)
    #     make_csv("linkidin_experience.csv", "\n\n", new=False)
    #     #     make_csv("linkidin_experience.csv", f'''{experience["company"]};{experience["designation"]};{experience["from_date"]};{experience["to_date"]};{self.people_id};''', new=False)
    #     # make_csv("linkidin_experience.csv", "\n\n", new=False)
    #     # make_csv("linkidin_experience.csv", f'''{experience["designation"]};{experience["company"]};{experience["from_date"]};{experience["to_date"]};{self.people_id}\n''', new=False)
    #     # make_csv("linkidin_experience.csv", "\n\n", new=False)
    #     self.experience_list.clear()
    #     time.sleep(5)
    #     return self

    # def export_education(self):
    #     for education in self.education_list:
    #         if education["degree"] == education["from_date"]:
    #             education["degree"] = ""
    #         make_csv("linkidin_education.csv", f"""{self.people_id};{self.founder_company};{education["institude"]};{education["degree"]};{education["from_date"]};{education["to_date"]}\n""", new=False)
    #     make_csv("linkidin_education.csv", "\n\n", new=False)
    #     # make_csv("linkidin_education.csv", f"""{education["degree"]};{education["from_date"]};{education["to_date"]};{education["institude"]};{self.people_id}\n""", new=False)
    #     # make_csv("linkidin_education.csv", "\n", new=False)
    #     self.education_list.clear()
    #     return self
    
    
    
    # =============================================================
    # =============================================================