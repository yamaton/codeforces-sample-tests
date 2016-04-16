CodeForces Automatic Scraping and Testing
=========================================

Test your Codeforces solution against sample cases with ease! This script scrapes sample input and output of the problem you specify, and then test your code against the sample cases. The script can handle Python, C++, Haskell, and Scala.
 
### Requirement

-   Python 3.x
-   [Beautiful Soup 4](<http://www.crummy.com/software/BeautifulSoup/>)


### Usage

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
python3 cft.py <filename-of-your-code>
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**NOTE:** the filename **must** contain a problem ID. You may have another
string in the filename as long as they are separated by space ` `, or hyphen
`-`, or underscore `_`. The prefix `CF` is specially treated, and neglected even without these separators. For example, following filenames are all allowed.

* 600D.cpp
* 600D-sample.py
* sample 600A\_code.py
* yet another\_sample-599D-spongebob.hs
* CF599A.scala

The script `cft.py` feeds the samples cases to your code as standard input, and returns “ok” if the standard output agrees with the samples.

![](<screenshots/py_600a.png>)

Otherwise, it returns “Incorrect”, and shows sample input, your output, and sample output. This happens as long as output strings do not agree **exactly**.

![](<screenshots/cpp_600d.png>)

### Configuration

Compilation options are set as follows. Please fix `src/cft.py` to change them.

**C++:**

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
clang++ -std=c++11 <your-code> -o <your-code>.out
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Haskell:**

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
ghc -O2 -Wall <your-code> -o <your-code>.out
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

### Tips

I personally make a symbolic link to the path

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
ln -s /my/path/to/src/cft.py ~/bin/cft
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

such that I can run this script like this.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
cft 600A.py
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
