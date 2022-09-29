from pprint import pprint
from facebook_scraper import _scraper
from facebook_scraper import *
from facebook_scraper.fb_types import Page
import json
from json_filter import filter_json


set_cookies("cookie.json")   #setting the cookies
MyPages = ['EchorouknewsTV/?_rdc=2&_rdr']   #List of pages to scrap
posts = 3    #number of posts to scrap in a page
final_list = [] #List that contains posts' details

for i in range (0,len(MyPages)):   #Looping through different pages

     print('****************************** Scraping {} ****************************** \n'.format(MyPages[i]))

     for post in get_posts(MyPages[i], pages=posts):    #Looping through posts
               post_id = post["post_id"] #Extract post id from post
               post_details = next(get_posts(post_urls=[post_id], options={"comments": True, "reactions": True }))
               final_list.append(post_details)
     json_string = json.dumps(final_list, indent=4, default=str)  #Storing data in a JSON file
     MyFile = "json_data_"+MyPages[i]+".json"   #Creating a new file with the page id
     with open(MyFile,'w') as outfile:  
               outfile.write(json_string)
     pprint(final_list)  #print the results
     filter_json(MyFile)    #Filtering JSON output and spliting it to 3 files (Posts, Comments, Replies)

 



  
