# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

l=open('C:/Users/Chaitali/Desktop/learning/NLP_PROJECT.txt')
l=open('C:/Users/Chaitali/Desktop/learning/hotel_review_bad.txt')
counter_amazing=0
counter_thanks=0
counter_great=0
counter_excellent=0
counter_Outstanding=0

counter_Worst=0
counter_smelly=0
counter_uncomfortable=0
counter_dirty=0
counter_rude=0
for line in(l):
    k=line.split()
    amazing_cnt=k.count('amazing')
    counter_amazing=counter_amazing+amazing_cnt
    thanks_cnt=k.count('thanks')
    counter_thanks=counter_thanks+thanks_cnt
    great_cnt=k.count('great')
    counter_great=counter_great+great_cnt
    excellent_cnt=k.count('excellent')
    counter_excellent=counter_excellent+excellent_cnt
    Outstanding_cnt=k.count('Outstanding')
    counter_Outstanding=counter_Outstanding+Outstanding_cnt
    
    Worst_cnt=k.count('Worst')
    counter_Worst=counter_Worst+Worst_cnt
    smelly_cnt=k.count('smelly')
    counter_smelly=counter_smelly+smelly_cnt
    uncomfortable_cnt=k.count('uncomfortable')
    counter_uncomfortable=counter_uncomfortable+uncomfortable_cnt
    dirty_cnt=k.count('dirty')
    counter_dirty=counter_dirty+dirty_cnt
    rude_cnt=k.count('rude')
    counter_rude=counter_rude+rude_cnt
    
positive=counter_amazing+counter_thanks+counter_great+counter_excellent+counter_Outstanding
negative=counter_Worst+counter_smelly+counter_uncomfortable+counter_dirty+counter_rude
if positive>0 and negative==0:
    print('NICE HOTEL')
else:
    print('BAD HOTEL')
print('positive:',positive)
print('negative:',negative)