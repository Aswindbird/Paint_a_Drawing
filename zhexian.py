from reportlab.graphics import renderPDF
from reportlab.graphics.shapes import Drawing,PolyLine
d = Drawing(300,300)
s1 = PolyLine([(100,100),(100,200),(200,200),(200,100),(100,100)])
s2 = PolyLine([(233,233),(267,267),(267,233),(233,267)])
d.add(s1)
d.add(s2)
renderPDF.drawToFile(d,'zhexian.pdf','A simple PDF file')