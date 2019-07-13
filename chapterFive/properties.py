

# python convention says we should access attributes directly i.e.

class Test:
    def __init__(self, one, two):
        self.one = one
        self.two = two


myTest = Test(1, 2)

print("The values are {} and {}".format(myTest.one, myTest.two))

# This is convenient, but has a weakness: If we want to change the way
# we access an attribute later, we will have to refactor all our code...


class Test2:
    def __init__(self, one, two):
        self.one = one
        self.two = two

    def getOne(self):
        return str(self.one)

    def getTwo(self):
        return str(self.two)

myTest2 = Test2(1, 2)

print("The values are {} and {}".format(myTest2.getOne(), myTest2.getTwo()))

# This works but can be inconvenient... Python provides the property method that
# allows us to access the modified attribute easily
# mark variables with an _ to signify they are private... should not be accessed directly


class TestProperty:
    def __init__(self, one, two):
        self._one = one
        self._two = two

    def _setOne(self, one):
        self._one = one

    def _getOne(self):
        return "The value is " + str(self._one)

    def _setTwo(self, two):
        self._two = two

    def _getTwo(self):
        return "The value is " + str(self._two)

    one = property(_getOne, _setOne)
    two = property(_getTwo, _setTwo)

testP = TestProperty(1, 2)

# with this method, the _private attribute is still accessible directly...
# keep this in mind

# Properties in depth example:
# property accepts four arguments (get, set, delete, docstring/description)

class myClass:
    def _getAttribute(self):
        return self._attribute

    def _setAttribute(self, value):
        self._attribute = value

    def _delAttribute(self):
        print("You just deleted your attribute!")
        del self._attribute

    attribute = property(_getAttribute, _setAttribute, _delAttribute,
                         "This is an attribute")

aClass = myClass()
aClass.attribute = "Patrick"

# This allows us to specify more specific behaviors in case of
# access, setting, deletion, or description
# Usually just getter and setter are used

# help(aClass)

# a property is an attribute we can invoke custom actions
