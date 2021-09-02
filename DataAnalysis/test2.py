import operator
class Grade:
    def __init__(self,name,chinese,math,english):
        self.name=name
        self.chinese=chinese
        self.math=math
        self.english=english
    def __repr__(self):
        return "{0} grade report".format(self.name)
    def __call__(self):
        aver=(self.chinese+self.math+self.english)/3
        print("{0:-^30}".format(aver))
    @property
    def math(self):
        return self.tmath
    @math.setter
    def math(self,value):
        if(value<=100 and value>=0):
            self.tmath = value
        else:
            raise IOError("out of range")

class Score:
    def __init__(self,null_s):
        self._score=null_s

    def __set__(self,instance,value):
        if(operator.gt(value,100) or operator.lt(value,0)):
            raise IOError("out of range")
        else:
            self._score=value

    def __get__(self,instance,owner):
        return self._score


class Student:
    history=Score(0)
    physics=Score(0)
    biology=Score(0)

    def __init__(self,name,history,physics,biology):
        self.history=history
        self.physics=physics
        self.biology=biology

    def __str__(self):
        return "std:{0} \n The transcript is as follows \n history:{1} physics:{2} biology:{3}".format(self.name,self.history,self.physics,self.biology)

    def avecal(self):
        res=(self.history+self.physics+self.biology)/3
        return res




'''if(__name__=="__main__"):
    try:
        g1 = Grade("xiaoming", 95,70, 80)
        print(g1)
        g1()
    except IOError as ioe:
        print(ioe)'''

if(__name__=="__main__"):
    try:
        s1=Student("xiaozhi",98,65,83)
        print(s1)
        av=s1.avecal()
        print("the average score of {0} is {1}".format(s1.name,av))
    except IOError as ioe:
        print(ioe)
    else:
        print("no problem".center(20,"*"))
