
from sys import argv,exit

def get_company_name(args: list) -> str:
    '''
    Modify the company name
    :param args: commandline arguments from user
    :type args: list of strings
    :return: capitalized company name
    :rtype: string
    '''
    res = map(str.capitalize,args[2:]) 
    return ' '.join(list(res))


if __name__ == "__main__":
    res = get_company_name(argv)
    print(res)
