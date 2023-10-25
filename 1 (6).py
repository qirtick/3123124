dct = {
  1: {
    1: 11,
    2: 12,
    3: 13,
  },
  2: {
    1: 21,
    2: 22,
    3: 23,
  },
  3: {
    1: 24,
    2: 25,
    3: 26,
  },
}

sum_elements = sum(sum(inner.values()) for inner in dct.values())
print("Сумма элементов словаря:", sum_elements)