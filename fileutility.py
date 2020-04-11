from tkinter import *

window = Tk()
window.geometry("300x600")
window.resizable(width=False, height=False)
window.title("File Utility")
window.iconbitmap("File-Explorer.ico")

padding_1 = Label(text="")
padding_1.pack()

top_Label = Label(text="File Utility", font=20)
top_Label.pack()

padding_2 = Label(text="")
padding_2.pack()
padding_3 = Label(text="")
padding_3.pack()

source_dir_label = Label(window, text="Source Directory")
source_dir_label.pack()
source_dir_entry = Entry(window, width=40)
source_dir_entry.pack()
padding_4 = Label(text="")
padding_4.pack()

dest_dir_label = Label(window, text="Destination Directory")
dest_dir_label.pack()
dest_dir_entry = Entry(window, width=40)
dest_dir_entry.pack()
padding_5 = Label(text="")
padding_5.pack()

file_operation_Label = Label(text="File Operation", font=14)
file_operation_Label.pack()
padding_6 = Label(text="")
padding_6.pack()

file_operation_frame = Frame(window, width=60, height=60)
file_operation_frame.pack()

# file operation function


v = IntVar()

R1 = Radiobutton(file_operation_frame, value="rename", text="Rename Files", variable=v)
R1.pack(anchor=W)
R2 = Radiobutton(file_operation_frame, value="move", text="Move Files", variable=v)
R2.pack(anchor=W)
R3 = Radiobutton(file_operation_frame, value="archive", text="Archive Files", variable=v)
R3.pack(anchor=W)

padding_7 = Label(text="")
padding_7.pack()
padding_8 = Label(text="")
padding_8.pack()

actionframe = Frame(window, width=80, height=80)
actionframe.pack()

cancelbtn = Button(actionframe, text="Cancel", width=10, padx=10, pady=5, state=DISABLED)
cancelbtn.pack(side=LEFT)
submitbtn = Button(actionframe, text="Submit", width=10, padx=10, pady=5, state=DISABLED)
submitbtn.pack(side=RIGHT)



window.mainloop()

if __name__ == "main":
    window.run()
