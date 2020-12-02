import re
from typing import List, Tuple


class PasswordInfo:
    def __init__(self, pass_info: str) -> None:
        # splits on '-', ' ', and ': '
        low, high, char, password = re.split("-| |: ", pass_info.strip())
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
        rchar = self.required_char
        in_low = self.password[self.low - 1] == rchar
        in_high = self.password[self.high - 1] == rchar

        return in_low != in_high

    def __repr__(self) -> str:
        return (
            f"PasswordInfo(password={self.password}, "
            f"char={self.required_char}, "
            f"low={self.low}, high={self.high})"
        )


def get_input(filename: str) -> List[PasswordInfo]:
    """Returns contents of filename as list of ints"""
    with open(filename, "r") as fh:
        lines = fh.readlines()

    return [PasswordInfo(x) for x in lines]


def password_validator(filename: str) -> Tuple[int, ...]:
    """Returns count of valid passwords, according to diff requirements"""
    pass_infos = get_input(filename)

    num_valid_count = 0
    num_valid_position = 0
    for pinfo in pass_infos:
        if pinfo.has_valid_count():
            num_valid_count += 1
        if pinfo.has_valid_position():
            num_valid_position += 1

    return num_valid_count, num_valid_position


count, position = password_validator("./input.txt")
print(f"Passwords with valid count: {count}")
print(f"Passwords with valid position: {position}")
