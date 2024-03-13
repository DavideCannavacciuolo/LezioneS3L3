
print ("Benvenuto in questo schema dove puoi scegliere il tipo di perimetro da poter calcolare")

print ("Scegli tra le varie opzioni:\n 1)Quadrato\n 2)Cerchio\n 3)Rettangolo")

x =  int ( input ("Inserisci la tua scelta: "))

if x == 1 :
	lato = float  ( input ("Inserisci il valore del lato: "))
	print ("Il perimetro del quadrato è: ",lato*4)

elif x == 2 :
	raggio = float ( input ("Inserisci il valore del raggio: "))
	print ("La circonferenza del cerchio è: ",2*3.14*raggio)

elif x == 3 : 
	base = float (input ("Inserisci il valore della base: "))
	altezza = float ( input ("Inserisci il valore dell'altezza: "))
	print ("Il perimetro del rettangolo è: ", 2*base + 2*altezza)

else :
	print ("Operazione sbagliata. Controlla di aver digitato correttamente l'opzione che hai scelto.\n Ripeti il comando per avviare l'esercizio")
