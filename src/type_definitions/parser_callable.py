from argparse import ArgumentParser
from collections.abc import Callable


type ParserCallable = Callable[[], ArgumentParser]
