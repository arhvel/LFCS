# -*- coding: utf-8 -*-
"""
Created on Wed Aug 25 16:56:58 2021

@author: adeyem01
"""

import pandas as pd
import operator, string
from itertools import groupby

class LFCS1P:
    
    def __init__(self, name):
        self.name = name
        self.data = None
        self.sequenceDB = None
   
    def Data(self,path):
        self.data = pd.read_csv(path, encoding = "ISO-8859-1")
        self.sequenceDB= self.data.iloc[0:,1].tolist()
        self.sdblength = len(self.sequenceDB)
		
    def get_SDBAvglength(self):
        return self.sdbavglength

    def get_SDBLength(self):
        return self.summation
        
    def get_SDBmaxLength(self):
        return self.sdbmaxlength
    
    def get_SDB(self):
        return self.sequenceDB
    
    def get_SDBsize(self):
        return self.sdblength
      
    
    def lfcs(self, maxpatternlength):
        self.userlen = maxpatternlength     
        
        self.minedpool = []       
        
        for i in range(len(self.sequenceDB)):
            self.subpattern = self.sequenceDB[i][i:self.userlen+i]
            self.subIdx = (self.subpattern,i+1)
            self.minedpool.append(self.subIdx)
        
        self.appearance = []
        self.pool = sorted(self.minedpool, key=operator.itemgetter(0))
        for pattern, indexes in groupby(self.pool, operator.itemgetter(0)):
            subb = (pattern, [item[1:] for item in indexes])
            _support = (len(subb[1]))
            collate = (subb,_support)
			
            self.appearance.append(collate)  
        
        self.appear = [(x,y,z) for (x,y),z in self.appearance]

        
        #remove duplicates to find relative and absolute support
        self.minedsequences = list(set(self.minedpool))

        self.frequent = []

        self.minedsequences = sorted(self.minedsequences, key=operator.itemgetter(0))
        for pattern, indexes in groupby(self.minedsequences, operator.itemgetter(0)):
            subb = (pattern, [item[1:] for item in indexes])
            _support = (len(subb[1]))
            percent = (_support/self.sdblength)*100
            collate = (subb,_support,percent)
			
            self.frequent.append(collate)      
        

        self.resList = [(w,x,y,z) for (w,x),y,z in self.frequent]

        
        return self.resList, self.appear

    def i_lfcs(self, maxpatternlength, startpos):
        self.userlen = maxpatternlength     
        
        self.minedpool = []       
        
        for i in range(len(self.sequenceDB)):
            self.subpattern = self.sequenceDB[i][self.start+i : self.userlen+self.start+i]
            self.subIdx = (self.subpattern,i+1)
            self.minedpool.append(self.subIdx)
        
        self.appearance = []
        self.pool = sorted(self.minedpool, key=operator.itemgetter(0))
        for pattern, indexes in groupby(self.pool, operator.itemgetter(0)):
            subb = (pattern, [item[1:] for item in indexes])
            _support = (len(subb[1]))
            collate = (subb,_support)
			
            self.appearance.append(collate)  
        
        self.appear = [(x,y,z) for (x,y),z in self.appearance]

        
        #remove duplicates to find relative and absolute support
        self.minedsequences = list(set(self.minedpool))

        self.frequent = []

        self.minedsequences = sorted(self.minedsequences, key=operator.itemgetter(0))
        for pattern, indexes in groupby(self.minedsequences, operator.itemgetter(0)):
            subb = (pattern, [item[1:] for item in indexes])
            _support = (len(subb[1]))
            percent = (_support/self.sdblength)*100
            collate = (subb,_support,percent)
			
            self.frequent.append(collate)      
        

        self.resList = [(w,x,y,z) for (w,x),y,z in self.frequent]

        
        return self.resList, self.appear

    
    
    
