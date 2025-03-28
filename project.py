#gather what we need
import csv
from collections import Counter
import matplotlib.pyplot as plt

#where the magic happens
def get_data():
  file = open('global_shark_attacks.csv', 'r')
  reader = csv.DictReader(file)
  data = []
  for i in reader:
    data.append(i)
  return data

data = get_data()

def getTopNYears(dataset, n):
  years = []
  for row in dataset:
    year = row.get('year')
    year = year[:-2]
    if year.isdigit():
        years.append(year)
  yearCounter = Counter(years)
  return (yearCounter.most_common(int(n)))

def getTopNCountries(dataset, n):
  countries = []
  for row in dataset:
    country = row.get('country')
    if country.isalpha():
        countries.append(country)
  countryCounter = Counter(countries)
  return countryCounter.most_common(int(n))

def getCauses(dataset):
    causes = []
    for row in dataset:
        cause = row.get('type')
        proper = True
        alpha = 'abcdefghijklmnopqrstuvwxyz '
        for i in cause:
            if i.lower() not in alpha:
                proper = False
        if cause == 'Invalid':
            causes.append('Other')
        else:
            if proper == True:
                causes.append(cause)
    causeCounter = Counter(causes)
    return causeCounter

def sexStats(dataset):
    sexlist = []
    for row in dataset:
        sex = row.get('sex')
        if sex == 'M':
            sexlist.append('Male')
        if sex == 'F':
            sexlist.append('Female')
    sexcounter = Counter(sexlist)
    sexcount = []
    for i in sexcounter:
        sexcount.append(f'{i}: {sexcounter[i]}')
    return sexcount

def fatality(dataset):
    fatalities = []
    for row in dataset:
        fatal = row.get('fatal_y_n')
        if fatal == 'Y':
            fatalities.append('Fatal')
        if fatal == 'N':
            fatalities.append('Nonfatal')
    fatalcounter = Counter(fatalities)
    fatalcount = []
    for i in fatalcounter:
        fatalcount.append(f'{i}: {fatalcounter[i]}')
    return fatalcount

def getOldestYear(dataset):
    years = []
    smol = float('inf')
    for row in dataset:
        year = row.get('year')
        year = year[:-2]
        if year.isdigit():
            years.append(int(year))
    for i in years:
        if i < smol and i != 1:
            smol = i
    return smol

def getNewestYear(dataset):
    years = []
    big = float('-inf')
    for row in dataset:
        year = row.get('year')
        year = year[:-2]
        if year.isdigit():
            years.append(int(year))
    for i in years:
        if i > big:
            big = i
    return big

def getYearStats(dataset, n):
    L = []
    for row in dataset:
        year = row.get('year')
        if year[:-2] == str(n):
            L.append(row)
    return L

def yearStats(dataset):
    L = []
    fatalities = []
    sexlist = []
    count = len(dataset)
    #fatalities in that year
    for row in dataset:
        fatal = row.get('fatal_y_n')
        if fatal == 'Y':
            fatalities.append('Fatal')
        if fatal == 'N':
            fatalities.append('Nonfatal')
    fatalcounter = Counter(fatalities)
    fatalcount = []
    for i in fatalcounter:
        fatalcount.append(f'{i}: {fatalcounter[i]}')
    L.append(fatalcount)
    #sex stats in that year
    for row in dataset:
        sex = row.get('sex')
        if sex == 'M':
            sexlist.append('Male')
        if sex == 'F':
            sexlist.append('Female')
    sexcounter = Counter(sexlist)
    sexcount = []
    for i in sexcounter:
        sexcount.append(f'{i}: {sexcounter[i]}')
    L.append(sexcount)
    #country with most
    countries = []
    for row in dataset:
        country = row.get('country')
        if country.isalpha():
            countries.append(country)
    countryCounter = Counter(countries)

    counttuple = countryCounter.most_common(int(1))
    #returns a list of tuples, so have to make sure to inclued the [0 when unpacking]
    topcountry, attacks = counttuple[0]
    L.append(f"The country with the most shark attacks this year was {topcountry} with {attacks} attacks")
    L.append(f'Total number of attacks this year was {count}')
    return L

def setofyears(dataset):
    years = []
    for row in dataset:
        year = row.get('year')
        year = year[:-2]
        if year.isdigit():
           years.append(year)
    years = set(years)
    return years

def getCountryStats(dataset, n):
    L = []
    for row in dataset:
        country = row.get('country')
        if country.lower() == n.lower():
            L.append(row)
    return L

