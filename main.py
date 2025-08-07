from pdf2docx import Converter

if __name__ == "__main__":
    # Specify the PDF file location
    pdf_file = r"o:\Книги\Переводы\Pole A. Statistical arbitrage.. Algorithmic trading insights and techniques (Wiley, 2007)(ISBN 0470138440)(257s)_FT_.pdf"

    # Specify the output DOCX file location
    docx_file = r"o:\Книги\Переводы\Pole A. Statistical arbitrage.. Algorithmic trading insights and techniques (Wiley, 2007)(ISBN 0470138440)(257s)_FT_.docx"

    # Convert the PDF file to a DOCX file
    cv = Converter(pdf_file)
    cv.convert(docx_file)
    cv.close()
