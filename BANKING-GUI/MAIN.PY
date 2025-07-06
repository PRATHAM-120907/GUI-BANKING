from tkinter import *
from tkinter import messagebox
import json
import pyperclip
from PIL import Image, ImageDraw, ImageFont
import os
BACKGROUND = "#91C8E4"
BUTTON_COLORS = "#E69DB8"
# AFTER GENERATING THE CREDIT CARD IT WILL SAVE AS ANOTHER USERNAME.PNG , U CAN SEE IT IN THE SIDE FOLDER NAMED GENERATED CARDS

info = {}
#---------------------------------------------CREATING ACCOUNT WINDOW----------------------
def creating_account_window():
    new_window = Toplevel(window)
    new_window.title("NEW ACCOUNT")
    new_window.geometry("800x500")
    new_window.configure(bg="#E67514")
 #-----------------------------------CREATING ACCOUNT CANVAS-------------------------------------
    new_canvas = Canvas(new_window, width=800, height=500, bg=BACKGROUND, highlightthickness=0)
    new_canvas.grid(row=0, column=0)

    new_canvas.create_text(400, 40, text="CREATE NEW ACCOUNT", font=("Arial", 20, "bold"), fill="#E67514")
 #-----------------------------------CREATING ACCOUNT ENTRY FIELDS-------------------------------------]
    new_canvas.create_text(90, 130, text="Account number", font=("Arial", 13, "bold"), anchor="w")
    acc_entry = Entry(new_window, width=30)
    acc_entry.focus()
    new_canvas.create_window(270, 130, window=acc_entry, anchor="w")

    new_canvas.create_text(90, 170, text="First Name", font=("Arial", 13, "bold"), anchor="w")
    first_entry = Entry(new_window, width=30)
    new_canvas.create_window(270, 170, window=first_entry, anchor="w")

    new_canvas.create_text(90, 210, text="Last Name", font=("Arial", 13, "bold"), anchor="w")
    last_entry = Entry(new_window, width=30)
    new_canvas.create_window(270, 210, window=last_entry, anchor="w")

    new_canvas.create_text(90, 250, text="Initial Amount", font=("Arial", 13, "bold"), anchor="w")
    amount_entry = Entry(new_window, width=30)
    new_canvas.create_window(270, 250, window=amount_entry, anchor="w")

    new_canvas.create_text(90, 290, text="Address", font=("Arial", 13, "bold"), anchor="w")
    address_entry = Entry(new_window, width=30)
    new_canvas.create_window(270, 290, window=address_entry, anchor="w")

    new_canvas.create_text(90, 330, text="Phone Number", font=("Arial", 13, "bold"), anchor="w")
    phone_entry = Entry(new_window, width=30)
    new_canvas.create_window(270, 330, window=phone_entry, anchor="w")

    new_canvas.create_text(90, 370, text="Date of Birth", font=("Arial", 13, "bold"), anchor="w")
    dob_entry = Entry(new_window, width=30)
    new_canvas.create_window(270, 370, window=dob_entry, anchor="w")

    new_canvas.create_text(90, 410, text="Email", font=("Arial", 13, "bold"), anchor="w")
    email_entry = Entry(new_window, width=30)
    new_canvas.create_window(270, 410, window=email_entry, anchor="w")

    new_canvas.create_text(90, 450, text="4 DIGIT PIN", font=("Arial", 13, "bold"), anchor="w")
    pin_entry = Entry(new_window, width=30, show="*")
    new_canvas.create_window(270, 450, window=pin_entry, anchor="w")
    #--------------------------------------------SAVING ACCOUNT INFO----------------------------------------
    def save_account_info():
        if not all([
            acc_entry.get(),
            first_entry.get(),
            last_entry.get(),
            amount_entry.get(),
            address_entry.get(),
            phone_entry.get(),
            dob_entry.get(),
            email_entry.get(),
            pin_entry.get()
        ]):
            messagebox.showerror("Error", "Please fill in all fields.")
            return

        if any(char.isdigit() for char in first_entry.get()):
            messagebox.showerror("Invalid Name", "First Name must not contain numbers.")
            return

        if any(char.isdigit() for char in last_entry.get()):
            messagebox.showerror("Invalid Name", "Last Name must not contain numbers.")
            return

        phone = phone_entry.get()
        if not phone.isdigit():
            messagebox.showerror("Invalid Phone", "Phone number must contain only digits.")
            return
        if len(phone) != 10:
            messagebox.showerror("Invalid Phone", "Phone number must be exactly 10 digits.")
            return

        pin = pin_entry.get()
        if not pin.isdigit() or len(pin) > 4:
            messagebox.showerror("Invalid PIN", "PIN must be a number with at most 4 digits.")
            return

        try:
            amount = float(amount_entry.get())
            if amount < 2000:
                messagebox.showerror("Minimum Balance Error", "Initial deposit must be at least ₹2000.")
                amount_entry.focus()
                return
        except ValueError:
            messagebox.showerror("Invalid Input", "Initial Amount must be a number.")
            return

        new_data = {
            "Account Number" : acc_entry.get(),
            "First Name": first_entry.get(),
            "Last Name": last_entry.get(),
            "Initial Amount": amount_entry.get(),
            "Address": address_entry.get(),
            "Phone Number": phone_entry.get(),
            "Date of Birth": dob_entry.get(),
            "Email": email_entry.get(),
            "4 DIGIT PIN": pin_entry.get()
        }

        try:
            with open("data/info.json", "r") as file:
                data = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            data = []

        data.append(new_data)

        with open("data/info.json", "w") as file:
            json.dump(data, file, indent=4)
            messagebox.showinfo("Success", "Account created successfully")

    submit_button = Button(new_canvas, text="SUBMIT DETAILS", font=("Arial", 16, "bold"),
                           bg="#4CAF50", fg="white", command=save_account_info)
    new_canvas.create_window(600, 250, window=submit_button)


