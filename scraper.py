# This is a template for a Python scraper on morph.io (https://morph.io)
# including some code snippets below that you should find helpful

import scraperwiki
import lxml.html
#
# # Read in a page
html = scraperwiki.scrape("https://uk.soccerway.com/teams/england/chelsea-football-club/661/")

# creates an empty dictionary variable to hold our data later
# format is something like {"name" : "Adam", "age" : 18, etc}
record = {}

#
# # Find something on the page using css selectors
root = lxml.html.fromstring(html)
#names = root.cssselect("td div a")
#for i in names:
  # print i.attrib['href']
  # print i.text.encode("ascii", "ignore")
  # record['link'] = i.attrib['href']
  # record['name'] = i.text.encode("ascii", "ignore")
  # print record
  # scraperwiki.sqlite.save(unique_keys=['link'], data=record) # this saves the data in a way you can download it.

players = root.cssselect("td")
print players

for i in players:
  print i.attrib

  
  

  


#
# # Write out to the sqlite database using scraperwiki library
# scraperwiki.sqlite.save(unique_keys=['name'], data={"name": "susan", "occupation": "software developer"})
#
# # An arbitrary query against the database
# scraperwiki.sql.select("* from data where 'name'='peter'")

# You don't have to do things with the ScraperWiki and lxml libraries.
# You can use whatever libraries you want: https://morph.io/documentation/python
# All that matters is that your final data is written to an SQLite database
# called "data.sqlite" in the current working directory which has at least a table
# called "data".
