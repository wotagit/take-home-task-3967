# (c) Copyright 2025 Take-Home-Assessment results_page.py module
"""
This file contains ResultsPage class definition
"""
from locators import ResultsPageLocators


class ResultsPage:
    """
    Train Journey Search Results Page
    """
    def __init__(self, page):
        """
        Initialize ResultsPage object
        :param page: page
        """
        self.page = page
        self.cancel_btn = page.locator(ResultsPageLocators.CANCEL_BTN)
        self.url = "https://venda.cp.pt/bilheteira/comprar/escolher-viagem?cid=*"

    def click_on_cancel_button(self) -> None:
        """
        Click on the cancel button.
        :param self: self reference
        :return (obj): None
        """
        print("Clicking on the cancel button...")
        self.cancel_btn.click()
