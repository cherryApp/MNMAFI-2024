from fpdf import FPDF

# Using the default font but removing bold for compatibility
pdf = FPDF()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.add_page()

# Use default font without bold to avoid encoding issues
pdf.add_font('Roboto', '', 'Roboto-Medium.ttf', uni=True)
pdf.add_font('RobotoBold', '', 'Roboto-Bold.ttf', uni=True)
pdf.set_font('Roboto', '', 12)

# Title
pdf.set_font('RobotoBold', '', 16)
pdf.cell(200, 10, txt="Python Programozás Alapjai Kvíz", ln=True, align='C')
pdf.ln(10)

# Questions
pdf.set_font('Roboto', '', 12)

# Quiz content
quiz_questions = [
    ("1. Melyik kulcsszóval lehet egy függvényből visszatérni?", 
     ["A) return", "B) break", "C) continue", "D) pass"], "A"),
    
    ("2. Melyik adattípus nincs a Pythonban?", 
     ["A) int", "B) float", "C) char", "D) list"], "C"),
    
    ("3. Hogyan deklarálunk üres listát Pythonban?", 
     ["A) empty[]", "B) empty()", "C) []", "D) {}"], "C"),
    
    ("4. Melyik az igaz a Python függvényekre?", 
     ["A) A függvények visszatérési értékkel kell rendelkezniük", 
      "B) Egy függvény nem hívhat meg másik függvényt", 
      "C) A függvények lambda formában is létrehozhatók", 
      "D) A függvények mindig argumentumot kérnek"], "C"),
    
    ("5. Mi történik, ha a Pythonban 0-val osztunk?", 
     ["A) 0", "B) Végtelen", "C) ZeroDivisionError", "D) SyntaxError"], "C"),
    
    ("6. Hogyan hozunk létre egy Python osztály példányát?", 
     ["A) class MyClass()", "B) obj = new MyClass()", "C) obj = MyClass()", "D) obj = MyClass"], "C"),
    
    ("7. Mi lesz az alábbi kódrészlet kimenete? print('Hello' + 'World')", 
     ["A) Hello World", "B) Hello+World", "C) HelloWorld", "D) SyntaxError"], "C"),
    
    ("8. Melyik metódus használható a Python fájlok olvasására?", 
     ["A) open()", "B) read()", "C) write()", "D) load()"], "B"),
    
    ("9. Mi a különbség a lista és a tuple között Pythonban?", 
     ["A) A tuple nem tartalmazhat karaktereket", 
      "B) A lista nem módosítható, a tuple igen", 
      "C) A tuple módosíthatatlan, a lista módosítható", 
      "D) Nincs különbség"], "C"),
    
    ("10. Melyik Python könyvtár használatos adatkezelésre?", 
     ["A) numpy", "B) pandas", "C) math", "D) random"], "B"),
    
    ("11. Mi az '__init__' metódus szerepe Pythonban?", 
     ["A) Az osztály adattagjait inicializálja", 
      "B) Egy osztályhoz tartozó függvényeket deklarálja", 
      "C) Hibakezelést valósít meg", 
      "D) Egy osztály példányainak létrehozására szolgál"], "A"),
    
    ("12. Mi történik az alábbi kódrészlettel? x = [1, 2, 3]; print(x[3])", 
     ["A) 3", "B) IndexError", "C) None", "D) 1"], "B"),
    
    ("13. Hogyan definiálunk Pythonban lambda függvényt?", 
     ["A) lambda x: x + 2", "B) def lambda x: x + 2", "C) func(x): x + 2", "D) lambda(x) -> x + 2"], "A"),
    
    ("14. Melyik modul szükséges a véletlenszám generáláshoz?", 
     ["A) random", "B) os", "C) math", "D) sys"], "A"),
    
    ("15. Mi lesz a kimenet? print(bool(0))", 
     ["A) True", "B) False", "C) Error", "D) 0"], "B"),
    
    ("16. Melyik metódust használjuk Pythonban a sztringek feldarabolásához?", 
     ["A) join()", "B) split()", "C) partition()", "D) cut()"], "B"),
    
    ("17. Hogyan módosítunk egy globális változót egy Python függvényben?", 
     ["A) global változó", "B) define változó", "C) változó = global", "D) set változó"], "A"),
    
    ("18. Mi lesz az alábbi kódrészlet kimenete? print(type([1, 2, 3]))", 
     ["A) tuple", "B) list", "C) array", "D) set"], "B"),
    
    ("19. Melyik kulcsszóval lehet hibát kezelni Pythonban?", 
     ["A) raise", "B) try", "C) catch", "D) except"], "D"),
    
    ("20. Melyik adattípusnak nincs fix mérete Pythonban?", 
     ["A) int", "B) str", "C) list", "D) tuple"], "C")
]

for question, options, _ in quiz_questions:
    pdf.multi_cell(0, 10, txt=question)
    for option in options:
        pdf.cell(0, 10, txt=option, ln=True)
    pdf.ln(5)

# Add new page for answer key
pdf.add_page()
pdf.set_font('RobotoBold', '', 16)
pdf.cell(200, 10, txt="Javítókulcs", ln=True, align='C')
pdf.ln(10)

# Answer key
pdf.set_font('Roboto', '', 12)

# Answer key content
answer_key = [
    "1. A",  # 1. Melyik kulcsszóval lehet egy függvényből visszatérni?
    "2. C",  # 2. Melyik adattípus nincs a Pythonban?
    "3. C",  # 3. Hogyan deklarálunk üres listát Pythonban?
    "4. C",  # 4. Melyik az igaz a Python függvényekre?
    "5. C",  # 5. Mi történik, ha a Pythonban 0-val osztunk?
    "6. C",  # 6. Hogyan hozunk létre egy Python osztály példányát?
    "7. C",  # 7. Mi lesz az alábbi kódrészlet kimenete? print('Hello' + 'World')
    "8. B",  # 8. Melyik metódus használható a Python fájlok olvasására?
    "9. C",  # 9. Mi a különbség a lista és a tuple között Pythonban?
    "10. B",  # 10. Melyik Python könyvtár használatos adatkezelésre?
    "11. A",  # 11. Mi az '__init__' metódus szerepe Pythonban?
    "12. B",  # 12. Mi történik az alábbi kódrészlettel? x = [1, 2, 3]; print(x[3])
    "13. A",  # 13. Hogyan definiálunk Pythonban lambda függvényt?
    "14. A",  # 14. Melyik modul szükséges a véletlenszám generáláshoz?
    "15. B",  # 15. Mi lesz a kimenet? print(bool(0))
    "16. B",  # 16. Melyik metódust használjuk Pythonban a sztringek feldarabolásához?
    "17. A",  # 17. Hogyan módosítunk egy globális változót egy Python függvényben?
    "18. B",  # 18. Mi lesz az alábbi kódrészlet kimenete? print(type([1, 2, 3]))
    "19. D",  # 19. Melyik kulcsszóval lehet hibát kezelni Pythonban?
    "20. C"   # 20. Melyik adattípusnak nincs fix mérete Pythonban?
]


for answer in answer_key:
    pdf.cell(0, 10, txt=answer, ln=True)

# Save the PDF to a file
file_path = "./python_quiz_standard.pdf"
pdf.output(file_path)

file_path  # Return the file path to the user
