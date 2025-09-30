import tkinter as tk
from tkinter import messagebox
import mysql.connector as mc
from tkinter import *

# Connect to the database
con = mc.connect(host="localhost", user="root", password="root", database="12a")
cur = con.cursor()


def reset_password():
    rp = tk.Toplevel()
    rp.title("Reset Password")
    rp.geometry('925x500+300+200')
    rp.configure(bg='white')
    rp.resizable(False, False)

    tk.Label(rp, text="Reset Password", font=('Arbil fatface', 30), bg='white').place(x=300, y=40)

    tk.Label(rp, text="User ID:", font=14, bg='white').place(x=320, y=130)
    user_id_entry = tk.Entry(rp, width=40)
    user_id_entry.place(x=320, y=170)

    tk.Label(rp, text="Mobile Number:", font=14, bg='white').place(x=320, y=202)
    phone_entry = tk.Entry(rp, width=40)
    phone_entry.place(x=320, y=242)

    tk.Label(rp, text="New Password:", font=14, bg='white').place(x=320, y=270)
    new_pw_entry = tk.Entry(rp, show="*", width=40)
    new_pw_entry.place(x=320, y=308)

    def update_password():
        user_id = user_id_entry.get()
        phone = phone_entry.get()
        new_password = new_pw_entry.get()

        q = "SELECT phone FROM login WHERE username = %s"
        cur.execute(q, (user_id,))
        result = cur.fetchone()

        if result and result[0] == phone:
            update_query = "UPDATE login SET pwd = %s WHERE username= %s"
            cur.execute(update_query, (new_password, user_id))
            con.commit()
            messagebox.showinfo("Success", "Password reset successfully!")
            rp.destroy()
        else:
            messagebox.showwarning("Error", "Invalid User ID or Phone Number")

    reset_btn = tk.Button(rp, text="Reset Password", command=update_password)
    reset_btn.place(x=380, y=380)

def signup():
    w = tk.Toplevel()
    w.title("Sign up page")
    w.geometry('925x500+300+200')
    w.configure(bg='white')
    w.resizable(False, False)



    sg = tk.Label(w, text="Sign Up", font=('Arbil fatface', 30), bg='white')
    sg.place(x=350, y=40)

    tk.Label(w, text="User ID:", font=14, bg='white').place(x=320, y=130)
    une = tk.Entry(w, width=40)
    une.place(x=320, y=170)

    tk.Label(w, text="Set Password:", font=14, bg='white').place(x=320, y=202)
    npwe = tk.Entry(w, show="*", width=40)
    npwe.place(x=320, y=242)

    tk.Label(w, text="Confirm Password:", font=14, bg='white').place(x=320, y=270)
    fpwe = tk.Entry(w, show="*", width=40)
    fpwe.place(x=320, y=308)

    tk.Label(w, text="Mobile Number:", font=14, bg='white').place(x=320, y=333)
    fpn = tk.Entry(w, width=40)
    fpn.place(x=320, y=369)

    def store_credentials():
        user_id = une.get()
        password1 = npwe.get()
        password2 = fpwe.get()
        phone = fpn.get()

        if len(phone) != 10 or not phone.isdigit():
            messagebox.showwarning("Error", "Phone number must be exactly 10 digits")
            return

        if password1 != password2:
            messagebox.showwarning("Error", "Passwords do not match")
            return

        if user_id and phone and password1:
            try:
                cur.execute("INSERT INTO login (username, pwd, phone) VALUES (%s, %s, %s)", (user_id, password1, phone))
                con.commit()
                messagebox.showinfo("Success", "Account created successfully!")
                w.destroy()
                pt=0
                q1='insert into scoreboard (username,score) values(%s,%s)'
                v1=(user_id,pt)
                cur.execute(q1,v1)
                con.commit()
            except mc.Error as e:
                messagebox.showerror("Database Error", str(e))
        else:
            messagebox.showwarning("Error", "Please fill all fields")

    button = tk.Button(w, text="Create Account", command=store_credentials)
    button.place(x=370, y=420)

