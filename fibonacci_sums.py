class AlicesBirthday:

    def generate_fibs(self, k):
        fibs = [1, 1]
        n = 2
        while n < k:
            fibs.append(fibs[n - 2] + fibs[n - 1])
            n += 1
        return fibs

    def partition(self, k):
        if k % 3 == 1:
            return [-1]
        if k % 3 == 0:
            fibonaccis = self.generate_fibs(k)
            return (x for index, x in enumerate(fibonaccis) if index % 3 == 2)
        if k % 3 == 2:
            fibonaccis = self.generate_fibs(k)
            return (x for index, x in enumerate(fibonaccis) if index % 3 == 1)


alice = AlicesBirthday()
for x in alice.partition(3):
    print(x)
