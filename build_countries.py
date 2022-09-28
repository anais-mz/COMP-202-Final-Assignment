# Anaïs Mortazavi Zadeh
# Student ID: 260925966

import copy

class Country:
    """
    Represents a country.
    
    Instance Attributes: iso_code (str), name (string), continents (list),
    co2_emissions (dict), population (dict)
    
    Class Attributes: min_year_recorded (int), max_year_recorded (int)
    
    """
    min_year_recorded = float('inf')
    max_year_recorded = float('-inf')
    
    def __init__(self, iso_code, name, list_of_continents, year, country_co2, country_pop):
        """
        (Country, str, str, list, int, float, int) -> NoneType
        
        This constructor uses the given inputs to initiate all the
        instance attributes accordingly.
        
        >>> r = Country("RUS", "Russia", ["ASIA", "EUROPE"], 2007, 1604.778, 14266000)
        >>> r.co2_emissions
        {2007: 1604.778}
        >>> r.continents
        ['ASIA', 'EUROPE']
        >>> r.population
        {2007: 14266000}
        
        >>> t = Country("AAA", "A test", ['EUROPE','NORTH AMERICA','SOUTH AMERICA'], 1990, -1, -1)
        >>> t.population
        {}
        
        >>> c = Country ('CAN', 'Canada', ['NORTH AMERICA'], 2001, -1, 1500000)
        >>> c.name
        'Canada'
        
        """
        # Valid Iso_Codes are 3 characters long
        # Important to remember that only OWID_KOS is longer than 3 letters
        if len(iso_code) == 3:
            self.iso_code = iso_code
        elif iso_code == "OWID_KOS":
            self.iso_code = "OWID_KOS"
        else:
            raise AssertionError
        
        self.name = name
        
        # We need to make a copy of the list
        continents = copy.copy(list_of_continents)
        self.continents = continents
        
        # If co2_emissions = -1, then the dictionary will be empty
        co2_emissions = {}
        if country_co2 != -1:
            co2_emissions[year] = country_co2  
        self.co2_emissions = co2_emissions
        
        # If population = -1, then the dictionary will be empty
        population = {} 
        if country_pop != -1:
            population[year] = country_pop
        self.population = population
        
        # Inputted year must be compared to min/max year
        # Min/max year must be updated if necessary
        if year < Country.min_year_recorded:
            Country.min_year_recorded = year
            
        if year > Country.max_year_recorded:
            Country.max_year_recorded = year
            
    def __str__(self):
        """
        (Country) -> str
        
        This instance method returns a string representation of a Country object.
        The string will contain the country name, continents, co2_emissions, and population.
        
        >>> c = Country ('CAN', 'Canada', ['NORTH AMERICA'], 2001, -1, 1500000)
        >>> str(c)
        'Canada\\tNORTH AMERICA\\t{}\\t{2001: 1500000}'
        
        >>> r = Country("RUS", "Russia", ["ASIA", "EUROPE"], 2007, 1604.778, 14266000)
        >>> str(r)
        'Russia\\tASIA,EUROPE\\t{2007: 1604.778}\\t{2007: 14266000}'
        
        >>> a = Country("AAA", "A test", ['OCEANIA', 'NORTH AMERICA', 'SOUTH AMERICA'], 1990, -1, -1)
        >>> str(a) == 'A test\\tOCEANIA,NORTH AMERICA,SOUTH AMERICA\\t{}\\t{}'
        True
        
        """
        # We join the different attributes and convert all to string
        country = self.name
        # Since continents are in a list, we need to join them with comma
        continents = ','.join(self.continents[:])
        co2_emissions = str(self.co2_emissions)
        population = str(self.population)
        
        # Separate everything with a tab, and return string representation 
        return country+'\t'+continents+'\t'+co2_emissions+'\t'+population
    
    def add_yearly_data(self, year_data):
        """
        (Country, str) -> NoneType
        
        This instance method takes a string (year_data) as input. This string includes
        year, co2_emissions, and population all separated by tabs. Using this info the
        method updates the appropriate attributes of the country, also updating min/ max year.
        
        >>> c = Country ('CAN', 'Canada', ['NORTH AMERICA'], 2001, -1, 1500000)
        >>> c.add_yearly_data('2020\\t25000\\t')
        >>> c.__str__()
        'Canada\\tNORTH AMERICA\\t{2020: 25000.0}\\t{2001: 1500000}'
        
        >>> a = Country("AFG", "Afghnistan", ["ASIA"], 1949, 0.015, 7663783)
        >>> a.add_yearly_data("2018\\t9.439\\t37122000")
        >>> a.co2_emissions == {1949: 0.015, 2018: 9.439}
        True
        
        >>> t = Country("AAA", "A test", ['EUROPE','NORTH AMERICA','SOUTH AMERICA'], 1990, -1, -1)
        >>> t.add_yearly_data('1990\\t6.789\\t')
        >>> t.co2_emissions == {1990: 6.789}
        True
        >>> t.population == {}
        True
        
        """
        # We need to update Country.min/max year accordingly
        
        year_data_list = year_data.split('\t')
        year = int(year_data_list[0])
        if year < Country.min_year_recorded:
            Country.min_year_recorded = year
            
        if year > Country.max_year_recorded:
            Country.max_year_recorded = year
        
        # An empty string means no data needs to be added to co2/population
        # So we only add yearly data if co2/population is NOT empty string
        if year_data_list[1] != '':
            co2_emissions = float(year_data_list[1])
            self.co2_emissions[year] = co2_emissions
        if year_data_list[2] != '':
            population = int(year_data_list[2])
            self.population[year] = population
        
    def get_co2_emissions_by_year(self, year):
        """
        (Country, int) -> float
        
        This instance method takes an integer representing a specific year, and returns
        the co2_emissions of that country in that specific year. If no data for that year,
        returns 0.0.
        
        >>> a = Country("AFG", "Afghnistan", ["ASIA"], 1949, 0.015, 7663783)
        >>> a.add_yearly_data("2018\\t9.439\\t37122000")
        >>> a.get_co2_emissions_by_year(1949)
        0.015
        
        >>> c = Country ('CAN', 'Canada', ['NORTH AMERICA'], 2001, -1, 1500000)
        >>> c.get_co2_emissions_by_year(2001)
        0.0
        
        >>> t = Country("AAA", "A test", ['EUROPE','NORTH AMERICA','SOUTH AMERICA'], 1990, -1, -1)
        >>> t.add_yearly_data('1990\\t6.789\\t')
        >>> t.co2_emissions
        {1990: 6.789}
        >>> t.get_co2_emissions_by_year(2000)
        0.0
        
        """
        # If there is no co2 data for that specific year, return 0.0
        if year in self.co2_emissions:
            return self.co2_emissions[year]
        else:
            return 0.0
        
    def get_co2_per_capita_by_year(self, year):
        """
        (Country, int) -> float
        
        This instance method takes an integer representing a specific year, and
        returns the total co2_emissions/per capita in tonnes for a country in that
        specific year. If either population or co2_emissions is missing, returns None. 
        
        >>> a = Country("AFG", "Afghnistan", ["ASIA"], 1949, -1, 7663783)
        >>> a.add_yearly_data("2018\\t9.439\\t37122000")
        >>> round(a.get_co2_per_capita_by_year(2018), 5)
        0.25427
        
        >>> c = Country ('CAN', 'Canada', ['NORTH AMERICA'], 2001, -1, 1500000)
        >>> print(c.get_co2_per_capita_by_year(2001))
        None
        
        >>> t = Country("AAA", "A test", ['EUROPE','NORTH AMERICA','SOUTH AMERICA'], 1990, 6.789, 123456789)
        >>> t.add_yearly_data("1990\\t\\t")
        >>> round(t.get_co2_per_capita_by_year(1990), 3)
        0.055

        """
        # If there is no population data for that specific year, return None
        if year in self.co2_emissions and year in self.population:
            co2_per_capita = (self.co2_emissions[year]*1000000)/self.population[year]
            return co2_per_capita
        else:
            return None
        
    def get_historical_co2(self, year):
        """
        (Country, int) -> float
        
        This instance method takes an integer representing a specific year and returns
        the total co2_emissions of all the years up to and including that specific year.
        
        >>> q = Country("QAT", "Qatar", ["ASIA"], 2007, 62.899, 1218000)
        >>> q.add_yearly_data("1993\\t30.985\\t501000")
        >>> q.add_yearly_data("1989\\t14.292\\t462000")
        >>> q.get_historical_co2(2000)
        45.277
        
        >>> c = Country ('CAN', 'Canada', ['NORTH AMERICA'], 2001, -1, 1500000)
        >>> c.add_yearly_data("2020\\t1.234\\t3900000")
        >>> c.add_yearly_data("1998\\t\\t")
        >>> c.co2_emissions == {2020: 1.234}
        True
        >>> c.get_historical_co2(2020) == 1.234
        True
        
        >>> t = Country("AAA", "A test", ['EUROPE','NORTH AMERICA','SOUTH AMERICA'], 1990, 6.789, 123456789)
        >>> t.get_historical_co2(1989)
        0.0
        
        """
        # We start with a total/historical co2 of 0.0
        # Then we add the co2 data for every year up to and including inputted year
        total_co2 = 0.0
        for k in self.co2_emissions:
            if k <= year:
                total_co2 += self.co2_emissions[k]
                
        return total_co2
    
    @classmethod
    def get_country_from_data(cls, country_data):
        """
        (type, str) -> Country
        
        This class method takes a string and returns a new Country object
        with the inputted info.
        
        >>> r = Country.get_country_from_data("RUS\\tRussia\\tASIA,EUROPE\\t1971\\t1533.262\\t130831000")
        >>> r.__str__()
        'Russia\\tASIA,EUROPE\\t{1971: 1533.262}\\t{1971: 130831000}'
        
        >>> c = Country.get_country_from_data("CAN\\tCanada\\tNORTH AMERICA\\t1791\\t0.004\\t")
        >>> c.__str__() == 'Canada\\tNORTH AMERICA\\t{1791: 0.004}\\t{}'
        True
        
        >>> a = Country.get_country_from_data("ALB\\tAlbania\\tEUROPE\\t1991\\t4.283\\t3280000")
        >>> a.add_yearly_data("2001\\t100.99\\t4000000")
        >>> a.__str__()
        'Albania\\tEUROPE\\t{1991: 4.283, 2001: 100.99}\\t{1991: 3280000, 2001: 4000000}'
        
        """
        # We know the order of items in the data
        # So we split into a list so we can use specific indices 
        country_data_list = country_data.split('\t')
        iso_code = country_data_list[0]
        country = country_data_list[1]
        continent = country_data_list[2].split(',')
        year = int(country_data_list[3])
        if country_data_list[4] != '':
            co2_emissions = float(country_data_list[4])
        else:
            # If the co2_emission is an empty string, then it will be -1
            co2_emissions = -1
        if country_data_list[5] != '':
            population = int(country_data_list[5])
        else:
            # If the population is an empty string, then it will be -1
            population = -1
        return cls(iso_code, country, continent, year, co2_emissions, population)
    
    @staticmethod
    def get_countries_by_continent(list_of_country_objects):
        """
        (list) -> dict
        
        This static method takes a list of Country objects and returns a dictionary
        of continents mapping to a list of country objects in the specific continent.
        
        >>> a = Country("AFG", "Afghanistan", ["ASIA"], 1949, 0.015, 7663783)
        >>> b = Country("ALB", "Albania", ["EUROPE"], 2007, 3.924, 3034000)
        >>> r = Country("RUS", "Russia", ["ASIA", "EUROPE"], 2007, 1604.778, 14266000)
        >>> c = [a, b, r]
        >>> d = Country.get_countries_by_continent(c)
        >>> str(d['ASIA'][1])
        'Russia\\tASIA,EUROPE\\t{2007: 1604.778}\\t{2007: 14266000}'
        
        >>> c = Country.get_country_from_data("CAN\\tCanada\\tNORTH AMERICA\\t1791\\t0.004\\t")
        >>> u = Country.get_country_from_data("USA\\tUnited States of America\\tNORTH AMERICA\\t1894\\t-1\\t-1")
        >>> l = [c, u]
        >>> d = Country.get_countries_by_continent(l)
        >>> str(d['NORTH AMERICA'][0]) == 'Canada\\tNORTH AMERICA\\t{1791: 0.004}\\t{}'
        True
        
        >>> t = Country("AAA", "A test", ['EUROPE','NORTH AMERICA','SOUTH AMERICA'], 1990, -1, -1)
        >>> l = [t]
        >>> d = Country.get_countries_by_continent(l)
        >>> str(d['EUROPE'][0]) == str(d['NORTH AMERICA'][0]) == str(d['SOUTH AMERICA'][0])
        True
        
        """
        country_continents = {}
        for country in list_of_country_objects:
            # We use the continents attribute to make sure we get all continents in file
            for i in country.continents:
                if i not in country_continents:
                    country_continents[i] = [country]
                else:
                    # Because value is a list, if i is already in dictionary
                    # Then we can just append to the 'value'
                    country_continents.get(i).append(country)
            
        return country_continents
    
    @staticmethod
    def get_total_historical_co2_emissions(list_of_country_objects, year):
        """
        (list, int) -> float
        
        This static method takes a list of Country objects and an integer represeting
        a specific year. The method returns a float representing the total co2_emissions
        of all the countries for all years up to and including that specific year.
        
        >>> b = Country("ALB", "Albania", ["EUROPE"], 2007, 3.924, 3034000)
        >>> r = Country("RUS", "Russia", ["ASIA", "EUROPE"], 2007, 1604.778, 14266000)
        >>> q = Country("QAT", "Qatar", ["ASIA"], 2007, 62.899, 1218000)
        >>> c = [b, r, q]
        >>> Country.get_total_historical_co2_emissions(c,2007)
        1671.601
        
        >>> c = Country.get_country_from_data("CAN\\tCanada\\tNORTH AMERICA\\t1791\\t0.004\\t")
        >>> u = Country.get_country_from_data("USA\\tUnited States of America\\tNORTH AMERICA\\t1894\\t-1\\t-1")
        >>> l = [c, u]
        >>> Country.get_total_historical_co2_emissions(l,1894) == c.co2_emissions[1791]
        True
        >>> Country.get_total_historical_co2_emissions(l,1791)
        0.004
        
        >>> t = Country("AAA", "A test", ['EUROPE','NORTH AMERICA','SOUTH AMERICA'], 1990, 6.789, 123456789)
        >>> r = Country("RUS", "Russia", ['ASIA','EUROPE'], 2015, 1.234, 9870000)
        >>> r.add_yearly_data("2020\\t9.843\\t8990000000")
        >>> l = [t, r]
        >>> Country.get_total_historical_co2_emissions(l, 2020)
        17.866
        >>> Country.get_total_historical_co2_emissions(l, 1989)
        0.0
        
        """
        # We start with historical/total emissions at 0
        # Then we add co2 emissions of all the countries for all
        # years up to and including input year
        total_co2_emissions = 0
        for country in list_of_country_objects:
            # We use get_historical_co2 instance method to get
            # historical co2_emissions for each country
            total_co2_emissions += country.get_historical_co2(year)
            
        return total_co2_emissions
    
    @staticmethod
    def get_total_co2_emissions_per_capita_by_year(list_of_country_objects, year):
        """
        (list, int) -> float
        
        This static method takes a list of Country objects and an integer representing
        a specific year. It returns a float representing the co2_emissions per capita
        (in tonnes) of all the countries in the list for that specific year.

        >>> c = Country("CAN", "Canada", ["NORTH AMERICA"], 1973, 0.004, -1)
        >>> t = Country("TUV", "Tuvalu", ["OCEANIA"], 1973, -1, 6000)
        >>> l = [c, t]
        >>> Country.get_total_co2_emissions_per_capita_by_year(l, 1973)
        0.0
        
        >>> s = Country("SEN", "Senegal", ["AFRICA"], 1971, 1.351, 4388000)
        >>> d = Country("DEN", "Denmark", ["EUROPE"], 1906, 6.544, 2746271)
        >>> c = [s, d]
        >>> Country.get_total_co2_emissions_per_capita_by_year(c, 2001)
        0.0
        
        >>> b = Country("ALB", "Albania", ["EUROPE"], 2007, 3.924, 3034000)
        >>> r = Country("RUS", "Russia", ["ASIA", "EUROPE"], 2007, -1, 14266000)
        >>> c = [b, r]
        >>> round(Country.get_total_co2_emissions_per_capita_by_year(c,2007), 5)
        1.29334
        
        """
        # REMEMBER THAT CO2_EMISSIONS ARE MEASURED IN TONNES FOR THIS METHOD
        # Since this method wants total co2 and total population, we start with 0
        total_co2 = 0
        total_population = 0
        # If data is present for that year, we add to population and co2
        try:
            for country in list_of_country_objects:
                if year in country.co2_emissions and year in country.population:
                    total_co2 += country.co2_emissions[year] * 1000000
                    total_population += country.population[year]
                
            return total_co2/total_population
        # If data is NOT present, co2/population remains 0 so we catch the error
        # And we return 0.0
        except ZeroDivisionError:
            return 0.0
        
    @staticmethod
    def get_co2_emissions_per_capita_by_year(list_of_country_objects, year):
        """
        (list, int) -> dict
        
        This static method takes a list of Country objects and an integer representing
        a specific year. The method returns a dictionary with each country mapping to
        the co2_emissions per capita (in tonnes) for that specific year.
        
        >>> b = Country("ALB", "Albania", ["EUROPE"], 2007, 3.924, 3034000)
        >>> r = Country("RUS", "Russia", ["ASIA", "EUROPE"], 2007, 1604.778, 14266000)
        >>> b.add_yearly_data("1991\\t4.283\\t3280000")
        >>> c = [b, r]
        >>> d2 = Country.get_co2_emissions_per_capita_by_year(c, 1991)
        >>> print(d2[r])
        None
        >>> round(d2[b], 5)
        1.30579
        
        >>> t = Country("AAA", "A test", ['EUROPE','NORTH AMERICA','SOUTH AMERICA'], 2015, 6.789, 123456789)
        >>> r = Country("RUS", "Russia", ['ASIA','EUROPE'], 2015, 1.234, 9870000)
        >>> r.add_yearly_data("2015\\t9.843\\t")
        >>> l = [t, r]
        >>> d1 = Country.get_co2_emissions_per_capita_by_year(l, 2015)
        >>> d1[t] == (6.789*1000000)/123456789
        True
        >>> d1[r] == (9.843*1000000)/9870000
        True
        
        >>> c = Country.get_country_from_data("CAN\\tCanada\\tNORTH AMERICA\\t1894\\t0.004\\t")
        >>> u = Country.get_country_from_data("USA\\tUnited States of America\\tNORTH AMERICA\\t1894\\t-1\\t-1")
        >>> l = [c, u]
        >>> d1 = Country.get_co2_emissions_per_capita_by_year(l, 1894)
        >>> d1 == {c: None, u: None}
        True
        
        """
        co2_emissions_per_capita = {}
        for country in list_of_country_objects:
            # We can use the get_co2_per_capita_by_year method from earlier
            # And if no data is present for a year, then the country will map to None
            co2_emissions_per_capita[country] = country.get_co2_per_capita_by_year(year)
                
        return co2_emissions_per_capita
    
    @staticmethod
    def get_historical_co2_emissions(list_of_country_objects, year):
        """
        (list, int) -> dict
        
        This static method takes a list of Country objects and an integer representing
        a specific year. The method returns a dictionary with each country mapping to
        a float representing the total co2_emissions of all years up to and including the
        input year.
        
        >>> b = Country("ALB", "Albania", ["EUROPE"], 2007, 3.924, 3034000)
        >>> r = Country("RUS", "Russia", ["ASIA", "EUROPE"], 2007, 1604.778, 14266000)
        >>> q = Country("QAT", "Qatar", ["ASIA"], 2007, 62.899, 1218000)
        >>> c = [b, r, q]
        >>> d1 = Country.get_historical_co2_emissions(c,2007)
        >>> len(d1)
        3
        >>> d1[q]
        62.899
        
        >>> c = Country.get_country_from_data("CAN\\tCanada\\tNORTH AMERICA\\t1894\\t0.004\\t")
        >>> u = Country.get_country_from_data("USA\\tUnited States of America\\tNORTH AMERICA\\t1894\\t-1\\t-1")
        >>> c.add_yearly_data("1761\\t6.789\\t123456789")
        >>> l = [c, u]
        >>> d1 = Country.get_historical_co2_emissions(l,1990)
        >>> len(d1)
        2
        >>> round(d1[c],3) == 6.793
        True
        >>> d1[u] == 0.0
        True
        
        >>> t = Country("AAA", "A test", ['EUROPE','NORTH AMERICA','SOUTH AMERICA'], 2015, 6.789, 123456789)
        >>> r = Country("RUS", "Russia", ['ASIA','EUROPE'], 2015, 1.234, 9870000)
        >>> r.add_yearly_data("2015\\t9.843\\t")
        >>> t.add_yearly_data("2014\\t1.234\\t1500000")
        >>> l = [t, r]
        >>> d1 = Country.get_historical_co2_emissions(l,2015)
        >>> d1 == {t: 8.023, r: 9.843}
        True
        
        """
        historical_co2_emissions = {}
        for country in list_of_country_objects:
            # We can use get_historical_co2 method from earlier
            # If there is no historical data, then method will return 0.0
            # And country will map to 0.0 in dictionary
            historical_co2_emissions[country] = country.get_historical_co2(year)
            
        return historical_co2_emissions
    
    @staticmethod
    def get_top_n(country_dict, n):
        """
        (dict, int) -> list
        
        This static method takes a dictionary of Country objects mapping to numbers.
        It also takes an integer. It returns a list of tuples– each tuple contains the
        iso_code of that country and the number it mapped to in the original dictionary.
        The list should contain only the top 'n' countries.

        >>> a = Country("ALB", "Albania", [], 0, 0.0, 0)
        >>> b = Country("AUT", "Austria", [], 0, 0.0, 0)
        >>> c = Country("BEL", "Belgium", [], 0, 0.0, 0)
        >>> d = Country("BOL", "Bolivia", [], 0, 0.0, 0)
        >>> e = Country("BRA", "Brazil", [], 0, 0.0, 0)
        >>> f = Country("IRL", "Ireland", [], 0, 0.0, 0)
        >>> g = Country("MAR", "Marocco", [], 0, 0.0, 0)
        >>> h = Country("NZL", "New Zealand", [], 0, 0.0, 0)
        >>> i = Country("PRY", "Paraguay", [], 0, 0.0, 0)
        >>> j = Country("PER", "Peru", [], 0, 0.0, 0)
        >>> k = Country("SEN", "Senegal", [], 0, 0.0, 0)
        >>> l = Country("THA", "Thailand", [], 0, 0.0, 0)
        >>> d = {a: 5, b: 5, c: 3, d: 10, e: 3, f: 9, g: 7, h: 8, i: 7, j: 4, k: 6, l: 0}
        >>> t = Country.get_top_n(d, 10)
        >>> t[:5] 
        [('BOL', 10), ('IRL', 9), ('NZL', 8), ('MAR', 7), ('PRY', 7)]
        >>> t[5:]
        [('SEN', 6), ('ALB', 5), ('AUT', 5), ('PER', 4), ('BEL', 3)]
        
        >>> a = Country("ALB", "Albania", [], 0, 0.0, 0)
        >>> b = Country("AUT", "Austria", [], 0, 0.0, 0)
        >>> c = Country("BEL", "Belgium", [], 0, 0.0, 0)
        >>> d = Country("BOL", "Bolivia", [], 0, 0.0, 0)
        >>> e = Country("BRA", "Brazil", [], 0, 0.0, 0)
        >>> f = Country("IRL", "Ireland", [], 0, 0.0, 0)
        >>> g = Country("MAR", "Marocco", [], 0, 0.0, 0)
        >>> d = {a: 5, b: 5, c: 4, d: 10, e: 3, f: 5, g: 0}
        >>> t = Country.get_top_n(d, 5)
        >>> t == [('BOL', 10), ('ALB', 5), ('AUT', 5), ('IRL', 5), ('BEL', 4)]
        True
        
        >>> b = Country("BOL", "Bolivia", [], 0, 0.0, 0)
        >>> k = Country("SEN", "Senegal", [], 0, 0.0, 0)
        >>> l = Country("THA", "Thailand", [], 0, 0.0, 0)
        >>> d = {k: 1.1, b: 1.2, l: 9.5}
        >>> t = Country.get_top_n(d, 3)
        >>> t == [('THA', 9.5), ('BOL', 1.2), ('SEN', 1.1)]
        True
        
        >>> d = Country("COD", "Democratic Republic of Congo", [], 0, 0.0, 0)
        >>> c = Country("COM", "Comoros", [], 0, 0.0, 0)
        >>> d = {d: 1.1, c: 1.1}
        >>> t = Country.get_top_n(d, 3)
        >>> t
        [('COM', 1.1), ('COD', 1.1)]
        
        """
        dict_items = country_dict.items()
        list_of_tuples = list(dict_items)
        # First we order tuples from lowest to highest number 
        for i in range(len(list_of_tuples)):
            for x in range(len(list_of_tuples)-i-1):
                if list_of_tuples[x][1] > list_of_tuples[x+1][1]:
                    y = list_of_tuples[x]
                    list_of_tuples[x] = list_of_tuples[x+1]
                    list_of_tuples[x+1] = y
        # Then reverse the order so that the list goes from highest to lowest number            
        list_of_tuples = list_of_tuples[::-1]
        # Then we arrange tuples alphabetically IF numbers are equal
        # IMPORTANT: ARRANGEMENT IS BASED OFF COUNTRY NAMES
        for i in range(len(list_of_tuples)):
            for x in range(len(list_of_tuples)-i-1):
                if list_of_tuples[x][1] == list_of_tuples[x+1][1]:
                    if list_of_tuples[x][0].name > list_of_tuples[x+1][0].name:
                        y = list_of_tuples[x]
                        list_of_tuples[x] = list_of_tuples[x+1]
                        list_of_tuples[x+1] = y
        # Since tuples are immutable, we have to convert to list
        # That way we can change country object to country iso_code for final_list
        final_list = []
        for i, tup in enumerate(list_of_tuples):
            tup_list = list(tup)
            tup_list[0] = tup_list[0].iso_code
            tup = tuple(tup_list)
            final_list.append(tup)
            
        # Then we return the top 'n' values of the list by slicing 
        return final_list[:n]