def countryStats(dataset):
    L = []
    fatalities = []
    sexlist = []
    count = len(dataset)

    #fatalities in that country
    for row in dataset:
        fatal = row.get('fatal_y_n')
        if fatal == 'Y':
            fatalities.append('Fatal')
        if fatal == 'N':
            fatalities.append('Nonfatal')
    fatalcounter = Counter(fatalities)
    fatalcount = []
    for i in fatalcounter:
        fatalcount.append(f'{i}: {fatalcounter[i]}')
    L.append(fatalcount)
    #sex stats in that country
    for row in dataset:
        sex = row.get('sex')
        if sex == 'M':
            sexlist.append('Male')
        if sex == 'F':
            sexlist.append('Female')
    sexcounter = Counter(sexlist)
    sexcount = []
    for i in sexcounter:
        sexcount.append(f'{i}: {sexcounter[i]}')
    L.append(sexcount)
    #year with most
    years = []
    for row in dataset:
        year = row.get('year')
        year = year[:-2]
        if year.isdigit():
            years.append(year)
    yearCounter = Counter(years)
    counttuple = yearCounter.most_common(1)
    #returns a list of tuples, so have to make sure to inclued the [0 when unpacking]
    topyear, attacks = counttuple[0]
    L.append(f"The year with the most shark attacks in this country was {topyear} with {attacks} attacks")
    L.append(f'Total number of attacks in this country is {count}')
    return L


def setofcountries(dataset):
    countries = []
    for row in dataset:
        country = row.get('country')
        if country.isalpha():
            countries.append(country.lower())
    countries = set(countries)
    return countries

def getgraph(dataset, n):
    L = []
    for row in dataset:
        country = row.get('country')
        if country.lower() == n.lower():
            L.append(row)
    return L

def graph(dataset):
    x = []
    y = []
    years = []
    for row in dataset:
        year = row.get('year')
        year = year[:-2]
        if year.isdigit():
            years.append(year)
    yearCounter = Counter(years)
    for i in yearCounter.keys():
      x.append(i)
    for i in yearCounter.values():
      y.append(i)
    x = x[::-1]
    y = y[::-1]
    plt.plot(x, y, label='Sharks')




#make it look pretty
def main():
    print('Data Analysis Options:')
    print('1) Years with most shark attacks \n2) Countries with most shark attacks \n3) Causes recorded \n4) Sex of individuals attacked \n5) Fatal Vs non-fatal atacks \n6) Oldest recorded year with an attack \n7) Most recent recorded year with an attack \n8) Statistics of a specific year \n9) Statistics of a specific country\n10) Create a graph of shark attacks over years in a country\n0) Exit')
    select = input('Please select an analysis option:')
    options = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
    while select not in options:
        select = input('Make sure your input is a number on the list of options:')
    else:
        if int(select) == 1:
            n = input('How many years would you like to view:')
            print( f'The top {n} years with the most shark attacks are: {getTopNYears(data, n)}' )
            next = input('Continue analysis? (y/n)')
            if next == 'y':
                main()
        elif int(select) == 2:
            n = input('How many countries would you like to view:')
            print( f'The top {n} countries with the most shark attacks are: {getTopNCountries(data, n)}' )
            next = input('Continue analysis? (y/n)')
            if next == 'y':
                main()

        elif int(select) == 3:
            print(getCauses(data))
            next = input('Continue analysis? (y/n)')
            if next == 'y':
                main()
        elif int(select) == 4:
            print(sexStats(data))
            next = input('Continue analysis? (y/n)')
            if next == 'y':
                main()
        elif int(select) == 5:
            print(fatality(data))
            next = input('Continue analysis? (y/n)')
            if next == 'y':
                main()

        elif int(select) == 6:
            print(f"The oldest recorded year with a shark attack is: {getOldestYear(data)}")
            next = input('Continue analysis? (y/n)')
            if next == 'y':
                main()
        elif int(select) == 7:
            print(f"The most recent recorded year with a shark attack is: {getNewestYear(data)}")
            next = input('Continue analysis? (y/n)')
            if next == 'y':
                main()
        elif int(select) == 8:
            year = input('What year would you like to look at (1000 - 2023): ')
            while year not in setofyears(data):
                year = input('Please select a valid year between 1000 and 2023: ')
            else:
                print('Fatalities:')
                print(yearStats(getYearStats(data, year))[0])
                print('Sex of victims:')
                print(yearStats(getYearStats(data, year))[1])
                print(yearStats(getYearStats(data, year))[2])
                print(yearStats(getYearStats(data, year))[3])
                next = input('Continue analysis? (y/n)')
                if next == 'y':
                  main()
        elif int(select) == 9:
            country = input('What country would you like to look at:')
            while country.lower() not in setofcountries(data):
                country = input('This country either isnt in the data set, or you have intered it in incorrectly. would you like a list of valid countries? (y/n)')
                if country == 'y':
                    for i in setofcountries(data):
                        print(i.capitalize())
                if country == 'n':
                    country = input('What country would you like to look at:')
            else:
                print('Fatalities:')
                print(countryStats(getCountryStats(data, country))[0])
                print('Sex of victims:')
                print(countryStats(getCountryStats(data, country))[1])
                print(countryStats(getCountryStats(data, country))[2])
                print(countryStats(getCountryStats(data, country))[3])
                next = input('Continue analysis? (y/n)')
                if next == 'y':
                  main()
        elif int(select) == 10:
            country = input('What country would you like to look at:')
            while country.lower() not in setofcountries(data):
                country = input('This country either isnt in the data set, or you have intered it in incorrectly. would you like a list of valid countries? (y/n)')
                if country == 'y':
                    for i in setofcountries(data):
                        print(i.capitalize())
                if country == 'n':
                    country = input('What country would you like to look at:')
            else:
              graph(getgraph(data, country))
        elif int(select) == 0:
            pass

main()
