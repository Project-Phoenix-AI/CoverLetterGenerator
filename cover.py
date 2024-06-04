from docx import Document
from docx.shared import Pt
from sys import argv,exit
from docx2pdf import convert
import os
from utils import get_company_name




interest = {'cs':'software engineer','ml':'machine learning engineer','ds':'data scientist', 'deng':'data engineer', 'mlops':'MLOps engineer'}
positions = {'cs':'software engineering','ml':'machine learning engineering','ds':'data science','deng':'data engineering','mlops':'MLOps engineering'}


if len(argv) >= 3:
    company = get_company_name(argv)
else:
    print(f"usage: python cover.py {list(positions.keys())} 'company name'")
    exit(0)

if argv[1] not in positions:
    print('invalid position:', argv[1], )
    print('valid positions:', list(positions.keys()))
    exit(1)

position = argv[1]

document = Document()

style = document.styles['Normal']
font = style.font
font.name = 'Calibri'#'Times New Roman'#'Calibri'
font.size = Pt(11)


greetings = document.add_paragraph("Dear Hiring Manager,")

body = f'''
I am writing to express my interest in the {interest[position]} position at {company}, as advertised. My academic background includes pursuing an MSc in Machine Learning from KTH Royal Institute of Technology, where I acquired a solid foundation in machine learning algorithms. Additionally, I have a degree in Electronics and Communication Engineering from Istanbul Technical University. 

With hands-on experience as a Data Scientist, I have implemented data processing workflows using google bigquery, cloud functions and pub/sub, developed neural networks and machine learning models for regression tasks.
'''

body = document.add_paragraph(body)
body.alignment = 0  # '3' corresponds to 'justify' alignment in docx

bullet_point_entry = document.add_paragraph('Throughout my career, I have developed expertise in:')

bullet_points = {'ml':[
                    'Google Cloud Platform (GCP), Google Big Query, Cloud Functions, Vertex AI, Qlik Sense',
                    'pandas, scikit-learn, keras, pytorch, tensorflow, flask, seaborn, matplotlib',
                    'Github Actions, Terraform, Docker'],
                'ds':[
                    'Google Cloud Platform (GCP), Google Big Query, Cloud Functions, Vertex AI, Qlik Sense',
                    'pandas, scikit-learn, keras, tensorflow, flask, seaborn, matplotlib',
                    'Github Actions, Terraform, Docker'],
                'cs':[
                    'Google Cloud Platform (GCP), Google Big Query, Cloud Functions, Vertex AI, Qlik Sense',
                    'pandas, scikit-learn, keras, tensorflow, flask, seaborn, matplotlib',
                    'Github Actions, Terraform, Docker'],
                'deng':[
                    'Google Cloud Platform (GCP), Google Big Query, Cloud Functions, Vertex AI, Qlik Sense',
                    'pandas, scikit-learn, keras, tensorflow, flask, seaborn, matplotlib',
                    'Github Actions, Terraform, Docker'],
                'all':[
                    'Google Cloud, Google Big Query, Cloud Functions, Pub/Sub, Qlik Sense',
                    'pandas, scikit-learn, keras, pytorch, tensorflow, flask, seaborn, matplotlib',
                    'Github Actions, Terraform, Docker'],
                }

for point in bullet_points['all']:
    bullet = document.add_paragraph(point)
    bullet.style = 'List Bullet'


summary =f'''
I am excited about the opportunity to bring my technical skills, innovative mindset, and passion for {positions[position]} to {company}. I am confident that my blend of academic knowledge, work experience, and commitment to excellence makes me a strong candidate for this position. Thank you for considering my application. I look forward to the opportunity to discuss how my skills and experiences can contribute to the success of your team.
'''
summmary = document.add_paragraph(summary)


name = document.add_paragraph('Berkan Yapıcı')

company_name = company.replace(' ','_')
doc_name = f'cover_letter_{company_name}_{position}.docx'


if not os.path.exists('cover_letters/docs'):
    os.mkdir('cover_letters/docs')

path = f'cover_letters/docs/{doc_name}'
document.save(path)

if not os.path.exists('cover_letters/pdfs'):
    os.mkdir('cover_letters/pdfs')
    
convert(path, f'cover_letters/pdfs/{doc_name.replace("docx","pdf")}')

print('cover letter:', company, '\nposition:' ,positions[position].capitalize())




