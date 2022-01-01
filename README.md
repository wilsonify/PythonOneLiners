# Python One Liners

This repository collects all Python one-liners that are of interest to the Pyhton community. One-Liners are concise snippets of source code (with or without library calls) that accomplish a given task in a concise and compressed manner. 

They are often used to call a Python script from the operating system terminal using the `python -c` command:

```python
python -c 'print("hello world")'
```
 
Here are additional resources for Python one-liners:

# Free Python One-Liners Learning Resources

* [Free ''Python One-Liners'' videos & book resources](https://pythononeliners.com/)
* [Collection of ''One-Liners'' with interactive shell](https://blog.finxter.com/10-python-one-liners/)
* [Book ''Python One-Liners''](https://www.amazon.com/gp/product/B07ZY7XMX8)
* [Interesting Quora Thread ''Python One-Liner''](https://www.quora.com/What-are-some-of-the-most-elegant-greatest-Python-one-liners)
* [Python One-Line X - How to accomplish different tasks in a single line](https://blog.finxter.com/python-one-line-x/)
* [Subreddit '''Python One-Liners'''](https://www.reddit.com/r/PythonOneLiners/)
* [Python One-Liners Wiki](https://wiki.python.org/moin/Powerful%20Python%20One-Liners)

# How to Contribute Your One-Liners

Feel free to submit your own one-liners in the `one_liners.py` Python file!

Creating your own one-liners is an excellent way to improve your understanding of the single line of Python code. After all, every complicated Python program consists just of a number of Python one-liners---chained together to a coherent whole!


# General One-Liner Commands From https://gist.github.com/craigls/2712084
'''
Some useful Python one-liners taken from http://www.reddit.com/r/Python/comments/fofan/suggestion_for_a_python_blogger_figure_out_what/

All modules listed are part of the standard library and should work with Python 2.6+

How to use:

    $ python -m [module] [arguments]

calendar - does default to displaying a yearly calendar, but it has a bunch of options (args are year or year month, options are HTML output, calendar locale, encoding, and some type-specific stuff, see python -m calendar -h)
cgi, dumps a bunch of information as HTML to stdout
CGIHTTPRequestHandler - same as SimpleHTTPServer except via the CGIHTTPRequestHandler: it will executes scripts it recognizes as CGI, instead of just sending them over (has not survived the transition to Python 3)
compileall - compiles a tree of Python files to bytecode, has a bunch of options. Does not compile to stripped files (pyo)
cProfiler - runs the provided script file (argument) under cProfiler
dis disassembles a python script
doctest - runs doctests on the provided files (which can be python scripts or doctest files)
encodings.rot_13 - rot13 encodes stdin to stdout (has not survived the transition to Python 3)
filecmp - directory entry comparison tool
fileinput - some kind of ghetto pseudo-annotate. No idea what use that thing might be of
formatter - reformats the provided file argument (or stdin) to stdout: 80c paragraphs &etc
ftplib - ghetto FTP client
gzip - ghetto gzip (or gunzip with -d), can only compress and decompress, does not delete the archive file
htmllib - strips HTML tags off of an HTML file
ifc - dumps some info about the provided aiff file (if given two paths, also copies path1 to path2)
imaplib - ghetto IMAP client
json.tool - pretty prints JSON
locale - displays current locale information
mimify - converts (mail) messages to and from MIME format
modulefinder - lists the modules imported by the provided script argument, and their location
pdb - automatically enters PDB post-mortem mode if the script crashes
platform - displays the platform string
poplib - dumps a bunch of info on a POP mailbox
profile - see cProfile
pstats - opens a statistics browser (for profile files)
pydoc - same as the pydoc command
quopri / uu  binhex / base64 - encode / decode - quoted-Printable / UUEncoded content.
shlex - displays tokenization result of the provided file argument (one token per line prefixed with Token:)
SimpleHTTPServer - serve the current directory over HTTP on port 8080
SimpleXMLRPCServer - XMLRPC server for power and addition
smtpd - SMTP proxy
telnetlib - telnet client
timeit - command line profiling interface
tokenize - dumps tokenization result of a Python file
urllib - fetches a url
webbrowser - opens provided URL in your default web browser (options: in a new window, in a new tab)
whichdb - tries to guess which db package (for db format nobody cares about) can be used to read a db file
'''