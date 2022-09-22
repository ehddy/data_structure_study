import math


kInputString = "aaaaaaaaaabbccccddddddeffffgghhhhhhhhh"
# kInputString = "For more than 20 years, Australia tried to maintain good relations with both the United States and China. It was good for trade and peaceful regional relations. But on Thursday, with the announcement of a new security deal with the United States and the United Kingdom, which will see Australia eventually field nuclear-powered submarines, Canberra made its position clear -- it has chosen Washington over Beijing. By choosing sides, some experts say Australia has unnecessarily antagonized China, the country's largest trading partner, while at the same time making itself overly reliant on the US for protection should tensions escalate in the Indo-Pacific."


class BinaryHeap:
    class Item:
        def __init__(self, priority=0, character=None, left=None, right=None):
            self.priority   = priority
            self.character  = character
            self.left       = left
            self.right      = right


    def size(self):
        return self.__heapSize


    def insert(self, item):
        self.__heapSize += 1
        self.__heap.append(item)

        self.__upHeap(self.__heapSize)


    def delete(self):
        if self.__heapSize <= 0:
            print("## Heap is EMPTY !")
            return None

        minimum = self.__heap[1]

        self.__heap[1], self.__heap[-1] = self.__heap[-1], self.__heap[1]
        del self.__heap[-1]
        self.__heapSize -= 1

        self.__downHeap(1)

        return minimum


    def print(self):
        print("#### Print binary heap ####")
        print("--------------------------------")
        for item in self.__heap:
            print(f"({item.priority}, {item.character}, {item.left}, {item.right})")
        print("--------------------------------")


    def __init__(self, frequencies):
        self.__construct(frequencies)


    def __construct(self, frequencies):
        self.__heap = [self.Item()]
        self.__heapSize = len(frequencies)

        # Convert.
        for key, value in frequencies.items():
            self.__heap.append(self.Item(value, key))

        # Construct.
        for i in range(self.__heapSize // 2, 0, -1):
            self.__downHeap(i)


    def __downHeap(self, i):
        while (2 * i) <= self.__heapSize:
            k = 2 * i
            if (k < self.__heapSize) and (self.__heap[k].priority > self.__heap[k+1].priority):
                k += 1            
            if self.__heap[i].priority < self.__heap[k].priority:
                break

            self.__heap[i], self.__heap[k] = self.__heap[k], self.__heap[i]
            i = k


    def __upHeap(self, index):
        while (index > 1) and (self.__heap[index//2].priority > self.__heap[index].priority):
            self.__heap[index], self.__heap[index//2] = self.__heap[index//2], self.__heap[index]
            index = index // 2


class HuffmanTree:
    kCodeAllocation_Left    = "0"
    kCodeAllocation_Right   = "1"


    def __init__(self, frequencies):
        self.binaryHeap = BinaryHeap(frequencies)
        self.binaryHeap.print()

        self.__construct()
        self.__allocateCode()


    def printHuffmanCode(self):
        print("#### Print huffman code ####")
        print(self.__code)


    def analyze(self, frequencies):
        totalCodeLengthOfFixedLengthCode = 0
        codeLengthPerCharacter = math.ceil(math.log2(len(frequencies)))
        for key, value in frequencies.items():
            totalCodeLengthOfFixedLengthCode += (codeLengthPerCharacter * value)

        totalCodeLengthOfHuffmanCode = 0
        for key, value in self.__code.items():
            totalCodeLengthOfHuffmanCode += (len(value) * frequencies[key])

        print("#### Compare total code length between fixed length coding and huffman coding ####")
        print(f"Fixed length code: {totalCodeLengthOfFixedLengthCode} bits")
        print(f"Huffman code: {totalCodeLengthOfHuffmanCode} bits")
        print(f"Compression ratio: {totalCodeLengthOfHuffmanCode * 100 / totalCodeLengthOfFixedLengthCode :.2f}%")


    def __construct(self):
        while self.binaryHeap.size() >= 2:
            item1 = self.binaryHeap.delete()
            item2 = self.binaryHeap.delete()

            newItem = BinaryHeap.Item(item1.priority + item2.priority, None, item1, item2)
            self.binaryHeap.insert(newItem)


    def __allocateCode(self):
        self.__code = {}

        if self.binaryHeap.size() != 1:
            print("  #### Unknown ERROR !")

        self.__traverse(self.binaryHeap.delete(), "")


    def __traverse(self, item, code):
        if item.left != None:
            self.__traverse(item.left, code + self.kCodeAllocation_Left)

        if item.character != None:
            self.__code[item.character] = code

        if item.right != None:
            self.__traverse(item.right, code + self.kCodeAllocation_Right)


def main():
    # Caculate character's frequencies.
    frequencies = calculateFrequency(kInputString)

    print("#### Input string & character's frequencies ####")
    print(f"Input string: '{kInputString}'")
    print(f"Character's frequencies: {frequencies}")
    print()

    # Construct huffman tree & Print huffman code.
    huffmanTree = HuffmanTree(frequencies)
    print()
    huffmanTree.printHuffmanCode()

    print()
    huffmanTree.analyze(frequencies)


def calculateFrequency(inputString):
    frequencies = {}

    for character in inputString:
        frequencies[character] = frequencies.get(character, 0) + 1

    return frequencies


main()
