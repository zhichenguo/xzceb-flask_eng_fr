import unittest

from translator import english_to_french, french_to_english

class TestEnglishToFrench(unittest.TestCase): 
    def test1(self):
        
        # Test for null input
        self.assertNotEqual(english_to_french(None), "Bonjour")
        # Test for the translation of the world 'Hello' and 'Bonjour' 
        self.assertEqual(english_to_french("Hello"), "Bonjour")


class TestFrenchToEnglish(unittest.TestCase): 
    def test1(self): 
        
        # Test for null input
        self.assertNotEqual(french_to_english(None), "Hello")
        # Test for the translation of the world 'Bonjour' and 'Hello' 
        self.assertEqual(french_to_english("Bonjour"), "Hello")

unittest.main()
