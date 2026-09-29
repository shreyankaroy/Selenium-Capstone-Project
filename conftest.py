import pytest
from selenium import webdriver

from utilities.config_reader import ConfigReader
from utilities.screenshot import Screenshot


@pytest.fixture
def driver(request):

    config = ConfigReader()

    browser = config.get_browser()

    if browser.lower() == "chrome":
        driver = webdriver.Chrome()

    else:
        raise ValueError(
            f"Unsupported browser: {browser}"
        )

    driver.maximize_window()

    yield driver

    # Take screenshot if test failed
    if request.node.rep_call.failed:

        Screenshot.capture(
            driver,
            request.node.name
        )

    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield

    report = outcome.get_result()

    setattr(
        item,
        "rep_" + report.when,
        report
    )