def startgame():
    user_id = entry_user_id.get()
    password = entry_password.get()

    try:
        cur.execute("SELECT username, pwd FROM login WHERE username = %s AND pwd = %s", (user_id, password))
        result = cur.fetchone()

        if result:
            wr=tk.Tk()
            wr.title=("WORDLE")
            wr.geometry('925x500+300+200')
            wr.configure(bg='black')
            tk.Label(wr,text='WORDLE',font=('Arial Black',40),bg='black', fg='white').place(x=500,y=5)
            squery='select* from scoreboard'
            
            cur.execute(squery)
            scoreq=cur.fetchall()
            for qwe in scoreq:
                if user_id==qwe[0]:
                    messagebox.showinfo('previous score', 'your previous score is  '+ str(qwe[1]))
            




                    
            o=open('words.txt','r')
            l=o.read()
            x=l.split()
            print(len(x))
            import random as r
            d=r.randint(0,len(x)-1)
            q=x[d]

            #q='words'
            

            
            game_won = False
            tk.Label(wr,text='1st TRY', font=('Arial Black', 14),bg='black',fg='white').place(x=380,y=150)
            et11=tk.Entry(wr,width=2,font=10)
            et11.place(x=500,y=154)
            et12=tk.Entry(wr,width=2,font=10)
            et12.place(x=550,y=154)
            et13=tk.Entry(wr,width=2,font=10)
            et13.place(x=600,y=154)
            et14=tk.Entry(wr,width=2,font=10)
            et14.place(x=650,y=154)
            et15=tk.Entry(wr,width=2,font=10)
            et15.place(x=700,y=154)

            def move_focus_to_entry2(event):
                if len(et11.get()) == 1:  # Check if one letter is entered
                    et12.focus()  # Move focus to entry2

            def move_focus_to_entry3(event):
                if len(et12.get()) == 1:  # Check if one letter is entered
                    et13.focus()  # Move focus to entry3
            def move_focus_to_entry4(event):
                if len(et13.get()) == 1:  # Check if one letter is entered
                    et14.focus()  # Move focus to entry3
            def move_focus_to_entry5(event):
                if len(et14.get()) == 1:  # Check if one letter is entered
                    et15.focus()  # Move focus to entry3
                    
            et11.bind('<KeyRelease>', move_focus_to_entry2)
            et12.bind('<KeyRelease>', move_focus_to_entry3)
            et13.bind('<KeyRelease>', move_focus_to_entry4)
            et14.bind('<KeyRelease>', move_focus_to_entry5)

            
            def submit1():
                e0 = et11.get()
                e1 = et12.get()
                e2 = et13.get()
                e3 = et14.get()
                e4 = et15.get()
                l = e0 + e1 + e2 + e3 + e4
                d = {e0: et11, e1: et12, e2: et13, e3: et14, e4: et15}
                

                matched_positions = [False] * len(q)
            
                if l == q:

                    et11.config(bg='green')
                    et12.config(bg='green')
                    et13.config(bg='green')
                    et14.config(bg='green')
                    et15.config(bg='green')

                    pts=10000
                    messagebox.showinfo("Congratulations!", "You have won 10000 points!")
                    game_won = True
                    qp1=cur.execute('select * from scoreboard')
                    es=cur.fetchall()
  
                    for i in es:
                        if user_id==i[0]: #to check if username eixists on the score board
                            os=int(i[1])
                            ns=os+pts
                            Qp1='update scoreboard set score=%s where username=%s'
                            t1=(ns,user_id)
                            cur.execute(Qp1,t1)
                            con.commit()


                            
                    
                    
                else:

                    if e0 == q[0]:
                        et11.config(bg='green')
                        matched_positions[0] = True
                    if e1 == q[1]:
                        et12.config(bg='green')
                        matched_positions[1] = True
                    if e2 == q[2]:
                        et13.config(bg='green')
                        matched_positions[2] = True
                    if e3 == q[3]:
                        et14.config(bg='green')
                        matched_positions[3] = True
                    if e4 == q[4]:
                        et15.config(bg='green')
                        matched_positions[4] = True

                    if e0 in q and not matched_positions[q.index(e0)]:
                        et11.config(bg='yellow')
                        matched_positions[q.index(e0)] = True
                    
                    if e1 in q and not matched_positions[q.index(e1)]:
                        et12.config(bg='yellow')
                        matched_positions[q.index(e1)] = True
                    
                    if e2 in q and not matched_positions[q.index(e2)]:
                        et13.config(bg='yellow')
                        matched_positions[q.index(e2)] = True
                    
                    if e3 in q and not matched_positions[q.index(e3)]:
                        et14.config(bg='yellow')
                        matched_positions[q.index(e3)] = True
                    
                    if e4 in q and not matched_positions[q.index(e4)]:
                        et15.config(bg='yellow')
                        matched_positions[q.index(e4)] = True

            
            
                
                        
            button1=tk.Button(wr,text='submit',command=submit1)
            button1.place(x=800,y=154)



            tk.Label(wr,text='2nd TRY', font=('Arial Black', 14),bg='black',fg='white').place(x=380,y=200)
            et21=tk.Entry(wr,width=2,font=10)
            et21.place(x=500,y=204)
            et22=tk.Entry(wr,width=2,font=10)
            et22.place(x=550,y=204)
            et23=tk.Entry(wr,width=2,font=10)
            et23.place(x=600,y=204)
            et24=tk.Entry(wr,width=2,font=10)
            et24.place(x=650,y=204)
            et25=tk.Entry(wr,width=2,font=10)
            et25.place(x=700,y=204)

            def move_focus_to_entry2(event):
                if len(et21.get()) == 1:  
                    et22.focus()  

            def move_focus_to_entry3(event):
                if len(et22.get()) == 1:  
                    et23.focus()  
            def move_focus_to_entry4(event):
                if len(et23.get()) == 1:  
                    et24.focus()  
            def move_focus_to_entry5(event):
                if len(et24.get()) == 1:  
                    et25.focus() 
                
            et21.bind('<KeyRelease>', move_focus_to_entry2)
            et22.bind('<KeyRelease>', move_focus_to_entry3)
            et23.bind('<KeyRelease>', move_focus_to_entry4)
            et24.bind('<KeyRelease>', move_focus_to_entry5)

           
            def submit2():
                e0=et21.get()
                e1=et22.get()
                e2=et23.get()
                e3=et24.get()
                e4=et25.get()
                l=e0+e1+e2+e3+e4
                matched_positions = [False] * len(q)
                if l==q:
                    et21.config(bg='green')
                    et22.config(bg='green')
                    et23.config(bg='green')
                    et24.config(bg='green')
                    et25.config(bg='green')
                   
                    messagebox.showinfo("Congratulations!", "You have won 8000 points!")
                    game_won = True


                    qp2=cur.execute('select * from scoreboard')
                    es=cur.fetchall()
                    pts=8000
  
                    for i in es:
                        if user_id==i[0]: #to check if username eixists on the score board
                            os=int(i[1])
                            ns=os+pts
                            Qp2='update scoreboard set score=%s where username=%s'
                            t2=(ns,user_id)
                            cur.execute(Qp2,t2)
                            con.commit()
                    wr.destroy()
                else:
                    if e0==q[0]:
                        et21.config(bg='green')
                        matched_positions[0] = True
                    if e1==q[1]:
                        et22.config(bg='green')
                        matched_positions[1] = True
                    if e2==q[2]:
                        et23.config(bg='green')
                        matched_positions[2] = True
                    if e3==q[3]:
                        et24.config(bg='green')
                        matched_positions[3] = True
                    if e4==q[4]:
                        et25.config(bg='green')
                        matched_positions[4] = True

                    if e0 in q and not matched_positions[q.index(e0)]:
                        et21.config(bg='yellow')
                        matched_positions[q.index(e0)] = True
                    
                    if e1 in q and not matched_positions[q.index(e1)]:
                        et22.config(bg='yellow')
                        matched_positions[q.index(e1)] = True
                    
                    if e2 in q and not matched_positions[q.index(e2)]:
                        et23.config(bg='yellow')
                        matched_positions[q.index(e2)] = True
                    
                    if e3 in q and not matched_positions[q.index(e3)]:
                        et24.config(bg='yellow')
                        matched_positions[q.index(e3)] = True
                    
                    if e4 in q and not matched_positions[q.index(e4)]:
                        et25.config(bg='yellow')
                        matched_positions[q.index(e4)] = True
                
                    
            button2=tk.Button(wr,text='submit',command=submit2)
            button2.place(x=800,y=204)


            tk.Label(wr,text='3rd TRY', font=('Arial Black', 14),bg='black',fg='white').place(x=380,y=250)
            et31=tk.Entry(wr,width=2,font=10)
            et31.place(x=500,y=254)
            et32=tk.Entry(wr,width=2,font=10)
            et32.place(x=550,y=254)
            et33=tk.Entry(wr,width=2,font=10)
            et33.place(x=600,y=254)
            et34=tk.Entry(wr,width=2,font=10)
            et34.place(x=650,y=254)
            et35=tk.Entry(wr,width=2,font=10)
            et35.place(x=700,y=254)

            def move_focus_to_entry2(event):
                if len(et31.get()) == 1:  # Check if one letter is entered
                    et32.focus()  # Move focus to entry2

            def move_focus_to_entry3(event):
                if len(et32.get()) == 1:  # Check if one letter is entered
                    et33.focus()  # Move focus to entry3
            def move_focus_to_entry4(event):
                if len(et33.get()) == 1:  # Check if one letter is entered
                    et34.focus()  # Move focus to entry3
            def move_focus_to_entry5(event):
                if len(et34.get()) == 1:  # Check if one letter is entered
                    et35.focus()  # Move focus to entry3
                
            et31.bind('<KeyRelease>', move_focus_to_entry2)
            et32.bind('<KeyRelease>', move_focus_to_entry3)
            et33.bind('<KeyRelease>', move_focus_to_entry4)
            et34.bind('<KeyRelease>', move_focus_to_entry5)

            

            def submit3():
                e0 = et31.get()
                e1 = et32.get()
                e2 = et33.get()
                e3 = et34.get()
                e4 = et35.get()
                l = e0 + e1 + e2 + e3 + e4
                d = {e0: et11, e1: et12, e2: et13, e3: et14, e4: et15}
            

                matched_positions = [False] * len(q)
                
                if l == q:

                    et31.config(bg='green')
                    et32.config(bg='green')
                    et33.config(bg='green')
                    et34.config(bg='green')
                    et35.config(bg='green')
                    
                    messagebox.showinfo("Congratulations!", "You have won 5000 points!")
                    game_won = True
                    pts=5000
                    qp3=cur.execute('select * from scoreboard')
                    es=cur.fetchall()
  
                    for i in es:
                        if user_id==i[0]: #to check if username eixists on the score board
                            os=int(i[1])
                            ns=os+pts
                            Qp2='update scoreboard set score=%s where username=%s'
                            t2=(ns,user_id)
                            cur.execute(Qp2,t2)
                            con.commit()
                    wr.destroy()
                else:

                    if e0 == q[0]:
                        et31.config(bg='green')
                        matched_positions[0] = True
                    if e1 == q[1]:
                        et32.config(bg='green')
                        matched_positions[1] = True
                    if e2 == q[2]:
                        et33.config(bg='green')
                        matched_positions[2] = True
                    if e3 == q[3]:
                        et34.config(bg='green')
                        matched_positions[3] = True
                    if e4 == q[4]:
                        et35.config(bg='green')
                        matched_positions[4] = True

                    if e0 in q and not matched_positions[q.index(e0)]:
                        et31.config(bg='yellow')
                        matched_positions[q.index(e0)] = True
                    
                    if e1 in q and not matched_positions[q.index(e1)]:
                        et32.config(bg='yellow')
                        matched_positions[q.index(e1)] = True
                    
                    if e2 in q and not matched_positions[q.index(e2)]:
                        et33.config(bg='yellow')
                        matched_positions[q.index(e2)] = True
                    
                    if e3 in q and not matched_positions[q.index(e3)]:
                        et34.config(bg='yellow')
                        matched_positions[q.index(e3)] = True
                    
                    if e4 in q and not matched_positions[q.index(e4)]:
                        et35.config(bg='yellow')
                        matched_positions[q.index(e4)] = True
            button3=tk.Button(wr,text='submit',command=submit3)
            button3.place(x=800,y=254)


            tk.Label(wr,text='4th TRY', font=('Arial Black', 14),bg='black',fg='white').place(x=380,y=300)
            et41=tk.Entry(wr,width=2,font=10)
            et41.place(x=500,y=304)
            et42=tk.Entry(wr,width=2,font=10)
            et42.place(x=550,y=304)
            et43=tk.Entry(wr,width=2,font=10)
            et43.place(x=600,y=304)
            et44=tk.Entry(wr,width=2,font=10)
            et44.place(x=650,y=304)
            et45=tk.Entry(wr,width=2,font=10)
            et45.place(x=700,y=304)

            def move_focus_to_entry2(event):
                if len(et41.get()) == 1:  # Check if one letter is entered
                    et42.focus()  # Move focus to entry2

            def move_focus_to_entry3(event):
                if len(et42.get()) == 1:  # Check if one letter is entered
                    et43.focus()  # Move focus to entry3
            def move_focus_to_entry4(event):
                if len(et43.get()) == 1:  # Check if one letter is entered
                    et44.focus()  # Move focus to entry3
            def move_focus_to_entry5(event):
                if len(et44.get()) == 1:  # Check if one letter is entered
                    et45.focus()  # Move focus to entry3
                
            et41.bind('<KeyRelease>', move_focus_to_entry2)
            et42.bind('<KeyRelease>', move_focus_to_entry3)
            et43.bind('<KeyRelease>', move_focus_to_entry4)
            et44.bind('<KeyRelease>', move_focus_to_entry5)

            pts=0

            def submit4():
                e0 = et41.get()
                e1 = et42.get()
                e2 = et43.get()
                e3 = et44.get()
                e4 = et45.get()
                l = e0 + e1 + e2 + e3 + e4
                d = {e0: et11, e1: et12, e2: et13, e3: et14, e4: et15}
            

                matched_positions = [False] * len(q)
                
                if l == q:

                    et41.config(bg='green')
                    et42.config(bg='green')
                    et43.config(bg='green')
                    et44.config(bg='green')
                    et45.config(bg='green')

                    messagebox.showinfo("Congratulations!", "You have won 3000 points!")
                    game_won = True
                    pts=3000
                    qp4=cur.execute('select * from scoreboard')
                    es=cur.fetchall()
  
                    for i in es:
                        if user_id==i[0]: #to check if username eixists on the score board
                            os=int(i[1])
                            ns=os+pts
                            Qp4='update scoreboard set score=%s where username=%s'
                            t4=(ns,user_id)
                            cur.execute(Qp4,t4)
                            con.commit()
                    wr.destroy()
                else:

                    if e0 == q[0]:
                        et41.config(bg='green')
                        matched_positions[0] = True
                    if e1 == q[1]:
                        et42.config(bg='green')
                        matched_positions[1] = True
                    if e2 == q[2]:
                        et43.config(bg='green')
                        matched_positions[2] = True
                    if e3 == q[3]:
                        et44.config(bg='green')
                        matched_positions[3] = True
                    if e4 == q[4]:
                        et45.config(bg='green')
                        matched_positions[4] = True

                    if e0 in q and not matched_positions[q.index(e0)]:
                        et41.config(bg='yellow')
                        matched_positions[q.index(e0)] = True
                    
                    if e1 in q and not matched_positions[q.index(e1)]:
                        et42.config(bg='yellow')
                        matched_positions[q.index(e1)] = True
                    
                    if e2 in q and not matched_positions[q.index(e2)]:
                        et43.config(bg='yellow')
                        matched_positions[q.index(e2)] = True
                    
                    if e3 in q and not matched_positions[q.index(e3)]:
                        et44.config(bg='yellow')
                        matched_positions[q.index(e3)] = True
                    
                    if e4 in q and not matched_positions[q.index(e4)]:
                        et45.config(bg='yellow')
                        matched_positions[q.index(e4)] = True
            button4=tk.Button(wr,text='submit',command=submit4)
            button4.place(x=800,y=304)


            game_won = False
            tk.Label(wr,text='5th TRY', font=('Arial Black', 14),bg='black',fg='white').place(x=380,y=350)
            et51=tk.Entry(wr,width=2,font=10)
            et51.place(x=500,y=354)
            et52=tk.Entry(wr,width=2,font=10)
            et52.place(x=550,y=354)
            et53=tk.Entry(wr,width=2,font=10)
            et53.place(x=600,y=354)
            et54=tk.Entry(wr,width=2,font=10)
            et54.place(x=650,y=354)
            et55=tk.Entry(wr,width=2,font=10)
            et55.place(x=700,y=354)

            def move_focus_to_entry2(event):
                if len(et51.get()) == 1:  # Check if one letter is entered
                    et52.focus()  # Move focus to entry2

            def move_focus_to_entry3(event):
                if len(et52.get()) == 1:  # Check if one letter is entered
                    et53.focus()  # Move focus to entry3
            def move_focus_to_entry4(event):
                if len(et53.get()) == 1:  # Check if one letter is entered
                    et54.focus()  # Move focus to entry3
            def move_focus_to_entry5(event):
                if len(et54.get()) == 1:  # Check if one letter is entered
                    et55.focus()  # Move focus to entry3
                    
            et51.bind('<KeyRelease>', move_focus_to_entry2)
            et52.bind('<KeyRelease>', move_focus_to_entry3)
            et53.bind('<KeyRelease>', move_focus_to_entry4)
            et54.bind('<KeyRelease>', move_focus_to_entry5)

            
            def submit5():
                e0 = et51.get()
                e1 = et52.get()
                e2 = et53.get()
                e3 = et54.get()
                e4 = et55.get()
                l = e0 + e1 + e2 + e3 + e4
                d = {e0: et11, e1: et12, e2: et13, e3: et14, e4: et15}
                

                matched_positions = [False] * len(q)
                
                if l == q:

                    et51.config(bg='green')
                    et52.config(bg='green')
                    et53.config(bg='green')
                    et54.config(bg='green')
                    et55.config(bg='green')
                    
                    messagebox.showinfo("Congratulations!", "You have won 1000 points!")
                    game_won = True
  
                    
                    pts=1000
                    qp5=cur.execute('select * from scoreboard')
                    es=cur.fetchall()
  
                    for i in es:
                        if user_id==i[0]: #to check if username eixists on the score board
                            os=int(i[1])
                            ns=os+pts
                            Qp5='update scoreboard set score=%s where username=%s'
                            t5=(ns,user_id)
                            cur.execute(Qp5,t5)
                            con.commit()
                else:
                    messagebox.showinfo("you lost",q)
                    wr.destroy()
                    
                

            button5=tk.Button(wr,text='submit',command=submit5)
            button5.place(x=800,y=354)
            wr.mainloop()

        else:
            messagebox.showwarning("Error", "Invalid credentials")
    except mc.Error as e:
        messagebox.showerror("Database Error", str(e))
        
    o.close()
    

