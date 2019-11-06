class Player:
    __seed=1  #record the number of the roll
    __name=''
    __locat=0
    __rolltime=1
    __money=0
    __point=0
    
    def __init__(self,name, locat = 0,seed=1):
        self.__seed=seed
        self.__name=name
        self.__locat=locat
        self.money=25000
        self.point=500

    def buybuild (self):

