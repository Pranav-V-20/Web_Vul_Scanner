from flask import Flask, request, render_template
from scanner.detector import scan_xss, scan_sqli
from scanner.logger import log_vulnerability

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    results = []
    if request.method == "POST":
        url = request.form.get("url")
        xss_results = scan_xss(url)
        sqli_results = scan_sqli(url)
        all_results = xss_results + sqli_results
        for vuln_type, vurl, payload in all_results:
            log_vulnerability(vuln_type, vurl, payload)
        results = all_results
    return render_template("index.html", results=results)
