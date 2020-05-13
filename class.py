class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def showname(self):
    print("Hi my name is " + self.name)
  def showage(self):
    print("Hi my age is " + str(self.age))
person1 = Person("Mike", 36)

print(person1.name)
print(person1.age)

person1.showname()
person1.showage()








