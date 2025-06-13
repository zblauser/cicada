import subprocess
import os
from pathlib import Path

def run_ffuf(target, wordlist=None):
	print(f"[+] Running FFUF against {target}")

	if "FUZZ" not in target:
		if target.endswith("/"):
			target += "FUZZ"
		else:
			target += "/FUZZ"

	if not wordlist:
		possible_paths = [
			"~/SecLists/Discovery/Web-Content/common.txt",
			"~/Library/Mobile Documents/com~apple~CloudDocs/Code/recon/marriott/SecLists/Discovery/Web-Content/common.txt",
			"/usr/share/wordlists/dirb/common.txt"
		]
		for path in possible_paths:
			expanded = os.path.expanduser(path)
			if os.path.isfile(expanded):
				wordlist = expanded
				print(f"[+] Auto-selected wordlist: {wordlist}")
				break
		else:
			return "[!] No valid wordlist found. Please use --wordlist."

	cmd = [
		"ffuf",
		"-u", target,
		"-w", wordlist,
		"-mc", "200,301,302,403,500",
		"-c",
		"-v",
		"-t", "25"
	]

	try:
		result = subprocess.run(cmd, capture_output=True, text=True)

		output = result.stdout.strip()		

		if not output:
			return "[!] FFUF ran but produced no output."


		return output

	except Exception as e:
		return f"Error running FFUF: {e}"
