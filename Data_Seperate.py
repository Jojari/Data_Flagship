import csv
import os

os.chdir('C:\\Users\\planning\\Desktop\\데이터플래그십\\')

open_wave_data = open('파고_Result\\result_wave_1.csv', 'r', encoding = 'cp949')
wave_data = csv.reader(open_wave_data)

write_new_wave = open('파고_201801_sample.csv', 'w', newline = '', encoding = 'cp949')
csv_writer_wave = csv.writer(write_new_wave)

index = 0

for line in wave_data:
    if index > 0:
        if int(line[4]) == 1 and int(line[5]) <= 10:
            csv_writer_wave.writerow(line)
        else:
            pass

    else:
        csv_writer_wave.writerow(line)

    index += 1

open_wave_data.close()
write_new_wave.close()

open_wind_data = open('풍속_Result\\result_wind_1(18).csv', 'r', encoding = 'cp949')
wind_data = csv.reader(open_wind_data)

write_new_wind = open('풍속_201801_sample.csv', 'w', newline='', encoding = 'cp949')
csv_writer_wind = csv.writer(write_new_wind)

index = 0

for line in wind_data:
    if index > 0:
        if int(line[4]) == 1 and int(line[5]) <= 10:
            csv_writer_wind.writerow(line)
        else:
            pass

    else:
        csv_writer_wind.writerow(line)

    index += 1

open_wind_data.close()
write_new_wind.close()