**Proletariat**

Rich Stoner, 2014

<hr>

A simple execution environment that sits on top of girder + ipython + celery.

### 


#### How to use

1. Prototype code in ipython, directly accessing girder models.

2. With a bit of magic, run the same code on a celery queue

3. Add hooks and run the scripts from the interface (ala romanesco without the typing)


#### How does it work?

1. Custom ipython notebook configuration with appropriate imports

2. Custom ipython notebook magic, to re-route commands to celery

3. A generalized execute celery execute task

4. A lightweight girder plugin to call the task from post data


#### Install

Currently, proletariat has heavy dependencies on my application hosting framework (Simple application Framework) and Kitware's girder. 



