import string
import random

def password():
	lettres = string.ascii_letters
	chiffres = string.digits
	ponc = string.punctuation

	try:
		ulettres = eval(input("lettre (True or False)"))
		uchiffres = eval(input("chiffres (True or False)"))
		uponc = eval(input("punctuation (True or False)"))

		l = int(input("lenght pass: "))

		char = ""
		char += lettres if ulettres else ""
		char += chiffres if uchiffres else ""
		char += ponc if uponc else ""

		passe = "".join(random.choices(char, k=l))
		print(passe)

	except:
		print("pass invalid")
		password()

password()

