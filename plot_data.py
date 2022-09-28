# Anaïs Mortazavi Zadeh
# Student ID: 260925966

from build_countries import *
from add_continents import *
from data_cleanup import *
import matplotlib.pyplot as plt

def get_bar_co2_pc_by_continent(countries_from_file_dict, year):
    """
    (dict, int) -> list
    
    This function takes a dictionary of iso_codes mapping to Country objects
    and an integer representing a specific year. The function creates a bar graph
    of co2_emissions per capita (in tonnes) for all countries in each continent.
    It returns the data points plotted.
    
    >>> d1 = get_countries_from_file("small_co2_data.tsv")
    >>> get_bar_co2_pc_by_continent(d1, 2001)
    [0.20320332558992543, 67.01626016260163, 7.6609004739336495, 1.4196063588190764]
    
    >>> d1 = get_countries_from_file("another_hist_bar_test.tsv")
    >>> get_bar_co2_pc_by_continent(d1, 2008)
    [0.0, 0.0, 0.9995407296647326, 0.056643300515454034, 11.294660943892238]
    
    >>> d1 = get_countries_from_file("large_co2_data.tsv")
    >>> get_bar_co2_pc_by_continent(d1, 1999)
    [1.0477316575433337, 2.6227274680001824, 7.9501098050609205, 14.499866263139383, 12.590780965014094, 2.4089666225576245]
    
    """
    x_axis = []
    y_axis = []
    # First we append all continent names to x_axis list
    list_of_countries = []
    for k in countries_from_file_dict:
        list_of_countries.append(countries_from_file_dict[k])
        for i in countries_from_file_dict[k].continents:
            if i not in x_axis:
                x_axis.append(i)
    # We use sort method to make sure x axis is alphabetical 
    x_axis.sort()
    
    # This gives us a dictionary of continents mapping to their corresponding countries
    countries_by_continent = Country.get_countries_by_continent(list_of_countries)
    for i in x_axis:
        # We get the index of the specific x_axis label
        # So that we can make sure y_axis values correspond correctly
        i_index = x_axis.index(i)
        for k in countries_by_continent:
            if k == i:
                # We use methods from build_countries module to get co2 emissions pc by year
                # For all countries in specific continents
                continent_co2 = Country.get_total_co2_emissions_per_capita_by_year(countries_by_continent[k], year)
                # We insert y-axis value into y_axis list at index we got earlier
                y_axis.insert(i_index, continent_co2)
                
    plt.bar(x_axis, y_axis)
    plt.title("CO2 emissions per capita in "+str(year)+" by anais.mortazavizadeh@mail.mcgill.ca", fontsize=10)
    plt.xticks(fontsize=7)
    plt.ylabel("co2 (in tonnes)")
    plt.savefig("co2_pc_by_continent_"+str(year)+".png")
    plt.close()
    return y_axis

def get_bar_historical_co2_by_continent(countries_from_file_dict, year):
    """
    (dict, int) -> list
    
    This function takes a dictionary of iso_codes mapping to Country objects
    and an integer representing a specific year. The function creates a bar graph
    of historical co2_emissions (in millions of tonnes) for all countries in each continent.
    It returns a list of the data points plotted.
    
    >>> d1 = get_countries_from_file("small_co2_data.tsv")
    >>> get_bar_historical_co2_by_continent(d1, 2015)
    [4.877, 207.54500000000002, 359.367, 149.34300000000002]
    
    >>> d1 = get_countries_from_file("another_hist_bar_test.tsv")
    >>> get_bar_historical_co2_by_continent(d1, 2008)
    [6779.0, 112.459, 113.693, 6.993, 11.1234]
    
    >>> d1 = get_countries_from_file("large_co2_data.tsv")
    >>> get_bar_historical_co2_by_continent(d1, 1999)
    [22637.899000000005, 269545.51900000015, 397574.58200000005, 331372.0910000002, 11548.733, 21687.317999999996]
    
    """
    x_axis = []
    y_axis = []
    list_of_countries = []
    # We add all continent names to x_axis list
    for k in countries_from_file_dict:
        list_of_countries.append(countries_from_file_dict[k])
        for i in countries_from_file_dict[k].continents:
            if i not in x_axis:
                x_axis.append(i)
    # We use sort method to make sure bars are in alphabetical order           
    x_axis.sort()
    countries_by_continent = Country.get_countries_by_continent(list_of_countries)
    
    for i in x_axis:
        i_index = x_axis.index(i)
        for k in countries_by_continent:
            if k == i:
                # Once again, we can use our methods from earlier
                # To determine total historical co2 emissions for
                # list of countries in each continent
                continent_historical_co2 = Country.get_total_historical_co2_emissions(countries_by_continent[k], year)
                y_axis.insert(i_index, continent_historical_co2)
    
    plt.bar(x_axis, y_axis)
    plt.title("Historical CO2 emissions up to "+str(year)+" by anais.mortazavizadeh@mail.mcgill.ca", fontsize=10)
    plt.xticks(fontsize=7)
    plt.ylabel("co2 (in millions of tonnes)")
    plt.savefig("hist_co2_by_continent_"+str(year)+".png")
    plt.close()
    # We return list of values being plotted
    return y_axis
    
