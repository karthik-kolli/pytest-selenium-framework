from abc import ABC, abstractmethod
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from config.browser_options import OPTION_MAP# your mapping from logical keys to args

class DriverManager(ABC):
    """
    Abstract base class responsible ONLY for
    browser lifecycle management.
    """

    def __init__(self):
        self.driver = None   # Memory slot for browser reference

    @abstractmethod
    def start_browser(self):
        pass
    
    """
    Quitbrowser is common for all the browsers
    """
    def quit_browser(self):
        if self.driver:
            print("Closing browser...")
            self.driver.quit()
            self.driver = None
        else:
            print("No browser to close")




class ChromeDriverManager(DriverManager):
    def start_browser(self, options_conf=None):
        """
        options_conf: dict of boolean flags from JSON
        Example: {'headless': True, 'disable_gpu': True}
        """
        if options_conf is None:
            options_conf = {}

        # Create ChromeOptions object
        options = ChromeOptions()

        # Loop through options_conf and add arguments dynamically
        for key, apply_flag in options_conf.items():
            if apply_flag:
                flag = OPTION_MAP.get(key)
                if flag:
                    options.add_argument(flag)

        # Create WebDriver
        self.driver = webdriver.Chrome(options=options)
        print("created driver in chromemanager ",self.driver)
        print("Chrome started with options:", [k for k, v in options_conf.items() if v])
        return self.driver





from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from core.driver_manager import DriverManager
from config.browser_options import OPTION_MAP

class FirefoxDriverManager(DriverManager):
    def start_browser(self, options_conf=None):
        if options_conf is None:
            options_conf = {}

        options = FirefoxOptions()
        for key, apply_flag in options_conf.items():
            if apply_flag:
                flag = OPTION_MAP.get(key)
                if flag:
                    options.add_argument(flag)

        self.driver = webdriver.Firefox(options=options)
        print("Firefox started with options:", [k for k, v in options_conf.items() if v])
        return self.driver



from selenium import webdriver
from selenium.webdriver.edge.options import Options as EdgeOptions
from core.driver_manager import DriverManager
from config.browser_options import OPTION_MAP

class EdgeDriverManager(DriverManager):
    def start_browser(self, options_conf=None):
        if options_conf is None:
            options_conf = {}

        options = EdgeOptions()
        for key, apply_flag in options_conf.items():
            if apply_flag:
                flag = OPTION_MAP.get(key)
                if flag:
                    options.add_argument(flag)

        self.driver = webdriver.Edge(options=options)
        print("Edge started with options:", [k for k, v in options_conf.items() if v])
        return self.driver
    

from selenium import webdriver
from core.driver_factory import DriverFactory
from config.browser_options import OPTION_MAP
if __name__ == "__main__":
    factory = DriverFactory()
    driver = factory.create_driver()  # automatically picks browser with run=True
    if driver:

        driver.get("https://google.com")

    factory.quit_driver()
