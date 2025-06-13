import subprocess

def start_mitmproxy():
	print("[+] Starting mitmproxy on port 8080...")
	try:
		return subprocess.Popen(["mitmproxy", "-p", "8080"])
	except Exception as e:
		print(f"Error launching mitmproxy: {e}")
		return None
