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
pdf.cell(200, 10, txt="Feszültségosztás Alapjai Kvíz", ln=True, align='C')
pdf.ln(10)

# Questions
pdf.set_font('Roboto', '', 12)

# Quiz content
quiz_questions = [
    ("1. Mi a feszültségosztó alapelve?", 
     ["A) Az áram minden ellenálláson azonos", 
      "B) Az ellenállásokon eső feszültség arányos az ellenállás értékével", 
      "C) Az áram fordítottan arányos az ellenállással", 
      "D) Az ellenállásokon eső feszültség konstans"], "B"),

    ("2. Mi történik, ha két egyenlő ellenállású komponens van sorba kötve?", 
     ["A) A teljes feszültség egyik ellenálláson esik", 
      "B) A feszültség egyenlően oszlik meg az ellenállások között", 
      "C) A feszültség nagyobb része az egyik ellenálláson esik", 
      "D) Csak az egyik ellenálláson folyik áram"], "B"),

    ("3. Melyik képlet írja le a feszültségosztó egyenletét két ellenállás esetén?", 
     ["A) V_out = V_in * (R2 / (R1 + R2))", 
      "B) V_out = V_in * (R1 / R2)", 
      "C) V_out = V_in * (R1 + R2)", 
      "D) V_out = V_in * (R2 / R1)"], "A"),

    ("4. Hogyan viszonyul az ellenállások értéke a feszültségelosztáshoz?", 
     ["A) Minél nagyobb az ellenállás, annál kisebb a rá eső feszültség", 
      "B) A nagyobb ellenállásra mindig nagyobb feszültség esik", 
      "C) Az ellenállás nem befolyásolja a feszültséget", 
      "D) A feszültség mindig aránytalanul oszlik el"], "B"),

    ("5. Hogyan viselkedik a feszültségosztó, ha az egyik ellenállás értéke nullához közelít?", 
     ["A) A teljes feszültség azon az ellenálláson esik", 
      "B) A teljes feszültség a másik ellenálláson esik", 
      "C) A feszültség arányosan oszlik meg", 
      "D) Az áram megszűnik folyni"], "B"),

    ("6. Melyik alkatrész használható tipikusan feszültségosztóként?", 
     ["A) Tranzisztor", "B) Ellenállás", "C) Kondenzátor", "D) Tekercs"], "B"),

    ("7. Milyen áramkörökben használunk gyakran feszültségosztót?", 
     ["A) Erősítők", "B) Digitális áramkörök", "C) Tápegységek", "D) Mindhárom"], "D"),

    ("8. Ha a bemeneti feszültség 12V, és két egyenlő 10Ω ellenállás van sorba kötve, mennyi lesz a kimeneti feszültség az egyik ellenálláson?", 
     ["A) 6V", "B) 12V", "C) 0V", "D) 3V"], "A"),

    ("9. Mi történik a feszültségosztó áramkörrel, ha az egyik ellenállás helyére rövidzárat teszünk?", 
     ["A) A teljes feszültség azon az ellenálláson esik, amely nincs rövidzáron", 
      "B) Az áram megszűnik", 
      "C) A teljes feszültség a rövidzáron esik", 
      "D) Az áram végtelen lesz"], "A"),

    ("10. Mi az a feszültségosztó tényező?", 
     ["A) Az áram értéke egy adott ellenálláson", 
      "B) Az ellenállások közötti arány", 
      "C) A kimeneti feszültség és a bemeneti feszültség aránya", 
      "D) Az áramkörben folyó áram nagysága"], "C")
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
    "1. B",  # 1. Mi a feszültségosztó alapelve?
    "2. B",  # 2. Mi történik, ha két egyenlő ellenállású komponens van sorba kötve?
    "3. A",  # 3. Melyik képlet írja le a feszültségosztó egyenletét két ellenállás esetén?
    "4. B",  # 4. Hogyan viszonyul az ellenállások értéke a feszültségelosztáshoz?
    "5. B",  # 5. Hogyan viselkedik a feszültségosztó, ha az egyik ellenállás értéke nullához közelít?
    "6. B",  # 6. Melyik alkatrész használható tipikusan feszültségosztóként?
    "7. D",  # 7. Milyen áramkörökben használunk gyakran feszültségosztót?
    "8. A",  # 8. Ha a bemeneti feszültség 12V, és két egyenlő 10Ω ellenállás van sorba kötve, mennyi lesz a kimeneti feszültség az egyik ellenálláson?
    "9. A",  # 9. Mi történik a feszültségosztó áramkörrel, ha az egyik ellenállás helyére rövidzárat teszünk?
    "10. C"  # 10. Mi az a feszültségosztó tényező?
]

for answer in answer_key:
    pdf.cell(0, 10, txt=answer, ln=True)

# Save the PDF to a file
file_path = "./python_quiz_standard.pdf"
pdf.output(file_path)

file_path  # Return the file path to the user
