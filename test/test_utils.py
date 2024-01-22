
from sys import argv,exit
from utils import get_company_name
def test_get_company_name():
    assert get_company_name(['cover.py','ds','meta']) == 'Meta'
    assert get_company_name(['cover.py','ds','embark','studios']) == 'Embark Studios' 
    assert get_company_name(['cover.py','ds','embark','studios','marketing']) == 'Embark Studios Marketing' 


def test_get_company_name_with_upper_case():
    assert get_company_name(['cover.py','ds','imc','trading']) == 'IMC Trading'
    assert get_company_name(['cover.py','ds','pvh','corp.']) == 'PVH Corp.' 
    assert get_company_name(['cover.py','ds','pvh','corp.','llc']) == 'PVH Corp. LLC' 

