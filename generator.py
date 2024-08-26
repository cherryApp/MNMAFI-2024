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
    ("1. Melyik a helyes szintaxis egy 'for' ciklusra Pythonban?",
     ["A) for x in range(6)", "B) for(int x=0; x<6; x++)", "C) foreach(x in range(6))", "D) loop x in range(6)"], "A"),
    ("2. Melyik adattípus nincs a Pythonban?",
     ["A) int", "B) float", "C) char", "D) list"], "C"),
    ("3. Milyen eredményt ad a következő kifejezés: 3 + 2 * 2?",
     ["A) 10", "B) 7", "C) 8", "D) 9"], "B"),
    ("4. Melyik függvénnyel tudunk egy karakterláncot egész számmá konvertálni Pythonban?",
     ["A) str()", "B) float()", "C) int()", "D) convert()"], "C"),
    ("5. Mi a különbség a '==' és a '=' operátorok között?",
     ["A) Nincs különbség", "B) A '==' hozzárendelés, az '=' összehasonlítás",
      "C) Az '=' hozzárendelés, a '==' összehasonlítás", "D) Mindkettő logikai operátor"], "C"),
    ("6. Hogyan hozunk létre üres listát Pythonban?",
     ["A) []", "B) list()", "C) {}", "D) empty[]"], "A"),
    ("7. Melyik metódus használható egy lista hosszának megállapítására?",
     ["A) count()", "B) len()", "C) size()", "D) length()"], "B"),
    ("8. Mi lesz az eredménye a következő kódnak? print('Hello'[-1])",
     ["A) H", "B) o", "C) Error", "D) üres karakter"], "B"),
    ("9. Melyik kulcsszó használható Pythonban függvény definiálására?",
     ["A) function", "B) def", "C) func", "D) define"], "B"),
    ("10. Melyik ciklus használható, ha nem tudjuk előre, hányszor kell futnia?",
     ["A) for", "B) foreach", "C) while", "D) repeat"], "C")
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
    "1. A", "2. C", "3. B", "4. C", "5. C",
    "6. A", "7. B", "8. B", "9. B", "10. C"
]

for answer in answer_key:
    pdf.cell(0, 10, txt=answer, ln=True)

# Save the PDF to a file
file_path = "./python_quiz_standard.pdf"
pdf.output(file_path)

file_path  # Return the file path to the user
