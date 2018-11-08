class crit:

    name = ""

    def __init__(self,name):

        self.name = name
    
    def talk(self):
        print ("Hi. I'm ", self.name)

crit1 = crit("Keat")
crit1.talk()


