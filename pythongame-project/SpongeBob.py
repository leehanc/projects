import turtle as t
# turtle 모듈 불러오기

import random
# random 모듈 불러오기

score=0

s = t.Screen()
# 배경 이미지 삽입

s.bgpic(picname = "pythongame-project/image/bg.gif")
# 배경이미지 경로

s.setup(600,600)
#배경 사이즈설정

# 터틀 이미지 생성

image1 = "pythongame-project/image/play1.gif"
#스폰지밥 경로

image2 = "pythongame-project/image/jip1.gif"
#집게사장 경로

food = "pythongame-project/image/food1.gif"
#게살버거 경로


# 터틀 이미지 추가

s.addshape(image1)
#이미지 터틀종류에 추가

s.addshape(image2)
#이미지 터틀종류에 추가

s.addshape(food)
#이미지 터틀종류에 추가

score=0
#스코어 초기설정

te = t.Turtle()
#집게사장 생성

te.shape(image2)
#집게사장 이미지 적용

te.speed(30)

te.up()

te.goto(0, 200)
#집게사장 위치

ts = t.Turtle()
#게살버거 생성

ts.shape(food)
#게살버거 이미지 적용

ts.speed(35)

ts.up()

ts.goto(random.randint(-230, 230),random.randint(-230, 230))
# 게살버거 랜덤 생성 좌표


#키보드설정
def turn_right():

    t.setheading(0)

def turn_up():

    t.setheading(90)

def turn_left():

    t.setheading(180)

def turn_down():

    t.setheading(270)

def play():
    
    global score
    #전역변수 사용

    t.fd(10+score)
    #스폰지 속도

    ang = te.towards(t.pos())
    #집게사장이 스폰지밥 쪽으로 회전
    
    te.setheading(ang)
    #집게사장 방향 
    
    te.forward(4+score)
    #집게사장 속도

    if t.distance(ts) < 20:
        #게살버거와 가까워지면
        
        t_text.clear()
        #남은 텍스트 청소
        
        score += 1
        #스코어 추가
        
        t_text.write(score,font=("", 20))
        #스코어 표시
        
        star_x = random.randint(-230, 230)
        #게살버거 추가 x,y 좌표
        
        star_y = random.randint(-230, 230)
        
        ts.goto(star_x, star_y)
        #게살버거 이동좌표
        
    if t.distance(te) >= 12:
        
        t. ontimer(play, 100)
        #100의1초마다 재실행
  
t_text=t.Turtle()
#스코어 추가

t_text.up()

t_text.color("red")

t_text.goto(-320,310)

t_text.hideturtle()
# 스코어만 보이게 하기위해 

t.setup(700, 700)

t.shape(image1)
# 스폰지밥 이미지

t.speed(40)
t.up()
t.onkeypress(turn_right, "Right")
t.onkeypress(turn_up, "Up")
t.onkeypress(turn_left, "Left")
t.onkeypress(turn_down, "Down")
t.listen()


play()
t.mainloop()