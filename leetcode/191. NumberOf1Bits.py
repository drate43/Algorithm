
def hammingWeight(self, n: int) -> int:
    bitn = 0;

    for i in range(32):
        bitn += (n&1);
        n = n >> 1;
    return bitn;




