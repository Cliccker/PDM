#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PyPDF2 import PdfFileReader, PdfFileWriter
import os


def split_pdf(infile, out_path):
    """
    :param infile: 待拆分的pdf文件
    :param out_path: 拆分成单页的pdf文件的存储路径
    :return: 无
    """

    if not os.path.exists(out_path):
        os.makedirs(out_path)
    with open(infile, 'rb') as infile:
    
        reader = PdfFileReader(infile)
        number_of_pages = reader.getNumPages()  #计算此PDF文件中的页数
        
        for i in range(number_of_pages):
            writer = PdfFileWriter()
            writer.addPage(reader.getPage(i))
            out_file_name = out_path + str(i+1)+'.pdf'
            with open(out_file_name, 'wb') as outfile:
                writer.write(outfile)


if __name__ == '__main__':
    in_File = 'pdf123789.pdf' # 这里只放文件名
    """
    . 代表当前所在目录
    .. 代表当前所在目录的父目录
    ./ 代表当前所在目录下的某个文件夹或文件
    ../ 代表当前所在目录的父目录下的某个文件夹或文件 """
    out_Path = './PDF试验/单页的/'  # 这里不改
    split_pdf(in_File, out_Path)