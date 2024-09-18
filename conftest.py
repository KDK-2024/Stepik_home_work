import pytest
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption('--languages', action='store', default=None,
                     help="Choose user_language: 'ru' or 'en-gb'")

@pytest.fixture(scope="function")
def browser(request):
    user_language = request.config.getoption("languages")

    browser = webdriver.Chrome()

    # Открытие базового URL
    base_url = "http://selenium1py.pythonanywhere.com/"

    # Если язык указан, добавляем его в URL
    if user_language in ["ru", "en-gb"]:
        full_url = f"{base_url}{user_language}/catalogue/coders-at-work_207/"
    else:
        raise pytest.UsageError("--languages should be 'ru' or 'en-gb'")

    browser.get(full_url)

    yield browser
    print("\nClosing browser..")
    browser.quit()