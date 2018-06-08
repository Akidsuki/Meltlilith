from unittest import TestCase
import caesar


class TestDistinctionCase(TestCase):
	# distinction_case に小文字を渡すと小文字判定が帰ってくる
	def test_distinction_case_lower_lower(self):
		expected = caesar.Case.LOWER
		actual = caesar.distinction_case("a")
		self.assertEquals(expected, actual)
	
	# distinction_case に大文字を渡すと大文字判定が帰ってくる
	def test_distinction_case_upper_upper(self):
		expected = caesar.Case.UPPER
		actual = caesar.distinction_case("A")
		self.assertEquals(expected, actual)
		
	# distinction_case に記号を渡すとエラー判定が帰ってくる
	def test_distinction_case_symbol_error(self):
		expected = caesar.Case.ERROR
		actual = caesar.distinction_case("_")
		self.assertEquals(expected, actual)
		
	# distinction_case に数字を渡すとエラー判定が帰ってくる
	def test_distinction_case_number_error(self):
		expected = caesar.Case.ERROR
		actual = caesar.distinction_case("9")
		self.assertEquals(expected, actual)
		
	# encode に文字列"AbCdE_fGhXz"と 2 を渡すと"CdEfG_hIjAb"が帰ってくる
	def test_encode_right_shift(self):
		expected = "CdEfG_hIjAb"
		actual = caesar.encode("AbCdE_fGhXz", 2)
		self.assertEquals(expected, actual)
		
	# encode に文字列"AbCdE_fGhIj"と -2 を渡すと"XzAbC_dEfGh"が帰ってくる
	def test_encode_right_shift(self):
		expected = "yZa_VwX"
		actual = caesar.encode("aBc_XyZ", -2)
		self.assertEquals(expected, actual)
