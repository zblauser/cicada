import subprocess

def start_interactsh_client():
	print("[+] Starting Interactsh client...")
	try:
		result = subprocess.run(
			["./interactsh-client"], 
			capture_output=True, text=True
		)
		return result.stdout
	except Exception as e:
		return f"Error running Interactsh client: {e}"
