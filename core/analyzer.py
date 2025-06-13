from core import decoder
import re

def analyze(logfile_path):
	print(f"[+] Running decode-all on: {logfile_path}")
	with open(logfile_path, "r") as f:
		text = f.read()

	# Look for encoded-looking values (base64, url-encoded strings)
	potential = re.findall(r"[A-Za-z0-9+/=]{10,}", text)  # base64-ish
	decoded_items = {}

	for item in set(potential):
		results = []
		b64 = decoder.base64_decode(item)
		if b64 != item and "Error" not in b64:
			results.append(("base64", b64))

		hexed = decoder.hex_decode(item)
		if hexed != item and "Error" not in hexed:
			results.append(("hex", hexed))

		url = decoder.url_decode(item)
		if url != item:
			results.append(("url", url))

		if results:
			decoded_items[item] = results

	if not decoded_items:
		print("[*] No encoded values found.")
	else:
		for raw, decodings in decoded_items.items():
			print(f"\n[+] Encoded: {raw}")
			for method, result in decodings:
				print(f"    [{method}] {result}")
