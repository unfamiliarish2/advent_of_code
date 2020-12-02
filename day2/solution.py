from functools import reduce
import re
from typing import Callable, List

class PasswordInfo:
    def __init__(self, pass_info: str) -> None:
    	# splits on '-', ' ', and ': '
    	low, high, char, password = re.split('-| |: ', pass_info.strip())
    	self.low = int(low)
    	self.high = int(high)
    	self.required_char = char
    	self.password = password

    def has_valid_count(self) -> bool:
    	char_count = self.password.count(self.required_char)
    	valid_low = self.low <= char_count
    	valid_high = char_count <= self.high
    
    	return valid_low and valid_high

    def has_valid_position(self) -> bool:
    	required_char = self.required_char
    	in_low = self.password[self.low] == required_char
    	in_high = self.password[self.high] == required_char

    	return in_low or in_high

    def __repr__(self) -> str:
    	return f'PasswordInfo(password={self.password}, ' \
    		f'char={self.required_char}, ' \
    		f'low={self.low}, high={self.high})'


def get_input(filename: str) -> List[PasswordInfo]:
    """Returns contents of filename as list of ints"""
    with open(filename,'r') as fh:
        lines = fh.readlines()

    return [PasswordInfo(x) for x in lines]


def password_validator(filename: str) -> int:
	pass_infos = get_input(filename)

	count = 0
	for pinfo in pass_infos:
		if pinfo.has_valid_count():
			count += 1

	return count


valid_passwords = password_validator("./input.txt")
print(valid_passwords)

