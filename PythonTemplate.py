# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 20:59:46 2024

@author: kimam
"""

import sys, re
from math import ceil, floor, sqrt, pi, factorial, gcd,sin,cos,tan,asin,acos,atan2,exp,log,log10
import math
from copy import deepcopy
from collections import Counter, deque,defaultdict as dd
from heapq import heapify, heappop, heappush
from itertools import accumulate, product, combinations, combinations_with_replacement,permutations
from bisect import bisect, bisect_left, bisect_right
from functools import reduce,lru_cache,cmp_to_key
from decimal import Decimal, getcontext,ROUND_HALF_UP
import sympy

sys.setrecursionlimit(10 ** 8)

def my_gcd(*numbers):#最大公約数,O(ln(n))らしい
    return reduce(gcd, numbers)

def my_lcm_base(x, y):
    return (x * y) // gcd(x, y)

def my_lcm(*numbers):#最小公倍数
    return reduce(my_lcm_base, numbers, 1)

def per(n,r):
    ans=1
    for i in range(r):
        ans*=(n-i)
    return ans

def com(n,r):
    return per(n,min(r,n-r))//factorial(min(r,n-r))

def prime_factorize(n):#素因数分解，リストで並ぶ．24→[2, 2, 2, 3],O(sqrt(n))多分
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a


def make_divisors(n):#約数がリストで出力される．O(sqrt(n))
    lower_divisors , upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors[::-1]

def sosuhantei(n):#0が素数じゃない，1が素数 abc239d.py
    if n<=1:
        return(0)
    elif n==2:
        return(1)
    elif n%2==0:
        return (0)
    else:
        for i in range(3,ceil(sqrt(n))+1,2):
            if n%i==0:
                return (0)
        return (1)

class unionfind():#print(uf.parents),0-index
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n#負だったら集合の数であり、親。
        self.edgen=[0]*n#その集合の辺の数。親のインデックスでのみ機能。

    def find(self, x):#xの親を出力
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        xp = self.find(x)
        yp = self.find(y)
        

        if xp == yp:
            self.edgen[xp]+=1
            return

        if -self.parents[xp]<-self.parents[yp]:
            
            self.parents[yp]+=self.parents[xp]
            self.edgen[yp]+=self.edgen[xp]+1
            
            self.parents[xp]=yp
        else:
            self.parents[xp]+=self.parents[yp]
            self.edgen[xp]+=self.edgen[yp]+1
            
            self.parents[yp]=xp

def yes():
    print("Yes")

def no():
    print("No")

def nb(n,m,a,b):
    g=[[] for _ in range(n)]
    #g=dd(list)
    for i in range(m):
        g[a[i]-1].append(b[i]-1)
        g[b[i]-1].append(a[i]-1)
    return g

mod=998244353
mod2=10**9+7

def zs(*a):#a,b,c,...=zs(a,b,c,...)
    return zip(*sorted(zip(*a)))

def zsr(*a):
    return zip(*sorted(zip(*a),reverse=1))

def primes(n):#素数列挙,eratosthenes
    is_prime = [1] * (n + 1)
    is_prime[0] = 0
    is_prime[1] = 0
    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]==0:
            continue
        for j in range(i * 2, n + 1, i):
            is_prime[j] = 0
    return [i for i in range(n + 1) if is_prime[i]]#素数がリストで出てくる
    #return is_prime#01で出てくる

class fenwick_tree:#0-index
    def __init__(self, n):
        self._n = n
        self.data = [0] * n

    def add(self, p, x):
        assert 0 <= p < self._n
        p += 1
        while p <= self._n:
            self.data[p - 1] += x
            p += p & -p

    def sum(self, l, r):
        assert 0 <= l <= r <= self._n
        return self._sum(r) - self._sum(l)

    def _sum(self, r):
        s = 0
        while r > 0:
            s += self.data[r - 1]
            r -= r & -r
        return s

class multiset:
    # n: サイズ、compress: 座圧対象list-likeを指定(nは無効)
    # multi: マルチセットか通常のOrderedSetか
    def __init__(self, n=0, *, compress=[], multi=True):
        self.multi = multi
        self.inv_compress = sorted(set(compress)) if len(compress) > 0 else [i for i in range(n)]
        self.compress = {k: v for v, k in enumerate(self.inv_compress)}
        self.counter_all = 0
        self.counter = [0] * len(self.inv_compress)
        self.bit = BIT(len(self.inv_compress))

    def add(self, x, n=1):     # O(log n)
        if not self.multi and n != 1: raise KeyError(n)
        x = self.compress[x]
        count = self.counter[x]
        if count == 0 or self.multi:  # multiなら複数カウントできる
            self.bit.add(x + 1, n)
            self.counter_all += n
            self.counter[x] += n

    def remove(self, x, n=1):  # O(log n)
        if not self.multi and n != 1: raise KeyError(n)
        x = self.compress[x]
        count = self.bit.get(x + 1)
        if count < n: raise KeyError(x)
        self.bit.add(x + 1, -n)
        self.counter_all -= n
        self.counter[x] -= n

    def __repr__(self):
        return f'MultiSet {{{(", ".join(map(str, list(self))))}}}'

    def __len__(self):         # oprator len: O(1)
        return self.counter_all

    def count(self, x):        # O(1)
        return self.counter[self.compress[x]]

    def __getitem__(self, i):  # operator []: O(log n)
        if i < 0: i += len(self)
        x = self.bit.lower_bound(i + 1)
        if x > self.bit.n: raise IndexError('list index out of range')
        return self.inv_compress[x - 1]

    def __contains__(self, x): # operator in: O(1)
        return self.bit.get(self.compress.get(x, self.bit.n) + 1, 0) > 0

    def bisectleft(self, x):  # O(log n)
        return self.bit.sum(bisect_left(self.inv_compress, x))

    def bisectright(self, x): # O(log n)
        return self.bit.sum(bisect_right(self.inv_compress, x))
    
class BIT:
    def __init__(self, n):
        self.n = len(n) if isinstance(n, list) else n
        self.size = 1 << (self.n - 1).bit_length()
        if isinstance(n, list):  # nは1-indexedなリスト
            a = [0]
            for p in n: a.append(p + a[-1])
            a += [a[-1]] * (self.size - self.n)
            self.d = [a[p] - a[p - (p & -p)] for p in range(self.size + 1)]
        else:                    # nは大きさ
            self.d = [0] * (self.size + 1)

    def __repr__(self):
        p = self.size
        res = []
        while p > 0:
            res2 = []
            for r in range(p, self.size + 1, p * 2):
                l = r - (r & -r) + 1
                res2.append(f'[{l}, {r}]:{self.d[r]}')
            res.append(' '.join(res2))
            p >>= 1
        res.append(f'{[self.sum(p + 1) - self.sum(p) for p in range(self.size)]}')
        return '\n'.join(res)

    def add(self, p, x):  # O(log(n)), 点pにxを加算
        assert p > 0
        while p <= self.size:
            self.d[p] += x
            p += p & -p

    def get(self, p, default=None):     # O(log(n))
        assert p > 0
        return self.sum(p) - self.sum(p - 1) if 1 <= p <= self.n or default is None else default

    def sum(self, p):     # O(log(n)), 閉区間[1, p]の累積和
        assert p >= 0
        res = 0
        while p > 0:
            res += self.d[p]
            p -= p & -p
        return res

    def lower_bound(self, x):   # O(log(n)), x <= 閉区間[1, p]の累積和 となる最小のp
        if x <= 0: return 0
        p, r = 0, self.size
        while r > 0:
            if p + r <= self.n and self.d[p + r] < x:
                x -= self.d[p + r]
                p += r
            r >>= 1
        return p + 1
    
def my_round(val, digit=1):#四捨五入,digitは...,100,10,1,0.1,0.01,...で入力．完璧ではない．
    return Decimal(str(val)).quantize(Decimal("1E"+str(int(log10(digit))+1)), rounding=ROUND_HALF_UP)

inf=float("inf")

def legendre(n,p):#n!が素数pで何回割り切れるか.O(logN)
    if n>=p:
        return n//p+legendre(n//p,p)
    else:
        return 0

"""
dj=[-1,0,1,1,1,0,-1,-1]
di=[1,1,1,0,-1,-1,-1,0]
"""

di=[0,1,0,-1]
dj=[1,0,-1,0]

def ncr_eu(n, r, mod):#nCr mod．P(Pは素数)
    ret = 1
    if r < n:
        inv = [1]
        for i in range(1, r+1):
            inv.append(max(1, (-(mod//i) * inv[mod % i]) % mod))
            ret = ret*(n+1-i)*inv[i] % mod
    return ret

class sum3d:#abc366dver6 tensor[x][y][z]
    def __init__(self,tensor):
        self.lenx=len(tensor)
        self.leny=len(tensor[0])
        self.lenz=len(tensor[0][0])
        self.at=[[[0]*(self.lenz+1) for _ in range(self.leny+1)] for _ in range(self.lenx+1)]
        for x in range(1,self.lenx+1):
            for y in range(1,self.leny+1):
                for z in range(1,self.lenz+1):
                    self.at[x][y][z]=tensor[x-1][y-1][z-1]
        for x in range(1,self.lenx+1):
            for y in range(1,self.leny+1):
                for z in range(1,self.lenz+1):
                    self.at[x][y][z]+=self.at[x][y][z-1]
        for x in range(1,self.lenx+1):
            for y in range(1,self.leny+1):
                for z in range(1,self.lenz+1):
                    self.at[x][y][z]+=self.at[x][y-1][z]
        for x in range(1,self.lenx+1):
            for y in range(1,self.leny+1):
                for z in range(1,self.lenz+1):
                    self.at[x][y][z]+=self.at[x-1][y][z]
    def query(self,lx,rx,ly,ry,lz,rz):
        return  self.at[rx][ry][rz]-self.at[rx][ry][lz]-self.at[rx][ly][rz]+self.at[rx][ly][lz]\
                -self.at[lx][ry][rz]+self.at[lx][ry][lz]+self.at[lx][ly][rz]-self.at[lx][ly][lz]

class sum2d:#abc366ver7 tensor[x][y]
    def __init__(self,tensor):
        self.lenx=len(tensor)
        self.leny=len(tensor[0])
        self.at=[[0]*(self.leny+1) for _ in range(self.lenx+1)]
        for x in range(1,self.lenx+1):
            for y in range(1,self.leny+1):
                    self.at[x][y]=tensor[x-1][y-1]
        for x in range(1,self.lenx+1):
            for y in range(1,self.leny+1):
                    self.at[x][y]+=self.at[x][y-1]
        for x in range(1,self.lenx+1):
            for y in range(1,self.leny+1):
                    self.at[x][y]+=self.at[x-1][y]
    def query(self,lx,rx,ly,ry):
        return  self.at[rx][ry]-self.at[rx][ly]-self.at[lx][ry]+self.at[lx][ly]

def base_10(num_n,n):#n進法->10進法
    num_10 = 0
    for s in str(num_n):
        num_10 *= n
        num_10 += int(s)
    return num_10


def base_n(num_10,n):#10進法->n進法
    str_n = ''
    while num_10:
        if num_10%n>=10:
            return -1
        str_n += str(num_10%n)
        num_10 //= n
    return int(str_n[::-1])

def ii(): return int(input())
def im(): return map(int, input().split())
def il(): return list(map(int,input().split()))
def ils(): return sorted(map(int,input().split()))
def ir1(n):return [int(input()) for _ in range(n)]
def ir(n): return map(list, zip(*[list(map(int, input().split())) for i in range(n)]))
#n=0だとRE
def irl(n): return [list(map(int,input().split())) for _ in range(n)]
#毎行の要素数が違っても機能する
def si(): return input()
def sm(): return input().split()
def sl(): return list(input().split())
def sr(n): return [input() for _ in range(n)]#['s#','#g']
def s_row_str(n): return [list(input().split()) for _ in range(n)]#[['s#'],['#g']]
def srl(n): return [list(input()) for _ in range(n)]#[['s','#'],['#','g']]swapのことを考えるとこの入力がいいかも

#@lru_cache(maxsize=1000)


    

    














