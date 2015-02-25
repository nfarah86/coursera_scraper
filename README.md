# Coursera Scraper App.... Scrapin' Away...

1. [Synopsis](#synopsis)

2. [Project Information](#project-information)

3. [Technologies Used](#technologies-used)

4. [How to run this town....(I mean script)](#technologies-used)

5. [License](#license)

## Synopsis

Want to find out what new and hip courses are out in Coursera? Want to see what Coursera is offering?  Hopefully Coursera doesn't change their page structure, otherwise this fabulous program will scrape https://www.coursera.org/courses?languages=en for the organization, author, title, start date, and duration. 

## Project Information
The coursera scraper has a couple of components to it (see below). This scraper downloads the asynchronus Coursera course page by mimicking browser behavior. The data is then stored in PosgreSQL defined by the SQLalchemy schema.
   
* scraper
* model 
* seed


##Executing script
*Fork this repo
*cd coursera_scraper_app/spiders
*pip install -r requirements.txt
*python scraper.py
*DOWNLOAD POSTGRES
*(uncomment line in main(),  python seed.py  This initializes db tables, 
*Then comment same line in main(),  python seed.py
*See POSTGRES docs for more info on queries and the likes

## Technologies Used
* Python 3.4.2
* PostgreSQL
* Selenium
* BeautifulSoup
* SQLAlchemy 

## License
Private end-user license agreement