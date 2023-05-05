import unittest
from unittest.mock import MagicMock
from movie import MovieApp


class TestMovieApp(unittest.TestCase):

    def setUp(self):
        self.movieApp = MovieApp(MagicMock())

    def test_searchMovie_with_results(self):
        expected = {
            'id': 121,
            'original_title': 'The Lord of the Rings: The Two Towers',
            'overview': 'Frodo and Sam are trekking to Mordor to destroy the One Ring of '
             'Power while Gimli, Legolas and Aragorn search for the '
             'orc-captured Merry and Pippin. All along, nefarious wizard '
             'Saruman awaits the Fellowship members at the Orthanc Tower in '
             'Isengard.',
            'release_date': '2002-12-18',
            'vote_average': 8.378}
        #Check with spaces
        actual = self.movieApp.movieDB.searchMovie("lord of the rings")
        self.assertEqual(expected, actual)
        expected = {'id': 268,
        'original_title': 'Batman',
        'overview': 'Batman must face his most ruthless nemesis when a deformed '
             'madman calling himself "The Joker" seizes control of Gotham\'s '
             'criminal underworld.',
        'release_date': '1989-06-23',
        'vote_average': 7.215}
        actual = self.movieApp.movieDB.searchMovie("Batman")
        self.assertEqual(expected, actual)
        #Check with numbers and spaces
        expected = {'id': 389,
            'original_title': '12 Angry Men',
            'overview': 'The defense and the prosecution have rested and the jury is '
             'filing into the jury room to decide if a young Spanish-American '
             'is guilty or innocent of murdering his father. What begins as an '
             'open and shut case soon becomes a mini-drama of each of the '
             "jurors' prejudices and preconceptions about the trial, the "
             'accused, and each other.',
            'release_date': '1957-04-10',
            'vote_average': 8.537}
        actual = self.movieApp.movieDB.searchMovie("12 Angry Men")
        self.assertEqual(expected, actual)
    def test_searchMovie_no_results(self):
        expected = "No Results"
        actual = self.movieApp.movieDB.searchMovie("asdlkjasdlkjasd")
        self.assertEqual(expected, actual)
        #Testing non valid names with spaces
        actual = self.movieApp.movieDB.searchMovie("HELLOWD AWFJUIB WUUIWBIUPAGU")
        self.assertEqual(expected, actual)
        #Testing with numbers i guess??
        actual = self.movieApp.movieDB.searchMovie("7126tf iygwafygu72i0wp902")
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
