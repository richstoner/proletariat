#### Proletariat 

Rich Stoner, 2014

*A simple execution environment that sits on top of girder + ipython + celery + magic.*

<hr><br>

### Magic?

What is this? 

This is an arbitrary task with hooks into girder, that you can write in ipython, that can be run asynchronously via celery and managed in flower. After installing the items in this repo to their respective locations, you should be able to run any ipython notebook cell as a celery task by simply adding `%%girder` to the beginning of the cell. 

![Client](https://raw.githubusercontent.com/richstoner/proletariat/master/screenshots/girder_on_celery.jpg)

This uses a custom ipython magic command to handle the imports and redirect the cell contents to a running celery worker. Unfortunately, we're only able to return the task id. 



<br><br>


### How to use

1. Prototype code in ipython, directly accessing girder models.

2. With a bit of magic, run the same code on a celery queue

3. Add hooks and run the scripts from the interface (ala romanesco without the typing)

### Direct girder access


**Thanks to some intelligent path settings, we can import the girder module directly, enabling us to access models with ease.**

![Client](https://raw.githubusercontent.com/richstoner/proletariat/master/screenshots/direct.jpg)

<br><br>

### Using the girder python client  

**We can also use the prebuilt girder client as a way to abstract out the commands.**

![Client](https://raw.githubusercontent.com/richstoner/proletariat/master/screenshots/client.jpg)


<br><br>

### What is required to make it work?

1. Custom ipython notebook configuration with appropriate imports

2. Custom ipython notebook magic, to re-route commands to celery

3. A generalized execute celery execute task

4. A lightweight girder plugin to call the task from post data

<br><br>

### Install

Currently, proletariat has heavy dependencies on my application hosting framework (Simple application Framework) and Kitware's girder. For more information, please visit:

1. [https://github.com/richstoner/simple-application-framework](https://github.com/richstoner/simple-application-framework)

2. [https://github.com/richstoner/girder](https://github.com/richstoner/girder)


<br><br>

### Mangement via supervisor helps:

![Client](https://raw.githubusercontent.com/richstoner/proletariat/master/screenshots/supervisor.jpg)


<hr>

Side note: Kitware has put together something similar that integrates with Girder. It's called Romanesco ([http://romanesco.readthedocs.org/en/latest/](http://romanesco.readthedocs.org/en/latest/)) and operates similar to my approach, but uses a bit strong typing and integration with girder. It is an integral part of their Tangelo platform: [http://tangelo.kitware.com/](http://tangelo.kitware.com/) & [https://github.com/tangelo-hub](https://github.com/tangelo-hub).






