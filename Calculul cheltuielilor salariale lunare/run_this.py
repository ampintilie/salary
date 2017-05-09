import sys
import locale
import csv
from Tkinter import *
import tkMessageBox
import calcul_salar
from PIL import ImageTk,Image
import matplotlib.pyplot as plt
import numpy as np
path = '/home/ana-maria/Docs/Info/Python/PycharmProjects/Calculul cheltuielilor salariale lunare/Angajati.yaml'
file = calcul_salar.total(path)[4] #valorile cheiei Angajati
file1 = calcul_salar.total(path)[5]#dictionarul din Fisierul yaml
path_image = '/home/ana-maria/Docs/Info/Python/PycharmProjects/Calculul cheltuielilor salariale lunare/p.jpg' #imagine productivitate


#returneaza numar angajati
numar_angajati = None
def numar_a():
    global numar_angajati
    a =  len(file) #numar angajati incarcati in fisier
    numar_angajati = a
    return numar_angajati

#returneaza anul
an = None
def an_r():
    global an
    a = entry_an.get()
    an = a
    return an

#returneaza luna introdusa de utilizator
luna = None
def luna_r():
    global luna
    a = entry_luna.get()
    luna = a
    return luna

#returneaza CNP introdus pentru modificarea angajatului
cnp = None
def cnp_r():
    global cnp
    a = entry.get()
    cnp = a
    return cnp


#returneaza cnp introdus pentru stergerea angajatului
c = None
def cnp_r2():
    global c
    a = entry_c.get()
    c = a
    return c

#returneaza Cifra de afaceri introdusa
ca = None
def ca_r():
    global ca
    a = entry_CA.get()
    ca = a
    return ca

#grafic_cheltuieli totale
def grafic_cheltuieli():
    luni = []
    ch = []
    with open('Date.csv',"rU") as file:
        plots = csv.reader(file)
        for row in plots:
            if row != []:
                print row[0]
                ch.append(int(row[0]))
                luni.append(row[1])
    y = np.arange(len(luni))
    plt.bar(y,ch,align='center',alpha=0.5,color='r')
    plt.xticks(y,luni)
    plt.xlabel('Lunile anului')
    plt.ylabel('Cheltuieli salariale totale')
    plt.title('Grafic cheltuieli lunare totale')
    #plt.legend()
    plt.show()

#grafic numar angajati
def grafic_angajati():
    luni = []
    angajati = []
    with open('Numar_angajati.csv',"rU") as file:
        plots = csv.reader(file)
        for row in plots:
            if row != []:
                print row[0]
                angajati.append(int(row[0]))
                luni.append(row[1])
    y = np.arange(len(luni))
    plt.bar(y,angajati,align='center',alpha=0.5,color='r')
    plt.xticks(y,luni)
    plt.xlabel('Lunile anului')
    plt.ylabel('Numar angajati')
    plt.title('Grafic numar angajati')
    #plt.legend()
    plt.show()

#grafic productivitate anuala pe salariat
def grafic_productivitate():
    an = []
    ch = []
    with open('Productivitate.csv', "rU") as file:
        plots = csv.reader(file)
        for row in plots:
            if row != []:
                print row[0]
                ch.append(int(row[0]))
                an.append(row[1])
    y = np.arange(len(an))
    plt.bar(y, ch, align='center', alpha=0.5, color='r')
    plt.xticks(y, an)
    plt.xlabel('An')
    plt.ylabel('Cifra de afaceri')
    plt.title('Productivitate anuala pe salariat')
    # plt.legend()
    plt.show()

#incarca datele pentru graficul cu productivitatea anuala/salariat
def incarcare_csv():
    calcul = int(ca_r()) / numar_a()
    with open('Productivitate.csv', 'a') as f:
        w = csv.writer(f)
        w.writerow([calcul ,an_r()])
        mtext = "\nProductivitate anuala/salariat: %s \nAnul: %s"%(calcul,an_r())
        Label(f14, text=mtext, font=("Times New Roman", 12)).pack()
    f.close()

