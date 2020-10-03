import pyttsx3
import PyPDF2
speaker = pyttsx3.init()
book = open('Data structures using c.pdf','rb')
reader=PyPDF2.PdfFileReader(book)
pages = reader.numPages
print(pages)
speaker.say("patrl londu h tu")
speaker.runAndWait()