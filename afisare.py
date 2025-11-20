import pygame, sys, os
from configuratieElectronica import configuratie_electronica_element, configuratie_electronica_ion, electroni_elemente

# Dimensiunea casetelor
width, height = 61, 61
# Spațiere între casete
spacing = 5
# Offset inițial
x_offset = 368
y_offset = 90

# Lista elementelor pe rânduri (Perioade)
rows = [
    ["H", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "He"],  # Perioda 1
    ["Li", "Be", "", "", "", "", "", "", "", "", "", "", "B", "C", "N", "O", "F", "Ne"],  # Perioada 2
    ["Na", "Mg", "", "", "", "", "", "", "", "", "", "", "Al", "Si", "P", "S", "Cl", "Ar"],  # Perioada 3
    ["K", "Ca", "Sc", "Ti", "V", "Cr", "Mn", "Fe", "Co", "Ni", "Cu", "Zn", "Ga", "Ge", "As", "Se", "Br", "Kr"],  # Perioada 4
    ["Rb", "Sr", "Y", "Zr", "Nb", "Mo", "Tc", "Ru", "Rh", "Pd", "Ag", "Cd", "In", "Sn", "Sb", "Te", "I", "Xe"],  # Perioada 5
    ["Cs", "Ba", "", "Hf", "Ta", "W", "Re", "Os", "Ir", "Pt", "Au", "Hg", "Tl", "Pb", "Bi", "Po", "At", "Rn"],  # Perioada 6
    ["Fr", "Ra", "", "Rf", "Db", "Sg", "Bh", "Hs", "Mt", "Ds", "Rg", "Cn", "Nh", "Fl", "Mc", "Lv", "Ts", "Og"],  # Perioada 7
]

elements = {}
for row_index, row in enumerate(rows):
    for col_index, symbol in enumerate(row):
        if symbol != "":
            x = x_offset + col_index * (width + spacing)
            y = y_offset + row_index * (height + spacing)
            elements[symbol] = pygame.Rect(x, y, width, height)


def afisare(font, element, text_color, font_size, screen):
    if element == "":
        return

    # Configuratia elementului
    _, e_orbial = configuratie_electronica_element(element)
    text_element = "Element: " + element + "    " + " ".join([f"{orb}{nr}" for orb, nr in e_orbial.items() if nr > 0])
    surf_elem = font.render(text_element, True, text_color)
    rect_elem = surf_elem.get_rect(topleft=(400, 780))
    screen.blit(surf_elem, rect_elem)

    # Configuratia ionului
    ion_elem, config_ion = configuratie_electronica_ion(element)
    _, e_orbial_ion = config_ion
    text_ion = " ".join([f"{orb}{nr}" for orb, nr in e_orbial_ion.items() if nr > 0])

    # Calcul sarcina
    sarcina = electroni_elemente[element] - electroni_elemente[ion_elem]
    if abs(sarcina) != 1:
        if sarcina > 0:
            ion_text = f"{element}^+{sarcina}"
        elif sarcina < 0:
            ion_text = f"{element}^-{-sarcina}"
        else:
            ion_text = element
    else:
        if sarcina == -1:
            ion_text = f"{element}^-"
        else:
            ion_text = f"{element}^+"
            

    surf_ion = font.render(f"Ion: {ion_text}    {text_ion}", True, text_color)
    rect_ion = surf_ion.get_rect(topleft=(400, 780 + font_size + 15))
    screen.blit(surf_ion, rect_ion)


def resource_path(relative_path):
    """Returnează calea completă către fișier, indiferent dacă e rulat ca .py sau .exe."""
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)