#scrie date in csv file pentru graficul cu cheltuielile totale
def writeToFile(calcul):
    with open('Date.csv', 'a') as f:
        w = csv.writer(f)
        w.writerow([calcul_salar.total(path)[3],luna_r()])


#sterge inputurile
def delete_entries():
    list = [entry,entry1,entry2,entry3,entry4]
    list1 = [entry5,entry6,entry7]
    for i in list:
        i.delete(0,END)
    for i in list1:
        i.delete(0, END)
        i.insert(0,int(0))


#scrie in csv datele pentru graficul numarului angajatilor
def writetofile_angajati(numar_angajati,luna):
    with open('Numar_angajati.csv', 'a') as f:
        w = csv.writer(f)
        w.writerow([numar_a(),luna_r()])


#printeaza rezultatele la calculul salariilor
def evaluate():
    mtext = "\n\n\n Luna: %s  \n\n\nRezultate: \n\n\nCheltuieli salarii nete: %s RON \nContributii angajati: %s RON \nContributii angajator: %s RON \nTotal cheltuieli cu Bugetul de Stat: %s RON \nTotal cheltuieli societate: %s RON" %(luna_r(),calcul_salar.total(path)[0],calcul_salar.total(path)[1],calcul_salar.total(path)[2],calcul_salar.total(path)[1]  + calcul_salar.total(path)[2],calcul_salar.total(path)[3])
    Label(f2,text=mtext,font=("Times New Roman",14)).pack()
    writeToFile(int(calcul_salar.total(path)[3]))
    writetofile_angajati(numar_a(),luna_r())


#adauga angajat in Angajati.yaml
def adauga_angajat():
    n1 = entry1.get()
    n2 = entry2.get()
    n3 = entry3.get()
    n4 = entry4.get()
    n5 = entry5.get()
    n6 = entry6.get()
    n7 = entry7.get()
    dict = {}
    dict1 = {}
    dict['name'] = n2
    dict['salar_brut'] = int(n3)
    dict['functie'] = n4
    dict['persoane'] = int(n5)
    dict['concediu_odihna'] = int(n6)
    dict['concediu_medical'] = int(n7)
    #dict1.update({n1:dict})
    #print dict1
    file.update({int(n1):dict})
    file1.update({"Angajati":file})
    numar_angajati = numar_a() + 1
    mtext = "\n Nume: %s,\nCNP: %s,\nSalar brut: %s,\nFunctie: %s,\nPersoane in intretinere: %s,\nConcediu odihna: %s,\nConcediu medical: %s" %(n2,n1,n3,n4,n5,n6,n7)
    Label(f6, text=mtext,font=("Times New Roman", 14)).pack()
    calcul_salar.dump_to_file(file1)
    delete_entries()

# compara CNP introdus cu datele din fisier si returneaza ce a gasit pentru "modifica angajat"
def compare(cnp):
    mtext = "\nAngajatul cu CNP-ul: %s, nu exista in baza de date!" % (cnp_r())
    for k, v in file.iteritems():
        if k == int(cnp):
            mtext = ""
            mtext1 = "Nume: %s, CNP: %s" % (v['name'],k)
            Button(f3, text=mtext1, font=("Times New Roman",13),command=lambda:calcul_salar.raise_frame(f4)).pack(fill=BOTH, pady=20)
    Label(f3, text=mtext, font=("Times New Roman", 12)).pack()


#compara CNP introdus cu datele din fisier si returneaza ce a gasit pentru "sterge angajat"
def compare1(cnp):
    cnp = cnp_r2()
    mtext = "\nAngajatul cu CNP-ul: %s, nu exista in baza de date!" % (cnp)
    for k, v in file.iteritems():
        if k == int(cnp):
            mtext = ""
            mtext1 = "Nume: %s, CNP: %s" % (v['name'],k)
            Label(f15, text=mtext1, font=("Times New Roman", 12)).pack()
    Label(f15, text=mtext, font=("Times New Roman", 12)).pack()



