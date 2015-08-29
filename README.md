Wikipedia Category Page Views
======
This script retrieves the view count (traffic statistics) for each page in a given Wikipedia category. From this you can determine which page / member of the category is most popular. For example:

```
$ python wiki-cat-views.py His_Dark_Materials
```
Will return:
```
Category:His_Dark_Materials
Member: 	View Count: 	Name:
1 of 12 	6927 		Dæmon (His Dark Materials)
2 of 12 	3629 		Dust (His Dark Materials)
3 of 12 	69268 		The Golden Compass (film)
4 of 12 	3793 		The Golden Compass (video game)
5 of 12 	55980 		His Dark Materials
6 of 12 	2322 		His Dark Materials (play)
7 of 12 	547 		Jordan College, Oxford
8 of 12 	1945 		Locations in His Dark Materials
9 of 12 	1287 		Republic of Heaven
10 of 12 	230 		Template:His Dark Materials
11 of 12 	354 		Category:His Dark Materials books
12 of 12 	274 		Category:His Dark Materials characters

Data Written to His_Dark_Materials_View_Data.csv
```
Note that the View Count and Name of each page is written to a csv file for easy further processing.

The view count is the from the last 90 days of the english Wikipedia article, scraped from http://stats.grok.se

## Limitations
This script currently only works for the first 500 pages in a given category due to a limitation of the MediaWiki API.

It can also be quite slow!

## Installation
This is a Python script written using Python 2.7.6 on OXS Yosemite (10.10.4).

The script uses the following non-standard libraries: requests and unicodecsv.

To instal download get-pip.py from (https://pip.pypa.io/en/latest/installing.html), then:
```
$ python get-pip.py
$ pip install requests unicodecsv
```

## Version 
* Version 1.0

## Alternatives
http://tools.wmflabs.org/glamtools/treeviews/

## Contact
#### Developer
* Homepage: [danielwells.me](http://www.danielwells.me)
* Twitter: [@DanielJohnWells](https://twitter.com/DanielJohnWells "Daniel Wells on twitter")