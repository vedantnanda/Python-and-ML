did = {}
ll = []
try:
    print("34"+3) #TypeError
    print(1/0) #ZeroDivisionError
    print(ll[1]) #IndexError
    fh = open("testfile","r") #FileNotFoundError
    fh.write("This command will generate error") #IOError
    print(did["alpha"]) #KeyError
    print(int("dasd")) #ValueError

except IOError:
    print("Error: can't find file / can't write to the file ")
except ZeroDivisionError:
    print("Division by zero not possible")
except KeyError:
    print("Key not found in dictionary")
except IndexError:
    print("Index out of range")
except NameError:
    print("name not defined")
except ValueError:
    print("Invalid casting types")
except TypeError:
    print("Incompatible Value types")
except FileNotFoundError:
    print("File not found")
except Exception:
    print("Exception generated")
else:
    print("No Error, successful execution")