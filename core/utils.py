from urllib.parse import urlparse
import os
import datetime
import re

def remove_ansi(text):
	ansi_escape = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')
	return ansi_escape.sub('', text)

def log_output(target_url, tool_name, data):
	# Extract clean domain (e.g., "example" from "https://example.com")
	parsed = urlparse(target_url)
	domain = parsed.netloc or parsed.path
	domain = domain.split(":")[0]  # remove port if any
	clean_name = domain.split(".")[0]  # take only 'example' from 'example.com'

	filename = f"{clean_name}.log"

	# Write or append to file
	with open(filename, "a") as f:
		timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
		f.write(f"\n=== {tool_name.upper()} === {timestamp} ===\n")
		f.write(remove_ansi(data))
		f.write("\n")

	print(f"[+] Output saved to {filename}")
