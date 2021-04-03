import pygame

pygame.init()  #   반드시 필요

#화면 크기 설정 

screen_width = 480 #가로
screen_height = 640 # 세로

screen = pygame.display.set_mode((screen_width,screen_height))

#화면 타이틀 설정
pygame.display.set_caption("세빈 게임")

#배경이미지 불러오기
background = pygame.image.load("D:/python/python_base/pygame_basic/제목 없음.png")

# 이벤트 루프
running = True #게임이 진행중인지 확인
while running :
    for event in pygame.event.get(): #어떤이벤트가 발생 하였는가?
        if event.type == pygame.QUIT: #창이 닫히는 이벤트 발생하였는가?
            running = False #게임끝

    screen.blit(background,(0,0)) #배경 그리기

    pygame.display.update() #게임화면을 다시그리기!


#pygame 종료
pygame.quit()