# Try Except Finally Example

try:
    f = open("myfile.txt","w")
    f.write("This is a text")

#if there is an error, the following will be printed out
except:
    print("There is an error")

#the following line of code will be printed regardless of any error
finally:
    print("This line of code will run no matter what")
    
