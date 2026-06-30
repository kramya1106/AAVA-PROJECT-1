"""
Additional methods for DashboardHelper
Merge into: helper/dashboard_helper.py
Instructions:
1. Add these static methods to the DashboardHelper class
"""

# Add these methods:

@staticmethod
def logout(page):
    """
    Perform logout action from dashboard.
    Clicks logout button, waits for navigation to login page, and verifies logout success.
    
    Args:
        page: Playwright page object
    """
    from pages.dashboard_side_menu_page import DashboardSideMenuPage
    from pages.hpid_page import HPIDPage
    from playwright.sync_api import expect
    from core.settings import framework_logger
    
    side_menu = DashboardSideMenuPage(page)
    
    # Click logout button
    if side_menu.logout_button.is_visible():
        side_menu.logout_button.click()
    else:
        # Handle dropdown case
        user_profile = page.locator(".user-profile, #userProfile, [data-testid='user-profile']")
        if user_profile.is_visible():
            user_profile.click()
            side_menu.logout_button.wait_for(state="visible", timeout=10000)
            side_menu.logout_button.click()
    
    # Wait for navigation to login page
    page.wait_for_url("**/login**", timeout=30000)
    
    # Verify login page is displayed
    hpid_page = HPIDPage(page)
    expect(hpid_page.login_form).to_be_visible(timeout=30000)
    
    framework_logger.info("Logout completed successfully")


@staticmethod
def verify_user_logged_in(page, expected_username=None):
    """
    Verify that user is logged in by checking dashboard elements.
    
    Args:
        page: Playwright page object
        expected_username: Optional username to verify (default: None)
    
    Returns:
        bool: True if user is logged in, False otherwise
    """
    from pages.overview_page import OverviewPage
    from playwright.sync_api import expect
    
    overview_page = OverviewPage(page)
    
    try:
        expect(overview_page.dashboard_container).to_be_visible(timeout=30000)
        expect(overview_page.user_info_section).to_be_visible(timeout=30000)
        
        if expected_username:
            expect(overview_page.user_name_display).to_contain_text(expected_username, timeout=10000)
        
        return True
    except Exception:
        return False
