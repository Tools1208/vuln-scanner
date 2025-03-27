import json
from jinja2 import Environment, FileSystemLoader
from datetime import datetime

class HTMLReport:
    def __init__(self, scan_results):
        self.results = scan_results
        self.template_env = Environment(
            loader=FileSystemLoader('data/templates')
        )

    def generate(self, output_path):
        template = self.template_env.get_template('report.html.j2')
        html_content = template.render(
            results=self.results,
            generated_at=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        )
        
        with open(output_path, 'w') as f:
            f.write(html_content)
        logging.info(f"Report generated: {output_path}")
