# -*- coding: utf-8 -*-
"""
author: Zhong Peng
createDate: 2017-04-19
lastModified: 2017-04-19
generate arff format files
"""
import csv
import os


# all_info_li = [[author_name, char_1, char_2, char_3, char_4, char_5, char_6, char_7, class], ]
all_info_li = list()
with open(r"author_characters.csv", "rb") as csvfile:
    reader = csv.reader(csvfile, dialect="excel")
    for row in reader:
        if reader.line_num <= 679:
            row.append("+1")
        elif reader.line_num > 25621:
            row.append("-1")
        else:
            continue
        all_info_li.append(row)
print "all_info_li init over"

char_1_li = list()
char_2_li = list()
char_3_li = list()
char_4_li = list()
char_5_li = list()
char_6_li = list()
char_7_li = list()
for item in all_info_li:
    char_1_li.append("{},{}{}".format(int(item[1]), item[-1], os.linesep))
    char_2_li.append("{},{}{}".format(int(item[2]), item[-1], os.linesep))
    char_3_li.append("{},{}{}".format(float(item[3]), item[-1], os.linesep))
    char_4_li.append("{},{}{}".format(int(item[4]), item[-1], os.linesep))
    char_5_li.append("{},{}{}".format(float(item[5]), item[-1], os.linesep))
    char_6_li.append("{},{}{}".format(float(item[6]), item[-1], os.linesep))
    char_7_li.append("{},{}{}".format(float(item[7]), item[-1], os.linesep))

with open(r"character_1.arff", "wb") as f:
    f.write("@RELATION char_1{}".format(os.linesep))
    f.write(os.linesep)
    f.write("@ATTRIBUTE char    REAL{}".format(os.linesep))
    f.write("@ATTRIBUTE class    {}{}".format("{+1, -1}", os.linesep))
    f.write(os.linesep)
    f.write("@DATA{}".format(os.linesep))
    f.writelines(char_1_li)

with open(r"character_2.arff", "wb") as f:
    f.write("@RELATION char_2{}".format(os.linesep))
    f.write(os.linesep)
    f.write("@ATTRIBUTE char    REAL{}".format(os.linesep))
    f.write("@ATTRIBUTE class    {}{}".format("{+1, -1}", os.linesep))
    f.write(os.linesep)
    f.write("@DATA{}".format(os.linesep))
    f.writelines(char_2_li)

with open(r"character_3.arff", "wb") as f:
    f.write("@RELATION char_3{}".format(os.linesep))
    f.write(os.linesep)
    f.write("@ATTRIBUTE char    REAL{}".format(os.linesep))
    f.write("@ATTRIBUTE class    {}{}".format("{+1, -1}", os.linesep))
    f.write(os.linesep)
    f.write("@DATA{}".format(os.linesep))
    f.writelines(char_3_li)

with open(r"character_4.arff", "wb") as f:
    f.write("@RELATION char_4{}".format(os.linesep))
    f.write(os.linesep)
    f.write("@ATTRIBUTE char    REAL{}".format(os.linesep))
    f.write("@ATTRIBUTE class    {}{}".format("{+1, -1}", os.linesep))
    f.write(os.linesep)
    f.write("@DATA{}".format(os.linesep))
    f.writelines(char_4_li)

with open(r"character_5.arff", "wb") as f:
    f.write("@RELATION char_5{}".format(os.linesep))
    f.write(os.linesep)
    f.write("@ATTRIBUTE char    REAL{}".format(os.linesep))
    f.write("@ATTRIBUTE class    {}{}".format("{+1, -1}", os.linesep))
    f.write(os.linesep)
    f.write("@DATA{}".format(os.linesep))
    f.writelines(char_5_li)

with open(r"character_6.arff", "wb") as f:
    f.write("@RELATION char_6{}".format(os.linesep))
    f.write(os.linesep)
    f.write("@ATTRIBUTE char    REAL{}".format(os.linesep))
    f.write("@ATTRIBUTE class    {}{}".format("{+1, -1}", os.linesep))
    f.write(os.linesep)
    f.write("@DATA{}".format(os.linesep))
    f.writelines(char_6_li)

with open(r"character_7.arff", "wb") as f:
    f.write("@RELATION char_7{}".format(os.linesep))
    f.write(os.linesep)
    f.write("@ATTRIBUTE char    REAL{}".format(os.linesep))
    f.write("@ATTRIBUTE class    {}{}".format("{+1, -1}", os.linesep))
    f.write(os.linesep)
    f.write("@DATA{}".format(os.linesep))
    f.writelines(char_7_li)
