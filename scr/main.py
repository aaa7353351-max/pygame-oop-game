#pygame random, sys 모듈 불러옴 필요한 라이브러리
import pygame, random, sys

pygame.init()
#화면 환경설정
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("마당을 나온 수탉")
#변수 설정
x,y = WIDTH/2, HEIGHT/2
speed= 5

#화면 띄우기 루프
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

clock = pygame.time.Clock()
font = pygame.font.Font(None,40)
#색상 
WHITE = (255,255,255)

# 클래스 정의

#클래스 Background / 배경그림관리 draw()
class Background:
    def __init__(self, img_path):
        self.image =  pygame.image.load(img_path).convert() #이미지 로드 후 최적화
        self.image = pygame.transform.scale(self.image, (WIDTH,HEIGHT)) #크기변환  




#클래스 Player / 조작 & hp관리 move(), draw()



# . . .클래스들 정리해두고 커밋 > 게임관리 클래스 Game 만들고 커밋 > 게임루프 run 구성후 커밋 >게임종료처리



#종료 
pygame.quit()
sys.exit()