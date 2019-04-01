This project gives the developer CLI tools to generate code. It will generate the view/service/repository/model structure for your project, including dependency injection. After fixing your container import, it will make your CRUD operations available straight away.

After installation, add a file `lagen.ini` with the following contents:

```
[lagen]
root = myproject
```


Currently, it requires you to use the `dependency_injector` package on top of Pyramid and SQLAlchemy.
The structure of your project has to be at least the following:

```
myfolder/
  
  myproject/
    
    model[s]/
    
    view[s]/
    
    repositor[y/ies]/
    
    service[s]/
    
    container[s]/
  
  route[s]
```

Otherwise it will not be able to find files. Your folder names can be plural or singular, that does not matter.


The command is: `lagen`
Optional commands are:
    `model`
    `view`
    `service`
    `repository`
    
or create them all by writing `scaffold`


Creating a service or a repository will create a file `base.py` with basic functions, only if it does not exist yet.
Creating these folders will also search for a file in `containers.py` with a name that indicates a repository or a service. It will append the container to this file, however it will not be able to import your repository/service as of right now. So you have to manually import these still.


Creating a view will append routes to your `routes.py` file.


Creating a model creates an empty husk. This is due to your models requiring largely custom code.

