#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#要转换的文件     相对路径
filepath='./mcu.bin'
#转换后的文件名称 相对路径
fileFillpath='./mcuFill.bin'
#单位是KB 长度
binFillLen=12
#填充字节
fillByte=b'\xff'


binFile=open(filepath,'rb') 
writeBinList=binFile.read()

binFillFile = open(fileFillpath, 'wb')

binFillFile.write(writeBinList) 

addFillLen=(binFillLen*1024-len(writeBinList))
for x in range(addFillLen):
    binFillFile.write(fillByte)

binFillFile.close()

print('------------------填充成功！------------------------')


#binfile.write( chr(255)  * (binLen*1024 - len(binfile)))
