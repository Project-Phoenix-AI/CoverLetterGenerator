
from sys import argv,exit

def get_company_name(args: list) -> str:
    '''
    Modify the company name
    :param args: commandline arguments from user
    :type args: list of strings
    :return: capitalized company name
    :rtype: string
    '''
    res = map(format_company_name,args[2:]) 
    res = list(res)
    return ' '.join(res)

def format_company_name(s):
    if len(s) <= 3:
        return s.upper()
    else:
        return s.capitalize()



if __name__ == "__main__":
    res = get_company_name(argv)
    print(res)
