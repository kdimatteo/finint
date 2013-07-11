#!/usr/bin/python

from calais import Calais
import re
import sys
import os   



def main(file_name):
    #strISIN = '^[A-Z]{2}[0-9]{10}$'
    #strISIN = '^[A-Z]{2}[A-Z0-9]{10}$'
    strISIN = '([A-Z]{2}[A-Z0-9]{10})'

    #strSEDOL = '^([A-Z0-9]{6})\d$'
    strSEDOL = '\s([0-9]{7})'
    strCUSIP = '\s([0-9]{3}[a-zA-Z0-9]{6})$'

    reISIN = re.compile(strISIN)
    reSEDOL = re.compile(strSEDOL)
    reCUSIP = re.compile(strCUSIP)

    content = read_file(file_name).replace('\n','').replace('\r','').replace('\t', '')
    print 'ISINs', re.findall(strISIN, content)
    print 'SEDOLs', reSEDOL.findall(content)
    print 'CUSIPs', reCUSIP.findall(content)


def get_entities(content):
    API_KEY = os.environ['API_KEY']
    calais = Calais(API_KEY, submitter="python-calais demo")
    result = calais.analyze(content)
    result.print_entities()


def read_file(file_name):
    f = open(file_name, 'r')
    content = f.read()
    f.close()
    return content


if __name__ == "__main__":
    if(sys.argv[1] != None):
        file_name = sys.argv[1]
        main(file_name)
    else:
        print 'you must supply name of file to parse'
        