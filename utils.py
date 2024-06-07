
from sys import argv,exit


def get_hiring_manager_name(args: list) -> str:
    name = args[2:4]
    name = list(map(lambda x: x.capitalize(),name))
    name =' '.join(name)
    if len(name) < 4:
        return 'Dear Hiring Manager,'
    introduction = f"Dear {name},"
    return introduction
    

def get_company_name(args: list) -> str:
    '''
    Modify the company name
    :param args: commandline arguments from user
    :type args: list of strings
    :return: capitalized company name
    :rtype: string
    '''
    company_name = map(lambda x: x.upper() if len(x) <= 3 else x.capitalize(), args[4:]) 
    company_name = list(company_name)
    return ' '.join(company_name)

def name_formatter(s):
    '''
    Format the names, changes ibm -> IBM
    '''
    if len(s) < 4:
        return s.upper()
    return s.capitalize()

if __name__ == "__main__":
    print(argv[0])
    print('company name:',get_company_name(argv))
    print('hiring manager name:',get_hiring_manager_name(argv))
    f = lambda x: x.upper() if len(x) <= 3 else x.capitalize()
