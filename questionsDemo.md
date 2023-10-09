**What does the term debugging refers to?** It refers to the process of fixing a program that already shows a malfunctioning signal
**What does the term debuggin refers to?** It refers to the process of running a program to try and ascertain whether or not it works as intended.
**What would be a good way of making a program easier to test and debug?** This could be accomplish by breaking the program up into separate components that can be implemented, tested and debugged independently of other components.
**Does testing prove the absence of bugs?** No, it only proves its presence.
**What is a test suit?** A collection of inputs that has a high likelyhood of revealing bugs, yet does not take too long to run.
**What happens on black-box testing?** The tester ignores the structure/design/implementation of the item being tested.
**What are some rules of thumb when it comes to glass-box testing?** ( 1 ) Exercise both branches of all if statements ( 2 ) Make sure that each except clause is executed ( 3 ) in for and while loops verify situations where the body is enter once, more than once, or other possible cases ( 4 ) for recurvise functions, check the base and recursive cases
**How are conductes tests usually?** Tests usually are conducted in two fases; starting with ( 1 ) unit testing ( 2 ) integration testing
**How can be bugs categorized?** They can be categorized into two dimensions; ( 1 ) Overt > Covert ( 2 ) Persistent intermittent
**How is the Overt > Covert category of bugs?** This category refers to how the program manifests the problem. While overt bugs make the program crash or take forever to run, covert bugs has no obvious manifestation of any anomaly.
**How is the Persisten > Intermittent category of bugs?** This category refers to the frequency of the bug's occurrence. While persistent means that every time the program is run with the same inputs the same error happens, intermittent bugs show up only  some of the time, even though the same input has been used.
**What are the best kind of bugs to have?** Overt and persistent. Good programmers try to write their programs in such a way that programming mistakes lead to bugs with such properties.

---

# Reading 6

**Testing**: The process of running a program to try and ascertain whether or not it words as intended.

**Debugging**: The process of trying to fix a program that you already know does not work as intended.

> Good programmers design their programs in ways that make them easier to test and debug. The key to doing this is breaking the program up into separate components that can be implemented, tested and debugged independently of other componentes

## Testing

> Program testing can be used to show the presence of bugs, but never to show their absence!

> No amount of experimentation can ever prove me right; a single experiment can prove me wrong.

**Test Suite**: a collection of inputs that has a high likelyhood of revealing bugs, yet does not take too long to run. The key to doing this in partitioning the space of all possible inputs into subsets that provide equivalent information aobut the correctness of the progam, and then constructing a test suit that contains at least one pinput from each partition.

## Black-box Testing
**Black-box testing**: The internal structure/design/implementation of the item being tested is not known to the tester. Only the external design and structure is tested.

- Tests need not be changed when the implementation changes

## Glass-box Testing

**White-box testing (also called Glass-box testing)**: The internal structure/design/implementation of the item being tested is known to the tester. Implementation and impact of the code are tested. 

- A glass-box test suite is **path-complete** if it exercises every potential path through the program.

Despite the limitations of glass-box testing, there are a few rules of thumb that are usually worth following:
- Exercise both branches of all if statements
- make sure that each except clause is executed
- For each for loop, have test cases in which:
    - The loop is not entered (e.g., if the loop is iterating over the elements of a list, maek sure that it its tested on the empty lists)
    - The body of the loop is executed exactly once
    - the body of the loop is executed more than once
- For each while loop:
    - Look at the same kinds of casaes as when dealing with for loops
    - Include tests cases corresoponding to all possible ways of exiting the loop
- For recursive functions, include tests cases that cause the function to return with no recursive calls, exactly one recursive call and more than one recurvise call. 

## Conducting Tests

Testing is often thought of as occuring in two phrases. 
One should always start with **unit testing**, during which testers construct and run tests design to ascertain whether individual units of code (e.g., functions or classes) work properly.
This is followed by **Integration testing**, which is designed to asceretain whether the program as a while behaves as intended.

