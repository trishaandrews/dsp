# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

[![Think Python](img/think_python.png)](http://www.greenteapress.com/thinkpython/)

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

Complete the following exercises to check your ability with Python.

These exercises are implemented with doctests, which are runnable tests inside docstrings. Fill in the function definitions. Correct solutions will make it possible to run (for example) `python -m doctest strings.py` with no messages about failures.

 * [Strings](python/strings.py)
 * [Lists](python/lists.py)


---

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

> Both lists and tuples store multiple values in indexed positions. However, lists are mutable while tuples are not. This means that you can change, add, and remove items in a list, but not in a tuple. Tuples can contain heterogeneous data, and are often used for constant data that should be structured, such as (x, y, z) location data. It wouldn't make sense to modify one of those values, since that would change the whole location. However, it would make sense to have a list of tuples, such as all the locations you visited over vacation. Because they are immutable, tuples can be used as keys in dictionaries so long as the data they contain is also immutable. 

---


---

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

> Python sets hold unordered, hashable data with no duplicates. Sets are unindexed, but can support mathematical set operations such as union and intersection. If you had a list of fruit you just bought, it could be `["banana", "orange", "banana", "kiwi"]`, but if you made a set of that list it would turn into `set(["banana", "orange", "kiwi"])` with the duplicate `"banana"` entry removed. You could then compare the set of fruit you just bought to the set of fruit you like, say `set(["kiwi", "apple", "banana"])` and perform mathematical set operations such as that `"kiwi"` and `"banana"` are in both lists. Performance for finding an element is much better in a set than in a list. For finding an element in a list, a comparison must be made with every item in the list for equality, which is O(n), however since items in sets are stored in a hashtable, it is possible to get x in s as O(1).
---


---

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

> Python's lambda keyword is used as a way to create small, anonymous functions. These functions can then be easily passed into other functions. Lambda functions can be used in functions like `filter` or `sorted`. For example, if you wanted to sort a list of tuples `ul = [(1,"C",2),(3,"A",5),(4,"B",3)]` by the second element, then you could use the sorted function as follows:

```python
sorted_list = sorted(ul, key=lambda tup: tup[1])
```
---


---

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

> List compressions are a way to create new lists by applying operations to the members of another list, sequence, or iterable. For example, if you wanted to create a list of the squares of the numbers 0-9, the result, `[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]` could be created from either the list compression `squares = [x**2 for x in range(10)]` or `squares = map(lambda x: x**2, range(10))`. In this case, the list compression is simpler and easier to read than the `map` operation. 
> If you want only some squares from the squares list, you can use the `filter` function or further list commpressions to select only the squares, say, greater than 1 and less than 40. We could get the result, `[4, 9, 16, 25, 36]`, by performing either `small_squares = filter(lambda x: x > 1 and x < 40, squares)` or the list compression `small_squares = [x**1 for x in range(10) if x**2 > 1 and x**2 < 40]`. The filter case starts with the already created squares list, while the list compressions can do both operations in one line. 
> If we wanted a set of squares from the numbers 0-9 instead of a list, we could generate it with a set compression. It would be `squares = {x**2 for x in range(10)}`.
> Finally, if we wanted a dictionary of the numbers 0-9 mapped to their squares, we could create that with a dictionary compression. It would be `squares = {x:x**2 for x in range(10)}`.

---


Write a Markov text generator, [markov.py](python/markov.py). Your program should be called from the command line with two arguments: the name of a file containing text to read, and the number of words to generate. For example, if `chains.txt` contains the short story by Frigyes Karinthy, we could run:

```bash
./markov.py chains.txt 40
```

A possible output would be:

> show himself once more than the universe and what I often catch myself playing our well-connected game went on. Our friend was absolutely correct: nobody from the group needed this way. We never been as the Earth has the network of eternity.

There are design choices to make; feel free to experiment and shape the program as you see fit. Jeff Atwood's [Markov and You](http://blog.codinghorror.com/markov-and-you/) is a fun place to get started learning about what you're trying to make.