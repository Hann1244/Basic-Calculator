from tkinter import *

def yaz(x):
    s = len(giris.get())
    giris.insert(s, str(x))

hesap = 7
s1 = 0

def işlemler(x):
    global hesap 
    hesap = x
    global s1
    s1 = float(giris.get())
    print(hesap)
    print(s1)
    giris.delete(0, "end")

s2 = 0
def hesapla():
    global s2
    s2 = float(giris.get())
    print(s2)
    global hesap 
    sonuç = 0
    if hesap == 0:
        sonuç = s1 + s2
    elif hesap == 1:
        sonuç = s1 - s2
    elif hesap == 2:
        sonuç = s1 * s2
    elif hesap == 3:
        sonuç = s1 / s2
    giris.delete(0, "end")
    giris.insert(0, str(sonuç))

def sifirla():
    global s1, s2, hesap
    s1 = 0
    s2 = 0
    hesap = 7
    giris.delete(0, "end")

def key_press(event):
    char = event.char
    if char.isdigit():
        yaz(char)
    elif char == '+':
        işlemler(0)
    elif char == '-':
        işlemler(1)
    elif char == '*':
        işlemler(2)
    elif char == '/':
        işlemler(3)
    elif char == '.':
        yaz('.')
    elif char == '\r':
        hesapla()
    elif char == 'c' or char == 'C':
        sifirla()
    elif char == 'q' or char == 'Q':
        pencere.quit()

def close_app():
    pencere.quit()

pencere = Tk()
pencere.title("HESAP MAKİNESİ")        
pencere.geometry("500x500")
giris = Entry(font="Verdana 14 bold", width=20, justify=RIGHT)
giris.place(x=80, y=20)

b = []
for i in range(1, 10):
    b.append(Button(text=str(i), font="Verdana 14 bold", width=4, command=lambda x=i: yaz(x)))
sayac = 0
for i in range(0, 3):
    for j in range(0, 3):
        b[sayac].place(x=80 + j * 70, y=80 + i * 70)    
        sayac += 1

işlem = []
for i in range(0, 4):
    işlem.append(Button(fg="RED", bg="GRAY", font="Verdana 14 bold", width=4, command=lambda x=i: işlemler(x)))
işlem[0]["text"] = "+"   
işlem[1]["text"] = "-" 
işlem[2]["text"] = "*" 
işlem[3]["text"] = "/"
for i in range(0, 4):
    işlem[i].place(x=300, y=80 + 50 * i) 

sifb = Button(text=0, font="Verdana 14 bold", width=4, command=lambda x=0: yaz(x))
sifb.place(x=80, y=280)     
noktb = Button(text=".", font="Verdana 14 bold", width=4, command=lambda x=".": yaz(x))
noktb.place(x=220, y=280)
esittrb = Button(text="=", fg="RED", bg="GRAY", font="Verdana 14 bold", width=4, command=hesapla)
esittrb.place(x=300, y=280)

resetb = Button(text="C", fg="RED", bg="GRAY", font="Verdana 14 bold", width=4, command=sifirla)
resetb.place(x=300, y=340)

exitb = Button(text="Exit", fg="WHITE", bg="RED", font="Verdana 14 bold", width=4, command=close_app)
exitb.place(x=300, y=400)

pencere.bind('<Key>', key_press)

pencere.mainloop()
