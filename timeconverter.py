## Program ##
import sys
def remove_spaces(string): # Removes spaces from inputs to prevent unwanted error messages
        if len(string) <= 1 or " " not in string:
            return string
        newstring = ""
        string = list(string)
        while " " in string:
            string.remove(" ")
        for i in string:
            newstring += i
        return newstring

def check_replay():
# Check if user wants to check the converter again
    replay = remove_spaces(input("\nThat was a fun ride, do over? (y,N) -> ").lower())
    while replay != "y" and replay != "n" and replay != "" and replay != "q" and not replay.isspace():
        print("Didn't catch that, answer with (y)es or (n)o. You can also press enter to exit")
        replay = remove_spaces(input("\nWish to start over? (y,N) -> ").lower())

    if replay == "y":
        timeconverter(first = False)
    else:
        print("\nSee you soon at the Starr Park! ;)")  
        quit()

def timeconverter(first = True):
    def translate_unit(unit, list1, translations): # Translate from input character to word (eg "y" -> "year")
        return translations[list1.index(unit)]

    def rev(lst): # Reverse list
        lst_copy = [] 
        reversed = []
        for i in lst:
            lst_copy.append(i)
        for _ in range(len(lst_copy)):
            reversed.append(lst_copy.pop())
        return reversed
    
    def remove_spaces(string): # Removes spaces from inputs to prevent unwanted error messages
        if len(string) <= 1 or " " not in string:
            return string
        newstring = ""
        string = list(string)
        while " " in string:
            string.remove(" ")
        for i in string:
            newstring += i
        return newstring
    
    def split_float(float_nmbr): # Get integer and float float parts of a number
        if isinstance(float_nmbr, int):
            return str(float_nmbr), "0"
        num_string = str(float_nmbr)
        int_st = ""
        float_st = ""
        dot_reached = False
        for i in num_string:
            if i == ".":
                dot_reached = True
            else:
                if not dot_reached:
                    int_st += i
                else:
                    float_st += i
        return int_st, float_st

    def make_readable(number): # Add commas where needed to make large numbers more readable
        if (not isinstance(number, int) and not isinstance(number, float)) or "e" in str(number):
            return number
        out_number = ""
        num_string = str(number)
        num_float = ""
        if isinstance(number, float):
            num_string, num_float = split_float(number)
        if len(num_string) > 3:
            remainder = len(num_string) % 3
            if remainder != 0:
                out_number += num_string[0:remainder] + ","
            for i in range(1, len(num_string[remainder:]) + 1):
                out_number += num_string[remainder:][i-1]
                if i % 3 == 0 and i != len(num_string[remainder:]):
                    out_number += ","    
        if isinstance(number, float):
            if len(num_string) <= 3:
                out_number += num_string
            out_number += "." + num_float
        return out_number

    def convert(value, unit, convert_to, list1): # Conversion algorithm
        if "mo" in list1[list1.index(unit):list1.index(convert_to)] or "mo" in list1[list1.index(convert_to):list1.index(unit)]:
            print("\nWARNING: This conversion assumes that a month has 30 days!")
        if list1.index(unit) < list1.index(convert_to):
            for i in multiconverts[list1.index(unit):list1.index(convert_to)]:
                value *= i
        else:
            list1 = rev(list1)
            for i in divconverts[list1.index(unit):list1.index(convert_to)]:
                value /= i
        return value
    
    def interface(): # Main interface with user
        def wlcm_msg():
            if first: # Check if it's the first time the user is using the converter
                print("\n\tWELCOME TO THE STARR TIME CONVERTER\n\tA place where nothing could ever go wrong, and why would it?")
            else:
                print("\n\tWELCOME BACK TO THE STARR TIME CONVERTER!\n\tHappy to see you again :)")
  
        def get_value(): # Get user's choices for value and conversion units
            value = remove_spaces(input(f"\nEnter value you wish to convert -> ").lower())
            if value != "q":
                try:
                    value = float(value)  
                except:
                    print("Wrong answer! Value must be a positive nonzero integer/float number")
                    value = get_value()
                    return value
                if value <= 0:
                    print("Wrong answer! Value must be a positive nonzero integer/float number")
                    value = get_value()
                    return value
                if value >= sys.maxsize:
                    print("Wrong answer! Value too large!")
                    value = get_value()
                    return value
                if value <= -sys.maxsize:
                    print("Wrong answer! Value too small!")
                    value = get_value()
                    return value
                else:
                    print(f"\n{make_readable(value)}. Got it.", end=" ")
                    return value

            else:
                print("Aborted. See you soon at the Starr Park! ;)")
                quit()
        
        def get_unit():
            unit = remove_spaces(input("What unit are you converting from? (c)enturies, (de)cades, (y)ears, (mo)nths, (d)ays, (h)ours, (m)inutes, (s)econds or (ms)(miliseconds) -> ").lower())
            if unit != "q":
                if unit not in units:
                    print("Error! You can only enter \"c\", \"de\", \"y\", \"mo\", \"w\", \"d\", \"h\", \"m\", \"s\" or \"ms\"")
                    unit = get_unit()
                    return unit
                else:
                    print(f"\nGreat! From {translations_plu[units.index(unit)]} it is.", end=" ")
                    return unit

            else:
                print("Aborted. See you soon at the Starr Park! ;)")
                quit()

        def get_convert_to():    
            convert_to = remove_spaces(input("Now what do you want to convert to? (c)enturies, (de)cades, (y)ears, (mo)nths, (d)ays, (h)ours, (m)inutes, (s)econds or (ms)(miliseconds) -> ").lower())
            if convert_to != "q":
                if convert_to not in units:
                    print("Error! You can only enter \"c\", \"de\", \"y\", \"mo\", \"w\", \"d\", \"h\", \"m\", \"s\" or \"ms\"")
                    convert_to = get_convert_to()
                    return convert_to
                else:
                    return convert_to
            else:
                print("Aborted. See you soon at the Starr Park! ;)")
                quit()
            

        # Launch UI and get user's data
        wlcm_msg()
        value, unit, convert_to = get_value(), get_unit(), get_convert_to()
        
        # Check that user isn't converting from the same unit they want to convert to
        if unit == convert_to:
            print(f"Why would you convert from {translate_unit(unit, units, translations_plu)} to {translate_unit(convert_to, units, translations_plu)}?. Try again!")
            timeconverter()
        return value, unit, convert_to
        
    # Some needed structures
    units = ["c", "de", "y", "mo", "d", "h", "m", "s", "ms"]
    translations = ["century", "decade", "year", "month", "day", "hour", "minute", "second", "milisecond"]
    translations_plu = ["centuries", "decades", "years", "months", "days", "hours", "minutes", "seconds", "miliseconds"]
    multiconverts = [10, 10, 12, 30,  24, 60, 60, 1000]
    divconverts = rev(multiconverts)
    

    value, unit, convert_to = interface() # Launch interface to get user data
    newValue = convert(value, unit, convert_to, units) # Execute conversion
    
    # Print conversion results in an aesthetic way
    print(f"\n\tConversion from {translations_plu[units.index(unit)]} to {translations_plu[units.index(convert_to)]} complete!\n")
    if value == 1:
        if int(newValue) == 1:
            print(f"{make_readable(value)} {translate_unit(unit, units, translations)} -> {make_readable(newValue)} {translate_unit(convert_to, units, translations)}")
        else:
            print(f"{make_readable(value)} {translate_unit(unit, units, translations)} -> {make_readable(newValue)} {translate_unit(convert_to, units, translations_plu)}")
    else:
        if int(newValue) == 1:
            print(f"{make_readable(value)} {translate_unit(unit, units, translations_plu)} -> {make_readable(newValue)} {translate_unit(convert_to, units, translations)}")
        else:
            print(f"{make_readable(value)} {translate_unit(unit, units, translations_plu)} -> {make_readable(newValue)} {translate_unit(convert_to, units, translations_plu)}")

    check_replay()

# Main
timeconverter()

