# Practice Code Challenge Theater Work 

## Learning Goals

- Classes and Instances
- Class and Instance Methods
- Variable Scope
- Object Relationships
- lists and list Methods

## Introduction

The Flatiron Theater Company is holding Auditions!

An actor may only `Audition` for one `Role`, while a `Role` may have many `Auditions` for it! 

![one to many](https://curriculum-content.s3.amazonaws.com/phase-3/active-record-theater-work/one_to_many.png)

## Getting started 

To get started, run `pipenv install` while inside of this directory.

## Instructions

Build out all of the methods listed in the deliverables. The methods are listed in a suggested order, but you can feel free to tackle the ones you think are
easiest. Be careful: some of the later methods rely on earlier ones.

You'll need to create your own sample instances so that you can try out your
code on your own. Make sure your relationships and methods work in the console.

We've provided you with a tool that you can use to test your code. To use it,
run `python debug.py` from the command line. This will start a `ipdb` session
with your classes defined. You can test out the methods that you write here. You can add code to the `debug.py` file to define variables and create sample
instances of your objects.

Writing error-free code is more important than completing all of the
deliverables listed - prioritize writing methods that work over writing more
methods that don't work. You should test your code in the console as you write.

Similarly, messy code that works is better than clean code that doesn't. First, prioritize getting things working. Then, if there is time at the end, refactor your code to adhere to best practices. When you encounter duplicated logic, extract it into a shared helper method.

## Deliverables

Write the following methods in the classes in the files provided. Feel free to
build out any helper methods if needed.

### Initializers and Properties

#### Role

- `Role __init__(self, character_name)`
    - 'Role' is initialized with a character_name (string).
    - Character_name **can be** changed after the `Role` is initialized.
- `Role property character_name()`
    - Returns the `Role`'s character_name.
    - Character_name's must be strings greater than 0 characters.
    - `raise Exception` if validation fails
- `Role class attribute all`
    - Returns a list of all roles.

#### Audition

- `Audition __init__(self, role, actor, location, phone)`
    - `Audition` is initialized with a `Role` instance, and a
    - actor (string)
    - location (string)
    - phone (string)
    - hired (boolean) which defaults to False
- `Audition property actor()`
    - Returns the actor for the `Audition` instance
    - Actor must be a string between 3 and 20 characters.
    - `raise Exception` if validation fails
- `Audition class attribute all`
    - Returns a list of all auditions
  
### Object Relationship Attributes and Properties

#### Audition

- `Audition role` returns an instance of role associated with this audition
- `Audition call_back()` will change the the hired attribute to `True`

#### Roles

- `Role auditions(self)` returns all of the auditions associated with this role 
- `Role actors(self)` returns an list of names from the actors associated with this role
- `Role locations(self)` returns an list of locations from the auditions associated with this role

### Aggregate and Association Methods

#### Role

- `Role lead(self)` returns the first instance of the audition that was hired for this role or returns a string 'no actor has been hired for this role'
- `Role understudy(self)` returns the second instance of the audition that was hired for this role or returns a string 'no actor has been hired for understudy for this role'

- `Role classmethod not_cast(cls)` returns a list of all `Role` instances for which there are no hired actors yet.
