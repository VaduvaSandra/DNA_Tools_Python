from IntrumenteADN import *
from Utilitati import colorat
import random

#Creem o secventa random de generare a secventelor ADN

randADNStr = ''.join([random.choice(Nucleotide) for nuc in range(50)])

print(f'\nSecventa: {colorat(randADNStr)}\n')

print(f'[1]: Lungimea secventei: {len(randADNStr)}\n')

print(f'[2]: Frecventa Nucleotidelor : {NumaraNucleotidele(randADNStr)}\n')

print(f'[3]: Transcriptia ADN->ARN: {colorat(Transcriptie(randADNStr))}\n ')

print(f"[4] : Secventa ADN + Complementul Invers:\n5'{colorat(randADNStr)} 3'")

print(f"  {''.join('|' for c in range(len(randADNStr)))}")

print(f"3'{colorat(complement_invers(randADNStr)[::-1])} 5' [Complement]")

print(f"5'{colorat(complement_invers(randADNStr))} 3' [Complement invers]\n")

print(f'[5] : Continutul GC : {continut_gc(randADNStr)}%\n')

print(f'[6] : Complementul GC in subsecvente k=5: {continut_gc_subsec(randADNStr, k=5)}\n')

print(f'[7] : Secventa de aminoacizi din ADN: {transcriere_sec(randADNStr)}\n')

print('[8] : Citire_cadre:')
for cadru in gen_cadru_citire(randADNStr):
    print(cadru)

print('\n[9]: Toate proteinele in 6 cadre de citire deschise:')
for prot in toate_proteinele_din_occs(NM_000207_3, 0, 0, True):
    print(f'{prot}')