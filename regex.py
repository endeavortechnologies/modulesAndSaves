from base64 import encode
import os
import re

for file in os.listdir():
	try:
		if file.lower().endswith(".dsav") or file.lower().endswith(".dsts"):
			with open(file, "r") as f_in:
				contents = f_in.readlines()
			for line in contents:
				if line.__contains__("</moduleName>"):
					old_line = line
					idx = contents.index(line)
					new_line = f"  <moduleName>{file}</moduleName>\n"
					line = line.replace(old_line, new_line)
					with open(file, "w") as f_out:
						contents[idx] = new_line
						f_out.writelines(contents)
						continue
	except UnicodeDecodeError:
		print("unicode decode error", file)
