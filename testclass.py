class test:

    __name = "Test"

    def __init__(self,name="Object"):
        self.name = name
    
    def talk(self,msg):
        print(self.name + ", " + msg)

    def myname(self)