

class EvenOnly(list):
    def append(self, integer):
        if not isinstance(integer, int):
            raise TypeError("Only integers can be added")
        if integer % 2:
            raise ValueError("Only even numbers can be added")
        super().append(integer)

# Try...except clause

# try:
#     no_return()
# except:
#     print("I caught an exception")
# print("executed after the exception")

# this version of funny_division does not handle the exeption
# of dividing by zero... so error propagates to console


def funny_division(divider):
        return 100/divider

# This version of funny_division handles the ZeroDivisionError
# but not other exeptions... like type errors


def funny_division(divider):
    try:
        return 100/divider
    except ZeroDivisionError:
        return "Cannot divide by Zero... DUH"

# This version of funny_division catches multiple exeptions


def funny_division3(divider):
    try:
        return 100/divider
    except (ZeroDivisionError, TypeError):
        return "Enter a number other than Zero"


for val in (0, "Hello", 50.0, 13):
    print("Testing {} with funny_division3:".format(val), " ")
    print(funny_division3(val))

# This version of funny_division catches all exceptions (not recommended)


def funny_division2(divider):
    try:
        return 100/divider
    except:
        return "Cannot divide by Zero... DUH"

# Unique handlers for different exceptions

def funny_division4(divider):
    try:
        return 100/divider
    except (ZeroDivisionError):
        return "Enter a number other than Zero"
    except (TypeError):
        return "Enter a number other than Zero"
    except (ValueError):
        return "Enter a number other than Zero"

for val in (0, "Hello", 50.0, 13):
    print("Testing {} with funny_division4:".format(val), " ")
    print(funny_division4(val))