In practice, testers cycle through these two phrases, since failures during integration testing lead to making changes to individual units.

Integrantion testing is almost always more challenging than unit testing. One reason for this is that the intended behaviour of an entire program is often considerably harder to characterize than the intended behaviour of each of its parts. 

In industry, testing process is highly automated, test drivers autonomously:
- Set up the environment needed to invoke the program (or  unit) to be tested
- Invoke the program (or unit) to be tested with a predefined or automatically generated sequence of inputs
- Save the results of these invocations
- Check the acceptability of the results of the tests
- Prepare an appropiate report

During unit testing, we often need to build **stubs** as well as **drivers**.

### Stubs

**Stubs**: simulate parts of the program that use the unit being tested.

These are useful because they allow people to test units that depend upon software or sometimes even hardware that does not yet exist. This allows teams of programmers to simultaneously develop and test multiple parts of a system.

Ideally, a stub should:
- Check the reasonableness of the environment and arguments supplied by the caller (calling a function with inappropriate arguments is a common error)
- Modify arguments and global variables in a manners consistent with the specification
- Return values consistent with the specification

**Whenever any change is made, no matter how small, you should check that the program still passes all of the tests that it used to pass**


**Drivers**: simulate the parts of the program that use the unit being tested


Automating the testing process facilitates regresion testing, which is the process of testing the system all over again given that it is common when something is fixed, it breaks something else that used to work.

## Debugging

> If your program has a bug, it is because you put it there. Bugs do not breed in progams.

Runtime Bugs can be categorized along two dimensions
- Overt > Covert: overt bug manifests as the program crashes or takes far longer (maybe forever ) to run than it should. Whereas covert bug has no obvious manifestation.
- Persistent > Intermittent: A persistent bug occurs every time the program is run with the same inputs. An intermitent bug occurs only some of the time, even when the program is run on the same inputs and seemingly under the same conditions.

**Overt**: Done os shown publicly or in an obvious way and not secret

**Covert**: Hidden or secret

> The best kind of bugs to have are overt and persistent. Good programmers try to write their programs in such a way that programming mistakes lead to bugs that are both overt and persistent. This is often called defensive progamming.

> Think of debugging as a search process, and each experiment as an attempt to reduce the size of the search space.

## Advice on Debugging;
- Look for the usual suspects: 
    - Passed araguments to a function in the wrong order
    - Misspelled a name
    - Failed to reinitialize a variable
    - Tested that two floating point numbers are equal instead of nearly equal
    - Tested for value equality when you menat object equality
- Ask yourself why it is doing what it is.
- One practical way to go about deciding where to look is asking where the bug cannot be
- Try to explain the problem to somebody else
- Don't believe everything you read, the code may not be doing what the comments suggest.
- Stop Debugging and start writing documentation
- Walk away, try again tomorrow

### After finding the bug

- ASk yourself if this bug explains all the observed symptoms, or whether it is jus the tip of the iceberg.
- Before making any change, try and understand the ramification of the proposed fix. Does it break something else? does it introduce excessive complexity? Does it offer the opportunity to tidy up other parts of the code?
- Always make sure that you can get back to where you are
- Maybe you be better off thinking about whether there is some better way to organize your program or some simpler algorithm that will be easier to implement correctly.

# Reading 7


**Exception**: 

- Exceptions, when raised, can and should be handled by the program
- A programmer can and should anticipate exceptions
-

**Polymorphism**: means to have many forms. In programming meanss the same function name being used for different types.

- Exceptions alert the userof the program to the fact that something troublesome has happened. It gives someone debugging the program a clear indication of where things went awry.


## Assertions

The Python assert statement provides programmers with a simple way to confirm that the state of a computation is as expected. An assert statement can take one of two forms:

> Assert Boolean Expression
or
> Assert Boolean expression, argument

