import hello

def printstuff():
    for x in range(100):
        print("{0} bottles of rootbeer on the wall!".format(x))

print("The __name__ is: ", __name__)

# Note the revised method of checking for __main__
# that is required when using Brython.
if "__main__" in __name__ : 
    print ("Welcome to the __main__ section of the __main__.py file!")
    #printstuff()
    yourname = input("Please enter your name: ")
    print("Hello, {0}".format(yourname))
    hello.hello("Sending love to hello")
    printstuff()
    print("And that's how it's done!")