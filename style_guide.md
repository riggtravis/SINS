# How to write code for this project
All of the code in this project follows the conventions laid out by the Python,
HTML, and Mako style guides for the most part. Please refer to those guides
whenever you are in doubt about how to format your code. However, there are a
few things that the developers of this project expect you do in order to
maintain consistency with our slightly lazy way of doing things.

# 1. Python
The only difference between how we write python code and how everyone else
writes python code is that we use tabs instead of spaces. We know that the
python community prefers spaces. We also know that the python style guide calls
for spaces. But we prefer pressing tab once or twice to mashing the space bar
into submission.

# 2. Mako
Most of what's written in Mako is written like HTML. This is because Mako is a
templating tool. It is fancy HTML that does things dynamically. So whenever you
are working on a Mako file, for the most part write like you are writing HTML.

## Special HTML expectations
Everything that is inside a tag block is indented. That includes the <html>
tags, the <head> tags, and the <body> tags. Mostly people don't indent inside of
these tags, but we do.

If the next tag after a tag block is at the same level as the tag block, put an
empty line between them. So please don't do this:

		<div>
			stuff
		</div>
		<div>
			more stuff
		</div>
		
But instead do this:

		<div>
			stuff
		</div>
		
		<div>
			more stuff
		</div>

## Special Mako logic expectations
Make sure that code is indented clearly inside of logical blocks. This is hard
to read:

		% if something:
			do.something()
		% endif
		
This is much easier to read:

		% if something:
				do.something()
		% endif