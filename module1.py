def rida_salvestamine(f:str,rida,str):
	"""
	
	"""
	fail.open(f,"a")
	fail.write(rida+"\n")
	fail.close()

def eng_lug(f:str,e:list):
	"""

	"""
	fail=open(f,"r")
	for rida in fail:
		e.append(rida.strip())
	fail.close()
	return e

def rus_lug(a:str,r:list):
	"""

	"""
	fail=open(a,"r")
	for rida in fail:
		r.append(rida.strip())
	fail.close()
	return r