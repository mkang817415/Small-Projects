
class gpa():
    def __init__(self, grades): 
        self.gpa = 0
        self.total_classes = 0 
        self.grades = grades
        
        self.gpa_dict = {
            "A": 4.0,
            "A-": 3.7,
            "B+": 3.3,
            "B": 3.0,
            "B-": 2.7,
            "C+": 2.3
        }
        
    def calc(self):
        for grade in self.grades:
            self.gpa += self.gpa_dict[grade]
            self.total_classes += 1
        self.gpa = self.gpa/self.total_classes
        return self.gpa
    
    def __str__(self):
        return f"Your GPA is {self.gpa}"
    
soph_grades = ['A', 'A', 'A-', 'A', 
               'B+', 'A-', 'A', 'A', 
               'B', 'B', 'A', 'B', 
               'A', 'A-', 'B'               
               ]
    
a = gpa(soph_grades)
print(a.calc())

kasei_grades = [
    'A-', 'A-', 'A-', 'A',
    'A', 'A', 'A', 'A-',
    'A', 'A', 'A', 'A'
]
b = gpa(kasei_grades)
print(b.calc())