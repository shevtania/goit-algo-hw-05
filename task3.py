import argparse
from pathlib import Path
from collections import Counter

# parsing 1 line from log-file with help .split in dict. Message is obtained as list, and it joined in string 
# with help map
def parse_log_line(line: str) -> dict:
    return {'date':line.split()[0],
            'time':line.split()[1],
            'level':line.split()[2],
            'message': ' '.join(map(str,line.split()[3:]))}

# function for loading logs. File is read as list of lines
def load_logs(file_path: str) -> list:
    lines = [] # list of lines
    parsed_lines_list = [] # list of dicts after patsing
    try:
        with open(Path(file_path), "r") as file:
            lines = file.readlines()
    except FileNotFoundError:
        print('File not found.') 
    except PermissionError:
        print('Permission  denied.')       
    except IOError:
        print("Cann't open file.")

    for line in lines:
        parsed_lines_list.append(parse_log_line(line)) # call the function parse_log_line(line) and append it in returned list 

    return parsed_lines_list    

# filter for logging level
def filter_logs_by_level(logs: list, level: str) -> list:
    levels_list = []
    for log in logs:
        if log['level'] == level.upper(): # we exclude pair k,v from dict with level == needed level  
            log.pop('level')
            levels_list.append(log) # append dict with len(dict) = 3 in list
    return levels_list            

# counting multiplicity of entry for every log with help Counter
def count_logs_by_level(logs: list) -> dict:
    count_dict = Counter()
    for log_dict in logs:
        count_dict[log_dict['level']] += 1
        
    return count_dict

# building table for printing result dict
def display_log_counts(counts: dict):
    s = "Рівень логування"
    t = " | "
    r = "Кількість"
    print(s,t,r)
    print("_" * (len(s) + len(t) + len(r)))
    for key, value in counts.items():
        print("{:<{}}{}{:<}".format(key, len(s) + 1, t, value))

def main():

# with help library argparse find filename as positional argument and logging level as optional argument
    parser = argparse.ArgumentParser()
    parser.add_argument("filename", help='Path to analized log file')
    # one optional argument with 4 choices. "-l" - short version, "--log_level" - long
    parser.add_argument("-l", "--log_level", help="level of logging you need", choices=['info', 'debug', 'warning', 'error'])
    args = parser.parse_args()

    logs = load_logs(args.filename)
    
    display_log_counts(count_logs_by_level(logs))
    # if optional argument is present, we print all information for this logging level 
    if args.log_level:
        msg = f"\nДеталі логів для рівня {args.log_level.upper()}:"
        print(msg)
        for item in filter_logs_by_level(logs, args.log_level):
            print(f"{item['date']} {item['time']} - {item['message']}")
    

if __name__ == "__main__":
    main()
   


