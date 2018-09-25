#Python code to illustrate parsing of XML files
# importing the required modules
import csv
import requests
import xml.etree.ElementTree as ET

def loadRSS():

    # url of rss feed
    url = 'https://onlinebooks.library.upenn.edu/newrss.xml'

    # creating HTTP response object from given url
    resp = requests.get(url)

    # saving the xml file
    with open('onlinebooks.xml', 'wb') as f:
        f.write(resp.content)


def parseXML(xmlfile):

    # create element tree object
    tree = ET.parse(xmlfile)

    # get root element
    root = tree.getroot()

    # create empty list for news items
    newsitems = []

    # iterate book item
    for item in root.findall('./channel/item'):
        print(item)
        # empty news dictionary

        # append news dictionary to news items list
        newsitems.append(item)

    # return news items list
    return newsitems




def main():
    # load rss from web to update existing xml file
    loadRSS()

    # parse xml file
    newsitems = parseXML('onlinebooks.xml')
    # store news items in a csv file
    #savetoCSV(newsitems)


if __name__ == "__main__":

    # calling main function
    main()
