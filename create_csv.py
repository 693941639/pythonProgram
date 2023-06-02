import csv
import datetime
import random

# 生成2016年的日期范围
start_date = datetime.date(2016, 1, 1)
end_date = datetime.date(2016, 12, 31)
date_range = [start_date + datetime.timedelta(days=x) for x in range((end_date - start_date).days + 1)]

# 打开CSV文件
with open('data.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)

    # 写入表头
    writer.writerow(['year', 'month', 'day', 'week', 'temp-2', 'temp-1', 'average', 'actual'])

    # 生成每一天的数据
    for date in date_range:
        year = date.year
        month = date.month
        day = date.day
        weekday = date.strftime('%A')
        temperature_2 = random.randint(0, 30)  # 前俩天的温度
        temperature_1 = random.randint(0, 30)  # 前一天的温度
        historical_avg = random.randint(0, 30)  # 历史以来当天的平均温度
        temperature = random.randint(0, 30)  # 当天的温度

        # 写入一行数据
        writer.writerow([year, month, day, weekday, temperature_2, temperature_1, historical_avg, temperature])
