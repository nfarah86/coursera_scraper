class Categories_To_TSV(object):
    
    def __init__(self, category_dictionary):
        """ 
        initalize with dictionary from scraper.py
        """
        self.category_dictionary = category_dictionary
        print(category_dictionary)
        
    
    def put_categories_into_file(self):
        """ 
        Writes to data.tsv
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

