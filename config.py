import json
from pathlib import Path

class Config:
    DEFAULTS = {
        'timeout': 10,
        'max_threads': 20,
        'wordlist_path': 'data/wordlists/directories.txt',
        'nuclei_templates_path': 'data/nuclei_templates/',
        'user_agent': 'VulnScanner/1.0',
        'verify_ssl': True,
        'max_retries': 3
    }

    def __init__(self, config_path):
        self.config_path = Path(config_path)
        self.settings = self.DEFAULTS.copy()

    def load(self):
        if self.config_path.exists():
            with open(self.config_path, 'r') as f:
                user_config = json.load(f)
                self.settings.update(user_config)
        else:
            logging.warning("Config file not found, using defaults")

    def __getitem__(self, key):
        return self.settings.get(key, None)

    def __setitem__(self, key, value):
        self.settings[key] = value
