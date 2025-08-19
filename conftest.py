import pytest
from playwright.sync_api import Page

# Per-test setup fixture to load the page
@pytest.fixture(autouse=True)
def load_page(page: Page):
	page.goto("https://demo.biometric.sk/")
import pytest

# Global setup fixture
@pytest.fixture(scope="session", autouse=True)
def global_setup():
	print("\n[Setup] Starting test session...")
	yield
	print("\n[Teardown] Test session finished.")
