#!/usr/bin/env python3
"""
Web-scrape input and output samples from a CodeForces problem, then returns the information in JSON

@author yamaton
@date 2015-08-31
"""
import urllib.request
import json
import sys
import itertools as it
import bs4      # BeautifulSoup 4


CODEFORCES_PROBLEM_URL = 'http://codeforces.com/problemset/problem/{}/{}'
CODEFORCES_CONETST_URL = 'http://codeforces.com/contest/{}/problem/{}'


def is_proper(prob_id):
    """
    Check if the given string is proper CodeForces problem ID.

    Args:
        prob_id (str): problem ID to be examined

    Return:
        bool.

    >>> is_proper('AA3')
    False

    >>> is_proper('413A')
    True

    >>> is_proper('310AB')
    False
    """
    if not prob_id.isalnum():
        return False
    decimals = ''.join(it.takewhile(lambda c: c.isdecimal(), prob_id))
    letters = ''.join(filter(lambda c: c.isalpha(), prob_id))

    if prob_id != decimals + letters or len(letters) != 1 or len(decimals) > 3:
        return False
    return True


def check_sanity(prob_id):
    """
    Exit if given string is NOT a CodeForces problem ID.

    Args:
        prob_id (str): problem ID to be examined

    Return:
        None
    """
    msg = 'Problem ID {} has bad format!'.format(prob_id)
    if not is_proper(prob_id):
        sys.exit(msg)


def geturl(prob_id, url=CODEFORCES_PROBLEM_URL):
    """
    Returns CodeForces URL for given problem ID.

    Args:
        prob_id (str)
        url (str)

    Returns:
        str

    >>> geturl('413B')
    'http://codeforces.com/problemset/problem/413/B'

    >>> geturl('A11')
    'http://codeforces.com/problemset/problem/11/A'
    """
    contest_id = ''.join(c for c in prob_id if c.isdecimal())
    problem_idx = ''.join(c for c in prob_id if c.isalpha()).upper()
    return url.format(contest_id, problem_idx)


def tag_content(bsform, classname, tag='div'):
    """
    Get content by searching over HTML segment

    Args:
        bsform (bs4.element.Tag)  BeautifulSoup constructor
        classname (str): class attribute under `tag` ('div' by default) Tag.
        tag (str): tag name. 'div' corresponds to "<div ...> ... </div>" tag
    """
    html = bsform.find_all(tag, class_=classname)
    lst = [x.pre.contents for x in html]
    return [[x for x in xs if type(x) is bs4.element.NavigableString]
            for xs in lst]


def save_samples(js):
    """
    Save input and output as text files from JSON string

    Args:
        js (str): JSON string with
            'sample_io' -> ['input': ... , 'output': ...]
            'id'

    input file is saved as '<problem_id>_<index>.in' like '23C_0.in'
    output file is saved as '<problem_id>_<index>.out' like '11A_1.out'
    """
    data = json.loads(js)
    problem_id = data['id']
    inputs = [x['input'] for x in data['sample_io']]
    outputs = [x['output'] for x in data['sample_io']]

    for i, (inp, out) in enumerate(zip(inputs, outputs)):
        name = problem_id + '_' + str(i)
        with open(name + '.in', 'w') as f:
            for line in inp:
                print(line, file=f)
        with open(name + '.out', 'w') as f:
            for line in out:
                print(line, file=f)


def extract_samples(problem_str, is_contest=False):
    """
    Go to CodeForces website and return input/output samples in JSON string

    Args:
        problem_str (str): proble ID

    Returns:
        str. JSON string of the form
        {
        'id': ...
        'url': ...
        'sample_io' (str): [ {'input': ...,
                               'output': ... } ]
        }
    """
    check_sanity(problem_str)
    if is_contest:
        url = geturl(problem_str, CODEFORCES_CONETST_URL)
    else:
        url = geturl(problem_str)

    with urllib.request.urlopen(url) as f:
        rawhtml = f.read()

    soup = bs4.BeautifulSoup(rawhtml, 'html.parser')
    testdoc = soup.find('div', 'sample-test')
    inputs = tag_content(testdoc, 'input')
    outputs = tag_content(testdoc, 'output')

    in_and_out = [{'input': x, 'output': y} for (x, y) in zip(inputs, outputs)]
    result = {'id': problem_str, 'url': url, 'sample_io': in_and_out}
    return json.dumps(result, indent=2)   # indent for pretty printing


if __name__ == '__main__':
    s = input().strip()
    js = extract_samples(s, is_contest=True)
    print('...saving sample input and output as {}_*.*'.format(s))
    save_samples(js)
