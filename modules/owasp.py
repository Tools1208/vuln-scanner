import requests
from modules.utils import check_sql_injection, check_xss, check_security_headers

class OWASPSecurityScanner:
    def __init__(self, target, proxy=None, verbose=False):
        self.target = target
        self.proxy = proxy
        self.verbose = verbose

    def scan(self):
        return {
            'injection': self.check_injection(),
            'broken_auth': self.check_broken_authentication(),
            'sensitive_data': self.check_sensitive_data_exposure(),
            'xxe': self.check_xxe(),
            'access_control': self.check_broken_access_control(),
            'security_misconfig': self.check_security_misconfiguration(),
            'xss': self.check_xss(),
            'insecure_deserialization': self.check_insecure_deserialization(),
            'components': self.check_vulnerable_components(),
            'logging': self.check_insufficient_logging()
        }

    def check_injection(self):
        # فحص SQL Injection و Command Injection
        return check_sql_injection(self.target, self.proxy)

    def check_xss(self):
        return check_xss(self.target, self.proxy)

    def check_security_misconfiguration(self):
        return check_security_headers(self.target, self.proxy)

    # إضافة باقي طرق الفحص...
