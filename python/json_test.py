#encoding: utf-8
import sys  
reload(sys)   
sys.setdefaultencoding('utf8')  

import json


class jsonClass:
	def decode(self, json_input):
		print "test"

	def decode_jsonLib(self,json_input):
		try:
			decoded = json.loads(json_input)
			# pretty printing of json-formatted string
			print json.dumps(decoded, sort_keys=True, indent=4)
			print decoded.keys()
		except (ValueError, KeyError, TypeError):
			print "JSON format error"



def ConvertCN(s):  
	return s.encode('gb18030')  

#main函数
if __name__ == '__main__':

	fp=open('jsondata.txt')
	allLines = fp.readlines()
	#print allLines


	fp.close()
	str=""
	for eachLine in allLines:
		eachLine=ConvertCN(eachLine)

		#转换成字符串
		for i in range(0,len(eachLine)):
			if eachLine[i]!= ' ' and eachLine[i]!= '	' and eachLine[i]!='\n': #删除空格和换行符，但是json双引号中的内容空格不能删除
				str+=eachLine[i]
		#print eachLine #支持输出换行符
	json_Instance=jsonClass()
	json_Instance.decode_jsonLib(str)

	#print str