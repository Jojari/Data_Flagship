import csv
import os

open_data = open("C:/Users/planning/Desktop/result_wind_3(20).csv", 'r', encoding="cp949")
data = csv.reader(open_data)

write_data = open("C:/Users/planning/Desktop/데이터플래그십/풍속_Result/result_wind_3(20).csv", 'w', newline="", encoding="cp949")
csv_writer = csv.writer(write_data)

i = 0

for line in data:
    if i > 0:
        if int(line[3]) > 2020:
            pass

        if int(line[4]) > 6:
            pass

        else:
            csv_writer.writerow(line)

    else:
        csv_writer.writerow(line)

    i += 1

write_data.close()
open_data.close()

### Merge_File의 코드가 이어짐 ###

write_data = open('C:/Users/planning/Desktop/데이터플래그십/result_wind_merged.csv', 'w', newline='', encoding='cp949')
csv_writer = csv.writer(write_data)

# 합칠 파일들이 있는 폴더의 Directory 입력(직접입력)
File_Directory = "C:/Users/planning/Desktop/데이터플래그십/풍속_Result/"

os.chdir(File_Directory)
file_list = os.listdir()

file_count = 0

for file_name in file_list:
    open_data = open(file_name, 'r', encoding="cp949")
    data = csv.reader(open_data)

    index = 0

    for line in data:
        if file_count > 0:
            if index > 0:
                csv_writer.writerow(line)
            index += 1

            if index % 10000 == 0:
                print(str(index) + '번째 라인까지 작성되었음')

        else:
            csv_writer.writerow(line)
            index += 1

            if index % 10000 == 0:
                print(str(index) + '번째 라인까지 작성되었음')

    file_count += 1
    open_data.close()

