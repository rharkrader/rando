import PyPDF2

def main() :
    pdfFile = "C:/Users/kreegan/OneDrive/RPGs/Call_of_Cthulhu/Dreamlands.pdf"

    pdfRead = PyPDF2.PdfFileReader(pdfFile)
    if pdfRead.isEncrypted:
        print("File is encrypted")
        pdfRead.decrypt("")
    firstPage = pdfRead.getPage(0)
    pageContent = firstPage.extractText()
    print(pageContent)

if __name__ == '__main__':
    main()