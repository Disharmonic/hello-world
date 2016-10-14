Python 3.5.2 (v3.5.2:4def2a2901a5, Jun 26 2016, 10:47:25) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> WARNING: The version of Tcl/Tk (8.5.9) in use may be unstable.
Visit http://www.python.org/download/mac/tcltk/ for current information.

>>> movies = [
	"The Holy Grail", 1975, "Terry Jones & Terry Gilliam", 91,
		["Graham Chapman",
			["Michael Palin", "John Cleese", "Terry Gilliam", "Eric Idle", "Terry Jones"]]]
>>> def print_lol(the_list):
	"""This is the "nester.py" module, and it provides one function called print_lol() which prints lists that may or may not include nested lists."""
	for each_item in the_list:
		if isinstance(each_item, list):
			print_lol(each_item)
		else:
			print(each_item)

			
>>> 
