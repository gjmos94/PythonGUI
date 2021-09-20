#GUI prototype
import tkinter as tk
import pandas as pd
import numpy as np
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfile

root = tk.Tk()

canvas = tk.Canvas(root, width=600, height=300)
canvas.grid(columnspan=3, rowspan=3)

#logo
logo= Image.open('iland.png')
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(image=logo)
logo_label.image = logo
logo_label.grid(column=1, row=0)

def testOpen_file():
    print("This works!!!")

#open file function
def open_file():
    browse_text.set("Completed")
    file = askopenfile(parent=root, mode='w', title="choose a file", filetype=[("Txt file", "*.txt")])
    file.write("Hello World!!!")

#instructions
instructions= tk.Label(root, text="Select a file to process", font="helvetica 12 bold", bg="white")
instructions.grid(columnspan=3,column=0, row=1)

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

#Browse Button Code
browse_text = tk.StringVar()                                                         #changed font, color, and bg of button
browsebtn = tk.Button(root, textvariable=browse_text, command=open_file, font="helvetica 12 bold", bg="navy blue", fg="gold", height=2 , width=15)
browse_text.set("Browse")
browsebtn.grid(column=1, row=2)
#changed Canvas and button color
canvas.configure(background='white')
root.configure(background="light blue")
root.mainloop()

