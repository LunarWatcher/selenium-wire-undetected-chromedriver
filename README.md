# selenium-wire-undetected-chromedriver

This project is an extension of [selenium-wire-lw](https://github.com/LunarWatcher/selenium-wire/) that adds an `UndetectedChrome` driver. This project only contains the `UndetectedChrome` webdriver. selenium-wire-lw is MIT-licensed and therefore compatible with GPLv3, but because GPL, this only works if selenium-wire-lw is a dependency. To avoid the implications of relicensing code, `UndetectedChrome` has to be separate from the main project, even though it's an optional dependency. Thanks, GPL.

For documentation and bug reports with selenium-wire itself, go to [selenium-wire-lw](https://github.com/LunarWatcher/selenium-wire/). Bug reports about specifically the undetected_chromedriver integration go in this repo.

## Usage
```
pip3 install selenium-wire-undetected-chromedriver
```
```python
from seleniumwire_gpl import UndetectedChrome

driver = UndetectedChrome(...)
```

For extended config and selenium-wire features, see the [selenium-wire repo](https://github.com/LunarWatcher/selenium-wire/)

## License

This project is forcibly licensed under GPLv3, because undetected_chromedriver, the problem dependency, is licensed under [GPLv3](https://github.com/ultrafunkamsterdam/undetected-chromedriver/blob/master/LICENSE). For the full license text, see the LICENSE file.

The other dependencies have other licenses:

* selenium-wire-lw: [MIT](https://github.com/LunarWatcher/selenium-wire/blob/master/LICENSE), with the following direct dependencies:
    * selenium: [Apache 2.0](https://github.com/SeleniumHQ/selenium/blob/trunk/LICENSE)
    * mitmproxy: [MIT](https://github.com/mitmproxy/mitmproxy/blob/main/LICENSE)
    * brotli: [MIT](https://github.com/google/brotli/blob/master/LICENSE)
    * python-zstd: [BSD 2-Clause](https://github.com/sergey-dryabzhinsky/python-zstd/blob/master/LICENSE)
* setuptools: [MIT](https://github.com/pypa/setuptools/blob/main/LICENSE)
    * Note: temporary dependency due to an upstream bug in undetected_chromedriver.

There are quite a few additional indirect dependencies not listed here as well.
