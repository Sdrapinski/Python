import tkinter as tk

def wlaczenie_okna():
    root = tk.Tk()
    
    root.geometry('500x460')
    root.title('Kalkulator')
    return root

def Ekran(root):
    ekran = [tk.Label(root,bg='#C0CBCB' ,width=70, anchor= 'w') for i in range(3)]
    for i in range(len(ekran)):
        ekran[i].grid(row = i , columnspan = 6 , ipady = 15, ipadx = 1)
        
    return ekran
    
def PoleNaDane(root,ekran):
    Pole = tk.Entry(root,highlightcolor = 'white' )
    Pole.grid(row = len(ekran),columnspan = 6,ipadx = 187,ipady=8)
    
    info = tk.Label(root,bg='white' ,width=70, anchor= 'w',borderwidth =2)
    info.grid(row=len(ekran)+1,columnspan=6,ipady = 15,ipadx =1 )
    
    return Pole,info

symbole = ['7','8','9','/','\u21BA','C','4','5','6','*','(',')','1','2','3','-','x^2','\u221A','0',',','%','+']

def onclick(Pole,symbol):
    def f():
        if symbol == '\u21BA':
            Bufor = Pole.get()[:-1]
            Pole.delete(0,tk.END)
            Pole.insert(0,Bufor)
        elif symbol =='C':
            Pole.delete(0,tk.END)
        else:
            text = symbol if symbol != 'x^2' else '^2'
            Pole.insert(tk.END,text)
        
    return f    
def oblicz(Pole,ekran,info):
    def czypoprawne(text):
        i =1
        
        while text[-1]==')':
            i+=1
        return text[-1].isdigit()
    def potegowanie(text):
        for i in range(len(text)):
            if text[i]=='^':
                text = text[:i]+'**' + text[i+1:]
        return text
    
    
    
    def f():
        text = Pole.get()
        
        if not czypoprawne(text):
            info['text'] = 'Bledne wyrazenie'
        else:
             for i in range(1,len(ekran)):
                 if ekran[i]['text']:
                     ekran [i-1]['text']=ekran[i]['text']
             if '^' in text: 
                 wyrazenie = potegowanie(text)
                 ekran [-1]['text'] = text + '=' + str(eval(wyrazenie))
             else: 
                 ekran [-1]['text'] = text + '=' + str(eval(text))
       
    return f

def przyciski(root,ekran,info):
    przycisk = [tk.Button(root,text=symbol) for symbol in symbole]
    
    j=len(ekran)+2
    for i in range(len(przycisk)):
         if i % 6 ==0:
             j+=1
         margin = 21 if len(symbole[i]) == 1 else 10
         przycisk[i].grid(row = j , column = i % 6 , ipady = 5, ipadx = margin+10)
         przycisk[i].configure(command = onclick(Pole,przycisk[i]['text']))
         
    znak_rowno = tk.Button(root,text='=',bg='#3256a8',borderwidth = 0,command =oblicz(Pole,ekran,info ))
    znak_rowno.grid(row = len(ekran)+6,column = 4,columnspan=2 , ipady=5,ipadx=margin+50)
    return przycisk
    


############                  
root = wlaczenie_okna()

ekran = Ekran(root)

Pole,info = PoleNaDane(root,ekran)

przycisk = przyciski(root,ekran,info)
root.mainloop()


