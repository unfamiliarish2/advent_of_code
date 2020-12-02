from dataclasses import dataclass
import re

@dataclass
class PasswordInfo:
    password: str
    required_char: str
    min_count: int
    max_count: int

    def __init__(self, pass_info: str) -> None:
    	# splits on '-', ' ', and ': '
    	min_, max_, char, pass_ = re.split('-| |: ', line.strip())
    	self.min_count = min_
    	self.max_count = max_
    	self.required_char = char
    	self.password = pass_


    def is_valid(self) -> bool:
    	char_count = self.password.count(self.required_char)
    	return min_count <= char_count and char_count <= max_count


def get_input(filename: str) -> List[PasswordInfo]:
    """Returns contents of filename as list of ints"""
    with open(filename,'r') as fh:
        lines = fh.readlines()



    return [int(x.strip()) for x in lines]
