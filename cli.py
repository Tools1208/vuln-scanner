import argparse
import json
import logging
from scanner import VulnerabilityScanner
from reports.html_report import HTMLReport
from reports.pdf_report import PDFReport
from config import Config

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[logging.StreamHandler()]
)

def main():
    parser = argparse.ArgumentParser(description="Advanced Vulnerability Scanner")
    parser.add_argument('-t', '--target', required=True, help="Target URL")
    parser.add_argument('-c', '--config', default='config.json', help="Config file path")
    parser.add_argument('-o', '--output', choices=['html', 'pdf'], default='html', help="Report format")
    parser.add_argument('--proxy', help="Proxy URL (e.g., http://127.0.0.1:8080)")
    parser.add_argument('--nuclei-templates', help="Custom Nuclei templates path")
    parser.add_argument('--api-key', help="NVD API Key for CVE checks")
    parser.add_argument('--verbose', action='store_true', help="Enable verbose output")

    args = parser.parse_args()

    # تحميل التهيئة
    config = Config(args.config)
    config.load()

    # إعداد المسح
    scanner = VulnerabilityScanner(
        target=args.target,
        config=config,
        proxy=args.proxy,
        api_key=args.api_key,
        verbose=args.verbose
    )

    # تنفيذ المسح
    results = scanner.run_full_scan()

    # توليد التقرير
    if args.output == 'html':
        HTMLReport(results).generate('scan_report.html')
    else:
        PDFReport(results).generate('scan_report.pdf')

if __name__ == "__main__":
    main()
