import csv
import os

os.chdir('D:/데이터플래그십 관련 자료')

open_data = open('DataFlagship_Accidents_and_Attributes_by_Grid(2018-2020).csv', 'r', encoding='cp949')
data = csv.reader(open_data)

write_data = open('DataFlagship_Accidents_and_Attributes_by_Grid(2018-2020)_final.csv', 'w', newline='', encoding='cp949')
csv_writer = csv.writer(write_data)

for idx, line in enumerate(data):
    if idx % 100000 == 0:
        print(str(idx) + '번째 줄 작성중...')
    if idx > 0:
        col_1 = line[:-12]
        col_month = [0, 0, 0, 0, 0, 0]
        col_time = [0, 0, 0, 0, 0, 0]
        col_2 = line[-6:]

        if int(line[5]) in [12, 1]:
            col_month[0] = 1
        if int(line[5]) in [2, 3]:
            col_month[1] = 1
        if int(line[5]) in [4, 5]:
            col_month[2] = 1
        if int(line[5]) in [6, 7]:
            col_month[3] = 1
        if int(line[5]) in [8, 9]:
            col_month[4] = 1
        if int(line[5]) in [10, 11]:
            col_month[5] = 1

        if 0 <= int(line[7]) < 4:
            col_time[0] = 1
        if 4 <= int(line[7]) < 8:
            col_time[1] = 1
        if 8 <= int(line[7]) < 12:
            col_time[2] = 1
        if 12 <= int(line[7]) < 16:
            col_time[3] = 1
        if 16 <= int(line[7]) < 20:
            col_time[4] = 1
        if 20 <= int(line[7]) < 24:
            col_time[5] = 1

        col = col_1 + col_month + col_time + col_2

        csv_writer.writerow(col)

    else:
        colname_1 = line[:-12]
        colname_2 = ['12-1월', '2-3월', '4-5월', '6-7월', '8-9월', '10-11월']
        colname_3 = line[-12:]

        colnames = colname_1 + colname_2 + colname_3
        csv_writer.writerow(colnames)

open_data.close()
write_data.close()

'''open_data = open('DataFlagship_Accidents_and_Attributes_by_Grid(2018-2020)_final.csv', 'r', encoding='cp949')
data = csv.reader(open_data)

write_data = open('DataFlagship_Accidents_and_Attributes_by_Grid(2018-2020)_verify.csv', 'w', newline='', encoding='cp949')
csv_writer = csv.writer(write_data)

for idx, line in enumerate(data):
    csv_writer.writerow(line)

    if idx > 10000:
        break

open_data.close()'''