import pandas as pd
import pymysql
from tkinter import *
from tkinter import messagebox
from geopy import distance

def insertData():                      #새로운 가맹점 입점 함수
    conn = pymysql.connect(host='127.0.0.1', user='root', password='gkakqkqh123', db='outback', charset='utf8')
    cur = conn.cursor()
    cur2 = conn.cursor()
    cur3 = conn.cursor()
    data1 = edt1.get()                 #data1~data6은 tkinter창에서 입력받는 정보
    data2 = edt2.get()
    data3 = edt3.get()
    data4 = edt4.get()
    data5 = edt5.get()
    data6 = edt6.get()
    check_lon, check_lat, check_dis = [], [], []
    csvData1, csvData2, csvData3, csvData4, csvData5, csvData6 = [], [], [], [], [], []
    cur.execute("SELECT * FROM Restaurant")
    cur2.execute("SELECT * FROM close_Restaurant")
    while True:
        column = cur.fetchone()
        if column == None:
            break
        check_lon.append(column[4])
        check_lat.append(column[5])

    restid_check = []
    while True:
        column = cur2.fetchone()
        if column == None:
            break
        restid_check.append(column[0])                    #기존에 생성되었다가 폐점된 지점의 restid를 리스트로 저장
    if int(data1) in restid_check:
        messagebox.showerror('입점 불가', '이미 폐점된 지점입니다.')      #기존에 생성되었다가 폐점된 지점의 restid를 입력받으면 입점이 불가하다고 경고창 생성
    else:
        for i in range(len(check_lat)):
            check_dis.append(dis(float(data6), check_lat[i], float(data5), check_lon[i]))    #기존 가맹점들과 새로 입점할 가맹점의 위치를 비교


        if min(check_dis) < 1.8:
            messagebox.showerror('입점 불가', '반경 1.8km 안에 매장이 있습니다.')                  #기존 가맹점들과의 거리가 1.8km 미만이면 입점 불가
        else:
            try:
                data7 = f"ST_geomFromText('point({data5} {data6})')"
                sql = "INSERT INTO Restaurant VALUES(" + data1 + ", '" + data2 + "', '" + data3 + "', '" + data4 + "', '" + data5 + "', '" + data6 + "', " + data7 + ")"
                cur.execute(sql)                  #tkinter창에서 입력받은 데이터들을 mysql의 Restaurant테이블에 데이터를 저장해준다.

            except:
                messagebox.showerror('오류', '데이터 입력 오류가 발생함')          #제대로된 정보를 입력하지 않으면 입력이 불가하다고 경고창을 생성
            else:
                messagebox.showinfo('성공', '등록되었습니다.')                   #정확한 정보만 입력되면 등록 성공
    cur3.execute("SELECT * FROM Restaurant")
    while True:
        column = cur3.fetchone()
        if column == None:
            break
        csvData1.append(column[0])
        csvData2.append(column[1])
        csvData3.append(column[2])
        csvData4.append(column[3])
        csvData5.append(column[4])
        csvData6.append(column[5])
    csv_data = {'restID': csvData1, 'restname': csvData2, 'restaddr': csvData3, 'restphone': csvData4,
                'longitude': csvData5, 'latitude': csvData6}
    csv_dataframe = pd.DataFrame(csv_data)
    excel_file_name = 'outback_1.csv'
    csv_dataframe.to_csv(excel_file_name, header=True, index=False, encoding='cp949')

    conn.commit()
    conn.close()

def dis(x1, x2, y1, y2):                  #구에서 두 점사이의 거리를 구하는 함수(x1, y1은 새로 입점하고자 하는 가맹점의 위도, 경도/x2, y2는 기존 운영중인 가맹점들의 위도, 경도)
    a = (x1, y1)
    b = (x2, y2)
    c = distance.distance(a, b).km
    return c

