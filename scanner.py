import requests
import json
from modules import owasp, ssl_tls, cve_check, dirbuster, nuclei_scan
from config import Config
from modules.utils import validate_url

class VulnerabilityScanner:
    def __init__(self, target, config: Config, proxy=None, api_key=None, verbose=False):
        self.target = validate_url(target)
        self.config = config
        self.proxy = proxy
        self.api_key = api_key
        self.verbose = verbose
        self.results = {
            'target': target,
            'owasp': {},
            'ssl_tls': {},
            'cve': [],
            'directories': [],
            'nuclei': []
        }

    def run_full_scan(self):
        """تنفيذ جميع عمليات المسح"""
        try:
            self._run_owasp_scan()
            self._run_ssl_tls_scan()
            self._run_cve_scan()
            self._run_dirbuster()
            self._run_nuclei_scan()
            return self.results
        except Exception as e:
            logging.error(f"Scan failed: {str(e)}")
            raise

    def _run_owasp_scan(self):
        """فحص OWASP Top 10"""
        logging.info("Starting OWASP Top 10 scan...")
        scanner = owasp.OWASPSecurityScanner(self.target, self.proxy, self.verbose)
        self.results['owasp'] = scanner.scan()

    def _run_ssl_tls_scan(self):
        """فحص SSL/TLS"""
        logging.info("Checking SSL/TLS configuration...")
        scanner = ssl_tls.SSLScanner(self.target)
        self.results['ssl_tls'] = scanner.scan()

    def _run_cve_scan(self):
        """فحص الثغرات المعروفة"""
        if not self.api_key:
            logging.warning("Skipping CVE scan: No API key provided")
            return
        logging.info("Checking for known vulnerabilities (CVE)...")
        scanner = cve_check.CVEScanner(self.target, self.api_key)
        self.results['cve'] = scanner.scan()

    def _run_dirbuster(self):
        """مسح الدليل"""
        logging.info("Starting directory brute-forcing...")
        scanner = dirbuster.DirectoryBruter(
            self.target,
            self.config['wordlist_path'],
            self.proxy,
            self.config['max_threads']
        )
        self.results['directories'] = scanner.scan()

    def _run_nuclei_scan(self):
        """فحص باستخدام Nuclei"""
        logging.info("Running Nuclei scan...")
        scanner = nuclei_scan.NucleiScanner(
            self.target,
            self.config['nuclei_templates_path']
        )
        self.results['nuclei'] = scanner.scan()