def get_countries_from_file(file_name):
    """
    (str) -> dict
    
    This function takes a string (file_name) and returns a dictionary
    of iso_codes mapping to their corresponding Country objects.
    
    >>> d1 = get_countries_from_file("small_co2_data.tsv")
    >>> len(d1)
    9
    >>> str(d1['ALB'])
    'Albania\\tEUROPE\\t{2002: 3.748}\\t{2002: 3126000}'
    
    >>> d1 = get_countries_from_file("add_continents_test.tsv")
    >>> len(d1)
    1
    >>> d1['AAA'].continents
    ['EUROPE', 'NORTH AMERICA', 'SOUTH AMERICA']
    >>> d1['AAA'].co2_emissions
    {2001: 1.123}
    >>> d1['AAA'].population
    {2001: 123456789}
    
    >>> d1 = get_countries_from_file("another_add_continents_test_copy.tsv")
    >>> len(d1)
    192
    >>> str(d1['BBB'])
    'Friendland\\tOCEANIA\\t{2001: 11.67986}\\t{}'
    
    """
    # Because we know the order of the objects in the file
    # We can use split so that we can use specific indices
    fobj = open(file_name, "r", encoding="utf-8")
    iso_code_dict = {}
    for line in fobj:
        line = line.replace('\n','')
        line_list = line.split('\t')
        # Now we know index 0 is always iso_code
        iso_code = line_list[0]
        # Index 1 is always country name
        country_name = line_list[1]
        # Index 2 is continents, and we split to get a list
        continent = line_list[2].split(',')
        # Year must be an integer
        year = int(line_list[3])
        # If index 4 is empty, then co2_emissions = -1
        if line_list[4] != '':
            # Must be float
            co2_emission = float(line_list[4])
        else:
            co2_emission = -1
        # If index 5 is empty, then population = -1
        if line_list[5] != '':
            # Must be int
            population = int(line_list[5])
        else:
            population = -1
        if iso_code not in iso_code_dict:
            iso_code_dict[iso_code] = Country(iso_code, country_name, continent, year, co2_emission, population)
        else:
            # If a country is already in dictionary, then we use add_yearly method from earlier
            # We take slice from the list we made earlier as input for add_yearly method
            iso_code_dict[iso_code].add_yearly_data('\t'.join(line_list[3:]))
    fobj.close()
    return iso_code_dict