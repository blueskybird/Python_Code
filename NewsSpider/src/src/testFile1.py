# -*- coding: utf-8 -*-
import re
import urllib

p = re.compile('\d+|”|“| |:|：|\(|\)|-|/|（|）|\\\\|%|\?|\[|\]|\#|\&|\*|\{|\}|\||\.|\w|，|＂|＂|》|《|<|=|>|!|;')

# zhurl=r'http://ent.china.com/music/nei/index_9.html'
# mypage=urllib.urlopen(zhurl).read()
#
# myItems = re.findall(r"\" target='_blank' class='title_default'>(.*?)</a>&nbsp;", mypage,re.S)
#
# for item in myItems:
#     item=re.sub(p,'',item)
#     print item

# item1="跨界赴日拍摄获重量级导演青睐<=>图<>"
item1="浙师大[被曝学]生因2.4新?建寝...室“中毒”; 校（（（）((()))方d否\d050-/认<===>dsf!!!FG"
# strr='one1two2three3four4'
# p = re.compile('\d+|”|“| |:|：|\(|\)|-|/|（|）|\\\\|\?|\[|\]|\.|\w')
item=re.sub(p,'',item1)
print item