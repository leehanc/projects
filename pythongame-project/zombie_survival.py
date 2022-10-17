import pygame
from random import *
from math import *
from datetime import datetime

# SCREEN SIZE
size = (1500, 900)

# enemy 왼쪽 이미지
enemy_left_motion_img = [['pythongame-project/image/a1_l.png','pythongame-project/image/a1_l.png','pythongame-project/image/a1_l.png','pythongame-project/image/a1_l.png', 'pythongame-project/image/a2_l.png', 'pythongame-project/image/a2_l.png','pythongame-project/image/a2_l.png','pythongame-project/image/a2_l.png','pythongame-project/image/a3_l.png','pythongame-project/image/a3_l.png','pythongame-project/image/a3_l.png','pythongame-project/image/a3_l.png', 'pythongame-project/image/a4_l.png','pythongame-project/image/a4_l.png','pythongame-project/image/a4_l.png','pythongame-project/image/a4_l.png'],\
                         ['pythongame-project/image/b4_l.png','pythongame-project/image/b1_l.png','pythongame-project/image/b1_l.png','pythongame-project/image/b1_l.png', 'pythongame-project/image/b1_l.png', 'pythongame-project/image/b2_l.png','pythongame-project/image/b2_l.png','pythongame-project/image/b2_l.png','pythongame-project/image/b2_l.png','pythongame-project/image/b3_l.png','pythongame-project/image/b3_l.png','pythongame-project/image/b3_l.png', 'pythongame-project/image/b3_l.png','pythongame-project/image/b4_l.png','pythongame-project/image/b4_l.png','pythongame-project/image/b4_l.png'],\
                         ['pythongame-project/image/c4_l.png','pythongame-project/image/c4_l.png','pythongame-project/image/c1_l.png','pythongame-project/image/c1_l.png', 'pythongame-project/image/c1_l.png', 'pythongame-project/image/c1_l.png','pythongame-project/image/c2_l.png','pythongame-project/image/c2_l.png','pythongame-project/image/c2_l.png','pythongame-project/image/c2_l.png','pythongame-project/image/c3_l.png','pythongame-project/image/c3_l.png', 'pythongame-project/image/c3_l.png','pythongame-project/image/c3_l.png','pythongame-project/image/c4_l.png','pythongame-project/image/c4_l.png'],\
                         ['pythongame-project/image/d4_l.png','pythongame-project/image/d4_l.png','pythongame-project/image/d4_l.png','pythongame-project/image/d1_l.png', 'pythongame-project/image/d1_l.png', 'pythongame-project/image/d1_l.png','pythongame-project/image/d1_l.png','pythongame-project/image/d2_l.png','pythongame-project/image/d2_l.png','pythongame-project/image/d2_l.png','pythongame-project/image/d2_l.png','pythongame-project/image/d3_l.png', 'pythongame-project/image/d3_l.png','pythongame-project/image/d3_l.png','pythongame-project/image/d3_l.png','pythongame-project/image/d4_l.png']]

# enemy 오른쪽 이미지
enemy_right_mode_img = [['pythongame-project/image/a1_r.png','pythongame-project/image/a1_r.png','pythongame-project/image/a1_r.png','pythongame-project/image/a1_r.png', 'pythongame-project/image/a2_r.png', 'pythongame-project/image/a2_r.png','pythongame-project/image/a2_r.png','pythongame-project/image/a2_r.png','pythongame-project/image/a3_r.png','pythongame-project/image/a3_r.png','pythongame-project/image/a3_r.png','pythongame-project/image/a3_r.png', 'pythongame-project/image/a4_r.png','pythongame-project/image/a4_r.png','pythongame-project/image/a4_r.png','pythongame-project/image/a4_r.png'],\
                        ['pythongame-project/image/b4_r.png','pythongame-project/image/b1_r.png','pythongame-project/image/b1_r.png','pythongame-project/image/b1_r.png', 'pythongame-project/image/b1_r.png', 'pythongame-project/image/b2_r.png','pythongame-project/image/b2_r.png','pythongame-project/image/b2_r.png','pythongame-project/image/b2_r.png','pythongame-project/image/b3_r.png','pythongame-project/image/b3_r.png','pythongame-project/image/b3_r.png', 'pythongame-project/image/b3_r.png','pythongame-project/image/b4_r.png','pythongame-project/image/b4_r.png','pythongame-project/image/b4_r.png'],\
                        ['pythongame-project/image/c4_r.png','pythongame-project/image/c4_r.png','pythongame-project/image/c1_r.png','pythongame-project/image/c1_r.png', 'pythongame-project/image/c1_r.png', 'pythongame-project/image/c1_r.png','pythongame-project/image/c2_r.png','pythongame-project/image/c2_r.png','pythongame-project/image/c2_r.png','pythongame-project/image/c2_r.png','pythongame-project/image/c3_r.png','pythongame-project/image/c3_r.png', 'pythongame-project/image/c3_r.png','pythongame-project/image/c3_r.png','pythongame-project/image/c4_r.png','pythongame-project/image/c4_r.png'],\
                        ['pythongame-project/image/d4_r.png','pythongame-project/image/d4_r.png','pythongame-project/image/d4_r.png','pythongame-project/image/d1_r.png', 'pythongame-project/image/d1_r.png', 'pythongame-project/image/d1_r.png','pythongame-project/image/d1_r.png','pythongame-project/image/d2_r.png','pythongame-project/image/d2_r.png','pythongame-project/image/d2_r.png','pythongame-project/image/d2_r.png','pythongame-project/image/d3_r.png', 'pythongame-project/image/d3_r.png','pythongame-project/image/d3_r.png','pythongame-project/image/d3_r.png','pythongame-project/image/d4_r.png']]

