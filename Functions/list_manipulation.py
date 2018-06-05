def list_manipulation(collection, command, location, value=None):
    if(command == "remove" and location == "end"):
        return collection.pop()
    elif(command == "remove" and location == "beginning"):
        return collection.pop(0)
    elif(command == "add" and location == "beginning"):
        collection.insert(0,value)
        return collection
    elif(command == "add" and location == "end"):
        collection.append(value)
        return collection


list_input = list(input("Enter the list to be manipulated : "))
operation = input("Enter the operation/command you would like to perform : ")
location = input("Location of the operation/command(beginning/end) : " )
value = input("Any value that should be added : ")

print(list_manipulation(list_input,operation,location,value))