import subprocess

def run_nuclei(target, template_path=None):
	print(f"[+] Scanning {target} with Nuclei...")
	try:
		cmd = ["nuclei", "-u", target]
		if template_path:
			cmd += ["-t", template_path]
		result = subprocess.run(cmd, capture_output=True, text=True)
		return result.stdout
	except FileNotFoundError:
		return "[!] Nuclei not found. Is it installed and in your PATH?"
	except Exception as e:
		return f"Error: {e}"
