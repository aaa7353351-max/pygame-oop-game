import pygame
pygame.init() 
# init은 처음에 적어주고시작

# pygame.quit() : pygame 종료

# display : 사용자가 보는 화면
# pygame.display: 실제로 눈에 pygame display 개념보이는 게임화면 창을 제어하는 도구  
# pygame.display.set_mode() :창 생성/ 창의 크기 속성 설정
# pygame.display.set_caption(): 창 제목 설정/ 창상단제목변경
# pygame.display.update(): 화면 새로고침/ 화면에 실제 반영
 
background = pygame.display.set_mode((640,480))
pygame.display.set_caption("nje-keyboard")

# event : 게임이 사용자 입력에 반응하는 방법(키보드나 마우스입력에 반응)
# pygame.event.get() : 이벤트를 리스트로 가져옴(이벤트: 사용자 입력)
#event.type : 이벤트 종류알려주는 속성(마우스클릭,키보드입력,창닫기클릭 . . )
# 1. pygame.QUIT: 창닫기
# 2. pygame.KEYDOWN : 키눌림
# 3. pygame.KEYUP : 키에서 손뗌
# 4. pygame.MOUSEBUTTONDOWN : 마우스 클릭
# 5. pygame.MOUSEBUTTONUP : 마우스 버튼 뗌

play = True
while play:
    for event in pygame.event.get():
        # print(event.type)
        if event.type == pygame.QUIT:
            play= False
        if event.type == pygame.KEYDOWN:
        # if event.key == 97: 
                # 아스키코드 a 
            if event.key == pygame.K_UP:  #위 키 , 아래 키, 오른 키, 왼 키
                print('up')
            elif event.key == pygame.K_DOWN: 
                print('down')
            elif event.key == pygame.K_RIGHT: 
                print('right')
            elif event.key == pygame.K_LEFT: 
                print('left')

pygame.quit()
