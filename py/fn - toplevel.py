# https://docs.python.org/3/library/functions.html
abs(x)
all(iterable)
	all([1,1,1]) # True
	all([1,1,0]) # False
any(iterable)
	any([0,0,1]) # True
	any([0,0,0]) # False
ascii(object)
bin(x)
bool(?x)
breakpoint(*args, **kws)
bytearray(?source, ?encoding, ?errors)
bytes(?source, ?encoding, ?errors)
callable(object)
chr(i)
@classmethod()
compile(source, filename, mode, flags=0, dont_inherit=False, optimize=-1)
complex(?real, ?imag)
delattr(object, name)
dict(**kwarg) | dict(mapping|iterable, **kwarg)
dir(?object)
divmod(a, b)
enumerate(iterable, start=0)
eval(expression, ?globals, ?locals)
exec(object, ?globals, ?locals)
filter(function, iterable)
float(?x)
format(value, ?format_spec)
frozenset(iterable)
getattr(object, name, ?default)
globals()
hasattr(object, name)
hash(object)
help(object)
hex(x)
id(object) # "identity" of object
input(?prompt)
int(?x, ?base=10)
isinstance(object, classinfo)
issubclass(object, classinfo)
iter(object[, sentinel)
len(s)
list(iterable)
locals()
map(function, iterable, ...)
max(iterable, *, ?key, ?default) | max(arg1, arg2, *args, ?key)
memoryview(object)
min(iterable, *, ?key, ?default) | min(arg1, arg2, *args, ?key)
next(iterator, ?default)
object()
oct(x)
open(file, mode='r|w|x|a|b|t|+', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)
	mode=
		'r' # open for reading (default)
		'w' # open for writing, truncating the file first
		'x' # open for exclusive creation, failing if the file already exists
		'a' # open for writing, appending to the end of the file if it exists
		'b' # binary mode
		't' # text mode (default)
		'+' # open for updating (reading and writing)
	encoding= locale.getpreferredencoding(False) # default encoding (platform-dependent): 'cp1252'
		'utf8'|'utf-8'|'u8'|'utf'|'U8'|'UTF'|'utf8_ucs2'|'utf8_ucs4' # all same
		# https://docs.python.org/3.9/library/codecs.html#standard-encodings
ord(c)
pow(base, exp, ?mod)
print(*objects, sep=' ', end='\n', file=<sys.stdout>, flush=False)
property(fget=None, fset=None, fdel=None, doc=None)
range(stop=0) | range(start=0, stop=0, ?step=1)
repr(object)
reversed(seq)
round(number, ?ndigits)
set(?iterable)
setattr(object, name, value)
slice(stop) | slice(start, stop, ?step)
sorted(iterable, *, key=None, reverse=False)
@staticmethod()
str(object='') | str(object=b'', encoding='utf-8', errors='strict')
sum(iterable, /, start=0)
super(?type, ?object_or_type])
tuple(?iterable)
type(?iterable|object) | type(name, bases, dict, **kwds)
vars(?object)
zip(*iterables)
__import__(name, globals=None, locals=None, fromlist=(), level=0))