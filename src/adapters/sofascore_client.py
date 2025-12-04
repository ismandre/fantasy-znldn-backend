import json
from typing import Any, override

from botasaurus.browser import Driver, browser  # type: ignore[import-not-found]

from domain.ports.http_client import HttpClient


class SofascoreClient(HttpClient):

    @override
    async def get(self, url: str) -> Any:
        return botasaurus_browser_get_json(url)


# from: https://github.com/oseymour/ScraperFC/blob/4af00054f5dd83c9e000c1d6c6de61bb6254d8ac/src/ScraperFC/utils
@browser(headless=True, output=None, create_error_logs=False, block_images_and_css=True)  # type: ignore[misc]
def botasaurus_browser_get_json(driver: Driver, url: str) -> Any:
    """Use Botasaurus BROWSER model to get JSON from page

    Parameters
    ----------
    driver : botasaurus.browser.Driver
        Browser object. Provided by Botasaurus decorator
    url : str
        The URL to scrape

    Returns
    -------
    dict
    """
    driver.get(url)
    page_source = driver.page_text
    result = json.loads(page_source)
    return result
