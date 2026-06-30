"""
Additional locators and methods for HPIDPage
Merge into: pages/hpid_page.py
Instructions:
1. Add locators to __init__ method
2. Add methods to the class body
"""

# Add to __init__:
# self.elements.login_form = "form, .login-form, #loginForm"
# self.elements.email_input = "[data-testid='email'], #username, #email, input[type='email']"
# self.elements.password_input = "[data-testid='password'], #password, input[type='password']"
# self.elements.sign_in_button = "[data-testid='sign-in-btn'], button:has-text('Sign In'), button:has-text('Login')"

# Add these methods:

def navigate_to_login(self):
    """Navigate to the login page."""
    self.page.goto("https://instantink.hpconnected.com")
    self.page.wait_for_load_state("networkidle", timeout=30000)
    self.wait.login_form(state="visible", timeout=30000)


def enter_credentials(self, email: str, password: str):
    """
    Enter username and password credentials.
    
    Args:
        email: User email/username
        password: User password
    """
    self.email_input.clear()
    self.email_input.fill(email)
    self.password_input.clear()
    self.password_input.fill(password)


def click_login_button(self):
    """Click the login/sign-in button and wait for navigation."""
    self.sign_in_button.click()
    self.page.wait_for_url("**/dashboard**", timeout=30000)


def verify_login_page_displayed(self):
    """Verify that the login page is displayed with login form visible."""
    from playwright.sync_api import expect
    expect(self.login_form).to_be_visible(timeout=30000)
    expect(self.email_input).to_be_visible(timeout=10000)
    expect(self.password_input).to_be_visible(timeout=10000)
