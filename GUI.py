# test comment
import tkinter as tk
import pandas as pd
import numpy as np
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfile
import re, datetime

# FUNCTIONS=========================================================================================================

# open file function
def open_file():
    x1 = " "

    file = askopenfile(parent=root, mode='r', title="choose a file", filetype=[("CSV File", "*.csv")])
    x1 = file.name  # This is getting the exact file address

    completeLabel = tk.Label(root, text=file.name + "has been processed", fg="Blue")
    completeLabel.place_forget()

    eStr1 = e1.get()   # These are getting the inputs from Entry boxes 1-3
    eStr2 = e2.get()
    eStr3 = e3.get()
    intCheck()

    if intCheck() == True:
        eStr3= int(eStr3)
        clean_rev(x1, eStr1, eStr2, eStr3)
        completeLabel.place(x=105, y=255)



    else:
        print("error")
        newWindow = tk.Toplevel(root)
        newWindow.geometry("350x50")
        completeLabel2 = tk.Label(newWindow, text="ERROR: Please enter numeric values ONLY", fg="red", font="bold")
        completeLabel2.grid(column=4, row=4)





    browse_text.set("Run")


def callrevRaquel():
    x1 = " "
    file = askopenfile(parent=root, mode='r', title="choose a file", filetype=[("Excel File", "*.xlsx")])
    x1 = file.name  # This is getting the exact file address
    revRaquel(x1)
    completeLabel = tk.Label(root, text=file.name + "has been processed", fg="Blue")
    completeLabel.place_forget()
    completeLabel.place(x=105, y=255)
def revRaquel(x):
    # Import the excel file that needs to have dates adjusted
    data1 = pd.read_excel(x)

    # Drop 1st column since it doesn't have useful information
    data1.pop(data1.columns[0])

    # Create new column which will store the "cleaned dates"
    data1['Date (clean)'] = None

    # To have easy access to the taget columns
    index_description = data1.columns.get_loc('Computation memo')
    index_date = data1.columns.get_loc('Date (clean)')

    # This for-loop looks for the first date on each box under Computation Memo column and send the new value to Date (clean)
    for row in range(0, len(data1)):
        date = re.search(r'([0-9]{2}\/[0-9]{2}\/[0-9]{4})', data1.iat[row, index_description]).group()
        data1.iat[row, index_date] = date

    data1.to_excel(x)


# to test openfile and entry box input
def testInput(f1,a1,a2,a3):
    print(type(f1))
    print(type(a1))
    print(type(a2))
    print(type(int(a3)))


def clean_rev(x, m1, m2, y):
    # This loads the CSV file into the console
    df1 = pd.read_csv(x)
    df1.columns = [
        'Posted_Dt',
        'Doc_Dt',
        'Doc',
        'Memo / Description',
        'Department',
        'Location',
        'Contract',
        'Customer Name',
        'JNL',
        'Curr',
        'Txn Amt',
        'Debit',
        'Credit',
        'Balance (USD)'
    ]
    df1 = df1.fillna(0)

    df1["Total Billed"] = df1.Credit - df1.Debit

    df1.drop(df1[df1['Memo / Description'] == 0].index, inplace=True)

    df1['Posted_Dt'] = pd.DatetimeIndex(df1['Posted_Dt']).month

    pivot1 = pd.pivot_table(df1, index=['Contract', 'Customer Name'],
                                columns='Posted_Dt',
                                values='Total Billed',
                                aggfunc='sum')

    df2 = pd.DataFrame(pivot1.to_records())

    df2 = df2.fillna(0)

    df2["Variance"] = df2[m1] - df2[m2]

    df_final = df2[(df2.Variance >= y) | (df2.Variance <= -y)]
    df_final.to_csv(x)


# function to check value of radio button selected
def clicked(value):
    if value == 2:
        Funct2()

    if value == 1:
        Funct1()

    if value == 3:
        Funct3()

# functions to be called by radio buttons to show menu frames
def Funct1():
    frame3.place_forget()
    frame2.place_forget()
    frame1.place(width=600, height=220)


def Funct2():
    frame1.place_forget()
    frame3.place_forget()
    frame2.place(width=600, height=220)

