def divide(a, b):
    try:
        return a/b
    except ZeroDivisionError:
        return "Division by zero is meaningless"
    except NameError:
        return "Name error"
    except TypeError:
        return "Input parameters have mismatched data types"
    except:
        return "Something went wrong!"

print(divide(1, '1'))
print("End of the program")