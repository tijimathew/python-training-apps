def divide(a, b):
    try:
        return a/b
    except ZeroDivisionError:
        return "Division by zero is meaningless"
    except NameError:
        return "Name error"
    except:
        return "Something went wrong!"

print(divide(1, 0))
print("End of the program")