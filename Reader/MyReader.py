
import pyttsx3
import PyPDF2,re
import epub_conversion
from epub_conversion.utils import open_book, convert_epub_to_lines
from bs4 import BeautifulSoup

import ebooklib
from ebooklib import epub

# talk function
engine = pyttsx3.init()
def talk(text):
        engine.say(text)
        engine.runAndWait()

# reader
meera='Welcome to Reader!'
# talk(meera)


# Get PDF
# loc = r"D:\SRead\\angels-and-demons.pdf"
# book = open(loc,'rb')
# reader = PyPDF2.PdfFileReader(book)
# pages = reader.numPages
# # talk('Your book has')
# # talk(pages)
# # talk('pages')
# print(pages)
# startpage = reader.getPage(10)
# # print(startpage['/Contents']['/Filter'])
# r=reader.
# print(r)
# print(startpage)

# text = startpage.extractText()
# print(startpage.extractText())
# print(text)
# talk(text)

# epub
# book2 = open_book(r"D:\SRead\\pub_angels-and-demons.epub")
# print(book2)
# lines = convert_epub_to_lines(book2)
# for sentence in lines:
#         print(sentence)
#         print('£££££££££')

# reader = PyPDF2.PdfFileReader(book)
# print(reader)
# pages = reader.numPages
# print(pages)
# startpage = reader.getPage(100)
# print(startpage)
# text = startpage.extractText()
# print(text.encode('utf-8')) 


book = epub.read_epub(r"D:\SRead\\The Monk Who Sold His Ferrari.epub")
docc=0
l=[]
for doc in book.get_items_of_type(ebooklib.ITEM_DOCUMENT):
#     print (doc.get_body_content().decode('utf-8'))
#     print('$$$$$$$$$$$$$$$')
#     print(type(doc))
    docc+=1
    l.append(doc)
print(l)
# for i in range(len(l)):
# print(l[2].get_content().decode('utf-8'))
soup = BeautifulSoup(l[20].get_content().decode('utf-8'))   
print(soup.prettify()) 
for ps in soup.find_all('p'):
        print(ps)
# for doc in book.get_items_of_type(ebooklib.ITEM_DOCUMENT):
#     print (dochttps://github.com/w3c/tidy-html5)
#     print('$$$$$$$$$$$$$$$')




# for doc in book.get_items():
#     print (doc)

# for doc in book.get_content():
#     print (doc)
    
# for doc in book.get_items_of_type(ebooklib.ITEM_IMAGE):
#     print (doc)


# for doc in book.get_items_of_type(ebooklib.ITEM_DOCUMENT):
#         for d in doc.get_content():
#                 print(d)

# converter = epub_conversion.converter.Converter(r"D:\SRead")
# print(converter)
# converter.convert(r"D:\SRead")



# tika
# from tika import parser # pip install tika

# raw = parser.from_file(r"D:\SRead\\angels-and-demons.pdf")
# print(raw['content'])