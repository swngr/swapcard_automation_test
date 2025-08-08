# 🧪 Google Book Shopping Test Automation

This is an automated UI test project built with **Python 3.12.4**, **pytest**, and **Selenium** to validate book search results on Google Shopping.

The project follows the **Page Object Model (POM)** design pattern, supports **Allure reporting**, and checks that all book products **from the second onward** meet a specified **minimum rating** threshold.

---

## 📁 Project Structure

```
.
├── pages/
│   ├── base_page.py
│   ├── landing_page.py
│   └── shopping_page.py
│
├── tests/
│   └── test_google_book_shopping.py
│
├── utils/
│   ├── config.py
│   └── helpers.py
│
├── conftest.py
├── pytest.ini
├── requirements.txt
└── screenshots/
```

---

## ✅ Features

- ✅ Page Object Model (POM)
- ✅ Parametrized test cases using `pytest.mark.parametrize`
- ✅ Allure reporting support
- ✅ Supports both headless and headed modes (via CLI)
- ✅ Visual debug highlighting in browser
- ✅ Screenshots captured on test failure
- ✅ Ratings extracted from product cards and validated from the second onward

---

## 🚀 How to Run

### 1. Clone the repository

```bash
git clone https://github.com/your-username/google-shopping-automation.git
cd google-shopping-automation
```

### 2. Create virtual environment and install dependencies

```bash
python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows

pip install -r requirements.txt
```

---

### ⚙️ Optional: Run in Headless or Headed Mode

> By default, the test runs in headed mode (Chrome UI).

To run **in headless mode**:

```bash
pytest --headless
```

To run **with Chrome UI (headed)**:

```bash
pytest
```

> 💡 This requires Google not to trigger reCAPTCHA. If blocked, use the workaround below.

---

### ⚠️ If You're Blocked by Google reCAPTCHA

If you encounter Google's bot protection, you can manually launch Chrome in remote debugging mode to bypass it.

#### 🪟 Windows

```bash
chrome.exe --remote-debugging-port=9222 --user-data-dir="C:/tmp/chrome"
```

#### 🍎 macOS

```bash
/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome \
--remote-debugging-port=9222 --user-data-dir="/tmp/chrome"
```

Make sure your test project uses this `conftest.py` configuration:

```python
options.debugger_address = "127.0.0.1:9222"
```

---

### 3. Run the test

```bash
pytest
```

Or from **PyCharm**: right-click the test file and click **Run**.

---

### 4. View Allure Report (optional)

Install Allure CLI if not already:

- **macOS:** `brew install allure`
- **Windows:** `choco install allure`

Then run:

```bash
pytest --alluredir=reports
allure serve reports
```

---

## 🔧 Test Parameters

The test uses this default dataset (in `utils/config.py`):

```python
DEFAULT_BOOKS = [
    ("les miserables", 4000, 4.0),
]
```

This means the test will:
- Search for **"book les miserables"** on Google
- Set max price to **4000**
- Confirm all products **from the 2nd one onward** have a rating **≥ 4.0**

---

## 📄 What the Test Does

1. Launches Google
2. Searches for the book (e.g., "book les miserables")
3. Switches to the Shopping tab
4. Sorts by **Price: High to Low**
5. Filters by max price (`4000`)
6. Collects all product ratings
7. Logs and reports all ratings from the 2nd onward
8. Does **not fail the test** if any rating is below minimum — only reports them

---

## 🧪 Sample Output

**Console:**
```
[DEBUG] EVEN Index 0: Rating = 4.9
[DEBUG] EVEN Index 2: Rating = 4.6
[DEBUG] EVEN Index 4: Rating = 3.7  ❌ Below threshold
```

**Allure Attachments:**
- ✅ Second product rating
- ⚠️ Any ratings below the threshold

---

## 📦 Dependencies

See `requirements.txt`:

```txt
selenium==4.21.0
pytest==8.2.1
allure-pytest==2.13.2
webdriver-manager==4.0.1
```
