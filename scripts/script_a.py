import foo.a_module
from foo.a_module import Person

foo.a_module.func()

Mike = Person(weights=100, heights=2)
print(Mike.get_bmi())
