__author__ = 'rt3lpiz'

from bs4 import BeautifulSoup as bs

import Tkinter


# url='http://data.nottinghamtravelwise.org.uk/parking.xml?noLocation=true?t=635523761921130000'
# filename=wget.download(url)


soup=bs(open('parking.xml'))

app=Tkinter.Tk()
def hello():
    canvas=Tkinter.Canvas(app, width=100, height=100)
    canvas.create_text(80, 40,  text='Hello')
    canvas.pack(anchor='center')
button=Tkinter.Button(app, text='Page 1', command=hello).pack(anchor='nw')
button1=Tkinter.Button(app, text='delete', command=hello).pack(anchor='ne')

app.mainloop()
