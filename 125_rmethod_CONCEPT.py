O1 * O2

type(O1).__mul__(O1, O2)

Lets assume that type(O1) does not implement __mul__

Then Python checks the possibility of computing O2 * O1

But for that to succeed

type(O2) = class of object O2 MUST CONTAIN A METHOD NAMED
__rmul__

and it should accept O1 for second parameter

type(O2).__rmul__(O2, O1)

