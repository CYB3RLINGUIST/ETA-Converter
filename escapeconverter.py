from Tkinter import Tk
from tkFileDialog import askopenfilename
print "Welcome to the unicode escape to ASCII converter!"
print"Please specify a file:"
Tk().withdraw()
tweetfile = askopenfilename()
sampleFile = open(tweetfile, 'r').read()
splitFile = sampleFile.split('\n')
for eachLine in splitFile:
        x = eachLine.encode('utf-8')
        print x.decode('unicode-escape')