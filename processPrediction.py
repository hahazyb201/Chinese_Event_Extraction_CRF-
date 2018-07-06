# _*_coding:utf-8_*_
with open("./Testfile",'r',encoding='UTF-8') as ft:
	with open("./result",'rb') as fr:
		with open("./prediction",'w',encoding='UTF-8') as p:
			items_test=ft.readlines()
			items_res=fr.readlines()
			for i in range(len(items_test)):
				itt=items_test[i].strip()
				itr=items_res[i].decode('utf-8').strip().split("\t")
				itn=itt+"\t"+itr[-1]+"\n"
				p.write(itn)