def gamerules():
    
    gr= tk.Toplevel()
    gr.title("GAME RULES")
    gr.geometry('960x500+300+200')
    gr.configure(bg='black')
    gr.resizable(False, False)

    cu='select * from login'
    cur.execute(cu)
    cu1=cur.fetchall()
    ui=entry_user_id.get()
    pi=entry_password.get()
    LL=[]
    for i in cu1:
        tt=(i[0],i[1])
        LL.append(tt)
    nt=(ui,pi)
    if nt in LL:

        tk.Label(gr, text="GAME RULES", font=('Arbil fatface', 30),bg='black',fg='yellow').place(x=370, y=40)
        tk.Label(gr, text="1. Guess a hidden five-letter word in 5 attempts or fewer", font=('Arbil fatface', 14),bg='black',fg='white').place(x=270, y=100)
        tk.Label(gr, text="2. After each guess, the game provides feedback in the form of color-coded \ntiles to help you figure out the correct word.", font=('Arbil fatface', 14),bg='black',fg='white').place(x=170, y=129)
        tk.Label(gr, text='3. Press "submit" to submit your guess.\n Enter words in lower case ONLY', font=('Arbil fatface', 14),bg='black',fg='white').place(x=350, y=190)
        tk.Label(gr, text='4. Green : The letter is correct and in the right position. \n Yellow : The letter is in the word but in the wrong position. \n White : The letter is not in the word at all.', font=('Arbil fatface', 14),bg='black',fg='white').place(x=300, y=240)
        tk.Label(gr, text="1st try:-10000 points, 2nd try:-8000 points, 3rd try:-5000 points, 4th try:-3000 points 5th try:-1000 points",font=18,bg='black',fg='yellow').place(x=30, y=320)
        tk.Label(gr, text="5 letters 5 tries, are you up for the prize!?", font=('Arbil fatface', 20),bg='black',fg='yellow').place(x=280, y=374)
        button=tk.Button(gr,text='ok',command=startgame)
        button.place(x=490,y=420)
        gr.mainloop()
    else:
        messagebox.showinfo('wrong','wrong credentials')
        gr.destroy()


# Main window
window = tk.Tk()
window.title("User Login")
window.geometry('925x500+300+200')
window.configure(bg='white')
window.resizable(False, False)

img=PhotoImage(file='wordle.png')
Label(window,image=img,bg='white').place(x=35,y=155)
frame=Frame(window,width=350,height=350,bg='white')
frame.place(x=480,y=70)

label_user_id = tk.Label(window, text="User ID:", font=20,bg='white')
label_user_id.place(x=580, y=130)
entry_user_id = tk.Entry(window, width=40)
entry_user_id.place(x=580, y=170)

label_password = tk.Label(window, text="Password:", font=14,bg='white')
label_password.place(x=580, y=202)
entry_password = tk.Entry(window, show="*", width=40)
entry_password.place(x=580, y=242)



button_submit = tk.Button(window, text="Submit", command=gamerules)
button_submit.place(x=700, y=295)

button_signup = tk.Button(window, text="Don't have an account? Sign Up", command=signup)
button_signup.place(x=650, y=350)

button_forgot_pw = tk.Button(window, text="Forgot Password?", command=reset_password)
button_forgot_pw.place(x=680, y=400)

window.mainloop()
