from Tkinter import *
from math import *

def card_check_digit(card):
	card_even=[]
	card_odd=[]
	card_number = entry.get()
	card_list_var = list(card_number)
	card_list = map(lambda x:int(x),card_list_var)
	#print card_list
	card_to_test = card_list[0:15]
	card_last = card_list[-1]
	card_to_test.reverse()
	card_to_test.insert(0,0)
	map(lambda x,y:card_even.append(int(x)) if y % 2 == 0 else card_odd.append(int(x)),card_to_test, range(len(card_to_test)))
	card_odd_2 = map(lambda x: int(x)*2,card_odd)
	card_over_nine = map(lambda x: x if x < 9 else (x - 9), card_odd_2)
	tot_odd = sum(card_over_nine)
	tot_even = sum(map(lambda x: int(x),card_even))
	final = tot_odd+tot_even
	last_val = 10 - final % 10
	if last_val==card_last:
		res.configure(text = "You card: " + 'True')
	else:	
		res.configure(text = "Ergebnis: " + 'False')    
    
w = Tk()
Label(w, text="Your Expression:").pack()
entry = Entry(w)
entry.bind("<Return>", card_check_digit)
entry.pack()
res = Label(w)
res.pack()
w.mainloop()
