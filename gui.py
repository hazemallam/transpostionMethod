from tkinter import *
import numpy
from encryption import *
from decryption import *

class GUI:
   # global l
    encryptin = encrption()
    decryptio = decryption()
    def __init__(self, window):
        self.window = window
        window.geometry('900x450+200+50')
        window.title('Trasposition')
        window.configure(bg='#000000')
        window.overrideredirect(1)

        self.main_label = Label(text='Trasposition: Encryption/Decryption', fg='white', bg = "#000000"
                           , font=("Times New Roman", 30, "bold"))
        self.main_label.pack(pady=30)
        self.plain_label = Label(text='Plain Text  ', fg='white', bg='#000000', font=("Times New Roman", 18, "bold"))
        self.plain_label.place(x=50, y=130)
        self.key_label = Label(text='Key  ', fg='white', bg='#000000', font=("Times New Roman", 18, "bold"))
        self.key_label.place(x=50, y=200)
        self.cipher_label = Label(text='cipher text  ', fg='white', bg='#000000', font=("Times New Roman", 18, "bold"))
        self.cipher_label.place(x=50, y=270)

        self.plain = Entry(window, width=65, fg='black', bd='8', font=("Times New Roman", 15, "bold"))
        self.plain.place(x=200, y=130)
        self.key = Entry(window, width=65, fg='black', bd='8', font=("Times New Roman", 15, "bold"))
        self.key.place(x=200, y=200)
        self.cipher = Entry(window, width=65, fg='black', bd='8', font=("Times New Roman", 15, "bold"))
        self.cipher.place(x=200, y=270)

        self.encryption = Button(text='ENCRYPTION', font=("Times New Roman", 14, "bold"), width=15, height=1, bg='#000000',
                            fg='green', bd=10, activebackground='red', activeforeground='black',command = self. encryption_)
        self.encryption.place(x=300, y=350)

        self.decryption = Button(text='DECRYPTION', font=("Times New Roman", 14, "bold"), width=15, height=1, bg='#000000',
                            fg='red', bd=10, activebackground='green', command =self.decryprion_simple)
        self.decryption.place(x=550, y=350)

        self.close = Button(text='X', font=("Times New Roman", 14, "bold"), width=3, height=1, bg='red', fg='white'
                      , activeforeground='black', command = self.close_)
        self.close.place(x=860, y=0)



    def set_text(self, var, text):
        var.delete(0, END)
        var.insert(0, text)
        return

    def key_handle(self, key):
        l = ""
        k = str(self.key.get())
        k =list(k)
        s = k
        for i in range(len(k)):
            if k[i] != s[i]:
                l += k[i]
            return l

    def encryption_(self):
        x = ""
        l = ""
        k = str(self.key.get())
       # k = list(k)
        #s = k
        #for i in range(len(k)):
         #   if k[i] not in l:
          #      l+= k[i]

        #print(l)

        m = str(self.plain.get())
        mssg = m.replace(" ","")
        #k = str(self.key.get())
        c = self.encryptin.Encryption(mssg, k)  #c = self.encryptin.Encryption(m, k) with spaces
        print(c)
        self.set_text(self.cipher, c)

    def encryption_noNumbers(self):
        m = str(self.plain.get())
        mssg = m.replace(" ", "")
        k = str(self.key.get())
        mssg_noNumber = ''.join(i for i in mssg if not i.isdigit())
        c = self.encryptin.Encryption(mssg_noNumber, k)
        print(c)
        self.set_text(self.cipher, c)


    def decryprion_simple(self):

        p = str(self.plain.get())
        m = str(self.cipher.get())
        k = str(self.key.get())
        p = self.decryptio.Decryption(m, k)
        print(p)
        self.set_text(self.plain, p)

    def decryption_remove_alphapitic(self):
        pri = ""
        p = str(self.plain.get())
        lenn = len(p.replace(" ", ""))      #lenn = len(p)   with spaces
        m = str(self.cipher.get())
        k = str(self.key.get())
        p = self.decryptio.Decryption(m, k)
        for i in range(lenn):
            pri += p[i]
        print(pri)
        self.set_text(self.plain, pri)




    def close_(self):
        self.window.destroy()


window = Tk()
gui = GUI(window)
window.mainloop()

