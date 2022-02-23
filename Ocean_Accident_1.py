import csv
from datetime import datetime

# Full-Column Name list(향후 활용 시 참고용)
colnames = ['GRID_ID', 'GRID_X', 'GRID_Y', 'YEAR', 'MONTH', 'DATE', 'HOUR', '12~1(월)', '2~3(월)', '4~5(월)', '6~7(월)', '8~9(월)', '10~11(월)', '0~3(시)', '3~6(시)', '6~9(시)', '9~12(시)', '12~15(시)', '15~18(시)', '18~21(시)', '21~24(시)',
                     '파고부이', '최대파고', '유의파고', '평균파고', '파주기', '풍속부이', '풍속', 'GUST풍속']

### 파일 일련번호 ###
num = 1

#1. 파고 처리
write_data = open('C:/Users/planning/Desktop/데이터플래그십/파고_Result/result_wave_' + str(num) + '.csv', 'w', newline='', encoding='cp949')
csv_writer = csv.writer(write_data)
csv_writer.writerow(['GRID_ID', 'GRID_X', 'GRID_Y', 'YEAR', 'MONTH', 'DATE', 'HOUR', '파고부이', '최대파고', '유의파고', '평균파고', '파주기'])

write_data.close()

# GRID Filename은 그리드 파일명 / Wave_Filename은 파고 파일명 / StartDate와 EndDate는 시작 및 종료일을 Datetime 데이터타입으로 Input
def WriteWave(GRID_Filename, Wave_Filename, StartDate, EndDate):
    open_grid_data = open('C:/Users/planning/Desktop/데이터플래그십/1. 파고/그리드별_최근접파고관측지점/' + GRID_Filename, 'r', encoding='cp949')
    grid_data = csv.reader(open_grid_data)

    write_data = open('C:/Users/planning/Desktop/데이터플래그십/파고_Result/result_wave_' + str(num) + '.csv', 'a', newline='', encoding='cp949')
    csv_writer = csv.writer(write_data)

    i = 0

    for grid_line in grid_data:

        if i > 0:
            result = [grid_line[0], grid_line[1], grid_line[2], 0, 0, 0, 0, grid_line[4], '', '', '', '']

            j = 0

            open_wave_data = open('C:/Users/planning/Desktop/데이터플래그십/1. 파고/' + Wave_Filename, 'r', encoding='cp949')
            wave_data = csv.reader(open_wave_data)

            for wave_line in wave_data:
                if j > 0:
                    dateT = datetime.strptime(wave_line[1], '%Y-%m-%d %H:%M')

                    if StartDate <= dateT and dateT < EndDate:
                        if grid_line[4] == wave_line[0]:
                            result = [grid_line[0], grid_line[1], grid_line[2], dateT.strftime('%Y'), dateT.strftime('%m'), dateT.strftime('%d'), dateT.strftime('%H'), grid_line[4], wave_line[3], wave_line[4], wave_line[5], wave_line[6]]
                            csv_writer.writerow(result)

                j += 1

            open_wave_data.close()

        print(grid_line)

        i += 1

    write_data.close()
    open_grid_data.close()

############################################################

#2. 풍속 처리
write_data = open('C:/Users/planning/Desktop/데이터플래그십/result_wind_' + str(num) + '.csv', 'w', newline='', encoding='cp949')
csv_writer = csv.writer(write_data)
csv_writer.writerow(['GRID_ID', 'GRID_X', 'GRID_Y', 'YEAR', 'MONTH', 'DATE', 'HOUR', '풍속부이', '풍속', 'GUST풍속'])

write_data.close()

# WriteWind의 경우, WriteWave의 결과파일에 연월일시 및 그리드ID를 기준으로 풍속부이 및 풍속관측값을 조인할 것이므로 간단히 작성됨
def WriteWind(GRID_Filename, Wind_Filename, StartDate, EndDate):
    open_grid_data = open('C:/Users/planning/Desktop/데이터플래그십/2. 풍속/그리드별_최근접풍속관측지점/' + GRID_Filename, 'r', encoding='cp949')
    grid_data = csv.reader(open_grid_data)

    write_data = open('C:/Users/planning/Desktop/데이터플래그십/result_wind_' + str(num) + '.csv', 'a', newline='', encoding='cp949')
    csv_writer = csv.writer(write_data)

    i = 0

    for grid_line in grid_data:

        if i > 0:
            result_2 = [grid_line[0], grid_line[1], grid_line[2], 0, 0, 0, 0, grid_line[4], '', '']

            j = 0

            open_wind_data = open('C:/Users/planning/Desktop/데이터플래그십/2. 풍속/' + Wind_Filename, 'r', encoding='cp949')
            wind_data = csv.reader(open_wind_data)

            for wind_line in wind_data:
                if j > 0:
                    dateT = datetime.strptime(wind_line[1], '%Y-%m-%d %H:%M')

                    if StartDate <= dateT and dateT < EndDate:
                        if grid_line[4] == wind_line[0]:
                            result_2 = [grid_line[0], grid_line[1], grid_line[2], dateT.strftime('%Y'), dateT.strftime('%m'), dateT.strftime('%d'), dateT.strftime('%H'), grid_line[4], wind_line[2], wind_line[4]]
                            csv_writer.writerow(result_2)

                j += 1

            open_wind_data.close()

        print(grid_line)

        i += 1

    write_data.close()
    open_grid_data.close()

############################################################

WriteWave('1-1.csv', '2018_파고.csv', datetime(2018, 1, 1, 00), datetime(2018, 9, 17, 00))
'''WriteWave('1-2.csv', '2018_파고.csv', datetime(2018, 9, 17, 00), datetime(2018, 11, 1, 00))
WriteWave('1-3.csv', '2018_파고.csv', datetime(2018, 11, 1, 00), datetime(2019, 1, 1, 00))

WriteWave('1-3.csv', '2019_파고.csv', datetime(2019, 1, 1, 00), datetime(2019, 12, 20, 00))
WriteWave('1-4.csv', '2019_파고.csv', datetime(2019, 12, 20, 00), datetime(2020, 1, 1, 00))

WriteWave('1-4.csv', '2020_파고.csv', datetime(2020, 1, 1, 00), datetime(2020, 11, 16, 00))
WriteWave('1-5.csv', '2020_파고.csv', datetime(2020, 11, 16, 00), datetime(2020, 12, 4, 00))
WriteWave('1-6.csv', '2020_파고.csv', datetime(2020, 12, 4, 00), datetime(2021, 1, 1, 00))


WriteWind('2-1.csv', '2018_풍속.csv', datetime(2018, 1, 1, 00), datetime(2019, 1, 1, 00))

WriteWind('2-1.csv', '2019_풍속.csv', datetime(2019, 1, 1, 00), datetime(2019, 11, 2, 00))
WriteWind('2-2.csv', '2019_풍속.csv', datetime(2019, 11, 2, 00), datetime(2019, 11, 5, 00))
WriteWind('2-3.csv', '2019_풍속.csv', datetime(2019, 11, 5, 00), datetime(2019, 12, 9, 00))
WriteWind('2-4.csv', '2019_풍속.csv', datetime(2019, 12, 9, 00), datetime(2020, 1, 1, 00))

WriteWind('2-4.csv', '2020_풍속.csv', datetime(2020, 1, 1, 00), datetime(2020, 2, 24, 00))
WriteWind('2-5.csv', '2020_풍속.csv', datetime(2020, 2, 24, 00), datetime(2021, 1, 1, 00))'''