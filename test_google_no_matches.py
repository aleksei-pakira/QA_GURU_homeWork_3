from selene import browser, be, have


def test_first():
    browser.open("https://www.google.com/")
    browser.element('[name="q"]').should(be.blank).type('photomagnitoelecticheskyeffect').press_enter()
    browser.element('[id="botstuff"]').should(have.text('По запросу photomagnitoelecticheskyeffect ничего не найдено'))