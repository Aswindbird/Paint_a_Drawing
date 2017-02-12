from reportlab.graphics.shapes import *
from reportlab.graphics import renderPDF
from reportlab.lib import colors
from reportlab.graphics.charts.lineplots import LinePlot
from reportlab.graphics.charts.textlabels import Label


COMMENT_CHARS = '#:'

drawing = Drawing(500,300)
data = []
f = open('predicted-sunspot-radio-flux.txt','r')
for line in f.readlines():
    if not line.isspace() and not line[0] in COMMENT_CHARS:
        data.append([float(n) for n in line.split()])
f.close()

time = [row[0]+row[1]/12.0 for row in data]
pre = [row[2] for row in data]
high = [row[3] for row in data]
low = [row[4] for row in data]

lp = LinePlot()
lp.x = 50
lp.y = 50
lp.height = 125
lp.width = 300
lp.data = [zip(time,pre),zip(time,high),zip(time,low)]
lp.lines[0].strokeColor = colors.red
lp.lines[1].strokeColor = colors.yellow
lp.lines[2].strokeColor = colors.blue

drawing.add(lp)
drawing.add(String(150,200,'Sunspot',fontSize=14,fillColor=colors.red))

renderPDF.drawToFile(drawing,'report2.pdf','Sunspots')