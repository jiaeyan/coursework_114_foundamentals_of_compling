import unittest
from recognizer import is_phone_number, is_email_address
from soundex import letters_to_numbers, truncate_to_three_digits, add_zero_padding, soundex_convert
from morphology import Parser
'''
Jiajie Sven Yan
'''
class TestHW1(unittest.TestCase):

	def setUp(self):
		self.f1 = letters_to_numbers()
		self.f2 = truncate_to_three_digits()
		self.f3 = add_zero_padding()
		self.mparser = Parser()

	def test_is_phone_number(self):
		self.assertTrue(is_phone_number('153-523-1295'))
		self.assertFalse(is_phone_number('15E-523-1295'))
		self.assertTrue(is_phone_number('(346)-656-6574'))
		self.assertTrue(is_phone_number('(684) 214 6879'))
		self.assertTrue(is_phone_number('223 8745453'))

	def test_is_email_address(self):
		self.assertTrue(is_email_address('tet@brandeis.edu'))
		self.assertFalse(is_email_address('tet@brandeis'))
		self.assertFalse(is_email_address('brandeis.edu'))
		self.assertTrue(is_email_address('svenyan@blcu.edu.cn'))
		self.assertTrue(is_email_address('svenyan@blcu.edu.cn.xx.xx.xx'))
		self.assertFalse(is_email_address('tet@1991.edu'))
		self.assertFalse(is_email_address('tet@happy.-'))
		self.assertFalse(is_email_address('tet@91-.edu'))

	def test_letters(self):
		self.assertEqual("".join(self.f1.transduce("washington")[0]), "w25235")
		self.assertEqual("".join(self.f1.transduce("jefferson")[0]), "j1625")
		self.assertEqual("".join(self.f1.transduce("adams")[0]), "a352")
		self.assertEqual("".join(self.f1.transduce("bush")[0]), "b2")

	def test_truncation(self):
		self.assertEqual("".join(self.f2.transduce("a33333")[0]), "a333")
		self.assertEqual("".join(self.f2.transduce("123456")[0]), "123")
		self.assertEqual("".join(self.f2.transduce("11")[0]), "11")
		self.assertEqual("".join(self.f2.transduce("5")[0]), "5")

	def test_padding(self):
		self.assertEqual("".join(self.f3.transduce("3")[0]), "300")
		self.assertEqual("".join(self.f3.transduce("b56")[0]), "b560")
		self.assertEqual("".join(self.f3.transduce("c111")[0]), "c111")

	def test_soundex(self):
		self.assertEqual(soundex_convert("jurafsky"), "j612")
		self.assertEqual(soundex_convert("Alice"), "A420")
		self.assertEqual(soundex_convert("josh"), "j200")
		self.assertEqual(soundex_convert("svenyan"), "s155")

	def test_morphology(self):
		havocking = [x for x in 'havocking']
		self.assertEqual(self.mparser.parse(havocking), "havoc+present participle")
		lick = ['l','i','c','k','+past form']
		self.assertEqual(self.mparser.generate(lick), "licked")
		panic = ['p','a','n','i','c','+present participle']
		self.assertEqual(self.mparser.generate(panic), "panicking")

if __name__ == '__main__':
	unittest.main()
