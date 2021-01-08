import collections
import csv
from typing import OrderedDict
import xmltodict
import os


def flatten_dict(y):
    out = OrderedDict()
    
    def flatten(x, name=''):
        #nested dict
        name = name.replace('profile_','')
        if type(x) is collections.OrderedDict:
            for a in x:
                flatten(x[a], name + a + '_')

        #nested list
        elif type(x) is list:
            i = 0
            for a in x:
                flatten(a,name+str(i)+'_')
                i+=1
        
        else:
            out[name[:-1]] = x

    flatten(y)
    return out

def display_title_bar():
    
    print('-------------------------------------------------------')
    print('*** This program converts your fff profile to a csv ***')
    print('-------------------------------------------------------\n\n')
    print('Instruction:')

def get_fff_profile():
    print('Put your desired fff profile into the \"profiles\" folder')
    input('Then press enter')
    
    infile_name = input('\n\nType the EXACT name of your profile excluding \".fff\"\n\t')
    infile_name += '.fff'
    return infile_name

def main():
    
    #get simplify3d fff profile
    infile_name = get_fff_profile()
    outfile_name = infile_name.strip('.fff') + '.csv'
    
    
    flatten_data = OrderedDict()
    inpath = os.path.join('profiles',infile_name)
    outpath = os.path.join('converted_csv',outfile_name) 
    while not os.path.exists(inpath):
        print(f'\nERROR :: your file \"{inpath}\" does not exist\n')
        print('-------------------------------------------------------')
        
        infile_name = get_fff_profile()
        outfile_name = infile_name.strip('.fff') + '.csv'
        
        inpath = os.path.join('profiles',infile_name)
        outpath = os.path.join('converted_csv',outfile_name) 
    
    with open(inpath,'r') as infile:
        print(f'\nParsing File: {inpath}')
        dict_data = xmltodict.parse(infile.read())
        flatten_data = flatten_dict(dict_data)
        print('Done Parsing')

    with open(outpath,'w',newline='') as outfile:
        print(f'Writing to File: {outpath}')
        writer = csv.writer(outfile)
        writer.writerow(flatten_data.keys())
        writer.writerow(flatten_data.values())
        print('Your csv is ready to import into your favorite spreadsheet software!')
        
if __name__=="__main__":
    display_title_bar()
    another = 'y'
    while another == 'y':
        main()
        print('\nDo you want to convert another profile?')
        another = input('Type \"Y\" or \"y\" if yes. otherwise press any key\n\t')
        another = another.lower()
        print('\n\n-------------------------------------------------------\n-------------------------------------------------------\n')
    exit()

    