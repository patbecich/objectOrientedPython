
class Contact:
    all_contacts = []

    def __init__(self, name, email):
        self.name = name
        self.email = email
        Contact.all_contacts.append(self)


class Supplier(Contact):
    def order(self, order):
        print("Order {} from {}".format(order, self.name))

## basic Overriding example

class Friend(Contact):
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone

## better method for overriding (avoid duplicate code)
## use super to execute the superclass __init__ with modifications

class ImprovedFriend(Contact):
    def __init__(self, name, email, phone):
        super().__init__(name, email)
        self.phone = phone
