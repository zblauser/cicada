from core import utils, decoder
import re
import os

def analyze(logfile_path):
	print(f"[+] Running decode-all on: {logfile_path}")
	with open(logfile_path, "r", errors="ignore") as f:
		text = f.read()

	potential = re.findall(r"[A-Za-z0-9+/=]{10,}", text) 
	decoded_items = {}
	output_lines = []

	for item in set(potential):
		results = []

		b64 = decoder.base64_decode(item)
		if b64 != item and "Error" not in b64 and decoder.is_printable(b64):
			results.append(("base64", b64))

		hexed = decoder.hex_decode(item)
		if hexed != item and "Error" not in hexed and decoder.is_printable(hexed):
			results.append(("hex", hexed))

		url = decoder.url_decode(item)
		if url != item and decoder.is_printable(url):
			results.append(("url", url))

		if results:
			decoded_items[item] = results
			output_lines.append(f"\n[+] Encoded: {item}")
			for method, result in results:
				output_lines.append(f"    [{method}] {result}")

	if not decoded_items:
		print("[*] No encoded values found.")
	else:
		for line in output_lines:
			print(line)

		target = os.path.basename(logfile_path).split(".")[0]
		log_path = utils.log_output(target, "decode", "\n".join(output_lines))
		print(f"\n[+] Saved decoded output to: {log_path}")
