# 1. 模組匯入 (Modules Import)
# 匯入內建的 datetime 模組（處理日期）與自訂的 bday_messages 
import datetime, bday_messages
# 2. 取得今天的日期
today = datetime.date.today()
# 3. 設定下一個生日的日期
next_birthday = datetime.date(2027, 7, 3)
# 4. 計算下一個生日距離今天的天數
days_away = (next_birthday - today).days
if today == next_birthday:
    print(bday_messages.random_message)
else:
    print(f'My next birthday is {days_away} days away!')

# 5. 計算已經活了多少天、多少年、多少月
day_lived = (today - datetime.date(1994, 7, 3)).days
years = day_lived // 365       
remaining_days = day_lived % 365 
months = remaining_days // 30
print(f'I have lived for {years} years and {months} months!')

# 6. 計算距離 80 歲還有多少天，輸入出生年月日
birth_year = 1994
birth_month = 7
birth_day = 3
eighty_bday = datetime.date(birth_year + 80, birth_month, birth_day)
days_left = (eighty_bday - today).days

print(f"The average life expectancy in Taiwan is 80 years old. I have {days_left} days left to live. Carpe diem and have fun!" )
