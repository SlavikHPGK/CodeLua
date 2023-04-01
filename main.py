# Класифікація обєктів

class Person:
  age = 15
  height = 175
  isMale = True
  name = "Cold"
  

me = Person()

class Friend:
  age = 16
  height = 180
  isMale = True
  name = "Coal"

friend = Friend()

class Cat:
  age = 9
  height = 30
  isFemale = True
  name = "Diamond"
  socialstatus = "Social-Nacionalist"

cat = Cat()

# вивід

print(me)
print(friend)
print(cat)
print(me.age)
print(friend.height)
print(cat.isFemale)
print(me.name)
print(cat.socialstatus)