#-------------------------------------DEPOSIT AMOUNT WINDOW--------------------------

def deposit_amount():
    add_window = Toplevel(window)
    add_window.title("DEPOSING AMOUNT")
    add_window.geometry("800x500")
    add_window.configure(bg=BACKGROUND)

    #--------------------------DEPOSIT AMOUNT CANVAS--------------------------------

    deposit_canvas = Canvas(add_window, width=800, height=500, bg=BACKGROUND, highlightthickness=0)
    deposit_canvas.grid(row=0 , column=0)
    deposit_canvas.create_text(400, 60, text="DEPOSING MONEY", font=("Arial", 30, "bold"), fill="#E67514")
    #-------------------------------------------------------------------------------------------------------
    #------------------------------CREATING DEPOSIT AMOUNT FIELD-------------------------------------------

    deposit_canvas.create_text(170, 200, text="ACCOUNT NUMBER", font=("Arial", 15, "bold"), anchor="center")
    deposit_account_entry = Entry(add_window, width=30)
    deposit_canvas.create_window(170, 230, window=deposit_account_entry)

    deposit_canvas.create_text(570, 200, text="ENTER MONEY", font=("Arial", 15, "bold"), anchor="center")
    money_entry = Entry(add_window, width=30)
    deposit_canvas.create_window(570, 230, window=money_entry)

    

    def update_balance():
        acc_no = deposit_account_entry.get()
        money_str = money_entry.get()

        if not acc_no or not money_str :
            messagebox.showerror(title="ERROR" ,message="Please fill in both fields.")
            return
        
        try:
            deposit = float(money_str)
            if deposit <=0:
                raise ValueError
        except ValueError:
            messagebox.showerror("INVALID AMOUNT" ,"PLEASE ENTER THE VALID POSITIVE NUMBER ")
            return
        
        try:
            with open ("data/info.json") as file:
                data = json.load(file)
        except (FileNotFoundError , json.JSONDecoderError):
             messagebox.showerror("Data Error", "No data file found or file is corrupted.")
             return
        for account in data:
            if account.get("Account Number") == acc_no:
                try:
                    current_balance = float(account["Initial Amount"])
                except ValueError:
                    current_balance =0
                
                new_balance = current_balance + deposit
                account["Initial Amount"] = str(new_balance)

                with open ("data/info.json" ,"w") as file :
                    json.dump(data , file , indent=4)
                    messagebox.showinfo("Success", f"₹{deposit} added to account {acc_no}.")
            return

        messagebox.showerror("Not Found", f"No account with number {acc_no} was found.")
            


    sum_bt = Button(deposit_canvas, text="SUBMIT DETAILS", font=("Arial", 16, "bold"),
                           bg="#4CAF50", fg="white", command=update_balance)
    deposit_canvas.create_window(370, 300 ,window=sum_bt)
#----------------------------------------------------------------------------------------------------------------
#--------------------------------------------WITHDRAW MONEY-----------------------------------------------

