import os
import pytest
from datetime import datetime
from playwright.sync_api import sync_playwright
from pytest_html import extras
from utils.config import REPORTS_DIR

os.makedirs(REPORTS_DIR, exist_ok=True)

# -----------------------------
# Session-scoped fixture for Playwright
# -----------------------------
@pytest.fixture(scope="session")
def playwright_instance():
    """Start Playwright once per session."""
    with sync_playwright() as p:
        yield p


# -----------------------------
# Function-scoped fixture for Browser + Page
# -----------------------------
@pytest.fixture(scope="function")
def browser_context(playwright_instance, request):
    """Create a new browser page for each test."""
    browser = playwright_instance.chromium.launch(headless=False)
    context = browser.new_context(viewport={"width": 1280, "height": 720})
    page = context.new_page()

    yield page

    # Teardown: screenshot if test failed
    rep_call = getattr(request.node, "rep_call", None)
    if rep_call and rep_call.failed:
        ts = datetime.utcnow().strftime("%Y%m%dT%H%M%SZ")
        screenshot_path = os.path.join(REPORTS_DIR, f"{request.node.name}_{ts}.png")
        page.screenshot(path=screenshot_path, full_page=True)
        if hasattr(rep_call, "extra"):
            rep_call.extra.append(extras.image(screenshot_path))
        else:
            rep_call.extra = [extras.image(screenshot_path)]

    context.close()
    browser.close()


# -----------------------------
# Hook to attach test results to item
# -----------------------------
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
