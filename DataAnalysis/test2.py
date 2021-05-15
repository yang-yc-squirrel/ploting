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



if(__name__=="__main__"):
    try:
        g1 = Grade("xiaoming", 87,70, 80)
        print(g1)
        g1()
    except IOError as ioe:
        print(ioe)
