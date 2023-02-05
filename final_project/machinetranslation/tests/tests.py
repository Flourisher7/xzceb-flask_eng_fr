import unittest
from machinetranslation import translator
class TestenglishToFrench(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(translator.english_to_french("Hello"), "Bonjour")
        self.assertNotEqual(translator.english_to_french(" "), "Bonjour")
        
class TestfrenchToEnglish(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(translator.french_to_english("Bonjour"), "Hello")
        self.assertNotEqual(translator.french_to_english(" "), "Hello")

if __name__=='__main()__':
    unittest.main()