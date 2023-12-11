#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    t = tuple(map(int, input().split()))

    c = t.count(t[0])
    print("Количество равных элементов:", c)
    print("Элементы, следующие за последним из них:", t[c:])
