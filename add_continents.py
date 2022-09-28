# Anaïs Mortazavi Zadeh
# Student ID: 260925966

def get_iso_codes_by_continent(iso_file):
    """
    (str) -> dict
    
    This function takes a string representing a file (iso_file)
    which has iso_codes and continents. The function returns a dictionary with
    continents (in upper case letter) mapping to a list of their respective countries
    (iso_codes).
    
    >>> d = get_iso_codes_by_continent("iso_codes_by_continent.tsv")
    >>> len(d['ASIA'])
    50
    
    >>> t = get_iso_codes_by_continent('iso_code_test_file.tsv')
    >>> t['ASIA'] == ['RUS']
    True
    >>> t['EUROPE']
    ['AAA', 'RUS']
    
    >>> a = get_iso_codes_by_continent('another_iso_code_test_file.tsv')
    >>> a
    {'EUROPE': ['DDD', 'RUS'], 'ASIA': ['RUS'], 'NORTH AMERICA': ['AAA'], 'SOUTH AMERICA': ['AAA'], 'OCEANIA': ['BBB'], 'AFRICA': ['CCC']}
    
    """
    # Important to remember: each continent in the dictionary maps to a list
    continents = {}
    fobj = open(iso_file, "r", encoding="utf-8")
    for line in fobj:
        line = line.replace('\n','')
        line = line.split('\t')
        # We know that at index 1, we will always have the continent
        key = line[1].upper()
        if key not in continents:
            continents[key] = [line[0]]
        else:
        # If the continent is already in the dictionary, then we just append to 'value'
            continents.get(key).append(line[0])
    fobj.close()
    return continents

def add_continents_to_data(input_filename, continents_filename, output_filename):
    """
    (str, str, str) -> int
    
    This function takes three strings: an input filename, continents filename,
    and an output filename. The function reads the input file, modifies it by
    adding continents in the third column, and writes it in the output file.
    
    >>> add_continents_to_data("large_clean_co2_data.tsv", "iso_codes_by_continent.tsv", "large_co2_data.tsv")
    17452
    
    >>> add_continents_to_data("final_final_check.tsv", "iso_code_test_file.tsv", "add_continents_test.tsv")
    1
    >>> fobj = open('add_continents_test.tsv', 'r', encoding='utf-8')
    >>> fobj.read()
    'AAA\\tA test\\tEUROPE,NORTH AMERICA,SOUTH AMERICA\\t2001\\t1.123\\t123456789'
    
    >>> add_continents_to_data("faulty_lines_large_cleaned.tsv", "another_iso_code_test_file.tsv", "another_add_continents_test.tsv")
    2006
    
    """
    fobj = open(input_filename, "r", encoding="utf-8")
    fobj2 = open(continents_filename, "r", encoding="utf-8")
    fobj3 = open(output_filename, "w", encoding="utf-8")
    file2_content = fobj2.read()
    # We put all file2 content on one line by replacing \n with \t
    file2_content = file2_content.replace('\n','\t')
    fobj2_list = file2_content.split('\t')
    number_of_lines = 0
    for line in fobj:
        continents = []
        line_list = line.split('\t')
        # We know country iso_code is always at index 0
        country = line_list[0]
        for n, i in enumerate(fobj2_list):
            if i == country:
                continents.append(fobj2_list[n+1].upper())
        # Some countries may be in more than one continent,
        # so we join continents with a comma
        s = ','.join(continents[:])
        # Insert continents in the index 2 position
        line_list.insert(2, s)
        # Join all elements with a tab
        line = '\t'.join(line_list[:])
        fobj3.write(line)
        # Each time line is written, we add 1 to number_of_lines
        number_of_lines += 1
    fobj.close()
    fobj2.close()
    fobj3.close()
    # We return the total number of lines written in the output file
    return number_of_lines