def withdraw_window():
    with_draw = Toplevel(window)
    with_draw.title("WITHDRAW AMOUNT")
    with_draw.geometry("800x500")
    with_draw.configure(bg=BACKGROUND)
    #---------------------------------WITHDRAW CANVAS CREATING-----------------------------------

    with_draw_canvas = Canvas(with_draw, width=800, height=500, bg=BACKGROUND, highlightthickness=0)
    with_draw_canvas.grid(row=0 , column=0)
    with_draw_canvas.create_text(400, 60, text="WITHDRAWING MONEY", font=("Arial", 30, "bold"), fill="#E67514")

    #---------------------------WITHDRAW MONEY FIELDS---------------------------------------------------------

    with_draw_canvas.create_text(170, 200, text="ACCOUNT NUMBER", font=("Arial", 15, "bold"), anchor="center")
    with_acc_no = Entry(with_draw , width=30)
    with_draw_canvas.create_window(170, 230, window=with_acc_no)

    with_draw_canvas.create_text(570, 200, text="ENTER MONEY", font=("Arial", 15, "bold"), anchor="center")
    money_entry = Entry(with_draw, width=30)
    with_draw_canvas.create_window(570, 230, window=money_entry)



    with_draw_canvas.create_text(370 ,200 ,text="PIN" ,font=("Arial", 15, "bold"), anchor="center")
    with_pin = Entry(with_draw, width=25, show="*")
    with_draw_canvas.create_window(370 ,230 ,window=with_pin)

    def withdraw_money():
        ac_no = with_acc_no.get()
        mo = money_entry.get()
        pin_en = with_pin.get()

        if not ac_no or not mo or not pin_en:
            messagebox.showerror("ERROR", "Please fill in all fields.")
            return
        try:
            withdraw_amount = float(mo)
            if withdraw_amount <= 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("Invalid Amount", "Please enter a valid, positive number.")
            return
        try:
            with open("data/info.json", "r") as file:
                data = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            messagebox.showerror("Data Error", "No data file found or file is corrupted.")
            return

        for account in data:
            if account.get("Account Number") == ac_no:
                stored_pin = account.get("4 DIGIT PIN")
                if stored_pin != pin_en:
                    messagebox.showerror("Authentication Failed", "Incorrect PIN.")
                    return

                try:
                    current_balance = float(account["Initial Amount"])
                except ValueError:
                    current_balance = 0

                if current_balance < withdraw_amount:
                    messagebox.showerror("INSUFFICIENT BALANCE", "Not enough balance to complete this transaction.")
                    return

                new_balance = current_balance - withdraw_amount
                account["Initial Amount"] = str(new_balance)

                with open("data/info.json", "w") as file:
                    json.dump(data, file, indent=4)

                messagebox.showinfo("Success", f"₹{withdraw_amount} withdrawn successfully from account {ac_no}.")
                return

        messagebox.showerror("Not Found", f"No account with number {ac_no} was found.")

    sum_bt = Button(with_draw, text="SUBMIT DETAILS", font=("Arial", 16, "bold"),
                    bg="#4CAF50", fg="white", command=withdraw_money)
    with_draw_canvas.create_window(370, 300, window=sum_bt)

#--------------------------------VIEW ACCOUNT CREATING WINDOW-----------------------------------------

def view_account_window():
    view_window = Toplevel(window)
    view_window.title("VIEW ACCOUNT")
    view_window.geometry("800x500")
    view_window.configure(bg=BACKGROUND)

    view_canvas = Canvas(view_window, width=800, height=500, bg=BACKGROUND, highlightthickness=0)
    view_canvas.grid(row=0, column=0)
    view_canvas.create_text(400, 40, text="VIEW ACCOUNT DETAILS", font=("Arial", 24, "bold"), fill="#E67514")

    # ----------------- Account Number Field ---------------------
    view_canvas.create_text(180, 120, text="ACCOUNT NUMBER", font=("Arial", 15, "bold"), anchor="center")
    acc_entry = Entry(view_window, width=30)
    view_canvas.create_window(180, 150, window=acc_entry)

    # ----------------- PIN Entry Field --------------------------
    view_canvas.create_text(580, 120, text="ENTER PIN", font=("Arial", 15, "bold"), anchor="center")
    pin_entry = Entry(view_window, width=30, show="*")
    view_canvas.create_window(580, 150, window=pin_entry)

    # ----------------- Results Box -----------------------------
    result_box = Text(view_window, width=90, height=12, font=("Courier", 10))
    view_canvas.create_window(400, 300, window=result_box)

    # ----------------- Search Function -------------------------
    def search_account():
        acc_no = acc_entry.get()
        pin_no = pin_entry.get()

        if not acc_no or not pin_no:
            messagebox.showerror("Error", "Please enter both Account Number and PIN.")
            return

        try:
            with open("data/info.json", "r") as file:
                data = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            messagebox.showerror("Data Error", "Data file missing or corrupted.")
            return

        for account in data:
            if account.get("Account Number") == acc_no:
                if account.get("4 DIGIT PIN") == pin_no:
                    
                    result_box.delete("1.0", END)
                    details = (
                        f"\nACCOUNT DETAILS\n"
                        f"-----------------------------\n"
                        f"Account Number:  {account['Account Number']}\n"
                        f"First Name:      {account['First Name']}\n"
                        f"Last Name:       {account['Last Name']}\n"
                        f"Balance (₹):     {account['Initial Amount']}\n"
                        f"Address:         {account['Address']}\n"
                        f"Phone Number:    {account['Phone Number']}\n"
                        f"Date of Birth:   {account['Date of Birth']}\n"
                        f"Email:           {account['Email']}\n"
                    )
                    result_box.insert(END, details)
                    return
                else:
                    messagebox.showerror("Authentication Failed", "Incorrect PIN.")
                    return

        messagebox.showerror("Not Found", f"No account found with number {acc_no}.")

    # ----------------- Search Button ---------------------------
    view_btn = Button(view_window, text="VIEW ACCOUNT", font=("Arial", 13, "bold"),
                      bg="#4CAF50", fg="white", command=search_account)
    view_canvas.create_window(400, 200, window=view_btn)
