from dataclasses import dataclass

@dataclass # DIFF decorators (wrapper/interface?)
class Student:
    # DIFF __init__ method is optional
    # DIFF  no self
    name: str # DIFF only need var type
    school_id: str
    gpa: float

    def __str__(self): # DIFF __str__ is optional
        return f"name: {self.name} ({self.school_id})\ngpa: {self.gpa}"


def main():
    somi = Student("Somi", "id123", 3.5)
    print(somi)

    print("") # line break

    echo = Student("Echo", "id456", 0.1)
    print(echo)

if __name__ == "__main__":
    main()
