import tkinter as tk


if __name__ == '__main__':
    window = tk.Tk()
    window.geometry("300x450")
    window.resizable(width=False, height=False)
    window.title("Portal")
    window.iconbitmap("File-Explorer.ico")

    padding_1 = tk.Label(text="")
    padding_1.pack()

    top_Label = tk.Label(text="Portal File Utility", font=20)
    top_Label.pack()

    padding_2 = tk.Label(text="")
    padding_2.pack()
    padding_3 = tk.Label(text="")
    padding_3.pack()

    source_dir_label = tk.Label(window, text="Source Directory")
    source_dir_label.pack()
    source_dir_entry = tk.Entry(window, width=40)
    source_dir_entry.pack()
    padding_4 = tk.Label(text="")
    padding_4.pack()


    def clear_source_entry():
        source_dir_entry.delete(0, 'end')


    file_operation_Label = tk.Label(text="File Operation Progress", font=12)
    file_operation_Label.pack()
    padding_6 = tk.Label(text="")
    padding_6.pack()

    file_operation_frame = tk.Frame(window, width=60, height=60)
    file_operation_frame.pack()

    actionframe = tk.Frame(window, width=80, height=80)
    actionframe.pack()

    cancelbtn = tk.Button(actionframe, text="Cancel", width=10, padx=10, pady=5, state='disabled',
                          command=clear_source_entry)
    cancelbtn.pack(side='left')
    submitbtn = tk.Button(actionframe, text="Submit", width=10, padx=10, pady=5, state='disabled')
    submitbtn.pack(side='right')


    def toggle_state(*_):
        if source_dir_entry.var.get():
            cancelbtn['state'] = 'normal'
            submitbtn['state'] = 'normal'

        else:
            cancelbtn['state'] = 'disabled'
            submitbtn['state'] = 'disabled'


    source_dir_entry.var = tk.StringVar()
    source_dir_entry['textvariable'] = source_dir_entry.var
    source_dir_entry.var.trace_add('write', toggle_state)

    padding_9 = tk.Label(text="")
    padding_9.pack()
    padding_10 = tk.Label(text="")
    padding_10.pack()
    window.mainloop()
