import logging
logging.basicConfig(
    level=logging.DEBUG
)

from seleniumwire_gpl import UndetectedChrome
import undetected_chromedriver as uc
import pytest

@pytest.fixture
def chrome_options():
    options = uc.ChromeOptions()
    options.add_argument("--headless=new")
    options.accept_insecure_certs = True
    return options

@pytest.fixture(scope="function")
def uchrome(chrome_options):
    driver = UndetectedChrome(
        options=chrome_options
    )
    # Forced timeout is set to avoid the driver getting stuck
    driver.set_page_load_timeout(5)

    yield driver
    driver.quit()
