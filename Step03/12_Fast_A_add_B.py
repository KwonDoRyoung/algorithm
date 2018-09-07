import sys

if __name__ == "__main__":
    T = int(sys.stdin.readline())
    for _ in xrange(T):
        n = sys.stdin.readline().split()
        print(int(n[0]) + int(n[1]))
