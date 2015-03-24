from string import Template
s = Template('$x,glorius $x!')
print s.substitute(x='slurm')
ss = Template('A $thing must never $action')
d = {}
d['thing'] = 'gentleman'
d['action'] = 'show his socks'
print ss.substitute(d)