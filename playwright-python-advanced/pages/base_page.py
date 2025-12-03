class BasePage:
    def __init__(self, page):
        self.page = page


    def goto(self, url):
        self.page.goto(url)


    def click(self, locator):
        self.page.click(locator)


    def fill(self, locator, text):
        self.page.fill(locator, text)


    def text_content(self, locator):
        return self.page.text_content(locator)


    def is_visible(self, locator):
        return self.page.locator(locator).is_visible()