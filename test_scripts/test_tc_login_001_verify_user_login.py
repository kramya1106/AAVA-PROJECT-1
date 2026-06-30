"""
Test Case ID: TC_LOGIN_001
Title: Verify user can login with valid credentials
Description: This test case verifies that a user can successfully login to the application 
using valid username and password credentials. The test validates the complete login flow 
from navigation to the login page through successful authentication and landing on the dashboard.
"""

import traceback
import pytest
from core.playwright_manager import PlaywrightManager
from core.settings import framework_logger
from helper.hpid_helper import HPIDHelper
from helper.dashboard_helper import DashboardHelper
from pages.hpid_page import HPIDPage
from pages.overview_page import OverviewPage
from pages.dashboard_side_menu_page import DashboardSideMenuPage
from playwright.sync_api import expect
import test_flows_common.test_flows_common as common
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


@pytest.mark.usefixtures("main_execution")
def test_tc_login_001_verify_user_login(stage_callback, tc_tracer, reporter):
    tcid = "TC_LOGIN_001"
    current_step = "Step 0"
    current_validation = "Initialization"
    
    USERNAME = "testuser@example.com"
    PASSWORD = "Test@12345"
    
    try:
        common.setup()
        
        # ── Step 1: Navigate to application URL ──
        current_step = "Step 1"
        current_validation = "Application login page should be displayed"
        
        with PlaywrightManager() as page:
            hpid_page = HPIDPage(page)
            page.goto("https://instantink.hpconnected.com")
            page.wait_for_load_state("networkidle", timeout=30000)
            expect(hpid_page.login_form).to_be_visible(timeout=30000)
            
            stage_callback("step1_login_page", page, screenshot_only=True)
            framework_logger.info(f"[{tcid}] Step 1: Navigated to login page successfully")
            reporter.validate(True, f"[{tcid}] Step 1: Navigated to login page successfully")
            
            # ── Step 2: Enter valid username in username field ──
            current_step = "Step 2"
            current_validation = "Username should be entered successfully"
            
            hpid_page.email_input.clear()
            hpid_page.email_input.fill(USERNAME)
            expect(hpid_page.email_input).to_have_value(USERNAME, timeout=10000)
            
            framework_logger.info(f"[{tcid}] Step 2: Username entered successfully")
            reporter.validate(True, f"[{tcid}] Step 2: Username entered successfully")
            
            # ── Step 3: Enter valid password in password field ──
            current_step = "Step 3"
            current_validation = "Password should be entered successfully"
            
            hpid_page.password_input.clear()
            hpid_page.password_input.fill(PASSWORD)
            expect(hpid_page.password_input).not_to_be_empty(timeout=10000)
            
            framework_logger.info(f"[{tcid}] Step 3: Password entered successfully")
            reporter.validate(True, f"[{tcid}] Step 3: Password entered successfully")
            
            # ── Step 4: Click on Login button ──
            current_step = "Step 4"
            current_validation = "User should be redirected to dashboard page"
            
            hpid_page.sign_in_button.click()
            page.wait_for_url("**/dashboard**", timeout=30000)
            
            overview_page = OverviewPage(page)
            expect(overview_page.dashboard_container).to_be_visible(timeout=30000)
            
            stage_callback("step4_dashboard_redirect", page, screenshot_only=True)
            framework_logger.info(f"[{tcid}] Step 4: User redirected to dashboard page successfully")
            reporter.validate(True, f"[{tcid}] Step 4: User redirected to dashboard page successfully")
            
            # ── Step 5: Verify dashboard page is displayed ──
            current_step = "Step 5"
            current_validation = "Dashboard page should be visible with user information"
            
            expect(overview_page.dashboard_container).to_be_visible(timeout=30000)
            expect(overview_page.user_info_section).to_be_visible(timeout=30000)
            
            framework_logger.info(f"[{tcid}] Step 5: Dashboard page displayed with user information")
            reporter.validate(True, f"[{tcid}] Step 5: Dashboard page displayed with user information")
            
            # ── Step 6: Verify user name is displayed on dashboard ──
            current_step = "Step 6"
            current_validation = "User name should be visible on the dashboard"
            
            expect(overview_page.user_name_display).to_be_visible(timeout=30000)
            user_name_text = overview_page.user_name_display.text_content()
            expect(overview_page.user_name_display).to_contain_text(USERNAME, timeout=10000)
            
            framework_logger.info(f"[{tcid}] Step 6: User name displayed on dashboard: {user_name_text}")
            reporter.validate(True, f"[{tcid}] Step 6: User name displayed on dashboard: {user_name_text}")
            
            # ── Step 7: Verify navigation menu is displayed ──
            current_step = "Step 7"
            current_validation = "Navigation menu should be visible with all menu items"
            
            side_menu = DashboardSideMenuPage(page)
            expect(side_menu.navigation_menu).to_be_visible(timeout=30000)
            menu_items_count = side_menu.menu_items.count()
            
            framework_logger.info(f"[{tcid}] Step 7: Navigation menu displayed with {menu_items_count} items")
            reporter.validate(True, f"[{tcid}] Step 7: Navigation menu displayed with {menu_items_count} items")
            
            # ── Step 8: Verify logout button is displayed ──
            current_step = "Step 8"
            current_validation = "Logout button should be visible"
            
            expect(side_menu.logout_button).to_be_visible(timeout=30000)
            
            stage_callback("step8_logout_button", page, screenshot_only=True)
            framework_logger.info(f"[{tcid}] Step 8: Logout button is visible")
            reporter.validate(True, f"[{tcid}] Step 8: Logout button is visible")
            
            # ── Step 9: Click on logout button ──
            current_step = "Step 9"
            current_validation = "User should be logged out and redirected to login page"
            
            side_menu.logout_button.click()
            page.wait_for_url("**/login**", timeout=30000)
            
            hpid_page_after_logout = HPIDPage(page)
            expect(hpid_page_after_logout.login_form).to_be_visible(timeout=30000)
            
            framework_logger.info(f"[{tcid}] Step 9: User logged out and redirected to login page")
            reporter.validate(True, f"[{tcid}] Step 9: User logged out and redirected to login page")
            
            # ── Step 10: Verify user is on login page ──
            current_step = "Step 10"
            current_validation = "Login page should be displayed with login form"
            
            expect(hpid_page_after_logout.login_form).to_be_visible(timeout=30000)
            expect(hpid_page_after_logout.email_input).to_be_visible(timeout=10000)
            expect(hpid_page_after_logout.password_input).to_be_visible(timeout=10000)
            
            stage_callback("step10_login_page_after_logout", page, screenshot_only=True)
            framework_logger.info(f"[{tcid}] Step 10: Login page displayed with login form after logout")
            reporter.validate(True, f"[{tcid}] Step 10: Login page displayed with login form after logout")
            
    except Exception as e:
        framework_logger.error(
            f"[{tcid}] Test failed at {current_step} — {current_validation}: "
            f"{e}\n{traceback.format_exc()}"
        )
        reporter.validate(False, f"[{tcid}] FAIL at {current_step} — {current_validation}: {str(e)}")
        raise
