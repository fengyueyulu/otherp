import xlrd
import xml.dom.minidom as md

x=xlrd.open_workbook('../text/student.xls')
sheet=x.sheet_by_index(0)
connect={}
# print(sheet.row_values(0))
for i in range(sheet.nrows):
    connect[i + 1] = sheet.row_values(i)[1:]
print(connect)
def write_to_xml(xlscontent):
    xmfile=md.Document()
    root=xmfile.createElement("root")
    student=xmfile.createElement("student")
    xmfile.appendChild(root)
    root.appendChild(student)

    comment=xmfile.createComment('学生信息表 "id" : [名字, 数学, 语文, 英文]')
    student.appendChild(comment)

    xmlconnect=xmfile.createTextNode(str(xlscontent))
    student.appendChild(xmlconnect)

    with open('../text/students.xml', 'wb') as f:
        f.write(xmfile.toprettyxml(encoding='utf-8'))

write_to_xml(connect)