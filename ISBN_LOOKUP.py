import isbnlib
from numpy import genfromtxt
import pandas as pd
from isbnlib.dev._exceptions import NoDataForSelectorError

# get the isbn's in a numpy array so we can iterate, use str variable to input into isbnlib.meta(), change the file path accordingly
data = genfromtxt('/home/mobius/Documents/Data Analysis/ISBN_Lookup/ISBN_CSV.csv', dtype=str, delimiter=',')

# loop through isbn's, fetching title and author
diz = []
for isbns in data:

    #try this if isbn is found
    try:
        book = isbnlib.meta(isbns)
        title = book['Title']
        authors = book['Authors']
        diz.append({'ISBN': isbns, 'Title': title, 'Author': authors})

    # exception for if isbn is not found
    except NoDataForSelectorError:
        title = 'Not Found'
        authors = 'Not Found'
        diz.append({'ISBN': isbns, 'Title': title, 'Author': authors})

# put data into a pandas dataframe for easy processing into csv
dizn = pd.DataFrame(diz, columns=('ISBN', 'Title', 'Author'))
# produce a csv file containing the contents of the dataframe dizn
dizn.to_csv('/home/mobius/Documents/Data Analysis/ISBN_Lookup/ISBN_Data.csv')



