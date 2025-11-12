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

# ----클래스 정의

    #클래스 Background / 배경그림관리 draw()
class Background:
    def __init__(self, img_path):
        self.image =  pygame.image.load(img_path).convert() #이미지 로드 후 최적화
        self.image = pygame.transform.scale(self.image, (WIDTH,HEIGHT)) #크기변환  
    def draw(self, screen):
        screen.blit(self.image,(0,0))
    #클래스 Player / 조작 & hp관리 move(), draw()
class Player:
    def __init__(self, img_path):
        self.image = pygame.image.load(img_path).convert_alpha()
        self.rect = self.image.get_rect(center=(100, HEIGHT // 2))
        self.hp = 3
    
    def move(self, keys):
        if keys[pygame.k_up] and self.rect.top >0: #캐릭터 위치
            self.rect.y -= 5
        if keys[pygame.K_DOWN] and self.rect.bottom < HEIGHT:
            self.rect.y += 5
        
    def draw(self, screen):
        screen.blit(self.image, self.rect)

class Enemy:
    def __init__(self, img_path):
        self.image = pygame.image.load(img_path).convert_alpha()
# 투명도 이미지 파일을 불러옴 
        self.rect = self.image.get_rect(center=(random.randint(WIDTH, WIDTH+200), random.randint(50, HEIGHT-50)))
        self.speed = random.randint(4, 7)
    def update(self):
        self.rect.x -= self.speed
        if self.rect.right < 0:
            self.rect.x = random.randint(WIDTH, WIDTH+200)
            self.rect.y = random.randint(50, HEIGHT-50)
    def draw(self, screen):
        screen.blit(self.image, self.rect)

class Item:
    def __init__(self, img_path):
        self.image = pygame.image.load(img_path).convert_alpha()
        self.rect = self.image.get_rect(center=(random.randint(WIDTH, WIDTH+200), random.randint(50, HEIGHT-50)))
        self.speed = 3
    def update(self):
        self.rect.x -= self.speed
        if self.rect.right < 0:
            self.rect.x = random.randint(WIDTH, WIDTH+300)
            self.rect.y = random.randint(50, HEIGHT-50)
    def draw(self, screen):
        screen.blit(self.image, self.rect)






# . . .클래스들 정리해두고 커밋 > 게임관리 클래스 Game 만들고 커밋 > 게임루프 run 구성후 커밋 >게임종료처리



#종료 
pygame.quit()
sys.exit()