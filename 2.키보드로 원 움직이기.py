import pygame

pygame.init() 

background = pygame.display.set_mode((640,480))
pygame.display.set_caption("nje-keyboard")

# 화면 중심에 좌표
width, height = background.get_size() #640//2 == 320
width, height = background.get_size() #480//2 == 240
x_pos = width//2
y_pos = height//2

# 마우스조종 적용 확인 
play = True
while play:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play= False
        if event.type == pygame.MOUSEMOTION:
            pass
            # print('마우스모션')
            # print(pygame.mouse.get_pos()) #실시간으로 마우스 좌표를 튜플의 형태로 알려줌
        if event.type == pygame.MOUSEBUTTONDOWN:
            # print('마우스버튼누름')
            #  print(pygame.mouse.get_pos())
            print(event.button) #누른 버튼 출력 왼쪽 1, 가운데 2, 오른쪽 3  휠 업다운 4/5
        if event.type == pygame.MOUSEBUTTONUP:
            # print('마우스버튼 뗌')    
            print(pygame.mouse.get_pos()) 

        
    background.fill((255,0,0))
    pygame.draw.circle(background, (0,0,255),(x_pos ,y_pos),5)
    pygame.display.update()

pygame.quit()

# 화면에 원 띄우기
# x_pos 변수 
# y_pos 변수

# 공이 화면 중심에 있을 수 있음