# 바람칼날 이미지
skill_list = ['pythongame-project/image/skill_1.png', 'pythongame-project/image/skill_2.png', 'pythongame-project/image/skill_3.png', 'pythongame-project/image/skill_4.png','pythongame-project/image/skill_5.png', 'pythongame-project/image/skill_6.png','pythongame-project/image/skill_7.png','pythongame-project/image/skill_8.png','pythongame-project/image/skill_9.png' ,'pythongame-project/image/skill_10.png', 'pythongame-project/image/skill_11.png', 'pythongame-project/image/skill_12.png','pythongame-project/image/skill_13.png', 'pythongame-project/image/skill_14.png', 'pythongame-project/image/skill_15.png']

# 기본공격 이미지
fire_list = ['pythongame-project/image/skill_16.png','pythongame-project/image/fire1.png','pythongame-project/image/fire2.png','pythongame-project/image/fire3.png','pythongame-project/image/fire4.png','pythongame-project/image/fire5.png','pythongame-project/image/fire6.png','pythongame-project/image/fire7.png','pythongame-project/image/fire8.png',\
                    'pythongame-project/image/fire9.png','pythongame-project/image/fire10.png','pythongame-project/image/fire11.png','pythongame-project/image/fire12.png','pythongame-project/image/fire13.png','pythongame-project/image/fire14.png','pythongame-project/image/fire15.png','pythongame-project/image/fire16.png',\
                    'pythongame-project/image/fire17.png','pythongame-project/image/fire18.png','pythongame-project/image/fire19.png','pythongame-project/image/fire20.png','pythongame-project/image/fire21.png','pythongame-project/image/fire22.png','pythongame-project/image/fire23.png','pythongame-project/image/fire24.png',\
                    'pythongame-project/image/fire25.png','pythongame-project/image/fire26.png','pythongame-project/image/fire27.png','pythongame-project/image/fire28.png','pythongame-project/image/fire29.png','pythongame-project/image/fire30.png']

pygame.init()

# 사운드 설정
pygame.mixer.init()
Sound_ingame = pygame.mixer.Sound("pythongame-project/image/game_music.mp3")      #ingame 로드
Sound_intro = pygame.mixer.Sound("pythongame-project/image/start_music.mp3")      #intro 로드
Sound_end = pygame.mixer.Sound("pythongame-project/image/end_music3.mp3")       #end 로드
Sound_intro.play(-1)                                   #시작 전 소리 무한 재생
Sound_intro.set_volume(0.3)
attack_fire = pygame.mixer.Sound("pythongame-project/image/fireball.mp3")     #공격 사운드1 로드
attack_sword = pygame.mixer.Sound("pythongame-project/image/sword1.mp3")       #공격 사운드2 로드
attack_nuclear = pygame.mixer.Sound("pythongame-project/image/small.wav")        #폭발음
damage_music = pygame.mixer.Sound("pythongame-project/image/damage_music.mp3") #타격음



