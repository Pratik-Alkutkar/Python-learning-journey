"""
case (i)    By rule, global variable should be accessible everywhere in source code. 
            But access of global variable to inner function in case of nested def 
            statement may get prevented if the outer functions defines a local variable 
            with the same name. 

            N = 100 
            def f(): 
                N = "Hello" 
                def g(): 
                    print(N) # g wants to access global N and not local N of outer function f()
                g() 
            f() 

            Solution: 
            use following statement 
            global N 
            inside g() 
            It will tell Python to bin all references of N in function g() to global version 
            of N 

            Soln 
            N = 100 
            def f(): 
                N = "Hello" 
                def g(): 
                    global N 
                    print(N) # reference of N will be boung to global N 
                g() 
            f() 

case (ii): Program logic requires that the global variable shoujld be modified 
            from the body of function 

            N = 100 
            def f(): 
                # Global N must be modified to 200 
                N = 200     # global N is not modified instead local N is created 
                            # because of LHS treatment of variable name 
            print(N) # 100 
            f() 
            print(N) # 100 

            Or worse 
            N = 100 
            def f(): 
                # Global N must be incremented by 1 
                N = N + 1   # global N is not modified and local N is not created 
                            # Results in UnboundLocalError exception as N is defined 
                            # in f() but referenced before its definition 
            f()

            Soln is as follows: 
            Write statement 
            global N 
            in function f() 
            because global statement not only binds RHS references within function 
            to global version of the variable but also LHS references. 

            N = 100 
            def f(): 
                global N 
                N = 200 # global N will be reassigned from 100 to 200 
                        # because global N forces Python to bind 
                        LHS use of N as well to global N 
            print(N) # 100 
            f() 
            print(N) # 200 

            N = 100 
            def f(): 
                global N 
                N = N + 1 # Because of global N, both RHS use of N (in N + 1)
                          # and LHS use of N (N = N + 1) are bound to global version 
                          # while evaluating N + 1, N will be resolved to global scope N 
                          # which is 100, 100 + 1 == 101 and 101 will be assigned to global N 
                          # In global symbol table N gives up its associtation with 100 
                          # and binds itself with 101. 
                          # Note that N is NOT created in local symbol table of f() 
                          # despite appearing on LHS for the first time 
            print(N) # 100 
            f() 
            print(N) # 101 

            One of the use is to create a global variable within function 

            # No variable is defined in global scope 
            def f(): 
                N = 100 # N will be created in local symbol table of f() 
            print(N) # NameError:
            -------------------

            # No variable is defined in global scope 
            def f(): 
                global N 
                N = 500     # 'N':500 will be stored in global symbol table 
            
            try: 
                print(N)
            except NameError: 
                exc_name, exc_data, exc_tb = sys.exc_info() 
                print(exc_name, exc_data)  # NameError: varible 'N' is not defined 
            f() 
            print(N) # 500 

            Remember. 

            import tkinker 

            def onClick(): 
                str_var.set(some string)

            def main(): 
                global str_var 
                root_window = tkinter.Tk() 
                root_window.title("Test")
                str_var = tkinter.StringVar() 
                L = tkinter.Label(root_window)
                L.configure(textvariable = str_var)

                B = tkinter.Button(root_window)
                B.configure(text='Change Lable', command=onClick)

                L.grid(0, 0) 
                B.grid(1, 0)
                root_window.mainloop()

            main()
"""