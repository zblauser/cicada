import base64
import urllib.parse
import binascii
import html
import string

def is_printable(s, threshold=0.85):
	printables = sum(1 for c in s if c in string.printable)
	return (printables / max(len(s), 1)) >= threshold

def base64_encode(data):
	return base64.b64encode(data.encode()).decode()

def base64_decode(data):
	try:
		return base64.b64decode(data.encode()).decode('utf-8', errors='replace')
	except Exception as e:
		return f"[!] Error decoding base64: {e}"

def url_encode(data):
	return urllib.parse.quote(data)

def url_decode(data):
	try:
		return urllib.parse.unquote(data)
	except Exception as e:
		return f"[!] Error decoding URL: {e}"

def hex_encode(data):
	return data.encode().hex()

def hex_decode(data):
	try:
		return bytes.fromhex(data).decode('utf-8', errors='replace')
	except Exception as e:
		return f"[!] Error decoding hex: {e}"

def html_decode(data):
	try:
		return html.unescape(data)
	except Exception as e:
		return f"[!] Error decoding HTML: {e}"

def auto_decode(data):
	"""Attempt all supported decodings and return a list of successful results."""
	results = []

	try:
		b64 = base64_decode(data)
		if is_printable(b64):
			results.append(('base64', b64))
	except Exception:
		pass

	try:
		hexed = hex_decode(data)
		if is_printable(hexed):
			results.append(('hex', hexed))
	except Exception:
		pass

	try:
		urld = url_decode(data)
		if is_printable(urld) and urld != data:
			results.append(('url', urld))
	except Exception:
		pass

	try:
		html_d = html_decode(data)
		if is_printable(html_d) and html_d != data:
			results.append(('html', html_d))
	except Exception:
		pass

	return results
