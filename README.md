# Cicada

## Change Log
[v0.0.2]

- Decode (or encode for offense) base64, hex, and URL content found in logs using `--decodeall` arg
- Running the program will greet you with an ASCII logo and listed [Mode] `[Fast], [Normal], [Deep], [Custom], [Help]`
- Added shorthand options to some of the arguments
- Custom word lists can be used for fuzzing in ffuf using `-w PATH` or `--wordlist PATH`
- If no wordlist is selected it will automatically search typical `SecLists` paths
- Additionally, you alter the path or add your own in `cicada.py`
- Scan, decode, and fuzz logs should all be written to a single `.log` file 
```bash
=== FUFF === 2025-06-14 02:19:24 ===

[!] FFUF ran but produced no output. 	

=== NUCLEI === 2025-06-14 02:19:24 ===

[azure-domain-tenant] [http] [info] https://....																																  
=== DECODE === 2025-06-14 02:14:30 ===                                                                           

[+] Encoded: dns=... 
[base64] v..
```

## Overview
Designed to meet my personal testing needs, clean logs, and real-world utility.

- Scanning via nuclei
- Fuzzing via ffuf (automatic '/FUZZ' handling)
- Base64 & URL encode/decoding
- Log-based analysis

Perhaps this can be of some use for some of your web recon needs.

---

## Usage
### Install Dependencies
#### Mitmproxy
```bash
pip install mitmproxy
```

#### Other tools (requires Go)
```bash
go install github.com/ffuf/ffuf/v2@latest
go install github.com/projectdiscovery/nuclei/v3/cmd/nuclei@latest
go install github.com/projectdiscovery/interactsh/cmd/interactsh-client@latest
go install github.com/OJ/gobuster/v3@latest
```

#### Add Go binaries to your PATH
```bash
export PATH=$PATH:$(go env GOPATH)/bin
```

### Launch with:
```bash
python cicada.py TARGET
```

---

## Current Timeline

- Tools
	- `analyzer`				[X]
	- `collaborator`			[ ]
	- `crawler`					[ ]
	- `decoder`					[X]
	- `intruder`				[X]
	- `proxy`					[ ]
	- `scanner`					[X]

- Scan Levels
	- fast						[X]
	- normal					[X]
	- deep						[X]

- Refine Input/Output
	- tighten log				[ ]
	- accept Hacker1 scope csv	[ ]

---

## Contributing

If you share the belief that simplicity empowers creativity, feel free to contribute.

#### Contribution is welcome in the form of:
- Forking this repo
- Submiting a Pull Request
- Bug reports and feature requests

Please ensure your code follows the existing style.

---

## Thank you for your attention.
If you hit any issues, feel free to open an issue on GitHub.
Pull requests, suggestions, or even thoughtful discussions are welcome.
