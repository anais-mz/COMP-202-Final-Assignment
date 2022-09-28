# Anaïs Mortazavi Zadeh
# Student ID: 260925966

def find_delim(single_line):
    """
    (str) -> str
    
    This function takes a string (single_line) and returns the most common
    delimiter in that string.
    Possible delimiters are: '\t',',',' ','-'.
    
    >>> find_delim("hello")
    Traceback (most recent call last):
    AssertionError: No delimiter found.
    
    >>> find_delim("my\\tname-is-anais")
    '-'
    
    >>> find_delim("0123,4")
    ','
    
    """
    # These are the only delimiters we will be considering
    delimiter = ['\t', ',', ' ', '-']
    
    base_occurrence = 1
    for i in delimiter:
        if i in single_line:
            for char in single_line:
                if char in delimiter:
                    # Every time char is a delimiter, the base_occurrence is updated
                    # base_occurrence will reflect number of times delimiter is in string
                    # The delimiter that has the highest occurrence will be returned
                    occurrence = single_line.count(char)
                    if occurrence >= base_occurrence:
                        base_occurrence = occurrence
                        most_common_delim = char
            return most_common_delim
    # If there are no delimiters in the inputted string, AssertionError is raised    
    raise AssertionError("No delimiter found.")

def clean_one(input_filename, output_filename):
    """
    (str, str) -> int
    
    This function takes an input file to read, modifies each line by replacing the most
    common delimiter with a tab, and writes each line in the output file.
    The function will return an integer representing the number of lines written in the output.
    
    >>> clean_one('small_raw_co2_data.txt', 'small_tab_sep_co2_data.tsv')
    10
    
    >>> clean_one('final_check.tsv', 'final_clean_one_check.tsv')
    1
    
    >>> clean_one('faulty_lines_large.tsv', 'final_clean_one_check.tsv')
    2006
    
    """
    # Important to note that this function replaces MOST COMMON delimiter with a tab
    
    fobj = open(input_filename, "r", encoding="utf-8")
    fobj2 = open(output_filename, "w", encoding="utf-8")
    number_of_lines = 0
    for line in fobj:
        # We can use the find_delim() function to find most common delimiter
        most_common_delim = find_delim(line)
        # Now we replace the most_common_delim with a tab
        line = line.replace(most_common_delim, '\t')
        fobj2.write(line)
        number_of_lines += 1
    # We need to return number of lines written in output file            
    return number_of_lines

def final_clean(input_filename, output_filename):
    """
    (str, str) -> int
    
    This function takes an input file, modifies it to make sure all lines have
    only 5 columns, and writes each line into the output file.
    All commas must be replaced with a dot for decimals.
    
    >>> final_clean('large_tab_sep_co2_data.tsv', 'large_clean_co2_data.tsv')
    17452
    
    >>> final_clean('faulty_lines_large.tsv', 'faulty_lines_large_cleaned.tsv')
    2006
    
    >>> fobj = open('final_check.tsv', 'w', encoding='utf-8')
    >>> line = fobj.write('AAA\\tA\\ttest\\t2001\\t1\\t123\\t123456789')
    >>> fobj.close()
    >>> final_clean('final_check.tsv','final_final_check.tsv')
    1
    >>> fobj2 = open('final_final_check.tsv', 'r', encoding='utf-8')
    >>> fobj2.read()
    'AAA\\tA test\\t2001\\t1.123\\t123456789'
    
    """
    # Important to note that there are different scenarios that will cause more than 5 columns
    # Scenario 1: if co2_emissions value is separated
    # Scenario 2: if country name has multiple words
    # Scenario 3: if both co2_emissions is separated AND country name has multiple words
    # We also have to replace commas with dots
    
    fobj = open(input_filename, "r", encoding="utf-8")
    fobj2 = open(output_filename, "w", encoding="utf-8")
    number_of_lines = 0
    for line in fobj:
        line = line.replace(',','.')
        # First we check if a line has more than 5 columns
        # If a line has more than 4 tabs, there are more than 5 columns
        if line.count('\t') > 4:
            line = line.split('\t')
            # If element at index 2 is a 4 digit integer,
            # then we know that the co2_emissions has been separated
            if len(line[2]) == 4 and line[2].isdecimal()==True:
                line = line[0]+"\t"+line[1]+"\t"+line[2]+"\t"+'.'.join([line[3],line[4]])+"\t"+line[5]
                fobj2.write(line)
                number_of_lines += 1
            else:
            # If element at index 2 is NOT a 4 digit integer,
            # We can assume that the country name has mutliple words
            # So, we find element that is 4 digit integer and join words before that
                for i in line:
                    if len(i) == 4 and i.isdecimal()==True:
                        x = line.index(i)
                        break
                line = line[0]+"\t"+" ".join(line[1:x])+"\t"+"\t".join(line[x:])
                # After that, we double check number of columns
                # to see if co2_emissions is also separated
                if line.count('\t') > 4:
                    line = line.split('\t')
                    line = line[0]+"\t"+line[1]+"\t"+line[2]+"\t"+'.'.join([line[3],line[4]])+"\t"+line[5]
                    fobj2.write(line)
                    number_of_lines += 1
                else:
                    fobj2.write(line)
                    number_of_lines += 1 
        else:
            fobj2.write(line)
            number_of_lines += 1
    # All lines are written in output file, and the number of lines written is returned
    return number_of_lines