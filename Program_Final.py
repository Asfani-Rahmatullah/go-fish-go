import pygame, random, sys, time
pygame.init()
pygame.mixer.init()
pygame.display.set_caption("Go Fish Go !!!")
screen=pygame.display.set_mode((1000,600))
pygame.mixer.music.load("assets/BGM.wav")
pygame.mixer.music.play(-1, 0.0)
pygame.mixer.music.set_volume(0.25)
class Aksesoris:
    def __init__(self):
        self.bg2=''
        self.x1=0
        self.x2=1000
        self.y=0
        self.jarak=20
        self.panah=''
        self.xpanah=0
        self.dpanah=0
        self.lvl=1
        self.HS_txt=''
        self.up=8
        self.font_score=pygame.font.SysFont('Arial',25,True,False)
        self.font_gagal=pygame.font.SysFont('Arial',30,True,False)
        self.font_hs=pygame.font.SysFont('Arial',25,True,False)
        self.font_new_highscore=pygame.font.SysFont('Arial',35,True,False)
        self.font_selamat=pygame.font.SysFont('Arial',50,True,False)
        self.font_score_main=pygame.font.SysFont('Calibri',20,True,False)
        self.font_tingkat=pygame.font.SysFont('Arial',30,True,False)
        self.kuning=(255,255,0)
        self.merah=(255,0,0)
        self.biru=(0,0,255)
        self.warna_gagal=(255,102,0)
        self.warna_score=(0,0,255)
        self.warna_hs=(204,51,0)
        self.warna_selamat=(51,255,0)
        self.warna_new_highscore=(255,204,0)
    def akhir(self,score):
        self.bg=pygame.image.load('assets/bg_akhir.jpg')
        self.bg=pygame.transform.scale(self.bg,(1000,600))
        screen.blit(self.bg,(0,0))
        self.score=int(score)
        txt_score=self.font_score.render('Your Score :'+str(self.score),True,self.warna_score)
        txt_gagal=self.font_gagal.render("Better Lucky Next Time",True,self.warna_gagal)
        txt_hs=self.font_hs.render('Current Highscore :'+str(self.HS),True,(255,255,255))
        txt_new_highscore=self.font_new_highscore.render('New Highscore :'+str(self.score),True,self.warna_new_highscore)
        txt_selamat=self.font_selamat.render("Congratulation!!!",True,self.warna_selamat)
        if self.HS>=self.score:
            screen.blit(txt_gagal,[300,300])
            screen.blit(txt_score,[360,350])
            screen.blit(txt_hs,[320,400])
        else:
            screen.blit(txt_selamat,[300,280])
            HSbaru=open(self.HS_txt,'w')
            screen.blit(txt_new_highscore,[380,350])
            HSbaru.write(str(self.score))
            HSbaru.close()
    def awal(self):
        self.bg=pygame.image.load('assets/bg_awal.jpg')
        self.bg=pygame.transform.scale(self.bg,(1000,600))
        screen.blit(self.bg,(0,0))
        self.panah=pygame.image.load('assets/panah.png')
        self.panah=pygame.transform.scale(self.panah,(80,50))
        screen.blit(self.panah,[self.xpanah,300])
        self.m1=pygame.image.load('assets/pemain_1.png')
        self.m1=pygame.transform.scale(self.m1,(80,50))
        screen.blit(self.m1,(0,250))
        self.m2=pygame.image.load('assets/pemain_2.png')
        self.m2=pygame.transform.scale(self.m2,(80,50))
        screen.blit(self.m2,(200,250))
        self.m3=pygame.image.load('assets/pemain_3.png')
        self.m3=pygame.transform.scale(self.m3,(80,50))                    
        screen.blit(self.m3,(400,250))
        self.m4=pygame.image.load('assets/pemain_4.png')
        self.m4=pygame.transform.scale(self.m4,(80,50))                    
        screen.blit(self.m4,(600,250))
        self.m5=pygame.image.load('assets/pemain_5.png')
        self.m5=pygame.transform.scale(self.m5,(80,50))                    
        screen.blit(self.m5,(800,250))
    def tingkat(self):
        self.bgt=pygame.image.load('assets/bg_tingkat.jpg')
        self.bgt=pygame.transform.scale(self.bgt,(1000,600))
        screen.blit(self.bgt,(0,0))
        txt_E=self.font_tingkat.render('PEMULA',True,(0,102,0))
        txt_M=self.font_tingkat.render('AMATIR',True,self.kuning)
        txt_H=self.font_tingkat.render('   PRO',True,self.merah)
        txt_P=self.font_tingkat.render('LEGEND',True,(102,0,102))
        txt_D=self.font_tingkat.render("DEWA",True,(0,0,0))
        screen.blit(txt_E,(50,250))
        screen.blit(txt_M,(250,250))
        screen.blit(txt_H,(450,250))
        screen.blit(txt_P,(650,250))
        screen.blit(txt_D,(850,250))
        self.panah=pygame.image.load('assets/panah2.png')
        self.panah=pygame.transform.scale(self.panah,(30,20))
        screen.blit(self.panah,[self.xpanah,300])
    def draw_bg(self,img,score,evo):
        #Exception Handle Highscore
        try:
            highestscorebaca=open(self.HS_txt,"r")
            self.HS=int(highestscorebaca.read())
        except ValueError:
            self.HS=0
        self.evo=evo
        self.score=score
        self.bg=pygame.image.load(img)
        self.bg2=pygame.image.load(img)
        self.bg=pygame.transform.scale(self.bg,(1000,600))
        self.bg2=pygame.transform.scale(self.bg2,(1000,600))
        screen.blit(self.bg,(self.x1,0))
        screen.blit(self.bg2,(self.x2,0))
        txt_lvl=self.font_tingkat.render('Level :'+str(self.lvl),True,(0,0,0))
        txt_score=self.font_score_main.render('Your Score :'+str(self.score),True,self.merah)
        txt_evo=self.font_score_main.render('EVOLUTION :'+str(self.evo)+'%',True,(0,51,0))
        txt_HS=self.font_score_main.render('Highest Score :'+str(self.HS),True,self.biru)
        screen.blit(txt_lvl,(700,10))
        screen.blit(txt_score,(5,10))
        screen.blit(txt_HS,(5,30))
        screen.blit(txt_evo,(450,10))
    def panah_pindah(self):
        self.xpanah+=self.dpanah
    def bg_down(self):
        self.x1-=self.up
        self.x2-=self.up
    def check_out(self):
        if self.x1<-1000:
            self.x1=1000
        elif self.x2<-1000:
            self.x2=1000
        if self.xpanah>=1000 or self.xpanah<0:
            self.xpanah-=self.dpanah
