import pyxel

SCREEN_WIDTH =120
SCREEN_HIGHT =160
i=0
j=0

class BotanHandler:
    def Right():
        if pyxel.btn(pyxel.KEY_RIGHT):
            return True
        else:
            return False
    def Left():
        if pyxel.btn(pyxel.KEY_LEFT):
            return True
        else:
            return False
    def Up():
        if pyxel.btn(pyxel.KEY_UP):
            return True
        else:
            return False

class Stand:
    def __init__(self):
        self.xVector=True
        self.xSpeed=0
        self.ySpeed=83
        self.yVector=True
    def HorizonalMove(self):
        if self.xVector==True and self.xSpeed<SCREEN_WIDTH-12:
            self.xSpeed+=1
            self.xVector=True
        elif self.xVector==True and self.xSpeed>=SCREEN_WIDTH-12:
            self.xSpeed-=1
            self.xVector=False
        elif self.xVector==False and self.xSpeed>0:
            self.xSpeed-=1
            self.xVector=False
        elif self.xVector==False and self.xSpeed<=0:
            self.xSpeed+=1
            self.xVector=True
        elif self.xVector==True and self.xSpeed<SCREEN_WIDTH-12:
            self.xSpeed+=2
            self.xVector=True
        elif self.xVector==True and self.xSpeed>=SCREEN_WIDTH-12:
            self.xSpeed-=2
            self.xVector=False
        elif self.xVector==False and self.xSpeed>0:
            self.xSpeed+=-2
            self.xVector=False
        elif self.xVector==False and self.xSpeed<=0:
            self.xSpeed+=2
            self.xVector=True
    
    def VerticalMove(self):
        if self.yVector==True and self.ySpeed<SCREEN_HIGHT-16-19:
            self.speedup=False
            self.ySpeed+=1
            self.yVector=True
        elif self.yVector==True and self.ySpeed>=SCREEN_HIGHT-16-19:
            self.ySpeed+=-1
            self.yVector=False
        elif self.yVector==False and self.ySpeed>self.top[self.topnum]:
            self.ySpeed+=-1
            self.yVector=False
        elif self.yVector==False and self.ySpeed<=self.top[self.topnum]:
            self.speedup=False
            self.xSpeed+=1
            self.yVector=True
            
            for i in range(7):
                if i*16<=self.xSpeed<=i*16+16 and self.count1[i]==0 and self.topnum==5:
                    self.flags1[i]=True
                    self.count1[i]=1
                elif i*16<=self.xSpeed<=i*16+16 and self.count1[i]==1 and self.topnum==5:
                    self.flags2[i]=True
                    self.count1[i]=2
                elif i*16<=self.xSpeed<=i*16+16 and self.count1[i]==2 and self.topnum==5:
                    self.flags3[i]=True
                    self.count1[i]=3
                elif self.count1==[3]*7 and self.topnum==5:
                    self.topnum+=-1
                    self.count1=[0]*7
                    self.flags1=[False]*7
                    self.flags2=[False]*7
                    self.flags3=[False]*7
                elif i*16<=self.xSpeed<=i*16+16 and self.count1[i]==0 and self.topnum==4:
                    self.flags1[i]=True
                    self.count1[i]=1
                elif i*16<=self.xSpeed<=i*16+16 and self.count1[i]==1 and self.topnum==4:
                    self.flags2[i]=True
                    self.count1[i]=2
                elif i*16<=self.xSpeed<=i*16+16 and self.count1[i]==2 and self.topnum==4:
                    self.flags3[i]=True
                    self.count1[i]=3
                elif self.count1==[3]*7 and self.topnum==4:
                    self.topnum+=-1
                    self.count1=[0]*7
                    self.flags1=[False]*7
                    self.flags2=[False]*7
                    self.flags3=[False]*7
                elif i*16<=self.xSpeed<=i*16+16 and self.count1[i]==0 and self.topnum==3:
                    self.flags1[i]=True
                    self.count1[i]=1
                elif i*16<=self.xSpeed<=i*16+16 and self.count1[i]==1 and self.topnum==3:
                    self.flags2[i]=True
                    self.count1[i]=2
                elif i*16<=self.xSpeed<=i*16+16 and self.count1[i]==2 and self.topnum==3:
                    self.flags3[i]=True
                    self.count1[i]=3
                elif self.count1==[3]*7 and self.topnum==3:
                    self.topnum+=-1
                    self.count1=[0]*7
                    self.flags1=[False]*7
                    self.flags2=[False]*7
                    self.flags3=[False]*7
                elif i*16<=self.xSpeed<=i*16+16 and self.count1[i]==0 and self.topnum==2:
                    self.flags1[i]=True
                    self.count1[i]=1
                elif i*16<=self.xSpeed<=i*16+16 and self.count1[i]==1 and self.topnum==2:
                    self.flags2[i]=True
                    self.count1[i]=2
                elif i*16<=self.xSpeed<=i*16+16 and self.count1[i]==2 and self.topnum==2:
                    self.flags3[i]=True
                    self.count1[i]=3
                elif self.count1==[3]*7 and self.topnum==2:
                    self.topnum+=-1
                    self.count1=[0]*7
                    self.flags1=[False]*7
                    self.flags2=[False]*7
                    self.flags3=[False]*7
                elif i*16<=self.xSpeed<=i*16+16 and self.count1[i]==0 and self.topnum==1:
                    self.flags1[i]=True
                    self.count1[i]=1
                elif i*16<=self.xSpeed<=i*16+16 and self.count1[i]==1 and self.topnum==1:
                    self.flags2[i]=True
                    self.count1[i]=2
                elif i*16<=self.xSpeed<=i*16+16 and self.count1[i]==2 and self.topnum==1:
                    self.flags3[i]=True
                    self.count1[i]=3
                elif self.count1==[3]*7 and self.topnum==1:
                    self.topnum+=-1
                    self.count1=[0]*7
                    self.flags1=[False]*7
                    self.flags2=[False]*7
                    self.flags3=[False]*7
    
    def Reflection(self):
        
