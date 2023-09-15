from fpdf import FPDF


name = input("Enter your name: ").title()

pdf = FPDF(orientation="portrait",format="A4")
pdf.add_page()
pdf.set_font("Times", "B", 30)
pdf.cell(0,20,"CS50 Shirtificate", align="C")
pdf.image("shirtificate.png", x=0.3, y=40)
pdf.set_font_size(30)
pdf.set_text_color(255,255,255)
pdf.text(x=50,y=120, txt=f"{name} took CS50")
pdf.output("shirtificate.pdf")
