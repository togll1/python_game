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

#캐릭터(sprite) 불러오기
charactor = pygame.image.load("D:\python\python_base\pygame_basic\sprite.png")
charactor_size = charactor.get_rect().size # 이미지 크기 구해옴
charactor_width = charactor_size[0] #캐릭 가로 크기
charactor_height = charactor_size[1]  #캐릭 세로 크기
charactor_x_pos = (screen_width - charactor_width) /2 #화면 가로의 절반 크기에 해당하는곳에 위치
charactor_y_pos = screen_height-charactor_height #화면 세로크기 가장 아래에



# 이벤트 루프
running = True #게임이 진행중인지 확인
while running :
    for event in pygame.event.get(): #어떤이벤트가 발생 하였는가?
        if event.type == pygame.QUIT: #창이 닫히는 이벤트 발생하였는가?
            running = False #게임끝

    screen.blit(background,(0,0)) #배경 그리기
    screen.blit(charactor,(charactor_x_pos,charactor_y_pos))

    pygame.display.update() #게임화면을 다시그리기!


#pygame 종료
pygame.quit()