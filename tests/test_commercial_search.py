from pages.commercial_page import SearchCommercial


class TestEducation:

    def test_not_empty_rent_search_on_map(self, chrome_browser):
        search_element = SearchCommercial(chrome_browser)
        search_element.go_to_site()
        search_element.click_rent_button()
        search_element.input_word("Невский проспект")
        search_element.click_search_map_button()
        assert "EmptySearchContent" not in chrome_browser.page_source

    def test_not_empty_buy_search_on_map(self, chrome_browser):
        search_element = SearchCommercial(chrome_browser)
        search_element.go_to_site()
        search_element.click_buy_button()
        search_element.input_word("Невский проспект")
        search_element.click_search_map_button()
        assert "EmptySearchContent" not in chrome_browser.page_source

    def test_not_empty_rent_search(self, chrome_browser):
        search_element = SearchCommercial(chrome_browser)
        search_element.go_to_site()
        search_element.click_rent_button()
        search_element.input_word("Невский проспект")
        search_element.click_search_button()
        assert "EmptySearchContent" not in chrome_browser.page_source

    def test_not_empty_buy_search(self, chrome_browser):
        search_element = SearchCommercial(chrome_browser)
        search_element.go_to_site()
        search_element.click_buy_button()
        search_element.input_word("Невский проспект")
        search_element.click_search_button()
        assert "EmptySearchContent" not in chrome_browser.page_source
