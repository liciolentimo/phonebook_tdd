
import unittest

from phonebook import Phonebook


class PhonebookTest(unittest.TestCase):

    def setUp(self):
        self.phonebook = Phonebook('dir')

    def tearDown(self):
        self.phonebook.clear() 
	    

    def test_lookup_entry_by_name(self):
        self.phonebook.add('Mike', '0707')
        self.assertEqual('0707', self.phonebook.lookup('Mike'))
     

    def test_missing_entry_raises_error(self):
        self.assertRaises(KeyError, self.phonebook.lookup, 'missing')

    def test_empty_phonebook_is_consistent(self):
        self.assertTrue(self.phonebook.is_consistent())

    @unittest.skip('Example')
    def test_is_consistent(self):
        self.assertTrue(self.phonebook.is_consistent())
        self.phonebook.add('Mike', '0707')
        self.assertTrue(self.phonebook.is_consistent())
        self.phonebook.add('Jane', '0705')
        self.assertTrue(self.phonebook.is_consistent())
        self.phonebook.add('John', '0743')  
        self.assertFalse(self.phonebook.is_consistent())
        self.phonebook.add('Jake', '0721')  
        self.assertFalse(self.phonebook.is_consistent())

    def test_phonebook_with_normal_entries_is_consistent(self):
        self.phonebook.add('test_missing_entry_raises_error', '0707')
        self.phonebook.add('Jane', '0705')
        self.assertTrue(self.phonebook.is_consistent())

    def test_phonebook_with_duplicate_entries_is_inconsistent(self):
        self.phonebook.add('Mike', '0707')
        self.phonebook.add('Jane', '0707')
        self.assertFalse(self.phonebook.is_consistent())

    def test_phonebook_with_that_prefix_one_another_is_inconsistent(self):
        self.phonebook.add('Mike', '0707')
        self.phonebook.add('Jane', '07')
        self.assertFalse(self.phonebook.is_consistent())

    def test_phonebook_adds_names_and_numbers(self):
        self.phonebook.add('John', '0707')
        self.assertIn('John', self.phonebook.get_names())
        self.assertIn('0707', self.phonebook.lookup('John'))

if __name__ == '__main__':
	unittest.main()