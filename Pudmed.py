# Author: Femke Spaans
# Date: 23-04-2021
# Name: Afvink 2
# Version: 1

# says from the package biopython import the following module, which is in this case entrez
from Bio import Entrez

"""
Function to ask user for a searchword
"""


def user_input():
    searchword = input("Please enter the word on which you would like to perform a search:")
    return searchword


def info_pubmed(searchword):
    Entrez.email = "f.spaans@gmail3711.com"
    # set the Entrez tool parameter and by default, it is Biopython. you might wanna ask some clarification on this one
    Entrez.tool = 'Demoscript'
    # einfo function to find index term counts, last update, and available links for each database
    info = Entrez.esearch(db="pubmed", term=searchword)
    record = Entrez.read(info)
    count = record['Count']
    handle = Entrez.esearch(db="pubmed", term=searchword, retmax=count)
    record = Entrez.read(handle)
    id_list = record['IdList']
    return id_list


def number_of_hits(id_list):
    date_list = []
    years = []
    for id in id_list:
        handle = Entrez.esummary(db="pubmed", id=id)
        record = Entrez.read(handle)
        date_list.append(record[0]['PubDate'])
    for date in date_list:
        data = date.split(' ')
        years.append(data[0])
    return years


def sort_years(years):
    years.sort()
    print(years)
    print(years.type())
    #for i in range(0, len(years)):
    #    years[i] = int(years[i])
    #print(years)
    #for year in range(min(int_years), max(int_years), 5):
        #print(year)




