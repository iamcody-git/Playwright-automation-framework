# Test Plan: SauceDemo

| Field | Details |
|---|---|
| **Project** | SauceDemo Web Application Testing |
| **Application URL** | https://www.saucedemo.com |
| **Prepared by** | Prashant  |
| **Version** | 1.0 |

---

## 1. Objective

Check that the main features of SauceDemo (login, products, cart, checkout, logout) work as expected, and record any bugs found.

## 2. Scope

### In scope
- **Login:** valid and invalid credentials, locked-out user, empty fields
- **Products page:** product list, product details, sorting, add/remove items
- **Cart:** add items, remove items, cart badge count, continue shopping
- **Checkout:** customer information form, order overview, order completion
- **Logout:** logging out and returning to the login page
- **Basic UI checks:** page titles, buttons, error messages, links

### Out of scope
- Performance and load testing
- Security testing
- Real payment processing (SauceDemo has none)
- Mobile apps (web browser only)

## 3. Test Types

- Functional testing
- Negative testing (invalid inputs)
- Basic UI/usability testing
- Cross-browser testing (basic)
- Regression testing (re-run after bug fixes)

## 4. Test Environment

| Item | Details |
|---|---|
| **Operating system** | Windows |
| **Browsers** | Chrome (primary), Firefox, Edge |
| **Screen** | Desktop / laptop |
| **Internet** | Required |

## 5. Test Data

**Password for all users:** `secret_sauce`

| Username | Purpose |
|---|---|
| `standard_user` | Normal user, main flow |
| `locked_out_user` | Should see a locked-out error |
| `problem_user` | Known to show broken images and behavior |
| `performance_glitch_user` | Slow response times |
| `error_user` | Triggers errors on some actions |
| `visual_user` | Shows visual differences in the UI |

**Checkout details:**

| Field | Value |
|---|---|
| First name | Test |
| Last name | User |
| Zip/Postal code | 12345 |

## 6. Deliverables

| File | Purpose |
|---|---|
| `01_test_plan.md` | This document |
| `02_test_scenarios.xlsx` | High-level list of what to test |
| `03_test_cases.xlsx` | Detailed test cases with steps |
| `04_test_execution_report.xlsx` | Results of each test run |
| `05_bug_reports.xlsx` | Bugs found during testing |

## 7. Tools

| Purpose | Tool |
|---|---|
| Test cases and reports | Excel or Google Sheets |
| Screenshots | Windows Snipping Tool |
| Bug tracking | Excel (or Jira, if available) |
| Browsers | Chrome, Firefox, Edge |

## 8. Entry and Exit Criteria

**Start testing when:**
- The website is reachable at the URL above
- Test data is ready
- Test cases are written and reviewed

**Stop testing when:**
- All planned test cases have been executed
- All critical and high-severity bugs are reported
- The execution report is complete

## 9. Bug Severity Levels

| Severity | Meaning | Example |
|---|---|---|
| **Critical** | Main feature does not work at all | Valid user cannot log in |
| **High** | Important feature broken, no workaround | Checkout cannot be completed |
| **Medium** | Feature works but with a problem | Sorting gives the wrong order |
| **Low** | Small cosmetic issue | Misaligned text or image |

## 10. Test Case ID Format

`TC_<MODULE>_<NUMBER>`, for example:
- `TC_LOGIN_001`
- `TC_INVENTORY_001`
- `TC_CART_001`
- `TC_CHECKOUT_001`
- `TC_LOGOUT_001`

## 11. Schedule

| Task | Duration | Status |
|---|---|---|
| Write test scenarios | 1 day | Not started |
| Write test cases | 2 days | Not started |
| Execute test cases | 2 days | Not started |
| Report bugs | Ongoing | Not started |
| Retest and final report | 1 day | Not started |

## 12. Risks and Assumptions

**Risks**
- SauceDemo is a public demo site, so it may be slow or unavailable at times.
- Some users (`problem_user`, `error_user`) are built to show bugs, so failures with them are expected.

**Assumptions**
- The website and test data stay the same during testing.
- Testing is done on a desktop browser.