#functie ce modifica nume angajat
def mod_nume(cnpr):
    cnp = cnpr
    nume = entry_nume.get()
    print cnp
    print nume
    for k, v in file.iteritems():
        if k == int(cnp):
            print "Nume: %s, CNP: %s" % (v['name'], k)
            mtext = "\n Nume:%s" % (v['name'])
            Label(f7, text=mtext, font=("Times New Roman", 14)).pack()
            v['name'] = nume
            print "Nume: %s, CNP: %s" % (v['name'], k)
            file[k] = v
            print file
            file1['Angajati'] = file
            print file1
            mtext = "\n Nume nou: %s" % (v['name'])
            Label(f7, text=mtext, font=("Times New Roman", 14)).pack()
            calcul_salar.dump_to_file(file1)
            entry_nume.delete(0,END)

#functie ce modifica salarul brut
def mod_salar(cnpr):
    cnp = cnpr
    salar = entry_salar.get()
    print cnp
    print "Salar",salar
    for k, v in file.iteritems():
        if k == int(cnp):
            print "Nume %s, Salar brut: %s" % (v['name'], v['salar_brut'])
            mtext = "\n Salar brut: %s RON." % (v['salar_brut'])
            Label(f8, text=mtext, font=("Times New Roman", 14)).pack()
            v['salar_brut'] = int(salar)
            print "Salar brut: %s, CNP: %s" % (v['salar_brut'], k)
            file[k] = v
            print file
            file1['Angajati'] = file
            print file1
            mtext = "\n Salar brut modificat: %s RON." % (v['salar_brut'])
            Label(f8, text=mtext, font=("Times New Roman", 14)).pack()
            calcul_salar.dump_to_file(file1)
            entry_nume.delete(0,END)

#functie ce modifca functia de baza a angajatului
def mod_functie(cnpr):
    cnp = cnpr
    functie = entry_functie.get()
    print cnp
    for k, v in file.iteritems():
        if k == int(cnp):
            print "Nume %s, Functie de baza: %s" % (v['name'], v['functie'])
            mtext = "\n Functie:%s" % (v['functie'])
            Label(f9, text=mtext, font=("Times New Roman", 14)).pack()
            v['functie'] = functie
            print "Functie: %s, CNP: %s" % (v['functie'], k)
            file[k] = v
            print file
            file1['Angajati'] = file
            print file1
            mtext = "\n Functie noua: %s" % (v['functie'])
            Label(f9, text=mtext, font=("Times New Roman", 14)).pack()
            calcul_salar.dump_to_file(file1)
            entry_nume.delete(0,END)

#functie ce modifica numarul de persoane in intretinere
def mod_persoane(cnpr):
    cnp = cnpr
    persoane = entry_persoane.get()
    for k, v in file.iteritems():
        if k == int(cnp):
            print "Nume %s, Persoane in intretinere: %s" % (v['name'], v['persoane'])
            mtext = "\n Persoane in intretinere:%s" % (v['persoane'])
            Label(f10, text=mtext, font=("Times New Roman", 14)).pack()
            v['persoane'] = int(persoane)
            print "Persoane in intretinere: %s, CNP: %s" % (v['persoane'], k)
            file[k] = v
            print file
            file1['Angajati'] = file
            print file1
            mtext = "\n Persoane in intretinere: %s" % (v['persoane'])
            Label(f10, text=mtext, font=("Times New Roman", 14)).pack()
            calcul_salar.dump_to_file(file1)
            entry_nume.delete(0,END)


#functie ce modifica concediul medical al unei persoane
def mod_cm(cnpr):
    cnp = cnpr
    cm = entry_cm.get()
    for k, v in file.iteritems():
        if k == int(cnp):
            print "Nume %s, Concediu medical(in zile): %s" % (v['name'], v['concediu_medical'])
            mtext = "\n Concediu medical(in zile):%s" % (v['concediu_medical'])
            Label(f11, text=mtext, font=("Times New Roman", 14)).pack()
            v['concediu_medical'] = int(cm)
            print "Concediu medical: %s, CNP: %s" % (v['concediu_medical'], k)
            file[k] = v
            print file
            file1['Angajati'] = file
            print file1
            mtext = "\n Concediu medical (in zile): %s" % (v['concediu_medical'])
            Label(f11, text=mtext, font=("Times New Roman", 14)).pack()
            calcul_salar.dump_to_file(file1)
            entry_nume.delete(0,END)


