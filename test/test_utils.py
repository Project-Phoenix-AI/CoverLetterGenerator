
from sys import argv,exit
from utils import get_company_name
def test_get_company_name():
    assert get_company_name(['cover.py','ds','meta']) == 'Meta'
    assert get_company_name(['cover.py','ds','embark','studios']) == 'Embark Studios' 
    assert get_company_name(['cover.py','ds','pvh','corp.']) == 'Pvh Corp.' 
    assert get_company_name(['cover.py','ds','pvh','corp.','llc']) == 'Pvh Corp. Llc' 