def get_bar_co2_pc_top_ten(countries_from_file_dict, year):
    """
    (dict, int) -> list
    
    This function takes a dictionary of iso_codes mapping to Country objects
    and an integer representing a specific year. The function creates a
    bar graph representing the co2_emissions per capita (in tonnes) of
    the top ten producing countries. The function returns a list of the
    values graphed.
    
    >>> d1 = get_countries_from_file("small_co2_data.tsv")
    >>> data = get_bar_co2_pc_top_ten(d1, 2001)
    >>> len(data)
    5
    >>> data[0]
    67.01626016260163
    >>> data[4]
    0.20320332558992543
    
    >>> d1 = get_countries_from_file("another_hist_bar_test.tsv")
    >>> data = get_bar_co2_pc_top_ten(d1, 2008)
    >>> len(data)
    3
    >>> data 
    [11.294660943892238, 0.9995407296647326, 0.056643300515454034]
    
    >>> d1 = get_countries_from_file("add_continents_test.tsv")
    >>> get_bar_co2_pc_top_ten(d1, 2001)
    [0.00909630008277633]
    
    """
    x_axis = []
    y_axis = []
    list_of_countries = []
    # This time we add all country codes to list_of_countries list
    for k in countries_from_file_dict:
        if year in countries_from_file_dict[k].co2_emissions and year in countries_from_file_dict[k].population:
            list_of_countries.append(countries_from_file_dict[k])
        
    co2_emissions_per_country =  Country.get_co2_emissions_per_capita_by_year(list_of_countries, year)
    # We use the get_top_n method with our dictionary co2_emissions_per_country
    # To get the top 10 co2 producing countries from greatest to least
    top_ten_co2 = Country.get_top_n(co2_emissions_per_country, 10)
    for tup in top_ten_co2:
        x_axis.append(tup[0])
        y_axis.append(tup[1])
        
    plt.bar(x_axis, y_axis)
    plt.title("Top 10 countries for CO2 emissions pc in "+str(year)+" by anais.mortazavizadeh@mail.mcgill.ca", fontsize=10)
    plt.xticks(fontsize=7)
    plt.ylabel("co2 (in tonnes)")
    plt.savefig("top_10_co2_pc_"+str(year)+".png")
    plt.close()
    return y_axis    
    
