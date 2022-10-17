## Ⅰ. 엘페이 고객 유지/이탈 분류 데이터 분석 (분류 기준: 50일)

## 가. MySQL에서 불러오기
## 1. Lpoint DB와 연결
install.packages("RMySQL")
library(RMySQL)

lpointDB <- dbConnect(
  MySQL(),
  user='root',
  password='joowon',
  host='127.0.0.1',
  dbname='lpoint'
)

dbSendQuery(lpointDB, 'set character set "utf8"')


## 2. 재이용기간 테이블 조회 (reuse_days)
reuse_days <- dbGetQuery(
  lpointDB,
  "Select * From 재이용기간;"
)


## 3. 엘페이이용정보 테이블 조회 (lpay_use_50)
lpay_use_50 <- dbGetQuery(
  lpointDB,
  "Select * From 엘페이이용정보;"
)


## 4. 엘페이를 이용한 고객의 고객정보 (성별, 연령대, 거주지코드)
lpay_cust_info<-dbGetQuery(
  lpointDB,
  "Select * From 고객정보 c Inner Join 엘페이이용정보 l on c.cust=l.cust;"
)


## 5. 엘페이를 이용한 고객의 이용정보 (제휴사코드, 거래수량, 채널, 거래일자(요일, 시간, 월))
lpay_use_info_50<-dbGetQuery(
  lpointDB,
  "Select * From 엘페이이용_view l Inner Join 엘페이이용정보 u On l.cust=u.cust;"
)


## 6. 고객을 범주형 변수로 만들기 위한 칼럼 추가
# 재구매기간이 50일 이내인 고객 -> '유지' 
#                   이상인 고객 -> '이탈'
lpay_use_50 <-transform(lpay_use_50, cust_dv=ifelse(max_days <= 50, "유지","이탈")) 



## 나. 변수 유의성 검정

## 1. 인구 통계학적 속성 분석

## 1) 성별과 이탈여부
# 사용할 변수 지정
cust_dv_50 <- lpay_use_50$cust_dv  # 고객 유지/이탈 구분
ma_fem_dv <- lpay_cust_info$ma_fem_dv  # 성별

# 빈도표 생성 (두개의 범주형 변수에 대한 빈도 표시) 
tab_50 <- table(ma_fem_dv,cust_dv_50)
print(tab_50)

# 카이제곱 검정
res_50 <- chisq.test(tab_50)

# 기대빈도 확인
# 기대빈도가 5미만인 셀이 없을 경우, 카이제곱 검정의 가정을 만족하는 것
res_50$expected

res_50



## 2) 연령대와 이탈여부
# 사용할 변수 지정
cust_dv_50 <- lpay_use_50$cust_dv  # 고객 유지/이탈 구분
ages <- lpay_cust_info$ages   # 연령대

# 빈도표 생성 (두개의 범주형 변수에 대한 빈도 표시) 
tab2_50 <- table(ages,cust_dv_50)
print(tab2_50)

## 카이제곱 검정
res2_50 <- chisq.test(tab2_50)

# 기대빈도 확인
# 기대빈도가 5미만인 셀이 없을 경우, 카이제곱 검정의 가정을 만족하는 것
res2_50$expected

res2_50



## 3) 거주지와 이탈여부
# 사용할 변수 지정
cust_dv_50 <- lpay_use_50$cust_dv    # 고객 유지/이탈 구분
zon_hlv <- lpay_cust_info$zon_hlv    # 거주지

# 빈도표 생성 (두개의 범주형 변수에 대한 빈도 표시) 
tab3_50 <- table(zon_hlv,cust_dv_50)
print(tab3_50)

# 카이제곱 검정
res3_50 <- chisq.test(tab3_50)

# 기대빈도 확인
# 기대빈도가 5미만인 셀이 없을 경우, 카이제곱 검정의 가정을 만족하는 것
res3_50$expected

res3_50



## 2. 구매행태적 속성 분석

## 1) 제휴사코드와 이탈여부

# 빈도표 생성(두개의 범주형 변수에 대한 빈도 표시) 
# 유지/이탈 구분 포함
table1_50 <- dbGetQuery(
  lpointDB,
  "select  round(sum(A01),0) as A01, round(sum(A02),0) as A02 ,round(sum(A03),0) as A03, round(sum(A04),0) as A04, round(sum(A05),0) as A05, round(sum(A06),0) as A06,
round(sum(B01),0) as B01, round(sum(C01),0) as C01, round(sum(C02),0) as C02, round(sum(D01),0) as D01, round(sum(D02),0) as D02, round(sum(E01),0) as E01, round(sum(L00),0) as L00, round(sum(L01),0) as L01,  
(case when max_days<=50 then '유지' else '이탈' end) as 구분
FROM 제휴사별이용비율 j INNER JOIN 재이용기간 r ON j.cust=r.cust
group by 구분
order by 구분;"
)

# 유지/이탈 구분 미포함 (1: 유지 2: 이탈)
cop_50 <- table1_50[1:14]
cop_50

# 카이제곱 검정
result_50<-chisq.test(cop_50)

# 기대빈도 확인
# 기대빈도가 5미만인 셀이 없을 경우, 카이제곱 검정의 가정을 만족하는 것
result_50$expected

result_50


## 2) 채널구분과 이탈여부

# 빈도표 생성(두개의 범주형 변수에 대한 빈도 표시) 
# 유지/이탈 구분 포함
table2_50 <- dbGetQuery(
  lpointDB,
  "SELECT  round(sum(오프라인),0) AS 오프라인, round(sum(온라인),0) AS 온라인,  
(CASE WHEN max_days<=50 THEN '유지' ELSE '이탈' END) AS 구분
FROM 채널별이용비율 j INNER JOIN 재이용기간 r ON j.cust=r.cust
GROUP BY 구분
ORDER BY 구분;"
)

# 유지/이탈 구분 미포함 (1: 유지 2: 이탈)
chnl_50 <- table2_50[1:2]
chnl_50

# 카이제곱 검정
result2_50 <- chisq.test(chnl_50)

# 기대빈도 확인
# 기대빈도가 5미만인 셀이 없을 경우, 카이제곱 검정의 가정을 만족하는 것
result2_50$expected

result2_50


## 3) 이용일수와 이탈여부

# count_days랑 cust_dv 사용 
# count_days가 1인 사람도 포함  => lpay_use_50 테이블만 사용 
count_days_50 <- lpay_use_50$count_days

# 고객들의 평균 이용 일수
mean(count_days_50)

# 유지고객의 count_days 
re_cust_50 <- subset(lpay_use_50, cust_dv=="유지")
data1_50 <- re_cust_50$count_days

# 이탈고객의 count_days 
no_cust_50 <- subset(lpay_use_50, cust_dv=="이탈")
data2_50 <- no_cust_50$count_days

# t 검정 (연속형 변수와 범주형 변수의 검정 방법) 
t.test(data1_50, data2_50, var.equal = FALSE) # p-value < 0.05: 두 집단의 평균은 다르다 

