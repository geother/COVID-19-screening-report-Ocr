# -*- coding: utf-8 -*-
import easyocr
import xlwings
import os

reader = easyocr.Reader(['ch_sim', 'en'])


class glb:
    def __init__(self):
        self.tot = 0
        self.cnt = 0
        self.name2id = {}
        self.imgName = os.listdir('img/')
        self.vis = []
        self.tmpCnt = 0


gb = glb()
wb = xlwings.Book('list.xlsx')
sheet = wb.sheets['Sheet1']


def handle(res):
    __check = False
    __name = ''
    __date = '000000000000'
    for x in res:
        if x == '阳性':
            __check = True
        if x in gb.name2id.keys():
            __name = x
        x = ''.join(ch for ch in x if ch.isalnum())
        if len(x) == 12 and x[0] == '2':
            if x > __date:
                __date = x
    if gb.name2id.get(__name, -1) == -1 or __date[0:4] < '2000':
        gb.tmpCnt += 1
        return 'unKnown_' + str(gb.tmpCnt)
    else:
        gb.vis[gb.name2id[__name][1]] = 1 if __check else -1
        sheet.range('C' + str(gb.name2id[__name][1] + 1)).value = str(__date)
        sheet.range('D' + str(gb.name2id[__name][1] + 1)).value = '否' if not __check else '是'
        print("That's good, ", __name)
        return str(gb.name2id[__name][0]) + '_' + __name


def main():

    while sheet.range('A' + str(gb.tot + 2)).value is not None:
        gb.tot += 1
        gb.name2id[sheet.range('B' + str(gb.tot + 1)).value] = (int(sheet.range('A' + str(gb.tot + 1)).value), gb.tot)

    for __img in gb.imgName:
        gb.tmpCnt += 1
        os.rename('img/' + __img, 'img/' + str(gb.tmpCnt) + '.' + __img.split('.')[1])
    gb.imgName = os.listdir('img/')
    gb.vis = [0 for _ in range(gb.tot + 10)]
    gb.tmpCnt = 0

    for __img in gb.imgName:
        res = reader.readtext('img/' + __img, detail=0)
        os.rename('img/' + __img, 'img/' + handle(res) + '.' + __img.split('.')[1])


if __name__ == '__main__':
    main()
