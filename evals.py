import csv
from recruitments import models
from SIG.models import SIGroup

def run():
	passed=models.Resume.objects.filter(qualified_for_round=3).order_by('id')
        model = models.Resume
	codeWriter = csv.writer(open('codeQualifiedGDEvals.csv','w'))
	garageWriter = csv.writer(open('garageQualifiedGDEvals.csv','w'))
	gadgetWriter = csv.writer(open('gadgetQualifiedGDEvals.csv','w'))
	headers = []
	for field in model._meta.fields:
		headers.append(field.name)
	codeWriter.writerow(headers)
	gadgetWriter.writerow(headers)
	garageWriter.writerow(headers)
	code=SIGroup.objects.get(name="Code")
	gadget=SIGroup.objects.get(name="Gadget")
	garage=SIGroup.objects.get(name="Garage")
	for resume in passed:
		row=[]
		PIeval=resume.resume.filter(current_round="Group Discussion")
                if PIeval is None:
                    print "This isnt working."
                for evaluation in PIeval:
			val=getattr(resume, field)
			if callable(val):
				val=val()
			if type(val)==unicode:
				val = val.encode("utf-8")
			row.append(val)
		for choice in resume.core_sig_choice.all():
			if(choice==code):
			        codeWriter.writerow(row)
                        if(choice==gadget):
				gadgetWriter.writerow(row)	
			if(choice==garage):
				garageWriter.writerow(row)
