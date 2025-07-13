import pyxel
import numpy as np
SCREEN_WIDTH =120
SCREEN_HIGHT =160
class BotanHandler:
    @staticmethod
    def Right():
        if pyxel.btn(pyxel.KEY_RIGHT):
            return True
        else:
            return False
    @staticmethod
    def Left():
        if pyxel.btn(pyxel.KEY_LEFT):
            return True
        else:
            return False
    @staticmethod
    def Up():
        if pyxel.btn(pyxel.KEY_UP):
            return True
        else:
            return False

class Stand:
    def __init__(self,xSpeed:int,
                 ySpeed:int,
                 xVector:bool,
                 yVector:bool,
                 ddx_xPosition:int,
                 ddx_yPosition:int,
                 BlockCount:np.array,
                 BlockXPosition:np.array,
                 BlockYPosition:np.array,
                 SpeedUp:bool):
        self.xSpeed=xSpeed
        self.ySpeed=ySpeed
        self.xVector=xVector
        self.yVector=yVector
        self.ddx_xPosition=ddx_xPosition
        self.ddx_yPosition=ddx_yPosition
        self.BlockCount=np.array(BlockCount)
        self.BlockXPosition=np.array(BlockXPosition)
        self.BlockYPosition=np.array(BlockYPosition)
        self.SpeedUp=SpeedUp
    
    def HorizonalMove(self):
        if self.xVector==True and self.xSpeed<SCREEN_WIDTH-12:
            self.ddx_xPosition+=self.xSpeed
            self.xVector=True
        elif self.xVector==True and self.xSpeed>=SCREEN_WIDTH-12:
            self.ddx_xPosition+=self.xSpeed
            self.xVector=False
        elif self.xVector==False and self.xSpeed>0:
            self.ddx_xPosition-=self.xSpeed
            self.xVector=False
        elif self.xVector==False and self.xSpeed<=0:
            self.ddx_xPosition+=self.xSpeed
            self.xVector=True
    
    def VerticalMove(self):
        if self.yVector==True and self.ySpeed<SCREEN_HIGHT-16-19:
            self.ddx_yPosition+=self.ySpeed
            self.yVector=True
        elif self.yVector==True and self.ySpeed>=SCREEN_HIGHT-16-19:
            self.ddx_yPosition-=self.ySpeed
            self.yVector=False
        for i in range(7):
            for j in range(5):
                if self.yVector==False and self.ddx_yPosition==self.BlockYPosition[j] and self.BlockXPosition[i]<=self.ddx_xPosition<=self.BlockXPosition[i+1]:
                    self.BlockCount[i][j]-=1
                    self.yVector=True
        # elif self.yVector==False and self.ySpeed>self.top[self.topnum]:
        #     self.ySpeed+=-1
        #     self.yVector=False
        # elif self.yVector==False and self.ySpeed<=self.top[self.topnum]:
        #     self.speedup=False
        #     self.xSpeed+=1
        #     self.yVector=True
            
        #     for i in range(7):
        #         for j in range(5)
        #         if i*16<=self.xSpeed<=i*16+16 and self.count1[i]==0 and j==5:
        #             self.flags1[i]=True
        #             self.count1[i]=1
        #         elif i*16<=self.xSpeed<=i*16+16 and self.count1[i]==1 and j==5:
        #             self.flags2[i]=True
        #             self.count1[i]=2
        #         elif i*16<=self.xSpeed<=i*16+16 and self.count1[i]==2 and j==5:
        #             self.flags3[i]=True
        #             self.count1[i]=3
        #         elif self.count1==[3]*7 and j==5:
        #             self.Block[i][j]=False
        #             self.count1=[0]*7
        #             self.flags1=[False]*7
        #             self.flags2=[False]*7
        #             self.flags3=[False]*7
        #         elif i*16<=self.xSpeed<=i*16+16 and self.count1[i]==0 and j==4:
        #             self.flags1[i]=True
        #             self.count1[i]=1
        #         elif i*16<=self.xSpeed<=i*16+16 and self.count1[i]==1 and j==4:
        #             self.flags2[i]=True
        #             self.count1[i]=2
        #         elif i*16<=self.xSpeed<=i*16+16 and self.count1[i]==2 and j==4:
        #             self.flags3[i]=True
        #             self.count1[i]=3
        #         elif self.count1==[3]*7 and j==4:
        #             self.topnum+=-1
        #             self.count1=[0]*7
        #             self.flags1=[False]*7
        #             self.flags2=[False]*7
        #             self.flags3=[False]*7
        #         elif i*16<=self.xSpeed<=i*16+16 and self.count1[i]==0 and j==3:
        #             self.flags1[i]=True
        #             self.count1[i]=1
        #         elif i*16<=self.xSpeed<=i*16+16 and self.count1[i]==1 and j==3:
        #             self.flags2[i]=True
        #             self.count1[i]=2
        #         elif i*16<=self.xSpeed<=i*16+16 and self.count1[i]==2 and j==3:
        #             self.flags3[i]=True
        #             self.count1[i]=3
        #         elif self.count1==[3]*7 and j==3:
        #             self.topnum+=-1
        #             self.count1=[0]*7
        #             self.flags1=[False]*7
        #             self.flags2=[False]*7
        #             self.flags3=[False]*7
        #         elif i*16<=self.xSpeed<=i*16+16 and self.count1[i]==0 and j==2:
        #             self.flags1[i]=True
        #             self.count1[i]=1
        #         elif i*16<=self.xSpeed<=i*16+16 and self.count1[i]==1 and j==2:
        #             self.flags2[i]=True
        #             self.count1[i]=2
        #         elif i*16<=self.xSpeed<=i*16+16 and self.count1[i]==2 and j==2:
        #             self.flags3[i]=True
        #             self.count1[i]=3
        #         elif self.count1==[3]*7 and j==2:
        #             self.topnum+=-1
        #             self.count1=[0]*7
        #             self.flags1=[False]*7
        #             self.flags2=[False]*7
        #             self.flags3=[False]*7
        #         elif i*16<=self.xSpeed<=i*16+16 and self.count1[i]==0 and j==1:
        #             self.flags1[i]=True
        #             self.count1[i]=1
        #         elif i*16<=self.xSpeed<=i*16+16 and self.count1[i]==1 and self.topnum==1:
        #             self.flags2[i]=True
        #             self.count1[i]=2
        #         elif i*16<=self.xSpeed<=i*16+16 and self.count1[i]==2 and self.topnum==1:
        #             self.flags3[i]=True
        #             self.count1[i]=3
        #         elif self.count1==[3]*7 and self.topnum==1:
        #             self.topnum+=-1
        #             self.count1=[0]*7
        #             self.flags1=[False]*7
        #             self.flags2=[False]*7
        #             self.flags3=[False]*7
    
    def StandReflection(self):
            if self.yVector==True and self.ddx_yPosition==SCREEN_HIGHT*3//4-8:
                if self.ddx_yPosition-16<=self.ddx_xPosition<=self.ddx_yPosition+36:
                    self.yVector=False
                    if pyxel.btn(pyxel.KEY_RIGHT) and pyxel.btn(pyxel.KEY_UP):
                        self.ddx_xPosition+=self.xSpeed*2
                    elif pyxel.btn(pyxel.KEY_LEFT) and pyxel.btn(pyxel.KEY_UP):
                        self.ddx_xPosition-=self.xSpeed*2
        
