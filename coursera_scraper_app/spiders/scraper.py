from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from bs4 import BeautifulSoup
from lxml import html
import time
import re
import sys
import csv

class Crawler_Spider(object):
    
    def __init__(self, url):
        self.url = url

    def fetch_content(self):
        """
        This method creates a ClientObject and fetches
        all the html from the website 
        """
        print("We're fetching loading the browser!")
        driver = webdriver.Firefox()
        driver.get(self.url)
        time.sleep(10)
        click_loop = True
        while click_loop:
            try:
                print("we're loading")
                load_courses_link = driver.find_element_by_link_text('Load more courses...').click()
                time.sleep(10)
                print("we're finished loading")
            except NoSuchElementException:
                print("element doesn't exist")
                click_loop = False
        content_type = driver.page_source
        return(content_type)

class Parsing_Content(object):

    def __init__(self, content):
        self.content = content
        
    def parse_html(self):
        """
        This method gets the html scraped and turns it to
        soup
        """
        print("we're are printing the soup")
        soup = BeautifulSoup(self.content)
        #extracted some extraneous info before parsing through categories
        for extra_script in soup(["style", "script", "head", "title"]):
            extra_script.extract()    
        #print(soup.prettify())
        return soup


    def parse_coursera_categories(self, html_soup):
        """
        This method uses the soup to scrape through coursera categories 
        """
        count = 0
        print("Fetching categories")
        coursera_category_soup = html_soup.findAll(class_='c-courseList-entry-full')

        coursera_categories_dictionary = {}
        coursera_institution_list = []
        coursera_author_list =[]
        coursera_title_list = []
        coursera_date_list = []
        coursera_duration_list=[]

        for coursera_category in coursera_category_soup: 
            
            count += 1
            print(count)  
            #parses through organizations
            coursera_institutions = coursera_category.find(class_='c-courseList-entry-university').text          
            coursera_institution_list.append(str(coursera_institutions))
            #parses through authors
            coursera_instructor_links = coursera_category.findAll(attrs={"data-js": "instructor-link"})  
            coursera_instructors_mult_list = parse_multiple_instructors(coursera_instructor_links)
            coursera_author_list.append(coursera_instructors_mult_list)
            #parses through titles
            coursera_course_titles = coursera_category.find(attrs={"class":"c-courseList-entry-title"}).find(text=True)
            coursera_title_list.append(str(coursera_course_titles))
            #parses through start date and duration
            coursera_start_date_soup = coursera_category.findAll(class_='bt3-col-xs-3 bt3-text-right')
            coursera_date_string, coursera_duration_string = parse_start_dates(coursera_start_date_soup)
            coursera_date_list.append(str(coursera_date_string))
            coursera_date_list_filter =list(filter(lambda x:x!= '', coursera_date_list)) #filters empty strings
            coursera_duration_list.append(str(coursera_duration_string))
        
        coursera_categories_dictionary['organizations'] = coursera_institution_list
        coursera_categories_dictionary['authors'] = coursera_author_list 
        coursera_categories_dictionary['titles'] = coursera_title_list 
        coursera_categories_dictionary['start-dates'] = coursera_date_list_filter
        coursera_categories_dictionary['durations'] = coursera_duration_list
        
        print(coursera_categories_dictionary)
        return(coursera_categories_dictionary)

class Categories_To_CSV(object):
    
    def __init__(self, category_dictionary):
        """ 
        initalize with dictionary from scraper.py
        """
        self.category_dictionary = category_dictionary
        
    
    def put_categories_into_file(self):
        """ 
        logic that puts the contents of dictionary
        to rows and columns
        """
        result = zip(self.category_dictionary['organizations'], 
            self.category_dictionary['authors'], 
            self.category_dictionary['titles'], 
            self.category_dictionary['start-dates'], 
            self.category_dictionary['durations']
        )
        format_to_string_tabs = "{!s}\t{!s}\t{!s}\t{!s}\t{!s}"
        with open('data.tsv', 'w') as ofile: 
            for row in result:
                ofile.write((format_to_string_tabs .format(*row)))
                ofile.write('\n')

def parse_multiple_instructors(coursera_instructor_list):
    """
    This method puts multiple authors into a list
    """
    coursera_instructor_lists = []
    for coursera_instructor in coursera_instructor_list:
        coursera_instructor_lists.append(str(coursera_instructor.text))        
        if coursera_instructor_lists[0] == '': #special case no author listed
            coursera_instructor_lists.append("Unknown Author")
    coursera_instructor_lists_filter =list(filter(lambda x:x!= '', coursera_instructor_lists)) #filter empty strings
    return(coursera_instructor_lists_filter)  

def parse_start_dates(coursera_start_date_soup):
    """
    This method puts start dates and duration into a list
    """
    print("fetching start dates")
    for start_date in coursera_start_date_soup:
        start_date_p = start_date.p.extract()
        start_date_p_string = str(start_date_p).replace('<p class="c-courseList-entry-noOpenSessions">', "").replace("</p>","").replace('<p class="c-courseList-entry-tagline">',"").replace("<p>", "")
        start_date_p_string_list = start_date_p_string.split('<br/>')
        if len(start_date_p_string_list) == 1: #exception for no duration portion on coursera list
            start_date_p_string_list.append("Indeterminate Duration")
    return(start_date_p_string_list)
        
def main():
    #creates clientObject and fetches html
    crawl_object = Crawler_Spider("https://www.coursera.org/courses?languages=en")
    content_object = crawl_object.fetch_content()
    
    #turns html to soup
    parsing_object = Parsing_Content(content_object)
    soup_object = parsing_object.parse_html()
    
    #grabs categories passing soup object
    category_object = Parsing_Content(content_object)
    category_dictionary = category_object.parse_coursera_categories(soup_object)

    #take categories and puts them into .csv doc
    category_object = Categories_To_CSV(category_dictionary)
    category_file_object = category_object.put_categories_into_file()

if __name__ == '__main__':
    main()





