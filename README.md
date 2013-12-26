PyTemplate
==========

A basic command line interface to Python's built-in string templating
designed to be used for generating static files.

This is a one-pass template system. If you have defined keywords
`'name': '{othername}'` and `'othername': 'Pat'`, then the template
`'My name is {name}'` will evaluate to `'My name is {othername}'`, not
`'My name is Pat'`.

Usage
-----

`pytemplate infile [template ...] [-o --output outfile]`

This command will fill in all template arguments in `infile`, writing
to `outfile` if specified and stdout otherwise. `file` is interpreted
as the contents of a Python string, and so can contain string
formatting directives using curly-brace syntax. All such directives
should be keyword directives, such as `My name is {name}`; see <a
href="http://www.python.org/dev/peps/pep-3101/">here</a> for details.

Since `infile` is treated as plain text, we need a way to specify the
formatting arguments. We do this with the template arguments, which
can either be Python modules (with a .py suffix) or any other file. If
a Python module is passed in as an argument, we load in all top-level
declarations from the module as keyword formatting arguments (use the
`__all__` module declaration to control unwanted exports). If any
other file is specified, we treat the contents of the file as plain
text and associate that text with the root of the file name as a
keyword argument.

Example
-------

`infile.txt`:

    This is a sample input file. We can load in keyword arguments such
    as '{foo}' or '{bar:.4f}' using a Python module. It is sometimes
    more convenient to load larger blocks of text such as
	
	{long}
	
	by a file such as `long.txt`.
	
`pyfile.py`:

    __all__ = ['foo', 'bar'] # We only export 'foo' and 'bar'
	
	from math import pi
	
	def foo_helper():
	    return 'some text'
		
	foo = foo_helper()
	
	bar = 2 * pi
	
`long.txt`

    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec
    gravida sapien nec quam sollicitudin luctus. Praesent feugiat,
    justo sed egestas condimentum, neque purus feugiat ante, et mattis
    nulla est nec tortor.
	
Running `pytemplate infile.txt long.txt pyfile.py` would write

    This is a sample input file. We can load in keyword arguments such
    as 'some text' or '6.2832' using a Python module. It is sometimes 
	more convenient to load larger blocks of text such as
	
    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec
    gravida sapien nec quam sollicitudin luctus. Praesent feugiat,
    justo sed egestas condimentum, neque purus feugiat ante, et mattis
    nulla est nec tortor.
	
	by a file such as `long.txt`.
