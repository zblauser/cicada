from urllib.parse import urlparse
import os
import datetime
import re

def banner(mode="[custom]"):                                                                                                         
    logo = fr"""                                                                                                        
                                                                                                                      
   )\.-.  .'(     )\.-.     /`-.      )\.-.     /`-.                                                                  
 ,' ,-,_) \  )  ,' ,-,_)  ,' _  \   ,'     )  ,' _  \                                                                 
(  .   _  ) (  (  .   _  (  '-' (  (  .-, (  (  '-' (                                                                 
 ) '..' ) \  )  ) '..' )  )   _  )  ) '._\ )  )   _  )                                                                
(  ,   (   ) \ (  ,   (  (  ,' ) \ (  ,   (  (  ,' ) \                                                                
 )/'._.'    )/  )/'._.'   )/    )/  )/ ._.'   )/    )/                                                                
                                                                                                                      
Cicada | {mode}                                                                                                      
"""                                                                                                                   
    print(logo) 

def remove_ansi(text):
	ansi_escape = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')
	return ansi_escape.sub('', text)

def log_output(target_url, tool_name, data):
	parsed = urlparse(target_url)
	domain = parsed.netloc or parsed.path
	domain = domain.split(":")[0] 
	clean_name = domain.split(".")[0]

	filename = f"{clean_name}.log"

	with open(filename, "a") as f:
		timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
		f.write(f"\n=== {tool_name.upper()} === {timestamp} ===\n")
		f.write(remove_ansi(data))
		f.write("\n")

	print(f"[+] Output saved to {filename}")
