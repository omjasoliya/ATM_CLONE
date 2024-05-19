# This is a clone of ATM machine which made by Tkinter and python
from tkinter import *
from tkinter import messagebox, Entry
import time

# ----------- -----------------------------------------------------------------------------------------------------------
Screen = Tk()
Screen.geometry("1200x700")
Screen.iconbitmap("E:/logo.ico")
Screen.title("ATM_PROJECT")
black_background_img = PhotoImage(file="E:/black_atm.png")
Label(Screen, image=black_background_img).pack()
# Label(Screen, text='').place(x=100, y=500)----------------label for add time
curr_img_100 = PhotoImage(file="E:/100-rs-note.png")
curr_img_500 = PhotoImage(file="E:/500-rs-note.png")
payment_success = PhotoImage(file="E:/pyment_success.png")
id_card = PhotoImage(file="E:/id-card.png")
main_page_avtar = PhotoImage(file="E:/main_page_avtar.png")
admin_page_avtar = PhotoImage(file="E:/admin_page_avtar.png")
card_number_input = StringVar()
pin_entry = StringVar()
money_entry = StringVar()
# deposite_entry = StringVar()
dep_amount = StringVar()
balance = StringVar()
admin_name_input = StringVar()
admin_email_input = StringVar()
admin_password_entry = StringVar()
num = 11
pin_number = str(num).zfill(4)
# global balance
balance = 42000