def selectData():
    strData1, strData2, strData3, strData4, strData5, strData6 = [], [], [], [], [], []

    conn = pymysql.connect(host='127.0.0.1', user='root', password='gkakqkqh123', db='outback', charset='utf8')
    cur = conn.cursor()
    cur.execute("SELECT * FROM Restaurant")
    strData1.append("가맹점 번호");   strData2.append("가맹지점")
    strData3.append("가맹점 주소");     strData4.append("전화번호")
    strData5.append("경도");     strData6.append("위도")
    strData1.append("------------");    strData2.append("------------")
    strData3.append("------------");    strData4.append("------------")
    strData5.append("------------");    strData6.append("------------")
    while True:
        column = cur.fetchone()
        if column == None:
            break;
        strData1.append(column[0]);
        strData2.append(f"{column[0]})  {column[1]}")
        strData3.append(f"{column[0]})  {column[2]}")
        strData4.append(f"{column[0]})  {column[3]}")
        strData5.append(f"{column[0]})  {column[4]}")
        strData6.append(f"{column[0]})  {column[5]}")

    listData1.delete(0, listData1.size()-1);  listData2.delete(0, listData2.size()-1)
    listData3.delete(0, listData3.size()-1);  listData4.delete(0, listData4.size()-1)
    listData5.delete(0, listData5.size()-1);  listData6.delete(0, listData6.size()-1)
    for item1, item2, item3, item4, item5, item6 in zip(strData1, strData2, strData3, strData4, strData5, strData6):
        listData1.insert(END, item1);   listData2.insert(END, item2)
        listData3.insert(END, item3);   listData4.insert(END, item4)
        listData5.insert(END, item5);   listData6.insert(END, item6)
    conn.close()

def deleteData():
    conn = pymysql.connect(host='127.0.0.1', user='root', password='gkakqkqh123', db='outback', charset='utf8')
    cur = conn.cursor()
    cur2 = conn.cursor()
    cur3 = conn.cursor()
    cur4 = conn.cursor()
    data1 = edt1.get()
    checklist=[]
    cur.execute("SELECT * FROM Restaurant")
    cur2.execute(f"SELECT * FROM Restaurant WHERE restID = {data1}")

    while True:
        column = cur.fetchone()
        if column == None:
            break
        checklist.append(column[0])
    closelist1, closelist2, closelist3, closelist4, closelist5, closelist6 = [], [], [], [], [], []
    close_csvdata1, close_csvdata2, close_csvdata3, close_csvdata4, close_csvdata5, close_csvdata6 = [], [], [], [], [], []
    while True:
        column = cur2.fetchone()
        if column == None:
            break;
        closelist1.append(column[0])
        closelist2.append(column[1])
        closelist3.append(column[2])
        closelist4.append(column[3])
        closelist5.append(column[4])
        closelist6.append(column[5])

    data2 = closelist2
    data3 = closelist3
    data4 = closelist4
    data5 = closelist5
    data6 = closelist6

    if int(data1) in checklist:
        data7 = f"ST_geomFromText('point({data5[0]} {data6[0]})')"
        sql = "INSERT INTO close_restaurant VALUES(" + data1 + ", '" + data2[0] + "', '" + data3[0] + "', '" + data4[0] + "', '" + data5[0] + "', '" + data6[0] + "', "+ data7 +")"
        cur2.execute(sql)
        cur3.execute(f"SELECT * FROM close_restaurant")
        while True:
            column = cur3.fetchone()
            if column == None:
                break;
            close_csvdata1.append(column[0])
            close_csvdata2.append(column[1])
            close_csvdata3.append(column[2])
            close_csvdata4.append(column[3])
            close_csvdata5.append(column[4])
            close_csvdata6.append(column[5])
        close_csvdata = {'restID': close_csvdata1, 'restname': close_csvdata2, 'restaddr': close_csvdata3,
                         'restphone': close_csvdata4, 'longitude': close_csvdata5, 'latitude': close_csvdata6}
        close_csvdataframe = pd.DataFrame(close_csvdata)
        close_file_name = 'close_outback_1.csv'
        close_csvdataframe.to_csv(close_file_name, header=True, index=False, encoding='cp949')



        sql = f"DELETE FROM restaurant WHERE restID = {data1}"
        cur.execute(sql)
        messagebox.showinfo('성공', '데이터 삭제 성공')

        cur4.execute("SELECT * FROM Restaurant")
        update_list1, update_list2, update_list3, update_list4, update_list5, update_list6 = [], [], [], [], [], []
        while True:
            column = cur2.fetchone()
            if column == None:
                break;
            update_list1.append(column[0])
            update_list2.append(column[1])
            update_list3.append(column[2])
            update_list4.append(column[3])
            update_list5.append(column[4])
            update_list6.append(column[5])
        csv_data = {'restID': update_list1, 'restname':update_list2, 'restaddr': update_list3, 'restphone':update_list4,
                    'longitude': update_list5, 'latitude': update_list6}
        csv_dataframe = pd.DataFrame(csv_data)
        excel_file_name = 'outback_1.csv'
        csv_dataframe.to_csv(excel_file_name, header=True, index=False, encoding='cp949')





    else:
        messagebox.showerror('오류', '데이터 입력 오류가 발생함')
    conn.commit()
    conn.close()

