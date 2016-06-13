# Research
My Undergraduate Research with Professor Dong Wang

Notes for 6/13/2016
- (10:42) Info window now displays number of people currently at a venue, according to Foursquare data, and a recent comment about the venue posted to its Foursquare profile
- (9:05) Started working on some additional features that can be used from Foursquare, such as number of people currently "checked in" and a recent user comment

Notes for 6/10/2016
- (4:42) Began a more thorough reading of the Instagram API. It might be possible to utilize the Instagram API, afterall, but it will require a much better understanding of it, other than a cursory reading
- (4:14) Instagram is going to have to be implemented due to the need for data diversity in the application
- (3:58) Going to look into ways that Instagram data can be used, perhaps outside of the API, although that does not seem likely
- (3:53) Unfortunately, after running many searches in different cities across the United States, most venues only have social media accounts on sites such as Facebook, Twitter, and Instagram; I have yet to find one with a link to Pinterest, whereas I consistently find links to Instagram
- (2:57) In order to access more of the data on Instagram, such as users' content other than my own, my application must receive approval from Instagram. The approval process only reviews apps that are final and production version apps. Using Instagram seems to be more trouble than it's worth, and I will begin moving towards using a more open API
- (2:22) In the meantime, I have manually obtained an access token, but plan on developing a way to programmatically generate one per user request
- (2:12) There does not seem to be a good way to programmatically obtain an Instagram access token, which feels necessary, as Instagram has pointed out that they can expire (they also failed to provide a timetable for when it would expire)
- (12:13) Generating an access token for Instagram is proving to be difficult, as it requires user approval for a server-side process; will continue to explore ways to obtain access token
- (11:39) The authentication process that is required for Instagram is much more involved than simply using the ClientID and ClientSecret. An access token must be generated through the ClientID, and the user must approve the application, thereby generating the token
- (9:02) Began learning to use Instagram API

Notes for 6/9/2016
- (4:59) Finished some very basic groundwork for an Instagram data crawlewr. Must explore it more in depth tomorrow to begin effectively using the Instagram info, which is obtained the same way as the Twitter username information
- (3:37) Added an Instagram tab to the info window
- (3:16) Successfully enabled adding a newline between each tweet; needed to use html methods, such as adding <br> to the tweet so that the info window string could properly format
- (1:52) Continuing to have issues getting the tweets to be on their own line
- (12:25) Seems to be an issue with the way it is processed when using content string, as when I use alerts to check if each Tweet has its own line, they, in fact, do, but when I check the info window, it is one, long, consecutive string
- (12:05) Recent tweets are easily obtained and sent to the client, but there remains the issue of the tweets not appearing on their own line
- (9:05) Resumed work on including recent Tweets in the current application

Notes for 6/8/2016
- (4:23) Plans for tomorrow include beginning to implement another social media dataset into the application. At the very least, work will begin on getting a very basic understanding of another social media's API. Most likely candidates at this point include Instagram and Pinterest, as a venue's actual appearance might be something users would want to know. Also, tomorrow will potentially entail the return of recent tweets by a venue's Twitter account
- (4:21) Successfully moved the Twitter data crawl to one function and one set of for loops; it appears to have sped up the process, although my recent tests of the network here on campus have shown that the internet speeds are back to their usual, fast speeds, so that possibly played a part in the apparent improvement in speed of the Twitter data crawl. 
- (3:51) Continuing to work on improving the speed of the Twitter data crawler
- (11:51) Planning on thoroughly commenting my code, as I have fallen behind on that. Also, considering moving the Twitter data crawl into one function, as it currently attempts to find all possible Twitter screennames before getting the Twitter account information, making it loop an additional time, essentially
- (11:01) No good way to determine if urls provided by Foursquare are bad or not. Will investigate ways to ensure that the response.get does not wait for long periods of time for a bad link. Currently just prohibiting the script from trying to connect to certain sites I have determined are bad
- (10:15) During testing, determined that certain Foursquare provided urls are broken, but do not get detected by a GET request for quite some time, if at all
- (9:19) Added the ability to click on the venue's Twitter screenname

Notes for 6/7/2016
- (4:12) Continuing to look for ways to expedite the web crawling process
- (3:37) Client-server model with two requests to the server now works, although the Twitter info takes a long time to get, probably due to web crawling. Will continue to explore faster methods of finding Twitter links on a venue's url
- (2:08) Client currently makes two requests to the server; the first request results in the Foursquare data, which, upon being received, causes the client to request the Twitter data
- (12:07) Currently debugging the POST request made by the client for the Twitter info; steady progress is being made and this should result in faster responses as the server does not have to make as many nested calls for a single request, meaning that the Foursquare data can be returned and then the client can ask the server for Twitter data
- (9:07) Began the process of optimiziing current client-server version of data crawler, as there is an undesirable time delay between when the user hits refresh and the new results appear; will attempt to split the script into separate requests from the server