# 객체 생성
class obj:
    def __init__(self):
        self.x = 0  # x 좌표
        self.y = 0  # y 좌표
        self.horizon_move = 0   # x축 이동거리
        self.vertical_move = 0   # y축 이동거리
        self.number = 0
    def put_img(self, address):
        self.img = pygame.image.load(address)
        self.image_width, self.image_height = self.img.get_size()      # 파일 가로 세로 크기 읽어오기
    def change_size(self, image_width, image_height):  # 이미지 파일 원하는 사이즈로 크기 변환
        self.img = pygame.transform.scale(self.img, (image_width, image_height))
        self.image_width, self.image_height = self.img.get_size()
    def show(self):
        screen.blit(self.img, (self.x, self.y))

def crash(a, b):  ## 충돌처리 함수 정의
    if (a.x - b.image_width <= b.x) and (b.x <= a.x + a.image_width):
        if (a.y - b.image_height <= b.y) and (b.y <= a.y + a.image_height):
            return True
        else:
            return False
    else:
        return False
    


# 스크린 설정
screen = pygame.display.set_mode(size)  # pg.dispaly.set_mode()
title = '인간 VS 좀비'
pygame.display.set_caption(title)

# 배경 생성
background = obj()
background.put_img('pythongame-project/image/earth_1500.png')

clock = pygame.time.Clock()
running = True
standby = 0

# 플레이어 생성
player = obj()
player.put_img('pythongame-project/image/wood_walk.gif')
player.x = round(size[0] / 2 - player.image_width / 2)
player.y = round(size[1] / 2 - player.image_height / 2)
# 플레이어 초기설정
player.horizon_move = 5
player.vertical_move = 5
player_rwalk = 0
player_lwalk = 0

# 체력바 생성
hp = obj()
hp.put_img('pythongame-project/image/hp.png')
hp.change_size(42, 5)
hp.x = player.x
hp.y = player.y + 30

kill = 0  # 킬수
dam = 0 # 데미지

# 기본공격 생성
fire = obj()
fire.put_img('pythongame-project/image/skill_16.png')
fire.change_size(1500, 900)
fire.x = 300
fire.y = 0

# 초기 설정
enemy_number = 0 # 적 생성순서
enemy_motion_number = 0 # 적의 움직임 순서
birth_position = 0 # 적이 생성되는 pos
how_many = 0.9 # 리젠율 초기값
enemy_list = []  # 적 리스트
delete_enemy_list = [] # 충돌 후 제거되는 적 리스트

bullet_list = []  # 총알 리스트
delete_bullet_list = [] # 충돌 후 총알 제거되는 리스트
orbital_bullet_status = False # 궤도 불렛 상태
orbital_bullet_theta = 0 # 초기 각도
shooting_count = 0 # 총알 갯수

# 바람칼날 생성
skill = obj()
skill.put_img('pythongame-project/image/skill_16.png')
skill.change_size(100, 100)
skill.x = player.x + 40
skill.y = player.y - 80

# 보스 생성
boss1 = obj()
boss1.x = -300
boss1.y = -300
boss1.put_img('pythongame-project/image/kingzom0_l.png')
boss1.horizon_move = 50
boss1_time = 210

boss2 = obj()
boss2.x = 1500
boss2.y = -300
boss2.put_img('pythongame-project/image/kingzom0_r.png')
boss2.horizon_move = 50
boss2_time = 240

boss3 = obj()
boss3.x = -300
boss3.y = -300
boss3.put_img('pythongame-project/image/kingzom2_l.png')
boss3.horizon_move = 50
boss3_time = 270

f = 0 # 핵폭탄

left_go = False
right_go = False
up_go = False
down_go = False
space_go = False
w_go = False
r_go = False
f_go = False