#functie ce modifica concediul de odihna al unei persoane
def mod_co(cnpr):
    cnp = cnpr
    co = entry_co.get()
    for k, v in file.iteritems():
        if k == int(cnp):
            print "Nume %s, Concediu de odihna(in zile): %s" % (v['name'], v['concediu_odihna'])
            mtext = "\n Concediu de odihna(in zile): %s" % (v['concediu_odihna'])
            Label(f12, text=mtext, font=("Times New Roman", 14)).pack()
            v['concediu_odihna'] = int(co)
            print "Concediu de odihna(in zile): %s, CNP: %s" % (v['concediu_odihna'], k)
            file[k] = v
            print file
            file1['Angajati'] = file
            print file1
            mtext = "\n Concediu de odihna(in zile): %s" % (v['concediu_odihna'])
            Label(f12, text=mtext, font=("Times New Roman", 14)).pack()
            calcul_salar.dump_to_file(file1)
            entry_nume.delete(0,END)


#sterge angajat din Angajati.yaml
def sterge_angajat():
        cnp = cnp_r2()
        mtext = "\nAngajatul cu CNP-ul: %s, nu exista in baza de date!" % (cnp)
        for k, v in file.iteritems():
            if k == int(cnp):
                mtext = ""
                mtext1 = "\nAngajatul cu CNP-ul: %s, a fost sters din baza de date!" % (cnp)
                Label(f15, text=mtext1, font=("Times New Roman", 12)).pack()
                print k
                del file[int(cnp)]
                print file
                file1['Angajati'] = file
                print file1
                calcul_salar.dump_to_file(file1)
                entry_c.delete(0,END)
                break
        Label(f3, text=mtext, font=("Times New Roman", 12)).pack()





root = Tk()
root.geometry("950x800")
root.title("Cheltuieli salariale")
f1 = Frame(root)
f2 = Frame(root)
f3 = Frame(root)
f4 = Frame(root)
f5 = Frame(root)
f6 = Frame(root)
f7 = Frame(root)
f8 = Frame(root)
f9 = Frame(root)
f10 = Frame(root)
f11 = Frame(root)
f12 = Frame(root)
f13 = Frame(root)
f14 = Frame(root)
f15 = Frame(root)
for frame in (f1, f2, f3, f4, f5,f6,f7,f8,f9,f10,f11,f12,f13,f14,f15):
    frame.grid(row=0, column=0, sticky='news')


#meniu principal

Label(f1, text='Cheltuieli salariale',bg="aquamarine",fg="black",font=("Times New Roman",16),height=2,width=87).pack(fill=X)
Button(f1, text='Calcul lunar total',font=("Times New Roman",14),command=lambda:calcul_salar.raise_frame(f2)).pack(pady=15)
Button(f1,text="Adauga angajat",font=("Times New Roman",14),command=lambda:calcul_salar.raise_frame(f6)).pack()
Button(f1,text="Modifica angajat",font=("Times New Roman",14),command=lambda:calcul_salar.raise_frame(f3)).pack(pady=15)
Button(f1,text="Sterge angajat",font=("Times New Roman",14),command=lambda:calcul_salar.raise_frame(f15)).pack()
Button(f1, text='Grafice',font=("Times New Roman",14),command=lambda:calcul_salar.raise_frame(f13)).pack(pady=15)
Button(f1,text="Iesire",font=("Times New Roman",14),bg="light salmon",command=root.destroy).pack()

#genereaza cheltuieli totale

Label(f2, text='Calcul cheltuieli salariale totale',font=("Times New Roman",14),bg="aquamarine").pack(fill=BOTH)
Label(f2,text="Luna de calcul:",font=("Times New Roman",12)).pack(pady=5)
entry_luna = Entry(f2,justify=CENTER,font=("Times New Roman",12),relief=SUNKEN)
entry_luna.pack()
entry_luna.delete(0,END)
Button(f2, text='Calcul', font=("Times New Roman",14),bg="PaleGreen2",command=lambda:evaluate()).pack(pady=15)
Button(f2, text='Inapoi',bg="light grey", font=("Times New Roman",12),command=lambda:calcul_salar.raise_frame(f1)).pack(pady=10)
Button(f2,text="Iesire",font=("Times New Roman",14),bg="light salmon",command=root.destroy).pack(pady=20)


