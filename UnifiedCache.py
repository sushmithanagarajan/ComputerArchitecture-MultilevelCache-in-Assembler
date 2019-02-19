import Cache
import string
class UnifiedCache:
    def __init__(self,no_of_blocks,words_per_block,codefilepath):
        mem = []
        with open(codefilepath) as f:
            lines = f.readlines()
        for line in lines:
            token = string.split(string.lower(line))
            if token[0] !='go':
                mem.append((int(token[1]), int(token[0],0)))
        self.Cache = Cache.Cache(mem,no_of_blocks,words_per_block)