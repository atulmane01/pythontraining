'''
1. How to create:
    Lists are used to store multiple items in a single variable.
    Lists are created using square brackets:

Create a List:

    thislist = ["apple", "banana", "cherry"]
    print(thislist)


2.How to assign element :
    List in python is mutable types which means it can be changed after assigning some value.
    # code
    List=[ 10, 20, 30, 40, 50, 60]
    print("original list ")
    print(List)

    #changing the first value
    List[0] = 11

    #changing the second value
    List[1] = 21

3.How to concatenate two list:
    The most conventional method to perform the list concatenation, the use of “+” operator can
    easily add the whole of one list behind the other list and hence perform the concatenation

    test_list3 = [1, 4, 5, 6, 5]
    test_list4 = [3, 5, 7, 2, 5]

    # using + operator to concat
    test_list3 = test_list3 + test_list4

    # Printing concatenated list
    print ("Concatenated list using + : "+ str(test_list3))


4. Methods and usage of it :
    1.Python List append():
        Add a single element to the end of the list

            currencies = ['Dollar', 'Euro', 'Pound']

            # append 'Yen' to the list
            currencies.append('rs')
            print(currencies)

            # Output: ['Dollar', 'Euro', 'Pound', 'rs']

    2.Python List clear():
        Removes all Items from the List

            prime_numbers = [2, 3, 5, 7, 9, 11]
            # remove all elements
            prime_numbers.clear()
            # Updated prime_numbers List
            print('List after clear():', prime_numbers)

            # Output: List after clear(): []

    3.Python List copy():
        returns a shallow copy of the list
            #mixed list
            prime_numbers = [2, 3, 5]
            #copying a list
            numbers = prime_numbers.copy()
            print('Copied List:', numbers)
            # Output: Copied List: [2, 3, 5]



    4.Python List count():
        returns count of the element in the list
        The count() method returns the number of times the specified element appears in the list.

        # create a list
            numbers = [2, 3, 5, 2, 11, 2, 7]
            # check the count of 2
            count = numbers.count(2)
            print('Count of 2:', count)
            # Output: Count of 2: 3

    5.Python List extend():
        adds iterable elements to the end of the list

        # create a list
            prime_numbers = [2, 3, 5]

            # create another list
            numbers = [1, 4]
            # add all elements of prime_numbers to numbers
            numbers.extend(prime_numbers)
            print('List after extend():', numbers)
            # Output: List after extend(): [1, 4, 2, 3, 5]

    6.Python List index():
        returns the index of the element in the list

        list1 = [1, 2, 3, 4, 1, 1, 1, 4, 5]
        print(list1.index(4))
        list2 = ['cat', 'bat', 'mat', 'cat', 'pet']
        print(list2.index('cat'))

        output:
        3
        0


    7.Python List insert()
        insert an element to the list.

        list1 = [ 1, 2, 3, 4, 5, 6, 7 ]
        # insert 10 at 4th index
        list1.insert(4, 10)
        print(list1)

        output:
        [1, 2, 3, 4, 10, 5, 6, 7]

    8.Python List pop()
        Removes element at the given index

        prime_numbers = [2, 3, 5, 7]
        # remove the element at index 2
        removed_element = prime_numbers.pop(2)
        print('Removed Element:', removed_element)
        print('Updated List:', prime_numbers)

        output:
        # Output:
        # Removed Element: 5
        # Updated List: [2, 3, 7]

    9.Python List remove():
        Removes item from the list
        prime_numbers = [2, 3, 5, 7, 9, 11]
        # remove 9 from the list
        prime_numbers.remove(9)
        # Updated prime_numbers List
        print('Updated List: ', prime_numbers)

        # Output: Updated List:  [2, 3, 5, 7, 11]

    10.Python List reverse()
        reverses the list

        prime_numbers = [2, 3, 5, 7]
        # reverse the order of list elements
        prime_numbers.reverse()
        print(prime_numbers)
        output:
            [7, 5, 3, 2]

    11.Python List sort()
        sorts elements of a list
        cars = ['Ford', 'BMW', 'Volvo']
        cars.sort()
        print(sort)



5.List comprehension:
    List comprehension in Python is an easy and compact syntax for creating a list from a string or another list.
        even_nums = []
        for x in range(21):
            if x%2 == 0:
                even_nums.append(x)
        print(even_nums)


6.Indexing and Slicing(Operations):
    Indexing means referring to an element of an iterable by its position within the iterable.
    Each of a string’s characters corresponds to an index number and each character can be accessed using their index number.

    We can access characters in a String in Two ways :
        1.Accessing Characters by Positive Index Number:
            In this type of Indexing, we pass a Positive index(which we want to access) in square brackets.
            The index number start from index number 0 (which denotes the first character of a string).
            EX.
                str = "HiIamATulhowareyou !"
                # accessing the character of str at 0th index
                print(str[0])
                # accessing the character of str at 6th index
                print(str[6])
                # accessing the character of str at 10th index
                print(str[10])

                output:
                    H
                    T
                    O

        2.Accessing Characters by Negative Index Number:
            In this type of Indexing, we pass the Negative index(which we want to access) in square brackets.
            Here the index number starts from index number -1 (which denotes the last character of a string).
            EX.
                str = "HiIamATulhowareyou!"
                # accessing the character of str at 0th index
                print(str[-1])
                # accessing the character of str at 6th index
                print(str[-5])
                # accessing the character of str at 10th index
                print(str[-10])

                output:
                    !
                    e
                    h
    2.Slicing:
        Slicing in Python is a feature that enables accessing parts of sequence.
        In slicing string, we create a substring, which is essentially a string that exists within another string.

        EX:
            # declaring the string
            str ="Hello Everyone!"

            print("Original String :-")
            print(str)

            # reversing the string using slicing
            print("Reverse String :-")
            print(str[: : -1])

            output:
             Original String :-
            Hello Everyone!
            Reverse String :-
            !enoyrevE olleH


'''