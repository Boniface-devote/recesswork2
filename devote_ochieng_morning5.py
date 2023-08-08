from tkinter import *
root = Tk()
root.geometry("600x200")


def reciept():
    top = Toplevel()
    top.geometry("600x200")
    top.config(background='white')
    commodity1="bread"
    pricel = 2500
    qtyl = 2
    total1 = pricel*qtyl

    commodity2="sugar"
    price2 = 4500
    qty2 = 1
    total2 = pricel*qty2

    commodity3="milk"
    price3 = 2700
    qty3 = 2
    total3 = pricel*qty3

    commodity4="butter"
    price4 = 3000
    qty4 = 1
    total4 = pricel*qty4


    l=Label(top,text='------RECEIPT----------')
    l.pack()
    l.config(background='white')
    heading = Label(top,text='ITEM\tPRICE\tQTY\tTOTAL')
    heading.pack()
    heading.config(background='white')

    item1=Label(top,text=f'{commodity1}\t{pricel}\t{qtyl}\t{total1}')
    item1.pack()
    item1.config(background='white')

    item2=Label(top,text=f'{commodity2}\t{price2}\t{qty2}\t{total2}')
    item2.pack()
    item2.config(background='white')

    item3=Label(top,text=f'{commodity3}\t{price3}\t{qty3}\t{total3}')
    item3.pack()
    item3.config(background='white')

    item4=Label(top,text=f'{commodity4}\t{price4}\t{qty4}\t{total4}')
    item4.pack()
    item4.config(background='white')

    t=Label(top,text='------TOTAL FOR GOODS----------')
    t.pack()
    t.config(background='white')
    heading = Label(top,text='NO. of Goods\tTOTAL')
    heading.pack()
    heading.config(background='white')

    total=Label(top,text=f'{4}\t\t{total1+total2+total3+total4}')
    total.pack()
    total.config(background='white')

b= Button(root,text='Print Receipt',command=reciept)
b.pack(padx=10,pady=10)
root.mainloop()
