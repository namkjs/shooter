import csv
from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import ast
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 640
class SystemsForm():
    def __init__(self,window,typeOf):
        self.acc_login = False
        self.sign_up = False
        self.window = window
        self.type = typeOf
        self.cfpassword = ''
        self.window.geometry(f'{SCREEN_WIDTH}x{SCREEN_HEIGHT}')
        self.window.attributes('-topmost',True)
        self.window.title(f'{typeOf}')
        self.window.resizable(False,False)
        img = Image.open(r'img\\background\\1.jpg')
        photo = img.resize((SCREEN_WIDTH,SCREEN_HEIGHT))
        self.bg = ImageTk.PhotoImage(photo)
        self.bg_img = Label(self.window,image= self.bg).place(x = 0,y =0,relwidth=1,relheight=1)
        # Login Frame
        Frame_login = Frame(self.window, bg = '#040405', width=400, height=360)
        Frame_login.place(x = SCREEN_WIDTH//2- 200, y = SCREEN_HEIGHT//2 - 180)
        #Create Login form
        img_logo = (Image.open(r'img\\game_logo.png'))
        resize = img_logo.resize((50,50))
        self.logo_img = ImageTk.PhotoImage(resize)
        self.logo = Label(Frame_login,bg='#040405', image=self.logo_img)
        self.logo.place(x = 120, y = 10)
        self.subtitle = Label(Frame_login,text = 'STEAM', fg= '#fff',bg='#040405', font= ('yu gothic ui',13,'bold'))
        self.subtitle.place(x = 176, y = 26)

        #UserName
        self.user_name = Label(Frame_login,text = 'UserName', fg= '#238636',bg='#040405',font= ('yu gothic ui',12,'bold'))
        self.user_name.place(x = 56,y = 70 )
        self.input_name = Entry(Frame_login,width=30,bg='#040405',relief=FLAT,highlightthickness=0,fg='white',font= ('yu gothic ui',12) )
        self.input_name.place( x = 58, y= 100)
        self.username_line = Canvas(Frame_login, width=274, height=2.0, bg="#bdb9b1", highlightthickness=0)
        self.username_line.place(x=58, y=122)

        #PassWord
        self.password = Label(Frame_login,text = 'PassWord', fg= '#238636',bg='#040405',font= ('yu gothic ui',12,'bold'))
        self.password.place(x = 56,y = 140 )
        self.input_password = Entry(Frame_login,width=30,relief=FLAT,highlightthickness=0,bg='#040405',fg='white',font= ('yu gothic ui',12), show='*' )
        self.input_password.place( x = 58, y= 170)
        self.password_line = Canvas(Frame_login, width=274, height=2.0, bg="#bdb9b1", highlightthickness=0)
        self.password_line.place(x=58, y=192)

        #Conform password
        if self.type == 'Sign up':
            cf_password = Label(Frame_login,text = 'Conform PassWord', fg= '#238636',bg='#040405',font= ('yu gothic ui',12,'bold'))
            cf_password.place(x = 56,y = 210 )
            self.cf_inputPass = Entry(Frame_login,width=30,relief=FLAT,highlightthickness=0,bg='#040405',fg='white',font= ('yu gothic ui',12), show='*' )
            self.cf_inputPass.place( x = 58, y= 240)
            cfpassword_line = Canvas(Frame_login, width=274, height=2.0, bg="#bdb9b1", highlightthickness=0)
            cfpassword_line.place(x=58, y=262)
            sign_label = Label(Frame_login, text='Have account?', font=("yu gothic ui", 10),bg="#040405", fg='white')
            sign_label.place(x=58, y=320)
            sign_up_btn = Button(Frame_login,text = 'Login',command = self.check_account,borderwidth=0,bg= '#040405', fg = '#58a6ff',font = ('yu gothic ui',10),cursor='hand2')
            sign_up_btn.place(x  = 146,y = 318)
            
        #Sign account
        if self.type=='Login':
            forget_btn = Button(Frame_login,text = 'Forgot password?', fg= '#58a6ff',bg='#040405',font= ('yu gothic ui',8),bd=0, cursor='hand2')
            forget_btn.place(x = 58, y = 192+24 )
        
        #Button
        login_btn = Button(Frame_login,text = f'{typeOf}',command=self.check_user, width= 10,bg= '#238636', fg = 'white',font = ('yu gothic ui',12),cursor='hand2')
        if self.type =='Sign up':
            login_btn.place(x = 232, y = 192+100)
        elif self.type =='Login':
            login_btn.place(x = 232, y = 192+14)
    # def change_type(self):
    #     self.type = 'Sign up'
    def check_account(self):
            self.sign_up = True
            self.window.destroy()
    def check_user(self):
        
        if self.input_name.get() =='' or self.input_password.get() =='':
            messagebox.showerror('Error', 'All field are required')
        elif self.type =='Sign up' and len(self.input_password.get()) < 6:
            messagebox.showerror('Error', 'Your password must have at least 6 character')
        elif self.type =='Sign up' and self.input_password.get()!=self.cf_inputPass.get():
            messagebox.showerror('Error','Password is not correct!')
        else:
            if self.type =='Login':
                # mo file de doc
                acc_exit = True
                f = open('account.txt','r')
                d = f.read()
                r = ast.literal_eval(d)
                f.close()
                for name in r.keys():
                    if self.input_name.get() ==name and self.input_password.get() == r[name]:
                        acc_exit = False
                        break
                # else:
                #     messagebox.showerror('Error','Invalid account')
                if acc_exit ==False:
                    self.acc_login = True
                    self.window.destroy()
                else:
                    messagebox.showerror('Error','Invalid account')
            if self.type =='Sign up':
                ok = True
                with open ('account.txt',newline='', mode = 'r+') as f:
                    account = {self.input_name.get():self.input_password.get()}
                    user = f.read()
                    # ep kieu dictionary
                    r = ast.literal_eval(user)
                    # r.update(account)
                    for name in r.keys():
                        if self.input_name.get() == name:
                            ok = False
                            break
                    r.update(account)
                    f.truncate(0)
                    f.close()
                    f = open('account.txt','w')
                    w= f.write(str(r))
                    if ok:
                        self.sign_up = True
                        self.window.destroy()
                    else:
                        messagebox.showerror('Error', 'User has exit. Try again!')
            