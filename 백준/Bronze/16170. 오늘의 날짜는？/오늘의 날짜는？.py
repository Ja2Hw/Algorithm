import datetime
#datetime.datetime.now() 메소드는 우리 나라의 현재 시간을 나타냄 = 나라 기준
#우리나라는 UTC+9으로 세계 표준시(UTC+0)보다 9시간 앞서있다 
data = datetime.datetime.now() - datetime.timedelta(hours=9)

print(data.year)
print(data.month)
print(data.day)
