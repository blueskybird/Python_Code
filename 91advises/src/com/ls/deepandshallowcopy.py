#-*- coding: utf-8 -*-
#思路一：利用切片操作和工厂方法list方法拷贝就叫浅拷贝，只是拷贝了最外围的对象本身，内部的元素都只是拷贝了一个引用而已。
#
#思路二：利用copy中的deepcopy方法进行拷贝就叫做深拷贝，外围和内部元素都进行了拷贝对象本身，而不是引用。
import copy

jack = ['jack', ['age', 20]]

#浅拷贝
#tom = jack[:]
#anny = list(jack)

#深拷贝
tom = copy.deepcopy(jack)
anny = copy.deepcopy(jack)

tom[0] = 'tom'
tom[1][0] = 'nianling'
anny[0] = 'anny'
anny[1][0] = 'suishu'
anny[1][1] = 18

print jack, tom, anny