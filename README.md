# <img src="https://cloud.githubusercontent.com/assets/7833470/10899314/63829980-8188-11e5-8cdd-4ded5bcb6e36.png" height="60"> Python Unit Testing

[![Build Status](https://travis-ci.org/justincastilla/python-unit-testing.svg?branch=master)](https://travis-ci.org/justincastilla/python-unit-testing)

## Unit tests
Tests can be broadly split into two categories: **Unit Tests** and **Integration Tests**. Both are important.

In **Unit Tests**, which we'll talk about today, we try to isolate each component (or class/function) and test it on its own. We separate our Controllers from our Views and test the boundary of its interface.
**Unit tests** tend to run faster because we're testing small components. By isolatign components from each other to test them we're forced to write better object-oriented code. The functionality can't blur across several modules without us having to do a lot of work in the test to stub that out.

## Integration Tests
In **Integration Tests** we combine components together, sometimes just a few and other times the entire system. In Django, integration tests often drive the server and test the entirety of the system--the full request response cycle. These tests tend to take much longer to run. They test the cohesion of components and that the interface between them is behaving as we expect.

Both types of tests are important. There are also other types but they can generally be broken down into finer grained versions of the above. Together the Unit and Integration tests you write become part of your test suite.

## How are tests used in industry?

Many companies require that all the code they develop comes with tests. Often before code can be depoloyed, or merged into master, the entire test suite is run and all tests must pass.

## Continuous Integration 

We will be using a *continuous integration service* called [**Travis CI**](https://travis-ci.org/) to ensure the code we push to github passes our tests.  This will ensure that our code passes all of the tests we assign it as we continue to develop. We can tell Travis to run the tests when we create pull requests or whenever we push code to a specific branch.  

### Prerequisites
To start using **Travis CI**, make sure you have:

- A GitHub account.
- Owner permissions for a project hosted on GitHub.


### To get started with **Travis CI**
1. Go to Travis-ci.com and Sign up with GitHub.
2. Accept the Authorization of **Travis CI**. You’ll be redirected to GitHub.
3. Click the green Activate button, and select the repositories you want to use with **Travis CI**.
4. Add a `.travis.yml` file to your repository to tell **Travis CI** what to do. The following example specifies a Python project that should be built with Python 3.7-dev.


```yml
language: python
python:
 - "3.6.4"
 - "3.6.5"
 - "3.7-dev
 ```


5. Add the `.travis.yml` file to git, commit and push, to trigger a **Travis CI** build:
> Travis only runs builds on the commits you push after you’ve added a `.travis.yml` file.

6. Check the build status page to see if your build passes or fails, according to the return status of the build command by visiting **Travis CI** .com build status and selecting your repository.
