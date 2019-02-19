import math
class Cache:
    def __init__(self,mem,no_of_blocks,words_per_block):
        self.mem = mem
        self.no_of_blocks = no_of_blocks
        self.wordbits = int(math.log(words_per_block, 2))
        self.words_per_block = words_per_block
        self.cache = [[0]*words_per_block]*no_of_blocks
        self.capacityMissCount = 0
        self.compulsoryMissCount = 0
        self.conflictMissCount = 0
        self.hitCount = 0

    def isFull(self):
        for row in self.cache:
            for col in row:
                if(col ==0):
                    return False
        return True

    def load(self,address):
        blockIndex = (address >> self.wordbits) & (self.no_of_blocks - 1)
        wordIndex = address & (self.words_per_block - 1)
        addr = address / (self.no_of_blocks*self.words_per_block)
        blockAddress = (addr*(self.no_of_blocks*self.words_per_block))+ (blockIndex * self.words_per_block)
        self.cache[blockIndex] = [{addr: m[1]} for m in self.mem[blockAddress:(blockAddress+(self.words_per_block))]]

        return self.cache[blockIndex][wordIndex].get(addr)

    def get(self, address):
        blockIndex = (address >> self.wordbits) & (self.no_of_blocks - 1)
        wordIndex = address & (self.words_per_block-1)
        addr = address / (self.no_of_blocks * self.words_per_block)
        elem = self.cache[blockIndex][wordIndex]
        if( elem != 0 and elem.get(addr,None)!= None ):
            self.hitCount += 1
            return elem[addr]
        else:
            if(elem == 0):
                self.compulsoryMissCount +=1
            if(elem != 0 and self.isFull()):
                self.capacityMissCount += 1
            elif(elem != 0):
                self.conflictMissCount += 1
            elem = self.load(address)
        return elem

    def printCache(self):
        return 'Cache Capacity '+str(self.no_of_blocks)+'*'+str(self.words_per_block)+' Hit Count ' + str(self.hitCount) +\
                                                                            ' miss count = '+str(self.compulsoryMissCount+self.capacityMissCount+self.conflictMissCount)+' Compulsory Misses = '+str(self.compulsoryMissCount)+' Conflict Misses = ' + str(self.conflictMissCount)+' Capacity Misses = ' + str(self.capacityMissCount)