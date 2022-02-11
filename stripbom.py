"""stripbom.py: Solve the problem about BOM"""
# -*- coding: utf-8 -*-
import os
import sys

with open(sys.argv[1], 'r', encoding='utf-8') as f:
    lines = f.readlines()
    dirname, filename = os.path.split(sys.argv[1])
    file_name, extension = os.path.splitext(filename)
    
    # Create a Requirement folder
    dirname = os.path.join(dirname, "Requirement")
    try: 
        os.mkdir(dirname)
    except OSError as error:
        print(error)  
    
    new_file = os.path.join(f'{dirname}', f'{file_name}_strip{extension}')
    with open(new_file, 'a', encoding='utf-8') as ff:
        for line in lines:
            line = line.replace(chr(65279), '')
            ff.write(line)
