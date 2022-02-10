'''
1. How to create:
    A set is created by placing all the items (elements) inside curly braces {} ,
    separated by comma, or by using the built-in set() function

    In Python, Set is an unordered collection of data type that is iterable, mutable and has no duplicate elements

    EX:
        my_set = {1, 2, 3}
        print(my_set)

2.How to assign element:

    GEEK = {'g', 'e', 'k'}

    # adding 's'
    GEEK.add('s')
    print('Letters are:', GEEK)

    # adding 's' again
    GEEK.add('s')
    print('Letters are:', GEEK)


3.How to concatenate two sets:

    1.union():
        The union() method returns a new set with all items from both sets:

        Ex:
        set1 = {"a", "b" , "c"}
        set2 = {1, 2, 3}

        set3 = set1.union(set2)
        print(set3)

        output:
        {1, 2, 'c', 3, 'b', 'a'}

    2.he update() method inserts the items in set2 into set1:

    Ex:
        set1 = {"a", "b" , "c"}
        set2 = {1, 2, 3}
        set1.update(set2)
        print(set1)
output:
        {'c', 1, 2, 3, 'b', 'a'}


4. Methods and usage of it:

    1.add():
        Adds an element to the set

        Ex:
        fruits = {"apple", "banana", "cherry"}

        fruits.add("orange")

        print(fruits)

    2.clear():
        Removes all the elements from the set

        EX:
        fruits = {"apple", "banana", "cherry"}
        fruits.clear()
        print(fruits)

    3.copy():
        The copy() method copies the set.

        fruits = {"apple", "banana", "cherry"}
        x = fruits.copy()
        print(x)

    4.pop():
        Removes an element from the set

        EX:
            fruits = {"apple", "banana", "cherry"}

            fruits.pop()

            print(fruits)

            output:
                {'apple', 'cherry'}

    5.remove():
        Removes the specified element

        ex:
            fruits = {"apple", "banana", "cherry"}

            fruits.remove("banana")

            print(fruits)


    6.discard():
        The discard() method removes the specified item from the set.

        fruits = {"apple", "banana", "cherry"}

        fruits.discard("banana")

        print(fruits)











'''