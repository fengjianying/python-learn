###类
class People():
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def sit(self):
        print(self.name.title() + " is now sitting")

my_friend = People("shiqi",25);
print(my_friend.name);
print(my_friend.age);
my_friend.sit()
##继承
class Man(People):
    def __init__(self,name,age):
        super().__init__(name,age)
        self.sex = "man"
    def speak_name(self):
        print(self.name + ' is lishen')
my_friend2 = Man("laopao",25);
my_friend2.sit()
my_friend2.speak_name()
print(my_friend2.sex)