if __name__ == '__main__':
    # 시작 대기 화면
    while standby == 0:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    Sound_intro.stop()  # 시작 전 소리 중지
                    Sound_ingame.play(-1)  # 배경 음악 시작
                    Sound_ingame.set_volume(0.3) # 볼륨 설정
                    standby = 1

        Surface = pygame.image.load('pythongame-project/image/Gstart.png')
        screen.blit(Surface, (0, 0))
        pygame.display.update()
        font = pygame.font.Font(None, 48)  # 대기화면 press 폰트
        text = font.render("PRESS SPACE KEY TO START THE GAME", True, (255, 255, 255))
        screen.blit(text, (round(size[0] / 2 - 330), round(size[1] / 3 + 300)))  # 대기화면 press 위치
        pygame.display.flip()

    #게임 시작
    start_time = datetime.now()  # 시간함수
    while running:
        
        now_time = datetime.now()
        delta_time = round((now_time - start_time).total_seconds())
        clock.tick(60)  # FPS 설정

        # 키보드 조작 입력
        for event in pygame.event.get():
            # 종료 조작
            if event.type == pygame.QUIT:
                running = False
            # 키보드 누르는 순간 처리
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    left_go = True
                if event.key == pygame.K_RIGHT:
                    right_go = True
                if event.key == pygame.K_SPACE:
                    space_go = True
                    shooting_count = 0
                if event.key == pygame.K_UP:
                    up_go = True
                if event.key == pygame.K_DOWN:
                    down_go = True
                if delta_time > 60:
                    if event.key == pygame.K_w:
                        w_go = True
                if delta_time > 120:
                    if event.key == pygame.K_r:
                        r_go = True
                        r = 0
                if event.key == pygame.K_f:
                    f_go = True

            # 키보드 떼는 순간 처리
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    left_go = False
                if event.key == pygame.K_RIGHT:
                    right_go = False
                if event.key == pygame.K_w:
                    w_go = False
                if event.key == pygame.K_r:
                    r_go = False
                if event.key == pygame.K_f:
                    f_go = False
                if event.key == pygame.K_SPACE:
                    space_go = False
                if event.key == pygame.K_UP:
                    up_go = False
                if event.key == pygame.K_DOWN:
                    down_go = False

        # 상하좌우 조작 동작
        if left_go == True:
            player.x -= player.horizon_move
            player_lwalk += 1
            if player.x <= 0: # 플레이어가 화면에 넘어가지 않게 설정
                player.x = 0
        if right_go == True:
            player.x += player.horizon_move
            player_rwalk += 1
            if player.x >= size[0] - player.image_width:
                player.x = size[0] - player.image_width
        if up_go == True:
            player.y -= player.vertical_move
            player_rwalk += 1
            if player.y <= 0:
                player.y = 0
        if down_go == True:
            player_lwalk += 1
            player.y += player.vertical_move
            if player.y >= size[1] - player.image_height:
                player.y = size[1] - player.image_height

        # 우측 이동 모션
        if right_go == True or up_go == True:
            if player_rwalk % 7 == 1:
                player.put_img('pythongame-project/image/woodwalk_1.png')
            elif player_rwalk%7 == 2:
                player.put_img('pythongame-project/image/woodwalk_2.png')
            elif player_rwalk%7 == 3:
                player.put_img('pythongame-project/image/woodwalk_3.png')
            elif player_rwalk%7 == 4:
                player.put_img('pythongame-project/image/woodwalk_4.png')
            elif player_rwalk%7 == 5:
                player.put_img('pythongame-project/image/woodwalk_5.png')
            else :
                player.put_img('pythongame-project/image/woodwalk_6.png')

        # 좌측 이동 모션
        if left_go == True or down_go == True:
            if player_lwalk % 7 == 1:
                player.put_img('pythongame-project/image/woodwalk_l1.png')
            elif player_lwalk % 7 == 2:
                player.put_img('pythongame-project/image/woodwalk_l2.png')
            elif player_lwalk % 7 == 3:
                player.put_img('pythongame-project/image/woodwalk_l3.png')
            elif player_lwalk % 7 == 4:
                player.put_img('pythongame-project/image/woodwalk_l4.png')
            elif player_lwalk % 7 == 5:
                player.put_img('pythongame-project/image/woodwalk_l5.png')
            else:
                player.put_img('pythongame-project/image/woodwalk_l6.png')

        # 플레이어 체력바 위치
        hp.x = player.x + 3
        hp.y = player.y + 47

        # enemy 생성빈도
        if delta_time > 15:
            how_many = 0.8
        if delta_time > 30:
            how_many = 0.7
        if delta_time > 45:
            how_many = 0.6
        if delta_time > 60:
            how_many = 0.5
        if delta_time > 100:
            how_many = 0.4

        if random() > how_many: # 적 생성
            birth_position = randint(1,4)
            # 화면 상단
            if birth_position == 0:
                enemy = obj()
                enemy.put_img(enemy_right_mode_img[0][0])
                enemy.change_size(48, 48)
                enemy.x = randrange(0, size[0] - enemy.image_width)
                enemy.y = enemy.image_height - round(player.image_height / 2)
                enemy.number = enemy_number
                enemy_number += 1
                enemy_list.append(enemy)
            # 화면 하단
            if birth_position == 1:
                enemy = obj()
                enemy.put_img(enemy_left_motion_img[0][0])
                enemy.change_size(48, 48)
                enemy.x = randrange(0, size[0])
                enemy.y= size[1]
                enemy.number = enemy_number
                enemy_number += 1
                enemy_list.append(enemy)
            # 화면 좌측
            if birth_position == 2:
                enemy = obj()
                enemy.put_img(enemy_left_motion_img[0][0])
                enemy.change_size(48, 48)
                enemy.x = 0 - enemy.image_width
                enemy.y= randrange(0, size[1])
                enemy.number = enemy_number
                enemy_number += 1
                enemy_list.append(enemy)
            # 화면 우측
            if birth_position == 3:
                enemy = obj()
                enemy.put_img(enemy_right_mode_img[0][0])
                enemy.change_size(48, 48)
                enemy.x = size[0]
                enemy.y= randrange(0, size[1] - enemy.image_height)
                enemy.number = enemy_number
                enemy_number += 1
                enemy_list.append(enemy)

        # enemy 이동 경로
        for i in range(len(enemy_list)):
            enemy_list[i].x -= (enemy_list[i].x - player.x) /50

            enemy_list[i].y -= (enemy_list[i].y - player.y) /50


        # enemy 모션
        for i in range(len(enemy_list)):
            if enemy_list[i].number % 4 == 0:
                if enemy_list[i].x > player.x:
                    enemy_list[i].put_img(enemy_right_mode_img[0][enemy_motion_number % 16])
                    enemy_list[i].change_size(48,48)
                if enemy_list[i].x < player.x:
                    enemy_list[i].put_img(enemy_left_motion_img[0][enemy_motion_number % 16])
                    enemy_list[i].change_size(48,48)
            if enemy_list[i].number % 4 == 1:
                if enemy_list[i].x > player.x:
                    enemy_list[i].put_img(enemy_right_mode_img[1][enemy_motion_number % 16])
                    enemy_list[i].change_size(48,48)
                if enemy_list[i].x < player.x:
                    enemy_list[i].put_img(enemy_left_motion_img[1][enemy_motion_number % 16])
                    enemy_list[i].change_size(48,48)
            if enemy_list[i].number % 4 == 2:
                if enemy_list[i].x > player.x:
                    enemy_list[i].put_img(enemy_right_mode_img[2][enemy_motion_number % 16])
                    enemy_list[i].change_size(48,48)
                if enemy_list[i].x < player.x:
                    enemy_list[i].put_img(enemy_left_motion_img[2][enemy_motion_number % 16])
                    enemy_list[i].change_size(48,48)
            if enemy_list[i].number % 4 == 3:
                if enemy_list[i].x > player.x:
                    enemy_list[i].put_img(enemy_right_mode_img[3][enemy_motion_number % 16])
                    enemy_list[i].change_size(48,48)
                if enemy_list[i].x < player.x:
                    enemy_list[i].put_img(enemy_left_motion_img[3][enemy_motion_number % 16])
                    enemy_list[i].change_size(48,48)

        if enemy_motion_number == 16:
            enemy_motion_number = 0
        enemy_motion_number += 1
        
        
        # 보스 생성
        if delta_time > boss1_time :
            if boss1.x >= size[0] - boss1.image_width :
                boss1.horizon_move = -5
            elif boss1.x <= 0 :
                boss1.horizon_move = 5
            boss1.x += boss1.horizon_move
            boss1.y = 150 - boss1.image_height / 2
        if delta_time > boss2_time :
            if boss2.x >= size[0] - boss2.image_width :
                boss2.horizon_move = -5
            elif boss2.x <= 0 :
                boss2.horizon_move = 5
            boss2.x += boss2.horizon_move
            boss2.y = 450 - boss2.image_height / 2
        if delta_time > boss3_time :
            if boss3.x >= size[0] - boss3.image_width :
                boss3.horizon_move = -5
            elif boss3.x <= 0 :
                boss3.horizon_move = 5
            boss3.x += boss3.horizon_move
            boss3.y = 750 - boss3.image_height / 2

