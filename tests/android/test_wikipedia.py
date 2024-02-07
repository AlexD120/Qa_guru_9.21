from allure_commons._allure import step
from appium.webdriver.common.appiumby import AppiumBy
from selene import have
from selene.support.shared.jquery_style import s, ss


def test_search_appium():
    with step('Type search'):
        s((AppiumBy.ACCESSIBILITY_ID, "Search Wikipedia")).click()
        s((AppiumBy.ID, "org.wikipedia.alpha:id/search_src_text")).type('Appium')
    with step('Verify content found'):
        results = ss((AppiumBy.ID, "org.wikipedia.alpha:id/page_list_item_title"))
        results.should(have.size_greater_than(0))
        results.first.should(have.text('Appium'))


def test_search_appleinc():
    with step('Type search'):
        s((AppiumBy.ACCESSIBILITY_ID, "Search Wikipedia")).click()
        s((AppiumBy.ID, "org.wikipedia.alpha:id/search_src_text")).type('Microsoft')
    with step('Verify content found'):
        results = ss((AppiumBy.ID, "org.wikipedia.alpha:id/page_list_item_title"))
        results.should(have.size_greater_than(0))
        results.first.should(have.text('Microsoft')).click()
        s((AppiumBy.ID, "org.wikipedia.alpha:id/page_web_view")).should(
            have.text('Microsoft')
        )
