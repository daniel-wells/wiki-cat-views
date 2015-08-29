import requests
import re
import argparse
import unicodecsv

# Command Line Integration

parser = argparse.ArgumentParser(description='This script takes a wikipedia category name and outputs the view count (last 90 days) of each member in the category. For example for the Category:His_Dark_Materials type wiki-cat-views.py His_Dark_Materials')
parser.add_argument('Category_Name')
args = parser.parse_args()


# Get Category Members from MediaWikiAPI

req = {'action':'query', 'format':'json', 'list':'categorymembers', 'cmtitle':'', 'cmlimit':'max'};

req['cmtitle'] = "Category:" + args.Category_Name;

print req['cmtitle']

json_data = requests.get('http://en.wikipedia.org/w/api.php', params=req).json()

Total_Members = len(json_data["query"]["categorymembers"])

NameViewDict = {}

Member_Count = 0;

print 'Member: \tView Count: \tName:'

# For each member in the category get view count data from stats.grok.se

for Member in json_data["query"]["categorymembers"]:
	Member_Name = Member["title"]
	root_url = 'http://stats.grok.se/en/latest90/'
	response = requests.get(root_url + Member_Name)
	result = re.search('viewed (.*)\n', response.text)
	Member_Views = result.group(1)
	NameViewDict[Member_Name] = Member_Views;
	Member_Count = Member_Count + 1;
	Converted_Member_Name = Member_Name.encode('utf-8');
	print '{} of {} \t{} \t\t{}'.format(Member_Count, Total_Members, Member_Views, Converted_Member_Name)


# Write Name ViewCount pairs to csv fle

writer = unicodecsv.writer(open(args.Category_Name+'_View_Data.csv', 'wb'))
for key, value in NameViewDict.items():
   writer.writerow([key, value])

print '\nData Written to {}'.format(args.Category_Name+'_View_Data.csv')

