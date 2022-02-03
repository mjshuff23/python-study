# A `module` is simply Python code in a separate file
# A `package` is the directory containing a set of modules, which is also a type of module
# `__init__.py` - is a special file that Python uses to recognize directories as containing packages
# A `submodule` is a module that is directly inside a module's folder
# A `function` is a function in a module

# project
# | README.md
# | __init__.py
# | shopping_list.py  # module
# |
# |--pet # package
# |  |
# |  |--mammal # submodule, module, and package
# |  |  | __init__.py 
# |  |  | dog.py # submodule
# |  |  | cat.py # submodule
# |  |  
# |  |--fish # submodule, module, and package
# |  |  | __init__.py 
# |  |  | salmon.py # submodule