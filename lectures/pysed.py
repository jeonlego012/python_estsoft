# command: python myscript.py -d {directory_name} -f {file_name} -find_string {origin_string} -change_string {new_string} 

import argparse
import os
import glob
import re


# read file list
def read_files(directory, filename):
    file_pattern = os.path.join(directory, filename)
    file_list = []
    
    for filepath in glob.glob(file_pattern):
        if os.path.isfile(filepath):
            file = open(filepath, 'r')
            file_list.append(file)
            
    return file_list



# change string by regular expression
def get_changed_file(file, origin_string, new_string):
    p = re.compile(origin_string)
    code = file.read()
    file.close()
    result = p.sub(new_string, code)
    return result
    

def main():
    # receive named parameter
    parser = argparse.ArgumentParser(description="this file replaces string in specific files. 'sed' command lego ver.")
    
    parser.add_argument("-d", "--directory", type=str, required=True, help="Directory name")
    parser.add_argument("-f", "--filename",type=str, default="*.*", help="File name (e.g., *.html, index.html)")
    parser.add_argument("-find_string", type=str, required=True, help="origin string")
    parser.add_argument("-change_string", type=str, required=True, help="new string")

    args = parser.parse_args()
    
    files = read_files(args.directory, args.filename)
    
    if not files:
        print(f"Failed: File '{args.directory}/{args.filename}' does not exist")
    
    for file in files:
        new_code = get_changed_file(file, args.find_string, args.change_string)
        new_file = open(file.name, "w")
        new_file.write(new_code)
        new_file.close()
        
        

if __name__ == "__main__":
    main()

