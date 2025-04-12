from VTK_Code import *
#returnValue = ""

def spam(returnValue):
    print("Hello world! I am executed spam!")
    returnValue = 'aaahhh'                          # this is hack to get values back, but is not needed

if __name__ == "__main__":
    returnValue = ""
    spam(returnValue)
    print("returnValue=",returnValue)