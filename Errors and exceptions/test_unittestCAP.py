import unittest
import unittestCAP

class TestCap(unittest.TestCase):

	def test_one_word(self):
		text = 'python'
		result = unittestCAP.cap_text(text)
		self.assertEqual(result,'Python')

	def test_two_multiple_words(self):
		text = 'monty python'
		result = unittestCAP.cap_text(text)
		self.assertEqual(result,'Monty Python')


if __name__ =='__main__':
	unittest.main()