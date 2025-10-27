# Quick Start - Testing Guide

## 🚀 Getting Started in 5 Minutes

### Step 1: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 2: Run All Tests

```bash
python run_tests.py
```

### Step 3: View Results

Open `coverage_html/index.html` in your browser to see detailed coverage report.

---

## 📋 What's Included

1. **25 Test Cases** covering all features
2. **Automated test execution** with pytest
3. **Code coverage reporting** (HTML, terminal, XML)
4. **Test documentation** (Test Plan, Test Cases, Reports)

---

## 📁 Key Files

- `run_tests.py` - Run this to execute all tests
- `TEST_PLAN.md` - Complete test plan document
- `TEST_CASES.md` - 25 detailed test cases
- `TEST_EXECUTION_REPORT.md` - Template for test results
- `TESTING_README.md` - Detailed testing guide

---

## ✅ Test Execution

### Run All Tests
```bash
python run_tests.py
```

### Run Specific Module
```bash
pytest tests/test_auth.py -v
pytest tests/test_farmer.py -v
```

### Run Specific Test
```bash
pytest tests/test_auth.py::TestAuthentication::test_login_valid_credentials -v
```

---

## 📊 Test Coverage

After running tests, check:
- Terminal: Coverage summary
- HTML: `coverage_html/index.html` - Detailed coverage
- XML: `test-results.xml` - JUnit format

---

## 📚 Documentation

1. **TEST_PLAN.md** - Test strategy, scope, and approach
2. **TEST_CASES.md** - Detailed test cases with procedures
3. **TEST_EXECUTION_REPORT.md** - Template for results documentation
4. **TESTING_README.md** - Complete testing guide

---

## 🔍 Quick Reference

### Test Modules

- `test_auth.py` - Authentication (TC_001-TC_005)
- `test_farmer.py` - Farmer Management (TC_006-TC_010)
- Additional modules as needed

### Test Types

- ✅ Black-box testing
- ✅ White-box testing
- ✅ Unit testing
- ✅ Integration testing

---

## ⚠️ Troubleshooting

**Problem**: Module import errors
```bash
pip install -r requirements.txt
```

**Problem**: Database connection errors
- Ensure MySQL server is running
- Check database credentials in main.py

---

## 📞 Support

For detailed instructions, see `TESTING_README.md`

---

**Happy Testing! 🎉**
