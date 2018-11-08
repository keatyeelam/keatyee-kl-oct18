class puppy:

    name = ""
    color = ""
    def __init__(self,name,color):

        self.name = name
        self.color = color
    
    def bark(self):
        print ("I am", self.color, self.name)

puppy1 = puppy("Max","brown")
puppy1.bark()

puppy2 = puppy("Ruby","black")
puppy2.bark()