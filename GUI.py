#GUI prototype

import tkinter as tk
import pandas as pd
import numpy as np
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfile

#open file function

def open_file():
    x1 = " "
    browse_text.set("Loading...")
    file = askopenfile(parent=root, mode='r', title="choose a file", filetype=[("CSV File", "*.csv")])
    x1 = file.name  # This is getting the exact file address
    eStr1 = e1.get()   # These are getting the inputs from Entry boxes 1-3
    eStr2 = e2.get()
    eStr3 = int(e3.get())

    clean_rev(x1, eStr1, eStr2, eStr3)
    newWindow = tk.Toplevel(root)
    newWindow.geometry("300x50")
    completeLabel = tk.Label(newWindow, text=file.name)
    completeLabel.grid(column=3, row=4)
    completeLabel2 = tk.Label(newWindow, text="has been processed")
    completeLabel2.grid(column=4, row=4)

    browse_text.set("Run")
def callClean():
    open_file()

def testInput(f1,a1,a2,a3): # to test openfile and entry box input
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
    df_final.to_csv(r'C:\Users\gregi\Downloads\finalTest.csv')

def clicked(value):
    if value == 2:
        # Added frames with new radio buttons and entry boxes for secondary apps
       center = tk.Frame(root, bg="teal", width=290, height=145)
       center.place(width=600, height=250)
       lab1=tk.Label(center, text="Value 1").grid(column=1, row=0, padx=20)
       lab2=tk.Label(center, text="Value 2").grid(column=1, row=1, padx=20)
       lab3=tk.Label(center, text="Value 3").grid(column=1, row=2, padx=20)
       e1 = tk.Entry(center)
       e2 = tk.Entry(center)
       e3 = tk.Entry(center)
       e1.grid(row=0, column=2)
       e2.grid(row=1, column=2)
       e3.grid(row=2, column=2)
       r = tk.IntVar()
       r.set("2")

       radB2 = tk.Radiobutton(root, text="Revenue Clean-up2", variable=r, value=1, command=lambda: clicked(r.get()))
       radB2.grid(column=1, row=3)
       radB2 = tk.Radiobutton(root, text="Sales Register2", variable=r, value=2, command=lambda: clicked(r.get()))
       radB2.grid(column=2, row=3)





##########################################################################################################
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$#
##########################################################################################################

root = tk.Tk()
canvas = tk.Canvas(root, width=600, height=300)
canvas.grid(columnspan=7, rowspan=5)
# logo
logo = Image.open('iland.png')
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(image=logo)
logo_label.image = logo
logo_label.grid(column=5, row=0, padx=50)

# radio buttons
r = tk.IntVar()
r.set("1")

radB=tk.Radiobutton(root, text="Revenue Clean-up", variable=r, value=1, command=lambda: clicked(r.get()))
radB.grid( column=5, row=3)
radB=tk.Radiobutton(root, text="Sales Register", variable=r, value=2, command=lambda: clicked(r.get()))
radB.grid( column=2, row=3)

# instructions
instructions= tk.Label(root, text="Select a file to process", font="helvetica 12 bold", bg="white")
instructions.grid(column=5, row=1)

#input boxes
tk.Label(root, text="Value 1").grid(column=1, row=0, padx=20)
tk.Label(root, text="Value 2").grid(column=1, row=1, padx=20)
tk.Label(root, text="Value 3").grid(column=1, row=2, padx=20)

e1 = tk.Entry(root)
e2 = tk.Entry(root)
e3 = tk.Entry(root)



e1.grid(row=0, column=2)
e2.grid(row=1, column=2)
e3.grid(row=2, column=2)



browse_text = tk.StringVar()                                                         # changed font, color, and bg of button
browsebtn = tk.Button(root, textvariable=browse_text, command=open_file, font="helvetica 12 bold", bg="navy blue", fg="gold", height=1, width=15)
browse_text.set("Run")
browsebtn.grid(column=5, row=2)



root.mainloop()





