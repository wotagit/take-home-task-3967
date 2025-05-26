# (c) Copyright 2025 Take-Home-Assessment app.py module
"""
This file contains test code for train journey booking system
"""
from playwright.sync_api import sync_playwright
from playwright.sync_api import expect
from datetime import date, timedelta
from search_page import SearchPage
from locators import SearchPageLocators

# Launch the browser and navigate to search page
playwright = sync_playwright().start()
browser = playwright.chromium.launch(headless=False, slow_mo=100)
page = browser.new_page()
search_page = SearchPage(page)
search_page.navigate()
try:
    # Enter search criteria
    depart_station = "Lagos"
    arrive_station = "Porto Campanha"
    today = date.today()
    depart_date = today + timedelta(days=3)
    depart_date = depart_date.strftime("%d %B, %Y") # format the date e.g. 28 May, 2025
    return_date = today + timedelta(days=5)
    return_date = return_date.strftime("%d %B, %Y")
    results_page = search_page.search_for_trips(depart_station, arrive_station, depart_date, return_date)
    page.wait_for_url(results_page.url) # wait for results page to appear

    # Navigate back to search page
    results_page.click_on_cancel_button()
    page.wait_for_url(search_page.url)

    # Validate search parameters are saved
    print("Validating search parameters have been saved...")
    expect(page.locator(SearchPageLocators.DEPART_STATION)).to_have_value(depart_station)
    expect(page.locator(SearchPageLocators.ARRIVE_STATION)).to_have_value(arrive_station)
    expect(page.locator(SearchPageLocators.DEPART_DATE)).to_have_value(depart_date)
    expect(page.locator(SearchPageLocators.RETURN_DATE)).to_have_value(return_date)
    print("Validation passed")

except Exception as e:
    print(f"Test failed with exception {e}")

finally: # Tidy-up
    browser.close()
    playwright.stop()
