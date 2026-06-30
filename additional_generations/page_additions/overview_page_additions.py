"""
Additional locators and methods for OverviewPage
Merge into: pages/overview_page.py
Instructions:
1. Add locators to __init__ method
2. Add methods to the class body
"""

# Add to __init__:
# self.elements.dashboard_container = "#dashboard, .dashboard-container, .main-content, [data-testid='dashboard']"
# self.elements.user_info_section = ".user-info, #userProfile, .user-section, [data-testid='user-info']"
# self.elements.user_name_display = ".username, .user-name, #userName, [data-testid='user-name']"

# Add these methods:

def verify_dashboard_displayed(self):
    """
    Verify that the dashboard page is displayed.
    Checks URL, dashboard container visibility, and user info section.
    """
    from playwright.sync_api import expect
    expect(self.page).to_have_url("**/dashboard**", timeout=30000)
    expect(self.dashboard_container).to_be_visible(timeout=30000)
    expect(self.user_info_section).to_be_visible(timeout=30000)


def get_user_name_text(self):
    """
    Retrieve the displayed user name text.
    
    Returns:
        str: The user name text displayed on the dashboard
    """
    self.wait.user_name_display(state="visible", timeout=30000)
    return self.user_name_display.text_content()
