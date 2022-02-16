# Notas

## Sobre Clases

## Makefile

## Pytest

What is Pytest?
pytest is framework that makes buildin simple and scalable test esay.

**¿Qué es un framework?**
    
    Un framework es un esquema o marco de trabajo que ofrece una estructura base para elaborar un proyecto con objetivos específicos, una especie de plantilla que sirve como punto de partida para la organización y desarrollo de software.
Ver más [aquí](https://docs.pytest.org/en/6.2.x/usage.html)

In general, pytest is invoked with the command pytest (see below for other ways to invoke pytest). This will execute all tests in all files whose names follow the form test_*.py or \*_test.py in the current directory and its subdirectories. More generally, pytest follows standard test discovery rules.

## pytest commands

[Ver esto](https://programmerclick.com/article/3366908761/)

**Uso básico**

    py.test [options] [file_or_dir] [file_or_dir] [...]

_____
pyest is for runnin test
mypy for check type hints
flake8 for cehcking style

src: "source" 

En el minuto 14:00 habla sobre 'fixture' -no me queda claro que es un fixture
ni el scope

tox: otra herramienta de testing

FitHub actiosn corre tox automáticamente

____
## Mutantes

[Mutation testing](https://searchitoperations.techtarget.com/definition/mutation-testing#:~:text=Mutation%20testing%2C%20also%20known%20as,cause%20errors%20in%20the%20program.)

- ¿Qué son los mutantes?

- ¿Cómo los cazamos?

- ¿Por qué son importantes?






Mutation testing, also known as code mutation testing, is a form of white box testing in which testers change specific components of an application's source code to ensure a software test suite will be able to detect the changes. Changes introduced to the software are intended to cause errors in the program. Mutation testing is directed to ensure the quality of a software testing suite, not the applications the suite will go on to test.

**Unit Test:** 
> UNIT TESTING is a type of software testing where individual units or components of a software are tested. The purpose is to validate that each unit of the software code performs as expected. Unit Testing is done during the development (coding phase) of an application by the developers


____

## Radian

Ver [esto](https://github.com/REditorSupport/vscode-R/wiki/Installation%3A-Windows)
 y [esto](https://www.infoworld.com/article/3625488/how-to-run-r-in-visual-studio-code.html)

radian version: 0.5.13
r executable: C:\Program Files\R\R-4.1.2\bin\R
r version: 4.1.2
python executable: C:\Users\Fernando\anaconda3\python.exe
python version: 3.9.7

To locate the path to radian.exe, run the following command:

> where.exe radian