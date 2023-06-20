
#se importa pygame y random
import pygame
import random

#se inicia pygame y el mixer de sonido
pygame.init()
pygame.mixer.init()

#se cargan los sonidos
coco_en_barril=pygame.mixer.Sound("Juego Cocos/sonidos/golpe_coco.mp3")
banana_en_barril=pygame.mixer.Sound("Juego Cocos/sonidos/banana_en_barril.mp3")
final_juego=pygame.mixer.Sound("Juego Cocos/sonidos/fin_juego.mp3")
sonido_fondo = pygame.mixer.Sound("Juego Cocos/sonidos/sonido_fondo.mp3")

#musica de fondo
pygame.mixer.Sound.play(sonido_fondo, -1)

#dimensiones de pantalla
pantalla_ancho=800
pantalla_alto=600

#pantalla
pantalla=pygame.display.set_mode((pantalla_ancho,pantalla_alto))
icono=pygame.image.load("Juego Cocos/barril.png")
pygame.display.set_icon(icono)

#titulo
pygame.display.set_caption("Atrapa Cocos")

#cargar y dibujar fondo
fondo_imagen=pygame.image.load("Juego Cocos/fondo_palmeras.png")
def dibujar_fondo():
    fondo_escala=pygame.transform.scale(fondo_imagen,(pantalla_ancho,pantalla_alto))
    pantalla.blit(fondo_escala,(0,0))

#fotogramas por segundo
reloj=pygame.time.Clock()
FPS=60

#fuentes para texto
comic=pygame.font.match_font('Comic Sans MS')
arial=pygame.font.match_font('Arial')

#colores
rojo=(203,50,52)
blanco=(255,255,255)
azul=(0,0,255)
amarillo=(255,255,0)

#mostrar texto en pantalla
def muestra_texto(pantalla,fuente,texto,color,dimensiones,x,y):
	tipo_letra=pygame.font.Font(fuente,dimensiones)
	superficie=tipo_letra.render(texto,True,color)
	rectangulo=superficie.get_rect()
	rectangulo.center = (x, y)
	pantalla.blit(superficie,rectangulo)

