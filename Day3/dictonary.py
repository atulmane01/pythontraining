'''
1. How to create:
    In Python, a Dictionary can be created by placing a sequence of elements within curly {} braces, separated by 'comma'.
     Dictionary holds pairs of values, one being the Key and the other corresponding pair element being its Key:value

     Ex:
        dict={"key":"value"}

2.How to assign element:
        we add a new element to the dictionary by using a new key as a subscript and assigning it a value.
        EX
            CountryCod = {"India": 91, "UK" : 44 , "USA" : 1}
            print(CountryCodeDict)
            CountryCod["Spain"]= 34
            print "After adding"
            print(CountryCod)

3.How to use it:
        Dictionary in Python is an unordered collection of data values, used to store data values like a map, which,
        unlike other Data Types that hold only a single value as an element,
        Dictionary holds key:value pair. Key-value is provided in the dictionary to make it more optimized.

        Dict = {1: 'atul', 'B' : 'mane'}
        print(Dict)


4.Methods:
    1.clear():
        The method clear() removes all items from the dictionary.

    EX
        dict = {'Name': 'Zara', 'Age': 7}
        print ("Start Len : %d" %  len(dict))

        dict.clear()
        print (len(dict))

    2.copy():
        The method copy() returns a shallow copy of the dictionary.

        EX
            dict1 = {'Name': 'Manni', 'Age': 7, 'Class': 'First'}
            dict2 = dict1.copy()
            print ("New Dictionary : ",dict2)


    3.items():
        The method items() returns a list of dict's (key, value) tuple pairs

        EX:
            dict = {'Name': 'Zara', 'Age': 7}
            print (dict.items())

    4.keys():
        The method keys() returns a list of all the available keys in the dictionary.

    EX:
            dict = {'Name': 'Zara', 'Age': 7}
            print (dict.keys())

    5.update():
        The method update() adds dictionary dict2's key-values pairs in to dict. This function does not return anything.

        Ex:
            dict = {'Name': 'Zara', 'Age': 7}
            dict2 = {'Sex': 'female' }

            dict.update(dict2)
            print ("updated dict : ", dict)

            output:
                updated dict :  {'Name': 'Zara', 'Age': 7, 'Sex': 'female'}

    6.values():
        The method values() returns a list of all the values available in a given dictionary.

        EX:
            dict = {'Sex': 'female', 'Age': 7, 'Name': 'Zara'}
            print ("Values : ",  list(dict.values()))

5.How to traverse through a dictionary:
    EX:
        a_dict = {'color': 'blue', 'fruit': 'apple', 'pet': 'dog'}
        for key in a_dict:
            print(key)

        output:
            color
            fruit
            pet


6.How to traverse through keys and values in a dictionary:
    A dictionary stores key-value pairs. Iterating over a dictionary accesses its keys and values individually.

    EX:
        a_dictionary = {"a": 1, "b": 2}
        for key, value in a_dictionary.items():
            print(key, value)

            output:
                a 1
                b 2


7.Dictionary comprehension :
    Dictionary comprehension is a powerful concept and can be used to substitute for loops and lambda functions
    Dictionary comprehension is a method for transforming one dictionary into another dictionary.
    Dictionary comprehension is an elegant and concise way to create dictionaries.
     ex:

        numbers = range(10)
        new_dict_for = {}

        # Add values to `new_dict` using for loop
        for n in numbers:
            if n%2==0:
                new_dict_for[n] = n**2

        print(new_dict_for)
        output:
        {0: 0, 8: 64, 2: 4, 4: 16, 6: 36}


        # Use dictionary comprehension
        new_dict_comp = {n:n**2 for n in numbers if n%2 == 0}
        print(new_dict_comp)
        output:

        {0: 0, 8: 64, 2: 4, 4: 16, 6: 36}

'''