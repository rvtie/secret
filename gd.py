import csv
from recruitments import models
from SIG.models import SIGroup

def run():
	passed=models.Resume.objects.filter(qualified_for_round=3).order_by('id')
	model = models.Resume
	writer = csv.writer(open('qualifiedGD.csv','w'))
	headers = []
	for field in model._meta.fields:
		headers.append(field.name)
	headers.append("Code")
	headers.append("Gadget")
	headers.append("Garage")
	writer.writerow(headers)
	code=SIGroup.objects.get(name="Code")
	gadget=SIGroup.objects.get(name="Gadget")
	garage=SIGroup.objects.get(name="Garage")
	resumeHeaders=headers[:-3]
	for resume in passed:
		row=[]
		codeChoice=False
		gadgetChoice=False
		garageChoice=False
		for field in resumeHeaders:
			val=getattr(resume, field)
			if callable(val):
				val=val()
			if type(val)==unicode:
				val = val.encode("utf-8")
			row.append(val)
		for choice in resume.core_sig_choice.all():
			if(choice==code):
				codeChoice=True
			if(choice==gadget):
				gadgetChoice=True	
			if(choice==garage):
				garageChoice=True
		if(codeChoice==True):
			row.append("YES")
		else:
			row.append("NO")	
		if(gadgetChoice==True):
			row.append("YES")
		else:
			row.append("NO")	
		if(garageChoice==True):
			row.append("YES")
		else:
			row.append("NO")	
		writer.writerow(row)

