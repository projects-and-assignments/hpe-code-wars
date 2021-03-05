Virtual CodeWars 2021 -- Open Beta Packet!

This ZIP file includes:

- judge_datasets:
    Directory which the judges used to test every problem.
    Use each input to test the program, there is also the expected output with which to compare.

- ringojs-1.2.0:
    Support directory for checkProb.bat.  Only needed if testing JavaScript.

- solutions:
    Contains all of the solutions the judges and problem authors wrote for the open beta problems.

- student_datasets:
    Directory with test data for every problem.
    Use each input to test your program, and compare with each expected output.

- codewars-2021openbeta-na-problems-2021-02-26-UTC-b28.pdf:
    Instruction sheet and Problems 0-7

- README.txt:
    This file.

- checkProb.bat:
    A Windows batch file like the one the Judges will use to test your programs.

    HOW TO USE:
        1. EDIT THE FILE to set your JDK and/or PYTHON paths.
            - You need JDKPATH if you are using Java or JavaScript.
            - You need PY3PATH or PY2PATH if you are using Python 3 or 2.

        2. COPY only one program "probXX.zzz" into the directory.  (For example, "prob10.py")
            - NOTE: A Python2 program must have its file extension changed to "py2"

        3. Open a Command Window  (Start Menu: "Command Prompt")
            - CD to your working directory.

        4. Type "checkProb" to test your program against all probXX datasets in the student_datasets directory.
            - Use "checkProb showin" to also show the test input during the run

    NOTE:  Using checkProb.bat is OPTIONAL.
        We provide it as an example of how we will be testing your programs.
        You do not need it.  But you must test your program against ALL input files.
        The Judges will test against modified input files, and your programs
        must correctly solve all of them to pass.
        See an explanation of how to test on the Instruction Sheet in the PDF file.
