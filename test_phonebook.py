
import unittest

from phonebook import Phonebook


class PhonebookTest(unittest.TestCase):

    def setUp(self):
        self.phonebook = Phonebook('dir')

    def tearDown(self):
        self.phonebook.clear() 
	    
	#test looks up entry by name
    def test_lookup_entry_by_name(self):
        self.phonebook.add('Mike', '0707')
        self.assertEqual('0707', self.phonebook.lookup('Mike'))
     
	 #test checks for a missing entry and raises an error
    def test_missing_entry_raises_error(self):
        self.assertRaises(KeyError, self.phonebook.lookup, 'missing')
	#test checks if phonebook is consistent and has name and phone
    def test_empty_phonebook_is_consistent(self):
        self.assertTrue(self.phonebook.is_consistent())

   
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
