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
class ddx:
    def __init__(self,
                 xSpeed:int,
                 ySpeed:int,
                 xVector:bool,
                 yVector:bool,
                 ddx_xPosition:int,
                 ddx_yPosition:int,
                 BlockCount:int,
                 BlockXPosition:np.array,
                 BlockYPosition:np.array):
        self.xSpeed=xSpeed
        self.ySpeed=ySpeed
        self.xVector=xVector
        self.yVector=yVector
        self.ddx_xPosition=ddx_xPosition
        self.ddx_yPosition=ddx_yPosition
        self.BlockCount=np.array(BlockCount)
        self.BlockXPosition=np.array(BlockXPosition)
        self.BlockYPosition=np.array(BlockYPosition)
    
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
        
class Stand:
    def __init__(self,
                 yVector,
                 xSpeed:int,
                 StandxPosition:int,
                 StandyPosition:int):
        self.xSpeed=xSpeed
        self.yVector=yVector
        self.StandxPosition=StandxPosition
        self.StandyPosition=StandyPosition
        self.BotanHandlerObj=BotanHandler()
    def HorizonalMove(self):
        if self.BotanHandlerObj.Right() and self.StandxPosition<SCREEN_WIDTH-32: #押され続けているのを検知
            self.StandxPosition+=self.xSpeed
            if self.BotanHandlerObj.Up():
                self.StandxPosition+=self.xSpeed*2
        elif self.BotanHandlerObj.Left() and self.xPosition>0:
            self.StandxPosition-=self.xSpeed
            if self.BotanHandlerObj.Up():
                self.StandxPosition-=self.xSpeed*2
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
        ddx_yPosition=83
        BlockCount=np.array([[3,3,3,3,3],
                        [3,3,3,3,3],
                        [3,3,3,3,3],
                        [3,3,3,3,3],
                        [3,3,3,3,3],
                        [3,3,3,3,3],
                        [3,3,3,3,3],])
        BlockXPosition=np.array([0,16,32,48,64,80,96,112])
        BlockYPosition=np.array([80,64,48,32,16])
        StandxPosition=16
        StandyPosition=SCREEN_HIGHT*3//4
        self.speedup=False
        self.BotanHandlerObj=BotanHandler()
        self.ddxObj=ddx(xSpeed,
                        ySpeed,
                        xVector,
                        yVector,
                        ddx_xPosition,
                        ddx_yPosition,
                        BlockCount,
                        BlockXPosition,
                        BlockYPosition)
        self.StandObj=Stand(xSpeed,
                            StandxPosition,
                            StandyPosition)
        pyxel.init(120,160,title="d/dx")
        pyxel.load("my_resource.pyxres") #イメージバンクの画像を読み込み
        pyxel.run(self.update,self.draw)
        

    def update(self): #フレーム更新時の処理
        if pyxel.btnp(pyxel.KEY_ESCAPE): #押した瞬間を検知
            pyxel.quit()
        self.ddxObj.HorizonalMove()
        self.ddxObj.VerticalMove()
        self.StandObj.StandReflection()
        self.StandObj.HorizonalMove()
                   
    def draw(self):
        pyxel.cls(pyxel.COLOR_NAVY)
        pyxel.blt(self.StandObj.StandxPosition,self.StandObj.StandyPosition,0,0,16,32,16,pyxel.COLOR_BLACK)
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