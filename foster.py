if __name__ == '__main__':
    from tkinter import *
    from tkinter import messagebox
    from tkinter import ttk


    class Foster:
        def __init__(self):
            self.root = root
            self.root.title('FOSTER HOME MANAGEMENT SYSTEM')
            self.root.geometry('1350x700+0+0')
            self.root.config(bg='gray')

            title = Label(self.root, text='FOSTER HOME MANAGEMENT SYSTEM', font=('dejavu serif', 25, 'bold'), bg='red',
                          fg='Gray')
            title.pack(side=TOP, fill=X)

            def Clear():
                entFno.delete(0, END)
                entFosterF.delete(0, END)
                entFosterM.delete(0, END)
                entDof.delete(0, END)
                entFosterC.delete(0, END)

            def sExit():
                sExit = messagebox.askyesno('Foster Home Management System', 'Please Confirm System Exit!')
                if sExit > 0:
                    root.destroy()
                    return

            buttonBack = Button(self.root, text='BACK', font=('dejavu serif', 15, 'bold'), bg='blue', fg='white')
            buttonBack.place(y=42)

            buttonExit = Button(self.root, text='Exit the System', font=('dejavu serif', 15, 'bold'), bg='blue',
                                fg='white', command=sExit)
            buttonExit.pack(side=TOP, anchor='e')

            # foster frame

            fosterFrame = Frame(self.root, relief=RIDGE, bd=2)
            fosterFrame.place(y=77, width=480, height=640)

            fosterTitle = Label(fosterFrame, text='MANAGE FOSTER PARENTS', font=('dejavu serif', 20, 'bold'),
                                fg='white')
            fosterTitle.grid(row=0, columnspan=2, sticky='n', pady=10)

            lblFno = Label(fosterFrame, text='Foster No.', font=('dejavu serif', 15, 'bold'))
            lblFno.grid(row=1, column=0, sticky='w', padx=20, pady=10)
            entFno = Entry(fosterFrame, font=('dejavu serif', 15, 'bold'), relief=RIDGE)
            entFno.grid(row=1, column=1, sticky='w', padx=20, pady=10)

            lblFosterF = Label(fosterFrame, text='Foster Father', font=('dejavu serif', 15, 'bold'))
            lblFosterF.grid(row=2, column=0, sticky='w', padx=20, pady=10)
            entFosterF = Entry(fosterFrame, font=('dejavu serif', 15, 'bold'), relief=RIDGE)
            entFosterF.grid(row=2, column=1, sticky='w', padx=20, pady=10)

            lblFosterM = Label(fosterFrame, text='Foster Mother', font=('dejavu serif', 15, 'bold'))
            lblFosterM.grid(row=3, column=0, sticky='w', padx=20, pady=10)
            entFosterM = Entry(fosterFrame, font=('dejavu serif', 15, 'bold'), relief=RIDGE)
            entFosterM.grid(row=3, column=1, sticky='w', padx=20, pady=10)

            lblDof = Label(fosterFrame, text='Date of Foster', font=('dejavu serif', 15, 'bold'))
            lblDof.grid(row=4, column=0, sticky='w', padx=20, pady=10)
            entDof = Entry(fosterFrame, font=('dejavu serif', 15, 'bold'), relief=RIDGE)
            entDof.grid(row=4, column=1, sticky='w', padx=20, pady=10)

            lblFosterC = Label(fosterFrame, text='Fostered Child', font=('dejavu serif', 15, 'bold'))
            lblFosterC.grid(row=5, column=0, sticky='w', padx=20, pady=10)
            entFosterC = Entry(fosterFrame, font=('dejavu serif', 15, 'bold'), relief=RIDGE)
            entFosterC.grid(row=5, column=1, sticky='w', padx=20, pady=10)

            lblChildG = Label(fosterFrame, text="Child's Gender", font=('dejavu serif', 15, 'bold'))
            lblChildG.grid(row=6, column=0, sticky='w', padx=20, pady=10)
            genderBox = ttk.Combobox(fosterFrame, width=19, font=('dejavu serif', 15, 'bold'), state='readonly')
            genderBox['values'] = ['Male', 'Female', 'Other']
            genderBox.grid(row=6, column=1, sticky='w', padx=20, pady=10)

            lblFosterCo = Label(fosterFrame, text='Contact', font=('dejavu serif', 15, 'bold'))
            lblFosterCo.grid(row=7, column=0, sticky='w', padx=20, pady=10)
            entFosterCo = Entry(fosterFrame, font=('dejavu serif', 15, 'bold'), relief=RIDGE)
            entFosterCo.grid(row=7, column=1, sticky='w', padx=20, pady=10)

            lblFosterE = Label(fosterFrame, text='Email', font=('dejavu serif', 15, 'bold'))
            lblFosterE.grid(row=8, column=0, sticky='w', padx=20, pady=10)
            entFosterE = Entry(fosterFrame, font=('dejavu serif', 15, 'bold'), relief=RIDGE)
            entFosterE.grid(row=8, column=1, sticky='w', padx=20, pady=10)

            lblFosterA = Label(fosterFrame, text='Address', font=('dejavu serif', 15, 'bold'))
            lblFosterA.grid(row=9, column=0, sticky='w', padx=20, pady=10)
            entFosterA = Entry(fosterFrame, font=('dejavu serif', 15, 'bold'), relief=RIDGE)
            entFosterA.grid(row=9, column=1, sticky='w', padx=20, pady=10)

            # foster buttons

            fosterButton = Frame(fosterFrame, bd=4, bg='red', relief=GROOVE)
            fosterButton.place(y=580, width=480)

            buttonAdd = Button(fosterButton, text='Add', bg='blue', fg='white', width=9)
            buttonAdd.grid(row=0, column=0, padx=7, pady=10)

            buttonUpdate = Button(fosterButton, text='Update', bg='blue', fg='white', width=9)
            buttonUpdate.grid(row=0, column=1, padx=10, pady=10)

            buttonDelete = Button(fosterButton, text='Delete', bg='blue', fg='white', width=9)
            buttonDelete.grid(row=0, column=2, padx=10, pady=10)

            buttonClear = Button(fosterButton, text='Clear', bg='blue', fg='white', width=9, command=Clear)
            buttonClear.grid(row=0, column=4, padx=10, pady=10)

            # foster detail

            fosterDetail = Frame(self.root, relief=RIDGE, bd=4)
            fosterDetail.place(x=480, y=77, width=885, height=640)

            lblSearch = Label(fosterDetail, text='Search By', fg='white', font=('times new roman', 20, 'bold'))
            lblSearch.grid(row=0, column=0, sticky='w', pady=10, padx=20)

            comboSearch = ttk.Combobox(fosterDetail, width=10, font=('times new roman', 15, 'bold'), state='readonly')
            comboSearch['values'] = ('ChildNo.', 'Name')
            comboSearch.grid(row=0, column=1, pady=10, padx=20)

            txtSearch = Entry(fosterDetail, width=20, font=('times new roman', 15, 'bold'), bd=5, relief=FLAT)
            txtSearch.grid(row=0, column=2, pady=10, padx=20, sticky='w')

            buttonSearch = Button(fosterDetail, text='Search', width=10)
            buttonSearch.grid(row=0, column=3, pady=10, padx=20)
            buttonShow = Button(fosterDetail, text='Show All', width=10)
            buttonShow.grid(row=0, column=4, pady=10, padx=20)

            # Show Details

            fosterFrame = Frame(fosterDetail, bd=2, relief=RAISED, bg='gray')
            fosterFrame.place(y=70, width=880, height=565)

            scrollX = Scrollbar(fosterFrame, orient=HORIZONTAL)
            scrollY = Scrollbar(fosterFrame, orient=VERTICAL)
            fosterView = ttk.Treeview(fosterFrame, columns=('fno', 'fName', 'mName', 'dof', 'fChild', 'gender',
                                                            'contact', 'email', 'address'), xscrollcommand=scrollX.set,
                                      yscrollcommand=scrollY.set)
            scrollX.pack(side=BOTTOM, fill=X)
            scrollY.pack(side=RIGHT, fill=Y)
            scrollX.config(command=fosterView.xview)
            scrollY.config(command=fosterView.yview)
            fosterView.heading('fno', text='Foster No.')
            fosterView.heading('fName', text='Foster Father')
            fosterView.heading('mName', text='Foster Mother')
            fosterView.heading('dof', text='Date of Foster')
            fosterView.heading('fChild', text='Fostered Child')
            fosterView.heading('gender', text="Gender")
            fosterView.heading('contact', text='Contact')
            fosterView.heading('email', text='Email')
            fosterView.heading('address', text='Address')
            fosterView['show'] = 'headings'
            fosterView.column('fno', width=70)
            fosterView.column('fName', width=200)
            fosterView.column('mName', width=200)
            fosterView.column('dof', width=150)
            fosterView.column('fChild', width=200)
            fosterView.column('gender', width=90)
            fosterView.column('contact', width=200)
            fosterView.column('email', width=200)
            fosterView.column('address', width=200)
            fosterView.pack(fill=BOTH, expand=1)
            fosterView.bind('<ButtonRelease-1>')

            # bottom level

            bottomLabel = Label(self.root, bg='red')
            bottomLabel.pack(side=BOTTOM, fill=X)

    root = Tk()
    Foster()
    root.mainloop()
