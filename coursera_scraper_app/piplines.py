from sqlalchemy.orm import sessionmaker
import models
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
        category = Category(**item)

        with open("./spiders/data.tsv", 'r') as category_reader:
            category_reader = csv.reader(category_reader, delimiter='\t')
            for line in category_reader:
                line[1] = line[1].replace('[', "").replace(']',"")
                organizations, authors, titles, start_date, duration = line
                print (line)

        # try:
        #   session.add(category)
        #   session.commit()
        # except:
        #   session.rollback()
        #   raise
        # finally:
        #   session.close()
        # return item

def main():
    w_text = Coursera_Pipline()
    print_text = w_text.process_item_to_db()

if __name__ == '__main__':
    main()
