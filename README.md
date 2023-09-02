# Northcoders Data Engineering Katas

Fork this repository to your own GitHub account because you will be pushing your own solutions to it.

Clone your fork of this repository to your local machine and `cd` into it:

```sh
$ git clone "your fork's URL"

$ cd de-py-katas
```

We are going to use the `make` command to perform some of the standard tasks for this repo. We'll cover `make` in more detail later in the course.

The first task is to set up your **virtual environment**.

Run this command in a terminal:
```bash
make create-environment
```

You should see the `venv` directory appear within the project folder.

Using `make` as described below wil mean you don't have to activate your environment.

After creating your virtual environment, we can install `pytest` by running:
```bash
make pytest
```

The `pytest` library will be used for unit tests. Additionally, there will be `flake8` checks to make sure for PEP8 compliance in the later katas, this will be checked via `make`. 

In the terminal, navigate to the root directory of the project, and run:

```
make flake
```

Then, you can use the command below to run your all tests and check for PEP8 compliance:

```
make run-checks
```

Work on the katas and commit changes as needed. When you are happy with your solution, push all your changes to your forked repo. You should push to your fork frequently but as a bare minimum please make sure it's up to date with last week's kata solutions before Monday morning each week:

```sh
$ git push origin main
```

---

## Instructions

This repo is a series of katas to practice your problem solving skills, there is a recommended running order below. There are more katas here than we expect you to complete but have provided extras for you to use as practice once you finish the course to help keep your skills sharp.

**Please start by reading the** `first_python_kata` **and completing** `sentence_to_camel_case`.

---

### Suggested Running Order:

1. sentence_to_camel_case✅🌡
2. get_distinct_letters✅🌡
3. get_frequencies✅🌡
4. create_counter✅🌡
5. lengthen_date✅🌡
6. get_century✅🌡
7. years_of_growth✅🌡
8. herd_the_babies✅🌡
9. sum_ascii✅🌡🔒
10. bubble_sort✅🌡🔒
11. extract_domain_name✅🌡🔒
12. caesar_cipher✅🌡🔒
13. roman_numeral_encoder✅🌡🔒
14. alphabet_position✅🌡🔒
15. count_bits✅🌡
16. digital_root
17. fill_square✅🌡
18. detect_pangram
19. morse_code✅🌡🔒
20. multiplication_table & (mod Z version)
21. reduce_by_steps✅🌡🔒8️⃣
22. find_partner
23. find_most_repeated
24. vowel_shift
25. alternating_split
26. crack_code✅🌡🔒8️⃣
27. binary_search
28. calculate_binary_score
29. justify_line
30. find_the_needle
31. validate_suduko
32. strange_sort
33. gdpr_mask✅🌡 8️⃣
34. sudoku_solver

---

## How to go about writing tests
There is no set way to write tests, each problem you face is unique and you will have to approach it with an open mind.  There are however some guidelines you can follow to give you more confidence that your tests are thorough. The following is a list of things to consider when writing tests:

- **Test the smallest units of functionality**. Write tests for each function or method. If a function calls another function you want to test them separately. This will make it easier to debug when something goes wrong.
- **Test the happy path first**. Write tests for the expected behaviour of your code. This will help you to make sure that your code is working as expected.  If a function is supposed to return a list, write a test that checks that it returns a list. If a function is supposed to take a string and a number as inputs, give the function a string and a number in your happy path tests.
- **Think about the problem outside of code to create test cases**. Programming is a tool we use to solve problems in the 'real world'. Think about how you would solve the problem without writing code (with a pen and paper).  What types of inputs could you get?  If it is a string, does it matter if it is empty, if letters are capitalised, if there are white spaces, numbers, special characters?  If it is a number, what happens if it is a float, a negative number, a very large number? If you think that these cases might be important, write tests for each of them. If you have multiple inputs, think about how different combinations of inputs might affect the output, and then write tests for each of these cases.
- **Organise your tests in a structured way**. You might be able to write simple tests in a single line and still have them be readable.  With more complex tests you might want to very obviously structure them in a 'arrange', 'act', 'assert' format.  You may even want to write comments to explain what parts of a test are doing if you think it would not be immediately obvious to someone else reading your code.  When you find a way that works for you, stick to it and keep it consistent throughout your testing.
- **Organise your test files in a structured way**. Test files can get large so organising your tests in a logical order can help someone else understand what is going on. Keep happy path tests together, and errors together etc. If your function has multiple inputs keep the tests that are testing the first input together.  You might want to use comments to separate different sections of your tests.
- **You can have multiple assert statements in a single test**. If you have a function that returns a list, you can write a test that asserts that the list has the correct length, and then another assert statement that checks that the list contains the correct values.  This can make your tests more readable and easier to debug rather than having a separate test for each assert statement.
- **What do you want to happen when things go wrong (the sad path)**?  If you give a function an input that it is not expecting, what should happen?  Should it throw an error?  Should it return a default value?  Should it return a string saying "woops something isn't quite right"? For these katas we want to focus on the happy path, but it is worth thinking about what you want to happen when things go wrong.  If you want to write tests for the sad path, decide what **you** want to happen... and then test for it!

Happy testing!