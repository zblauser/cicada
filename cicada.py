import argparse
from urllib.parse import urlparse
from core import scanner, intruder, decoder, analyzer, utils

def extract_log_basename(url):
	parsed = urlparse(url)
	domain = parsed.netloc or parsed.path
	domain = domain.split(":")[0]
	return domain.split(".")[0]

def r_scanner(target):
	output = scanner.run_nuclei(target)
	print(output)
	utils.log_output(target, "nuclei", output)

def r_fuzzer(target, wordlist):
	output = intruder.run_ffuf(target, wordlist)
	print(output)
	utils.log_output(target, "fuff", output)

def r_decoders(args):	
	if args.b64encode:
		print(decoder.base64_encode(args.b64encode))
	if args.b64decode:
		print(decoder.base64_decode(args.b64decode))
	if args.urlencode:
		print(decoder.url_encode(args.urlencode))
	if args.urldecode:
		print(decoder.url_decode(args.urldecode))

def r_logdecoders(args):
	if args.decodeall:
		logfile = args.decodeall if isinstance(args.decodeall, str) else None
		if not logfile and args.target:
			logfile = f"{extract_log_basename(args.target)}.log"
		if logfile:
			analyzer.decode_all_from_log(logfile)
		else:
			print("[-] Please provide a log file with --decodeall or use it with a target.")

def parse_args():
	banner = """
 
   )\.-.  .'(     )\.-.     /`-.      )\.-.     /`-.  
 ,' ,-,_) \  )  ,' ,-,_)  ,' _  \   ,'     )  ,' _  \ 
(  .   _  ) (  (  .   _  (  '-' (  (  .-, (  (  '-' ( 
 ) '..' ) \  )  ) '..' )  )   _  )  ) '._\ )  )   _  )  
(  ,   (   ) \ (  ,   (  (  ,' ) \ (  ,   (  (  ,' ) \ 
 )/'._.'    )/  )/'._.'   )/    )/  )/ ._.'   )/    )/ 
"""
	parser = argparse.ArgumentParser(
		description = banner,	
		usage=argparse.SUPPRESS,
		formatter_class=argparse.RawDescriptionHelpFormatter
)

	parser.add_argument("target", help="Target URL/IP", nargs="?")
	parser.add_argument("-s", "--scan", action="store_true", help="Run vulnerability scanner")
	parser.add_argument("-z", "--fuzz", action="store_true", help="Run FFUF fuzzing")
	parser.add_argument("-w", "--wordlist", help="Path to wordlist file (e.g., SecLists/.../common.txt)")
	parser.add_argument("-b", "--b64encode", help="Base64 encode string")
	parser.add_argument("-x", "--b64decode", help="Base64 decode string")
	parser.add_argument("-e", "--urlencode", help="URL encode string")
	parser.add_argument("-u", "--urldecode", help="URL decode string")
	parser.add_argument("-a", "--decodeall", nargs="?", const=True, help="Decode encoded content from log (optional: provide filename)")
	
	parser.add_argument("-d", "--deep", action="store_true", help="Deep mode (all tools)")	
	parser.add_argument("-n", "--normal", action="store_true", help="Normal mode (default subset without arguments)")
	parser.add_argument("-f", "--fast", action="store_true", help="Fast mode (quick scan)")

	return parser.parse_args()

def main():
	args = parse_args()

	r_decoders(args)
	r_logdecoders(args)

	selected = []

	if args.deep:
		selected = ['scanner', 'fuzzer', 'analyze', 'decode']
	elif args.fast:
		selected = ['scanner', 'fuzzer']
	elif args.normal or not any ([args.scan, args.fuzz, args.deep, args.fast]):
		selected = ['scanner', 'fuzzer', 'decode']
	else:
		if args.scan:
			selected.append('scanner')
		if args.fuzz:
			selected.append('fuzzer')

	if args.target and selected:
		print(f"[*] Running tools: {', '.join(selected)}")

		if 'scanner' in selected:
			r_scanner(args.target)
		if 'fuzzer' in selected:
			r_fuzzer(args.target, args.wordlist)
		if 'analyze' in selected:
			log = f"{extract_log_basename(args.target)}.log"
			analyzer.analyze(log)
		if 'decode' in selected:
			log = f"{extract_log_basename(args.target)}.log"
			analyzer.decode_all_from_log(log)

	elif not args.target and any(tool in selected for tool in ['scanner', 'fuzzer']):
		print("[-] Target is required for scan/fuzz modes.")

if __name__ == "__main__":
	main()
