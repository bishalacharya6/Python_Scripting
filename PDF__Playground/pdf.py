import PyPDF2
import sys

inputs = sys.argv[1:]

def combined (pdf_lists):
	merger = PyPDF2.PdfFileMerger()
	for pdf in pdf_lists:
		merger.append(pdf)
	merger.write('super.pdf')



combined(inputs)