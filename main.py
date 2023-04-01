import time

class Person:
  age = 15
  height = 175
  isMale = True
  name = "Cold"
  money = 0 

  def __init__(self, name, age, height):
    self.name = name
    self.age = age
    self.height = height

  def work(self, days):
    while days != 0:
      time.sleep(1)
      self.money += 1
      days -= 1

me = Person('Cold', 15, 175)
friend = Person('Coal', 16, 180)

print(me.money)
me.work(3)
print(me.money)

print(me.name)





