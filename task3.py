import sys
from pathlib import Path


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
    levels_list = [log for log in logs if log['level'] == level.upper()] # add in list dicts with level == needed level 
    
    return levels_list            

# counting multiplicity of entry for every log 
def count_logs_by_level(logs: list) -> dict:    
    count_dict = {}
    levels = {log['level'] for log in logs} # set with values of "level"

    for  i in levels:
        counted = list(filter(lambda x: x['level'] == i, logs))  # list with dicts, where "level" == value from levels set
        count_dict[i] = len(counted) # length (counted) = quantity
        
    return count_dict

# building table for printing result dict
def display_log_counts(counts: dict):
# sorted list of tuples, where key => tuple[0], value => tuple[1], sort by value, reverse order 
    sorted_items = sorted(counts.items(), key=lambda x: x[1], reverse=True)

    s = "Рівень логування"
    t = " | "
    r = "Кількість"
    print(s,t,r)
    print("_" * (len(s) + len(t) + len(r)))
    for value in sorted_items:
        print("{:<{}}{}{:<}".format(value[0], len(s) + 1, t, value[1]))

def main():

# with help library sys find filename as args[1]  argument and logging level as optional argument args[2]
    try:
        filename = sys.argv[1]
        logs = load_logs(filename)
        count_logs_by_level(logs)
        display_log_counts(count_logs_by_level(logs))
        
    except IndexError:
        print("Input path and name of log file")
    
    args = sys.argv[2:] 
       
    if args:
        for arg in args:
            msg = f"\nДеталі логів для рівня {arg.upper()}:"
            print(msg)
            for item in filter_logs_by_level(logs, arg):
                print(f"{item['date']} {item['time']} - {item['message']}")

    

if __name__ == "__main__":
    main()
   


