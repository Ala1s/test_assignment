
def del_duplicates(l):
    """
    Deletes duplicates from list while preserving initial sorting

    Вычислительная сложность:
    Операции доступа к элементам в list и set в Python выполняются за O(1)
    set реализован как хэш-таблица, так что в большинстве случаев проверка наличия элемента в set занимает O(1).
    Если же при записи элементов в set случались коллизии - в худшем случае проверка будет занимать O(n).
    Функции в любом случае придется пройтись по всем элементам списка.
    Таким образом, сложность:
    в худшем случае: O(n^2) - если будут коллизии в хэш-таблице
    (более реалистичная) средняя оценка: O(n)

    По памяти:
    В любом случае нужно хранить весь список полученный на вход, плюс set просмотренных элементов, 
    который в худшем случае (если все элементы различны) будет содержать n элементов.
    Поэтому асимптотическая оценка сложности по памяти: O(2*n) = O(n)

    >>> del_duplicates([1,2,3,1])
    [1, 2, 3]
    >>> del_duplicates([1,3,2,1,5,3,5,1,4])
    [1, 3, 2, 5, 4]
    >>> del_duplicates([1,5,6,7,2,5,3,6,8,3,5])
    [1, 5, 6, 7, 2, 3, 8]
    """
    seen = set()
    i=0
    while i<len(l):
        if l[i] not in seen:
            seen.add(l[i])
            i+=1
        else:
            del[l[i]]
    return l

if __name__ == "__main__":
    import doctest
    doctest.testmod()