This is a python3 syntax checker for 3.11.4 implemented using ANTLR4 with Python. It was created as part of a class project.
The idea is that it mainly checks that data structures are correct when doing operations in the file.

It covers
- For loop declarations
- While Loop declarations
- If statement, elif statements, else statement.
- Operations +,-,/,%,//,*,** with support for parenthesis between data types and checks what is valid. All expressions are left-recursive except for ** which is right recursive.
- The program is run through main.py
- There is a MyExprVisitor.py class that implements the labels from the Expr.g4(ANTLR4 file) which declares the grammar.


Note:
- There are a few invalid multiplications like "hello"*5 is allowed and 5*"hello" is allowed.
- Multiple elif statements are not perfectly done.
- Sometimes it says unexpected EOF(end of file) but then says the program is built correctly.

Future Work:
- Fix elif statements
- Multi-line comments
- Decorators
- EOF file issues.