Assertions are a useful defensive programming tool. They can be used to confirm that the arguments to a function are of appropriate types. They are also a useful debugging tool, as can be used to confirm the intermediate values have the expected values or that a function return an acceptable value.


# Lecture


Defensive progamming:
- Write specifications for functions
- Modularize programs
- Check conditions on inputs/outputs (assertions)

**Classses of tests**:

- Unit Testing:
    - Validate each piece of program
    - Testing each funcdtion separately
- Regression Testing
    - Add test for bugs as you find them
    - Catch reintroduced errors that were previously fixed
- Integration Testing
    - Does overall program work?
    - Tent to rush to do this


**Black box testing**: Testing through specification
- Can be done without looking at the code
- Can be done by someone other than the implementer to avoid some implementer biases
- TEsting can be reused if implementation changes
 
**Glass box testing**: Testing through code
- Use code directly to guide design of test cases
- Called path complete if every potential paath through code is tested at least once
- What are some drawbacks of this type of testing?
    - Can go through loops arbitrarily many times
    - Missing paths
- **Guidelines**:
    - Branches: exercise all parts of a conditional
    - For loops: Loop not entered, body of the loop executed exactly once and body of the loop executed more than once
    - While loops: same as for loops, cases that catch all ways of exiting loop

## Debugging

- Steep learning curve
- Goals is to have a bug-free program
- Tools
    - Built in IDLE and Anaconda
    - Python Tutor
    - print statement
    - Use yoru brain, be **systematic** in your hunt. 


### print Statements

- Good way to test hypothesis
- When to print?
    - Entering a function
    - Parameters
    - Function results
- Use **bisection method**:
    - Put a print half way in code
    - Decide where bug may be depending on values

### Debugging steps

- Study the progam  code
    - don't ask what is wrong
    - ask how did I get the unexpected result
    - Is it part of a family?
- Scientific method
    - Study available data
    - Form hypothesis
    - Repeatable experiments
    - Pick simplest input to test with

### Logic Errors

- Think before writing new code
- Draw pictures, take a break
- Explain the to someone else, or a rubber ducky.

### Do's and Dont's

#### Do not

- Write entire program
- Test entire program
- Debug entire program
- Change code
- Remember where the bug was
- Test code
- Forget where bug was or what change you made
- Panic

#### Do
- Write a function
- Test the function, debug the function
- Write a function
- Test the function, debug the function
- Do integration testing
- Backup code
- Write down potential bug in a comment
- Test Code compare new version with old version


## Exceptions

else: Body of this is executed when execution of associated try body completes with no exceptions

finally: body of this is always executed after try, else and except clauses, even if they raise another error or executed a break, continue or return.

- Useful for clean-up code that should be run no matter what else happened (e.g, closing a file)


### What to do with exceptions?

- Fail silently:
    - Substitute default values or just continue (Bad idea, user gets no warning)
- Return an 'error' value: What value to choose? (complicates code having to check for a special value)
- Stop execution, signal error condition: In python raise and exception
> raise Exception("Descriptive string")

## Assertions

- Want to be sure that assumptions on state of computation are as expected
- Use an assert statement to raise and AssertionError exceptioni if assumptions are not met
- an example of good defensive programming
-

### Assertions as defensive programming

- Assertions don't allow a programmer to control response to unexpected conditions
- Ensure that execution halts whenever and expected condition is not met
- Typically used to check inputs to functions, but can be used anywhere
- Can be used to check outputs of a function to avoid propagating bad values
- Can make it easier to locate a source of a bug

### Where to use assertions?

- Goals is to spot bugs as soon as introduced and make clear where they happened .
- Use as a supplement to testing
- Raise exceptions if users supplies bad data input
- Use assertions to:
    - Check types of arguments or values
    - Check that invariants on data structures are met
    - Check constraints on returns values
    - Check for violations of constraints on procedure (e.g., no duplicates in a list)

