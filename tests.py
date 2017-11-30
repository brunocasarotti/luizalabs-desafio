import unittest
import search

class TestSearch(unittest.TestCase):
    def test_words_movies_for_not_empty_after_process(self):
        '''words_movies must not be empty after processed'''
        search.process()
        self.assertTrue(len(search.words_movies.items()) > 0)

    def test_movie_ids_same_length(self):
        '''movie_ids variable should have the same lenght
        as the number of files inside the data directory'''
        search.process()
        self.assertEqual(len(search.movie_ids), len(search.os.listdir(search.location)))

    def test_type_of_terms(self):
        '''Assert that the main method in search module
        get the correct input type of data'''
        with self.assertRaises(TypeError):
            search.main([])
        with self.assertRaises(TypeError):
            search.main(1)
        with self.assertRaises(TypeError):
            search.main(dict())


if __name__ == '__main__':
    unittest.main()

