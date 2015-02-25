from sqlalchemy.orm import sessionmaker
from models import db_connect, Category, create_categories_table
import csv


class Coursera_Pipline(object):
    """
     Coursera pipeline for storing
     scraped items into db
     """
    
    def __init__(self):
        engine = db_connect()
        create_categories_table(engine)
        self.Session = sessionmaker(bind = engine,
                                        autocommit = False,
                                        autoflush = False)

    def process_item_to_db(self):
        """ 
        Saves categories scraped into db
        """
        session = self.Session()

        with open("./spiders/data.tsv", 'r') as category_reader:
            category_reader = csv.reader(category_reader, delimiter='\t')
            for line in category_reader:
                line[1] = line[1].replace('[', "").replace(']',"")
                organizations, authors, titles, start_date, duration = line
                #print (line)

                category = model.Category()
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
        return category

def main():
    w_text = Coursera_Pipline()
    print_text = w_text.process_item_to_db()

if __name__ == '__main__':
    main()