def check_data():                     #로그인 tkinter 창에서 저장된 아이디/비밀번호를 입력했을 때 관리자 tkinter창으로 연결
    if (user_id.get() == "Passing" and password.get() == "Story")\
            or (user_id.get() == "outback" and password.get() == "abcd"):
       window_login.destroy()         #로그인 성공 시 로그인 tkinter창을 닫고 check 함수에서 생성한 관리자 tkinter창 생성
       check()
    else:
        messagebox.showerror("경고", "허용되지 않은 접근입니다.")

def check():                          #check_data에서 로그인에 성공하면 관리자 tkinter창 생성 함수
    window_manage = Tk()
    window_manage.title("가맹점 위치제한 입점 관리 시스템")
    window_manage.geometry('1200x500')
    edtFrame = Frame(window_manage)
    edtFrame.pack()
    listFrame = Frame(window_manage)
    listFrame.pack(side=BOTTOM, fill=BOTH, expand=1)
    global listData1, listData2, listData3, listData4, listData5, listData6
    global rest_ID, restName, restAddr, restPhone, longitude, latitude
    global edt1, edt2, edt3, edt4, edt5, edt6
    rest_ID = Label(edtFrame, text="가맹점 번호 :").pack(side=LEFT, pady=30)
    edt1 = Entry(edtFrame, width=10)
    edt1.pack(side=LEFT, padx=10, pady=10)
    restName = Label(edtFrame, text="가맹지점 :").pack(side=LEFT, pady=30)
    edt2 = Entry(edtFrame, width=10)
    edt2.pack(side=LEFT, padx=10, pady=10)
    restAddr = Label(edtFrame, text="가맹점 주소 :").pack(side=LEFT, pady=30)
    edt3 = Entry(edtFrame, width=10)
    edt3.pack(side=LEFT, padx=10, pady=10)
    restPhone = Label(edtFrame, text="전화번호 :").pack(side=LEFT, pady=30)
    edt4 = Entry(edtFrame, width=10)
    edt4.pack(side=LEFT, padx=10, pady=10)
    longitude = Label(edtFrame, text="경도 :").pack(side=LEFT, pady=30)
    edt5 = Entry(edtFrame, width=10)
    edt5.pack(side=LEFT, padx=10, pady=10)
    latitude = Label(edtFrame, text="위도 :").pack(side=LEFT, pady=30)
    edt6 = Entry(edtFrame, width=10)
    edt6.pack(side=LEFT, padx=10, pady=10)
    btnInsert = Button(edtFrame, text="입력", command=insertData)
    btnInsert.pack(side=LEFT, padx=10, pady=10)
    btnInsert = Button(edtFrame, text="조회", command=selectData)
    btnInsert.pack(side=LEFT, padx=10, pady=10)
    btnInsert = Button(edtFrame, text="삭제", command=deleteData)
    btnInsert.pack(side=LEFT, padx=10, pady=10)
    listData1 = Listbox(listFrame, bg='white')
    listData1.pack(side=LEFT, fill=BOTH)
    listData2 = Listbox(listFrame, bg='white')
    listData2.pack(side=LEFT, fill=BOTH)
    listData3 = Listbox(listFrame, bg='white')
    listData3.pack(side=LEFT, fill=BOTH, expand=1)
    listData4 = Listbox(listFrame, bg='white')
    listData4.pack(side=LEFT, fill=BOTH)
    listData5 = Listbox(listFrame, bg='white')
    listData5.pack(side=LEFT, fill=BOTH)
    listData6 = Listbox(listFrame, bg='white')
    listData6.pack(side=LEFT, fill=BOTH)
    window_manage.mainloop()

window_login = Tk()
window_login.title("관리자 로그인")
window_login.geometry('320x157')

wall = PhotoImage(file = "outback2.png")
Label(image = wall).place(x = -2,y = -2)

user_id, password = StringVar(), StringVar()

Label(window_login, text = "Username : ").grid(row = 0, column = 0, padx = 10, pady = 10)
Label(window_login, text = "Password : ").grid(row = 1, column = 0, padx = 10, pady = 10)
Entry(window_login, textvariable = user_id).grid(row = 0, column = 1, padx = 10, pady = 10)
Entry(window_login, textvariable = password, show ="*").grid(row = 1, column = 1, padx = 10, pady = 10)
Button(window_login, text = "Login", command = check_data).grid(row = 2, column = 1, padx = 10, pady = 10)

window_login.mainloop()