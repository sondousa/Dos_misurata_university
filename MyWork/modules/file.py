from pathlib import Path

def file():
	while 1:
		path=Path(input(f"Enter file name (eg:pass.txt) \n>"))
		if not path.is_file():
			print("[!] No such file.....")
			continue
		return path
