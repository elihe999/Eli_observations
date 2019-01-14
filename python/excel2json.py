# -*- coding:utf-8 -*-
# @Goal     : learn how to use xlrd and xlwt to read and write the Excel.
# @Input    : Excel raw file
# @Author   : Eli

import sys
import os
import xlwt
import xlrd

def excel2Json(file_path):
    # open excel
    if getData(file_path) is not None:
        book = getData(file_path)
        # how many sheet
        worksheets = book.sheet_names()
        print("sheet list:")
        for sheet in worksheets:
            print('%s,%s' %(worksheets.index(sheet), sheet))

def getData(file_path):
    try:
        data = xlrd.open_workbook(file_path)
        return data
    except BaseException as e:
        print(e)
        print('Fail to read Excel')
        return None

if __name__ == '__main__':
    file_path = "./example.xlsx"
    excel2Json(file_path)
