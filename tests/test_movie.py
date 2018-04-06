import unittest
from app.models import Movie


class MovieTest(unittest.TestCase):
    '''
    Test class to test behaviour of the Movie class
    '''
    def setUp(self):
        '''
        set up method that will run before every test
        '''
        self.new_movie = Movie(1234,'Python Must Be Crazy','A thrilling new Python series','https://developers,themoviedb.org/3/getting-started/images/khsjha27hbs',8.5,129993)
    
    def test_instance(self):
        self.assertTrue(isinstance(self.new_movie,Movie))

        
