from tkinter import *
import time
import database

y_align = 230
ex_al = 150
prod_count = 0
row = 200
col = 100


def number_check(x):
    print(x)


off = []
bud_num = 0

shopping_list = []


class FundManagerWindow:
    def __init__(self, window, page1, page2, page3, page4, page5, login_page, name1_inp, name2_inp, id_inp, phone_inp,
                 email_inp, pin_inp, pin_check, bud_name_inp, cost_inp, freq_inp1, freq_inp2, freq_inp3, freq_inp4,
                 bud_num_del, var, login_phone, login_pin, bud_num_settle, bud_set_amount, goods_box, save,
                 confirm_list_canvas):
        self.window = window
        self.page1 = page1
        self.page2 = page2
        self.page3 = page3
        self.page4 = page4
        self.page5 = page5
        self.name1_inp = name1_inp
        self.name2_inp = name2_inp
        self.id_inp = id_inp
        self.phone_inp = phone_inp
        self.email_inp = email_inp
        self.pin_inp = pin_inp
        self.pin_check = pin_check
        # for creating and deleting budgets budgets
        self.bud_name_inp = bud_name_inp
        self.cost_inp = cost_inp
        self.freq_inp1 = freq_inp1
        self.freq_inp2 = freq_inp2
        self.freq_inp3 = freq_inp3
        self.freq_inp4 = freq_inp4
        self.bud_num_del = bud_num_del
        self.var = var
        # for login page
        self.login_phone = login_phone
        self.login_pin = login_pin
        # to settle bill
        self.bud_num_settle = bud_num_settle
        self.bud_set_amount = bud_set_amount
        # shopping list
        self.goods_box = goods_box
        self.confirm_list_canvas = confirm_list_canvas
        # goods save button
        self.save = save

        self.login_page = login_page
        self.page1 = Canvas(self.window, height=600, bg="#004F6E", highlightthickness=0)
        self.page2 = Canvas(self.window, height=600, bg="#004F6E", highlightthickness=0)
        self.page3 = Canvas(self.window, height=600, bg="#004F6E", highlightthickness=0)
        self.page4 = Canvas(self.window, height=600, bg="#004F6E", highlightthickness=0)
        self.page5 = Canvas(self.window, height=600, bg="#004F6E", highlightthickness=0)
        self.login_page = Canvas(self.window, height=600, bg="#004F6E", highlightthickness=0)

        window.title("FUND MANAGER")
        window.resizable(width=False, height=False)
        window.geometry('800x600')
        self.index = Canvas(window, height=600, bg="#004F6E", highlightthickness=0)
        self.index.pack(fill=BOTH, expand=YES)

        self.create_acc = Button(self.index, text="CREATE ACCOUNT", font="forte", bg="#0096c7",
                                 command=self.createAccPage)
        self.create_acc.place(bordermode=INSIDE, height=50.0, width=500.0, x=180.0, y=200.0)

        self.login_acc = Button(self.index, text="LOG IN", font="forte", bg="#0096c7", command=self.loginPage)
        self.login_acc.place(bordermode=INSIDE, height=50.0, width=500.0, x=180.0, y=250.0)

        self.title = Label(self.index, text="PAW TECHNOLOGIES", font=("chiller", 48), bg="#004F6E", fg="#fcc203")
        self.title.place(bordermode=INSIDE, height=70, width=800, x=0, y=40)
        self.title2 = Label(self.index, text="PAW TECHNOLOGIES-2021 \nAll terms and conditions apply",
                            font=("Bradley Hand ITC", 16), bg="#004F6E", fg="#fcc203")
        self.title2.place(bordermode=INSIDE, height=50, width=800, x=0, y=400)

    def index_to_create_acc(self):
        self.index.pack_forget()
        self.page1.pack(fill=BOTH, expand=YES)
        # self.createAccPage()

    def create_acc_page_to_index(self):
        self.page1.pack_forget()
        self.index.pack(fill=BOTH, expand=YES)

    def index_to_login(self):
        self.index.pack_forget()
        self.login_page.pack(fill=BOTH, expand=YES)

    def login_to_index(self):
        self.login_page.pack_forget()
        self.index.pack(fill=BOTH, expand=YES)

    def createAccPage(self):
        self.index_to_create_acc()
        # self.index.destroy()
        # self.page1.pack(fill=BOTH, expand=YES)
        back_button = Button(self.page1, text="<GO BACK", font="forte", bg="#004F6E", relief=FLAT,
                             command=self.create_acc_page_to_index)
        back_button.place(bordermode=INSIDE, width=150, height=50, x=5, y=30)
        name1_label = Label(self.page1, text="First Name", font="InkFree", bg="#00A6E7", width=20, height=2)
        name1_label.place(bordermode=INSIDE, height=50.0, width=300.0, x=100.0, y=190.0)
        name2_label = Label(self.page1, text="SECOND NAME", font="InkFree", bg="#004F6E", width=20, height=2)
        name2_label.place(bordermode=INSIDE, height=50.0, width=300.0, x=100.0, y=240.0)
        id_num = Label(self.page1, text="NATIONAL ID", font="InkFree", bg="#00A6E7", width=20, height=2)
        id_num.place(bordermode=INSIDE, height=50.0, width=300.0, x=100.0, y=290.0)
        phone = Label(self.page1, text="PHONE NUMBER", font="InkFree", bg="#004F6E", width=20, height=2)
        phone.place(bordermode=INSIDE, height=50.0, width=300.0, x=100.0, y=340.0)
        email = Label(self.page1, text="EMAIL", font="InkFree", bg="#00A6E7", width=20, height=2)
        email.place(bordermode=INSIDE, height=50.0, width=300.0, x=100.0, y=390.0)
        pin = Label(self.page1, text="4-DIGIT PIN", font="InkFree", bg="#004F6E", width=20, height=2)
        pin.place(bordermode=INSIDE, height=50.0, width=300.0, x=100.0, y=440.0)
        pin_pin = Label(self.page1, text="CONFIRM PIN", font="InkFree", bg="#00A6E7", width=20, height=2)
        pin_pin.place(bordermode=INSIDE, height=50.0, width=300.0, x=100.0, y=490.0)

        label = Label(self.page1, text="CREATE ACCOUNT", font=("Martina", 18), bg="#3ca689", fg="white")
        label.place(bordermode=INSIDE, height=50.0, width=300.0, x=250.0, y=90.0)
        log = Button(self.page1, text="or LOGIN", font=("Martina", 14), bg="#3ca689", fg="white",
                     command=self.createAccPageTo_login)
        # button here
        log.place(bordermode=INSIDE, height=30.0, width=250.0, x=260.0, y=150.0)
        self.name1_inp = Entry(self.page1, font=("InkFree", 16))
        self.name1_inp.place(bordermode=INSIDE, height=50.0, width=300.0, x=400.0, y=190.0)

        self.name2_inp = Entry(self.page1, font=("InkFree", 16), bg="#94bdff")
        self.name2_inp.place(bordermode=INSIDE, height=50.0, width=300.0, x=400.0, y=240.0)

        self.id_inp = Entry(self.page1, font=("InkFree", 16))
        self.id_inp.place(bordermode=INSIDE, height=50.0, width=300.0, x=400.0, y=290.0)

        self.phone_inp = Entry(self.page1, font=("InkFree", 16), bg="#94bdff")
        self.phone_inp.place(bordermode=INSIDE, height=50.0, width=300.0, x=400.0, y=340.0)

        self.email_inp = Entry(self.page1, font=("InkFree", 16))
        self.email_inp.place(bordermode=INSIDE, height=50.0, width=300.0, x=400.0, y=390.0)

        self.pin_inp = Entry(self.page1, font=("InkFree", 16), bg="#94bdff")
        self.pin_inp.place(bordermode=INSIDE, height=50.0, width=300.0, x=400.0, y=440.0)

        self.pin_check = Entry(self.page1, font=("InkFree", 16))
        self.pin_check.place(bordermode=INSIDE, height=50.0, width=300.0, x=400.0, y=490.0)

        submit = Button(self.page1, text="REGISTER", font="Forte", bg="#3ca689", width=20, height=1,
                        command=self.create)
        submit.place(bordermode=INSIDE, height=40.0, width=300.0, x=250.0, y=550.0)

    def createAccPageTo_login(self):
        self.page1.pack_forget()
        self.login_page.pack(fill=BOTH)

    def create(self):  # save account creation details
        identity = self.name1_inp.get()
        identity2 = self.name2_inp.get()
        id_no = self.id_inp.get()
        phone = self.phone_inp.get()
        e_mail = self.email_inp.get()
        pin = self.pin_inp.get()
        pin2 = self.pin_check.get()
        if int(pin2) == int(pin):
            # account = [identity, identity2, id_no, phone, email, pin]
            successful = Message(self.page1, text=("dear", identity, ", account creation successful"), font="forte",
                                 bg="#3ca689", fg="orange")
            successful.pack(expand=YES)
            database.create_account(identity, identity2, id_no, phone, e_mail, pin)
            time.sleep(3)
            self.homePage()
        else:
            successful = Message(self.page1, text="PLEASE ENTER PIN IN DIGIT FORMAT", font="forte",
                                 bg="#3ca689", fg="orange")
            successful.pack(expand=YES)

    def loginPage(self):  # page to log in for existing accounts
        # self.index.forget()
        # self.login_page.pack(fill=BOTH, expand=YES)
        self.index_to_login()
        self.createAccPageTo_login()
        back_button = Button(self.login_page, text="<GO BACK", font="forte", bg="#004F6E", relief=FLAT,
                             command=self.login_to_index)
        back_button.place(bordermode=INSIDE, width=150, height=50, x=5, y=30)
        title_label = Label(self.login_page, text="FUNDS ASSISTANT", font=("constantia", 24), bg="#004F6E", fg="gold")
        title_label.place(bordermode=INSIDE, width=400, height=70, x=200, y=100)
        name_label = Label(self.login_page, text="ENTER PHONE NUMBER", font="forte", bg="#3ca689", fg="white")
        name_label.place(bordermode=INSIDE, width=200, height=40, x=200, y=250)
        pin_label = Label(self.login_page, text="ENTER YOUR PIN", font="forte", bg="#3ca689", fg="white")
        pin_label.place(bordermode=INSIDE, width=200, height=40, x=200, y=300)

        self.login_phone = Entry(self.login_page, font="Constantia")
        self.login_phone.place(bordermode=INSIDE, width=200, height=40, x=400, y=250)
        self.login_pin = Entry(self.login_page, font="constantia")
        self.login_pin.place(bordermode=INSIDE, width=200, height=40, x=400, y=300)

        login_button = Button(self.login_page, text="LOGIN", font="forte", bg="#3ca689", fg="white",
                              command=self.existingLogin)
        login_button.place(bordermode=INSIDE, width=200, height=40, x=300, y=350)

    def existingLogin(self):  # check login details
        # counter = 3
        existing_phone = self.login_phone.get()
        existing_pin = self.login_pin.get()
        x = database.loggingInCheck(existing_phone)
        for v in x:
            if int(v) == int(existing_pin):
                self.homePage()
                self.login_page.pack_forget()
                # y = Message(self.login_page, text=x, font="forte", bg="red")
                # y.pack()
            else:
                y = Message(self.login_page, text="WRONG LOG IN DETAILS", font="forte", bg="red", width=50, height=20)
                y.pack()

    def homeFromSettle(self):
        self.page4.destroy()
        self.page2.pack(fill=BOTH)

    def Page1ToHomePage(self):
        self.page1.pack_forget()
        self.page2.pack(fill=BOTH)

    def homePage(self):
        # self.page1.forget()
        self.page4.forget()
        self.Page1ToHomePage()
        # self.page2.pack(fill=BOTH)
        title_label = Label(self.page2, text="WELCOME", font=("forte", 24), bg="#00A6E7", width=70, height=1)
        title_label.place(bordermode=INSIDE, height=50, width=800, x=0, y=10)
        set_budget = Button(self.page2, text="*CREATE BUDGET*", width=5, height=2, bg="#0384fc", fg="white",
                            font="forte", command=self.createBudgetPage)
        set_budget.place(bordermode=INSIDE, height=50, width=300, x=200, y=200)
        settle_bills = Button(self.page2, text="*SETTLE BILLS*", width=5, height=2, bg="#0384fc", fg="white",
                              font="forte", command=self.settleBill)
        settle_bills.place(bordermode=INSIDE, height=50, width=300, x=200, y=252)
        # check for balances in all accounts
        # check_balances = Button(self.page2, text="*CHECK FUND BALANCES*", width=5, height=2, bg="#0384fc", fg="white",
        #                        font="forte")
        # check_balances.place(bordermode=INSIDE, height=50, width=300, x=200, y=304)
        # print_report = Button(self.page2, text="*PRINT REPORT*", width=5, height=2, bg="#0384fc", fg="white",
        #                      font="forte")
        # print_report.place(bordermode=INSIDE, height=50, width=300, x=200, y=356)
        shopping_assistant = Button(self.page2, text="*SHOPPING ASSISTANCE*", width=5, height=2, bg="#0384fc",
                                    fg="white", font="forte", command=self.shoppingPage)
        shopping_assistant.place(bordermode=INSIDE, height=50, width=300, x=200, y=408)

    def home_to_settle_Bill(self):
        self.page2.pack_forget()
        self.page4.pack(fill=BOTH, expand=YES)

    def settle_bill_to_home(self):
        self.page4.pack_forget()
        self.page2.pack(fill=BOTH, expand=YES)

    def home_to_create_budget(self):
        self.page2.pack_forget()
        self.page3.pack(fill=BOTH, expand=YES)

    def create_budget_to_home(self):
        self.page3.pack_forget()
        self.page2.pack(fill=BOTH, expand=YES)

    def createBudgetPage(self):
        # self.page2.destroy()
        # self.page3.pack(fill=BOTH, expand=YES)
        self.home_to_create_budget()
        back_button = Button(self.page3, text="<GO BACK", font="forte", bg="#004F6E", relief=FLAT,
                             command=self.create_budget_to_home)
        back_button.place(bordermode=INSIDE, width=150, height=50, x=5, y=10)
        create_bud_label = Label(self.page3, text="CREATE BUDGET", font="Constantia", bg="#0384fc", fg="white",
                                 relief=FLAT)
        create_bud_label.place(bordermode=INSIDE, heigh=50, width=406, x=100, y=45)
        budget_name = Label(self.page3, text="ENTER BUDGET NAME", font="forte", bg="#0384fc", fg="white")
        budget_name.place(bordermode=INSIDE, height=50, width=200, x=100, y=100)
        budget_cost = Label(self.page3, text="BUDGET COST", font="forte", bg="#0384fc", fg="white")
        budget_cost.place(bordermode=INSIDE, height=50, width=200, x=100, y=152)
        frequency = Label(self.page3, text="FREQUENCY", font="forte", bg="#0384fc", fg="white")
        frequency.place(bordermode=INSIDE, height=50, width=200, x=100, y=204)
        self.bud_name_inp = Entry(self.page3, font=("InkFree", 16), bg="#94bdff")
        self.bud_name_inp.place(bordermode=INSIDE, height=50, width=205, x=300, y=100)
        self.cost_inp = Entry(self.page3, font=("InkFree", 16), bg="#94bdff")
        self.cost_inp.place(bordermode=INSIDE, height=50, width=205, x=300, y=152)
        # create these functions to pass the arguments to the saver function
        # var1 = "DAILY"
        # var2 = "WEEKLY"
        # var3 = "MONTHLY"
        # var4 = "ANNUALLY"
        self.freq_inp1 = Checkbutton(self.page3, text="DAILY", font="constantia", variable=self.var_set("daily"),
                                     bg="#94bdff")
        self.freq_inp1.place(bordermode=INSIDE, x=300, y=204, width=105, height=25)
        self.freq_inp2 = Checkbutton(self.page3, text="WEEKLY", font="constantia", variable=self.var_set("weekly"),
                                     bg="#94bdff")
        self.freq_inp2.place(bordermode=INSIDE, x=400, y=204, width=105, height=25)
        self.freq_inp3 = Checkbutton(self.page3, text="MONTHLY", font="constantia", variable=self.var_set("monthly"),
                                     bg="#94bdff")
        self.freq_inp3.place(bordermode=INSIDE, x=300, y=229, width=105, height=25)
        self.freq_inp4 = Checkbutton(self.page3, text="ANNUALLY", font="constantia", variable=self.var_set("annually"),
                                     bg="#94bdff")
        self.freq_inp4.place(bordermode=INSIDE, x=400, y=229, width=105, height=25)
        create_budget_button = Button(self.page3, text="CREATE BUDGET", font="forte", bg="#0384fc", fg="white",
                                      relief=FLAT, command=self.initialise_budget)
        create_budget_button.place(bordermode=INSIDE, width=150, height=50, x=160, y=265)
        budget_number = Label(self.page3, text=bud_num, bg="#0384fc", fg="white", font="forte")
        budget_number.place(bordermode=INSIDE, width=150, height=48, x=350, y=265)
        existing_budgets = Label(self.page3, bg="#0384fc")
        existing_budgets.place(bordermode=INSIDE, width=240, height=500, x=550, y=50)

        del_bud = Label(self.page3, text="DELETE A BUDGET", font="Constantia", bg="#0384fc", fg="white", relief=FLAT)
        del_bud.place(bordermode=INSIDE, width=400, height=50, x=100, y=355)
        select_bud = Label(self.page3, text="BUDGET NUMBER", font="forte", bg="#0384fc", fg="white", relief=FLAT)
        select_bud.place(bordermode=INSIDE, width=150, height=40, x=100, y=410)
        self.bud_num_del = Entry(self.page3, font=("Consolas", 16))
        self.bud_num_del.place(bordermode=INSIDE, width=250, height=40, x=250, y=410)
        delete_bud = Button(self.page3, text="DELETE BUDGET", font="forte", bg="#0384fc", fg="white", relief=FLAT,
                            command=self.deleteBud)
        delete_bud.place(bordermode=INSIDE, width=150, height=50, x=100, y=455)

    def deleteBud(self):
        to_del = self.bud_num_del.get()
        database.delete_bud(to_del)

    def var_set(self, a):  # handle the four frequencies
        self.var = a

    def initialise_budget(self):  # save the budget details to the database
        global bud_num
        budget_title = self.bud_name_inp.get()
        budget_cost = self.cost_inp.get()
        database.create_budget(bud_num, budget_title, budget_cost, "UNPAID", self.var)
        bud_num += 1

    def settleBill(self):
        # self.page2.forget()
        # self.page4.pack(fill=BOTH, expand=YES)
        self.home_to_settle_Bill()
        back_button = Button(self.page4, text="GO BACK", font="forte", bg="#004F6E", fg="white",
                             command=self.settle_bill_to_home)
        back_button.place(bordermode=INSIDE, width=90, height=40, x=210, y=380)
        settle_bud_title = Label(self.page4, text="SETTLE BUDGET", font="Constantia", bg="#0384fc", fg="white",
                                 relief=FLAT)
        settle_bud_title.place(bordermode=INSIDE, height=50, width=406, x=100, y=45)
        list_of_budgets = Label(self.page4, bg="#0384fc")
        list_of_budgets.place(bordermode=INSIDE, width=240, height=500, x=550, y=50)

        bud_numb = Label(self.page4, text="BUDGET NUMBER", font="forte", bg="#0384fc", fg="white", relief=FLAT)
        bud_numb.place(bordermode=INSIDE, width=170, height=50, x=100, y=100)
        amount = Label(self.page4, text="Amount name+exp amount", font="Consolas", bg="#0384fc", fg="white",
                       relief=FLAT)
        amount.place(bordermode=INSIDE, width=350, height=100, x=100, y=155)
        payout = Label(self.page4, text="AMOUNT TO PAYOUT", font="forte", bg="#0384fc", fg="white", relief=FLAT)
        payout.place(bordermode=INSIDE, width=170, height=50, x=100, y=257)

        self.bud_num_settle = Entry(self.page4, font=("Constantia", 16))
        self.bud_num_settle.place(bordermode=INSIDE, width=235, height=50, x=270, y=100)
        self.bud_set_amount = Entry(self.page4, font=("Constantia", 16))
        self.bud_set_amount.place(bordermode=INSIDE, width=235, height=50, x=270, y=257)
        payout_button = Button(self.page4, text="PAYOUT", font="forte", bg="#0384fc", fg="white",
                               command=self.settleBillLogic)
        payout_button.place(bordermode=INSIDE, width=235, height=50, x=210,
                            y=315)  # call message box to confirm and alert
        # if payment will destabilize the month's budget

    def settleBillLogic(self):
        bud_num_settle = int(self.bud_num_settle.get())
        settle_amount = int(self.bud_set_amount.get())
        # total_bill_cost = database.settleBills()
        bill_cost = database.check_bill_cost(bud_num_settle)
        bill_balance = int(bill_cost) - settle_amount
        if bill_balance == 0:
            database.delete_bud(bud_num_settle)
            settled = Message(self.page4, text=("BUDGET NUMBER", bud_num_settle, "HAS BEEN FULLY SETTLED AND DELETED"),
                              bg="red")
            settled.pack()
        else:
            database.updateBillBal(bill_balance, bud_num_settle)
            bal = settle_amount / bill_cost * 100
            bill_balance = database.check_bill_cost(bud_num_settle)
            half_settled = Message(self.page4, text=("BUDGET", bal, "% SETTLED\nKSh.", bill_balance, "remaining"),
                                   bg="red")
            half_settled.pack()

    def homeToPage2_to_shopping(self):
        self.page2.pack_forget()
        self.page5.pack(fill=BOTH, expand=YES)

    def shopping_to_homeToPage2(self):
        self.page5.pack_forget()
        self.page2.pack(fill=BOTH, expand=YES)

    def shoppingPage(self):
        self.homeToPage2_to_shopping()
        self.page5.pack(fill=BOTH, expand=YES)
        back_button = Button(self.page5, text="<GO BACK", font="forte", bg="#004F6E", relief=FLAT,
                             command=self.shopping_to_homeToPage2)
        back_button.place(bordermode=INSIDE, width=150, height=50, x=5, y=30)
        shopping_title = Label(self.page5, text="SHOPPING ASSISTANT", font=("Constantia", 16), bg="#0384fc", fg="white")
        shopping_title.place(bordermode=INSIDE, width=500, height=50, x=150, y=40)
        create_shopping_btn = Button(self.page5, text="CREATE A SHOPPING LIST", font="forte", bg="#0384fc", fg="white")
        create_shopping_btn.place(bordermode=INSIDE, width=400, height=50, x=200, y=100)
        plus = Button(self.page5, text="+ ADD ITEM", font="forte", bg="#0384fc", fg="white",
                      command=lambda: [self.goodsEntry(), self.shoppingBoxAlign(), self.recordList()])
        plus.place(bordermode=INSIDE, width=100, height=50, x=300, y=160)

        confirm = Button(self.page5, text="CONFIRM*", font="forte", bg="#0384fc", fg="white",
                         command=self.Closure)
        confirm.place(bordermode=INSIDE, width=100, height=50, x=400, y=160)

    def Closure(self):
        time.sleep(5)
        self.shopping_to_homeToPage2()

    def goodsEntry(self):
        global prod_count
        global y_align
        self.goods_box = Entry(self.page5, font=("Constantia", 16))
        self.goods_box.place(bordermode=INSIDE, width=235, height=30, x=ex_al, y=y_align)
        self.saveItem()
        y_align += 40
        prod_count += 1

    def saveItem(self):
        global row
        self.save = Button(self.page5, text="Save Item", font="chiller", bg="lightblue", fg="white",
                           command=lambda: [self.recordList(), self.forgetSaverButton(self.save),
                                            self.goodsEntry(), self.shoppingBoxAlign()])
        self.save.place(bordermode=INSIDE, width=235, height=30, x=(ex_al + 200), y=y_align)
        row += 40

    @staticmethod
    def forgetSaverButton(button):
        button.place_forget()

    def recordList(self):
        shopping_list.append(self.goods_box.get())

    @staticmethod
    def confirm_shopping_list():
        for k in shopping_list:
            print(k)

    @staticmethod
    def shoppingBoxAlign():
        global prod_count
        global y_align
        global ex_al
        if prod_count == 9:
            y_align = 230
            ex_al += 240


root = Tk()
my_gui = FundManagerWindow(root, Canvas, Canvas, Canvas, Canvas, Canvas, Canvas, str, str, str, str, str, str, str, str,
                           int, str, str, str, str, int, str, str, str, int, int, Entry, Button, Canvas)
root.mainloop()
