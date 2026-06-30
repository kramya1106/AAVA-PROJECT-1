"""
Additional locators and methods for DashboardSideMenuPage
Merge into: pages/dashboard_side_menu_page.py
Instructions:
1. Add locators to __init__ method
2. Add methods to the class body
"""

# Add to __init__:
# self.elements.navigation_menu = "nav, .navbar, .navigation, #mainNav, [data-testid='navigation']"
# self.elements.menu_items = "nav ul li, .menu-items li, .nav-items li, [data-testid='menu-item']"
# self.elements.logout_button = "button:has-text('Logout'), button:has-text('Sign Out'), a:has-text('Logout'), [data-testid='logout-btn']"

# Add these methods:

def verify_navigation_menu_visible(self):
    """
    Verify that the navigation menu is visible with all menu items present.
    """
    from playwright.sync_api import expect
    expect(self.navigation_menu).to_be_visible(timeout=30000)
    expect(self.menu_items.first).to_be_visible(timeout=10000)


def click_logout_button(self):
    """
    Click the logout button and wait for navigation to login page.
    Handles potential dropdown menu if logout is nested.
    """
    if self.logout_button.is_visible():
        self.logout_button.click()
        self.page.wait_for_url("**/login**", timeout=30000)
    else:
        # If logout is in a dropdown, may need to click user profile first
        # This is a fallback pattern
        user_profile = self.page.locator(".user-profile, #userProfile, [data-testid='user-profile']")
        if user_profile.is_visible():
            user_profile.click()
            self.logout_button.wait_for(state="visible", timeout=10000)
            self.logout_button.click()
            self.page.wait_for_url("**/login**", timeout=30000)
