Coding Style for Python
=======================

Foreword
--------

- This only reflects my personal tastes.  So
  just ignore them.  Even I myself doesn't follow this.
- Use python 3.


Styles stolen from PEP 8
------------------------

### Indentation

Don't use tabs.

### Maximum line length

79 characters.  

For flowing long blocks of text (docstrings or comments), limiting the
length to 72 characters is recommended.

The preferred way of wrapping long lines is by using Python's implied
line continuation inside parentheses, brackets and braces.  If necessary,
you can add an extra pair of parentheses around an expression, but
sometimes using a backslash looks better.

### Blank lines

Extra blank lines may be used (sparingly) to separate groups of related
functions.  Blank lines may be omitted between a bunch of related
one-liners.

Use blank lines in functions, sparingly, to indicate logical sections.

### Imports

Imports should usually be on separate lines, e.g.::

    import os
    import sys

but::

    form subprocess import Popen, PIPE

Imports are always put at the top of the file, just after any module
comments and docstrings, and before module globals and constants.

Imports should be grouped in the following order:

1. standard library imports
2. related third party imports
3. local application/library specific imports

You should put a blank line between each group of imports.

Put any relevant ``__all__`` specification after the imports.

### Whitespace

Avoid extraneous whitespace in the following situations:

- Immediately inside parentheses, brackets or braces.
- Immediately before a comma, semicolon, or colon:
- Immediately before the open parenthesis that starts the argument
- Immediately before the open parenthesis that starts an indexing or slicing:
- More than one space around an assignment (or other) operator to
  align it with another.
  
Other Recommendations

- Always surround these binary operators with a single space on
  either side: assignment (=), augmented assignment (+=, -= etc.),
  comparisons (==, <, >, !=, <>, <=, >=, in, not in, is, is not),
  Booleans (and, or, not).

- Use spaces around arithmetic operators 
- Don't use spaces around the '=' sign when used to indicate a
  keyword argument or a default parameter value.

### Comments and docstrings

Block comments generally apply to some (or all) code that follows them,
and are indented to the same level as that code.  Each line of a block
comment starts with a # and a single space (unless it is indented text
inside the comment).

Paragraphs inside a block comment are separated by a line containing a
single #.

An inline comment is a comment on the same line as a statement.  Inline
comments should be separated by at least two spaces from the statement.
They should start with a # and a single space.

For docstring, the """ that ends a multiline docstring should be on a 
line by itself, and preferably preceded by a blank line, e.g.::

  """Return a foobang

  Optional plotz says to frobnicate the bizbaz first.

  """

For one liner docstrings, it's okay to keep the closing """ on the same
line.

### Names

Never use the characters 'l' (lowercase letter el), 'O' (uppercase
letter oh), or 'I' (uppercase letter eye) as single character variable
names.

In some fonts, these characters are indistinguishable from the numerals
one and zero. 

Since module names are mapped to file names, and some file systems are
case insensitive and truncate long names, modules should have short, 
all-lowercase names.  Underscores can be used in the module name if it
improves readability.


Styles stolen from Google
-------------------------

[Google python style](http://google-styleguide.googlecode.com/svn/trunk/pyguide.html)

### Python Interpreter

Modules should begin with #!/usr/bin/env python<version>

Always use the most specific version you can use, e.g., /usr/bin/python2.4,
not /usr/bin/python2. This makes it easier to find dependencies when
upgrading to a different Python version and also avoids confusion and
breakage during use.

### Comments

Any function or method which is not both obvious and very short needs a
doc string. Additionally, any externally accessible function or method regardless
of length or simplicity needs a doc string. The doc string should include 
what the function does and have detailed descriptions of the input and out
put. It should not, generally, describe how it does it unless it's some
complicated algorithm. For tricky code block/inline comments within the
code are more appropriate. The doc string should give enough information to
write a call to the function without looking at a single line of the function's
code. Args should be individually documented, an explanation following after
a colon, and should use a uniform hanging indent of 2 or 4 spaces. The
doc string should specify the expected types where specific types are required.
A "Raises:" section should list all exceptions that can be raised by the
function. The doc string for generator functions should use "Yields:"
rather than "Returns:". 

Sometimes I do not describe input and output, since I use very_long_input_argument_name and doctests.

### Main

Even a file meant to be used as a script should be importable and a mere
import should not have the side effect of executing the script's main
functionality. The main functionality should be in a main() function.

In Python, pychecker, pydoc, and unit tests require modules to be importable.
Your code should always check if __name__ == '__main__' before executing
your main program so that the main program is not executed when the module
is imported. 



Styles stolen from Scheme-style
---------------------------------

[Scheme Style](http://community.schemewiki.org/?scheme-style)

### Indent subexpressions equally

My note: that in Python, it usually looks bad to write something like the following Scheme::

    (list (foo) 
          (bar) 
          (baz)) 

But in Python::
    
    list = lambda : [foo,
                     bar,
                     baz,]

This is very hard to type.

If you only use 2 spaces to indent (and want to save typing), you get::

  list = lambda : [foo,
    bar,
    baz,]

This looks ugly.  Thus we prefer to break the line::

  list = lambda : [
    foo,
    bar,
    baz,
  ]

### Break for one - break for all

If you subexpressions onto multiple lines, put every subexpression on a single line. 

Personal
--------

### Indentation

Use 2 spaces to indent.  (This goes against PEP 8, though Ruby and Lua defaults to 2 spaces.)

### Immutability


Try to use variables as constants when possible. Consider importing [const.py][].
[const.py]: https://gitcafe.com/weakish/whci/blob/master/const.py

Prefer tuple over list and dictionaries:

For example, use `namedtuple('Dict', 'x y')(1, 2)` for `{'x': 1, 'y': 2}`.


### Variables

* Don't use CamlCase as compound_variable names.  CamlCase is somewhat less
  readable, especially when the name includes acronyms or initialisms, e.g.
  `getACCVSURL` v.s. `get_a_C_CVS_URL`.  And you shouldn't need CamlCase to
  shorten line length.  Also, `aVeryLongCmalCaseVariableName` is not_readable_at_all.
* Avoid global variables.

### Functions

* Use pure functions when possible.
* Prefer small functions.
* Try to make functions look pure from outside when it's not pure inside.
* Isolate side-effects.

### Branching and looping

* Prefer generator expression/map/reduce/filter/recursion
  over for loop.
* Prefer if/else ternary expression. 

### Modules

* Use '_' prefixed names instead of ``__all__`` list.  This is simple and
  straight up, and doesn't require the additional effort to maintain an
  extra list. 
* Avoid use from import when possible.

### Tests

Most of the time I just use doctest,
since it's easy to maintain coherent code, test and documentation.


### Classes

Be classless.
Well, this is not possible.
But at least avoid writing `class`.
We already have closures to conveniently implemented higher-order functions, and modules.