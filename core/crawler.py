import subprocess

def run_gobuster(target, wordlist="/usr/share/wordlists/dirb/common.txt"):
	print(f"[+] Crawling {target} using gobuster...")
	try:
		result = subprocess.run(
			["gobuster", "dir", "-u", target, "-w", wordlist],
			capture_output=True, text=True
		)
		return result.stdout
	except Exception as e:
		return f"Error: {e}"
