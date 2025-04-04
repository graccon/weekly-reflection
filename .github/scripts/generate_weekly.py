import datetime
import os

# 오늘 날짜 정보
today = datetime.date.today()
year = today.year
month = today.month

# 주차 계산 (해당 월 기준 몇 번째 주인지)
def get_week_of_month(date):
    first_day = date.replace(day=1)
    adjusted_dom = date.day + first_day.weekday()
    return int((adjusted_dom - 1) / 7 + 1)

week = get_week_of_month(today)

# 파일명: WK2025_04_01.md
filename = f"WK{year}_{month:02d}_{week:02d}.md"
folder = f"{year}"
filepath = os.path.join(folder, filename)

# 이미 존재하면 건너뜀
if os.path.exists(filepath):
    print(f"{filepath} already exists. Skipping.")
    exit(0)

# 템플릿 불러오기
with open("templates/weekly_template.md", "r", encoding="utf-8") as f:
    template = f.read()

# 템플릿 값 치환
filled = template.replace("{{YEAR}}", str(year)) \
                 .replace("{{MONTH}}", f"{month:02d}") \
                 .replace("{{WEEK}}", f"{week:02d}") \
                 .replace("{{DATE}}", today.strftime("%Y.%m.%d"))

# 디렉토리 없으면 생성
os.makedirs(folder, exist_ok=True)

# 회고 파일 생성
with open(filepath, "w", encoding="utf-8") as f:
    f.write(filled)