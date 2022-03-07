# Clean segments in a TM in excel format when they have unescaped entities and then remove html tags

import html
from isort import file
import pandas as pd
import sys
from bs4 import BeautifulSoup

def cleanHtml(path,column):

    mydata = pd.read_excel(path)

    #cast all records to str to avoid errors
    mydata[column] = mydata[column].apply(str)

    #create new column with the unescaped version of the series given and unescape the entities
    unescapedColumnName = column + "_unescaped"
   
    mydata[unescapedColumnName] = mydata[column].apply(html.unescape)

    #create new column with the tags removed from the unescaped column

    cleanColumnName = unescapedColumnName + "_noTags"

    mydata[cleanColumnName] = mydata[unescapedColumnName].apply(removeTags)
    
    mydata.to_excel(path)

    print("Done")

        

def removeTags(eltexto):

    removed = BeautifulSoup(eltexto, "html5lib").text
      
    return(removed)

#Parameters example to clean the en-us column in file.xlsx: cleanHtml.py "c:\thepath\to\the\file.xlsx" "en-us"
cleanHtml(sys.argv[1], sys.argv[2])

