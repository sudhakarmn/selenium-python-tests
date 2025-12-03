from pages.base_page import BasePage


class HomePage(BasePage):
    success_message = "text=Congratulations" # adapt based on actual page


    def is_logged_in(self):
        return self.is_visible(self.success_message)