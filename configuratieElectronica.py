 #! Valoarea maxima de electroni de pe fiecare orbital
orbitali = {
    '1s': 2,
    '2s': 2,
    '2p': 6,
    '3s': 2,
    '3p': 6,
    '4s': 2,
    '3d': 10,
    '4p': 6,
    '5s': 2,
    '4d': 10,
    '5p': 6,
    '6s': 2,
    '4f': 14,
    '5d': 10,
    '6p': 6,
    '7s': 2,
    '5f': 14,
    '6d': 10,
    '6f': 14,
}

#! Valoarea maxima de electroni de pe fiecare strat
straturi = {
    '1': 2,
    '2': 8,
    '3': 18,
    '4': 32,
    '5': 32,
    '6': 18,
    '7': 8
}

#! Elementele chimice
elemente = [
    # Perioada 1
    "H", "He",

    # Perioada 2
    "Li", "Be", "B", "C", "N", "O", "F", "Ne",

    # Perioada 3
    "Na", "Mg", "Al", "Si", "P", "S", "Cl", "Ar",

    # Perioada 4
    "K", "Ca", "Sc", "Ti", "V", "Cr", "Mn", "Fe", "Co", "Ni", "Cu", "Zn",
    "Ga", "Ge", "As", "Se", "Br", "Kr",

    # Perioada 5
    "Rb", "Sr", "Y", "Zr", "Nb", "Mo", "Tc", "Ru", "Rh", "Pd", "Ag", "Cd",
    "In", "Sn", "Sb", "Te", "I", "Xe",

    # Perioada 6 si lantanide
    "Cs", "Ba",
    
    "La", "Ce", "Pr", "Nd", "Pm", "Sm", "Eu", "Gd", "Tb", "Dy",
    "Ho", "Er", "Tm", "Yb", "Lu",
    
    "Hf", "Ta", "W", "Re", "Os", "Ir", "Pt",
    "Au", "Hg", "Tl", "Pb", "Bi", "Po", "At", "Rn",

    # Perioada 7 si actinide
    "Fr", "Ra", 
    
    "Ac", "Th", "Pa", "U", "Np", "Pu", "Am", "Cm", "Bk", "Cf",
    "Es", "Fm", "Md", "No", "Lr",
    
    "Rf", "Db", "Sg", "Bh", "Hs", "Mt", "Ds",
    "Rg", "Cn", "Nh", "Fl", "Mc", "Lv", "Ts", "Og"
]

#! Simbolurile elementelor chimice respectiv "m" pentru metale, "n" pentru nemetale si "gn" pentru gaze nobile
tip_elemente = {
    # Perioada 1
    "H": "n", "He": "gn",
    
    # Perioada 2
    "Li": "m", "Be": "m", "B": "n", "C": "n", "N": "n", "O": "n", "F": "n", "Ne": "gn",
    
    # Perioada 3
    "Na": "m", "Mg": "m", "Al": "m", "Si": "n", "P": "n", "S": "n", "Cl": "n", "Ar": "gn",
    
    # Perioada 4
    "K": "m", "Ca": "m", "Sc": "m", "Ti": "m", "V": "m", "Cr": "m", "Mn": "m", "Fe": "m",
    "Co": "m", "Ni": "m", "Cu": "m", "Zn": "m", "Ga": "m", "Ge": "n", "As": "n", "Se": "n",
    "Br": "n", "Kr": "gn",
    
    # Perioada 5
    "Rb": "m", "Sr": "m", "Y": "m", "Zr": "m", "Nb": "m", "Mo": "m", "Tc": "m", "Ru": "m",
    "Rh": "m", "Pd": "m", "Ag": "m", "Cd": "m", "In": "m", "Sn": "m", "Sb": "n", "Te": "n",
    "I": "n", "Xe": "gn",
    
    # Perioada 6 si lantanide
    "Cs": "m", "Ba": "m",
    
    "La": "m", "Ce": "m", "Pr": "m", "Nd": "m", "Pm": "m", "Sm": "m",
    "Eu": "m", "Gd": "m", "Tb": "m", "Dy": "m", "Ho": "m", "Er": "m", "Tm": "m", "Yb": "m",
    "Lu": "m", 
    
    "Hf": "m", "Ta": "m", "W": "m", "Re": "m", "Os": "m", "Ir": "m", "Pt": "m",
    "Au": "m", "Hg": "m", "Tl": "m", "Pb": "m", "Bi": "m", "Po": "n", "At": "n", "Rn": "gn",
    
    # Perioada 7 si actinide
    "Fr": "m", "Ra": "m",
    
    "Ac": "m", "Th": "m", "Pa": "m", "U": "m", "Np": "m", "Pu": "m",
    "Am": "m", "Cm": "m", "Bk": "m", "Cf": "m", "Es": "m", "Fm": "m", "Md": "m", "No": "m",
    "Lr": "m",
     
    "Rf": "m", "Db": "m", "Sg": "m", "Bh": "m", "Hs": "m", "Mt": "m", "Ds": "m",
    "Rg": "m", "Cn": "m", "Nh": "m", "Fl": "m", "Mc": "m", "Lv": "m", "Ts": "n", "Og": "gn"
}

