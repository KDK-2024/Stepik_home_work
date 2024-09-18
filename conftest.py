import pytest
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption('--languages', action='store', default=None,
                     help="Choose user_languages: 'ru' or 'en'")

@pytest.fixture(scope="function")
def browser(request):
    languages = request.config.getoption("languages")

    if languages == "ru":
        print("\nstart browser for test in russian languages")
        browser = webdriver.Chrome()
    elif languages == "en":
        print("\nstart browser for test in english languages")
        browser = webdriver.Chrome()
    else:
        raise pytest.UsageError("--languages should be 'ru' or 'en'")
    yield browser
    print("\nquit browser..")
    browser.quit()