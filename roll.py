from random import randint

#--------------import script-------------------------
map1=[i for i in range(37)]
mapname=[0]+[None for i in range(1,37)]
mapown=['system']+[None for i in range(1,37)]
mapprice=[0]+[500 for i in range(1,37)]
mapleave=[0 for i in range(37)]
ainum=0


#--------------设置全局变量------------------------------

class Player:
    __seed=1  #record the number of the roll
    __name=''
    __locat=0
    __rolltime=1
    def __init__(self,name,locat=0,seed=1):
        self.__seed=seed
        self.__name=name
        self.__locat=locat
def roll(ob):
    #from random import randint
    # import can be here,but import operating over and over spend resouce so put that in file head
    seed=ob._Player__seed
    locat=ob._Player__locat
    a=0     #record the step in this round

    for i in range(seed):
        a+=randint(1,6)
    if locat+a <= 36:
        print('%s%d颗骰子，丢出%d,移动到%s' % (ob._Player__name,seed,a,str(locat+a)))
        #if not over EOF the map
        ob._Player__locat+=a
    else:
        print('%s%d颗骰子，丢出%d,移动到%s' % (ob._Player__name,seed,a,str((locat+a)-37)))
        #if over the map, player will return map 0 and restart it
        ob._Player__locat=(locat+a)-37


#---------test code-------------every thing have pass-----------this code can be used in Rich program-----
#this code support mulit rolls and over the map EOF.
play1=Player('Nick',2,2)#Nick have 2 rolls and locating port 2
play1._Player__rolltime=7#Nick have 2 rolls in 6 round

for i in range(100):
    if play1._Player__rolltime>1: #if play have the chances to use mulit rolls
        play1._Player__rolltime-=1 #reduce once time of the chances in this round
        roll(play1)                 #roll once used mulit rolls, set the number of the rolls in other process 
    else:
        play1._Player__seed=1  #if there no changes used mulit rolls set the number
                               #of roll is 1
        roll(play1)            #roll once used 1 roll





              
