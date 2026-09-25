## Getting Started
 
### Prerequisites
- Python 3.10+
- Git
### Installation
 
```bash
git clone https://github.com/iamcody-git/Playwright-automation-framework.git
cd Playwright-automation-framework/automation_testing
 
python -m venv venv
venv\Scripts\activate          # Windows
# source venv/bin/activate     # macOS/Linux
 
pip install -r requirements.txt
playwright install
```
 
### Running Tests
 
```bash
pytest                     # run the full suite
pytest -m smoke            # quick smoke check
pytest -m regression       # full regression set
pytest tests/test_login.py # a single module
pytest --headed             # watch the browser while it runs
```
 
## Reports
 
After each run, open `automation_testing/reports/report.html` in a browser. Screenshots of failed tests are saved in `automation_testing/reports/artifacts/`.
 
## Continuous Integration
 
Every push and pull request to `main` triggers the GitHub Actions workflow (`.github/workflows/playwright-tests.yml`), which installs dependencies, runs the full suite headless on Ubuntu, and uploads the HTML report as a downloadable artifact. See the **Actions** tab for run history.
 
## Design Notes
 
- **Page Object Model** keeps locators and page actions out of test files, so a UI change only requires updating one file in `pages/`.
- **Fixtures** in `conftest.py` chain naturally (`login_page` → `inventory_page` → `cart_page` → `checkout_page`), so each test file only asks for the state it needs.
- **Data-driven**: usernames, password, and checkout details live in `test_data/users.json`, not hardcoded in tests.
- **Markers** (`smoke`, `regression`) let you run a fast subset or the full suite.
