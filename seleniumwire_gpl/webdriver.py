from seleniumwire.webdriver import DriverCommonMixin
from seleniumwire.options import SeleniumWireOptions
from seleniumwire.inspect import InspectRequestsMixin
import undetected_chromedriver as uc

class UndetectedChrome(uc.Chrome, InspectRequestsMixin, DriverCommonMixin):
    def __init__(self, *args, seleniumwire_options: SeleniumWireOptions = SeleniumWireOptions(), **kwargs):
        """Initialise a new Undetected Chrome WebDriver instance."""
        options = kwargs.get("options", uc.ChromeOptions())
        if not isinstance(options, uc.ChromeOptions):
            raise ValueError(
                "You must use undetected_chromedriver.ChromeOptions with this "
                "webdriver"
            )
        kwargs["options"] = options
        self._setup_backend(seleniumwire_options, options)
        super().__init__(*args, **kwargs)