#----------------------------------------------------------------------------------------------------
def generate_credit_card(name):
    try:
        
        card = Image.open("data/card.png")  
        draw = ImageDraw.Draw(card)

        
        font = ImageFont.truetype("arial.ttf", 24)

        
        position = (40, card.height - 60)
        draw.text(position, name, fill="white", font=font)

        
        card.save(f"generated_cards/{name.replace(' ', '_')}_card.png")
        messagebox.showinfo("Success", "Your credit card has been generated!")
    except Exception as e:
        messagebox.showerror("Error", f"Could not generate credit card: {e}")




def credit_card_window():
    card_win = Toplevel(window)
    card_win.title("Generate Credit Card")
    card_win.geometry("400x200")
    card_win.configure(bg=BACKGROUND)

    Label(card_win, text="Enter Account Number:", font=("Arial", 12, "bold"), bg=BACKGROUND).pack(pady=10)
    acc_entry = Entry(card_win, width=30)
    acc_entry.focus()
    acc_entry.pack()

    def check_and_generate():
        acc_no = acc_entry.get()
        try:
            with open("data/info.json", "r") as file:
                data = json.load(file)
        except Exception:
            messagebox.showerror("Error", "Could not load account data.")
            return

        for account in data:
            if account.get("Account Number") == acc_no:
                full_name = f"{account['First Name']} {account['Last Name']}"
                generate_credit_card(full_name)
                return

        messagebox.showerror("Not Found", "No account matches that number.")

    Button(card_win, text="Generate Card", font=("Arial", 12, "bold"),
           bg="#4CAF50", fg="white", command=check_and_generate).pack(pady=20)


#--------------------------------------------MAIN WINDOW--------------------------------------------
window = Tk()
window.title("BANKING SYSTEM")
window.geometry("800x500")
window.configure(bg=BACKGROUND)
#---------------------------------------------MAIN CANVAS--------------------------------------------------
canvas = Canvas(window, width=800, height=500, bg=BACKGROUND, highlightthickness=0)
canvas.grid(row=0, column=0)

canvas.create_text(400, 60, text="AMERICAN EXPRESS", font=("Arial", 35, "bold"))
#------------------------------------------------------------------------------------------------------------


#---------------------------------------------------MAIN PAGE BUTTONS--------------------------------------------
create_account = Button(window, text="CREATE ACCOUNT", width=20, height=2,
                        font=("Arial", 10, "bold"), bg=BUTTON_COLORS, command=creating_account_window)
canvas.create_window(90, 180, window=create_account, anchor="w")
canvas.create_text(350, 180, text="JOIN US", font=("Arial", 20, "italic"), anchor="w")

deposit_money = Button(window, text="DEPOSIT MONEY", width=20, height=2,
                       font=("Arial", 10, "bold"), bg=BUTTON_COLORS , command=deposit_amount)
canvas.create_window(90, 250, window=deposit_money, anchor="w")
canvas.create_text(350, 250, text="ADD ON", font=("Arial", 20, "italic"), anchor="w")

withdraw_money = Button(window, text="WITHDRAW MONEY", width=20, height=2,
                        font=("Arial", 10, "bold"), bg=BUTTON_COLORS ,command=withdraw_window)
canvas.create_window(90, 320, window=withdraw_money, anchor="w")
canvas.create_text(350, 320, text="MAKING OUT", font=("Arial", 20, "italic"), anchor="w")

view_account = Button(window, text="VIEW ACCOUNT", width=20, height=2,
                      font=("Arial", 10, "bold"), bg=BUTTON_COLORS , command=view_account_window)
canvas.create_window(90, 390, window=view_account, anchor="w")
canvas.create_text(350, 390, text="LET'S SEE", font=("Arial", 20, "italic"), anchor="w")

credit_card = Button(window ,text="CREDIT CARD" , width=20 ,height=2, font=("Arial", 10, "bold"), bg=BUTTON_COLORS ,command=credit_card_window)
canvas.create_window(90 , 460,  window=credit_card , anchor="w")
canvas.create_text(350 ,460 , text="GET YOUR CARD",font=("Arial", 20, "italic"), anchor="w" )




window.mainloop()
