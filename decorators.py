def decorator(func):
    def wrapper():
        print("Transaction is starting")
        func()
        print("Transaction End")
    return wrapper

@decorator  
def hello():
    print("The amount is transfering to the benificiaries account")

hello()