class App:
    def __init__(self): #初期値を与える
        self.player_x=40
        # self.xSpeed=0
        self.ySpeed=83
        # self.xVector=True
        self.yVector=True
        self.top={5:80,4:64,3:48,2:32,1:16}
        self.topnum=5
        self.count1=[0]*7
        self.flags1=[False]*7
        self.flags2=[False]*7
        self.flags3=[False]*7
        self.speedup=False
        BotanHandler=BotanHandler()
        Stand=Stand()
        pyxel.init(120,160,title="d/dx")
        pyxel.load("my_resource.pyxres") #イメージバンクの画像を読み込み
        pyxel.run(self.update,self.draw)
        

    def update(self): #フレーム更新時の処理
        if pyxel.btnp(pyxel.KEY_ESCAPE): #押した瞬間を検知
            pyxel.quit()
        
        if BotanHandler.Right() and self.player_x<SCREEN_WIDTH-32: #押され続けているのを検知
            self.player_x+=1
            if pyxel.btn(pyxel.KEY_UP):
                self.player_x+=1
        elif BotanHandler.Left() and self.player_x>0:
            self.player_x-=1
            if BotanHandler.Up():
                self.player_x-=1
        #台の操作
        
        Stand.HorizonalMove(self)
        Stand.VerticalMove(self)
                
       
        #ddxの当たり判定
                    
        
        if self.yVector==True and self.ySpeed==SCREEN_HIGHT*3//4-8:
            if self.player_x-16<=self.xSpeed<=self.player_x+36:
                self.yVector=False
                if pyxel.btn(pyxel.KEY_RIGHT) and pyxel.btn(pyxel.KEY_UP):
                    self.xSpeed+=1
                    self.speedup=True
                elif pyxel.btn(pyxel.KEY_LEFT) and pyxel.btn(pyxel.KEY_UP):
                    self.xSpeed-=1
                    self.speedup=True
        #台の当たり判定
        
                   
    def draw(self):
        pyxel.cls(pyxel.COLOR_NAVY)
        pyxel.blt(self.player_x,SCREEN_HIGHT*3//4,0,0,16,32,16,pyxel.COLOR_BLACK)
        #台
        pyxel.blt(self.xSpeed,self.ySpeed,0,0,0,16,16,pyxel.COLOR_BLACK)
        #d/dx
        # for i in range(4):
        #     for j in range(15):
        #         pyxel.blt(j*8,i*8,0,16,0,8,16,pyxel.COLOR_BLACK)
        #x
        for i in range(5):
            for j in range(7):
                if self.flags1[j]==False and self.topnum==5:
                    pyxel.blt(j*16+8,i*16,0,24,0,16,16,pyxel.COLOR_BLACK)
                elif self.flags1[j]==True and self.count1[j]==1 and self.topnum==5:
                    pyxel.blt(j*16+8,32+36,0,32,16,11,8,pyxel.COLOR_BLACK)  #2x
                    pyxel.blt(j*16+8,0,0,24,0,16,16,pyxel.COLOR_BLACK)  #x^2
                    pyxel.blt(j*16+8,16,0,24,0,16,16,pyxel.COLOR_BLACK)
                    pyxel.blt(j*16+8,32,0,24,0,16,16,pyxel.COLOR_BLACK)
                    pyxel.blt(j*16+8,48,0,24,0,16,16,pyxel.COLOR_BLACK)
                elif self.flags2[j]==True and self.count1[j]==2 and self.topnum==5:
                    pyxel.blt(j*16+8,32+36,0,16,32,12,10,pyxel.COLOR_BLACK)  #2
                    pyxel.blt(j*16+8,0,0,24,0,16,16,pyxel.COLOR_BLACK)
                    pyxel.blt(j*16+8,16,0,24,0,16,16,pyxel.COLOR_BLACK)
                    pyxel.blt(j*16+8,32,0,24,0,16,16,pyxel.COLOR_BLACK)
                    pyxel.blt(j*16+8,48,0,24,0,16,16,pyxel.COLOR_BLACK)
                elif self.flags3[j]==True and self.count1[j]==3 and self.topnum==5:
                    pyxel.blt(j*16+8,32+36,0,32,32,16,16,pyxel.COLOR_BLACK)  # 
                    pyxel.blt(j*16+8,0,0,24,0,16,16,pyxel.COLOR_BLACK)
                    pyxel.blt(j*16+8,16,0,24,0,16,16,pyxel.COLOR_BLACK)
                    pyxel.blt(j*16+8,32,0,24,0,16,16,pyxel.COLOR_BLACK)
                    pyxel.blt(j*16+8,48,0,24,0,16,16,pyxel.COLOR_BLACK)
                elif self.count1[j]==0 and self.topnum==4:
                    pyxel.blt(j*16+8,32+36,0,32,32,16,16,pyxel.COLOR_BLACK)
                    pyxel.blt(j*16+8,0,0,24,0,16,16,pyxel.COLOR_BLACK)
                    pyxel.blt(j*16+8,16,0,24,0,16,16,pyxel.COLOR_BLACK)
                    pyxel.blt(j*16+8,32,0,24,0,16,16,pyxel.COLOR_BLACK)
                    pyxel.blt(j*16+8,48,0,24,0,16,16,pyxel.COLOR_BLACK)
                elif self.flags1[j]==True and self.count1[j]==1 and self.topnum==4:
                    pyxel.blt(j*16+8,32+36,0,32,32,16,16,pyxel.COLOR_BLACK)
                    pyxel.blt(j*16+8,48,0,32,16,11,8,pyxel.COLOR_BLACK)
                    pyxel.blt(j*16+8,0,0,24,0,16,16,pyxel.COLOR_BLACK)
                    pyxel.blt(j*16+8,16,0,24,0,16,16,pyxel.COLOR_BLACK)
                    pyxel.blt(j*16+8,32,0,24,0,16,16,pyxel.COLOR_BLACK)
                elif self.flags2[j]==True and self.count1[j]==2 and self.topnum==4:
                    pyxel.blt(j*16+8,32+36,0,32,32,16,16,pyxel.COLOR_BLACK)
                    pyxel.blt(j*16+8,48,0,16,32,12,10,pyxel.COLOR_BLACK)
                    pyxel.blt(j*16+8,0,0,24,0,16,16,pyxel.COLOR_BLACK)
                    pyxel.blt(j*16+8,16,0,24,0,16,16,pyxel.COLOR_BLACK)
                    pyxel.blt(j*16+8,32,0,24,0,16,16,pyxel.COLOR_BLACK)
                elif self.flags3[j]==True and self.count1[j]==3 and self.topnum==4:
                    pyxel.blt(j*16+8,32+36,0,32,32,16,16,pyxel.COLOR_BLACK)
                    pyxel.blt(j*16+8,48,0,32,32,16,16,pyxel.COLOR_BLACK)
                    pyxel.blt(j*16+8,0,0,24,0,16,16,pyxel.COLOR_BLACK)
                    pyxel.blt(j*16+8,16,0,24,0,16,16,pyxel.COLOR_BLACK)
                    pyxel.blt(j*16+8,32,0,24,0,16,16,pyxel.COLOR_BLACK)
                elif self.count1[j]==0 and self.topnum==3:
                    pyxel.blt(j*16+8,32+36,0,32,32,16,16,pyxel.COLOR_BLACK) 
                    pyxel.blt(j*16+8,48,0,32,32,16,16,pyxel.COLOR_BLACK)
                    pyxel.blt(j*16+8,0,0,24,0,16,16,pyxel.COLOR_BLACK)
                    pyxel.blt(j*16+8,16,0,24,0,16,16,pyxel.COLOR_BLACK)
                    pyxel.blt(j*16+8,32,0,24,0,16,16,pyxel.COLOR_BLACK)
                elif self.flags1[j]==True and self.count1[j]==1 and self.topnum==3:
                    pyxel.blt(j*16+8,32+36,0,32,32,16,16,pyxel.COLOR_BLACK) 
                    pyxel.blt(j*16+8,48,0,32,32,16,16,pyxel.COLOR_BLACK)
                    pyxel.blt(j*16+8,32,0,32,16,11,8,pyxel.COLOR_BLACK)
                    pyxel.blt(j*16+8,16,0,24,0,16,16,pyxel.COLOR_BLACK)
                    pyxel.blt(j*16+8,0,0,24,0,16,16,pyxel.COLOR_BLACK)
                elif self.flags2[j]==True and self.count1[j]==2 and self.topnum==3:
                    pyxel.blt(j*16+8,32+36,0,32,32,16,16,pyxel.COLOR_BLACK) 
                    pyxel.blt(j*16+8,48,0,32,32,16,16,pyxel.COLOR_BLACK)
                    pyxel.blt(j*16+8,32,0,16,32,12,10,pyxel.COLOR_BLACK)
                    pyxel.blt(j*16+8,16,0,24,0,16,16,pyxel.COLOR_BLACK)
                    pyxel.blt(j*16+8,0,0,24,0,16,16,pyxel.COLOR_BLACK)
                elif self.flags3[j]==True and self.count1[j]==3 and self.topnum==3:
                    pyxel.blt(j*16+8,32+36,0,32,32,16,16,pyxel.COLOR_BLACK) 
                    pyxel.blt(j*16+8,48,0,32,32,16,16,pyxel.COLOR_BLACK)
                    pyxel.blt(j*16+8,32,0,32,32,16,16,pyxel.COLOR_BLACK)
                    pyxel.blt(j*16+8,16,0,24,0,16,16,pyxel.COLOR_BLACK)
                    pyxel.blt(j*16+8,0,0,24,0,16,16,pyxel.COLOR_BLACK)
                elif self.count1[j]==0 and self.topnum==2:
                    pyxel.blt(j*16+8,32+36,0,32,32,16,16,pyxel.COLOR_BLACK) 
                    pyxel.blt(j*16+8,48,0,32,32,16,16,pyxel.COLOR_BLACK)
                    pyxel.blt(j*16+8,32,0,32,32,16,16,pyxel.COLOR_BLACK)
                    pyxel.blt(j*16+8,16,0,24,0,16,16,pyxel.COLOR_BLACK)
                    pyxel.blt(j*16+8,0,0,24,0,16,16,pyxel.COLOR_BLACK)
                elif self.flags1[j]==True and self.count1[j]==1 and self.topnum==2:
                    pyxel.blt(j*16+8,32+36,0,32,32,16,16,pyxel.COLOR_BLACK) 
                    pyxel.blt(j*16+8,48,0,32,32,16,16,pyxel.COLOR_BLACK)
                    pyxel.blt(j*16+8,32,0,32,32,16,16,pyxel.COLOR_BLACK)
                    pyxel.blt(j*16+8,16,0,32,16,11,8,pyxel.COLOR_BLACK)
                    pyxel.blt(j*16+8,0,0,24,0,16,16,pyxel.COLOR_BLACK)
                elif self.flags2[j]==True and self.count1[j]==2 and self.topnum==2:
                    pyxel.blt(j*16+8,32+36,0,32,32,16,16,pyxel.COLOR_BLACK) 
                    pyxel.blt(j*16+8,48,0,32,32,16,16,pyxel.COLOR_BLACK)
                    pyxel.blt(j*16+8,32,0,32,32,16,16,pyxel.COLOR_BLACK)
                    pyxel.blt(j*16+8,16,0,16,32,12,10,pyxel.COLOR_BLACK)
                    pyxel.blt(j*16+8,0,0,24,0,16,16,pyxel.COLOR_BLACK)
                elif self.flags3[j]==True and self.count1[j]==3 and self.topnum==2:
                    pyxel.blt(j*16+8,32+36,0,32,32,16,16,pyxel.COLOR_BLACK) 
                    pyxel.blt(j*16+8,48,0,32,32,16,16,pyxel.COLOR_BLACK)
                    pyxel.blt(j*16+8,32,0,32,32,16,16,pyxel.COLOR_BLACK)
                    pyxel.blt(j*16+8,16,0,32,32,16,16,pyxel.COLOR_BLACK)
                    pyxel.blt(j*16+8,0,0,24,0,16,16,pyxel.COLOR_BLACK)
                elif self.count1[j]==0 and self.topnum==1:
                    pyxel.blt(j*16+8,32+36,0,32,32,16,16,pyxel.COLOR_BLACK) 
                    pyxel.blt(j*16+8,48,0,32,32,16,16,pyxel.COLOR_BLACK)
                    pyxel.blt(j*16+8,32,0,32,32,16,16,pyxel.COLOR_BLACK)
                    pyxel.blt(j*16+8,16,0,32,32,16,16,pyxel.COLOR_BLACK)
                    pyxel.blt(j*16+8,0,0,24,0,16,16,pyxel.COLOR_BLACK)
                elif self.flags1[j]==True and self.count1[j]==1 and self.topnum==1:
                    pyxel.blt(j*16+8,32+36,0,32,32,16,16,pyxel.COLOR_BLACK) 
                    pyxel.blt(j*16+8,48,0,32,32,16,16,pyxel.COLOR_BLACK)
                    pyxel.blt(j*16+8,32,0,32,32,16,16,pyxel.COLOR_BLACK)
                    pyxel.blt(j*16+8,16,0,32,32,16,16,pyxel.COLOR_BLACK)
                    pyxel.blt(j*16+8,0,0,32,16,11,8,pyxel.COLOR_BLACK)
                elif self.flags2[j]==True and self.count1[j]==2 and self.topnum==1:
                    pyxel.blt(j*16+8,32+36,0,32,32,16,16,pyxel.COLOR_BLACK) 
                    pyxel.blt(j*16+8,48,0,32,32,16,16,pyxel.COLOR_BLACK)
                    pyxel.blt(j*16+8,32,0,32,32,16,16,pyxel.COLOR_BLACK)
                    pyxel.blt(j*16+8,16,0,32,32,16,16,pyxel.COLOR_BLACK)
                    pyxel.blt(j*16+8,0,0,16,32,12,10,pyxel.COLOR_BLACK)
                elif self.flags3[j]==True and self.count1[j]==3 and self.topnum==1:
                    pyxel.blt(j*16+8,32+36,0,32,32,16,16,pyxel.COLOR_BLACK) 
                    pyxel.blt(j*16+8,48,0,32,32,16,16,pyxel.COLOR_BLACK)
                    pyxel.blt(j*16+8,32,0,32,32,16,16,pyxel.COLOR_BLACK)
                    pyxel.blt(j*16+8,16,0,32,32,16,16,pyxel.COLOR_BLACK)
                    pyxel.blt(j*16+8,0,0,32,32,16,16,pyxel.COLOR_BLACK)
        #x^2
        for i in range(8):
            pyxel.blt(i*15,135,0,0,28,15,19,pyxel.COLOR_BLACK)
        #e^x
  
App()