#modifica date angajat

#cauta angajat de modificat
Label(f3, text='Modificari',font=("Times New Roman",12),fg="black",bg="aquamarine").pack(fill=BOTH)
Label(f3,text="Adauga CNP:",font=("Times New Roman",12)).pack(pady=25)
entry = Entry(f3,justify=RIGHT,font=("Times New Roman",12),relief=SUNKEN)
entry.pack()
Button(f3, text='Confirma',font=("Times New Roman",12),bg='PaleGreen2', command=lambda:compare(cnp_r())).pack(pady=20)
Button(f3, text='Inapoi',font=("Times New Roman",12), bg="light grey",command=lambda:calcul_salar.raise_frame(f1)).pack(pady=20)

#selecteaza ce atribut trebuie modificat
Label(f4, text='Modificari', font=("Times New Roman", 12), fg="black", bg="aquamarine").pack()
Button(f4, text='Nume', font=("Times New Roman", 12), command=lambda: calcul_salar.raise_frame(f7)).pack(fill=BOTH,pady=5)
Button(f4, text='Salar brut', font=("Times New Roman", 12), command=lambda: calcul_salar.raise_frame(f8)).pack(fill=BOTH,pady=5)
Button(f4, text='Functie de baza:',font=("Times New Roman",12), command=lambda:calcul_salar.raise_frame(f9)).pack(fill=BOTH)
Button(f4, text='Persoane in intretinere',font=("Times New Roman",12), command=lambda:calcul_salar.raise_frame(f10)).pack(fill=BOTH,pady=5)
Button(f4, text='Concediu medical',font=("Times New Roman",12), command=lambda:calcul_salar.raise_frame(f11)).pack(fill=BOTH)
Button(f4, text='Concediu de odihna', font=("Times New Roman",12),command=lambda:calcul_salar.raise_frame(f12)).pack(fill=BOTH,pady=5)
Button(f4, text='Inapoi', font=("Times New Roman",12),command=lambda:calcul_salar.raise_frame(f3)).pack(fill=BOTH,pady=20)

#modifica nume frame
Label(f7, text="Modifica nume:", font=("Times New Roman", 12), fg="black", bg="aquamarine").pack()
entry_nume = Entry(f7, justify=LEFT, font=("Times New Roman", 12), relief=SUNKEN)
entry_nume.pack()
Button(f7, text='Confirma',font=("Times New Roman",12),bg='PaleGreen2',command=lambda:mod_nume(cnp_r())).pack(pady=10)
Button(f7, text='Inapoi', font=("Times New Roman", 12), bg='PaleGreen2',command=lambda: calcul_salar.raise_frame(f4)).pack(pady=10)
Button(f7, text='Iesire', font=("Times New Roman", 12), bg='light salmon', command=root.destroy).pack(pady=10)

#modifica salar brut frame
Label(f8,text="Modifica salar brut:",font=("Times New Roman",12),fg="black",bg="aquamarine").pack()
entry_salar = Entry(f8,justify=RIGHT,font=("Times New Roman",12),relief=SUNKEN)
entry_salar.pack()
Button(f8, text='Confirma',font=("Times New Roman",12),bg='PaleGreen2',command=lambda:mod_salar(cnp_r())).pack(pady=10)
Button(f8, text='Inapoi',font=("Times New Roman",12),bg='PaleGreen2', command=lambda:calcul_salar.raise_frame(f4)).pack(pady=10)
Button(f8, text='Iesire',font=("Times New Roman",12),bg='light salmon',command=root.destroy).pack(pady=10)

