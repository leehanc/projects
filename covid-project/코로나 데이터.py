from matplotlib import pyplot as plt

import csv

from matplotlib import font_manager,rc

import numpy


font_name = font_manager.FontProperties(fname="c:\\windows\\Fonts\\malgun.ttf").get_name()

rc('font', family=font_name)


infile = open("엑셀자료/matplotlib 코로나 자료.csv", "r")

data = csv.reader(infile)


label=[]

x=[]

y=[]

z=[]


for line in data:
    
    label.append(line[0])     # line[1] 내용 추가
    
    x.append(float(line[2]))  # line[2] 내용 추가
    
    y.append(float(line[3]))  # line[3] 내용 추가

    z.append(float(line[4]))  # line[4] 내용 추가


x1 = numpy.arange(len(label))


plt.bar(x1-0.1, x, label='확진자 수', width=0.2, color='#dd0000')
# x가 나타내는 그래프 설정

plt.bar(x1+0.1, y, label='인구 수', width=0.2, color='#ddff00')
# y가 나타내는 그래프 설정

plt.xticks(x1,label)

plt.plot(label, z, label='선별진료소 수', color='blue',  marker='o')
# 꺽인 선 그래프 설정 

plt.legend()  # 상단 라벨 작성

plt.xlabel('지역')
# x축 내용 작성

plt.ylabel('%')
# y축 내용 작성

plt.ylim(0, 40)
# y축 

plt.title('지역별 인구 및 확진자 수')
# 그래프 타이틀 작성

plt.show()

infile.close()
