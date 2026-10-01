# Crate a clas
class Employee:

    # Initializing
    def __init__(self):
        print("Employee created")

    # Calling destructer
    def __del__(self):
        print("Destructer called")

def Create_obj():
    print("Making object......")
    obj = Employee()
    print("Function end....")
    return obj

print("Calling create obj() function")
obj = Create_obj
print("Program end.....")