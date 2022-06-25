from Structuri import *
from collections import Counter
import random

# Ne asiguram ca secventa data este o secventa ADN
def Secventavalidata(adn_sec):
    tmpsec = adn_sec.upper()
    for nuc in tmpsec:
        if nuc not in Nucleotide:
            return False
    return tmpsec

def NumaraNucleotidele(sec):
    tmpFrecDic = {"A": 0, "C": 0, "G": 0, "T": 0}
    for nuc in sec:
        tmpFrecDic[nuc] += 1
    return tmpFrecDic


def Transcriptie(sec):
    #ADN -> ARN
    return sec.replace("T", "U")

def complement_invers(sec):
    return ''.join([ComplementulInvers_ADN[nuc] for nuc in sec])[::-1]

def continut_gc(sec):
    "Continutul GC intr-o secventa ADN/ARN"
    return round(sec.count('C') + sec.count('G') / len(sec) * 100)

def continut_gc_subsec(sec, k=20):
    res = []
    for i in range(0, len(sec) - k+1, k):
        subsec = sec[i:i + k]
        res.append(continut_gc(subsec))
    return res

def transcriere_sec(sec, pos_init=0):
    "Transcriu o secventa ADN intr-o secventa de aminoacid"
    return [ADN_Codoni[sec[pos:pos+3]] for pos in range(pos_init, len(sec) -2, 3)]

def gen_cadru_citire(sec):
    "O modalitate de a diviza secventa de nucleotide intr-o molecula de acid nucleic intr-un set de triplete consecutive, care nu se suprapun "
    cadre = []
    cadre.append(transcriere_sec(sec, 0))
    cadre.append(transcriere_sec(sec, 1))
    cadre.append(transcriere_sec(sec, 2))
    cadre.append(transcriere_sec(complement_invers(sec), 0))
    cadre.append(transcriere_sec(complement_invers(sec), 1))
    cadre.append(transcriere_sec(complement_invers(sec), 2))
    return cadre

def proteine_din_cc(aa_sec):
    "Calculeaza toate posibilele proteine intr-o secventa de aminoacizi si returneaza o lista a posibilelor proteine"
    prot_actuala = []
    proteine = []
    for aa in aa_sec:
        if aa == "_":
            #Se opreste din acumularea de aminoacizi daca _ - STOP a fost gasit
            if prot_actuala:
                for p in prot_actuala:
                    proteine.append(p)
                prot_actuala = []
        else:
            #Incepe acumularea de aminoacizi daca M- START  a fost gasit
            if aa == "M":
                prot_actuala.append("")
            for i in range(len(prot_actuala)):
                prot_actuala[i] += aa
    return proteine

def toate_proteinele_din_occs(sec, startCitirePoz = 0, sfarsitCitirePoz = 0, ordonat =False):
    "Calculeaza totate posibilele proteine din toate cadrele de citire"
    if sfarsitCitirePoz > startCitirePoz:
        ccs = gen_cadru_citire(sec[startCitirePoz : sfarsitCitirePoz])
    else:
        ccs = gen_cadru_citire(sec)

    res = []
    for cc in ccs:
        prot = proteine_din_cc(cc)
        for p in prot:
            res.append(p)

    if ordonat:
        return sorted(res, key=len, reverse=True)
    return res



