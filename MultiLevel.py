import string, Cache, math
class multiLevelCache:
        def __init__(self, no_of_blocks, words_per_block, codefilepath):
            mem = []
            with open(codefilepath) as f:
                lines = f.readlines()
            for line in lines:
                token = string.split(string.lower(line))
                if token[0] != 'go':
                    mem.append((int(token[1]), int(token[0], 0)))
            self.no_of_blocks = no_of_blocks
            self.wordbits = int(math.log(words_per_block, 2))
            self.words_per_block = words_per_block
            self.cache = [[0] * words_per_block] * no_of_blocks
            self.l2Cache = Cache.Cache(mem, no_of_blocks, words_per_block)
            self.capacityMissCount = 0
            self.compulsoryMissCount = 0
            self.conflictMissCount = 0
            self.hitCount = 0

        def isFull(self):
            for row in self.cache:
                for col in row:
                    if (col == 0):
                        return False
            return True

        def load(self, address):
            blockIndex = (address >> self.wordbits) & (self.no_of_blocks - 1)
            wordIndex = address & (self.words_per_block - 1)
            addr = address / (self.no_of_blocks * self.words_per_block)
            self.cache[blockIndex][wordIndex] = { addr : self.l2Cache.get(address)}

            return self.cache[blockIndex][wordIndex].get(addr)

        def get(self, address):
            blockIndex = (address >> self.wordbits) & (self.no_of_blocks - 1)
            wordIndex = address & (self.words_per_block - 1)
            addr = address / (self.no_of_blocks * self.words_per_block)
            elem = self.cache[blockIndex][wordIndex]
            if (elem != 0 and elem.get(addr, None) != None):
                self.hitCount += 1
                return elem[addr]
            else:

                if (elem == 0):
                    self.compulsoryMissCount += 1
                if (elem != 0 and self.isFull()):
                    self.capacityMissCount += 1
                elif (elem != 0):
                    self.conflictMissCount += 1
                elem = self.load(address)
            return elem

        def printCache(self):
            return 'L1 Cache Capacity ' + str(self.no_of_blocks) + '*' + str(self.words_per_block) + ' Hit Count ' + str(
                self.hitCount) + \
                   ' miss count = ' + str(
                self.compulsoryMissCount + self.capacityMissCount + self.conflictMissCount) + ' Compulsory Misses = ' + str(
                self.compulsoryMissCount) + ' Conflict Misses = ' + str(
                self.conflictMissCount) + ' Capacity Misses = ' + str(self.capacityMissCount) + '\n L2 Cache Capacity ' + str(self.l2Cache.no_of_blocks) + '*' + str(self.l2Cache.words_per_block) + ' Hit Count ' + str(
                self.l2Cache.hitCount) + \
                   ' miss count = ' + str(
                self.l2Cache.compulsoryMissCount + self.l2Cache.capacityMissCount + self.l2Cache.conflictMissCount) + ' Compulsory Misses = ' + str(
                self.l2Cache.compulsoryMissCount) + ' Conflict Misses = ' + str(
                self.l2Cache.conflictMissCount) + ' Capacity Misses = ' + str(self.l2Cache.capacityMissCount)