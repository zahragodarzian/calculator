import tkinter as tk 
window=tk.Tk()
window.geometry("300x450")
window.resizable(False,False)
window.title("calculator")

def click(number):
    display.insert(tk.END,number)


def op_click(op):
    display.insert(tk.END,op)

def eqal():
    e=display.get()
    result=eval(e)
    display.delete(0,tk.END)
    display.insert(tk.END,result)
    print(result)


def delet():
    display.delete(0,tk.END) 


display=tk.Entry(window,border=15,font=("Arial Black",10),justify="right")
button1=tk.Button(window,text="1",font=("Arial Black",10),command=lambda x=1 :click(x))
button2=tk.Button(window,text="2",font=("Arial Black",10),command=lambda x=2 :click(x))
button3=tk.Button(window,text="3",font=("Arial Black",10),command=lambda x=3 :click(x))
button4=tk.Button(window,text="4",font=("Arial Black",10),command=lambda x=4 :click(x))
button5=tk.Button(window,text="5",font=("Arial Black",10),command=lambda x=5 :click(x))
button6=tk.Button(window,text="6",font=("Arial Black",10),command=lambda x=6 :click(x))
button7=tk.Button(window,text="7",font=("Arial Black",10),command=lambda x=7 :click(x))
button8=tk.Button(window,text="8",font=("Arial Black",10),command=lambda x=8 :click(x))
button9=tk.Button(window,text="9",font=("Arial Black",10),command=lambda x=9 :click(x))
button0=tk.Button(window,text="0",font=("Arial Black",10),command=lambda x=0 :click(x))
buttonsum=tk.Button(window,text="+",font=("Arial Black",10),command=lambda o="+" :op_click(o))
buttonsub=tk.Button(window,text="-",font=("Arial Black",10),command=lambda o="-" :op_click(o))
buttonmul=tk.Button(window,text="*",font=("Arial Black",10),command=lambda o="*" :op_click(o))
buttonDIV=tk.Button(window,text="/",font=("Arial Black",10),command=lambda o="+" :op_click(o))
buttoneqal=tk.Button(window,text="=",font=("Arial Black",10),command=eqal)
buttonc=tk.Button(window,text="c",font=("Arial Black",10),command=delet)



display.grid(row=0,column=0,columnspan=4,sticky="news")
button7.grid(row=1,column=0,sticky="news")
button8.grid(row=1,column=1,sticky="news")
button9.grid(row=1,column=2,sticky="news")
buttonsum.grid(row=1,column=3,sticky="news")

button4.grid(row=2,column=0,sticky="news")
button5.grid(row=2,column=1,sticky="news")
button6.grid(row=2,column=2,sticky="news")
buttonsub.grid(row=2,column=3,sticky="news")
button1.grid(row=3,column=0,sticky="news")
button2.grid(row=3,column=1,sticky="news")
button3.grid(row=3,column=2,sticky="news")
buttonmul.grid(row=3,column=3,sticky="news")
buttonc.grid(row=4,column=0,sticky="news")
button0.grid(row=4,column=1,sticky="news")
buttoneqal.grid(row=4,column=2,sticky="news")
buttonDIV.grid(row=4,column=3,sticky="news")






for x in range(0,5):
    for i in range(0,4):
        window.rowconfigure(x,weight=1)
        window.columnconfigure(i,weight=1)






window.mainloop()
