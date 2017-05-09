#import locale
import yaml
from Tkinter import *


def calcul (salar_brut,persoane):
    def ded(persoane):
        if salar_brut <= 1500:
            if persoane == 0:
                deducere = 300
            elif persoane == 1:
                deducere = 400
            elif persoane == 2:
                deducere = 500
            elif persoane == 3:
                deducere = 600
            else:
                deducere = 800
            return deducere
        elif salar_brut >= 1501 and salar_brut < 3000:
            if persoane == 0:
                deducere = 300*(1-((salar_brut - 1500)/1500.))
            elif persoane == 1:
                deducere = 400*(1-((salar_brut - 1500)/1500.))
            elif persoane == 2:
                deducere = 500*(1-((salar_brut - 1500)/1500.))
            elif persoane == 3:
                deducere = 600*(1-((salar_brut - 1500)/1500.))
            else:
                deducere = 800*(1-((salar_brut - 1500)/1500.))
            return round(deducere,2)
        elif salar_brut >= 3000:
            deducere = 0
            return deducere

    #print "Salar brut", salar_brut
    cas_angajat = salar_brut * 10.5 / 100
    somaj_angajat = salar_brut * 0.5 / 100
    sanatate_angajat = salar_brut * 5.5 / 100
    Impozit = 0
    if salar_brut > 0:
        Impozit = (salar_brut - cas_angajat - somaj_angajat - sanatate_angajat - ded(persoane))*16/100

    Salar_net = round(salar_brut - cas_angajat - somaj_angajat - sanatate_angajat - Impozit)
    retineri = [cas_angajat,somaj_angajat,sanatate_angajat,round(Impozit,2),ded(persoane)]
    denumire = ["Cas", "Somaj", "Asigurare sanatate", "Impozit","deducere"]
    retineri_angajat =round(cas_angajat + somaj_angajat + sanatate_angajat + Impozit)

    sanatate_angajator = salar_brut * 5.2/100
    Somaj_angajator = salar_brut * 0.5/100
    Cas_angajator = salar_brut * 15.8/100
    cci = salar_brut * 0.85/100
    Risc_accidente = salar_brut * 0.4/100
    Fond_creantesalariale = salar_brut * 0.25/100
    retineri_angajator = round(sanatate_angajator + Somaj_angajator + Cas_angajator + cci + Risc_accidente + Fond_creantesalariale)
    Suma_platita = round(salar_brut + retineri_angajator)
    return int(Salar_net),int(Suma_platita),int(retineri_angajat),int(retineri_angajator)



def total(fisier):
    salarii = 0
    contr_angajat = 0
    contr_angajator = 0
    total = 0
    with open(fisier, 'r') as file:
        f1 = yaml.load(file)
        f2 = f1['Angajati']
        for k, v in f2.iteritems():
            salarii = salarii + calcul(v['salar_brut'], v['persoane'])[0]
            contr_angajat = contr_angajat + calcul(v['salar_brut'], v['persoane'])[2]
            contr_angajator = contr_angajator +calcul(v['salar_brut'], v['persoane'])[3]
            total = total + calcul(v['salar_brut'], v['persoane'])[1]
    print "Cheltuieli salarii nete", salarii
    print "Contributii angajati", contr_angajat
    print "Contributii angajator", contr_angajator
    print "Total ch", total
    return salarii,contr_angajat,contr_angajator,total,f2,f1

def raise_frame(frame):
    frame.tkraise()

def dump_to_file(date):
    with open('Angajati.yaml', 'w') as data:
        yaml.dump(date, data, default_flow_style=False)
        data.close()

