class Student:
    # [assignment] Skeleton class. Add your code here
    
    def __init__(self, name: str, age: int, tracks: list, score: float):
            self.name:str = name
            self.age:int = age
            self.tracks:list = tracks
            self.score:float = score

    def change_name(self, change_name):
            self.change_name = change_name
            print ("New name :", change_name)

    def change_age(self, change_age):
            self.change_age = change_age
            print ("New age :", change_age)

    def add_track(self, add_track):
            self.tracks.append(add_track)
            print ("Track: ", add_track)

    def get_score(self):
            print("Score: ", self.score)



Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)

# Expected methods
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
Bob.get_score()
