import math


def chunks(l, n):
    """
    Yield successive n-sized chunks from l.
    """
    for i in xrange(0, len(l), n):
        yield l[i:i+n]


def stacked_chunks(l, n):
	"""
	Yield n-stacks of chunks from l
	"""
	c = int(math.ceil(len(l) / float(n)))
	for i in xrange(c):
		yield l[i::c]
