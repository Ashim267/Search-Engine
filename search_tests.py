from search import keyword_to_titles, title_to_info, search, article_length,key_by_author, filter_to_author, filter_out, articles_from_year
from search_tests_helper import get_print, print_basic, print_advanced, print_advanced_option
from wiki import article_metadata
from unittest.mock import patch
from unittest import TestCase, main

class TestSearch(TestCase):

    ##############
    # UNIT TESTS #
    ##############

    def test_example_unit_test(self):
        dummy_keyword_dict = {
            'cat': ['title1', 'title2', 'title3'],
            'dog': ['title3', 'title4']
        }
        expected_search_results = ['title3', 'title4']
        self.assertEqual(search('dog', dummy_keyword_dict), expected_search_results)

    def test_keyword_to_titles(self):
        listy=[['legacy', 'Mr', 11, 55, ['cartoon']],['leg', 'Mr', 11, 55, ['car']]]
        listy1=[['legacy', 'Mr', 11, 55, ['cartoon']],['leg', 'Mr', 11, 55, ['cartoon']]]
        self.assertEqual(keyword_to_titles(listy), {'cartoon':['legacy'],'car':['leg']})
        self.assertEqual(keyword_to_titles([]), {})
        self.assertEqual(keyword_to_titles(listy1), {'cartoon':['legacy','leg']})

    def test_title_to_info(self):
        listy=[['legacy', 'Mr', 11, 55, ['cartoon']]]
        listy1=[['legacy', 'Mr', 11, 55, ['cartoon']],['leg', 'Mr', 11, 55, ['cartoon']]]
        self.assertEqual(title_to_info(listy), {'legacy': {'author': 'Mr', 'timestamp': 11, 'length': 55}})
        self.assertEqual(title_to_info([]), {})
        self.assertEqual(title_to_info(listy1), {'legacy': {'author': 'Mr', 'timestamp': 11, 'length': 55},'leg': {'author': 'Mr', 'timestamp': 11, 'length': 55}})

    def test_search(self):
        listy={'cartoon':['legacy'],'car':['leg']}
        listy1={'cartoon':['legacy','leg']}
        self.assertEqual(search('la',{}), [])
        self.assertEqual(search('car',listy),['leg'])
        self.assertEqual(search('cartoon',listy1),['legacy','leg'])

    def test_article_length(self):
        listy={'legacy': {'author': 'Mr', 'timestamp': 11, 'length': 55}}
        listy1={'legacy': {'author': 'Mr', 'timestamp': 11, 'length': 550},'leg': {'author': 'Mr', 'timestamp': 11, 'length': 55}}
        self.assertEqual(article_length(100,['legacy'],listy),['legacy'])
        self.assertEqual(article_length(100,['legacy','leg'],listy1),['leg'])
        self.assertEqual(article_length(100,[],listy1),[])

    def test_key_by_author(self):
        listy={'legacy': {'author': 'Mr', 'timestamp': 11, 'length': 55}}
        listy1={'legacy': {'author': 'Mr', 'timestamp': 11, 'length': 550},'leg': {'author': 'Mr', 'timestamp': 11, 'length': 55}}
        self.assertEqual(key_by_author(['legacy'],listy),{'Mr':['legacy']})
        self.assertEqual(key_by_author([],listy),{})
        self.assertEqual(key_by_author(['legacy'],listy1),{'Mr':['legacy']})
        
    def test_filter_to_author(self):
        listy={'legacy': {'author': 'Mr', 'timestamp': 11, 'length': 55}}
        listy1={'legacy': {'author': 'Mr', 'timestamp': 11, 'length': 550},'leg': {'author': 'Wadia', 'timestamp': 11, 'length': 55}}
        self.assertEqual(filter_to_author('Mr',['legacy'],listy),['legacy'])
        self.assertEqual(filter_to_author('Rank',['legacy','leg'],listy1),[])
        self.assertEqual(filter_to_author('',[],listy1),[])
    
    def test_filter_out(self):
        listy={'cartoon':['legacy'],'car':['leg']}
        listy1={'cartoon':['legacy','leg']}
        self.assertEqual(filter_out('cartoon',['legacy'],listy1),[])
        self.assertEqual(filter_out('car',['legacy','leg'],listy),['legacy'])
        self.assertEqual(filter_out('',[],listy1),[])

    def test_articles_from_year(self):
        listy={'legacy': {'author': 'Mr', 'timestamp': 1069994121, 'length': 55}}
        listy1={'legacy': {'author': 'Mr', 'timestamp': 1069994121, 'length': 550},'leg': {'author': 'Wadia', 'timestamp': 1069, 'length': 55}}
        self.assertEqual(articles_from_year(2003,['legacy'],listy),['legacy'])
        self.assertEqual(articles_from_year(2003,['legacy','leg'],listy1),['legacy'])
        self.assertEqual(articles_from_year(2005,['legacy','leg'],listy1),[])


    #####################
    # INTEGRATION TESTS #
    #####################

    @patch('builtins.input')
    def test_example_integration_test(self, input_mock):
        keyword = 'soccer'
        advanced_option = 5
        advanced_response = 2009

        output = get_print(input_mock, [keyword, advanced_option, advanced_response])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + str(advanced_response) + "\n\nHere are your articles: ['Spain national beach soccer team', 'Steven Cohen (soccer)']\n"

        self.assertEqual(output, expected)

    @patch('builtins.input')
    def test_integration_test_1(self, input_mock):
        keyword = '2003'
        advanced_option = 5
        advanced_response = 2009

        output = get_print(input_mock, [keyword, advanced_option, advanced_response])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + str(advanced_response) + "\n\nHere are your articles: ['2009 in music']\n"

        self.assertEqual(output, expected)

    @patch('builtins.input')
    def test_integration_test_2(self, input_mock):
        keyword = '2003'
        advanced_option = 1
        advanced_response = '9999999'

        output = get_print(input_mock, [keyword, advanced_option, advanced_response])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + str(advanced_response) + "\n\nHere are your articles: ['2009 in music', 'List of dystopian music, TV programs, and games']\n"

        self.assertEqual(output, expected)

    @patch('builtins.input')
    def test_integration_test_3(self, input_mock):
        keyword = '2003'
        advanced_option = 2
        

        output = get_print(input_mock, [keyword, advanced_option])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + "\n\nHere are your articles: {'RussBot': ['2009 in music'], 'Bearcat': ['List of dystopian music, TV programs, and games']}\n"

        self.assertEqual(output, expected)

    @patch('builtins.input')
    def test_integration_test_4(self, input_mock):
        keyword = '2003'
        advanced_option = 3
        advanced_response = 'tiger'

        output = get_print(input_mock, [keyword, advanced_option, advanced_response])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + str(advanced_response) + "\n\nNo articles found\n"

        self.assertEqual(output, expected)

    @patch('builtins.input')
    def test_integration_test_5(self, input_mock):
        keyword = '2003'
        advanced_option = 4
        advanced_response = '2009'

        output = get_print(input_mock, [keyword, advanced_option, advanced_response])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + str(advanced_response) + "\n\nHere are your articles: ['List of dystopian music, TV programs, and games']\n"

        self.assertEqual(output, expected)

    @patch('builtins.input')
    def test_integration_test_3(self, input_mock):
        keyword = '2003'
        advanced_option = 6
        

        output = get_print(input_mock, [keyword, advanced_option])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + "\n\nHere are your articles: ['2009 in music', 'List of dystopian music, TV programs, and games']\n"

        self.assertEqual(output, expected)

    

# Write tests above this line. Do not remove.
if __name__ == "__main__":
    main()
