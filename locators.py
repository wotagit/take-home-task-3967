# (c) Copyright 2025 Take-Home-Assessment locators.py module
"""
This file contains locators for each page object
"""
class SearchPageLocators:
    DEPART_STATION = "input[placeholder='From ']"
    ARRIVE_STATION = "input[placeholder='To ']"
    DEPART_DATE = "input[id='datepicker-first']"
    RETURN_DATE = "input[id='datepicker-second']"
    CLOSE_BTN = "div[class='input-group date'] button:nth-child(3)"
    SUBMIT_BTN = "input[value='Submit »']"


class ResultsPageLocators:
    CANCEL_BTN = "input[id='exitButton']"