Notes for 6/6/2016
- (4:08) Began exploring the Instagram API options as the next social media site to integrate into the application
- (3:37) Very basic version of multi-tabbed info windows is now working
- (2:32) Continuing to explore different ways to present the Twitter information
- (12:15) Opted to removed displaying account information, as the user probably cares more about what people are saying about venue than how many followers, etc. a venue has
- (10:42) The venues' Twitter accounts, if available, are now presented in the info window. Currently looking into ways to show recent tweets
- (9:05) Resumed work on cleaning up the tabbed infowindow

Notes for 6/3/2016
- (4:45) Finally got a very sloppy, basic version of a tabbed infowindow working. Next step is to put the Twitter related data into the Twitter tap
- (4:01) It seems to be a versioning or linking issue that's preventing the tabs from behaving properly. Will continue to investigate
- (3:43) I've continued to experience problems with jQuery, but I am confident this is the best method for including large amounts of information regarding a venue; the infowindows need to be as compact as possible
- (12:00) Currently attempting to use jQuery to add tabs to the Infowindows; running into some issues, but this seems like the best approach
- (9:05) Resumed determining best method for displaying Twitter info

Notes for 6/2/2016
- (4:41) Began exploring ways to display the Twitter information; considering putting some of it inside the InfoWindows directly on the Googlemap, depending on the availability of "pages" inside InfoWindows. Other options include including putting a text window beside the Googlemap
- (4:38) Bug fixed. Was grabbing more than just the text in each status, making it not JSON serializable
- (4:18) Server now successfully sends the account information of each venue's Twitter; there's a bug that is preventing me from sending a list containing a Twitter's recent statuses, and I'm currently looking for a way to still include this information
- (3:56) Client-server version now works much more quickly. Working on the best approach to sending the Twitter data back to the web page
- (2:57) Bad Twitter link bug solved - hopefully
- (2:52) Successfully only searching for Twitter urls on the home page; currently working on a bug where a Twitter link cannot be cleanly separated in order to obtain the user name
- (1:40) Removed the 'Section' parameter from the basic Foursquare data crawler and began looking into faster web crawling methods
- (12:04) When I attempted to add the Twitter crawler to the client-server version, response times increased greatly depending on what kind of search was made. Through testing, I've determined that the 'Section' parameter for Foursquare often returns the same results, even if a different category is chosen. Further, some of the venues' websites are bad links, causing the web crawler to wait for a timeout, or the websites have many nested pages, meaning I need to limit how many pages the web crawler will search for a Twitter link. Truthfully, a venue will most likely have a link to its Twitter account on the mainpage, so I will explore this further. I plan to git reset this directory because I want a fresh start following lunch.
- (9:05) Resumed work on adding Twitter data to the client-server version

Notes for 6/1/2016
- (4:31) Other goals for the next week are to add an upload button the mobile app to allow for greater testing, as well as the added ability for users to view already taken photos
- (4:00) Currently looking into the best approach to integrating the new basic data crawler with the webpage version. Issue of formatting the data sent back by the python script as well as what HTML element to use. Will investigate in greater depth on Thursday and Friday.
- (12:27) Datacrawler now gets a list of venues through Foursquare, uses the websites provided to find a Twitter account, and then displays information related to each venue's Twitter
- (11:05) Successfully crawling a venue's website, should it have one, and obtaining the venue's Twitter account, should it have one
- (9:11) Began looking into ways to pull urls from a webpage. BeautifulSoup appears to be a common and efficient way of parsing a webpage for desired information

Notes for 5/31/2016
- (4:33) There does not seem to be an easy way to go from a venue's Foursquare profile to its Twitter profile. The first solution I can think of is to use Foursquare to find the venue's website and check it for a link to its Twitter; mildly tedious, but it seems to be the "best" option at this point
- (4:10) Next step is to attempt to find Twitter accounts for the venues captured by Foursquare data crawler; current use of Twitter is a live feed of Tweets in the area
- (3:55) Fixed the issue of Tweets being compared in lower case against strings that have varied case
- (3:10) Tweets are now accepted if they contain something matching the section or query aspect of the Foursquare search
- (2:40) Tweets are now accepted as relevant if they contain a venue's name or a venue's category. The next step is to include the search parameters of the Foursquare data crawl, such as food, outdoors, coffee, etc.
- (1:45) Began constraining the Tweets that are accepted to those that contain the names of the venues obtained by the Foursquare Data Crawler
- (12:33) Kept running into errors; determined I was hitting rate limits. Planning on exploring ways to avoid hitting rate limits. Also will continue to improve upon the Tweets that are collected
- (9:05) Continuing work on the Twitter Stream