def pantalla_principal():  
    pantalla.fill(amarillo)
    muestra_texto(pantalla,comic,"AtRaPa CoCoS",rojo,66, pantalla_ancho // 2, pantalla_alto // 4)
    muestra_texto(pantalla,comic,"AtRaPa CoCoS",azul,65, pantalla_ancho // 2, pantalla_alto // 4)
    pygame.draw.rect(pantalla,rojo,[320,300,142,42]) 
    pygame.draw.rect(pantalla,rojo,[320,400,142,42])
    pygame.draw.rect(pantalla,blanco,[320,300,140,40]) 
    pygame.draw.rect(pantalla,blanco,[320,400,140,40]) 
    muestra_texto(pantalla,comic,"Jugar!",rojo,28,385,318)
    muestra_texto(pantalla,comic,"Salir",azul,30,385,418)
    pygame.display.flip()
    esperar= True
    while esperar:
        reloj.tick(60)
        mouse=pygame.mouse.get_pos()
        for event in pygame.event.get(): 
            if mouse[0]>320 and mouse[0]<460 and mouse[1]>300 and mouse[1]<340:
                if event.type==pygame.MOUSEBUTTONDOWN:
                    esperar=False
            if mouse[0]>320 and mouse[0]<460 and mouse[1]>400 and mouse[1]<440:
                if event.type==pygame.MOUSEBUTTONDOWN:
                    pygame.quit()
            if event.type==pygame.QUIT:
                pygame.quit()
                
#clase cocos
class Cocos(pygame.sprite.Sprite):

    #se carga imagen, velocidad y posicion
    def __init__(self,x,y):
        super().__init__()
        self.imagen_aleatoria=random.randrange(2)
        if self.imagen_aleatoria==0:
            self.image=pygame.image.load("Juego Cocos/coco1.png")
            self.velocidad_y=2
        if self.imagen_aleatoria==1:
            self.image=pygame.image.load("Juego Cocos/coco2.png")
            self.velocidad_y=4
        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y
    
    #dibujar en pantalla
    def dibujar(self):
        pantalla.blit(self.image,self.rect)

    #actualizacion de posicion
    def update(self):
        self.rect.y += self.velocidad_y

    #se reinicia el objeto en posicion aleatoria   
    def reiniciar(self):
        pos_aleatoria=random.randrange(8)
        if pos_aleatoria==0:
            self.rect.x=50
            self.rect.y=200
        if pos_aleatoria==1:
            self.rect.x=100
            self.rect.y=200
        if pos_aleatoria==2:
            self.rect.x=200
            self.rect.y=300
        if pos_aleatoria==3:
            self.rect.x=300
            self.rect.y=300
        if pos_aleatoria==4:
            self.rect.x=pantalla_ancho//2
            self.rect.y=250
        if pos_aleatoria==5:
            self.rect.x=480
            self.rect.y=250
        if pos_aleatoria==6:
            self.rect.x=600
            self.rect.y=250
        if pos_aleatoria==7:
            self.rect.x=730
            self.rect.y=250

    #colision con barril, suma de puntos y limites de pantalla
    def Colision(self):
        puntos=0
        colision=20
        if self.rect.y> pantalla_alto:
           self.reiniciar()
        if self.rect.colliderect(barril.rect):
           if self.rect.bottom - barril.rect.top< colision:
               if self.velocidad_y==2:
                  puntos +=1
               if self.velocidad_y==4:
                  puntos +=2
               pygame.mixer.Sound.play(coco_en_barril)
               self.reiniciar()
        return puntos

#clase bananas
class Bananas(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.image=pygame.image.load("Juego Cocos/bananas.png")  
        self.velocidad_y=6 
        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y
    def dibujar(self):
        pantalla.blit(self.image,self.rect)
    def update(self):
        self.rect.y += self.velocidad_y
    def reiniciar(self):
        pos_aleatoria=random.randrange(8)
        if pos_aleatoria==0:
            self.rect.x=50
            self.rect.y=200
        if pos_aleatoria==1:
            self.rect.x=100
            self.rect.y=200
        if pos_aleatoria==2:
            self.rect.x=200
            self.rect.y=300
        if pos_aleatoria==3:
            self.rect.x=300
            self.rect.y=300
        if pos_aleatoria==4:
            self.rect.x=pantalla_ancho//2
            self.rect.y=250
        if pos_aleatoria==5:
            self.rect.x=480
            self.rect.y=250
        if pos_aleatoria==6:
            self.rect.x=600
            self.rect.y=250
        if pos_aleatoria==7:
            self.rect.x=730
            self.rect.y=250
    def Colision(self):
        puntos=0
        colision=20
        if self.rect.y> pantalla_alto:
           self.reiniciar()
        if self.rect.colliderect(barril.rect):
          if self.rect.bottom - barril.rect.top< colision:
              puntos +=5
              pygame.mixer.Sound.play(banana_en_barril)
              self.reiniciar()
        return puntos

#clase barril
class Barril(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pygame.image.load("Juego Cocos/barril.png")
        self.rect=self.image.get_rect()
        self.rect.x=pantalla_ancho//2
        self.rect.y=pantalla_alto-100
    def dibujar(self):
        pantalla.blit(self.image,self.rect)
    
    #movimiento con teclado y limites de pantalla
    def update(self):
        velocidad_x=0
        teclas=pygame.key.get_pressed()
        if teclas[pygame.K_LEFT]:
            self.rect.x -= 10
        if teclas[pygame.K_RIGHT]:
            self.rect.x += 10 
        if self.rect.right> pantalla_ancho:
            self.rect.right=pantalla_ancho
        if self.rect.left<0:
            self.rect.x=0
        self.rect.x += velocidad_x



#variables para terminar juego, mostrar texto y sonido cuando termina
terminar_juego=False
texto_fin_juego=False
contador_sonido_fin=0

pantalla_inicio=True

#acumulador puntos
puntos_total=0

tiempo=0
contador=0
#bucle de juego
jugar=True
while jugar:
    if pantalla_inicio:
        pantalla_principal()
        pantalla_inicio=False
        #instanciacion de objetos
        coco1=Cocos(50,200)
        coco2=Cocos(100,200)
        coco3=Cocos(200,300)
        banana1=Bananas(600,250)
        coco4=Cocos(300,300)
        coco5=Cocos(pantalla_ancho//2,250)
        coco6=Cocos(480,250)
        banana2=Bananas(730,250)
        barril=Barril()
    reloj.tick(FPS)

    dibujar_fondo()
    coco1.dibujar()
    coco2.dibujar()
    coco3.dibujar()
    coco4.dibujar()
    coco5.dibujar()
    coco6.dibujar()
    banana1.dibujar()
    banana2.dibujar()
    barril.dibujar()
    
    #si no se termina el juego, se siguen actualizando los objetos
    if terminar_juego==False:
        coco1.update()
        coco2.update()
        coco3.update()
        coco4.update()
        coco5.update()
        coco6.update()
        banana1.update()
        banana2.update()
        barril.update()

        #se comprueban colisiones, y se acumulan los puntos
        puntos1=coco1.Colision()
        puntos2=coco2.Colision()
        puntos3=coco3.Colision()
        puntos4=coco4.Colision()
        puntos5=coco5.Colision()
        puntos6=coco6.Colision()
        puntos7=banana1.Colision()
        puntos8=banana2.Colision()
        puntos_total=(puntos_total+puntos1+puntos2+puntos3+puntos4+puntos5+
        puntos6+puntos7+puntos8)

    #se muestran los puntos
    muestra_texto(pantalla,comic,"Puntos: "+str(puntos_total),rojo,40,pantalla_ancho-200,40)

    #busqueda de evento para salir del juego
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            jugar=False

    #tiempo de juego (1 minuto)
    if terminar_juego==False:
        contador +=1
        if contador==60:
            tiempo +=1
            contador=0
    if tiempo >= 60:
        terminar_juego=True
        texto_fin_juego=True
    if texto_fin_juego==True:
        muestra_texto(pantalla,comic,"FIN DEL JUEGO!",azul,80,pantalla_ancho//2,pantalla_alto//2)
        if contador_sonido_fin<1:
            pygame.mixer.Sound.play(final_juego)
            contador_sonido_fin +=1
    muestra_texto(pantalla,comic,str(tiempo),blanco,40,400,40)
    
    #actualizacion de pantalla
    pygame.display.flip()
pygame.quit()