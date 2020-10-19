import pytest
from SkyFrame.SkyscanPage import SkyscanPage
from SkyscannerTest.test_base import TestBase


class TestSmoke(TestBase):

    def test_end_to_end(self):
        self.skyscannerpage = SkyscanPage(self.driver)
        self.skyscannerpage.login()
        self.skyscannerpage.subscribe()
        self.skyscannerpage.get_currencies()
        assert self.skyscannerpage.get_browse_dates()


