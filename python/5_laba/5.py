# 7. Генератор для объединения последовательностей по
# заданной стратегии. Сверните возвращемые последовательности 
# в зависимости от типа данных в них.
# К генератору должна быть применена хотя бы одна из функций map, reduce, filter.

def genFunc(seq1, seq2, func):
    if isinstance(seq1, list) and isinstance(seq2, list):
        res = list(func(seq1, seq2))
    elif isinstance(seq1, str) and isinstance(seq2, str):
        res = ''.join(func(seq1, seq2))
    else:
        raise ValueError("Unsupported data types")

    yield res

def f1(seq1, seq2):
    return list(map(lambda x, y: x + y, seq1, seq2)) #sum

def f2(seq1, seq2):
    return list(map(lambda x, y: x * y, seq1, seq2)) #mult

seq1 = [1,2,3]
seq2 = [4,5,6]

print(next(genFunc(seq1, seq2, f2)))