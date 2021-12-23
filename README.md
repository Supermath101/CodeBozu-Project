# CodeBozu-Project

#Deliverable 1
For this deliverable, we used:
- the 'lxml' parser from the beautiful soup 4 library
- pandas (to create the csv file)
- requests (to request data from a site)
- regex (to find the information we wanted to scrape

We created a separate file for the subroutines that scraped the data and created the csv file (by the name of Bio_Data.py).

To scrape the data, regex to select the data that suited our needs. The data was selected from a table on each wikipedia page. This table was found by inspecting the html code and using the find_all() function. 

While scraping the data, we encountered a bug that did not allow the location of birth to be stored correctly (as some of the location of the birth of some presidents contained one or more hyperlinks). This issue was resolved by the use of a list to collect all the linked and non-linked places making up the location of birth of a president.

Once the data was extracted, we made a csv file by utilising the pandas library.  
