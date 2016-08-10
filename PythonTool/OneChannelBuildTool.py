#!/usr/bin/python
# coding=utf-8
import zipfile
import shutil
import os
import sys

def pack(source,dest,channel_id):
    target_channel = channel_id
    # 拼接对应渠道号的apk
    target_apk = dest
    # 拷贝建立新apk
    shutil.copy(source,  target_apk)
    # zip获取新建立的apk文件
    zipped = zipfile.ZipFile(target_apk, 'a', zipfile.ZIP_DEFLATED)
    # 初始化渠道信息
    empty_channel_file = "META-INF/fengbaochannel_{channel}".format(channel = target_channel)
    # 写入渠道信息
    src_empty_file = 'info/czt.txt'
    zipped.write(src_empty_file, empty_channel_file)
    # 关闭zip流
    zipped.close()

def usage():
	print "Usage:"
	print "\tpython OneChannelBuildTool source dest channel_id\n"
	print "\tsource: full path of apk to pack"
	print "\tdest: full path of packed apk file"
	print "\tchannel_id: int or string represent for specifical channel"
	print "\n"

	print "example:"
	print "\tpython OneChannelBuildTool /tmp/a.apk /tmp/b.apk 110\n"

if __name__ == '__main__':
	args = sys.argv
	argc = len(sys.argv)
	if argc < 4:
		usage()
		sys.exit(1)
	print args,argc
	source = args[1]
	dest = args[2]
	channel_id = args[3]

	print source,dest,channel_id
	pack(source,dest,channel_id)