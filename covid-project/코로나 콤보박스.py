import tkinter.ttk as ttk
from tkinter import *

regions = ['서울', '경기도', '강원도', '충청도', '경상도','전라도', '제주도']
#리스트가 적어서 직접 리스트를 만들어 주었고 데이터가 많으면 파일을 불러와야함

root = Tk()

root.title("지역별 확진자 및 선별진료소")
#윈도우 창 제목

root.geometry("400x260")
#윈도우 창 크기

combobox = ttk.Combobox(root, height = 5, values =regions)
#목록 5개 보임, 높이가 5, values는 리스트를 의미함

combobox.pack()
#콤보박스 생성

combobox.set("지역 선택")
#values를 선택하기 전에 미리 입력된 텍스트

def btncmd():
    if combobox.get() == '서울':
        #서울을 선택했을 때 출력되는 문장(경기도, 강원도, 충청도, 경상도, 전라도, 제주도)
        label.configure(text = "누적 확진자 :   3,066,376\n지역별 인구수 : 9,505,926\n선별 진료소 :   71\n서울은 확진자에 비해 선별진료소가 적습니다")
    elif combobox.get() == '경기도':
        label.configure(text = "누적 확진자 :   4,996,509\n지역별 인구수 : 16,520,600\n선별 진료소 :  151\n경기도는 확진자에 비해 선별진료소가 적습니다")
    elif combobox.get() == '강원도':
         label.configure(text = "누적 확진자 :   390,879\n지역별 인구수 : 1,538,660\n선별 진료소 :  39\n강원도는 확진자에 비해 선별진료소가 많습니다")
    elif combobox.get() == '충청도':
         label.configure(text = "누적 확진자 :   1,382,746\n지역별 인구수 : 5,541,384\n선별 진료소 :  80\n충청도는 확진자에 비해 선별진료소가 많습니다")
    elif combobox.get() == '경상도':
         label.configure(text = "누적 확진자 :   3,317,421\n지역별 인구수 : 11,668,480\n선별 진료소 :  191\n경상도는 확진자에 비해 선별진료소가 많습니다")
    elif combobox.get() == '전라도':
         label.configure(text = "누적 확진자 :   1,316,618\n지역별 인구수 : 6,180,732\n선별 진료소 :  97\n전라도는 확진자에 비해 선별진료소가 많습니다")
    elif combobox.get() == '제주도':
        label.configure(text = "누적 확진자 :   187,860\n지역별 인구수 : 676,691\n선별 진료소 :  13\n제주도는 확진자에 비해 선별진료소가 적당합니다")

btn = Button(root, text="선택", command=btncmd)
#출력되는 문장을 받아오기 위한 버튼

btn.pack()
#버튼생성

label = Label(root)
#Label을 통해서 문장을 출력

label.pack() 

root.mainloop()
#실행
