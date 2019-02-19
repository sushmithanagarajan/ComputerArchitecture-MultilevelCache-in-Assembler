import Cache
import string
import os
import time
import sys
class SplitCache:
#define the init class with variables
        def __init__(self, blockno, wordsinblock, fileloc):
            mem = []
            with open(fileloc) as f:
                lines = f.readlines()
            for line in lines:
                token = string.split(string.lower(line))
                if token[0] != 'go':
                    mem.append((int(token[1]), int(token[0], 0)))
            self.codeCache = Cache.Cache(mem, blockno, wordsinblock)
            self.dataCache = Cache.Cache(mem, blockno, wordsinblock)
			
			