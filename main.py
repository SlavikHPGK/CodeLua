
class Person:
  age = 15
  height = 175
  isMale = True
  name = "Cold"
  

  def __init__(self, name, age, height):
    self.name = name
    self.age = age
    self.height = height

me = Person('Cold', 15, 175)
friend = Person('Coal', 16, 180)

print(me.height)




