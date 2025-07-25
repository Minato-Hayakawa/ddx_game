import pyxel
import numpy as np

SCREEN_WIDTH =120
SCREEN_HIGHT =160
xSpeed=1
ySpeed=1
xVector=True
yVector=True
ddx_xVector=True
ddx_yVector=True
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
    
    def __init__(
        self,
        xSpeed:int,
        ySpeed:int,
        ddx_xVector:bool,
        ddx_yVector:bool,
        ddx_xPosition:int,
        ddx_yPosition:int,
        StandxPosition:int,
        StandyPosition:int,
        BlockCount:int,
        BlockXPosition:np.array,
        BlockYPosition:np.array
        ):
        self.xSpeed=xSpeed
        self.ySpeed=ySpeed
        self.ddx_xVector=ddx_xVector
        self.ddx_yVector=ddx_yVector
        self.ddx_xPosition=ddx_xPosition
        self.ddx_yPosition=ddx_yPosition
        self.StandxPosition=StandxPosition
        self.StandyPosition=StandyPosition
        self.BlockCount=np.array(BlockCount)
        self.BlockXPosition=np.array(BlockXPosition)
        self.BlockYPosition=np.array(BlockYPosition)
    
    def HorizonalMove(self):
        if self.ddx_xVector==True and self.ddx_xPosition<SCREEN_WIDTH-12:
            self.ddx_xPosition+=self.xSpeed
            self.ddx_xVector=True
        elif self.ddx_xVector==True and self.ddx_xPosition>=SCREEN_WIDTH-12:
            self.ddx_xPosition+=self.xSpeed
            self.ddx_xVector=False
        elif self.ddx_xVector==False and self.ddx_xPosition>0:
            self.ddx_xPosition-=self.xSpeed
            self.ddx_xVector=False
        elif self.ddx_xVector==False and self.ddx_xPosition<=0:
            self.ddx_xPosition+=self.xSpeed
            self.ddx_xVector=True
    
    def VerticalMove(self):
        if self.ddx_yVector==True and self.ddx_yPosition<SCREEN_HIGHT-16-19:
            self.ddx_yPosition+=self.ySpeed
        elif self.ddx_yVector==False and ddx_yPosition<SCREEN_HIGHT-16-19:
            self.ddx_yPosition-=self.xSpeed
        elif self.ddx_yVector==True and ddx_yPosition>=SCREEN_HIGHT-100:
            self.ddx_yPosition-=self.ySpeed
            self.ddx_yVector=False
        if self.ddx_yPosition>=110 and self.StandxPosition-16<=self.ddx_xPosition<=self.StandxPosition+72:
            self.ddx_yVector=False
        for i in range(7):
            for j in range(5):
                if self.ddx_yVector==False and self.ddx_yPosition==self.BlockYPosition[j] and self.BlockXPosition[i]<=self.ddx_xPosition<=self.BlockXPosition[i+1]:
                    self.BlockCount[i][j]-=1
                    self.ddx_yVector=True
                if self.BlockCount[i][j]==0:
                    if (i-1)*16<self.ddx_xPosition<i*16 and self.ddx_yPosition<=(j+1)*16:
                        self.ddx_yVector=False
                    elif self.ddx_xPosition==i*16 and self.ddx_yPosition<=(j+1)*16:
                        self.ddx_xVector=False
                    elif (i-1)*16<=self.ddx_xPosition and self.ddx_yPosition<=(j+1)*16:
                        self.ddx_xVector=True
        
class Stand:
    def __init__(
        self,
        yVector,
        xSpeed:int,
        StandxPosition:int,
        StandyPosition:int
        ):
        self.xSpeed=xSpeed
        self.yVector=yVector
        self.StandxPosition=StandxPosition
        self.StandyPosition=StandyPosition
        self.BotanHandlerObj=BotanHandler()
        self.ddxObj=ddx(
            xSpeed,
            ySpeed,
            ddx_xVector,
            ddx_yVector,
            ddx_xPosition,
            ddx_yPosition,
            StandxPosition,
            StandyPosition,
            BlockCount,
            BlockXPosition,
            BlockYPosition
        )
        
    def HorizonalMove(self):
        if self.BotanHandlerObj.Right() and self.StandxPosition<SCREEN_WIDTH-32: #押され続けているのを検知
            self.StandxPosition+=self.xSpeed
            if self.BotanHandlerObj.Up():
                self.StandxPosition+=self.xSpeed*2
        elif self.BotanHandlerObj.Left() and self.StandxPosition>0:
            self.StandxPosition-=self.xSpeed
            if self.BotanHandlerObj.Up():
                self.StandxPosition-=self.xSpeed*2
            
        
class App:
    def __init__(self): #初期値を与える
        self.speedup=False
        self.BotanHandlerObj=BotanHandler()
        self.ddxObj=ddx(            
            xSpeed,
            ySpeed,
            ddx_xVector,
            ddx_yVector,
            ddx_xPosition,
            ddx_yPosition,
            StandxPosition,
            StandyPosition,
            BlockCount,
            BlockXPosition,
            BlockYPosition)
        self.StandObj=Stand(xSpeed,
                            yVector,
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
        self.StandObj.HorizonalMove()
        print(self.ddxObj.ddx_yPosition)
                   
    def draw(self):
        pyxel.cls(pyxel.COLOR_NAVY)
        pyxel.blt(self.StandObj.StandxPosition,self.StandObj.StandyPosition,0,0,16,32,16,pyxel.COLOR_BLACK)
        #台
        pyxel.blt(self.ddxObj.ddx_xPosition,self.ddxObj.ddx_yPosition,0,0,0,16,16,pyxel.COLOR_BLACK)
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