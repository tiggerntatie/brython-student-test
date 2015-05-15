import hello

def printstuff():
    for x in range(100):
        print("{0} bottles of rootbeer on the wall!".format(x))

print("The file's __name__ is: ", __name__)

# Note the revised method of checking for __main__
# that is required when using Brython.
if "__main__" in __name__ : 
    print ("Welcome to the __main__ section of the __main__.py file!")
    #printstuff()
    yourname = input("Please enter your name: ")
    print("Hello, {0}".format(yourname))
    hello.hello("Sending hate to hello")
    printstuff()
    print("Begin testing text file read...")
    f = open("test.txt",'r')
    print(f.read())
    f.close()
    print("Begin testing binary file read...")
    f = open("sun.rays.small.png", 'rb')
    bd = f.read(100)
    #print(type(bd))   # this has suddenly stopped working
    print(bd)
    f.close() 
    print("Begin testing binary data...")
    bd = b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x01\x00\x00\x00\x01\x00\x08\x06\x00\x00\x00\\r\xa8f\x00\x00\x00\tpHYs\x00\x00\x0b\x13\x00\x00\x0b\x13\x01\x00\x9a\x9c\x18\x00\x00\nOiCCPPhotoshop ICC profile\x00\x00x'
    print(bd)