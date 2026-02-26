from core.driver_manager import ChromeDriverManager, FirefoxDriverManager, EdgeDriverManager
from config.selected_options import SELECTED_OPTIONS #selectedoptions by me
from config.browser_options import OPTION_MAP  # mapping logical names 

class DriverFactory:
    """
    Creates driver for the browser marked run=True in JSON
    """

    def __init__(self):
        self.driver = None
        self.driver_name = None

    def create_driver(self):
        """
        Picks the first browser in JSON with run=True and starts it.
        """
        browser_to_run = None
        options_conf = None

        # Find first browser with run=True
        for browser_name, conf in SELECTED_OPTIONS.items():
            if conf.get("run", False):
                browser_to_run = browser_name
                arg_key = f"{browser_name}_arguments"
                options_conf = conf.get(arg_key, {})
                break

        if not browser_to_run:
            print("No browser run flag is True in JSON → nothing to start")
            return None

        # Map browser name to manager class
        manager_map = {
            "chrome": ChromeDriverManager,
            "firefox": FirefoxDriverManager,
            "edge": EdgeDriverManager
        }

        manager_class = manager_map.get(browser_to_run.lower())
        if not manager_class:
            print(f"No manager class found for {browser_to_run}")
            return None

        manager = manager_class()
        print("created the browser instance :", manager.__class__)
        self.driver = manager.start_browser(options_conf)
        self.driver_name = browser_to_run
        print(f"{browser_to_run.capitalize()} driver created successfully")
        print("driver in driverfactory :",self.driver)
        return self.driver

    def quit_driver(self):
        if self.driver:
            print(f"Closing {self.driver_name} browser...")
            self.driver.quit()
            self.driver = None
            self.driver_name = None
        else:
            print("No driver to quit")