#! Simbolurile elementelor chimice respectiv numarul lor de electroni
electroni_elemente = {element: electroni + 1 for electroni, element in enumerate(tip_elemente.keys())}

#! Ionii elementelor
ioni = {
    # Perioada 1
    "H": "He", "He": "He",

    # Perioada 2
    "Li": "He", "Be": "He", "B": "Ne", "C": "Ne",
    "N": "Ne", "O": "Ne", "F": "Ne", "Ne": "Ne",

    # Perioada 3
    "Na": "Ne", "Mg": "Ne", "Al": "Ne", "Si": "Ar",
    "P": "Ar", "S": "Ar", "Cl": "Ar", "Ar": "Ar",

    # Perioada 4
    "K": "Ar", "Ca": "Ar", "Sc": "Ar", "Ti": "Ar",
    "V": "Ar", "Cr": "Ar", "Mn": "Ar", "Fe": "Ar",
    "Co": "Ar", "Ni": "Ar", "Cu": "Ar", "Zn": "Ar",
    "Ga": "Ar", "Ge": "Kr", "As": "Kr", "Se": "Kr",
    "Br": "Kr", "Kr": "Kr",

    # Perioada 5
    "Rb": "Kr", "Sr": "Kr", "Y": "Kr", "Zr": "Kr",
    "Nb": "Kr", "Mo": "Kr", "Tc": "Kr", "Ru": "Kr",
    "Rh": "Kr", "Pd": "Kr", "Ag": "Kr", "Cd": "Kr",
    "In": "Kr", "Sn": "Xe", "Sb": "Xe", "Te": "Xe",
    "I": "Xe", "Xe": "Xe",

    # Perioada 6
    "Cs": "Xe", "Ba": "Xe",
    "La": "Xe", "Ce": "Xe", "Pr": "Xe", "Nd": "Xe",
    "Pm": "Xe", "Sm": "Xe", "Eu": "Xe", "Gd": "Xe",
    "Tb": "Xe", "Dy": "Xe", "Ho": "Xe", "Er": "Xe",
    "Tm": "Xe", "Yb": "Xe", "Lu": "Xe",
    "Hf": "Rn", "Ta": "Rn", "W": "Rn", "Re": "Rn",
    "Os": "Rn", "Ir": "Rn", "Pt": "Rn", "Au": "Rn",
    "Hg": "Rn", "Tl": "Rn", "Pb": "Rn", "Bi": "Rn",
    "Po": "Rn", "At": "Rn", "Rn": "Rn",

    # Perioada 7
    "Fr": "Og", "Ra": "Og",
    "Ac": "Og", "Th": "Og", "Pa": "Og", "U": "Og",
    "Np": "Og", "Pu": "Og", "Am": "Og", "Cm": "Og",
    "Bk": "Og", "Cf": "Og", "Es": "Og", "Fm": "Og",
    "Md": "Og", "No": "Og", "Lr": "Og",
    "Rf": "Og", "Db": "Og", "Sg": "Og", "Bh": "Og",
    "Hs": "Og", "Mt": "Og", "Ds": "Og", "Rg": "Og",
    "Cn": "Og", "Nh": "Og", "Fl": "Og", "Mc": "Og",
    "Lv": "Og", "Ts": "Og", "Og": "Og"
}


def configuratie_electronica_element(element):
    electroni = electroni_elemente[element]
    
    #! Configuratie pe orbitali
    orb = [] #? Limita de electroni pe fiecare orbital
    elec = [] #? Numarul de electroni pe fiecare orbital

    for orbital, capacitate in orbitali.items():
        orb.append(capacitate)
        elec.append(0)
    
    i = 0
    for e in range(electroni):
        if not elec[i] < orb[i]:
            i += 1
        elec[i] += 1
    # printListsAsDict(orb, elec)
    
    j = 0
    for i in orbitali.keys():
        # print(i, elec[j])
        j += 1
    
    # print('\n')

    #! Configuratie pe straturi
    e_strat = {}
    for i in range(7):
        e_strat[str(i + 1)] = 0
    
    for i, o in enumerate(orbitali.keys()):
        strat = o[0]
        e_strat[strat] += elec[i]
        # print(e_strat[o], elec[int(o)])
    # print(e_strat)
    
    e_orbial = {}
    for i, j in enumerate(orbitali.keys()):
        e_orbial[j] = elec[i]
    
    return e_strat, e_orbial


def ion(element):
    tip = tip_elemente[element]
    i_elem = elemente.index(element)
    
    if tip == "gn":
        return element
    
    return ioni[element]


def configuratie_electronica_ion(element):
    i = ion(element)
    config = configuratie_electronica_element(i)
    return i, config


