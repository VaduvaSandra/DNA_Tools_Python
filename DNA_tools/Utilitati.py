def colorat(sec):
    bculori = {
        'A': '\033[92m',
        'C': '\033[94m',
        'G': '\033[93m',
        'T': '\033[91m',
        'U': '\033[91m',
        'reset': '\033[0,0m'
    }
    tmpStr = ""

    for nuc in sec:
        if nuc in bculori:
            tmpStr += bculori[nuc] + nuc
        else:
            tmpStr += bculori['reset'] + nuc
    return tmpStr + '\033[0;0m'