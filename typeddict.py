from typing import TypedDict

class Person(TypedDict):
    
    name: str
    age: int
    
new_person: Person = {
    'name' : 'Rajshree',
    'age' : 13
}
print(new_person)