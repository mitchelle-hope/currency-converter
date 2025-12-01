Moringa AI Capstone Project: Beginner's Toolkit with GenAI

**Author:** Mitchelle Hope  
**Technology:** Python with REST API Integration (ExchangeRate-API)  
**Project Type:** Command-Line Currency Converter  
**Date:** December 2025

---

## 📍 1. Title & Objective

### What Technology Did I Choose?
**Python REST API Integration** - Specifically building a currency converter that fetches real-time exchange rates from the ExchangeRate-API.

### Why Did I Choose It?
- Real-world application: Currency conversion is used daily in e-commerce, travel, and finance
- Combines multiple concepts: API calls, error handling, data structures, and user interaction
- Demonstrates practical problem-solving with external data sources
- Portfolio-ready project that shows technical competency

### End Goal
Create a fully functional command-line currency converter that:
- Fetches real-time exchange rates from an external API
- Converts between 150+ world currencies
- Handles network errors gracefully with offline fallback
- Provides a professional, menu-driven user interface
- Demonstrates clean code practices and proper documentation

---

## 🔍 2. Quick Summary of the Technology

### What is REST API Integration?
REST (Representational State Transfer) APIs allow applications to communicate over HTTP, enabling data exchange between different systems. In this project, we use the `requests` library in Python to fetch real-time currency exchange rates.

### Where Is It Used?
- **E-commerce platforms:** Payment processing in multiple currencies
- **Travel websites:** Real-time price conversions
- **Banking apps:** International money transfers
- **Financial dashboards:** Portfolio tracking across currencies
- **Mobile apps:** Any app dealing with international users

### Real-World Example
When you shop on Amazon and see prices in your local currency, or when PayPal converts USD to KES, they're using currency conversion APIs similar to what we built.

**Companies using this technology:**
- Stripe (payment processing)
- Wise (international transfers)
- Booking.com (hotel prices)
- Airbnb (listing conversions)

---

## 💻 3. System Requirements

### Operating System
- ✅ Windows 10/11
- ✅ macOS 10.14+
- ✅ Linux (Ubuntu 18.04+)

### Software Requirements
```
Python: 3.7 or higher
Code Editor: VS Code (recommended), PyCharm, or any text editor
Package Manager: pip (comes with Python)
Internet Connection: Required for real-time rates (optional for offline mode)
```

### Python Libraries
```
requests==2.31.0  # For HTTP requests to API
```

### Verification Commands
```bash
# Check Python version
python --version  # Should show 3.7+

# Check pip
pip --version

# Check internet connection
ping google.com
```

---

## 🚀 4. Installation & Setup Instructions

### Step 1: Clone or Download the Project
```bash
# Option A: Clone from GitHub
git clone https://github.com/yourusername/currency-converter.git
cd currency-converter

# Option B: Download ZIP and extract
# Navigate to the extracted folder
```

### Step 2: Create Virtual Environment (Recommended)
```bash
# Windows
python -m venv .venv
.venv\Scripts\activate

# macOS/Linux
python3 -m venv .venv
source .venv/bin/activate
```

**Expected Output:**
```
(.venv) PS C:\Users\mitch\...\Currency-Converter>
```
The `(.venv)` prefix shows the virtual environment is active.

### Step 3: Install Dependencies
```bash
pip install requests
```

**Expected Output:**
```
Collecting requests
  Downloading requests-2.31.0-py3-none-any.whl (62 kB)
Successfully installed requests-2.31.0
```

### Step 4: Verify Installation
```bash
python -c "import requests; print('✓ Requests library installed successfully')"
```

### Step 5: Run the Application
```bash
python currency_converter.py
```

**Expected First Screen:**
```
🌍 Welcome to Professional Currency Converter!
==================================================
Fetching latest exchange rates...
✓ Rates updated successfully (Base: USD)

==================================================
   CURRENCY CONVERTER
==================================================
1. Convert Currency
2. View Exchange Rates
3. List All Currencies
4. Update Rates
5. Exit
==================================================

Select an option (1-5): _
```