def get_bar_top_ten_historical_co2(countries_from_file_dict, year):
    """
    (dict, int) -> list
    
    This function takes a dictionary of iso_codes mapping to Country objects
    and an integer representing a specific year. The function creates a
    bar graph representing the historical co2_emissions (in millions of tonnes) of
    the top ten producing countries. The function returns a list of the
    values graphed.
    
    >>> d1 = get_countries_from_file("small_co2_data.tsv")
    >>> get_bar_top_ten_historical_co2(d1, 2015)
    [306.696, 166.33, 149.34300000000002, 48.923, 41.215, 3.748, 3.324, 1.553, 0.0]
    
    >>> d2 = get_countries_from_file("add_continents_test.tsv")
    >>> get_bar_top_ten_historical_co2(d2, 2008)
    [1.123]
    
    >>> d1 = get_countries_from_file("another_hist_bar_test.tsv")
    >>> get_bar_top_ten_historical_co2(d1, 2009)
    [7778894.993, 6779.0, 112.459, 11.1234, 1.234]
    
    """
    # This graph is similar to previous graph: get_bar_co2_pc_top_ten
    x_axis = []
    y_axis = []
    list_of_countries = []
    for k in countries_from_file_dict:
        list_of_countries.append(countries_from_file_dict[k])
    # Main difference between previous graph and this one is that
    # We use get_historical_co2_emissions and then get_top_n to graph
    # top ten co2 producing countries for all years up to and including
    # the specific input year
    historical_emissions = Country.get_historical_co2_emissions(list_of_countries, year)
    top_ten_historical = Country.get_top_n(historical_emissions, 10)
    for tup in top_ten_historical:
        x_axis.append(tup[0])
        y_axis.append(tup[1])
        
    plt.bar(x_axis, y_axis)
    plt.title("Top 10 countries for historical CO2 up to "+str(year)+" by anais.mortazavizadeh@mail.mcgill.ca", fontsize=10)
    plt.xticks(fontsize=7)
    plt.ylabel("co2 (in millions of tonnes)")
    plt.savefig("top_10_hist_co2_"+str(year)+".png")
    plt.close()
    return y_axis
   
def get_plot_co2_emissions(countries_from_file_dict, list_of_iso_codes, min_year, max_year):
    """
    (dict, list, int, int) -> list

    This function takes a dictionary of iso codes mapping to Country objects.
    It also takes a list of strings (iso_codes), and an integer representing
    min year and another representing max year. The function returns a 2D list
    with each sublist containing co2_emissions from min year to max year. This
    data is also plotted.

    >>> d2 = get_countries_from_file("large_co2_data.tsv")
    >>> data = get_plot_co2_emissions(d2, ["USA", "CHN", "RUS", "DEU", "GBR"], 1800, 2000)
    >>> len(data[0])
    201
    >>> data[2][4]
    0.0
    >>> data[4][190]
    600.773
    >>> data[3][200]
    900.376

    >>> d2 = get_countries_from_file("add_continents_test.tsv")
    >>> data = get_plot_co2_emissions(d2, ["AAA"], 1999, 2009)
    >>> data
    [[0.0, 0.0, 1.123, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]]
    
    >>> d2 = get_countries_from_file("add_continents_test.tsv")
    >>> data = get_plot_co2_emissions(d2, ["RUS","BEL"], 1999, 2009)
    >>> data
    []
    
    """
    all_data = []
    x_coord = [min_year]
    # These are 5 different line styles for plotting
    line_styles = ['o--','*-','>-.','.:','^--']
    # Since there needs to be 10 points plotted
    # We take difference between min and max year, and divide by 10
    difference_between_years = max_year - min_year
    interval = difference_between_years//10
    # We add interval to each value in x_coord list
    for i in x_coord:
        if len(x_coord) <= 10:
            x_coord.append(i+interval)
    # Each time we go through loop we change line style
    # Each time we plot a line
    style = 0        
    for i in list_of_iso_codes:
        y_coord = []
        country_data = []
        year = min_year
        if i in countries_from_file_dict:
            while min_year <= year <= max_year:
                country_data.append(countries_from_file_dict[i].get_co2_emissions_by_year(year))
                year += 1
        else:
            # If the iso_code is not in dictionary
            # We do NOT plot that country
            continue
        all_data.append(country_data)
        for x in x_coord:
            y_coord.append(countries_from_file_dict[i].get_co2_emissions_by_year(x))
        plt.plot(x_coord, y_coord, line_styles[style])
        style += 1
    
    
    plt.legend(list_of_iso_codes)
    plt.ylabel("co2 (in millions of tonnes)")
    plt.title("CO2 emissions between "+str(min_year)+" and "+str(max_year)+" by anais.mortazavizadeh@mail.mcgill.ca", fontsize=10)
    plt.savefig("co2_emissions_"+str(min_year)+"_"+str(max_year)+".png")
    plt.close()
    
    return all_data
