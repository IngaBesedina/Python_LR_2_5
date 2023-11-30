#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    A = tuple(map(int, input().split()))

    k = A.count(A[0])
    print("Количество равных элементов:", k)
    print("Элементы, следующие за равными элементами: ", A[k:len(A)+1])
