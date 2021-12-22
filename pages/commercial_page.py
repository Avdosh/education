from .page import BasePage
from selenium.webdriver.common.by import By

class LocatorsCommercial:
    LOCATOR_SEARCH_BUTTON = (By.XPATH, "//a[contains(@data-mark,'FiltersSearchButton')]")
    LOCATOR_SEARCH_MAP_BUTTON = (By.XPATH, "//a[contains(@data-mark,'FiltersSearchOnMapButton')]")
    LOCATOR_BUY_BUTTON = (By.XPATH, "//a[starts-with(@href, '/kupit/')]")
    LOCATOR_RENT_BUTTON = (By.XPATH, "//a[starts-with(@href, '/snyat/')]")
    LOCATOR_INPUT_FIELD = (By.ID, "geo-suggest-input")

class SearchCommercial(BasePage):

    def click(self, locator):
        return self.find_element(locator, time=2).click()

    def click_search_button(self):
        return self.click(LocatorsCommercial.LOCATOR_SEARCH_BUTTON)

    def click_search_map_button(self):
        return self.click(LocatorsCommercial.LOCATOR_SEARCH_MAP_BUTTON)

    def click_buy_button(self):
         return self.click(LocatorsCommercial.LOCATOR_BUY_BUTTON)

    def click_rent_button(self):
         return self.click(LocatorsCommercial.LOCATOR_RENT_BUTTON)

    def input_word(self, word):
        input_field = self.find_element(LocatorsCommercial.LOCATOR_INPUT_FIELD)
        input_field.click()
        input_field.send_keys(word)
        return input_field




