# 🔒 Web Application Vulnerability Scanner

A lightweight Python-based scanner to detect common web application vulnerabilities such as **XSS**, **SQL Injection**, and **CSRF**. Designed with a user-friendly **Flask UI**, it crawls target URLs, injects payloads, and analyzes responses using pattern matching and regex—based on the **OWASP Top 10** security risks.

---

## 🚀 Features

- 🌐 **Crawler**: Automatically extracts internal links and input fields from target websites.
- 💉 **Payload Injection**: Tests for vulnerabilities by injecting predefined malicious payloads.
- 🔍 **Vulnerability Detection**:
  - **Cross-Site Scripting (XSS)**
  - **SQL Injection (SQLi)**
  - **Cross-Site Request Forgery (CSRF)**
- 📊 **Severity Classification**: Categorizes vulnerabilities as Low, Medium, or High.
- 🧾 **Flask Web Interface**: Simple UI to run scans, view results, and generate reports.
- 📁 **Logs and Evidence**: Logs each finding with affected URLs, parameters, payloads, and raw response evidence.

---

## 📁 Project Structure

```

web\_vuln\_scanner/
├── app.py                  # Flask app (UI)
├── scanner/
│   ├── **init**.py
│   ├── crawler.py          # Crawls pages and extracts forms
│   ├── detector.py         # Contains XSS, SQLi, CSRF detectors
│   ├── payloads.py         # List of injection payloads
│   └── logger.py           # Logs and reports results
├── static/                 # CSS/JS for UI
├── templates/              # HTML templates (Flask)
└── requirements.txt        # Python dependencies

````

---

## 🛠️ Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/web-vuln-scanner.git
cd web-vuln-scanner

# (Optional) Create and activate a virtual environment
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

# Install dependencies
pip install -r requirements.txt

# Run the scanner UI
python app.py

# Use this URL
http://testphp.vulnweb.com/
````

---

## 🌐 How to Use

1. Launch the Flask UI (`python app.py`).
2. Enter the target URL in the form.
3. Click **Start Scan**.
4. View results in a table with details such as:

   * Vulnerability Type
   * Affected URL & Parameter
   * Payload used
   * Severity
5. Download logs or evidence if needed.

---

## Web application

![Screenshot 2025-06-12 133710](https://github.com/user-attachments/assets/9f477a48-c59d-4eb6-a0be-55bf28c38abe)


## 🧪 Sample Output

```json
{
  "url": "http://example.com/login",
  "vulnerabilities": [
    {
      "type": "SQL Injection",
      "parameter": "username",
      "payload": "' OR '1'='1",
      "evidence": "You have an error in your SQL syntax;",
      "severity": "High"
    },
    {
      "type": "XSS",
      "parameter": "search",
      "payload": "<script>alert(1)</script>",
      "evidence": "<script>alert(1)</script>",
      "severity": "Medium"
    }
  ]
}
```

---

## 📌 Roadmap

* [x] XSS, SQLi, and CSRF detection
* [x] Web crawler with form discovery
* [x] Flask-based UI
* [x] Logging and report generation
* [ ] PDF report export
* [ ] Login page and cookie/session support
* [ ] Add support for Command Injection, File Upload flaws, etc.
* [ ] Multithreading for faster scans

---

## 📚 References

* [OWASP Top 10](https://owasp.org/www-project-top-ten/)
* [BeautifulSoup Documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
* [Flask Documentation](https://flask.palletsprojects.com/)

---

## 🛡️ Disclaimer

This tool is intended for **educational and ethical testing purposes only**. Do **not** use it on websites you do not own or have explicit permission to test.
