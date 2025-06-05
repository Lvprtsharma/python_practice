"""
Problem: Implement a basic Person class with name and age attributes, and methods to display info.

Explanation:
This example demonstrates various Object-Oriented Programming concepts in Python:
1. Basic class implementation with instance attributes
2. Property decorators for data validation
3. Magic methods for string representation
4. Class methods and static methods
5. Inheritance and method overriding
"""

class Person:
    """
    Method 1: Basic implementation
    Demonstrates basic class structure with instance methods
    """
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")
    
    def have_birthday(self):
        self.age += 1
        return self.age

class PersonWithValidation:
    """
    Method 2: Implementation with property decorators
    Demonstrates data validation and encapsulation
    """
    def __init__(self, name, age):
        self._name = None
        self._age = None
        self.name = name  # Uses the property setter
        self.age = age    # Uses the property setter
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Name must be a string")
        if not value.strip():
            raise ValueError("Name cannot be empty")
        self._name = value.strip()
    
    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, value):
        if not isinstance(value, int):
            raise TypeError("Age must be an integer")
        if value < 0 or value > 150:
            raise ValueError("Age must be between 0 and 150")
        self._age = value
    
    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")

class PersonWithMagicMethods:
    """
    Method 3: Implementation with magic methods
    Demonstrates Python's special methods
    """
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self):
        return f"Person(name='{self.name}', age={self.age})"
    
    def __repr__(self):
        return f"PersonWithMagicMethods('{self.name}', {self.age})"
    
    def __eq__(self, other):
        if not isinstance(other, PersonWithMagicMethods):
            return NotImplemented
        return self.name == other.name and self.age == other.age
    
    def __lt__(self, other):
        if not isinstance(other, PersonWithMagicMethods):
            return NotImplemented
        return self.age < other.age

class PersonWithClassMethods:
    """
    Method 4: Implementation with class and static methods
    Demonstrates class-level functionality
    """
    population = 0
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        PersonWithClassMethods.population += 1
    
    @classmethod
    def from_birth_year(cls, name, birth_year):
        """Create a Person instance from birth year instead of age"""
        from datetime import datetime
        age = datetime.now().year - birth_year
        return cls(name, age)
    
    @staticmethod
    def is_adult(age):
        """Check if age represents an adult"""
        return age >= 18
    
    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")
        print(f"Is adult? {self.is_adult(self.age)}")

class Employee(PersonWithMagicMethods):
    """
    Method 5: Implementation with inheritance
    Demonstrates inheritance and method overriding
    """
    def __init__(self, name, age, employee_id, salary):
        super().__init__(name, age)
        self.employee_id = employee_id
        self.salary = salary
    
    def display_info(self):
        print(f"Employee ID: {self.employee_id}")
        print(f"Name: {self.name}, Age: {self.age}")
        print(f"Salary: ${self.salary:,.2f}")
    
    def give_raise(self, amount):
        self.salary += amount

# Example usage
if __name__ == "__main__":
    print("1. Basic Person Class:")
    p1 = Person("Alice", 30)
    p1.display_info()
    print(f"After birthday: {p1.have_birthday()}")
    
    print("\n2. Person With Validation:")
    try:
        p2 = PersonWithValidation("Bob", 25)
        p2.display_info()
        # This will raise an error
        p2.age = -5
    except ValueError as e:
        print(f"Validation Error: {e}")
    
    print("\n3. Person With Magic Methods:")
    p3a = PersonWithMagicMethods("Charlie", 35)
    p3b = PersonWithMagicMethods("David", 40)
    print(f"str(): {p3a}")
    print(f"repr(): {repr(p3a)}")
    print(f"Comparison: {p3a < p3b}")
    
    print("\n4. Person With Class Methods:")
    p4 = PersonWithClassMethods.from_birth_year("Eve", 1990)
    p4.display_info()
    print(f"Total population: {PersonWithClassMethods.population}")
    print(f"Is 20 adult? {PersonWithClassMethods.is_adult(20)}")
    
    print("\n5. Employee (Inheritance):")
    e1 = Employee("Frank", 45, "E123", 50000)
    e1.display_info()
    e1.give_raise(5000)
    print("\nAfter raise:")
    e1.display_info() 