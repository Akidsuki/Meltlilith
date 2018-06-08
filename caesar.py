from enum import IntEnum, auto
"""

シーザー暗号変換用
encodeに指定の引数を渡すことで使用する、記号は無視しそのまま返す
:param message: string  変換する文字列
:param shift: integer  文字コードをシフトする数 前方にシフト < 0 < 後方にシフト

example:
	shift = 2
		A => C
		x => a
	shift = -5
		a => f
		W => B
"""


class Case(IntEnum):
	"""大文字小文字構造体

		UPPER: 大文字
		LOWER: 小文字
		ERROR: アルファベット以外
	"""
	UPPER = auto()
	LOWER = auto()
	ERROR = auto()
	

def distinction_case(char):
	"""
	大文字小文字の判定
	:param char: string
	:return: Case
	"""
	if "a" <= char <= "z":
		return Case.LOWER
	elif "A" <= char <= "Z":
		return Case.UPPER
	else:
		return Case.ERROR
	

def left_shift(char, shift):
	"""
	:param char: string
	:param shift: integer
	:return: string
	"""
	if distinction_case(char) == Case.UPPER:
		if ord("Z") < ord(char) + shift:
			return chr((ord("A") - 1) + (shift - (ord("Z") - ord(char))))
		else:
			return chr(ord(char) + shift)
	elif distinction_case(char) == Case.LOWER:
		if ord("z") < ord(char) + shift:
			return chr((ord("a") - 1) + (shift - (ord("z") - ord(char))))
		else:
			return chr(ord(char) + shift)
	else:
		return char
	

def right_shift(char, shift):
	"""
	:param char: string
	:param shift: integer
	:return: string
	"""
	if distinction_case(char) == Case.UPPER:
		if ord(char) + shift < ord("A"):
			return chr((ord("Z") + 1) + shift + ord(char))
		else:
			return chr(ord(char) + shift)
	elif distinction_case(char) == Case.LOWER:
		if ord(char) + shift < ord("a"):
			return chr((ord("z") + 1) + shift + ord(char))
		else:
			return chr(ord(char) + shift)
	else:
		return char
	

def encode(message, shift):
	"""
	
	:param message: string
	:param shift: integer
	:return: string
	"""
	
	result = ''
	shift = int(shift % 26)
	
	if shift < 0:
		for char in message:
			result += right_shift(char, shift)
	elif shift > 0:
		for char in message:
			result += left_shift(char, shift)
	else:
		return "error shift 0"
	
	return result
