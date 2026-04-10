#Package and Modules
from tkinter import *
from tkinter.messagebox import showerror

# GUI function 

def data_input():
    password = user_input.get()
    output_label.config(text=f"Result\n")

    if not password.strip():
        showerror("Error", "Password cannot be empty!")
        return 

    user_pwd = PasswordStrengthChecker(password)

    input_page.pack_forget()
    output_page.pack(fill=BOTH, expand=True)

    text_box.config(state=NORMAL)
    text_box.delete(1.0, END)
    text_box.insert(END, user_pwd.conditions_check())
    text_box.config(state=DISABLED)

def go_back():
    output_page.pack_forget()
    input_page.pack(fill=BOTH, expand=True)

window = Tk()

#GUI Configuration

#Title, Icon, Transperency & Color
window.title("Password Strength Analyzer")
window.iconbitmap(r"F:\Python\PAdlock.ico")
window.attributes('-alpha',0.9)
window.config(bg="black")

#pages 
main_frame = Frame(window, bg="black")
main_frame.pack(fill=BOTH, expand=True)

#Width and size 
window_width = 750
window_height = 700

sys_width = window.winfo_screenwidth()
sys_height = window.winfo_screenheight()

center_x_coordinate = int(sys_width/2 - window_width/2)
center_y_coordinate = int(sys_height/2 - window_height/2)

window.geometry(f"{window_width}x{window_height}+{center_x_coordinate}+{center_y_coordinate}")

window.resizable(False,False)

input_page = Frame(main_frame, bg="black")
user_input = StringVar()

# label
entry_label = Label(input_page,text="Enter your Password", font=("Times New Roman",20,"bold"),fg="white",bg="black")
entry_label.pack(padx=10,pady=250)

# Entry
user_entry = Entry(input_page,font=("Times New Roman",15),justify="center",bg="white",textvariable=user_input)
user_entry.place(x=248,y=300,width = 250)

# Button 
input_button = Button(input_page,text="Submit",font=("Times New Roman",10),justify="center",command=data_input)
input_button.place(x=348,y=340,width=60)

# Start with input page
input_page.pack(fill=BOTH, expand=True)

#output page 
output_page = Frame(main_frame, bg="black")

output_label = Label(output_page,text="Result",font=("Times New Roman", 20, "bold"),fg="white", bg="black")
output_label.pack(pady=(120,20))

back_button = Button(output_page,text="Back",command=go_back)
back_button.place(x=348,y=600,width=60)

#outputbox

text_box = Text(output_page, height=20, width=80)
text_box.pack(pady=10)

window.mainloop()
