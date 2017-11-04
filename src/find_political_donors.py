import os.path
import csv
import heapq
import datetime

with open(os.path.dirname(os.path.abspath(__file__)) + '/../input/itcont.txt') as infile:
    with open (os.path.dirname(os.path.abspath(__file__)) + '/../output/medianvals_by_zip.txt','w') as zipfile:
        reader = csv.reader(infile, delimiter='|')
        zip_writer = csv.writer(zipfile, delimiter='|')
        zip_stats = []
        date_stats = []
        for row in reader:

            if row[0] != '' and row[14] != '' and row[15] == '':

                if len(row[10]) >= 5:
                    tail=len(zip_stats)
                    trans_amt = int(row[14])
                    index = next((i for i, x in enumerate(zip_stats) if x[0] == row[0] and x[1] == row[10][0:5]),'null')
                    if index == 'null':
                        zip_stats_append = [row[0], row[10][0:5], trans_amt, 1, trans_amt, [-trans_amt], [], 1]
                        zip_stats.append(zip_stats_append)
                        heapq.heapify(zip_stats[tail][5])
                        heapq.heapify(zip_stats[tail][6])
                        zip_writer.writerow(zip_stats[tail][0:5])
                        # print(0)
                    else:
                        zip_stats[index][3] = zip_stats[index][3] + 1
                        zip_stats[index][4] = zip_stats[index][4] + trans_amt
                        if trans_amt <= -zip_stats[index][5][0]:
                            heapq.heappush(zip_stats[index][5], -trans_amt)
                            zip_stats[index][7] = zip_stats[index][7] + 1
                        else:
                            heapq.heappush(zip_stats[index][6], trans_amt)
                            zip_stats[index][7] = zip_stats[index][7] - 1
                        if zip_stats[index][7] == 2:
                            heapq.heappush(zip_stats[index][6], -heapq.heappop(zip_stats[index][5]))
                            zip_stats[index][7] = 0
                            sums = zip_stats[index][6][0] - zip_stats[index][5][0]
                            if sums % 2 == 0:
                                zip_stats[index][2] = int(sums / 2)
                            else:
                                zip_stats[index][2] = int((sums + 1) / 2)
                        elif zip_stats[index][7] == -2:
                            heapq.heappush(zip_stats[index][5], -heapq.heappop(zip_stats[index][6]))
                            zip_stats[index][7] = 0
                            sums = zip_stats[index][6][0] - zip_stats[index][5][0]
                            if sums % 2 == 0:
                                zip_stats[index][2] = int(sums / 2)
                            else:
                                zip_stats[index][2] = int((sums + 1) / 2)
                        elif zip_stats[index][7] == 0:
                            sums = zip_stats[index][6][0] - zip_stats[index][5][0]
                            if sums % 2 == 0:
                                zip_stats[index][2] = int(sums / 2)
                            else:
                                zip_stats[index][2] = int((sums + 1) / 2)
                        elif zip_stats[index][7] == 1:
                            zip_stats[index][2] = -zip_stats[index][5][0]
                        elif zip_stats[index][7] == -1:
                            zip_stats[index][2] = zip_stats[index][6][0]
                        zip_writer.writerow(zip_stats[index][0:5])
                        # print(0)

                if len(row[13]) == 8 and int(row[13][0:2]) <= 12 and int(row[13][2:4]) <= 31 and (int(row[13][4:8]) >= 2015 and int(row[13][4:8]) <= 2017):
                    date = datetime.datetime.strptime(row[13],'%m%d%Y')
                    tail=len(date_stats)
                    trans_amt = int(row[14])
                    index = next((i for i, x in enumerate(date_stats) if x[0] == row[0] and x[1] == date),'null')
                    if index == 'null':
                        date_stats_append = [row[0], date, trans_amt, 1, trans_amt, [-trans_amt], [], 1]
                        date_stats.append(date_stats_append)
                        heapq.heapify(date_stats[tail][5])
                        heapq.heapify(date_stats[tail][6])
                        #date_writer.writerow(date_stats[tail][0:5])
                        # print(0)
                    else:
                        date_stats[index][3] = date_stats[index][3] + 1
                        date_stats[index][4] = date_stats[index][4] + trans_amt
                        if trans_amt <= -date_stats[index][5][0]:
                            heapq.heappush(date_stats[index][5], -trans_amt)
                            date_stats[index][7] = date_stats[index][7] + 1
                        else:
                            heapq.heappush(date_stats[index][6], trans_amt)
                            date_stats[index][7] = date_stats[index][7] - 1
                        if date_stats[index][7] == 2:
                            heapq.heappush(date_stats[index][6], -heapq.heappop(date_stats[index][5]))
                            date_stats[index][7] = 0
                            sums = date_stats[index][6][0] - date_stats[index][5][0]
                            if sums % 2 == 0:
                                date_stats[index][2] = int(sums / 2)
                            else:
                                date_stats[index][2] = int((sums + 1) / 2)
                        elif date_stats[index][7] == -2:
                            heapq.heappush(date_stats[index][5], -heapq.heappop(date_stats[index][6]))
                            date_stats[index][7] = 0
                            sums = date_stats[index][6][0] - date_stats[index][5][0]
                            if sums % 2 == 0:
                                date_stats[index][2] = int(sums / 2)
                            else:
                                date_stats[index][2] = int((sums + 1) / 2)
                        elif date_stats[index][7] == 0:
                            sums = date_stats[index][6][0] - date_stats[index][5][0]
                            if sums % 2 == 0:
                                date_stats[index][2] = int(sums / 2)
                            else:
                                date_stats[index][2] = int((sums + 1) / 2)
                        elif date_stats[index][7] == 1:
                            date_stats[index][2] = -date_stats[index][5][0]
                        elif date_stats[index][7] == -1:
                            date_stats[index][2] = date_stats[index][6][0]
                        #date_writer.writerow(date_stats[index][0:5])
                        # print(0)

date_stats = sorted(date_stats,key=lambda x: (x[0],x[1]))

with open(os.path.dirname(os.path.abspath(__file__)) + '/../output/medianvals_by_date.txt', 'w') as datefile:
    date_writer = csv.writer(datefile, delimiter='|')
    for row in date_stats:
        row[1] = row[1].strftime('%m%d%Y')
        date_writer.writerow(row[0:5])