Notes for 5/30/2016
- (5:10) Currently have a very basic version of a Twitter stream that relates to the location of the Foursquare search
- (3:04) Successfully completed Task 3 of Assignment 1. Will now begin attempting to integrate the Foursquare Data Crawler and a basic Twitter Data Crawler
- (12:24) Successfully completed Tasks 1 and 2 of Assignment 1 from Dr. Wang's Social Sensing course. Task 3 might not be as necessary to become familiar with, as that's what the Foursquare Data Crawler does: explore a given area. I suppose an additional stream of data could be useful in addition to the data Foursquare obtains; that stream of data would be in addition to the map that Foursquare generates.
- (9:09) Began exploring the Twitter API in order to begin data diversification

Notes for 5/27/2016
- (4:20) Tentatively will claim that the application successfully geotags photos that do not have that feature enabled. I need to ensure that the EXIF data is permanently modified through SetAttribute(), which the documentation seems to indicate. Nevertheless, a very basic Geotagging Photo Application is complete, in that the application requires the user to enable Location Services, and, if the user uses the built-in geotagging features, simply displays the photo and its EXIF data, otherwise, it manually sets the photos EXIF Latitude and Longitude
- (2:57) Successfully obtaining the latitude and longitude of the device
- (10:48) Successfully obtaining the EXIF data when the user takes a photo
- (9:13) Opting to remove the ability for the user to select an old photo, as there's no way for the app to generate an accurate geotag should it not have one already. Further, Camera intent should work fine, the phone's geolocation need only be obtained as the picture is taken, at which point the app will then modify the EXIF data.

Notes for 5/26/2016
- (4:57) For tomorrow:
	- Determine a photo's filename
	- If photo was just taken, write the lat and long to the photo's EXIF data
- (4:27) EXIF Info that every image is stored with will be the best approach. App will allow the user to select a picture already taken, or to take a new one. It should then check for geolocation information in the EXIF Info, and, if there, should accept the photo; otherwise, the app should reject the user's photo.
- (4:12) Standard Camera App's geotagging ability cannot be programmatically enabled. This means that simply using an Intent in Android Studio will not suffice. Must completely explore the Android Camera API
- (12:36) Spent the morning reworking the Camera application. Application now operates very basically, allowing the user to either select a picture already on the phone, or to take a new one. The next step is to enforce the user to enable location services for the camera application

Notes for 5/25/2016
- (4:46) Found a lengthy tutorial on uploading photos to a server. Will explore in more detail tomorrow
- (4:39) Standard Camera App on Android devices can already enable location embedding, as it turns out. Previous work on BasicCameraApp is unnecessary, and a new project will be started, which will simply utilize the already existing camera application to take the photos, but send them to an online directory, instead of saving them locally.
- (3:30) Resumed work on the mobile application
- *(1:52) Next steps: GPS based search, and move towards data diversification*
- (1:41) Resolved minor bug of markers not clearing.
- (12:33) Python server successfully runs the script and sends the desired information to the client. Small issue remains where old markers need to be deleted upon starting a new search. Should be a simple fix
- (10:17) Web page successfully interacts with the Python server. Next step is adding data crawler script to the server

Notes for 5/24/2016
- (5:20) Prior data crawler remains untouched (besides minor quality of life update this morning)
- (5:15) Began turning Python script into server. Tomorrow will entail continuing that effort by finishing the server's ability to process requests and then send the results back, which the JS will then use to generate the proper map.
- (12:10) Basic webpage has been setup. Next step is changing the Python script to JavaScript
- (9:33) Planning on moving from simple Python script to interactive webpage; Python script might need to be turned into JS
- Removed URL from venues that do not have one

Notes for 4/20/2016
- Added venues' phone numbers to the infowindow
- Images provided by Foursquare seem to be bad links
- Hours of operation are also unreliable on Foursquare
- Explore Twitter API, Flickr, and Facebook for additional data
- Add GPS search
- GPS Photo-App

Notes for 4/18/2016
- Fell behind in consistently working on the application as I became bogged down by assignments in other courses
- Successfully added venues' websites to the infowindow, including making them a hyperlink
- Also began to refine the search process by adding try-except blocks
- Next step is to continue to improve the range of the search function by revisiting the features of the Foursquare API
- Also, explore the JSON datasets to determine other pertinent information to go into the infowindows.
- Long-term, use the Foursquare data to jump to other social media sites for extra data

Notes for 4/6/2016
- Moved API keys into a text file to prevent access to them on Github
- Ran into a minor issue getting information about a location, such as likes, because not all venues contain those indices
- Added information like steet address to info box. Next step would be links to websites, as well as Facebook and Twitter pages
- Added the venue's rating to the info window

Notes for 3/30/2016
- Markers' info box now correctly displays venues Name
- Must implement method to include important information regarding venue in the body of the info box
- Explore how to use gitignore to store things like API Keys

Notes for 3/23/2016
- Markers are displayed with an info box
- Markers' locations determined by dataset
- Info box does not contain info regarding the dataset

Notes for 3/15/2016
- Successfully have the data crawler also write the html file
- Currently working on getting the dataset to be written to the html file

Notes for 3/2/2016
- Must develop function to loop through all elements of array of dataset
- Must find way to get dataset created from Python script into an html object



