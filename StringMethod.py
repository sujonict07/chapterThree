print 'This is a test'.replace('is','eez')
print '1+2+3+4+5+6+7'.split('+')
print '   Internal whitespace is kept     '.strip()
from string import maketrans
table = maketrans('cs','kz')
print len(table)
print 'this is anc incredible test'.translate(table)