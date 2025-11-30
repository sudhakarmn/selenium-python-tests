from utils.driver_factory import DriverFactory


def before_scenario(context, scenario):
    context.driver = DriverFactory.create_driver()


def after_scenario(context, scenario):
    if hasattr(context, "driver"):
        context.driver.quit()
