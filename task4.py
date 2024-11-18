# decorator for exceptions
def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return 'This contact doesnt exist, please try again.'
        except ValueError as exception:
            return exception.args[0] # we return args of error, in order to know what kind of error we catch
        except IndexError:
            return 'This contact cannot be added, it already exists.'
        except TypeError:
            return 'Unknown command or parametrs, please try again.'
    return inner

contacts = {}


# function for greeting

def greeting():
    return 'How can I help you?'

# add contact in dict and check the number of args
@input_error
def add_contact(*args):
    name, phone = args
    if name in contacts.keys():
        return 'This person already in contacts. Choose command "change"'
    else:
        contacts[name] = phone
    return "Contact added."

# check the number of args, change phone of contact 
@input_error
def change_contact(*args):
    #if len(args) < 2:
    #    return 'Not enough arguments'
    name, phone = args
    if name not in contacts.keys():
        return "This person isn't  in your contacts. Choose command 'add'"
    else:
        contacts[name] = phone
    return f'Contact  {name} changed'

# check contacts existance and show contact information when contacts exist
@input_error
def show_phone(name):
    return f'Name: {name}, phone: {contacts[name]}'     


def show_all():
    if not contacts:
        return 'Your contacts is empty.'
    else:    
        return '\n'.join([f'Name: {k}, phone {contacts[k]}' for k in contacts.keys()]) # join name and phone of contacts. 
    
# dict with commands as keys and function as values    
COMMAND_HANDLER = {
                   'hello': greeting,
                   'add': add_contact,
                   'change': change_contact,
                   'phone': show_phone,
                   'all': show_all
                   }


def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def main():
    
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        # there commands are turn into function calling
        elif command in COMMAND_HANDLER:
            result = COMMAND_HANDLER.get(command)(*args)
            print(result)
        
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()