---

## 🎯 5. Minimal Working Example

### What Does This Example Do?
The converter fetches real-time exchange rates and converts 100 USD to Canadian Dollars (CAD).

### Code Walkthrough

```python
import requests
from datetime import datetime

# Step 1: Define the API endpoint
API_URL = "https://api.exchangerate-api.com/v4/latest/USD"

# Step 2: Make HTTP GET request
response = requests.get(API_URL, timeout=5)

# Step 3: Parse JSON response
data = response.json()
rates = data['rates']

# Step 4: Get specific rate
cad_rate = rates['CAD']

# Step 5: Perform conversion
amount_usd = 100
amount_cad = amount_usd * cad_rate

# Step 6: Display result
print(f"100 USD = {amount_cad:.2f} CAD")
```

### Expected Output
```
100 USD = 132.00 CAD
```

### How It Works
1. **API Call:** Sends GET request to ExchangeRate-API
2. **JSON Response:** Receives data containing all exchange rates
3. **Rate Extraction:** Gets CAD rate from the response dictionary
4. **Conversion:** Multiplies USD amount by CAD rate
5. **Formatting:** Displays result with 2 decimal places

### Full Feature Demonstration

**Test Case 1: Convert Currency**
```
Select an option (1-5): 1

Enter amount: 100
From currency (e.g., USD): USD
To currency (e.g., EUR): KES

✓ 100.0 USD = 12950.00 KES
```

**Test Case 2: View All Currencies**
```
Select an option (1-5): 3

✓ 161 currencies supported:
----------------------------------------
  AED  AFN  ALL  AMD  ANG  AOA  ARS  AUD  AWG  AZN
  [... 161 currencies total ...]
```

**Test Case 3: Offline Mode**
```
# Disconnect internet and run

⚠️  Unable to fetch rates. Using offline rates...
✓ Using offline rates

# Still works with 10 fallback currencies
```

---

## 🤖 6. AI Prompt Journal

### Overview
I used GenAI (Claude at ai.moringaschool.com) throughout the development process to learn Python API integration, handle errors, and structure the project professionally.

---

