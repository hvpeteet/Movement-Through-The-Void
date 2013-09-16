x = [2,3,4,3,2,1,2,1,2,2,2,2,5,12,14]
x.sort()
print x
class person(object):
    def __init__(self,name, age = 0):
        self.age = age
        self.name = name
    def __lt__(self, other):
        return self.age<other.age
    def __str__(self):
        return self.name
mormor = person("mormor", 70)
ely = person("ely", 13)
henry = person("henry", 18)
alex = person ("alex", 17)
ana = person("ana", 52)
y = [mormor, ely, henry, alex, ana]
for i in y:
    print i
    
y.sort()
for i in y:
    print i
