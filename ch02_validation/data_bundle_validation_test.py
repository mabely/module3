# -*- coding: utf-8 -*-

from data_bundle_validation import *

# Test calls to program:
print ('TEST EXAMPLE 1')

result = DataBundlePurchase('1234', 34.55)
print ('-----\nRESULT:', result)
print ('-' * 50, '\n')

print ('TEST EXAMPLE 2')
result = DataBundlePurchase('2345', -22.00)
print ('-----\nRESULT:', result)
print ('-' * 50, '\n')

print ('TEST EXAMPLE 3')
result = DataBundlePurchase('3456', 17.55)
print ('-----\nRESULT:', result)
print ('-' * 50, '\n')

