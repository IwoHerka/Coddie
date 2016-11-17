# Coddie: An Interpreter for Extended Relational Algebra

Inspired by the simplicity and elegance of both the Scheme programming language, and the relational algebra formal system, Coddie is an interpreter with Lisp-like syntax that presents in a succint way a tool to study and explore relational algebra, as defined by E.F. Codd in his famous paper *A relational Model of Data for Large Shared Data Banks*, but extended in order to provite lighweight manipulation of data and data presentation.

This report describes the development and usage of Coddie. Coddie alows the user to define relations, to query them, and display them in appropiate forms. Now follows a description of  some examples of Coddie's capabilities.

**Example Queries:**

```scheme
(insert            
		(create rel (STRING INTEGER) (name year))
		("Philip Flajolet" 1934))

(display 
	(project 
		(project employee (name salary)) 
		(name)))

(display 
	(union 
		(project 
			(project managers (number surname)) 
			(number)) 
		(project graduates (number))))

(select 
	relation 
	(and (= name "Donald") (<= age 45) 
		(or 
			(= religion "muslim") 
			(<> lastname "Curry")
)))
```

### Coddie as Language for Data Modeling

Coddie is the combination of two very different parts, the first one, is the REPL, that provides an interface for interaction with the user; it offers a bridge between the relations, and the queries by the user. The second part, is the data modeling part, which allows definition of data, noth the structure and contents of relations, the former, can be done in the REPL, and in coddie files. Here is a description of both.

#### Coddie REPL

`REPL.py`

```
$ unix_workstation python Coddie/REPL.py

-----------	|	CODDIE - An Interpreter for Extended Relational Algebra
\         /	|	
 \       /	|	Documentation https://github.com/scvalencia/Coddie
  =======       |	Type "(help)" for help.
 /       \	|	
/         \	|	
-----------	|	Version 0.1.1 (2016-04-17)

>>>

```

Once the REPL is ready, it's possible to begin playing with the interactive relational algebra interpreter. The most basic operations to perfom, is to load a model that's properly described in a `codd` file. A file of this kind, has the description (mandatory) and the content (optional) of each relation. The description have both the attributes of a relation and its datatypes. The following file `model.codd`, describes two relations and the way to define them and populate them if needed. `codd` files, at the moment, are the only way to persist a querying session with the interpreter.

```sql
RELATION employee {
	nr : INTEGER
	name : STRING
	salary : INTEGER
}

INSERT (1, "John", 100) INTO employee

RELATION turingaward {
	firstname : STRING
	lastname : STRING
	year : INTEGER
	motivation : STRING
}

-- INSERT () INTO TuringAward
-- INSERT (1, 2, 3, 4) INTO TuringAward

INSERT ("Alan", "Perlis", 1966, "Compiler, construction") INTO turingaward
INSERT ("Alan", "Perlis", 1966, "Compiler, construction and, contributions") INTO turingaward

INSERT ("Maurice", "Wilkes", 1967, "Computer design and APIs") INTO turingaward
INSERT ("Richard", "Hamming", 1968, "Numerical methods and error correcting codes") INTO turingaward
INSERT ("Marvin", "Minsky", 1969, "AI research") INTO turingaward
INSERT ("James", "Wilkinson", 1970, "Numerical analysis in computation") INTO turingaward
INSERT ("John", "McCarthy", 1971, "AI research and LISP") INTO turingaward
INSERT ("Edsger", "Dijkstra", 1972, "Development of ALGOL, and the art of programming") INTO turingaward
```

This `codd` file, defines a relation called `employee` (relations should be named in lowercase letters), whose attributes are `nr`, `name`, `salary`, with types `INTEGER`, `STRING`, `INTEGER` each. the attributes must be in lowercase letters, while the types must be written in uppercase letter. The command `INSERT (1, "John", 100) INTO employee`, inserts the given tuple to the specific relation. Any mismatch of the arity of syntax violation, will be reported by the REPL.

The way to load relations defined in `codd` files to the enviroment, and the response of the REPL is:

```
>>> (fetch "src/relations/model.codd")

Loaded relation: employee
Loaded relation: turingaward
```

Now, the enviroment contains both relations. The command `env`, serves as a way to visualize the current collection of relations that can be queried.

```
>>> (env)

employee(nr:integer, name:string, salary:integer)
turingaward(firstname:string, lastname:string, year:integer, motivation:string)
```

In order to display the current state of a relation within the enviroment, there exist the `display` command, that receives an expression that evaluates to a relation (the name of a relation, or a pure query that itself evaluates to a relation).

```
>>> (display employee)

+------+--------+----------+
|   nr | name   |   salary |
+======+========+==========+
|    1 | "John" |      100 |
+------+--------+----------+
```

Tuple insertion to an specific relation, is done by using the `insert` command, which takes an expression that evaluates to a relation, and a tuple. For succesfull operation, it's needded the types to be the correct ones, and the first argument must evaluate to a relation.

```
>>> (insert employee (2 "Hillary" 100))
>>> (display employee)

+------+-----------+----------+
|   nr | name      |   salary |
+======+===========+==========+
|    2 | "Hillary" |      100 |
+------+-----------+----------+
|    1 | "John"    |      100 |
+------+-----------+----------+
```

Besides of applying the `fetch` operation on the correct arguments, a relation can be created directly (without the use of relational operators). The `create` command, takes as argument a name denoting the name of the new relation, a tuple of types, and a tuple of named attributes. It adds to the enviroment the new relation. The `create` command, evaluates itself to the created relation.

```
>>> (insert            
        (create rel (STRING INTEGER) (name year))
        ("Philip Flajolet" 1934))			
>>> (env)

rel(name:string, year:integer)

>>> (display rel)

+-------------------+--------+
| name              |   year |
+===================+========+
| "Philip Flajolet" |   1934 |
+-------------------+--------+
```




$$\sigma_{(firstname\ =\ "Pepito")\ \wedge\ (year\ \leq\ 45)\ \wedge\ ((motivation\ =\ "muslim")\ \vee\ (lastname\ \neq\ "Knuth"))}\ (turingaward)$$