### Prompt 1: Initial Learning
**Link to Curriculum:** [Introduction to APIs](https://ai.moringaschool.com)

**Prompt Used:**
```
I want to learn Python. Provide a guided learning experience tailored to my background 
and goals. I am an entry level python coder and want to create a currency converter 
system for two hours. Deliver a structured learning plan with hands-on exercises, 
real-world examples, and a simple runnable currency converter.
```

**AI's Response Summary:**
The AI provided a comprehensive 2-hour learning path covering:
- Python fundamentals (variables, data types, functions)
- Dictionary usage for storing exchange rates
- API integration with the `requests` library
- Error handling with try-except blocks
- Complete working code with professional structure

**What I Learned:**
- How to structure a Python project with classes
- The importance of error handling for network requests
- Using dictionaries to store and access exchange rates efficiently
- Type hints for better code documentation

**Evaluation:** ⭐⭐⭐⭐⭐ (5/5)
- Extremely helpful for understanding project structure
- Provided working code that I could build upon
- Explained concepts with practical examples

---

### Prompt 2: Fixing API Errors
**Link to Curriculum:** [Error Handling](https://ai.moringaschool.com)

**Prompt Used:**
```
I'm getting an error: "Failed to resolve 'api.frankfruter.app'" 
Why am I getting this error and how can I fix it?
```

**AI's Response Summary:**
The AI identified a typo in my API URL:
- Wrong: `api.frankfruter.app`
- Correct: `api.frankfurter.app`
- Explained DNS resolution errors
- Provided corrected code with proper error handling

**What I Learned:**
- How to read Python error stack traces
- Network errors mean DNS/connection issues
- Importance of double-checking URLs
- Adding timeout parameters to prevent hanging

**Evaluation:** ⭐⭐⭐⭐⭐ (5/5)
- Quickly identified the root cause
- Explained technical concepts clearly
- Provided prevention strategies

---

### Prompt 3: Understanding Code Structure
**Link to Curriculum:** [Object-Oriented Programming](https://ai.moringaschool.com)

**Prompt Used:**
```
What is the code expected to do? What output should I expect from terminal?
```

**AI's Response Summary:**
The AI provided:
- Detailed breakdown of each code section
- Expected terminal output for each menu option
- Flow diagrams showing program logic
- Test cases with expected results

**What I Learned:**
- How the menu system loops continuously
- How the CurrencyConverter class encapsulates logic
- The conversion formula: `(amount / from_rate) * to_rate`
- Expected behavior for edge cases (errors, offline mode)

**Evaluation:** ⭐⭐⭐⭐⭐ (5/5)
- Clear explanation of program flow
- Visual examples of expected output
- Helped me understand before running code

---

### Prompt 4: Capstone Alignment
**Link to Curriculum:** [Project Documentation](https://ai.moringaschool.com)

**Prompt Used:**
```
1. Is it safe to push this to GitHub?
2. Add a README that aligns with the capstone agenda
3. Ensure I achieve the deliverables of the capstone project
4. Does my project show what is needed on a scale of 1-10?
```

**AI's Response Summary:**
The AI confirmed:
- ✅ Code is safe to push (no secrets/credentials)
- Project rating: 8.5/10
- Missing: AI prompt documentation and common errors section
- Provided capstone-formatted README template

**What I Learned:**
- How to document learning process with AI
- Importance of reflection in technical writing
- GitHub safety practices (what not to commit)
- Professional README structure

**Evaluation:** ⭐⭐⭐⭐⭐ (5/5)
- Thorough project evaluation
- Actionable improvement suggestions
- Capstone-specific guidance

---

### Overall AI Learning Reflection

**How GenAI Improved My Productivity:**
1. **Accelerated Learning:** What might take days of reading docs took 2 hours
2. **Error Resolution:** Instant debugging help instead of googling for hours
3. **Best Practices:** Learned professional code structure from the start
4. **Documentation:** Got help creating professional-grade documentation

**What AI Did Well:**
- Provided context-aware explanations
- Generated working, tested code
- Explained "why" not just "how"
- Adapted to my skill level

**What I Had to Figure Out Myself:**
- Understanding Python virtual environments
- Choosing between different API providers
- Customizing the code for my preferences
- Testing edge cases thoroughly

**Key Takeaway:**
GenAI is an incredible learning accelerator, but hands-on practice and testing are essential. The AI gave me the roadmap; I had to walk the path.

---

## 🐛 7. Common Issues & Fixes

### Issue 1: Module Not Found Error
**Error Message:**
```
ModuleNotFoundError: No module named 'requests'
```

**Cause:** The `requests` library is not installed in your Python environment.

**Solution:**
```bash
# Make sure virtual environment is activated
pip install requests

# Verify installation
python -c "import requests; print('✓ Success')"
```

**Reference:** [Python Package Installation Guide](https://packaging.python.org/tutorials/installing-packages/)

---

### Issue 2: Network/Connection Errors
**Error Message:**
```
urllib3.exceptions.NameResolutionError: Failed to resolve 'api.exchangerate-api.com'
socket.gaierror: [Errno 11001] getaddrinfo failed
```

**Cause:** 
- No internet connection
- Firewall blocking requests
- DNS issues
- Typo in API URL

**Solution:**
```python
# The code already handles this with fallback rates
# But you can test your connection:

import requests
try:
    response = requests.get("https://www.google.com", timeout=5)
    print("✓ Internet connection working")
except:
    print("❌ No internet - check your connection")
```

**What Happens:**
- App automatically switches to offline mode
- Uses 10 pre-defined currency rates
- Shows warning: "⚠️ Unable to fetch rates. Using offline rates..."

**Reference:** [Requests Library Error Handling](https://docs.python-requests.org/en/latest/user/quickstart/#errors-and-exceptions)

---

### Issue 3: Invalid Currency Code
**Error Message:**
```
❌ Currency not found or conversion failed.
```

**Cause:** Entered currency code not supported or misspelled.

**Solution:**
```bash
# Use option 3 to see all available currencies
Select an option (1-5): 3

# Common valid codes:
USD - US Dollar
EUR - Euro
GBP - British Pound
KES - Kenyan Shilling
JPY - Japanese Yen
CAD - Canadian Dollar

# Invalid examples:
UK  - Wrong (use GBP)
DOLLAR - Wrong (use USD)
usa - Wrong (must be uppercase: USA is not valid, USD is)
```

**Reference:** [ISO 4217 Currency Codes](https://en.wikipedia.org/wiki/ISO_4217)

---

### Issue 4: Invalid Amount Input
**Error Message:**
```
❌ Invalid input. Please enter a valid amount.
```

**Cause:** Entered non-numeric value when amount was expected.

**Solution:**
```bash
# ❌ Wrong inputs:
Enter amount: abc
Enter amount: $100
Enter amount: one hundred

# ✅ Correct inputs:
Enter amount: 100
Enter amount: 100.50
Enter amount: 0.99
```

**Code Explanation:**
```python
# This is what happens behind the scenes:
try:
    amount = float(input("\nEnter amount: "))  # Converts to number
except ValueError:  # Catches non-numeric input
    print("❌ Invalid input. Please enter a valid amount.")
```

---

### Issue 5: Virtual Environment Not Activating
**Problem:** Commands not recognizing installed packages.

**Windows Solution:**
```bash
# If PowerShell blocks scripts:
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

# Then activate:
.venv\Scripts\activate
```

**macOS/Linux Solution:**
```bash
# Make sure you're using source, not just running the file
source .venv/bin/activate

# If permission denied:
chmod +x .venv/bin/activate
```

**Verification:**
```bash
# You should see (.venv) prefix:
(.venv) PS C:\...\Currency-Converter>
```

**Reference:** [Python Virtual Environments Guide](https://docs.python.org/3/tutorial/venv.html)

---

### Issue 6: API Rate Limiting
**Error Message:**
```
Error: API returned status code 429
```

**Cause:** Too many requests to the API in a short time (rare with free tier).

**Solution:**
- Wait 1-2 minutes before trying again
- The app uses offline mode automatically
- Free tier allows 1,500 requests/month

**Code Enhancement:**
```python
# Add rate limit handling:
if response.status_code == 429:
    print("⚠️ Rate limit reached. Using cached rates...")
    # Use fallback rates
```

---

### Issue 7: Python Version Too Old
**Error Message:**
```
SyntaxError: invalid syntax (f-strings not supported)
```

**Cause:** Using Python version below 3.6.

**Solution:**
```bash
# Check version
python --version

# If below 3.7, upgrade Python:
# Windows: Download from python.org
# Mac: brew install python3
# Linux: sudo apt update && sudo apt install python3.10
```

---

## 📚 8. References

### Official Documentation
- [Python Official Tutorial](https://docs.python.org/3/tutorial/) - Python basics
- [Requests Library Documentation](https://docs.python-requests.org/) - HTTP requests in Python
- [ExchangeRate-API Docs](https://www.exchangerate-api.com/docs/overview) - API used in project

### Video Tutorials
- [Python Requests Library Tutorial](https://www.youtube.com/watch?v=tb8gHvYlCFs) - Corey Schafer
- [Working with APIs in Python](https://www.youtube.com/watch?v=9JNoTj0u-2g) - Tech With Tim
- [Python Error Handling](https://www.youtube.com/watch?v=NIWwJbo-9_8) - Programming with Mosh

### Helpful Blog Posts
- [Real Python: API Integration Guide](https://realpython.com/api-integration-in-python/)
- [How to Structure Python Projects](https://docs.python-guide.org/writing/structure/)
- [Best Practices for Error Handling](https://realpython.com/python-exceptions/)

### Tools Used
- **VS Code:** Code editor ([download](https://code.visualstudio.com/))
- **Git:** Version control ([download](https://git-scm.com/))
- **GitHub:** Code hosting ([github.com](https://github.com))
- **Claude AI:** Learning assistant ([ai.moringaschool.com](https://ai.moringaschool.com))

### API Resources
- [ExchangeRate-API](https://www.exchangerate-api.com/) - Primary API used
- [Frankfurter API](https://www.frankfurter.app/) - Alternative option
- [ISO 4217 Currency Codes](https://www.iban.com/currency-codes) - Valid currency codes

### Troubleshooting Resources
- [Stack Overflow: Python Requests](https://stackoverflow.com/questions/tagged/python-requests)
- [Python Error Messages Explained](https://realpython.com/python-traceback/)
- [Network Debugging Guide](https://www.geeksforgeeks.org/python-network-programming/)

---

## 🎓 Learning Outcomes

### Skills Demonstrated
✅ **API Integration:** Successfully integrated external REST API  
✅ **Error Handling:** Implemented comprehensive try-except blocks  
✅ **Object-Oriented Programming:** Created well-structured classes  
✅ **User Interface:** Built intuitive menu-driven CLI  
✅ **Data Structures:** Used dictionaries for efficient data storage  
✅ **Documentation:** Added clear docstrings and comments  
✅ **Version Control:** Prepared project for GitHub  
✅ **Problem-Solving:** Debugged errors and implemented solutions  

### Before vs After This Project

| Aspect | Before | After |
|--------|--------|-------|
| API Knowledge | None | Can integrate REST APIs |
| Error Handling | Basic | Professional try-except usage |
| Code Structure | Scripts | Object-oriented classes |
| Documentation | Minimal | Comprehensive README |
| Debugging | Struggled | Can read stack traces |
| Git/GitHub | Unfamiliar | Repo-ready projects |

---

## 🚀 Running the Project

### Quick Start
```bash
# 1. Navigate to project folder
cd currency-converter

# 2. Activate virtual environment (if created)
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # Mac/Linux

# 3. Run the application
python currency_converter.py

# 4. Try option 1: Convert 100 USD to KES
```

### Sample Usage Session
```
Select an option (1-5): 1
Enter amount: 500
From currency (e.g., USD): USD
To currency (e.g., EUR): KES
✓ 500.0 USD = 64750.00 KES

Select an option (1-5): 3
✓ 161 currencies supported
[Lists all currencies...]

Select an option (1-5): 5
👋 Thank you for using Currency Converter!
```

---

## 📦 Project Structure
```
currency-converter/
│
├── currency_converter.py    # Main application
├── requirements.txt         # Dependencies
├── README.md               # This file
├── .gitignore             # Git ignore rules
│
└── .venv/                 # Virtual environment (not in git)
```

---

## 🌟 Future Enhancements

### Planned Features
- [ ] Historical rate tracking (show rate changes over time)
- [ ] Cryptocurrency support (Bitcoin, Ethereum)
- [ ] GUI version using Tkinter
- [ ] Export conversion history to CSV
- [ ] Multi-currency comparison tool
- [ ] Rate alerts (notify when rate reaches target)

---

## 📄 License
MIT License - Free to use and modify

---

## 👤 Author
**Mitchelle Hope**
- GitHub: [@mitchelle-hope](https://github.com/mitchelle-hope)
- Email: mitchelle.hope@student.moringaschool.com
- Moringa School: AI Capstone Project 2025


## 🙏 Acknowledgments
- **Moringa School:** For the structured learning opportunity
- **Claude AI:** For guided learning and debugging assistance
- **ExchangeRate-API:** For providing free, reliable currency data
- **Python Community:** For excellent documentation and resources
