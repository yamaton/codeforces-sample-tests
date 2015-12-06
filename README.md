CodeForces Automatic Testing of Sample Inputs
==============================================


Test your code against the Codeforces sample inputs. The script can handle
Python, C++, Haskell, and Scala.

 
**Usage:**

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
python3 cft.py <your-code> <problem-id>
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 

**NOTE:** the filename **must** contain a problem ID. You may have another
string in the filename as long as they are separated by space ` `, or hyphen `-`, or
underscore `_`. For example, following filenames are all allowed.

 

-   600D.cpp

-   600D-sample.py

-   sample 600A\_code.py

-   yet another\_sample-599D-spongebob.hs

 

The script `cft.py` returns “ok” if the output of your code agrees with the
sample output.

![](<screenshots/py_600a.png>)

 
Otherwise, it shows Input, your output, and correct output. It raises
“Incorrect” if output strings do not agree exactly.

![](<screenshots/cpp_600d.png>)


### Configuration

Compilation options are set as follows. Please fix `src/cft.py` to change them.

**C++:**
```
clang++ -std=c++11 <your-code> -o <your-code>.out
```

**Haskell:**
```
ghc -O2 -Wall <your-code> -o <your-code>.out
```





### Tips

I personally make a shell script 
```
#!/bin/sh
python /to/your/path/to/cft.py $1
```

such that I can run like this.

```
cft 600A.py
```