from module1 import*
rus_list=[]
eng_list=[]
rus_list=failist_lugemine("rus.txt",rus_list)
eng_list=failist_lugemine("eng.txt",eng_list)

while True:
	menu=input("Rääkida -R, \nKõik sõnad -S, \nTõlkida -T, \nUus sõna -U, \nViga -V, \nKontroll -K, \nLõpp -L \n")
	if menu.upper()=="U":
		rus=uus_sona("rus.txt", input("Новое слово: "))
		eng=uus_sona("eng.txt", input("New word: "))
	elif menu.upper()=="S":
		print(rus_list)
		print(eng_list)
	elif menu.upper()=="T":
		tolkimine(eng_list,rus_list)
	elif menu.upper()=="L":
		print("Хорошо, тикаем")
		break
	elif menu.upper()=="K":
		kontroll(eng_list,rus_list)
	#elif menu.upper()=="R":
	#keel=input("Mis keels ütelda?")
	#	sonad=""
	#	if keel=="ru":
	#		mas=rus_list
	#		lang="ru"
	#	else:
	#		mas=eng_list
	#		lang="eng"
	#	for sona in mas:
	#		sonad=sonad+" "+sona
	#	heli(sonad,lang)
	#else:
		break