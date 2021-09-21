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
    file = askopenfile(parent=root, mode='r', title="choose a file", filetype=[("Excel file", "*.xlsx")])
    #file.write("Hello World$!!!")
    browse_text.set("Processing..")
    x1 = file.name
    print(x1)  #This is printing out the exact address of chosen file
    clean_rev(x1, e1, e2, e3)

def callClean():
    x1 = ''
    open_file()
   # clean_rev(x1, e1, e2, e3)

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
    df_final.to_csv(r'C:\Users\mosco\OneDrive\Documents\Python Scripts\final_rev_analysis.csv')

def clicked(value):
    myLabel = tk.Label(root, text=value)
    myLabel.pack
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
r.set("5")

radB=tk.Radiobutton(root, text="Revenue Clean-up", variable=r, value=1, command=lambda: clicked(r.get()))
radB.grid( column=5, row=3)
radB=tk.Radiobutton(root, text="Sales Register", variable=r, value=2, command=lambda: clicked(r.get()))
radB.grid( column=2, row=3)
radB=tk.Radiobutton(root, text="Burst rate check", variable=r, value=3, command=lambda: clicked(r.get()))
radB.grid( column=1, row=3, padx=50)
# instructions
instructions= tk.Label(root, text="Select a file to process", font="helvetica 12 bold", bg="white")
instructions.grid(column=5, row=1)

    pivot1 = pd.pivot_table(df1, index=['Contract', 'Customer Name'],
                                columns='Posted_Dt',
                                values='Total Billed',
                                aggfunc='sum')

    df2 = pd.DataFrame(pivot1.to_records())

    df2 = df2.fillna(0)

    df2["Variance"] = df2[m1] - df2[m2]

    df_final = df2[(df2.Variance >= y) | (df2.Variance <= -y)]
    df_final.to_csv(r'C:\Users\mosco\OneDrive\Documents\Python Scripts\final_rev_analysis.csv')

#input boxes
tk.Label(root, text="Value 1").grid(column=1, row=0,padx=20)
tk.Label(root, text="Value 2").grid(column=1, row=1,padx=20)
tk.Label(root, text="Value 3").grid(column=1, row=2,padx=20)

e1 = tk.Entry(root)
e2 = tk.Entry(root)
e3 = tk.Entry(root)
#e4 = tk.Entry(root)

e1.grid(row=0, column=2)
e2.grid(row=1, column=2)
e3.grid(row=2, column=2)
#e4.grid(row=3, column=2)
#Browse Button Code


browse_text = tk.StringVar()                                                         #changed font, color, and bg of button
browsebtn = tk.Button(root, textvariable=browse_text, command=callClean, font="helvetica 12 bold", bg="navy blue", fg="gold", height=1, width=15)
browse_text.set("Run")
browsebtn.grid(column=5, row=2)
#button 2
#browse_text2 = tk.StringVar()
#browsebtn2 = tk.Button(root, textvariable=browse_text2, command=open_file, font="helvetica 12 bold", bg="navy blue", fg="gold", height=1 , width=15)
#browse_text2.set("Sales Register")
#browsebtn2.grid(column=6, row=4)
#button 3
#browse_text3 = tk.StringVar()
#browsebtn3 = tk.Button(root, textvariable=browse_text3, command=open_file, font="helvetica 12 bold", bg="navy blue", fg="gold", height=1 , width=15)
#browse_text3.set("Burst Rate Check")
#browsebtn3.grid(column=6, row=6)

#browse_text4 = tk.StringVar()
#browsebtn4 = tk.Button(root, textvariable=browse_text4, command=open_file, font="helvetica 12 bold", bg="navy blue", fg="gold", height=1 , width=15)
#browse_text4.set("Choose a File")
#browsebtn4.grid(column=6, row=8)
#changed Canvas and button color
#canvas.configure(background='white')
#root.configure(background="white")


root.mainloop()




