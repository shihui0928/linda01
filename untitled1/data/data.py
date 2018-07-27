import xlrd
import MySQLdb
# #打开excel表格，参数是文件路径
# data=xlrd.open_workbook('test.xlsx')
#
# #table=data.sheets()[0]
# #table=data.sheet_by_index(0)
#
# table=data.sheet_by_name(u'Sheet1')
#
# nrows=table.nrows
# nrows=table.ncols
#
# print(table.row_values(0))
# print(table.col_values(0))

# class ExcelUtil():
#     def __init__(self,excelPath,sheetName):
#         self.data=xlrd.open_workbook(excelPath)
#         self.table=self.data.sheet_by_name(sheetName)
#         self.keys=self.table.row_values(0)
#         self.rowNum=self.table.nrows #总行数
#         self.colNum=self.table.ncols #总列数
#     def dict_data(self):
#         if self.rowNum<=1:
#             print("总行数小于1")
#         else:
#             r=[]
#             j=1
#             for i in range(self.rowNum-1):
#                 s={}
#                 values=self.table.row_values(j)
#                 for x in range(self.colNum):
#                     s[self.keys[x]]=values[x]
#                 r.append(s)
#                 j+=1
#             return r
# if __name__=="__main__":
#     filepath="test.xlsx"
#     sheetName="Sheet1"
#     data=ExcelUtil(filepath,sheetName)
#     print(data.dict_data())

