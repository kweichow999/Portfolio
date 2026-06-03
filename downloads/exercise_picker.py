# https://www.youtube.com/@MatikkamatskutTube/playlists
# https://www.geogebra.org/classic

def main(course, amount):
    import random;  list, exercises, string = [], [], ""

    material = [
    ("MAY1 Luvut ja lukujonot", 357), ("MAA2 Polynomifunktiot ja -yhtälöt", 351), ("MAA3 Geometria", 325), 
    ("MAA4 Vektorit", 301), ("MAA5 Analyyttinen geometria", 354), ("MAA6 Derivaatta", 342),
    ("MAA7 Trigonometriset funktiot", 353), ("MAA8 Juuri- ja logaritmifunktiot", 343), ("MAA9 Integraalilaskenta", 316),
    ("MAA10 Todennäköisyys ja tilastot", 327), ("MAA11 Lukuteoria ja todistaminen", 299), ("MAA12 Algoritmit matematiikassa", 301),
    ("MAA13 Differentiaali- ja integraalilaskennan jatkokurssi", 297)
    ]
    
    if course == 0:
        selection = random.choice(material)
    if course >= 1 and course <= 13:
        selection = material[course - 1]

    for i in range(1, selection[1] + 1):
        list.append(i)

    random.shuffle(list)
    
    for i in range(0, amount):
        exercises.append(list.pop())

    exercises.sort()

    for i in exercises:
        string += f"{i}  "

    print(f"\n\n\n{selection[0]}\n\n{string}\n\n\n")

main(0, 5)