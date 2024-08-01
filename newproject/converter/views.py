from django.shortcuts import render
from django.http import HttpResponse
from .forms import UploadFileForm
from docx import Document
import fitz  # PyMuPDF

def pdf_to_word_view(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            pdf_file = request.FILES['file']
            docx_file = convert_pdf_to_word(pdf_file)
            response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
            response['Content-Disposition'] = f'attachment; filename="converted.docx"'
            docx_file.save(response)
            return response
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})

def convert_pdf_to_word(pdf_file):
    doc = fitz.open(stream=pdf_file.read(), filetype="pdf")
    docx_file = Document()

    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        text = page.get_text("text")
        docx_file.add_paragraph(text)
    
    return docx_file
