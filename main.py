#pygame random, sys 모듈 불러옴 필요한 라이브러리
import pygame, random, sys

pygame.init()
#화면 환경설정
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("키위새의 비행")
#변수 설정
x,y = WIDTH/2, HEIGHT/2
speed= 5


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
        if keys[pygame.K_UP] and self.rect.top >0: #캐릭터 위치
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
        self.image = pygame.image.load("image/키위아이템.png").convert_alpha()
        self.rect = self.image.get_rect(center=(random.randint(WIDTH, WIDTH+200), random.randint(50, HEIGHT-50)))
        self.speed = 3
    def update(self):
        self.rect.x -= self.speed
        if self.rect.right < 0:
            self.rect.x = random.randint(WIDTH, WIDTH+300)
            self.rect.y = random.randint(50, HEIGHT-50)
    def draw(self, screen):
        screen.blit(self.image, self.rect)

# ----게임 클래스 
class Game:
    def __init__(self):
        self.bg = Background("image/배경.jpg")
        self.player = Player("image/키위새.png")
        self.enemies = [Enemy("image/enemy.png") for _ in range(3)]
        self.items = [Item("item.png")]
        self.start_time = pygame.time.get_ticks()
        self.running = True
    def check_collision(self):
       # 적 충돌
        for e in self.enemies:
            if self.player.rect.colliderect(e.rect):
                self.player.hp -= 1
                e.rect.x = WIDTH + random.randint(100, 300)
                if self.player.hp <= 0:
                    self.running = False
        # 아이템 충돌
        for i in self.items:
            if self.player.rect.colliderect(i.rect):
                self.player.hp += 1
                i.rect.x = WIDTH + random.randint(300, 500)

#---- 게임루프구성
    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            keys = pygame.key.get_pressed()
            self.player.move(keys)
            # 업데이트
            for e in self.enemies:
                e.update()
            for i in self.items:
                i.update()
            self.check_collision()
            # 점수 계산
            elapsed_time = (pygame.time.get_ticks() - self.start_time) // 1000
            # 화면 그리기
            self.bg.draw(screen)
            self.player.draw(screen)
            for e in self.enemies:
                e.draw(screen)
            for i in self.items:
                i.draw(screen)
            # 정보 표시
            text = font.render(f"HP: {self.player.hp}   Time: {elapsed_time}", True, WHITE)
            screen.blit(text, (10, 10))
            pygame.display.flip()
            clock.tick(60)
        # 게임 종료 화면
        screen.fill((0, 0, 0))
        gameover_text = font.render(f"Game Over! Score: {elapsed_time}", True, WHITE)
        screen.blit(gameover_text, (WIDTH//2 - 150, HEIGHT//2))
        pygame.display.flip()
        pygame.time.wait(2000)
# --- 실행 --- #
if __name__ == "__main__":
    Game().run()















# . . .클래스들 정리해두고 커밋(완) > 게임관리 클래스 Game 만들고 커밋 > 게임루프 run 구성후 커밋 >게임종료처리

# 추가해야할 이미지 배경, 적, 그리고 브금 설정하기

#종료 
pygame.quit()
sys.exit()