class Car:
    def __init__ (self,x,y,p,l):
        self.car=''
        self.evo=80
        self.y=y
        self.x=x
        self.dx=0
        self.width=l
        self.height=p
        self.dy=0
    def set_car(self,C):
        self.car=pygame.image.load(C)
    def draw_car(self):
        self.car=pygame.transform.scale(self.car,(self.width,self.height))
        screen.blit(self.car,[self.x,self.y])
    def draw_enemy(self,y):
        self.y=y
        self.car=pygame.transform.scale(self.car,(self.width,self.height))
        screen.blit(self.car,[self.x,self.y])
    def movexy(self):
        self.y+=self.dy
        self.x+=self.dx
    def move(self,x):
        self.x-=x
    def check_out_screen2(self,m):
        if self.x<=-900:
            self.x=m
    def check_out_screen(self):
        if self.y+self.height>=600 or self.y<0:
            self.y-=self.dy
        if self.x<0 or self.x+self.width>=1000:
            self.x-=self.dx
#Class Game
class Game:
    def __init__(self):
        self.bg=''
        self.player=''
        self.img=''
    def start(self):
        self.score=0
        self.lebar=30
        self.panjang=50
        self.bg=Aksesoris()
        self.player=Car(0,100,self.lebar,self.panjang)
        stop=False
        clock=pygame.time.Clock()
        while not stop:
            self.bg.check_out()
            for event in pygame.event.get():
                self.bg.check_out()
                if event.type==pygame.QUIT:
                    stop=True
                    pygame.quit()
                    sys.exit()                    
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_LEFT:
                        self.bg.dpanah-=200
                    elif event.key==pygame.K_RIGHT:
                        self.bg.dpanah+=200
                    if event.key==pygame.K_RETURN:
                        stop=True
                if event.type==pygame.KEYUP:
                    self.bg.dpanah=0
            self.bg.awal()
            self.bg.panah_pindah()
            pygame.display.update()
            clock.tick(60)
        if self.bg.xpanah==0:
            self.img='assets/pemain_1.png'
            self.player.set_car('assets/pemain_1.png')
            self.bg.up=8
            self.bg.lvl='EASY'
        elif self.bg.xpanah==200:
            self.img='assets/pemain_2.png'
            self.player.set_car('assets/pemain_2.png')
            self.bg.up=13
            self.bg.lvl='MEDIUM'
        elif self.bg.xpanah==400:
            self.img='assets/pemain_3.png'
            self.player.set_car('assets/pemain_3.png')
            self.bg.up=17
            self.bg.lvl='HARD'
        elif self.bg.xpanah==600:
            self.img='assets/pemain_4.png'
            self.player.set_car('assets/pemain_4.png')
            self.bg.up=13
            self.bg.lvl='MEDIUM'
        elif self.bg.xpanah==800:
            self.img='assets/pemain_5.png'
            self.player.set_car('assets/pemain_5.png')
            self.bg.up=17
            self.bg.lvl='HARD'
    def tingkat(self):
        pilih=False
        clock=pygame.time.Clock()
        self.bg.xpanah=100
        while not pilih:
            self.bg.check_out()
            for event in pygame.event.get():
                self.bg.check_out()
                if event.type==pygame.QUIT:
                    pilih=True
                    pygame.quit()
                    sys.exit()                    
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_LEFT:
                        self.bg.dpanah-=200
                    elif event.key==pygame.K_RIGHT:
                        self.bg.dpanah+=200
                    if event.key==pygame.K_RETURN:
                        pilih=True
                if event.type==pygame.KEYUP:
                    self.bg.dpanah=0
            self.bg.tingkat()
            self.bg.panah_pindah()
            pygame.display.update()
            clock.tick(60)
        if self.bg.xpanah==100:
            self.bg.up=5
            self.bg.lvl='PEMULA'
            self.bg.HS_txt='pemula.txt'
        elif self.bg.xpanah==300:
            self.bg.up=8
            self.bg.lvl='AMATIR'
            self.bg.HS_txt='amatir.txt'
        elif self.bg.xpanah==500:
            self.bg.up=10
            self.bg.lvl='PRO'
            self.bg.HS_txt='pro.txt'
        elif self.bg.xpanah==700:
            self.bg.up=15
            self.bg.lvl='LEGEND'
            self.bg.HS_txt='legend.txt'
        elif self.bg.xpanah==900:
            self.bg.up=20
            self.bg.lvl='DEWA'
            self.bg.HS_txt='dewa.txt'
    def main(self):
        stop=False
        clock=pygame.time.Clock()
        scoreawal=0
        evo=0
        #koordinat aset
        yhiu=[0,80,160,180,220,260,280,340,380,400,440,480]
        ypedang_1=[0,80,160,180,220,260,280,340,380,400,440,480]
        ypedang_2=[0,80,160,180,220,260,280,340,380,400,440,480]
        ypedang_3=[0,80,160,180,220,260,280,340,380,400,440,480]
        yorca=[0,80,160,180,220,260,280,340,380,400,440,480]
        ykoin1=[0,80,160,180,220,260,280,340,380,400,440,480]
        ykoin2=[0,80,160,180,220,260,280,340,380,400,440,480]
        ykoin3=[0,80,160,180,220,260,280,340,380,400,440,480]
        yubur1=[0,80,160,180,220,260,280,340,380,400,440,480]
        yubur2=[0,80,160,180,220,260,280,340,380,400,440,480]
        ybuntal1=[0,80,160,180,220,260,280,340,380,400,440,480]
        ybuntal2=[0,80,160,180,220,260,280,340,380,400,440,480]
        #Random Koordinat y
        random.shuffle(yubur1)
        random.shuffle(yubur2)
        random.shuffle(ybuntal1)
        random.shuffle(ybuntal2)
        random.shuffle(yhiu)
        random.shuffle(ypedang_1)
        random.shuffle(ypedang_2)
        random.shuffle(ypedang_3)
        random.shuffle(yorca)
        random.shuffle(ykoin1)
        random.shuffle(ykoin2)
        random.shuffle(ykoin3)
        #Variabel gambar
        ikan=['assets/ikan_1.png','assets/ikan_2.png','assets/ikan_3.png','assets/ikan_4.png']
        ubur=['assets/ubur_1.png','assets/ubur_2.png','assets/ubur_3.png','assets/ubur_4.png']
        orca=['assets/orca1.png','assets/orca2.png','assets/orca3.png']
        hiu=['assets/hiu_4.png','assets/hiu_1.png','assets/hiu_2.png','assets/hiu_3.png','assets/hiu_5.png']
        buntal=['assets/buntal_1.png','assets/buntal_2.png','assets/buntal_3.png','assets/buntal_4.png','assets/buntal_5.png']
        pedang=['assets/pedang_1.png','assets/pedang_2.png','assets/pedang_3.png','assets/pedang_4.png','assets/pedang_5.png','assets/pedang_6.png','assets/pedang_7.png']
        #Enemy Object
        self.ubur1=Car(1500,yubur1[random.randrange(0,11)],60,30)
        self.ubur2=Car(1500,yubur2[random.randrange(0,11)],60,30)
        self.buntal1=Car(1500,ybuntal1[random.randrange(0,11)],50,50)
        self.buntal2=Car(1500,ybuntal2[random.randrange(0,11)],50,50)
        self.hiu=Car(5000,yhiu[random.randrange(0,11)], 100, 180)
        self.pedang1=Car(700,ypedang_1[random.randrange(0,11)],30,100)
        self.pedang3=Car(800,ypedang_1[random.randrange(0,11)],30,100)
        self.ikan1=Car(1000,ykoin1[random.randrange(0,11)],25,35)
        self.ikan2=Car(1200,ykoin2[random.randrange(0,11)],25,35)
        self.ikan3=Car(1300,ykoin3[random.randrange(0,11)],25,35)
        self.pedang2=Car(900,ypedang_2[random.randrange(0,11)],30,100)
        self.orca=Car(10000,yorca[random.randrange(0,11)],130,200)
        self.player.check_out_screen()
        #set Enemy
        self.pedang1.set_car(pedang[random.randrange(0,2)])
        self.pedang2.set_car(pedang[random.randrange(0,2)])
        self.pedang3.set_car(pedang[random.randrange(0,2)])
        self.orca.set_car(orca[random.randrange(0,2)])
        self.hiu.set_car(hiu[random.randrange(0,3)])
        self.orca.set_car(orca[random.randrange(0,2)])
        self.ikan1.set_car(ikan[random.randrange(0,3)])
        self.ikan2.set_car(ikan[random.randrange(0,3)])
        self.ikan3.set_car(ikan[random.randrange(0,3)])
        self.ubur1.set_car(ubur[random.randrange(0,3)])
        self.ubur2.set_car(ubur[random.randrange(0,3)])
        self.buntal1.set_car(buntal[random.randrange(0,4)])
        self.buntal2.set_car(buntal[random.randrange(0,4)])
        #set volume
        self.makan_fx=pygame.mixer.Sound("assets/koin.wav")
        self.makan_fx.set_volume(0.5)
        self.end=pygame.mixer.Sound('assets/end.wav')
        self.end.set_volume(0.25)
        self.setrum=pygame.mixer.Sound('assets/setrum.wav')
        self.setrum.set_volume(0.25)
        self.lvl_up=pygame.mixer.Sound("assets/lvl_up.wav")
        self.lvl_up.set_volume(1)
        while not stop:
            for event in pygame.event.get():
                self.player.check_out_screen()
                if event.type==pygame.QUIT:
                    self.end.play()
                    stop=True
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_UP:
                        self.player.dy=-25
                    if event.key==pygame.K_DOWN:
                        self.player.dy=+25
                    if event.key==pygame.K_LEFT:
                        self.player.dx=-25
                    if event.key==pygame.K_RIGHT:
                        self.player.dx=+25
                if event.type==pygame.KEYUP:
                    self.player.dy=0
                    self.player.dx=0
            #Shuffle Koordinat X
            if self.pedang1.x<=-200:
                random.shuffle(ypedang_1)
                self.pedang1.set_car(pedang[random.randrange(0,6)])
            if self.pedang3.x<=-200:
                random.shuffle(ypedang_3)
                self.pedang3.set_car(pedang[random.randrange(0,6)])
            if self.hiu.x<=-200:
                random.shuffle(yhiu)
                self.hiu.set_car(hiu[random.randrange(0,4)]) 
            if self.pedang2.x<=-200:
                random.shuffle(ypedang_2)
                self.pedang2.set_car(pedang[random.randrange(0,6)])
            if self.ikan1.x<=-200:
                random.shuffle(ykoin1)
                self.ikan1.set_car(ikan[random.randrange(0,3)])
            if self.ikan2.x<=-200:
                random.shuffle(ykoin2)
                self.ikan2.set_car(ikan[random.randrange(0,3)])
            if self.ikan3.x<=-200:
                random.shuffle(ykoin3)
                self.ikan3.set_car(ikan[random.randrange(0,3)])
            if self.ubur1.x <=-100:
                random.shuffle(yubur1)
                self.ubur1.set_car(ubur[random.randrange(0,3)])
            if self.ubur2.x<=-100:
                random.shuffle(yubur2)
                self.ubur2.set_car(ubur[random.randrange(0,3)])
            if self.buntal1.x<=-100:
                random.shuffle(ybuntal1)
                self.buntal1.set_car(buntal[random.randrange(0,4)])
            if self.buntal2.x<=-100:
                random.shuffle(ybuntal2)
                self.buntal2.set_car(buntal[random.randrange(0,4)])
            #Check Collusion
            if self.pedang1.y+self.pedang1.height>=self.player.y and self.pedang1.y<self.player.y+self.player.height and self.pedang1.x+self.pedang1.width>self.player.x and self.pedang1.x<self.player.x+self.player.width:
                if self.player.height>self.pedang1.height:
                    self.pedang1.x=-400
                    self.makan_fx.play()
                    evo+=10
                else:
                    self.end.play()
                    stop=True
            if self.pedang2.y+self.pedang2.height>=self.player.y and self.pedang2.y<self.player.y+self.player.height and self.pedang2.x+self.pedang2.width>self.player.x and self.pedang2.x<self.player.x+self.player.width:
                if self.player.height>self.pedang1.height:
                    self.pedang2.x=-400
                    self.makan_fx.play()
                    evo+=10
                else:
                    self.end.play()
                    stop=True
            if self.pedang3.y+self.pedang3.height>=self.player.y and self.pedang3.y<self.player.y+self.player.height and self.pedang3.x+self.pedang3.width>self.player.x and self.pedang3.x<self.player.x+self.player.width:
                if self.player.height>self.pedang1.height:
                    self.pedang3.x=-400
                    evo+=10
                    self.makan_fx.play()
                else:
                    self.end.play()
                    stop=True
            if self.hiu.y+self.hiu.height>=self.player.y and self.hiu.y<self.player.y+self.player.height and self.hiu.x+self.hiu.width>self.player.x and self.hiu.x<self.player.x+self.player.width:
                if self.player.height>self.hiu.height:
                    self.hiu.x=-400
                    evo+=20
                    self.makan_fx.play()
                else:
                    self.end.play()
                    stop=True
            if self.orca.y+self.orca.height>=self.player.y and self.orca.y<self.player.y+self.player.height and self.orca.x+self.orca.width>self.player.x and self.orca.x<self.player.x+self.player.width:
                if self.player.height>self.orca.height:
                    self.orca.x=-400
                    self.makan_fx.play()
                    evo+=25
                else:
                    self.end.play()
                    stop=True
            if self.ikan1.y+self.ikan1.height>=self.player.y and self.ikan1.y<self.player.y+self.player.height and self.ikan1.x+self.ikan1.width>self.player.x and self.ikan1.x<self.player.x+self.player.width:
                self.ikan1.x=-400
                evo+=5
                self.makan_fx.play()
            if self.ikan2.y+self.ikan2.height>=self.player.y and self.ikan2.y<self.player.y+self.player.height and self.ikan2.x+self.ikan2.width>self.player.x and self.ikan2.x<self.player.x+self.player.width:
                self.ikan2.x=-400
                evo+=5
                self.makan_fx.play()
            if self.ikan3.y+self.ikan3.height>=self.player.y and self.ikan3.y<self.player.y+self.player.height and self.ikan3.x+self.ikan3.width>self.player.x and self.ikan3.x<self.player.x+self.player.width:
                evo+=5
                self.ikan3.x=-400
                self.makan_fx.play()
            if self.ubur1.y+self.ubur1.height>=self.player.y and self.ubur1.y<self.player.y+self.player.height and self.ubur1.x+self.ubur1.width>self.player.x and self.ubur1.x<self.player.x+self.player.width:
                self.setrum.play()
                scoreawal-=20
                self.ubur1.x-=self.ubur1.width
            if self.ubur2.y+self.ubur2.height>=self.player.y and self.ubur2.y<self.player.y+self.player.height and self.ubur2.x+self.ubur2.width>self.player.x and self.ubur2.x<self.player.x+self.player.width:
                self.setrum.play()
                scoreawal-=20
                self.ubur2.x-=self.ubur2.width
            if self.buntal1.y+self.buntal1.height>=self.player.y and self.buntal1.y<self.player.y+self.player.height and self.buntal1.x+self.buntal1.width>self.player.x and self.buntal1.x<self.player.x+self.player.width:
                self.end.play()
                stop=True
            if self.buntal2.y+self.buntal2.height>=self.player.y and self.buntal2.y<self.player.y+self.player.height and self.buntal2.x+self.buntal2.width>self.player.x and self.buntal2.x<self.player.x+self.player.width:
                self.end.play()
                stop=True            
            if evo>=100:
                self.lvl_up.play()
                scoreawal+=50
                self.lebar+=10
                self.panjang+=10
                self.player=Car(self.player.x,self.player.y,self.lebar,self.panjang)
                self.player.set_car(self.img)
                evo=evo-100
            self.bg.draw_bg('bg2.jpg',self.score,evo)
            scoreawal+=0.5
            self.score=int(scoreawal//10)
            self.bg.bg_down()
            self.player.draw_car()
            self.player.movexy()
            self.bg.check_out()
            #Draw Objek            
            self.pedang1.draw_enemy(ypedang_1[3])
            self.pedang2.draw_enemy(ypedang_2[5])
            self.pedang3.draw_enemy(ypedang_3[7])            
            self.ikan1.draw_enemy(ykoin1[6])
            self.ikan2.draw_enemy(ykoin2[1])
            self.ikan3.draw_enemy(ykoin3[4])
            self.orca.draw_enemy(yorca[9])
            self.hiu.draw_enemy(yhiu[10])
            self.buntal1.draw_enemy(ybuntal1[1])
            self.buntal2.draw_enemy(ybuntal2[3])
            self.ubur1.draw_enemy(yubur1[4])
            self.ubur2.draw_enemy(yubur2[5])
            #Move Objek
            self.ubur1.move(5)
            self.ubur2.move(5)
            self.buntal1.move(7)
            self.buntal2.move(7)
            self.pedang1.move(10)
            self.pedang2.move(15)            
            self.pedang3.move(17)
            self.hiu.move(20)
            self.orca.move(23)
            self.ikan1.move(12)
            self.ikan2.move(20)
            self.ikan3.move(8)
            #Check Out Screen
            self.player.check_out_screen()
            self.pedang1.check_out_screen2(1200)
            self.pedang2.check_out_screen2(1200)
            self.pedang3.check_out_screen2(1200)
            self.hiu.check_out_screen2(7500)
            self.ikan1.check_out_screen2(1300)
            self.ikan2.check_out_screen2(1300)
            self.ikan3.check_out_screen2(1300)
            self.buntal1.check_out_screen2(1200)
            self.buntal2.check_out_screen2(1250)
            self.ubur1.check_out_screen2(1100)
            self.ubur2.check_out_screen2(1400)
            pygame.display.update()
            clock.tick(600)
            pygame.display.flip()
    def over(self):
        self.panjang=50
        self.lebar=30
        stop=False
        while not stop:
            self.bg.akhir(self.score)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    stop=True
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_SPACE:
                        time.sleep(1)
                        self.start()
                        self.tingkat()
                        self.main()
        pygame.quit()
#MAIN PROGRAM !!!
Pemain=Game()
Pemain.start()
Pemain.tingkat()
Pemain.main()
Pemain.over()
