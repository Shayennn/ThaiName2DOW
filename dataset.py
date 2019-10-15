from os import listdir, path
from datetime import date
import re


def load():
    nameList = []
    dowList = []
    for name in listdir('datasets'):
        f = open(path.join('datasets', name), 'r')
        firstLine = f.readline()
        day, month, year = firstLine[0:2], firstLine[2:4], firstLine[4:8]
        day, month, year = int(day), int(month), int(year)
        f.close()
        dateObj = date(year, month, day)
        name = name.strip()
        nameList.append(name)
        dowList.append(dateObj.weekday())
    nameCharList, dowList = countThai(nameList, dowList)
    return nameCharList, dowList


def countThai(texts, dowList):
    output = []
    newDowList = []
    chars = prepareThaiChars()
    pt = re.compile(r'^[ก-ฮะ-ฺเ-ํ]+$')
    for i, text in enumerate(texts):
        tmpOpt = []
        if pt.search(text) is None:
            continue
        for c in chars:
            tmpOpt.append(text.count(c))
        output.append(tmpOpt)
        newDowList.append(dowList[i])
    return output, newDowList


def prepareThaiChars():
    thaiCharRanges = [('ก', 'ฮ'), ('ะ', 'ฺ'), ('เ', 'ํ')]
    chars = []
    for start, end in thaiCharRanges:
        start = start.encode('tis-620')[0]
        end = end.encode('tis-620')[0]
        for code in range(start, end+1):
            chars.append(bytes([code]).decode('tis-620'))
    return chars
