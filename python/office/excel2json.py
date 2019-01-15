# -*- coding:utf-8 -*-
# @Goal     : learn how to use xlrd and xlwt to read and write the Excel.
# @Input    : Excel raw file
# @Author   : Eli

import xlrd
import json


def excel2Json(file_path):
    # open excel
    if getData(file_path) is not None:
        book = getData(file_path)
        # how many sheet
        worksheets = book.sheet_names()
        print("sheet list:")
        for sheet in worksheets:
            result = {}
            fin = []
            result['children'] = []
            print('%s,%s' %(worksheets.index(sheet), sheet))
            # for each sheet
            sheet = book.sheet_by_index(worksheets.index(sheet))
            # set the first row as title
            row_title = sheet.row_values(0)
            rowsNum = sheet.nrows
            colsNum = sheet.ncols
            for row in range(rowsNum):
                if row == 0:
                    continue
                temp = {}
                for col in range(colsNum):
                    # Ignore the empty cell
                    if str(row_title[col]) != '':
                        temp[str(row_title[col])] = sheet.row_values(row)[col]
                result["children"].append(temp)
            json_data=json.dumps(result,indent = 4, sort_keys=True)

            print(json_data)


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
