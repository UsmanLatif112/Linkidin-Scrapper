import contextlib, time
from .page import BasePage
from resources.resourcces import ProfileResources



def make_csv(filename: str, data, new=True):
    """make a csv file with the given filename
    and enter the data
    """
    mode = "w" if new else "a"
    with open(filename, mode, newline="", encoding='utf-8') as f:
        f.writelines(data)


class ProfilePage(BasePage):
    experience_list = []
    education_list = []
    def __init__(self, url: str, people_id: str, *args, **kwargs) -> None:
        self.url = url
        self.people_id = people_id
        super().__init__(*args, **kwargs)

    def get_experience(self):
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
                    temp_dict = {
                        "designation": designation,
                        "company": company_name,
                        "from_date": from_date,
                        "to_date": to_date,
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
                        temp_dict = {
                            "designation": designation,
                            "company": company_name,
                            "from_date": from_date,
                            "to_date": to_date,
                        }
                        self.experience_list.append(temp_dict.copy())
        return self
    
    def get_education(self):
        time.sleep(5)
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
                    
                    temp_dict = {
                            "degree": degree,
                            "from_date": from_date,
                            "to_date": to_date,
                            "institude": institude,
                        }
                    self.education_list.append(temp_dict.copy())
            except:
                pass
        return self
    
    def export_experience(self):
        for experience in self.experience_list:
            if experience["company"] == experience["from_date"]:
                experience["company"] = ""
            make_csv("linkidin_experience.csv", f'''{experience["company"]};{experience["designation"]};{experience["from_date"]};{experience["to_date"]};{self.people_id};''', new=False)
        make_csv("linkidin_experience.csv", "\n\n", new=False)
        # make_csv("linkidin_experience.csv", f'''{experience["designation"]};{experience["company"]};{experience["from_date"]};{experience["to_date"]};{self.people_id}\n''', new=False)
        # make_csv("linkidin_experience.csv", "\n\n", new=False)
        self.experience_list.clear()
        time.sleep(5)
        return self

    def export_education(self):
        for education in self.education_list:
            if education["degree"] == education["from_date"]:
                education["degree"] = ""
            make_csv("linkidin_education.csv", f"""{education["institude"]};{education["degree"]};{education["from_date"]};{education["to_date"]};{self.people_id};""", new=False)
        make_csv("linkidin_education.csv", "\n\n", new=False)
        # make_csv("linkidin_education.csv", f"""{education["degree"]};{education["from_date"]};{education["to_date"]};{education["institude"]};{self.people_id}\n""", new=False)
        # make_csv("linkidin_education.csv", "\n", new=False)
        self.education_list.clear()
        return self
