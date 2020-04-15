# The DUDE, QTECH, UTM = ":"
# BDCOM = "." 
# D-Link = "-"

# Переменная run созданная для работы цикла, после выполения условия и заключающей операции 
# значение переменной меняется на False что останавливает цикл 
import pyperclip
run = True


while run :
	addres = pyperclip.paste() #input('Введите mac-address: ')
		
	if len(addres) == 14 or len(addres) == 17 :

		if '-' in addres :

			if input('Выберите формат:\n 1.BDCOM \n 2.The DUDE, QTECH, UTM\n --->') is '1' :
				
				# Dlink to BDCOM MAC-ADDRESS created
				addres = addres.replace("-", "", 1)
				addres = addres.replace("-", ".", 1)
				addres = addres.replace("-", "", 1)
				addres = addres.replace("-", ".", 1)
				addres = addres.replace("-", "", 1)
				
				pyperclip.copy(addres)
				print(addres)
				
				run = False
			else :
				# D-Link to The DUDE, QTECH, UTM created
				addres = addres.replace("-", ":")
				
				pyperclip.copy(addres)
				print(addres)
				
				run = False

		elif ':' in addres :
			if input('Выберите формат:\n 1.BDCOM \n 2.D-Link\n --->') is '1' :

				# Dlink to BDCOM MAC-ADDRESS created
				addres = addres.replace(":", "", 1)
				addres = addres.replace(":", ".", 1)
				addres = addres.replace(":", "", 1)
				addres = addres.replace(":", ".", 1)
				addres = addres.replace(":", "", 1)

				pyperclip.copy(addres)
				print(addres)
				
				run = False

			else :
				# The DUDE, QTECH, UTM to D-Link created
				addres = addres.replace(":", "-")
				
				pyperclip.copy(addres)
				print(addres)
				
				run = False

		elif '.' in addres :
			if input('Выберите формат:\n 1.The DUDE, QTECH, UTM \n 2.D-Link\n --->') is '1' :
				# Следующие оперции разделят удалят из строки точку и разобьют строку на 6 частей
				# и затем будут собраны с двоеточиями после каждых двух символом кроме последней пары

				# BDCOM to The DUDE, QTECH, UTM created	
				addres = addres.replace(".", "")
				a = addres[0:2]
				b = addres[2:4]
				c = addres[4:6]
				d = addres[6:8]
				e = addres[8:10]
				f = addres[10:12]
				

				addres = a + ":" + b + ":" + c + ":" + d + ":" + e + ":" + f
				pyperclip.copy(addres)
				print(addres)
				run = False

			else :
				
				#BDCOM to D-Link created 
				addres = addres.replace(".", "")
				a = addres[0:2]
				b = addres[2:4]
				c = addres[4:6]
				d = addres[6:8]
				e = addres[8:10]
				f = addres[10:12]

				addres = a + "-" + b + "-" + c + "-" + d + "-" + e + "-" + f

				pyperclip.copy(addres)
				print(addres)

				run = False



	else :
		print("Incorrect mac-address")
		run = False