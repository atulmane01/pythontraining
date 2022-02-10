'''

1.Break:
         statement is used to terminate the execution of the loop containing it.
         As soon as the loop comes across a break statement,
         the loop terminates and the execution transfers to the next statement following the loop
    EX:
    for val in "string" :
    if val == "i":
       break
       print(val)
    print("the end")

2.Continue:
        The continue statement is used to skip the rest of the code in the loop for the current iteration.
        It does not terminate the loop like the break statement and continues with the remaining iterations.
    EX:
      for val in "string" :
    if val == "i":
       continue
       print(val)
   print("the end")
        Output:
        s
        t
        r
        n
        g
        the end

3.Pass :

    The pass statement is a null operation. It basically means that the statement is required syntactically
    but you do not wish to execute any command or code.

    for val in "please":
        if val == "a":
            pass
            print("pass block")
            print(val)

          Output:

        p
        l
        e
        pass block
        a
        s
        e



'''