class App:
    def __init__(self): #初期値を与える
        xSpeed=1
        ySpeed=1
        xVector=True
        yVector=True
        ddx_xPosition=40
        ddx_yPosition=40
        BlockCount=np.array([[3,3,3,3,3],
                        [3,3,3,3,3],
                        [3,3,3,3,3],
                        [3,3,3,3,3],
                        [3,3,3,3,3],
                        [3,3,3,3,3],
                        [3,3,3,3,3],])
        BlockXPosition=np.array([0,16,32,48,64,80,96,112])
        BlockYPosition=np.array([80,64,48,32,16])
        SpeedUp=False
        self.speedup=False
        self.BotanHandlerObj=BotanHandler()
        self.StandObj=Stand(xSpeed,
                            ySpeed,
                            xVector,
                            yVector,
                            ddx_xPosition,
                            ddx_yPosition,
                            BlockCount,
                            BlockXPosition,
                            BlockYPosition,
                            SpeedUp)
        pyxel.init(120,160,title="d/dx")
        pyxel.load("my_resource.pyxres") #イメージバンクの画像を読み込み
        pyxel.run(self.update,self.draw)
        

    def update(self): #フレーム更新時の処理
        if pyxel.btnp(pyxel.KEY_ESCAPE): #押した瞬間を検知
            pyxel.quit()
        
        if self.BotanHandlerObj.Right() and self.StandObj.xPosition<SCREEN_WIDTH-32: #押され続けているのを検知
            self.StandObj.xPosition+=1
            if self.BotanHandlerObj.Up():
                self.StandObj.xPosition+=1
        elif self.BotanHandlerObj.Left() and self.StandObj.xPosition>0:
            self.StandObj.xPosition-=1
            if self.BotanHandlerObj.Up():
                self.StandObj.xPosition-=1
        #台の操作
        
        self.StandObj.HorizonalMove()
        self.StandObj.VerticalMove()
        self.StandObj.Reflection()
                   
    def draw(self):
        pyxel.cls(pyxel.COLOR_NAVY)
        pyxel.blt(self.StandObj.xPosition,SCREEN_HIGHT*3//4,0,0,16,32,16,pyxel.COLOR_BLACK)
        #台
        pyxel.blt(self.StandObj.xPosition,self.StandObj.yPosition,0,0,0,16,16,pyxel.COLOR_BLACK)
        #d/dx
        # for i in range(4):
        #     for j in range(15):
        #         pyxel.blt(j*8,i*8,0,16,0,8,16,pyxel.COLOR_BLACK)
        #x
        for i in range(7):
            for j in range(5):
                # if self.StandObj.BlockCount[i][j]==3:
                pyxel.blt(i*16+8,j*16,0,24,0,16,16,pyxel.COLOR_BLACK)
                # elif self.StandObj.BlockCount[i][j]==2:
                #     pyxel.blt(j*16+8,32+36,0,32,16,11,8,pyxel.COLOR_BLACK)  #2x
                #     pyxel.blt(j*16+8,0,0,24,0,16,16,pyxel.COLOR_BLACK)  #x^2
                #     pyxel.blt(j*16+8,16,0,24,0,16,16,pyxel.COLOR_BLACK)
                #     pyxel.blt(j*16+8,32,0,24,0,16,16,pyxel.COLOR_BLACK)
                #     pyxel.blt(j*16+8,48,0,24,0,16,16,pyxel.COLOR_BLACK)
                # elif self.flags2[j]==True and self.count1[j]==2 and self.topnum==5:
                #     pyxel.blt(j*16+8,32+36,0,16,32,12,10,pyxel.COLOR_BLACK)  #2
                #     pyxel.blt(j*16+8,0,0,24,0,16,16,pyxel.COLOR_BLACK)
                #     pyxel.blt(j*16+8,16,0,24,0,16,16,pyxel.COLOR_BLACK)
                #     pyxel.blt(j*16+8,32,0,24,0,16,16,pyxel.COLOR_BLACK)
                #     pyxel.blt(j*16+8,48,0,24,0,16,16,pyxel.COLOR_BLACK)
                # elif self.flags3[j]==True and self.count1[j]==3 and self.topnum==5:
                #     pyxel.blt(j*16+8,32+36,0,32,32,16,16,pyxel.COLOR_BLACK)  # 
                #     pyxel.blt(j*16+8,0,0,24,0,16,16,pyxel.COLOR_BLACK)
                #     pyxel.blt(j*16+8,16,0,24,0,16,16,pyxel.COLOR_BLACK)
                #     pyxel.blt(j*16+8,32,0,24,0,16,16,pyxel.COLOR_BLACK)
                #     pyxel.blt(j*16+8,48,0,24,0,16,16,pyxel.COLOR_BLACK)
                # elif self.count1[j]==0 and self.topnum==4:
                #     pyxel.blt(j*16+8,32+36,0,32,32,16,16,pyxel.COLOR_BLACK)
                #     pyxel.blt(j*16+8,0,0,24,0,16,16,pyxel.COLOR_BLACK)
                #     pyxel.blt(j*16+8,16,0,24,0,16,16,pyxel.COLOR_BLACK)
                #     pyxel.blt(j*16+8,32,0,24,0,16,16,pyxel.COLOR_BLACK)
                #     pyxel.blt(j*16+8,48,0,24,0,16,16,pyxel.COLOR_BLACK)
                # elif self.flags1[j]==True and self.count1[j]==1 and self.topnum==4:
                #     pyxel.blt(j*16+8,32+36,0,32,32,16,16,pyxel.COLOR_BLACK)
                #     pyxel.blt(j*16+8,48,0,32,16,11,8,pyxel.COLOR_BLACK)
                #     pyxel.blt(j*16+8,0,0,24,0,16,16,pyxel.COLOR_BLACK)
                #     pyxel.blt(j*16+8,16,0,24,0,16,16,pyxel.COLOR_BLACK)
                #     pyxel.blt(j*16+8,32,0,24,0,16,16,pyxel.COLOR_BLACK)
                # elif self.flags2[j]==True and self.count1[j]==2 and self.topnum==4:
                #     pyxel.blt(j*16+8,32+36,0,32,32,16,16,pyxel.COLOR_BLACK)
                #     pyxel.blt(j*16+8,48,0,16,32,12,10,pyxel.COLOR_BLACK)
                #     pyxel.blt(j*16+8,0,0,24,0,16,16,pyxel.COLOR_BLACK)
                #     pyxel.blt(j*16+8,16,0,24,0,16,16,pyxel.COLOR_BLACK)
                #     pyxel.blt(j*16+8,32,0,24,0,16,16,pyxel.COLOR_BLACK)
                # elif self.flags3[j]==True and self.count1[j]==3 and self.topnum==4:
                #     pyxel.blt(j*16+8,32+36,0,32,32,16,16,pyxel.COLOR_BLACK)
                #     pyxel.blt(j*16+8,48,0,32,32,16,16,pyxel.COLOR_BLACK)
                #     pyxel.blt(j*16+8,0,0,24,0,16,16,pyxel.COLOR_BLACK)
                #     pyxel.blt(j*16+8,16,0,24,0,16,16,pyxel.COLOR_BLACK)
                #     pyxel.blt(j*16+8,32,0,24,0,16,16,pyxel.COLOR_BLACK)
                # elif self.count1[j]==0 and self.topnum==3:
                #     pyxel.blt(j*16+8,32+36,0,32,32,16,16,pyxel.COLOR_BLACK) 
                #     pyxel.blt(j*16+8,48,0,32,32,16,16,pyxel.COLOR_BLACK)
                #     pyxel.blt(j*16+8,0,0,24,0,16,16,pyxel.COLOR_BLACK)
                #     pyxel.blt(j*16+8,16,0,24,0,16,16,pyxel.COLOR_BLACK)
                #     pyxel.blt(j*16+8,32,0,24,0,16,16,pyxel.COLOR_BLACK)
                # elif self.flags1[j]==True and self.count1[j]==1 and self.topnum==3:
                #     pyxel.blt(j*16+8,32+36,0,32,32,16,16,pyxel.COLOR_BLACK) 
                #     pyxel.blt(j*16+8,48,0,32,32,16,16,pyxel.COLOR_BLACK)
                #     pyxel.blt(j*16+8,32,0,32,16,11,8,pyxel.COLOR_BLACK)
                #     pyxel.blt(j*16+8,16,0,24,0,16,16,pyxel.COLOR_BLACK)
                #     pyxel.blt(j*16+8,0,0,24,0,16,16,pyxel.COLOR_BLACK)
                # elif self.flags2[j]==True and self.count1[j]==2 and self.topnum==3:
                #     pyxel.blt(j*16+8,32+36,0,32,32,16,16,pyxel.COLOR_BLACK) 
                #     pyxel.blt(j*16+8,48,0,32,32,16,16,pyxel.COLOR_BLACK)
                #     pyxel.blt(j*16+8,32,0,16,32,12,10,pyxel.COLOR_BLACK)
                #     pyxel.blt(j*16+8,16,0,24,0,16,16,pyxel.COLOR_BLACK)
                #     pyxel.blt(j*16+8,0,0,24,0,16,16,pyxel.COLOR_BLACK)
                # elif self.flags3[j]==True and self.count1[j]==3 and self.topnum==3:
                #     pyxel.blt(j*16+8,32+36,0,32,32,16,16,pyxel.COLOR_BLACK) 
                #     pyxel.blt(j*16+8,48,0,32,32,16,16,pyxel.COLOR_BLACK)
                #     pyxel.blt(j*16+8,32,0,32,32,16,16,pyxel.COLOR_BLACK)
                #     pyxel.blt(j*16+8,16,0,24,0,16,16,pyxel.COLOR_BLACK)
                #     pyxel.blt(j*16+8,0,0,24,0,16,16,pyxel.COLOR_BLACK)
                # elif self.count1[j]==0 and self.topnum==2:
                #     pyxel.blt(j*16+8,32+36,0,32,32,16,16,pyxel.COLOR_BLACK) 
                #     pyxel.blt(j*16+8,48,0,32,32,16,16,pyxel.COLOR_BLACK)
                #     pyxel.blt(j*16+8,32,0,32,32,16,16,pyxel.COLOR_BLACK)
                #     pyxel.blt(j*16+8,16,0,24,0,16,16,pyxel.COLOR_BLACK)
                #     pyxel.blt(j*16+8,0,0,24,0,16,16,pyxel.COLOR_BLACK)
                # elif self.flags1[j]==True and self.count1[j]==1 and self.topnum==2:
                #     pyxel.blt(j*16+8,32+36,0,32,32,16,16,pyxel.COLOR_BLACK) 
                #     pyxel.blt(j*16+8,48,0,32,32,16,16,pyxel.COLOR_BLACK)
                #     pyxel.blt(j*16+8,32,0,32,32,16,16,pyxel.COLOR_BLACK)
                #     pyxel.blt(j*16+8,16,0,32,16,11,8,pyxel.COLOR_BLACK)
                #     pyxel.blt(j*16+8,0,0,24,0,16,16,pyxel.COLOR_BLACK)
                # elif self.flags2[j]==True and self.count1[j]==2 and self.topnum==2:
                #     pyxel.blt(j*16+8,32+36,0,32,32,16,16,pyxel.COLOR_BLACK) 
                #     pyxel.blt(j*16+8,48,0,32,32,16,16,pyxel.COLOR_BLACK)
                #     pyxel.blt(j*16+8,32,0,32,32,16,16,pyxel.COLOR_BLACK)
                #     pyxel.blt(j*16+8,16,0,16,32,12,10,pyxel.COLOR_BLACK)
                #     pyxel.blt(j*16+8,0,0,24,0,16,16,pyxel.COLOR_BLACK)
                # elif self.flags3[j]==True and self.count1[j]==3 and self.topnum==2:
                #     pyxel.blt(j*16+8,32+36,0,32,32,16,16,pyxel.COLOR_BLACK) 
                #     pyxel.blt(j*16+8,48,0,32,32,16,16,pyxel.COLOR_BLACK)
                #     pyxel.blt(j*16+8,32,0,32,32,16,16,pyxel.COLOR_BLACK)
                #     pyxel.blt(j*16+8,16,0,32,32,16,16,pyxel.COLOR_BLACK)
                #     pyxel.blt(j*16+8,0,0,24,0,16,16,pyxel.COLOR_BLACK)
                # elif self.count1[j]==0 and self.topnum==1:
                #     pyxel.blt(j*16+8,32+36,0,32,32,16,16,pyxel.COLOR_BLACK) 
                #     pyxel.blt(j*16+8,48,0,32,32,16,16,pyxel.COLOR_BLACK)
                #     pyxel.blt(j*16+8,32,0,32,32,16,16,pyxel.COLOR_BLACK)
                #     pyxel.blt(j*16+8,16,0,32,32,16,16,pyxel.COLOR_BLACK)
                #     pyxel.blt(j*16+8,0,0,24,0,16,16,pyxel.COLOR_BLACK)
                # elif self.flags1[j]==True and self.count1[j]==1 and self.topnum==1:
                #     pyxel.blt(j*16+8,32+36,0,32,32,16,16,pyxel.COLOR_BLACK) 
                #     pyxel.blt(j*16+8,48,0,32,32,16,16,pyxel.COLOR_BLACK)
                #     pyxel.blt(j*16+8,32,0,32,32,16,16,pyxel.COLOR_BLACK)
                #     pyxel.blt(j*16+8,16,0,32,32,16,16,pyxel.COLOR_BLACK)
                #     pyxel.blt(j*16+8,0,0,32,16,11,8,pyxel.COLOR_BLACK)
                # elif self.flags2[j]==True and self.count1[j]==2 and self.topnum==1:
                #     pyxel.blt(j*16+8,32+36,0,32,32,16,16,pyxel.COLOR_BLACK) 
                #     pyxel.blt(j*16+8,48,0,32,32,16,16,pyxel.COLOR_BLACK)
                #     pyxel.blt(j*16+8,32,0,32,32,16,16,pyxel.COLOR_BLACK)
                #     pyxel.blt(j*16+8,16,0,32,32,16,16,pyxel.COLOR_BLACK)
                #     pyxel.blt(j*16+8,0,0,16,32,12,10,pyxel.COLOR_BLACK)
                # elif self.flags3[j]==True and self.count1[j]==3 and self.topnum==1:
                #     pyxel.blt(j*16+8,32+36,0,32,32,16,16,pyxel.COLOR_BLACK) 
                #     pyxel.blt(j*16+8,48,0,32,32,16,16,pyxel.COLOR_BLACK)
                #     pyxel.blt(j*16+8,32,0,32,32,16,16,pyxel.COLOR_BLACK)
                #     pyxel.blt(j*16+8,16,0,32,32,16,16,pyxel.COLOR_BLACK)
                #     pyxel.blt(j*16+8,0,0,32,32,16,16,pyxel.COLOR_BLACK)
        #x^2
        for i in range(8):
            pyxel.blt(i*15,135,0,0,28,15,19,pyxel.COLOR_BLACK)
        #e^x
  
App()