import re
 
p = re.compile(r'\d+')
a= p.findall('one1two2three3four4')
print len(a)
