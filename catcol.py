#/user/bin/python
#-*- coding:utf-8 -*-
#author : Fat cat
#description : Tools for show col detail of file

import os
import sys
import argparse

class Change():
    
    '''
    对文本中每行进行处理
    '''
    
    def __inint__(self,row):
        self.row = row

    def changdu(self):
        n_col = len(self)
        list_length = []
        for i in range(n_col):
            list_length.append(str(i+1))
        return list_length

    '''
    统计表头长度
    '''

    def short(self):
        new_list = []
        for i in self:
            m = str(i)
            if len(m) < 20:
                new_list.append(m)
            else:
                m = m[:20] + '...'
                new_list.append(m)
        return new_list

    '''
    限制每行中各个列中文本的长度，如果超过20个字符
    就将20个字符之后的字符改为 ...
    '''

    def colourfile(self):
        for i in self:
            yellow = '\033[1;33m'
            pink = '\033[1;35m'
            blue = '\033[1;34m'
            print (yellow + i[0] + '\t' + pink + i[1] + '\t' + blue + '\t'.join(i[2:]))
            
    '''
    对输出结果施加不同的颜色
    列号为黄色
    表头为粉色
    例子为蓝色
    '''
            
class Document():
    '''
    对文本进行处理
    '''
    def __inint__(self,row):
        self.row = row

    def tryfile(self):
        infile = open(self,'r')
        try:
            test = infile.readline()
        except UnicodeDecodeError:
            infile = open(self,'r',encoding='gbk')
            try:
                test = infile.readline()
            except UnicodeDecodeError:
                print ("error, file isn't code with utf-8 or gbk")
                os.exit(1)
            else:
                pass
        else:
            pass
        return infile,test

    '''
    判断文本是否为utf-8编码的，如果不是则改为gbk
    编码打开，成功打开后，提取第一行作为表头，如
    果两个编码都不是，则报错
    '''
        
    def handle_csv(file):
        infile = Document.tryfile(file)[0]
        title = Document.tryfile(file)[1]
        titles = title.strip().split(',')
        num_list = Change.changdu(titles)
        list_all = [num_list,titles]
        for i in range(3):
            line = infile.readline()
            lines = line.strip().split(',')
            liness = Change.short(lines)
            list_all.append(liness)
            list_all.append(liness)
        newlist = map(list,zip(*list_all)) #变换行列
        Change.colourfile(newlist)
        infile.close()

    '''
    处理csv文件，打开，取前三行作为示例，由于前
    面已经提取过第一行，所以，这次提取的三行是从
    第二行开始的也就是，2-4行。
    '''
 
    def handle_any(file):
        infile = Document.tryfile(file)[0]
        title = Document.tryfile(file)[1]
        titles = title.strip().split('\t')
        num_list = Change.changdu(titles)
        list_all = [num_list,titles]
        for i in range(3):
            line = infile.readline()
            lines = line.strip().split('\t')
            liness = Change.short(lines)
            list_all.append(liness)
        newlist = map(list,zip(*list_all))
        Change.colourfile(newlist)
        infile.close()
        
    '''
    整体跟上面类似，但是本次处理的是未知格式的文件，
    精力有限，默认位置格式的文件都为\t 也就是制表符
    间隔的。
    '''

 
def main():
    parser = argparse.ArgumentParser(description="catcol (Tools for show each col overview\
     of file)",prog="catcol",usage="%(prog)s file (xls,xlsx,csv,vcf) [option]")
    parser.add_argument('-v','--version',action='version',version='%(prog)s 1.0')
    parser.add_argument('filename')
    args = parser.parse_args()
    filename = args.filename
    if filename.endswith('csv'):
        Document.handle_csv(filename)
    else:
        Document.handle_any(filename)

    '''
    定义全部变量，判断输入文件类型
    '''
        
if __name__ == '__main__':
    main()
