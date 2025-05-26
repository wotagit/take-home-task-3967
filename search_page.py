# (c) Copyright 2025 Take-Home-Assessment search_page.py module
"""
This file contains SearchPage class definition
"""
from results_page import ResultsPage
from locators import SearchPageLocators


class SearchPage:
    """
    Train Journey Search Page
    """
    def __init__(self, page):
        """
        Initialize SearchPage object
        :param page: page
        """
        print("Initializing SearchPage object...")
        self.page = page
        self.depart_station_input = page.locator(SearchPageLocators.DEPART_STATION)
        self.arrive_station_input = page.locator(SearchPageLocators.ARRIVE_STATION)
        self.depart_date_input = page.locator(SearchPageLocators.DEPART_DATE)
        self.return_date_input = page.locator(SearchPageLocators.RETURN_DATE)
        self.close_btn = page.locator(SearchPageLocators.CLOSE_BTN)
        self.submit_btn = page.locator(SearchPageLocators.SUBMIT_BTN)
        self.url = "https://www.cp.pt/passageiros/en/buy-tickets"

    def navigate(self) -> None:
        """
        Navigate to the search page
        :param self: self reference
        :return (obj): None
        """
        print("Navigating to the search page...")
        self.page.goto(self.url)

    def search_for_trips(
            self, 
            depart_station: str, 
            arrive_station: str, 
            depart_date: str, 
            return_date: str) -> "ResultsPage":
        """
        Enter search parameters and perform search
        :param depart_station (str): departure station
        :param arrive_station (str): destination station
        :param depart_date (str): departure date
        :param return_date (str): return date
        :return (obj): ResultsPage object
        """
        print("Entering search parameters...")
        self.depart_station_input.fill(depart_station)
        self.arrive_station_input.fill(arrive_station)
        self.depart_date_input.clear()
        self.depart_date_input.fill(depart_date)
        self.return_date_input.clear()
        self.return_date_input.fill(return_date)
        self.close_btn.click()  # close date picker
        self.submit_btn.click() # submit search
        return ResultsPage(self.page)
