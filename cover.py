from docx import Document
from docx.shared import Pt
from sys import argv,exit


if len(argv) < 4:
    print("usage: python cover.py position(ml,ds,cs) company(company name)")
    exit(0)
print(len(argv))
assert len(argv) < 4 == "usage: python cover.py position(ml,ds,cs) job_type(intern,full,part) company(company name)"

position = argv[1]
if len(argv) == 5:
    company = argv[2].capitalize() + " " + argv[3]
else:
    company = argv[2].capitalize()

document = Document()

style = document.styles['Normal']
font = style.font
font.name = 'Calibri'#'Times New Roman'#'Calibri'
font.size = Pt(13)

greetings =document.add_paragraph("Dear Hiring Manager,")

interest = {'cs':'programming','ml':'applications of machine learning','ds':'machine learning'}

body = "I have graduated from Istanbul Technical University with a degree in electronics and communication engineering. "\
       "I am currently studying Msc. machine learning at KTH Royal Institute of Technology in Stockholm. "\
      f"My academic background and keen interest in {interest[position]} make me a perfect candidate for this position. "\
       "I am good at adapting to new environments and working with a team."


body = document.add_paragraph(body)

bullet_point_entry = document.add_paragraph('I have experience in:')

bullet_points = {'ml':[
                    'Python’s data science libraries like pandas, scikit-learn, keras, tensorflow.',
                    'Machine learning algorithms and applications',
                    'Java'],
                'ds':[
                    'Python’s data science libraries like pandas, scikit-learn, keras, tensorflow.',
                    'Machine learning algorithms and applications',
                    'Java',
                    'SQL'],
                'cs':[
                    'Python’s data science libraries like pandas, scikit-learn, keras, tensorflow.',
                    'Machine learning algorithms and applications',
                    'Java']
                }

for point in bullet_points[position]:
    bullet = document.add_paragraph(point)
    bullet.style = 'List Bullet'


summary =f'I believe all of these experiences will enable me to carry out a very successful job so that '\
         f'I can build an expertise in this field. I sincerely claim my aspiration to be part of the {company} without '\
         'frustrating the expectations on me throughout this journey.'
summary = document.add_paragraph(summary)

name = document.add_paragraph('Berkan Yapıcı')

doc_name = f'cover_letter_{company}.docx'
save_path = f'cover_letters/{doc_name}'
document.save(save_path)


