

class UsefulClass:
    "This might be useful to other modules"
    pass


def main():
    "Creates a useful class and does something with it for our module"
    useful = UsefulClass()
    print(useful)


if __name__ == "__main__":
    main()

# every modules has a __name__ (special variable b/c of __x__)
# when the module is not imported, the __name__ is set to "__main__"
