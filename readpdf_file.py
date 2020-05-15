# this program extracts text from a pdf file and stores it on a string which then later
# allows us to do search for a particular word that we're looking for

import PyPDF2
p = open("meetingminutes.pdf", "rb")
p_reader = PyPDF2.PdfFileReader(p)
page = p_reader.getPage(1)
str1 = page.extractText()
print("The contents of the pages are : ", str1)
print("Enter word you want to find from the above content:")
while True:
    w = input()

    if w in str1:
        print("{} found.".format(w))

    else:
        print("{} not found.".format(w))
        break

p.close()



