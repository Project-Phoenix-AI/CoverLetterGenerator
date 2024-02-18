from docx import Document
from docx.shared import Pt
from sys import argv,exit
from docx2pdf import convert
import os
from utils import get_company_name

if len(argv) < 3:
    print("usage: python cover.py position(ml,ds,cs) company(company name)")
    exit(0)


if len(argv) >= 3:
    company = get_company_name(argv)

interest = {'cs':'software engineer','ml':'machine learning engineer','ds':'data scientist', 'deng':'data engineer', 'mlops':'MLOps engineer'}
positions = {'cs':'software engineering','ml':'machine learning engineering','ds':'data science','deng':'data engineering','mlops':'MLOps engineering'}

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

greetings =document.add_paragraph("Dear Hiring Manager,")


body = f'''
I am writing to express my interest in the {interest[position]} position at {company}, as advertised. With a strong background in machine learning and hands-on experience in implementing data processing workflows, developing neural networks, and applying advanced statistical analysis, I believe I am well-equipped to contribute effectively to your team.

In my role as a Junior Data Scientist at PRICER, I successfully implemented and optimized data processing workflows using Google Cloud Functions, developed and maintained data pipelines with Google BigQuery, and applied advanced statistical analysis and machine learning models to extract meaningful insights from large datasets. The opportunity to visualize findings with Qlik Sense dashboards enhanced my communication skills, making complex data accessible to R&D team.

My academic background includes pursuing an MSc in Machine Learning from KTH Royal Institute of Technology, where I acquired a solid foundation in machine learning techniques. Additionally, I have a degree in Electronics and Communication Engineering from Istanbul Technical University.

I am proud to mention that I won the TUBITAK BIGG 2021 award, an Individual Young Entrepreneur program, supporting the early incubation of OMVISION. This startup focuses on the application of deep learning in the healthcare industry, showcasing my entrepreneurial spirit and commitment to innovation.
'''

body = document.add_paragraph(body)
body.alignment = 0  # '3' corresponds to 'justify' alignment in docx

bullet_point_entry = document.add_paragraph('I have experience in:')

bullet_points = {'ml':[
                    'GCP, Google Big Query, Cloud Functions, Vertex AI, Qlik Sense',
                    'pandas, scikit-learn, keras, tensorflow, flask, seaborn, matplotlib',
                    'Github Actions, Terraform, Docker'],
                'ds':[
                    'GCP, Google Big Query, Cloud Functions, Vertex AI, Qlik Sense',
                    'pandas, scikit-learn, keras, tensorflow, flask, seaborn, matplotlib',
                    'Github Actions, Terraform, Docker'],
                'cs':[
                    'GCP, Google Big Query, Cloud Functions, Vertex AI, Qlik Sense',
                    'pandas, scikit-learn, keras, tensorflow, flask, seaborn, matplotlib',
                    'Github Actions, Terraform, Docker'],
                'deng':[
                    'GCP, Google Big Query, Cloud Functions, Vertex AI, Qlik Sense',
                    'pandas, scikit-learn, keras, tensorflow, flask, seaborn, matplotlib',
                    'Github Actions, Terraform, Docker'],
                }

for point in bullet_points[position]:
    bullet = document.add_paragraph(point)
    bullet.style = 'List Bullet'


summary =f'''
I am excited about the opportunity to bring my technical skills, innovative mindset, and passion for {positions[position]} to {company}. I am confident that my blend of academic knowledge, hands-on experience, and commitment to excellence makes me a strong candidate for this position.
Thank you for considering my application. I look forward to the opportunity to discuss how my skills and experiences align with the goals of your team.
'''
summary = document.add_paragraph(summary)

name = document.add_paragraph('Berkan Yapıcı')

company_name = company.replace(' ','_')
doc_name = f'cover_letter_{company_name}_{position}.docx'

if not os.path.exists('cover_letters/docs'):
    os.mkdir('cover_letters/docs')

if not os.path.exists('cover_letters'):
    os.mkdir('cover_letters/pdf') 

save_path = f'cover_letters/docs/{doc_name}'
document.save(save_path)
print('cover letter:', company, '\nposition:' ,positions[position])







