import pytest
from termcolor import colored


@pytest.fixture()
def set_up():
    print(colored("Start test", 'green'))
    yield
    print(colored("Finish test", 'green'))

@pytest.fixture()
def set_group(scope="module"):
    print(colored("Enter system", 'green'))
    yield
    print(colored("Exit system", 'green'))