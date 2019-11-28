from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk, Image
import pymysql

LARGE_FONT = ("Verdana", 12)
FONT = ('new times roman', 15, 'bold')
Label_Font = ('new times roman', 15, 'bold')
Title_Font = ('new times roman', 25, 'bold')
Search_Font = ('new times roman', 20, 'bold')
Search_Index = ('new times roman', 10, 'bold')
Foster_Title = ('new times roman', 24, 'bold')


class FosterHome(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (HomePage, ManageChildren, ManageParent):
            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(HomePage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class HomePage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        tk.Frame.config(self, background='blue')
        title = Label(self, text='FOSTER HOME MANAGEMENT SYSTEM', font=Title_Font, bg='red', fg='Gray')
        title.pack(side=TOP, fill=X)

        def sExit():
            sExit = messagebox.askyesno('Foster Home Management System', 'Please Confirm System Exit!')
            if sExit > 0:
                app.destroy()
                return

        button = tk.Button(self, text="Manage Children", width=50,
                           command=lambda: controller.show_frame(ManageChildren))
        button.pack(pady=60)

        button2 = tk.Button(self, text="Manage Parents", width=50,
                            command=lambda: controller.show_frame(ManageParent))
        button2.pack(pady=60)

        button3 = tk.Button(self, text='Exit System', width=50, command=sExit)
        button3.pack(pady=60)


class ManageChildren(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        title = Label(self, text='FOSTER HOME MANAGEMENT SYSTEM', font=Title_Font, bg='red', fg='Gray')
        title.pack(side=TOP, fill=X)

        # ===============================  HOME BUTTON  ========================================/#
        button1 = tk.Button(self, text='Back to Main Window', font=FONT, bg='blue',
                            command=lambda: controller.show_frame(HomePage))
        button1.pack(side=TOP, anchor='e')

        # ===============================  VIEW FOSTER PARENTS BUTTON  ========================/#
        button2 = tk.Button(self, text='Manage Foster Parents', font=FONT, bg='blue',
                            command=lambda: controller.show_frame(ManageParent))
        button2.place(y=42)

        # ============================== EXITING SYSTEM =======================================/#
        def sExit():
            sExit = messagebox.askyesno('Foster Home Management System', 'Please Confirm System Exit!')
            if sExit > 0:
                self.destroy()
                return

        # ===============================  EXIT BUTTON  =======================================/#
        button3 = tk.Button(self, text='Exit System', font=FONT, bg='blue', command=sExit)
        button3.place(y=42, x=260)

        # ===============================  STRING VARIABLES  ==================================/#
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
        self.search_by = StringVar()
        self.search_txt = StringVar()

        all_var = cno_var.get(), gName_var.get(), mName_var.get(), sName_var.get(), mother_var.get(), \
                  father_var.get(), dob_var.get(), pob_var.get(), doa_var.get(), gender_var.get(), address_var.get()

        # ================================  Add CHILD FUNCTION =================================/#

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

        # ============================== FETCH DETAILS FUNCTION ================================/#
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

        # =============================  DISPLAY FOCUSED DETAILS ===============================/#
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

        # ==============================  UPDATING DATA  ======================================/#
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

        # ==============================  DELETING DATA  =====================================/#
        def Delete():
            con = pymysql.connect(host='localhost', user='jadrey', password='password', database='fhms')
            cur = con.cursor()
            cur.execute('delete from Children where ChildNo=%s', cno_var.get())
            con.commit()
            con.close()
            fetchDetails()
            Clear()

        # ===============================  CLEARING DATA  =====================================/#
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

        # ===============================  MANAGE CHILDREN FRAME  =============================/#
        manageFrame = Frame(self, relief=RIDGE, bd=2)
        manageFrame.place(y=77, width=480, height=640)

        # ===============================  MANAGE TITLE  ======================================/#
        manageTitle = Label(manageFrame, text='MANAGE CHILDREN', fg='white', font=Title_Font)
        manageTitle.grid(row=0, columnspan=2, pady=10, sticky='n')

        # ===============================  TEXT & ENTRIES  ====================================/#
        lblCno = Label(manageFrame, text='Child No.', font=Label_Font)
        lblCno.grid(row=1, column=0, sticky='w', padx=20, pady=10)
        entCno = Entry(manageFrame, font=Label_Font, relief=RIDGE, textvariable=cno_var)
        entCno.grid(row=1, column=1, sticky='w', padx=20, pady=5)

        lblGName = Label(manageFrame, text='Given Name:', font=Label_Font)
        lblGName.grid(row=2, column=0, sticky='w', padx=20, pady=10)
        entGName = Entry(manageFrame, font=Label_Font, relief=RIDGE, textvariable=gName_var)
        entGName.grid(row=2, column=1, sticky='w', padx=20, pady=10)

        lblMiddle = Label(manageFrame, text='Middle Name:', font=Label_Font)
        lblMiddle.grid(row=3, column=0, sticky='w', padx=20, pady=10)
        entMiddle = Entry(manageFrame, font=Label_Font, relief=RIDGE, textvariable=mName_var)
        entMiddle.grid(row=3, column=1, sticky='w', padx=20, pady=10)

        lblSurname = Label(manageFrame, text='Surname:', font=Label_Font)
        lblSurname.grid(row=4, column=0, sticky='w', padx=20, pady=10)
        entSurname = Entry(manageFrame, font=Label_Font, relief=RIDGE, textvariable=sName_var)
        entSurname.grid(row=4, column=1, sticky='w', padx=20, pady=10)

        lblMother = Label(manageFrame, text="Mother's Name:", font=Label_Font)
        lblMother.grid(row=5, column=0, sticky='w', padx=20, pady=10)
        entMother = Entry(manageFrame, font=Label_Font, relief=RIDGE, textvariable=mother_var)
        entMother.grid(row=5, column=1, sticky='w', padx=20, pady=10)

        lblFather = Label(manageFrame, text="Father's Name:", font=Label_Font)
        lblFather.grid(row=6, column=0, sticky='w', padx=20, pady=10)
        entFather = Entry(manageFrame, font=Label_Font, relief=RIDGE, textvariable=father_var)
        entFather.grid(row=6, column=1, sticky='w', padx=20, pady=10)

        lblDob = Label(manageFrame, text='Date of Birth:', font=Label_Font)
        lblDob.grid(row=7, column=0, sticky='w', padx=20, pady=10)
        entDob = Entry(manageFrame, font=Label_Font, relief=RIDGE, textvariable=dob_var)
        entDob.grid(row=7, column=1, sticky='w', padx=20, pady=10)

        lblPob = Label(manageFrame, text='Place of Birth:', font=Label_Font)
        lblPob.grid(row=8, column=0, sticky='w', padx=20, pady=10)
        entPob = Entry(manageFrame, font=Label_Font, relief=RIDGE, textvariable=pob_var)
        entPob.grid(row=8, column=1, sticky='w', padx=20, pady=10)

        lblDoa = Label(manageFrame, text='Date of Arrival:', font=Label_Font)
        lblDoa.grid(row=9, column=0, sticky='w', padx=20, pady=10)
        entDoa = Entry(manageFrame, font=Label_Font, relief=RIDGE, textvariable=doa_var)
        entDoa.grid(row=9, column=1, sticky='w', padx=20, pady=10)

        lblGender = Label(manageFrame, text='Gender:', font=Label_Font)
        lblGender.grid(row=10, column=0, sticky='w', padx=20, pady=10)
        comboG = ttk.Combobox(manageFrame, width=19, font=Label_Font, state='readonly', textvariable=gender_var)
        comboG['values'] = ['Male', 'Female', 'Other']
        comboG.grid(row=10, column=1, padx=20, pady=10)

        lblAddress = Label(manageFrame, text='Address:', font=Label_Font)
        lblAddress.grid(row=11, column=0, sticky='w', padx=20, pady=10)
        entAddress = Entry(manageFrame, font=Label_Font, relief=RIDGE, textvariable=address_var)
        entAddress.grid(row=11, column=1, sticky='w', padx=20, pady=10)

        # ===============================  CHILD BUTTON FRAME ======================================/#

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

        # ==============================  DETAILS FRAME =======================================/#

        detailFrame = Frame(self, bd=4, relief=RIDGE, bg='crimson')
        detailFrame.place(x=480, y=77, width=885, height=640)

        childrenFrame = Frame(detailFrame, bd=2, relief=RAISED, bg='gray')
        childrenFrame.place(y=70, width=880, height=565)

        scrollX = Scrollbar(detailFrame, orient=HORIZONTAL)
        scrollY = Scrollbar(detailFrame, orient=VERTICAL)
        childrenView = ttk.Treeview(detailFrame, columns=('cno', 'gName', 'mName', 'sName', 'mother',
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

        # ==============================  BOTTOM LABEL  =======================================/#
        bottomLabel = Label(self, bg='red')
        bottomLabel.pack(side=BOTTOM, fill=X)


class ManageParent(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        title = Label(self, text='FOSTER HOME MANAGEMENT SYSTEM', font=Title_Font, bg='red',
                      fg='Gray')
        title.pack(side=TOP, fill=X)

        # ===============================  HOME BUTTON  ========================================/#
        button1 = tk.Button(self, text="Back to Main Window", font=FONT, bg='blue',
                            command=lambda: controller.show_frame(HomePage))
        button1.pack(side=TOP, anchor='e')

        # ===============================  VIEW CHILDREN BUTTON  ================================/#
        button2 = tk.Button(self, text="Manage Children", font=FONT, bg='blue',
                            command=lambda: controller.show_frame(ManageChildren))
        button2.place(x=2, y=42)

        # ==============================  VARIABLES  ============================================/#
        fno_var = StringVar()
        fFather_var = StringVar()
        fMother_var = StringVar()
        dof_var = StringVar()
        fChild_var = StringVar()
        fGender_Var = StringVar()
        fContact_var = StringVar()
        fEmail_var = StringVar()
        fAddress_var = StringVar()

        # ==============================  CLEARING DATA  =======================================/#
        def fClear():
            fno_var.set('')
            fFather_var.set('')
            fMother_var.set('')
            dof_var.set('')
            fChild_var.set('')
            fGender_Var.set('')
            fContact_var.set('')
            fEmail_var.set('')
            fAddress_var.set('')

        # ==============================  EXITING SYSTEM =======================================/#
        def sExit():
            sExit = messagebox.askyesno('Foster Home Management System', 'Please Confirm System Exit!')
            if sExit > 0:
                self.destroy()
                return

        # ===============================  EXIT BUTTON  =======================================/#
        button3 = tk.Button(self, text='Exit System', font=FONT, bg='blue', command=sExit)
        button3.place(y=42, x=200)

        # ===============================  ADD PARENTS FUNCTION  ===============================/#
        def addParent():
            con = pymysql.connect(host='localhost', user='jadrey', password='password', database='fhms')
            cur = con.cursor()
            cur.execute('insert into Parent values (%s,%s,%s,%s,%s,%s,%s,%s)', (fno_var.get(),
                                                                                fFather_var.get(),
                                                                                fMother_var.get(),
                                                                                dof_var.get(),
                                                                                fChild_var.get(),
                                                                                fContact_var.get(),
                                                                                fEmail_var.get(),
                                                                                fAddress_var.get()))
            con.commit()
            fetchParent()
            fClear()
            con.close()

        # ============================== FETCH PARENT DETAILS FUNCTION ================================/#
        def fetchParent():
            con = pymysql.connect(host='localhost', user='jadrey', password='password', database='fhms')
            cur = con.cursor()
            cur.execute('select * from Parent')
            rows = cur.fetchall()
            if len(rows) != 0:
                fosterView.delete(*fosterView.get_children())
                for row in rows:
                    fosterView.insert('', END, values=row)
                    con.commit()
            con.close()

        # =============================  DISPLAY FOCUSED DETAILS ===============================/#
        def getParent(self):
            rowFocus = fosterView.focus()
            focus = fosterView.item(rowFocus)
            row = focus['values']
            print(row)
            fno_var.set(row[0])
            fFather_var.set(row[1])
            fMother_var.set(row[2])
            dof_var.set(row[3])
            fChild_var.set(row[4])
            fContact_var.set(row[5])
            fEmail_var.set(row[6])
            fAddress_var.set(row[7])

        # ==============================  UPDATING DATA  ======================================/#
        def Update():
            con = pymysql.connect(host='localhost', user='jadrey', password='password', database='fhms')
            cur = con.cursor()
            cur.execute('update Parent set FosterFather=%s, FosterMother=%s, DoF=%s, ChildNo=%s, \
                        Contact=%s, Email=%s, Address=%s where ParentNo=%s', (
                fFather_var.get(),
                fMother_var.get(),
                dof_var.get(),
                fChild_var.get(),
                fContact_var.get(),
                fEmail_var.get(),
                fAddress_var.get(),
                fno_var.get()
            ))
            con.commit()
            fetchParent()
            fClear()
            con.close()

        # ==============================  DELETING DATA  =====================================/#
        def Delete():
            messagebox.showwarning('Warning', 'You are about to delete this data')
            con = pymysql.connect(host='localhost', user='jadrey', password='password', database='fhms')
            cur = con.cursor()
            cur.execute('delete from Parent where ParentNo=%s', fno_var.get())
            con.commit()
            con.close()
            fetchParent()
            fClear()

        # ===============================  MANAGE FOSTER PARENTS ===============================/#
        fosterFrame = Frame(self, relief=RIDGE, bd=2)
        fosterFrame.place(y=77, width=480, height=640)

        # ===============================  MANAGE FOSTER PARENT TITLE  =========================/#
        fosterTitle = Label(fosterFrame, text='MANAGE FOSTER PARENTS', font=Foster_Title,
                            fg='white')
        fosterTitle.grid(row=0, columnspan=2, sticky='n', pady=10)

        # ===============================  TEXT & ENTRIES  ======================================/#

        lblFno = Label(fosterFrame, text='Foster No.', font=Label_Font)
        lblFno.grid(row=1, column=0, sticky='w', padx=20, pady=10)
        entFno = Entry(fosterFrame, font=Label_Font, relief=RIDGE, textvariable=fno_var)
        entFno.grid(row=1, column=1, sticky='w', padx=20, pady=10)

        lblFosterF = Label(fosterFrame, text='Foster Father', font=Label_Font)
        lblFosterF.grid(row=2, column=0, sticky='w', padx=20, pady=10)
        entFosterF = Entry(fosterFrame, font=Label_Font, relief=RIDGE, textvariable=fFather_var)
        entFosterF.grid(row=2, column=1, sticky='w', padx=20, pady=10)

        lblFosterM = Label(fosterFrame, text='Foster Mother', font=Label_Font)
        lblFosterM.grid(row=3, column=0, sticky='w', padx=20, pady=10)
        entFosterM = Entry(fosterFrame, font=Label_Font, relief=RIDGE, textvariable=fMother_var)
        entFosterM.grid(row=3, column=1, sticky='w', padx=20, pady=10)

        lblDof = Label(fosterFrame, text='Date of Foster', font=Label_Font)
        lblDof.grid(row=4, column=0, sticky='w', padx=20, pady=10)
        entDof = Entry(fosterFrame, font=Label_Font, relief=RIDGE, textvariable=dof_var)
        entDof.grid(row=4, column=1, sticky='w', padx=20, pady=10)

        lblFosterC = Label(fosterFrame, text="Child's Details", font=Label_Font)
        lblFosterC.grid(row=5, column=0, sticky='w', padx=20, pady=10)
        entFosterC = Entry(fosterFrame, font=Label_Font, relief=RIDGE, textvariable=fChild_var)
        entFosterC.grid(row=5, column=1, sticky='w', padx=20, pady=10)

        lblFosterCo = Label(fosterFrame, text='Contact', font=Label_Font)
        lblFosterCo.grid(row=6, column=0, sticky='w', padx=20, pady=10)
        entFosterCo = Entry(fosterFrame, font=Label_Font, relief=RIDGE, textvariable=fContact_var)
        entFosterCo.grid(row=6, column=1, sticky='w', padx=20, pady=10)

        lblFosterE = Label(fosterFrame, text='Email', font=Label_Font)
        lblFosterE.grid(row=7, column=0, sticky='w', padx=20, pady=10)
        entFosterE = Entry(fosterFrame, font=Label_Font, relief=RIDGE, textvariable=fEmail_var)
        entFosterE.grid(row=7, column=1, sticky='w', padx=20, pady=10)

        lblFosterA = Label(fosterFrame, text='Address', font=Label_Font)
        lblFosterA.grid(row=8, column=0, sticky='w', padx=20, pady=10)
        entFosterA = Entry(fosterFrame, font=Label_Font, relief=RIDGE, textvariable=fAddress_var)
        entFosterA.grid(row=8, column=1, sticky='w', padx=20, pady=10)

        # ===============================  FOSTER BUTTON FRAME ========================================/#

        fosterButton = Frame(fosterFrame, bd=4, bg='red', relief=GROOVE)
        fosterButton.place(y=580, width=480)

        buttonAdd = Button(fosterButton, text='Add', bg='blue', fg='white', width=9, command=addParent)
        buttonAdd.grid(row=0, column=0, padx=7, pady=10)

        buttonUpdate = Button(fosterButton, text='Update', bg='blue', fg='white', width=9, command=Update)
        buttonUpdate.grid(row=0, column=1, padx=10, pady=10)

        buttonDelete = Button(fosterButton, text='Delete', bg='blue', fg='white', width=9, command=Delete)
        buttonDelete.grid(row=0, column=2, padx=10, pady=10)

        buttonClear = Button(fosterButton, text='Clear', bg='blue', fg='white', width=9, command=fClear)
        buttonClear.grid(row=0, column=4, padx=10, pady=10)

        # ===============================  DETAIL FRAME  ============================================/#

        fosterDetail = Frame(self, relief=RIDGE, bd=4, bg='crimson')
        fosterDetail.place(x=480, y=77, width=885, height=640)

        fosterFrame = Frame(fosterDetail, bd=2, relief=RAISED, bg='gray')
        fosterFrame.place(y=70, width=880, height=565)

        scrollX = Scrollbar(fosterDetail, orient=HORIZONTAL)
        scrollY = Scrollbar(fosterDetail, orient=VERTICAL)
        fosterView = ttk.Treeview(fosterDetail, columns=('fno', 'fName', 'mName', 'dof', 'fChild', 'contact', 'email',
                                                         'address'), xscrollcommand=scrollX.set,
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
        fosterView.heading('contact', text='Contact')
        fosterView.heading('email', text='Email')
        fosterView.heading('address', text='Address')
        fosterView['show'] = 'headings'
        fosterView.column('fno', width=70)
        fosterView.column('fName', width=200)
        fosterView.column('mName', width=200)
        fosterView.column('dof', width=150)
        fosterView.column('fChild', width=200)
        fosterView.column('contact', width=200)
        fosterView.column('email', width=200)
        fosterView.column('address', width=200)
        fosterView.pack(fill=BOTH, expand=1)
        fosterView.bind('<ButtonRelease-1>', getParent)
        fetchParent()

        # ==================================  BOTTOM LABEL  ====================================/#
        bottomLabel = Label(self, bg='red')
        bottomLabel.pack(side=BOTTOM, fill=X)


app = FosterHome()
app.title('Foster Home Management System')
app.geometry('1365x740+0+0')
app.resizable(0, 0)
app.config(background='blue')
app.mainloop()