def Funct3():
    frame1.place_forget()
    frame2.place_forget()
    frame3.place(width=600, height=220)

# checks for integer values in entry boxes, will return error
def intCheck():
    try:
        int(e1.get())
        int(e2.get())
        int(e3.get())
        return True
    except ValueError:
        return False


def printingTest():
    print("THIS IS THE SECOND WIDGET")


# MAIN CODE=========================================================================================================

# root canvas and frames set up along with icon and title of window
root = tk.Tk()
root.title('Revenue Clean Up')
root.iconbitmap('ilandicon.ico')


canvas = tk.Canvas(root)
root.geometry("600x300")
# frames will not cover radio buttons in root
frame1 = tk.Frame(root, bg="#F0F0F0", width=290, height=145)
frame2 = tk.Frame(root, bg="#F0F0F0", width=290, height=145)
frame3 = tk.Frame(root, bg="#F0F0F0", width=290, height=145)


# logos for both frames
logo = Image.open('iland.png')
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(frame1, image=logo)
logo_label.image = logo
logo_label.place(x=380, y=40)

logo2 = Image.open('iland.png')
logo2 = ImageTk.PhotoImage(logo2)
logo2_label = tk.Label(frame2, image=logo2)
logo2_label.image = logo2
logo2_label.place(x=380, y=40)

logo3 = Image.open('iland.png')
logo3 = ImageTk.PhotoImage(logo3)
logo3_label = tk.Label(frame3, image=logo3)
logo3_label.image = logo3
logo3_label.place(x=380, y=40)


# radio buttons for main root bottom menu
r = tk.IntVar()
r.set("1")

radB=tk.Radiobutton(root, text="Revenue Clean-up", variable=r, value=1, command=lambda: clicked(r.get()))
radB.place(x=80,y=220)
radB=tk.Radiobutton(root, text="Pay Match", variable=r, value=2, command=lambda: clicked(r.get()))
radB.place(x=250,y=220)
radB=tk.Radiobutton(root, text="Raquel Rev Report", variable=r, value=3, command=lambda: clicked(r.get()))
radB.place(x=375,y=220)


# instructions for both frames
instructions = tk.Label(frame1, text="Select a file to process", font="helvetica 12 bold", bg="#F0F0F0")
instructions.place(x=375, y=120)
instructions2 = tk.Label(frame2, text="Select a file to process", font="helvetica 12 bold", bg="#F0F0F0")
instructions2.place(x=375, y=120)
instructions3 = tk.Label(frame3, text="Select a file to process", font="helvetica 12 bold", bg="#F0F0F0")
instructions3.place(x=375, y=120)


# input boxes and labels for both frames
tk.Label(frame1, text="Month 1").place(x=80, y=50)
tk.Label(frame1, text="Month 2").place(x=80, y=100)
tk.Label(frame1, text="Variance scope").place(x=80, y=150)

e1 = tk.Entry(frame1)
e2 = tk.Entry(frame1)
e3 = tk.Entry(frame1)
e1.place(x=180, y=50)
e2.place(x=180, y=100)
e3.place(x=180, y=150)

tk.Label(frame2, text = "Value").place(x=80, y=50)
e4 = tk.Entry(frame2)
e4.place(x=180, y=50)


# RUN button set up for both frames
browse_text = tk.StringVar()                                                         # changed font, color, and bg of button
browsebtn = tk.Button(frame1, textvariable=browse_text, command=open_file, font="helvetica 12 bold", bg="navy blue", fg="gold", height=1, width=15)
browse_text.set("Run")
browsebtn.place(x=380, y=170)

browsebtn2 = tk.Button(frame2, textvariable=browse_text, command=printingTest,  font="helvetica 12 bold", bg="navy blue", fg="gold", height=1, width=15)
browse_text.set("Run")
browsebtn2.place(x=380, y=170)

browsebtn3 = tk.Button(frame3, textvariable=browse_text, command=callrevRaquel,  font="helvetica 12 bold", bg="navy blue", fg="gold", height=1, width=15)
browse_text.set("Run")
browsebtn3.place(x=380, y=170)


#  starts off program on  frame 1
Funct1()

root.mainloop()





