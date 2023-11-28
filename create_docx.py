from docx import Document

document = Document()
document.add_heading('A simple text', level=1)
document.add_paragraph('some more text ... ')

document.save('docx_file.docx')
