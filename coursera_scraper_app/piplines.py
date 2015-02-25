import csv
import models

def process_item_to_db(session):
    """ 
    Saves categories scraped into db
    """
    with open("./spiders/data.tsv", 'r') as category_reader:
        category_reader = csv.reader(category_reader, delimiter='\t')
        for line in category_reader:
            line[1] = line[1].replace('[', "").replace(']',"")
            organizations, authors, titles, start_date, duration = line
            #print (line)

            category = models.Category()
            category.organizations = organizations
            category.authors = authors
            category.titles = titles
            category.start_date = start_date
            category.duration = duration
            try:
              session.add(category)
              session.commit()
            except:
              session.rollback()
              raise
            finally:
              session.close()
            #return category

def main(session):
    process_item_to_db(session)
    
if __name__ == '__main__':
    session = models.connect()
    main(session)