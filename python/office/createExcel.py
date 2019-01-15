# -*- coding:utf-8 -*-
# @File :   createExcel
# @Input:   
# @Author:  https://pypi.org/project/xlwt/

import xlwt
from datetime import datetime

# style
style0 = xlwt.easyxf('font: name Times New Roman, color-index red, bold on', num_format_str='#,##0.00')
style1 = xlwt.easyxf(num_format_str='D-MMM-YY')

# create workbook
workbook = xlwt.Workbook(encoding = 'utf-8')
# create worksheet
worksheet = workbook.add_sheet('My New Worksheet')

# Write
# !!! You can not over write the same place

# worksheet.write(1, 0, label = 'new cell')
worksheet.write(0, 0, 1234.56, style0)
worksheet.write(1, 0, datetime.now(), style1)
worksheet.write(2, 0, 1)
worksheet.write(2, 1, 1)
worksheet.write(2, 2, xlwt.Formula("A3+B3"))

workbook.save('Example2.xls')
