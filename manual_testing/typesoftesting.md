# Types of Testing in QA

A reference guide to the major categories of software testing, organized by purpose and approach.

## 1. By Level (Testing Pyramid)

### Unit Testing
Tests individual components or functions in isolation, usually written by developers.
- **Scope:** Single function, method, or class
- **Tools:** JUnit, pytest, Jest, NUnit
- **Goal:** Verify each piece of code works correctly on its own

### Integration Testing
Tests how multiple units or modules work together.
- **Scope:** Interactions between components (e.g., API calls, database access)
- **Tools:** Postman, TestNG, Supertest
- **Goal:** Catch issues at the boundaries between modules

### System Testing
Tests the complete, integrated application as a whole.
- **Scope:** End-to-end application behavior
- **Goal:** Validate the system meets specified requirements

### Acceptance Testing
Confirms the software meets business needs and is ready for release.
- **Types:** User Acceptance Testing (UAT), Business Acceptance Testing (BAT)
- **Goal:** Get sign-off from stakeholders or end users

---

## 2. By Execution Method

### Manual Testing
A human tester executes test cases without automation scripts.
- **Best for:** Exploratory testing, usability checks, one-off or early-stage testing

### Automated Testing
Test cases are executed via scripts and tools.
- **Best for:** Regression suites, repetitive tests, CI/CD pipelines
- **Tools:** Selenium, Cypress, Playwright, Appium

---

## 3. By Knowledge of Internal Structure

### Black Box Testing
Tester has no knowledge of internal code; focuses on inputs and outputs.
- **Examples:** Functional testing, acceptance testing

### White Box Testing
Tester has full knowledge of internal code structure and logic.
- **Examples:** Unit testing, code coverage analysis, path testing

### Gray Box Testing
A hybrid — tester has partial knowledge of internal workings.
- **Examples:** Integration testing with some architectural knowledge

---

## 4. Functional Testing Types

| Type | Purpose |
|---|---|
| **Smoke Testing** | Quick check that critical functions work after a build |
| **Sanity Testing** | Narrow, focused check after a minor change or bug fix |
| **Regression Testing** | Ensures new changes haven't broken existing functionality |
| **Functional Testing** | Verifies each feature works according to requirements |
| **Interface Testing** | Validates communication between systems (APIs, UI-to-backend) |

---

## 5. Non-Functional Testing Types

| Type | Purpose |
|---|---|
| **Performance Testing** | Measures speed, responsiveness, and stability under load |
| **Load Testing** | Checks behavior under expected user load |
| **Stress Testing** | Pushes the system beyond limits to find breaking points |
| **Scalability Testing** | Measures how well the system scales with increased demand |
| **Security Testing** | Identifies vulnerabilities and ensures data protection |
| **Usability Testing** | Evaluates ease of use and user experience |
| **Compatibility Testing** | Confirms the app works across browsers, devices, and OS versions |
| **Accessibility Testing** | Ensures the app is usable by people with disabilities (WCAG compliance) |
| **Reliability Testing** | Verifies consistent performance over time |
| **Volume Testing** | Tests behavior with large amounts of data |

---

## 6. Other Notable Testing Types

### Exploratory Testing
Testers actively explore the application without predefined test scripts, using intuition and experience to find defects.

### Ad Hoc Testing
Informal, unstructured testing performed without a plan, often to catch obvious issues quickly.

### Regression Testing
Re-running previously passed tests after code changes to ensure nothing broke.

### Alpha Testing
Internal testing conducted by the development/QA team before external release.

### Beta Testing
Testing conducted by real users in a live environment before final release.

### A/B Testing
Comparing two versions of a feature to determine which performs better.

### Mutation Testing
Introduces small code changes ("mutants") to check if the test suite catches them, validating test suite quality.

### Localization Testing
Verifies the application works correctly for a specific locale, language, or region.

### Recovery Testing
Tests how well an application recovers from crashes or failures.

---

## Choosing the Right Testing Type

- **Early in development:** Unit, integration, smoke
- **Before release:** Regression, system, UAT, security
- **Post-release / ongoing:** Performance, monitoring, A/B testing
- **User-facing concerns:** Usability, accessibility, compatibility

A solid QA strategy typically layers several of these types together, automating what's repeatable and reserving manual/exploratory testing for areas needing human judgment.