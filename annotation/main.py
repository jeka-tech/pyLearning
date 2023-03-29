from typing import Union


def mux (a: Union[int, float], b: int) -> int:
    return a*b

if __name__ == '__main__':
    print(mux(2.4, 6))