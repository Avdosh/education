from selenium.webdriver.common.keys import Keys


class TestEducation:

    def test_not_empty_search(self, fix):
        fix.get("https://spb.cian.ru/commercial/")
        assert "Коммерческая" in fix.title
        elem = fix.find_element_by_xpath('//input[@id="geo-suggest-input"]')
        elem.clear()
        elem.send_keys("Невский проспект")
        elem.send_keys(Keys.RETURN)
        assert "EmptySearchContent" not in fix.page_source