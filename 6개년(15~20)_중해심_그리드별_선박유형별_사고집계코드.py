import csv
import os

'''os.chdir('D:/2021/1. Works/6. 데이터플래그십/1. 데이터플래그십 데이터 가공/4. 그리드별 선박유형별 사고비율분석/')

open_data = open('중해심_그리드별_해양사고_Binary_15_to_20_4326.csv', 'r', encoding='cp949')
data = csv.reader(open_data)

write_data_2015 = open('연도별/중해심_그리드별_해양사고_Binary_2015_4326.csv', 'w', newline="", encoding='cp949')
csv_writer_2015 = csv.writer(write_data_2015)

write_data_2016 = open('연도별/중해심_그리드별_해양사고_Binary_2016_4326.csv', 'w', newline="", encoding='cp949')
csv_writer_2016 = csv.writer(write_data_2016)

write_data_2017 = open('연도별/중해심_그리드별_해양사고_Binary_2017_4326.csv', 'w', newline="", encoding='cp949')
csv_writer_2017 = csv.writer(write_data_2017)

write_data_2018 = open('연도별/중해심_그리드별_해양사고_Binary_2018_4326.csv', 'w', newline="", encoding='cp949')
csv_writer_2018 = csv.writer(write_data_2018)

write_data_2019 = open('연도별/중해심_그리드별_해양사고_Binary_2019_4326.csv', 'w', newline="", encoding='cp949')
csv_writer_2019 = csv.writer(write_data_2019)

write_data_2020 = open('연도별/중해심_그리드별_해양사고_Binary_2020_4326.csv', 'w', newline="", encoding='cp949')
csv_writer_2020 = csv.writer(write_data_2020)

idx = 0

for line in data:
    if idx != 0:
        row = line[1:]

        if line[0] == '2015':
            print(line[0])
            csv_writer_2015.writerow(row)

        if line[0] == '2016':
            print(line[0])
            csv_writer_2016.writerow(row)

        if line[0] == '2017':
            print(line[0])
            csv_writer_2017.writerow(row)

        if line[0] == '2018':
            print(line[0])
            csv_writer_2018.writerow(row)

        if line[0] == '2019':
            print(line[0])
            csv_writer_2019.writerow(row)

        if line[0] == '2020':
            print(line[0])
            csv_writer_2020.writerow(row)

    else:
        colnames = line[1:]

        csv_writer_2015.writerow(colnames)
        csv_writer_2016.writerow(colnames)
        csv_writer_2017.writerow(colnames)
        csv_writer_2018.writerow(colnames)
        csv_writer_2019.writerow(colnames)
        csv_writer_2020.writerow(colnames)

    idx += 1

write_data_2015.close()
write_data_2016.close()
write_data_2017.close()
write_data_2018.close()
write_data_2019.close()
write_data_2020.close()
open_data.close()'''

####################################################################################

os.chdir('C:/Users/Planning/Desktop/중해심_작업폴더/')
open_data = open('KOMSA_Damage_and_Age_Type_By_GRID.csv', 'r', encoding='cp949')
data = csv.reader(open_data)

GID_Dict = {}

for idx, line in enumerate(data):
    if idx > 0:
        if line[0] not in GID_Dict:
            GID_Dict[line[0]] = {'선박연령': [], '피해구분': []}

        GID_Dict[line[0]]['선박연령'].append(line[4])
        GID_Dict[line[0]]['피해구분'].append(line[5])

print(GID_Dict)

open_data.close()

write_data = open('KOMSA_Damage_and_Age_Type_By_GRID_mod.csv', 'w', newline='', encoding='cp949')
csv_writer = csv.writer(write_data)

csv_writer.writerow(['GID', '선박연령', '피해구분'])

for GID in GID_Dict.keys():
    Grid_ID = int(GID)

    try:
        Ship_Age = int(GID_Dict[GID]['선박연령'])

    except TypeError:
        Ship_Age = GID_Dict[GID]['선박연령']

    Ship_Damage = GID_Dict[GID]['피해구분']

    csv_writer.writerow([Grid_ID, Ship_Age, Ship_Damage])

write_data.close()