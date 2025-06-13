import base64
import urllib.parse

def base64_encode(data):
	return base64.b64encode(data.encode()).decode()

def base64_decode(data):
	try:
		return base64.b64decode(data.encode()).decode()
	except Exception as e:
		return f"Error decoding base64: {e}"

def url_encode(data):
	return urllib.parse.quote(data)

def url_decode(data):
	return urllib.parse.unquote(data)