#modifica functie de baza frame
Label(f9,text="Modifica functie de baza:",font=("Times New Roman",12),fg="black",bg="aquamarine").pack()
entry_functie = Entry(f9,justify=LEFT,font=("Times New Roman",12),relief=SUNKEN)
entry_functie.pack()
Button(f9, text='Confirma',font=("Times New Roman",12),bg='PaleGreen2',command=lambda:mod_functie(cnp_r())).pack(pady=10)
Button(f9, text='Inapoi',font=("Times New Roman",12),bg='PaleGreen2', command=lambda:calcul_salar.raise_frame(f4)).pack(pady=10)
Button(f9, text='Iesire',font=("Times New Roman",12),bg='light salmon',command=root.destroy).pack(pady=10)

#modifica persoane in intretinere frame
Label(f10,text="Modifica numarul persoanelor in intretinere:",font=("Times New Roman",12),fg="black",bg="aquamarine").pack()
entry_persoane = Entry(f10,justify=RIGHT,font=("Times New Roman",12),relief=SUNKEN)
entry_persoane.pack()
Button(f10, text='Confirma',font=("Times New Roman",12),bg='PaleGreen2',command=lambda:mod_persoane(cnp_r())).pack(pady=10)
Button(f10, text='Inapoi',font=("Times New Roman",12),bg='PaleGreen2', command=lambda:calcul_salar.raise_frame(f4)).pack(pady=10)
Button(f10, text='Iesire',font=("Times New Roman",12),bg='light salmon',command=root.destroy).pack(pady=10)

#modifica concediu medical
Label(f11,text="Modifica concediu medical:",font=("Times New Roman",12),fg="black",bg="aquamarine").pack()
entry_cm = Entry(f11,justify=RIGHT,font=("Times New Roman",12),relief=SUNKEN)
entry_cm.pack()
Button(f11, text='Confirma',font=("Times New Roman",12),bg='PaleGreen2',command=lambda:mod_cm(cnp_r())).pack(pady=10)
Button(f11, text='Inapoi',font=("Times New Roman",12),bg='PaleGreen2', command=lambda:calcul_salar.raise_frame(f4)).pack(pady=10)
Button(f11, text='Iesire',font=("Times New Roman",12),bg='light salmon',command=root.destroy).pack(pady=10)

#modifica concediu de odihna
Label(f12,text="Modifica concediu de odihna:",font=("Times New Roman",12),fg="black",bg="aquamarine").pack()
entry_co = Entry(f12,justify=RIGHT,font=("Times New Roman",12),relief=SUNKEN)
entry_co.pack()
Button(f12, text='Confirma',font=("Times New Roman",12),bg='PaleGreen2',command=lambda:mod_co(cnp_r())).pack(pady=10)
Button(f12, text='Inapoi',font=("Times New Roman",12),bg='PaleGreen2', command=lambda:calcul_salar.raise_frame(f4)).pack(pady=10)
Button(f12, text='Iesire',font=("Times New Roman",12),bg='light salmon',command=root.destroy).pack(pady=10)

#adauga angajat
Label(f6, text='Adauga salariat',font=("Times New Roman",12),fg="black",bg="aquamarine").pack()
Label(f6,text="CNP:",font=("Times New Roman",12)).pack()
entry1 = Entry(f6,justify=RIGHT,font=("Times New Roman",12),relief=SUNKEN)
entry1.pack()

Label(f6,text="Adauga nume:",font=("Times New Roman",12)).pack()
entry2 = Entry(f6,justify=LEFT,font=("Times New Roman",12),relief=SUNKEN)
entry2.pack()

Label(f6,text="Salar brut:",font=("Times New Roman",12)).pack()
entry3 = Entry(f6,justify=RIGHT,font=("Times New Roman",12),relief=SUNKEN)
entry3.pack()

Label(f6,text="Functie:",font=("Times New Roman",12)).pack()
entry4 = Entry(f6,justify=LEFT,font=("Times New Roman",12),relief=SUNKEN)
entry4.pack()

Label(f6,text="Persoane in intretinere:",font=("Times New Roman",12)).pack()
x = IntVar()
entry5 = Entry(f6,text= x,justify=RIGHT,font=("Times New Roman",12),relief=SUNKEN)
x.set(0)
entry5.pack()
y = IntVar()

