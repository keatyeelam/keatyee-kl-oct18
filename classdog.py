class dog:
    name = ""
    age = 0

    def __init__(self,name,age):
        self.name = name
        self.age = age

dog1 = dog("Jake", 7)
dog2 = dog("Mark", 3)
dog3 = dog("Luky", 5)


def get_biggest_number(*arg):
    return max(arg)

print("The oldest dog is {} years old".format(get_biggest_number(dog1.age,dog2.age,dog3.age)))


        