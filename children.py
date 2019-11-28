if __name__ == '__main__':
    from tkinter import *
    from tkinter import ttk
    from tkinter import messagebox
    import pymysql


    class Children:
        def __init__(self):
            self.root = root
            self.root.title('FOSTER HOME MANAGEMENT SYSTEM')
            self.root.geometry('1350x700+0+0')
            self.root.config(bg='gray')

            title = Label(self.root, text='FOSTER HOME MANAGEMENT SYSTEM', font=('dejavu serif', 25, 'bold'), bg='red',
                          fg='Gray')
            title.pack(side=TOP, fill=X)

            manageFrame = Frame(self.root, relief=RIDGE, bd=2)
            manageFrame.place(y=77, width=480, height=640)

            # , bg='GRAY80'
            # Variables
            cno_var = StringVar()
            gName_var = StringVar()
            mName_var = StringVar()
            sName_var = StringVar()
            mother_var = StringVar()
            father_var = StringVar()
            dob_var = StringVar()
            pob_var = StringVar()
            doa_var = StringVar()
            gender_var = StringVar()
            address_var = StringVar()
            search_by = StringVar()
            search_txt = StringVar()

            all_var = cno_var.get(), gName_var.get(), mName_var.get(), sName_var.get(), mother_var.get(), \
                      father_var.get(), dob_var.get(), pob_var.get(), doa_var.get(), gender_var.get(), address_var.get()

            def addChild():
                if cno_var.get() == '' or gName_var.get() == '':
                    messagebox.showwarning('Warning', 'Please fill out the important fields!')
                else:
                    con = pymysql.connect(host='localhost', user='jadrey', password='password', database='fhms')
                    cur = con.cursor()
                    cur.execute('insert into Children values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)', (cno_var.get(),
                                                                                                  gName_var.get(),
                                                                                                  mName_var.get(),
                                                                                                  sName_var.get(),
                                                                                                  mother_var.get(),
                                                                                                  father_var.get(),
                                                                                                  dob_var.get(),
                                                                                                  pob_var.get(),
                                                                                                  doa_var.get(),
                                                                                                  gender_var.get(),
                                                                                                  address_var.get()))
                    con.commit()
                    fetchDetails()
                    Clear()
                    con.close()
                    messagebox.showinfo('Success', 'New data has been entered')

            def fetchDetails():
                con = pymysql.connect(host='localhost', user='jadrey', password='password', database='fhms')
                cur = con.cursor()
                cur.execute('select * from Children')
                rows = cur.fetchall()
                if len(rows) != 0:
                    childrenView.delete(*childrenView.get_children())
                    for row in rows:
                        childrenView.insert('', END, values=row)
                        con.commit()
                con.close()

            def getFocus(self):
                rowFocus = childrenView.focus()
                focus = childrenView.item(rowFocus)
                row = focus['values']
                print(row)
                cno_var.set(row[0])
                gName_var.set(row[1])
                mName_var.set(row[2])
                sName_var.set(row[3])
                mother_var.set(row[4])
                father_var.set(row[5])
                dob_var.set(row[6])
                pob_var.set(row[7])
                doa_var.set(row[8])
                gender_var.set(row[9])
                address_var.set(row[10])

            def Update():
                con = pymysql.connect(host='localhost', user='jadrey', password='password', database='fhms')
                cur = con.cursor()
                cur.execute('update Children set GivenName=%s, MiddleName=%s, Surname=%s, MothersName=%s, \
                            FathersName=%s, DoB=%s, PoB=%s, DoA=%s, Gender=%s, Address=%s where ChildNo=%s', (
                    gName_var.get(),
                    mName_var.get(),
                    sName_var.get(),
                    mother_var.get(),
                    father_var.get(),
                    dob_var.get(),
                    pob_var.get(),
                    doa_var.get(),
                    gender_var.get(),
                    address_var.get(),
                    cno_var.get()
                ))
                con.commit()
                fetchDetails()
                Clear()
                con.close()

            def Delete():
                if all_var == '':
                    messagebox.showerror('Error', 'Select field to delete')
                else:
                    messagebox.showwarning('Warning', 'You are about to delete this data')
                    con = pymysql.connect(host='localhost', user='jadrey', password='password', database='fhms')
                    cur = con.cursor()
                    cur.execute('delete from Children where ChildNo=%s', cno_var.get())
                    con.commit()
                    con.close()
                    fetchDetails()
                    Clear()

            def searchChildren():
                con = pymysql.connect(host='localhost', user='jadrey', password='password', database='fhms')
                cur = con.cursor()
                cur.execute("select ChildNo, Surname from Children where ChildNo=%s"+str(search_by.get())+"LIKE '%" +
                            str(search_txt.get())+"%'")
                rows = cur.fetchall()
                if len(rows) != 0:
                    childrenView.delete(*childrenView.get_children())
                    for row in rows:
                        childrenView.insert('', END, values=row)
                        con.commit()
                con.close()

            def sExit():
                sExit = messagebox.askyesno('Foster Home Management System', 'Please Confirm System Exit!')
                if sExit > 0:
                    root.destroy()
                    return

            exitButton = Button(self.root, text='Exit the System', font=('dejavu serif', 15, 'bold'), bg='blue',
                                fg='white', command=sExit)
            exitButton.pack(side=TOP, anchor='e')

            fosterButton = Button(self.root, text='View Foster System', font=('dejavu serif', 15, 'bold'), bg='blue',
                                  fg='white')
            fosterButton.place(y=42)

            def Clear():
                cno_var.set('')
                gName_var.set('')
                mName_var.set('')
                sName_var.set('')
                mother_var.set('')
                father_var.set('')
                dob_var.set('')
                pob_var.set('')
                doa_var.set('')
                gender_var.set('')
                address_var.set('')

            # creating the management views

            manageTitle = Label(manageFrame, text='MANAGE CHILDREN', fg='white', font=('dejavu serif', 25, 'bold'))
            manageTitle.grid(row=0, columnspan=2, pady=10, sticky='n')

            lblCno = Label(manageFrame, text='Child No.', font=('dejavu serif', 15, 'bold'))
            lblCno.grid(row=1, column=0, sticky='w', padx=20, pady=10)
            entCno = Entry(manageFrame, font=('dejavu serif', 15, 'bold'), relief=RIDGE, textvariable=cno_var)
            entCno.grid(row=1, column=1, sticky='w', padx=20, pady=5)

            lblGName = Label(manageFrame, text='Given Name:', font=('dejavu serif', 15, 'bold'))
            lblGName.grid(row=2, column=0, sticky='w', padx=20, pady=10)
            entGName = Entry(manageFrame, font=('dejavu serif', 15, 'bold'), relief=RIDGE, textvariable=gName_var)
            entGName.grid(row=2, column=1, sticky='w', padx=20, pady=10)

            lblMiddle = Label(manageFrame, text='Middle Name:', font=('dejavu serif', 15, 'bold'))
            lblMiddle.grid(row=3, column=0, sticky='w', padx=20, pady=10)
            entMiddle = Entry(manageFrame, font=('dejavu serif', 15, 'bold'), relief=RIDGE, textvariable=mName_var)
            entMiddle.grid(row=3, column=1, sticky='w', padx=20, pady=10)

            lblSurname = Label(manageFrame, text='Surname:', font=('dejavu serif', 15, 'bold'))
            lblSurname.grid(row=4, column=0, sticky='w', padx=20, pady=10)
            entSurname = Entry(manageFrame, font=('dejavu serif', 15, 'bold'), relief=RIDGE,
                               textvariable=sName_var)
            entSurname.grid(row=4, column=1, sticky='w', padx=20, pady=10)

            lblMother = Label(manageFrame, text="Mother's Name:", font=('dejavu serif', 15, 'bold'))
            lblMother.grid(row=5, column=0, sticky='w', padx=20, pady=10)
            entMother = Entry(manageFrame, font=('dejavu serif', 15, 'bold'), relief=RIDGE,
                              textvariable=mother_var)
            entMother.grid(row=5, column=1, sticky='w', padx=20, pady=10)

            lblFather = Label(manageFrame, text="Father's Name:", font=('dejavu serif', 15, 'bold'))
            lblFather.grid(row=6, column=0, sticky='w', padx=20, pady=10)
            entFather = Entry(manageFrame, font=('dejavu serif', 15, 'bold'), relief=RIDGE,
                              textvariable=father_var)
            entFather.grid(row=6, column=1, sticky='w', padx=20, pady=10)

            lblDob = Label(manageFrame, text='Date of Birth:', font=('dejavu serif', 15, 'bold'))
            lblDob.grid(row=7, column=0, sticky='w', padx=20, pady=10)
            entDob = Entry(manageFrame, font=('dejavu serif', 15, 'bold'), relief=RIDGE, textvariable=dob_var)
            entDob.grid(row=7, column=1, sticky='w', padx=20, pady=10)

            lblPob = Label(manageFrame, text='Place of Birth:', font=('dejavu serif', 15, 'bold'))
            lblPob.grid(row=8, column=0, sticky='w', padx=20, pady=10)
            entPob = Entry(manageFrame, font=('dejavu serif', 15, 'bold'), relief=RIDGE, textvariable=pob_var)
            entPob.grid(row=8, column=1, sticky='w', padx=20, pady=10)

            lblDoa = Label(manageFrame, text='Date of Arrival:', font=('dejavu serif', 15, 'bold'))
            lblDoa.grid(row=9, column=0, sticky='w', padx=20, pady=10)
            entDoa = Entry(manageFrame, font=('dejavu serif', 15, 'bold'), relief=RIDGE, textvariable=doa_var)
            entDoa.grid(row=9, column=1, sticky='w', padx=20, pady=10)

            lblGender = Label(manageFrame, text='Gender:', font=('dejavu serif', 15, 'bold'))
            lblGender.grid(row=10, column=0, sticky='w', padx=20, pady=10)
            comboG = ttk.Combobox(manageFrame, width=19, font=('dejavu serif', 15, 'bold'), state='readonly',
                                  textvariable=gender_var)
            comboG['values'] = ['Male', 'Female', 'Other']
            comboG.grid(row=10, column=1, padx=20, pady=10)

            lblAddress = Label(manageFrame, text='Address:', font=('dejavu serif', 15, 'bold'))
            lblAddress.grid(row=11, column=0, sticky='w', padx=20, pady=10)
            entAddress = Entry(manageFrame, font=('dejavu serif', 15, 'bold'), relief=RIDGE,
                               textvariable=address_var)
            entAddress.grid(row=11, column=1, sticky='w', padx=20, pady=10)

            # Button Frame

            buttonFrame = Frame(manageFrame, bd=4, bg='red', relief=GROOVE)
            buttonFrame.place(y=580, width=480)

            buttonAdd = Button(buttonFrame, text='Add', bg='blue', fg='white', width=9, command=addChild)
            buttonAdd.grid(row=0, column=0, padx=7, pady=10)

            buttonUpdate = Button(buttonFrame, text='Update', bg='blue', fg='white', width=9, command=Update)
            buttonUpdate.grid(row=0, column=1, padx=10, pady=10)

            buttonDelete = Button(buttonFrame, text='Delete', bg='blue', fg='white', width=9, command=Delete)
            buttonDelete.grid(row=0, column=2, padx=10, pady=10)

            buttonClear = Button(buttonFrame, text='Clear', bg='blue', fg='white', width=9, command=Clear)
            buttonClear.grid(row=0, column=4, padx=10, pady=10)

            # Detail Frame

            detailFrame = Frame(self.root, bd=4, relief=RIDGE, bg='crimson')
            detailFrame.place(x=480, y=77, width=885, height=640)

            lblSearch = Label(detailFrame, text='Search By', bg='crimson', fg='white',
                              font=('times new roman', 20, 'bold'))
            lblSearch.grid(row=0, column=0, sticky='w', pady=10, padx=20)

            comboSearch = ttk.Combobox(detailFrame, width=10, font=('times new roman', 15, 'bold'), state='readonly',
                                       textvariable=search_by)
            comboSearch['values'] = ('ChildNo.', 'Name')
            comboSearch.grid(row=0, column=1, pady=10, padx=20)

            txtSearch = Entry(detailFrame, width=20, font=('times new roman', 15, 'bold'), bd=5, relief=FLAT,
                              textvariable=search_txt)
            txtSearch.grid(row=0, column=2, pady=10, padx=20, sticky='w')

            buttonSearch = Button(detailFrame, text='Search', width=10, command=searchChildren)
            buttonSearch.grid(row=0, column=3, pady=10, padx=20)
            buttonShow = Button(detailFrame, text='Show All', width=10, command=fetchDetails)
            buttonShow.grid(row=0, column=4, pady=10, padx=20)

            # Show Details

            childrenFrame = Frame(detailFrame, bd=2, relief=RAISED, bg='gray')
            childrenFrame.place(y=70, width=880, height=565)

            scrollX = Scrollbar(childrenFrame, orient=HORIZONTAL)
            scrollY = Scrollbar(childrenFrame, orient=VERTICAL)
            childrenView = ttk.Treeview(childrenFrame, columns=('cno', 'gName', 'mName', 'sName', 'mother',
                                                                'father', 'dob', 'pob', 'doa', 'gender', 'address'),
                                        xscrollcommand=scrollX.set,
                                        yscrollcommand=scrollY.set)
            scrollX.pack(side=BOTTOM, fill=X)
            scrollY.pack(side=RIGHT, fill=Y)
            scrollX.config(command=childrenView.xview)
            scrollY.config(command=childrenView.yview)
            childrenView.heading('cno', text='Child No.')
            childrenView.heading('gName', text='First Name')
            childrenView.heading('mName', text='Middle Name')
            childrenView.heading('sName', text='Surname')
            childrenView.heading('mother', text="Mother's Name")
            childrenView.heading('father', text="Father's Name")
            childrenView.heading('dob', text='Date of Birth')
            childrenView.heading('pob', text='Place of Birth')
            childrenView.heading('doa', text='Date of Arrival')
            childrenView.heading('gender', text='Gender')
            childrenView.heading('address', text='Address')
            childrenView['show'] = 'headings'
            childrenView.column('cno', width=70)
            childrenView.column('gName', width=100)
            childrenView.column('mName', width=100)
            childrenView.column('sName', width=100)
            childrenView.column('mother', width=200)
            childrenView.column('father', width=200)
            childrenView.column('dob', width=100)
            childrenView.column('pob', width=200)
            childrenView.column('doa', width=100)
            childrenView.column('gender', width=70)
            childrenView.column('address', width=200)
            childrenView.pack(fill=BOTH, expand=1)
            childrenView.bind('<ButtonRelease-1>', getFocus)
            fetchDetails()

            # Bottom label

            bottomLabel = Label(self.root, bg='red')
            bottomLabel.pack(side=BOTTOM, fill=X)

    root = Tk()
    Children()
    root.mainloop()
