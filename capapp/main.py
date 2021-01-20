from tkinter import *



div = Tk()
div.geometry("1500x800+50+20")
div.resizable(width=False, height=False)
div.title('Text Capitalization ')
div.iconbitmap(r'abc.ico')zz
AB=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
ab=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
noab=[',','.',':',';','(',')']

lis=[]
def maj():
   
    userinp=usertext.get("1.0","end")
    for i in userinp:    
        for j in ab:
            if i ==j :
                indx=ab.index(j)
                for k in AB:
                    li=AB[indx]
                    lis.append(li)
                    break   
        for j in AB:
            if i ==j :
                indx1=AB.index(j)
                for k in AB:
                    li=AB[indx1]
                    lis.append(li)
                    break    
            elif i==' ':
                cap=' '
                lis.append(cap)
                break
            elif i=='\n':
                cap='\n'
                lis.append(cap)
                break
        for u in noab:
            if i ==u :
                indx1=noab.index(u)
                for k in noab:
                    li=noab[indx1]
                    lis.append(li)
                    break
        for l in i :
            try:
                numb = int(i)
                lis.append(numb)
                break
            except ValueError:
                pass
    
    
    ins=''.join(map(str, lis))
    lis.clear()
    return boxen.insert(0.1,ins)
    


def clsncap():
    usertext.delete(1.0,END)
def clscap():
    boxen.delete(1.0,END)
def clsall():
    boxen.delete(1.0,END)
    usertext.delete(1.0,END)

texbox1=Label(div,font=('Arial',20),text="No Capitalization Text :")
texbox1.place(x=250, y=10)
texbox2=Label(div,font=('Arial',20),text="Capitalization Text :")
texbox2.place(x=1000, y=10)

usertext=Text(div,font=('Arial',12),height=35,width=80)
usertext.place(x=20, y=50)

boxen=Text(div,font=('Arial',12),height=35,width=80)
boxen.place(x=760, y=50)

sendtext=Button(div,font=('Arial',16),width=16,padx=20,pady=10,bg='#FFFF00', text="Capitalization",command=maj)
sendtext.place(x=60, y=690)

clsncp=Button(div,font=('Arial',16),width=16,text='Clear No Cap text',padx=20,pady=10,bg='#FFFF00',command=clsncap)
clsncp.place(x=400, y=690)

clscp=Button(div,font=('Arial',16),width=16,text='Clear Cap text',padx=20,pady=10,bg='#FFFF00',command=clscap)
clscp.place(x=800, y=690)

clsall=Button(div,font=('Arial',16),width=16,text='Clear All',padx=20,pady=10,bg='#FFFF00',command=clsall)
clsall.place(x=1200, y=690)

Copyright=Label(div,font=('Arial',20),text="Copyright Hamza Essalhi")
Copyright.place(x=600, y=760)




div.mainloop()
