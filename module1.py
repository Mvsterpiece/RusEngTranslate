def failist_lugemine(f:str,l:list):
	"""

	"""
	fail=open(f,"r", encoding="utf-8-sig")
	for rida in fail:
		l.append(rida.strip())
	fail.close()
	return l

def failisse_salvestamine(f:str,l:list):
	fail=open(f,"w")
	for el in l:
		fail.write(el,"\n")
	fail.close()

def rida_salvestamine(f:str,rida:str):
	"""

	"""
	fail=open(f,"a")
	fail.write(rida+"\n")
	fail.close()

def uus_sona(f:str,rida:str)->list:
	"""

	"""
	l=[]
	with open(f,"a",encoding="utf-8-sig") as fail:
		fail.write(rida+"\n")
	l=failist_lugemine(f)
	return l

def tolkimine(l1:list,l2:list):
	sona=input("Mida tõlkida? \n")
	if sona in l1:
		tolk=l2[l1.index(sona)]
		print(sona+"-",tolk)
	elif sona in l2:
		tolk=l1[l2.index(sona)]
		print(sona+"-",tolk)
	else:
		print("Sõna puudub sõnastikus")	

def viga(l1:list,f1:str,l2:list,f2:str):
	sona=input("Word with mistake?")
	if sona not in l1 and sona not in l2:
		print("Sõna puudub")
	else:
		if sona in l1:
			tolk=l2[l1.index(sona)]
			l1.remove(sona)
			l2.remove(tolk)
		elif sona in l2:
			tolk=l1[l2.index(sona)]
			l2.remove(sona)
			l1.remove(tolk)
		l1.append(input("Введите новое слово: "))
		l2.append(input("Write a new word: "))
		failisse_salvestamine(f1,l1)
		failisse_salvestamine(f2,l2)
#def correction(sona:str,l:list):
#	for i in range(len(1)):
#		if l[i]==sona:
#		uus_sona=sona.replace(sona,input("New word: "))
#		l.insert(i,uus_sona)
#		l.remove(sona)
#	return l

def failist(mas:list,file:str):
	fail.open(f,"r", encoding="utf-8-sig")
	for sona in mas:
		f.write(sona+"\n")
	fail.close()

#import os
#from gtts import gTTS
#def heli(text:str,keel:str):
#	obj=gTTS(text=text,lang=keel,slow=False).save("heli.mp3")
#	#os.system("heli.mp3")
import random
def kontroll(l1:list,l2:list):
	result=0
	l3=[]
	l3.extend(l1)
	l3.extend(l2)
	random.shuffle(l3)
	print("Random list ",l3)
	for i in range(len(l1)):
		answer=input(f"Переведи данное слово - '{l3[i]}': ")
		if answer in l1 or answer in l2:
			if l3[i] in l1:
				if l1.index(l3[i])==l2.index(answer):
					result+=1
					print("Правильно!")
					print()
			elif l3[i] in l2:
				if l2.index(l3[i])==l1.index(answer):
					result+=1
					print("Правильно!")
					print()
		else:
			print("Неправильно!")
			print()
	resultPercent=(round(result/len(l1))*100)
	print(f"Ваш результат: {resultPercent}%")
