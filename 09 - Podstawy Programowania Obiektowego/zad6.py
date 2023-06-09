class Pracownik:
    def __init__(self, position, sallary, name, surname, seniority, student_status ):
        self.position = position
        self.sallary = sallary
        self.name = name
        self.surname = surname
        self.seniority = seniority
        self.student_status = student_status


    def salary_increase(self, inflation):
        self.sallary = self.sallary*(1 + inflation/100)


    def taxes(self):

        if self.student_status == 0 :
            taxes = self.sallary * 0.19 + 317.20
        else:
            taxes = self.sallary * 0.19

    def create_email(self):
        vowels = ['a', 'e', 'i', 'o', 'u', 'y']  # Lista zawierająca samogłoski
        without_vowels = ''

        for char in (self.name + self.surname):
            if char.lower() not in vowels:
                without_vowels += char
        email = without_vowels + '@work.com'
        return email