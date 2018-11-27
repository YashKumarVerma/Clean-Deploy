from path import Path
from itertools import chain

d = Path('.');
config = d.walkfiles(".*");
md 		= d.walkfiles("*.md");
license = d.walkfiles("*.license");

files = chain(md, config, license);

for file in files:
	print("Deleting :" + file);
	file.remove()

print("Process Ended.");