Label(f6,text="Concediu odihna:",font=("Times New Roman",12)).pack()
entry6 = Entry(f6,text= y,justify=RIGHT,font=("Times New Roman",12),relief=SUNKEN)
y.set(0)
entry6.pack()
z = IntVar()

Label(f6,text="Concediu medical:",font=("Times New Roman",12)).pack()
entry7 = Entry(f6,text= z,justify=RIGHT,font=("Times New Roman",12),relief=SUNKEN)
z.set(0)
entry7.pack()

Button(f6, text='Confirma',font=("Times New Roman",12),bg='PaleGreen2',command=lambda:adauga_angajat()).pack(pady=10)
Button(f6, text='Inapoi',font=("Times New Roman",12),bg='PaleGreen2', command=lambda:calcul_salar.raise_frame(f1)).pack(pady=5)
Button(f6, text='Iesire',font=("Times New Roman",12),bg='light salmon',command=root.destroy).pack(pady=10)


#genereaza grafice
Label(f13, text='Genereaza grafice',font=("Times New Roman",14),bg="aquamarine").pack(fill=BOTH)
Button(f13, text='Graficul numarului de salariati', font=("Times New Roman",14),command=lambda:grafic_angajati()).pack(pady=10)
Button(f13, text='Graficul cheltuielilor salariale lunare totale', font=("Times New Roman",14),command=lambda:grafic_cheltuieli()).pack(pady=10)
Button(f13, text='Productivitatea anuala pe salariat', font=("Times New Roman",14),command=lambda:calcul_salar.raise_frame(f14)).pack(pady=5)
Button(f13, text='Inapoi',bg="light grey", font=("Times New Roman",12),command=lambda:calcul_salar.raise_frame(f1)).pack(pady=20)
Button(f13,text="Iesire",font=("Times New Roman",14),bg="light salmon",command=root.destroy).pack()
img = ImageTk.PhotoImage(Image.open(path_image))
Label(f13,image=img).pack(pady=35)


Label(f14, text="Productivitatea anuala pe salariat",bg="aquamarine", font=("Times New Roman", 14)).pack()
Label(f14, text="Introduceti Cifra de afaceri:", font=("Times New Roman", 12)).pack()
entry_CA = Entry(f14, justify=RIGHT, font=("Times New Roman", 12), relief=SUNKEN)
entry_CA.pack()
Label(f14, text="Introduceti anul:", font=("Times New Roman", 12)).pack()
entry_an = Entry(f14, justify=RIGHT, font=("Times New Roman", 12), relief=SUNKEN)
entry_an.pack()
Button(f14, text='OK',bg="PaleGreen2", font=("Times New Roman",12),command=lambda:incarcare_csv()).pack()
Button(f14, text='Genereaza',bg="PaleGreen2", font=("Times New Roman",12),command=lambda:grafic_productivitate()).pack(pady=20)
Button(f14, text='Inapoi',bg="light grey", font=("Times New Roman",12),command=lambda:calcul_salar.raise_frame(f1)).pack()
Button(f14,text="Iesire",font=("Times New Roman",14),bg="light salmon",command=root.destroy).pack(pady=20)
entry_CA.delete(0,END)
entry_an.delete(0,END)


#sterge anagjat din baza de date
Label(f15, text='Sterge angajat',font=("Times New Roman",12),fg="black",bg="aquamarine").pack(fill=BOTH)
Label(f15,text="Adauga CNP:",font=("Times New Roman",12)).pack(pady=25)
entry_c = Entry(f15,justify=RIGHT,font=("Times New Roman",12),relief=SUNKEN)
entry_c.pack()
Button(f15, text='Confirma',font=("Times New Roman",12),bg='PaleGreen2', command=lambda:compare1(cnp_r2())).pack(pady=20)
Button(f15, text='Sterge',font=("Times New Roman",12),bg='light salmon', command=lambda:sterge_angajat()).pack()
Button(f15, text='Inapoi',font=("Times New Roman",12), bg="light grey",command=lambda:calcul_salar.raise_frame(f1)).pack(pady=20)



calcul_salar.raise_frame(f1)

root.mainloop()