# player, 보스 충돌 코드
        if crash(boss1, player) == True:
            dam = 80
        if crash(boss2, player) == True:
            dam = 80
        if crash(boss3, player) == True:
            dam = 80

        # skill 생성
        if r_go == True:
            attack_sword.play()
            attack_sword.set_volume(0.5)
            for j in range(len(enemy_list)):
                q = skill
                w = enemy_list[j]
                if crash(q, w) == True:
                    delete_enemy_list.append(j)
            skill.put_img(skill_list[r % 15])
            r += 1
            if r == 14:
                r = 0
        else:
            skill.put_img('pythongame-project/image/skill_16.png')

        if right_go or up_go:
            skill.x = player.x + 40
            skill.y = player.y - 80
        if left_go or down_go:
            skill.x = player.x - 140
            skill.y = player.y - 80

        # 핵폭탄 생성
        if f_go == True and f < 31:
            attack_nuclear.play()
            attack_nuclear.set_volume(0.3)
            fire.put_img(fire_list[f % 30])
            fire.change_size(900, 900)
            f += 1
            for j in range(len(enemy_list)):
                # q = bullet_list[i]
                q = fire
                w = enemy_list[j]
                if crash(q, w) == True:
                    # delete_bullet_list.append(i)
                    delete_enemy_list.append(j)

        # 불렛 생성
        distance_list=[]
        if space_go == True and shooting_count % 6 == 0:
            attack_fire.play()
            attack_fire.set_volume(0.2)
            bullet = obj()
            bullet.put_img('pythongame-project/image/fireball.png')
            bullet.change_size(10, 10)
            bullet.x = round(player.x + player.image_width / 2 - bullet.image_width / 2)
            bullet.y = round(player.y + player.image_height / 2 - bullet.image_height / 2)

            # 총알 - 플레이어 거리 계산
            for i in range(len(enemy_list)):
                distance = ((enemy_list[i].x-player.x)**2 + (enemy_list[i].y-player.y)**2) **0.5
                distance_list.append(distance)
                if distance_list[i] == min(distance_list) :
                    bullet.horizon_move = (enemy_list[i].x - player.x) / 30
                    bullet.vertical_move = (enemy_list[i].y - player.y) / 30
            bullet_list.append(bullet)
        shooting_count += 1

        # 불렛 이동
        delete_bullet_list = []
        for i in range(len(bullet_list)):
            bullet_list[i].x += bullet_list[i].horizon_move
            bullet_list[i].y += bullet_list[i].vertical_move
            if bullet_list[i].y <= 0 or bullet_list[i].y > size[1] or bullet_list[i].x <= 0 or bullet_list[i].x > size[
                0]:
                delete_bullet_list.append(i)
        delete_bullet_list.reverse()
        for d in delete_bullet_list:
            del bullet_list[d]

        # 불렛 충돌 코드
        for i in range(len(bullet_list)):  ##미사일
            for j in range(len(enemy_list)):  ##외계인
                q = bullet_list[i]
                w = enemy_list[j]
                if crash(q, w) == True:
                    delete_bullet_list.append(i)  # 해당 코드 제거 시 관통효과, 삽입 시 단일 공격
                    delete_enemy_list.append(j)

        try:
            delete_bullet_list.reverse()
            delete_enemy_list.reverse()
            for dm in delete_bullet_list:
                del bullet_list[dm]
            for da in delete_enemy_list:
                del enemy_list[da]
                kill += 1  # 충돌 지우는 코드 지워질 시 외계인 +1킬
        except:
            pass

        # 궤도불렛 생성
        orbital_bullet_theta += 5
        if radians(orbital_bullet_theta) == 2 * pi:
            orbital_bullet_theta = 0
        if w_go == True:
            orbital_bullet = obj()
            orbital_bullet.put_img('pythongame-project/image/book.png')
            orbital_bullet.change_size(10, 10)
            orbital_bullet_status = True

        # 궤도불렛 경로
        if orbital_bullet_status == True:
            orbital_bullet.x = player.x + player.image_width / 2 + 90 * cos(radians(orbital_bullet_theta))
            orbital_bullet.y = player.y + player.image_height / 2 + 90 * sin(radians(orbital_bullet_theta))

        # 궤도불렛 충돌 코드
        delete_bullet_list = []
        delete_enemy_list = []
        if orbital_bullet_status == True:
            for j in range(len(enemy_list)):
                # q = bullet_list[i]
                q = orbital_bullet
                w = enemy_list[j]
                if crash(q, w) == True:
                    # delete_bullet_list.append(i)
                    delete_enemy_list.append(j)

        try:
            delete_bullet_list.reverse()
            delete_enemy_list.reverse()
            for dm in delete_bullet_list:
                del bullet_list[dm]
            for da in delete_enemy_list:
                del enemy_list[da]
                kill += 1  #충돌 지우는 코드 지워질 시 외계인 +1킬
        except:
            pass

        # 플레이어 충돌 코드
        for i in range(len(enemy_list)):
            a = enemy_list[i]
            if crash(a, player) == True:
                dam += 1
                damage_music.play()
                damage_music.set_volume(0.2)
                hp.change_size(40 - dam /2, 5)

        # 플레이어 사망 시 재시작화면 출력
        while dam == 80:
            Sound_ingame.stop()
            Sound_end.play(-1)
            Sound_end.set_volume(0.5)
            clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_b:
                        Sound_intro.stop()  # 시작 전 소리 중지
                        Sound_end.stop()
                        Sound_ingame.play(-1)  # 배경 음악 시작
                        #### 초기값 가져오기
                        # 플레이어 초기값
                        player = obj()
                        player.put_img('pythongame-project/image/wood_walk.gif')
                        player.x = round(size[0] / 2 - player.image_width / 2)
                        player.y = round(size[1] / 2 - player.image_height / 2)
                        player.horizon_move = 5
                        player.vertical_move = 5
                        player_rwalk = 0
                        player_lwalk = 0

                        # 플레이어 초기값
                        hp = obj()
                        hp.put_img('pythongame-project/image/hp.png')
                        hp.change_size(40, 5)
                        hp.x = player.x
                        hp.y = player.y + 30

                        # 킬과 데미지 초기값
                        kill = 0  # 킬수
                        dam = 0 # 데미지

                        # 기본공격 초기값
                        fire = obj()
                        fire.put_img('pythongame-project/image/skill_16.png')
                        fire.change_size(1500, 900)
                        fire.x = 300
                        fire.y = 0

                        # enemy 초기값
                        enemy_number = 0
                        enemy_motion_number = 0
                        birth_position = 0
                        how_many = 0.9
                        enemy_list = []  # 적 리스트
                        delete_enemy_list = []

                        # 총알 초기값
                        bullet_list = []  # 총 알 리스트
                        delete_bullet_list = []
                        orbital_bullet_status = False
                        orbital_bullet_num = 1
                        orbital_bullet_theta = 0
                        k = 0

                        # 스킬 초기값
                        skill = obj()
                        skill.put_img('pythongame-project/image/skill_16.png')
                        skill.change_size(100, 100)
                        skill.x = player.x + 40
                        skill.y = player.y - 80

                        #핵폭탄 초기값
                        f = 0

                        # 키조작 초기값
                        left_go = False
                        right_go = False
                        up_go = False
                        down_go = False
                        space_go = False
                        w_go = False
                        r_go = False
                        f_go = False
                        start_time = datetime.now()

            Surface = pygame.image.load('pythongame-project/image/Gover.png')
            screen.blit(Surface, (0, 0))
            pygame.display.update()
            font = pygame.font.Font(None, 48)
            text = font.render("PRESS B KEY TO RESTART THE GAME", True, (255, 255, 255))
            screen.blit(text, (round(size[0] / 2 - 330), round(size[1] / 3 + 300)))
            pygame.display.flip()

        # 화면 출력
        background.show()
        player.show()
        skill.show()
        hp.show()
        fire.show()
        
        if orbital_bullet_status == True :
            orbital_bullet.show()
        for bullet in bullet_list:
            bullet.show()
        for enemy in enemy_list:
            enemy.show()
        if delta_time > boss1_time :
            boss1.show()
        if delta_time > boss2_time :
            boss2.show()
        if delta_time > boss3_time :
            boss3.show()

        # 스코어 생성
        font1 = pygame.font.Font("C:\\Windows\\Fonts\\bahnschrift.ttf", 30)
        text_kill = font1.render("Kill:{}".format(kill), True, (255, 255, 255))
        screen.blit(text_kill,(1350, 0))

        # 타이머 생성
        second = str(delta_time % 60)
        second = second.zfill(2)
        font2 = pygame.font.Font("C:\\Windows\\Fonts\\bahnschrift.ttf", 50)
        text_time = font2.render("{}:{}".format(delta_time//60, second), True, (255, 255, 255))

        screen.blit(text_time,(700, 40))

        pygame.display.update()

    quit()









