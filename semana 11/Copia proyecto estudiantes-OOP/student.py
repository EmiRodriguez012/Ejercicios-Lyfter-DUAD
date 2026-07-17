class Student():
    def __init__(self, name, section, spanish_grade, english_grade, social_stds_grade, science_grade):
        self.name = name
        self.section = section
        self.spanish_grade = spanish_grade
        self.english_grade = english_grade
        self.social_stds_grade = social_stds_grade
        self.science_grade = science_grade

    def convert_to_dict(self):
        return {
            "name": self.name,
            "section": self.section,
            "spanish_grade": self.spanish_grade,
            "english_grade": self.english_grade,
            "social_stds_grade": self.social_stds_grade,
            "science_grade": self.science_grade
            
        }

    @classmethod
    def convert_from_dict(cls, data):

        return cls(
            data["name"],
            data["section"],
            int(data["spanish_grade"]),
            int(data["english_grade"]),
            int(data["social_stds_grade"]),
            int(data["science_grade"])
        )
              