# ----------------------------------------------------------------------------------------------------------------------
def First_Page():
    def Admin_page():

        def clear_admin_data():
            admin_email_input.delete(0, END)
            admin_name_input.delete(0, END)
            admin_password_entry.delete(0, END)

        def cancel_admin_data():
            bank_logo_adminpage.destroy()
            bank_name_adminpage.destroy()
            admin_avtar.destroy()
            admin_name_input.destroy()
            admin_password_entry.destroy()
            admin_name.destroy()
            admin_email.destroy()
            admin_password.destroy()
            admin_name_input.destroy()
            admin_email_input.destroy()
            clear_button.destroy()
            next_button.destroy()
            cancel_button.destroy()
            First_Page()

        def admin_side_data_validation_page():

            def admin_display_page():
                def admin_home_btn():
                    welcome_admin.destroy()
                    cash_data.destroy()
                    available_500_data.destroy()
                    available_500.destroy()
                    available_100.destroy()
                    available_100_data.destroy()
                    home_admin_btn.destroy()
                    bank_logo_adminpage.destroy()
                    First_Page()

                welcome_admin = Label(Screen, text=" Welcome Administrator", fg='White', bg='#2A2A2A', width=20,
                                      font=('sans-serif', 33))
                welcome_admin.place(x=340, y=125)
                cash_data = Label(Screen, text=" Availabel Monitization Report ", fg='Grey', bg='#2A2A2A', width=23,
                                  font=('sans-serif', 33))
                cash_data.place(x=305, y=190)
                available_500 = Label(Screen, image=curr_img_500, bg='#2A2A2A')
                available_500.place(x=240, y=270)
                available_100 = Label(Screen, image=curr_img_100, bg='#2A2A2A')
                available_100.place(x=240, y=430)
                available_500_data = Label(Screen, text="X     400   =    2,00,000 ₹", fg='Grey', bg='#2A2A2A',
                                           width=18, font=('sans-serif', 33))
                available_500_data.place(x=550, y=300)
                available_100_data = Label(Screen, text="X     1000   =    1,00,000 ₹", fg='Grey', bg='#2A2A2A',
                                           width=20, font=('sans-serif', 33))
                available_100_data.place(x=510, y=460)
                home_admin_btn = Button(Screen, text="HOME", bg='#2A2A2A', fg='#E0AE6A', height=1, width=7, border=0.5,
                                        relief='sunken', font='century', command=admin_home_btn)
                home_admin_btn.place(x=560, y=630)
                bank_name_adminpage.destroy()
                admin_avtar.destroy()
                admin_name_input.destroy()
                admin_password_entry.destroy()
                admin_name.destroy()
                admin_email.destroy()
                admin_password.destroy()
                admin_name_input.destroy()
                admin_email_input.destroy()
                clear_button.destroy()
                next_button.destroy()
                cancel_button.destroy()

            def admin_information_authentication_function():
                name = admin_name_input.get()
                email_address = admin_email_input.get()
                password = admin_password_entry.get()

                if name != '':
                    if email_address != '':
                        if password != '':
                            if name.isalpha():
                                # here code snippet is for check email validity---------------------------------------------
                                email_check_point = False
                                for _ in range(0, len(email_address)):
                                    if '@' in email_address[_]:
                                        if email_address[0] != '.' and email_address[0] != '@':
                                            email_check_point = True
                                # here code snippet is for check passwords strength-----------------------------------------
                                l, u, p, d = 0, 0, 0, 0
                                cap_alphabates = "ABCDEFGHIJKLMANOPQRSTUVWXYZ"
                                small_alphabatates = cap_alphabates.lower()
                                special_char = "@$_"
                                digits = "0123456789"
                                if len(password) >= 8:
                                    for i in password:
                                        if i in small_alphabatates:
                                            l += 1
                                        if i in cap_alphabates:
                                            u += 1
                                        if i in digits:
                                            d += 1
                                        if i in special_char:
                                            p += 1
                                # -------------------------------------------------------------------------------------------

                                if email_check_point:
                                    if l >= 1 and u >= 1 and p >= 1 and d >= 1 and (l + p + d + u) == len(password):
                                        if name == 'om' and email_address == 'omdjasoliya45@gmail.com' and password == 'Om@001122':
                                            admin_display_page()
                                        else:
                                            messagebox.showinfo("OOPS !", "Please Enter Right Infromation",
                                                                parent=Screen)
                                    else:
                                        messagebox.showinfo("OOPS !",
                                                            "Please Enter valied format of password \n it shoud have minimum"
                                                            "8 length \n it shoud have 1 Uppercase \n it shoud have 1 "
                                                            "Lowercase \n it shoud have 1 Special chracter \n it "
                                                            "shoud have 1 Digit ", parent=Screen)

                                else:
                                    messagebox.showinfo("OOPS !", "Please Enter valied email Address",
                                                        parent=Screen)
                            else:
                                messagebox.showinfo("OOPS !", "Please Fill Your name in terms of alphabates",
                                                    parent=Screen)

                        else:
                            messagebox.showinfo("OOPS !", "Please Fill Your Password", parent=Screen)
                    else:
                        messagebox.showinfo("OOPS !", "Please Fill Your Email", parent=Screen)
                else:
                    messagebox.showinfo("OOPS !", "Please Fill Your Name", parent=Screen)

            admin_information_authentication_function()

        avtar_lable.destroy()
        user_Button.destroy()
        admin_Button.destroy()
        bank_name_firstpage.destroy()
        bank_logo_firstpage.destroy()
        bank_logo_adminpage = Label(Screen, text="🏦", fg='GREY', bg='#2A2A2A', width=2, font=('century', 45))
        bank_logo_adminpage.place(x=550, y=-12)
        bank_name_adminpage = Label(Screen, text="THE BHARAT SARTHI", fg='white', bg='#2A2A2A', width=25,
                                    font=('century', 35))
        bank_name_adminpage.place(x=220, y=125)
        admin_avtar = Label(Screen, image=admin_page_avtar, bg='#2A2A2A')
        admin_avtar.place(x=175, y=245)
        admin_name_input = Entry(Screen, width=24, bg='#2A2A2A', fg='grey', font=('Cascadia Code', 25), borderwidth=0,
                                 highlightthickness=2,
                                 insertbackground="white")
        admin_name_input.config(highlightbackground="#5F9EA0", highlightcolor="#5F9EA0")
        admin_name_input.focus()
        admin_name_input.place(x=480, y=255)
        admin_name = Label(Screen, text="Username", fg='#00FFFF', bg='#2A2A2A', width=9, font=('Cascadia Code', 15))
        admin_name.place(x=503, y=237)
        admin_email_input = Entry(Screen, width=24, bg='#2A2A2A', fg='grey', font=('Cascadia Code', 25), borderwidth=0,
                                  highlightthickness=2,
                                  insertbackground="white")
        admin_email_input.config(highlightbackground="#5F9EA0", highlightcolor="#5F9EA0")
        admin_email_input.focus()
        admin_email_input.place(x=480, y=335)
        admin_email = Label(Screen, text="Email", fg='#00FFFF', bg='#2A2A2A', width=6, font=('Cascadia Code', 15))
        admin_email.place(x=503, y=317)
        admin_password_entry = Entry(Screen, width=24, bg='#2A2A2A', fg='grey', font=('Cascadia Code', 25),
                                     borderwidth=0,
                                     highlightthickness=2,
                                     insertbackground="white")
        admin_password_entry.config(highlightbackground="#5F9EA0", highlightcolor="#5F9EA0")
        admin_password_entry.focus()
        admin_password_entry.place(x=480, y=415)
        admin_password = Label(Screen, text="Password", fg='#00FFFF', bg='#2A2A2A', width=9, font=('Cascadia Code', 15))
        admin_password.place(x=503, y=397)
        cancel_button = Button(Screen, text="CANCEL", bg='#2A2A2A', fg='red', height=1, width=8,
                               border=0.5,
                               relief='sunken', font='century', command=cancel_admin_data)
        cancel_button.place(x=480, y=490)
        clear_button = Button(Screen, text="CLEAR", bg='#2A2A2A', fg='grey', height=1, width=8, border=0.5,
                              relief='sunken', font='century', command=clear_admin_data)
        clear_button.place(x=651, y=490)

        next_button = Button(Screen, text="NEXT", bg='#2A2A2A', fg='#E0AE6A', height=1, width=8, border=0.5,
                             relief='sunken', font='century', command=admin_side_data_validation_page)
        next_button.place(x=830, y=490)

    def user_first_page():  #
        def clear():
            card_number_input.delete(0, END)

        def close_user_page():
            bank_name.destroy()
            insert_instruction.destroy()
            card_number_input.destroy()
            cancel_button_withdraw_screen.destroy()
            clear_button.destroy()
            next_button.destroy()
            First_Page()

        def second_screen():
            def second_page_clear():
                pin_entry.delete(0, END)

            def second_page_cancel():
                pin_input.destroy()
                welcome_msg.destroy()
                cancel_button_second_screen.destroy()
                clear_button_second_screen.destroy()
                next_button_second_screen.destroy()
                pin_entry.destroy()
                user_first_page()

            def third_page():
                def withdraw_page():
                    def withdraw_success():
                        def back_withdraw_success():
                            wait_msg.destroy()
                            # balance_data.destroy()
                            home_btn.home_button_withdraw_success_screen.destroy()
                            success_msg.successful_msg.destroy()
                            First_Page()

                        if int(balance) >= int(money_entry.get()):
                            money_amount = money_entry.get()
                            if int(money_amount) > int(25000):
                                messagebox.showinfo("OOPS !", "Please enter amount less than 25,000", parent=Screen)
                            elif int(balance) >= int(money_amount) <= int(25000):
                                if int(money_amount) % 100 == 0:
                                    updated_balance_after_withdraw = balance - int(money_entry.get())
                                    notes_msg.destroy()
                                    currency_image_100.destroy()
                                    currency_image_500.destroy()
                                    withdraw_entry.destroy()
                                    money_entry.destroy()
                                    Caution_msg.destroy()
                                    cancel_button_withdraw_screen.destroy()
                                    next_button_withdraw_screen.destroy()
                                    clear_button_withdraw_screen.destroy()
                                    wait_msg = Label(Screen, text='Please Wait for Transaction.......', fg='#fefefa',
                                                     bg='#2A2A2A', width=26,
                                                     font=('sans-serif', 40))
                                    wait_msg.after(4500, lambda: wait_msg.destroy())
                                    wait_msg.place(x=190, y=280)

                                    # balance_data = Label(Screen, text=updated_balance_after_withdraw, fg='#fefefa',
                                    #                      bg='#2A2A2A', width=26,
                                    #                      font=('sans-serif', 40))
                                    # balance_data.place(x=190, y=480)
                                    def success_msg():
                                        success_msg.successful_msg = Label(Screen, image=payment_success, bg='#2A2A2A')
                                        success_msg.successful_msg.place(x=430, y=220)

                                    Screen.after(4500, success_msg)

                                    def home_btn():
                                        home_btn.home_button_withdraw_success_screen = Button(Screen, text="HOME",
                                                                                              bg='#2A2A2A',
                                                                                              fg='#E0AE6A', height=1,
                                                                                              width=7,
                                                                                              border=0.5,
                                                                                              relief='sunken',
                                                                                              font='century',
                                                                                              command=back_withdraw_success)
                                        home_btn.home_button_withdraw_success_screen.place(x=525, y=630)

                                    Screen.after(4500, home_btn)

                                else:
                                    messagebox.showinfo("OOPS !", "Enter Amount In Multiple of available Monitization",
                                                        parent=Screen)
                        else:
                            messagebox.showinfo("OOPS !", "Your account doesn't have sufficient balance", parent=Screen)

                    def clear_amount():
                        money_entry.delete(0, END)

                    def cancel_withdraw_page():
                        notes_msg.destroy()
                        currency_image_100.destroy()
                        currency_image_500.destroy()
                        withdraw_entry.destroy()
                        money_entry.destroy()
                        Caution_msg.destroy()
                        cancel_button_withdraw_screen.destroy()
                        next_button_withdraw_screen.destroy()
                        clear_button_withdraw_screen.destroy()
                        user_first_page()

                    service_msg.destroy()
                    cancel_button_third_screen.destroy()
                    withdraw_btn.destroy()
                    deposite_btn.destroy()
                    mini_stmt_btn.destroy()
                    check_balance.destroy()
                    notes_msg = Label(Screen, text="Available Monitization", fg='#fefefa', bg='#2A2A2A', width=22,
                                      font=('Dancing Script', 23))
                    notes_msg.place(x=420, y=200)
                    currency_image_100 = Label(Screen, image=curr_img_100, bg='#2A2A2A')
                    currency_image_100.place(x=300, y=250)
                    currency_image_500 = Label(Screen, image=curr_img_500, bg='#2A2A2A')
                    currency_image_500.place(x=650, y=250)
                    withdraw_entry = Label(Screen, text="Please Enter Amount (₹)", fg='Grey', bg='#2A2A2A', width=24,
                                           font=('Dancing Script', 23))
                    withdraw_entry.place(x=400, y=380)
                    money_entry = Entry(Screen, width=6, bg='#2A2A2A', fg='white', font=('century', 27), borderwidth=0,
                                        highlightthickness=0,
                                        insertbackground="grey")
                    money_entry.focus()
                    money_entry.place(x=520, y=445)
                    Caution_msg = Label(Screen, text="NOTE : Enter amount in terms of available Monitization", fg='red',
                                        bg='#2A2A2A', width=52,
                                        font=('Dancing Script', 18))
                    Caution_msg.place(x=250, y=625)
                    cancel_button_withdraw_screen = Button(Screen, text="CANCEL", bg='#2A2A2A', fg='red', height=1,
                                                           width=7,
                                                           border=0.5,
                                                           relief='sunken', font='century',
                                                           command=cancel_withdraw_page)
                    cancel_button_withdraw_screen.place(x=355, y=530)
                    clear_button_withdraw_screen = Button(Screen, text="CLEAR", bg='#2A2A2A', fg='grey', height=1,
                                                          width=7,
                                                          border=0.5,
                                                          relief='sunken', font='century', command=clear_amount)
                    clear_button_withdraw_screen.place(x=540, y=530)
                    next_button_withdraw_screen = Button(Screen, text="NEXT", bg='#2A2A2A', fg='#E0AE6A', height=1,
                                                         width=7,
                                                         border=0.5,
                                                         relief='sunken', font='century', command=withdraw_success)
                    next_button_withdraw_screen.place(x=725, y=530)

                    # if int(balance) <= int(money_entry.get()):
                    #     if int(money_entry.get()) >= int(25000):
                    #         messagebox.showinfo("OOPS !", "Please enter amount less than 25,000", parent=Screen)

                def check_balance():
                    def cancel_check_balance():
                        bank_name_balance.destroy()
                        welcome_msg_balance.destroy()
                        balance_of_user.destroy()
                        id_symbol.destroy()
                        cancel_button_balance_check_screen.destroy()
                        First_Page()

                    service_msg.destroy()
                    cancel_button_third_screen.destroy()
                    withdraw_btn.destroy()
                    deposite_btn.destroy()
                    mini_stmt_btn.destroy()
                    check_balance.destroy()
                    bank_name_balance = Label(Screen, text=" THE GREAT  BHARAT  BANK ", fg='white', bg='#2A2A2A',
                                              width=25,
                                              font=('century', 35))
                    bank_name_balance.place(x=220, y=220)
                    welcome_msg_balance = Label(Screen, text=" Welcome User ! ", fg='Grey', bg='#2A2A2A', width=20,
                                                font=('sans-serif', 33))
                    welcome_msg_balance.place(x=320, y=290)
                    updated_balance = int(22000)
                    balance_of_user = Label(Screen, text="Your account balance is 22000", fg='Grey', bg='#2A2A2A',
                                            width=28,
                                            font=('sans-serif', 33))
                    balance_of_user.place(x=225, y=490)
                    id_symbol = Label(Screen, image=id_card, bg='#2A2A2A')
                    id_symbol.place(x=515, y=335)
                    cancel_button_balance_check_screen = Button(Screen, text="HOME", bg='#2A2A2A', fg='#E0AE6A',
                                                                height=1,
                                                                width=7,
                                                                border=0.5,
                                                                relief='sunken', font='century',
                                                                command=cancel_check_balance)
                    cancel_button_balance_check_screen.place(x=525, y=630)

                def deposite():
                    def cancel_deposite_page():
                        notes_msg_deposite.destroy()
                        currency_image_100_deposite.destroy()
                        currency_image_500_deposite.destroy()
                        deposite_entry_label.destroy()
                        deposite_entry.destroy()
                        Caution_msg_deposite.destroy()
                        cancel_button_deposite_screen.destroy()
                        clear_button_deposite_screen.destroy()
                        next_button_deposite_screen.destroy()
                        First_Page()

                    def deposite_sucess():
                        def back_diposite_success():
                            wait_msg.destroy()
                            # balance_data.destroy()
                            home_btn.home_button_withdraw_success_screen.destroy()
                            success_msg.successful_msg.destroy()
                            First_Page()

                        dep_amount = deposite_entry.get()
                        if int(dep_amount) % int(100) == 0:
                            notes_msg_deposite.destroy()
                            currency_image_100_deposite.destroy()
                            currency_image_500_deposite.destroy()
                            deposite_entry_label.destroy()
                            deposite_entry.destroy()
                            Caution_msg_deposite.destroy()
                            cancel_button_deposite_screen.destroy()
                            clear_button_deposite_screen.destroy()
                            next_button_deposite_screen.destroy()
                            wait_msg = Label(Screen, text='Please Wait for Transaction.......', fg='#fefefa',
                                             bg='#2A2A2A', width=26,
                                             font=('sans-serif', 40))
                            wait_msg.after(4500, lambda: wait_msg.destroy())
                            wait_msg.place(x=190, y=280)

                            # balance_data = Label(Screen, text=updated_balance_after_withdraw, fg='#fefefa',
                            #                      bg='#2A2A2A', width=26,
                            #                      font=('sans-serif', 40))
                            # balance_data.place(x=190, y=480)
                            def success_msg():
                                success_msg.successful_msg = Label(Screen, image=payment_success, bg='#2A2A2A')
                                success_msg.successful_msg.place(x=430, y=220)

                            Screen.after(4500, success_msg)

                            time_label = Label(Screen, font=('calibri', 15, 'bold'),
                                               background='#2A2A2A',
                                               foreground='#E0AE6A')
                            time_label.place(x=525, y=510)
                            string = time.strftime('%H:%M:%S %p')
                            time_label.config(text=string)

                            def home_btn():
                                home_btn.home_button_withdraw_success_screen = Button(Screen, text="HOME",
                                                                                      bg='#2A2A2A',
                                                                                      fg='#E0AE6A', height=1,
                                                                                      width=7,
                                                                                      border=0.5,
                                                                                      relief='sunken',
                                                                                      font='century',
                                                                                      command=back_diposite_success)
                                home_btn.home_button_withdraw_success_screen.place(x=525, y=630)

                            Screen.after(4500, home_btn)
                        else:
                            messagebox.showinfo("OOPS !", "Enter Amount In Multiple of available Monitization",
                                                parent=Screen)

                    service_msg.destroy()
                    cancel_button_third_screen.destroy()
                    withdraw_btn.destroy()
                    deposite_btn.destroy()
                    mini_stmt_btn.destroy()
                    check_balance.destroy()

                    def clear_deposite_amount():
                        deposite_entry.delete(0, END)

                    notes_msg_deposite = Label(Screen, text="Accepted Monitization", fg='#fefefa', bg='#2A2A2A',
                                               width=22,
                                               font=('Dancing Script', 23))
                    notes_msg_deposite.place(x=420, y=200)
                    currency_image_100_deposite = Label(Screen, image=curr_img_100, bg='#2A2A2A')
                    currency_image_100_deposite.place(x=300, y=250)
                    currency_image_500_deposite = Label(Screen, image=curr_img_500, bg='#2A2A2A')
                    currency_image_500_deposite.place(x=650, y=250)
                    deposite_entry_label = Label(Screen, text="Please Enter Amount (₹)", fg='Grey', bg='#2A2A2A',
                                                 width=24,
                                                 font=('Dancing Script', 23))
                    deposite_entry_label.place(x=400, y=380)
                    deposite_entry = Entry(Screen, width=6, bg='#2A2A2A', fg='white', font=('century', 27),
                                           borderwidth=0,
                                           highlightthickness=0,
                                           insertbackground="grey")
                    deposite_entry.get()
                    deposite_entry.focus()
                    deposite_entry.place(x=520, y=445)
                    Caution_msg_deposite = Label(Screen, text="NOTE : Enter amount in terms of accepted Monitization",
                                                 fg='red',
                                                 bg='#2A2A2A', width=52,
                                                 font=('Dancing Script', 18))
                    Caution_msg_deposite.place(x=250, y=625)
                    cancel_button_deposite_screen = Button(Screen, text="CANCEL", bg='#2A2A2A', fg='red', height=1,
                                                           width=7,
                                                           border=0.5,
                                                           relief='sunken', font='century',
                                                           command=cancel_deposite_page)
                    cancel_button_deposite_screen.place(x=355, y=530)
                    clear_button_deposite_screen = Button(Screen, text="CLEAR", bg='#2A2A2A', fg='grey', height=1,
                                                          width=7,
                                                          border=0.5,
                                                          relief='sunken', font='century',
                                                          command=clear_deposite_amount)
                    clear_button_deposite_screen.place(x=540, y=530)
                    next_button_deposite_screen = Button(Screen, text="NEXT", bg='#2A2A2A', fg='#E0AE6A', height=1,
                                                         width=7,
                                                         border=0.5,
                                                         relief='sunken', font='century', command=deposite_sucess)
                    next_button_deposite_screen.place(x=725, y=530)

                def mini_statement():
                    # service_msg.destroy()
                    # cancel_button_third_screen.destroy()
                    # withdraw_btn.destroy()
                    # deposite_btn.destroy()
                    # mini_stmt_btn.destroy()
                    # check_balance.destroy()
                    messagebox.showinfo("mini statements", "Sorry for inconvenience \n PLease try Later..")

                def cancel_Thirdpage():
                    service_msg.destroy()
                    cancel_button_third_screen.destroy()
                    withdraw_btn.destroy()
                    deposite_btn.destroy()
                    mini_stmt_btn.destroy()
                    check_balance.destroy()
                    First_Page()

                if int(pin_entry.get()) == int(pin_number):
                    # print(int(pin_entry.get()))
                    pin_input.destroy()
                    welcome_msg.destroy()
                    cancel_button_second_screen.destroy()
                    clear_button_second_screen.destroy()
                    next_button_second_screen.destroy()
                    pin_entry.destroy()
                    service_msg = Label(Screen, text="Please Choose Service ", fg='white', bg='#2A2A2A', width=20,
                                        font=('Dancing Script', 23))
                    service_msg.place(x=420, y=200)
                    cancel_button_third_screen = Button(Screen, text="CANCEL", bg='#2A2A2A', fg='red', height=1,
                                                        width=10,
                                                        border=1.4, relief='sunken', font='century 18',
                                                        command=cancel_Thirdpage)
                    cancel_button_third_screen.place(x=525, y=625)
                    withdraw_btn = Button(Screen, text="Withdraw", bg='#2A2A2A', fg='#E0AE6A', height=1, width=16,
                                          border=0.5, relief='sunken', font='century 18', command=withdraw_page)
                    withdraw_btn.place(x=220, y=290)
                    check_balance = Button(Screen, text="Balance Inquiry", bg='#2A2A2A', fg='#E0AE6A', height=1,
                                           width=16,
                                           border=0.5, relief='sunken', font='century 18', command=check_balance)
                    check_balance.place(x=220, y=420)
                    mini_stmt_btn = Button(Screen, text="Mini Statement", bg='#2A2A2A', fg='#E0AE6A', height=1,
                                           width=16,
                                           border=0.5, relief='sunken', font='century 18', command=mini_statement)
                    mini_stmt_btn.place(x=720, y=290)
                    deposite_btn = Button(Screen, text="Deposite", bg='#2A2A2A', fg='#E0AE6A', height=1, width=16,
                                          border=0.5, relief='sunken', font='century 18', command=deposite)
                    deposite_btn.place(x=720, y=420)



                else:
                    messagebox.showinfo("OOPS !", "Please enter right PIN number", parent=Screen)

            if int(card_number_input.get()) == 123456789123 and len(card_number_input.get()) == 12:
                bank_name.destroy()
                insert_instruction.destroy()
                card_number_input.destroy()
                cancel_button_withdraw_screen.destroy()
                clear_button.destroy()
                next_button.destroy()
                bank_logo.place(x=550, y=113)
                welcome_msg = Label(Screen, text=" Welcome User ! ", fg='white', bg='#2A2A2A', width=20,
                                    font=('sans-serif', 33))
                welcome_msg.place(x=320, y=200)
                pin_input = Label(Screen, text="ENTER YOUR 4 DIGIT PIN", fg='grey', bg='#2A2A2A', width=25,
                                  font=('sans-serif', 15))
                pin_input.place(x=440, y=290)
                pin_entry = Entry(Screen, width=4, bg='#2A2A2A', fg='white', font=('century', 18), borderwidth=0,
                                  highlightthickness=0,
                                  insertbackground="grey")
                pin_entry.focus()
                pin_entry.place(x=545, y=380)
                cancel_button_second_screen = Button(Screen, text="CANCEL", bg='#2A2A2A', fg='red', height=1, width=7,
                                                     border=0.5,
                                                     relief='sunken', font='century', command=second_page_cancel)
                cancel_button_second_screen.place(x=355, y=480)
                clear_button_second_screen = Button(Screen, text="CLEAR", bg='#2A2A2A', fg='grey', height=1, width=7,
                                                    border=0.5,
                                                    relief='sunken', font='century', command=second_page_clear)
                clear_button_second_screen.place(x=540, y=480)
                next_button_second_screen = Button(Screen, text="NEXT", bg='#2A2A2A', fg='#E0AE6A', height=1, width=7,
                                                   border=0.5,
                                                   relief='sunken', font='century', command=third_page)
                next_button_second_screen.place(x=725, y=480)
            else:
                messagebox.showinfo("OOPS !", "Please enter right card number", parent=Screen)

        bank_logo_firstpage.destroy()
        bank_name_firstpage.destroy()

        avtar_lable.destroy()
        user_Button.destroy()
        admin_Button.destroy()
        bank_logo = Label(Screen, text="🏦", fg='GREY', bg='#2A2A2A', width=2, font=('century', 45))
        bank_logo.place(x=550, y=120)
        bank_name = Label(Screen, text=" THE GREAT  BHARAT  BANK ", fg='white', bg='#2A2A2A', width=25,
                          font=('century', 35))
        bank_name.place(x=220, y=220)
        insert_instruction = Label(Screen, text="Please Insert Your Card Number 🪪", fg='grey', bg='#2A2A2A', width=30,
                                   font=('century', 23))
        insert_instruction.place(x=300, y=310)
        card_number_input = Entry(Screen, width=30, bg='#2A2A2A', fg='white', font=('century', 18), borderwidth=0,
                                  highlightthickness=2,
                                  insertbackground="white")
        card_number_input.config(highlightbackground="#DAC979", highlightcolor="#BEA352")
        card_number_input.pack()
        card_number_input.focus()
        card_number_input.place(x=400, y=410)
        cancel_button_withdraw_screen = Button(Screen, text="CANCEL", bg='#2A2A2A', fg='red', height=1, width=7,
                                               border=0.5,
                                               relief='sunken', font='century', command=close_user_page)
        cancel_button_withdraw_screen.place(x=400, y=490)
        clear_button = Button(Screen, text="CLEAR", bg='#2A2A2A', fg='grey', height=1, width=7, border=0.5,
                              relief='sunken', font='century', command=clear)
        clear_button.place(x=549, y=490)

        next_button = Button(Screen, text="NEXT", bg='#2A2A2A', fg='#E0AE6A', height=1, width=7, border=0.5,
                             relief='sunken', font='century', command=second_screen)
        next_button.place(x=695, y=490)

        # ()

    bank_logo_firstpage = Label(Screen, text="🏦", fg='GREY', bg='#2A2A2A', width=2, font=('century', 45))
    bank_logo_firstpage.place(x=550, y=120)
    bank_name_firstpage = Label(Screen, text=" THE GREAT  BHARAT  BANK ", fg='white', bg='#2A2A2A', width=25,
                                font=('century', 35))
    bank_name_firstpage.place(x=220, y=200)
    avtar_lable = Label(Screen, image=main_page_avtar, bg='#2A2A2A')
    avtar_lable.place(x=275, y=270)
    user_Button = Button(Screen, text="🌐           User               ", bg='#2A2A2A', fg='#E0AE6A', height=1, width=18,
                         border=1.5,
                         relief='sunken', font='century 18', command=user_first_page)
    user_Button.place(x=605, y=340)
    admin_Button = Button(Screen, text="🔑          Admin              ", bg='#2A2A2A', fg='#E0AE6A', height=1, width=18,
                          border=1.5,
                          relief='sunken', font='century 18', command=Admin_page)
    admin_Button.place(x=605, y=428)


First_Page()
# ------------------------------Dont touch this End part--------------------------------------------------------------
Screen.mainloop()
