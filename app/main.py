class SoftwareEngineer:
    def __init__(self, name: str, skills: list) -> None:
        skills = []
        self.name = name
        self.skills = skills

    def learn_skill(self, skill: str):
        skill.append(self.skills)


class FrontendDeveloper(SoftwareEngineer):
    def __init__(self, name: str,
                 skills: list = ("JavaScript", "HTML", "CSS")
                ) -> None:
        super().__init__(name, skills)

    def create_awesome_web_page(self):
        print(f"{self.name} is creating a webpage...")
        return "<h1>Hello world</h1>"


class BackendDeveloper(SoftwareEngineer):
    def __init__(self, name: str,
                 skills: list = ("Python", "SQL", "Django")
                ) -> None:
        super().__init__(name, skills)

    def create_powerful_api(self):
        print(f"{self.name} is creating an API...")
        return "http://127.0.0.1:8000"


class AndroidDeveloper(SoftwareEngineer):
    def __init__(self, name: str,
                 skills: list = ("Java", "Android Studio")
                ) -> None:
        super().__init__(name, skills)

    def create_smooth_mobile_app(self):
        print(f"{self.name} is creating a mobile app...")
        return "Ads every three swipes"


class FullStackDeveloper(BackendDeveloper,
                         FrontendDeveloper,
                         SoftwareEngineer
                        ):
    def __init__(self, name: str,) -> None:
        super().__init__(name)
    def create_web_application(self):
        print(f"{self.name} started creating a web application...",
              "create_powerful_api, create_awesome_web_page"
             )
