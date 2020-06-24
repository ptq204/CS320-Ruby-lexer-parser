# Ruby programming language  

## **Students**    
Le Bao Chau - 1651006  
Pham The Quyen - 1651029  

## **Table of contents**  
[Ruby programming language](#ruby-programming-language)
  - [Students](#students)
  - [Table of contents](#table-of-contents)
  - [1. Introduction](#1-introduction)
    - [1.1 History](#11-history)
    - [1.2 Setup and Installation](#12-setup-and-installation)
      - [1.2.1 Installation](#121-installation)
      - [1.2.2 How to run](#122-how-to-run)
    - [1.3 Ruby paradigm](#13-ruby-paradigm)
      - [1.3.1 Object-oriented programming](#131-object-oriented-programming)
      - [1.3.2 Functional programming](#132-functional-programming)
        - [lambdas](#lambdas)
        - [closures](#closures)
      - [1.3.3 Procedural programming](#133-procedural-programming)
  - [2. Syntax and Semantic](#2-syntax-and-semantic)
    - [2.1 Indentifiers](#21-indentifiers)
    - [2.2 Keywords](#22-keywords)
    - [2.3 BNF](#23-bnf)
  - [3. Examples](#3-examples)
    - [3.1 Conditional statements](#31-conditional-statements)
    - [3.2 Loops](#32-loops)
      - [3.2.1 Normal loop](#321-normal-loop)
      - [3.2.2 Process over Array](#322-process-over-array)
    - [3.3 Method](#33-method)
      - [3.3.1 Method invocation](#331-method-invocation)
      - [3.3.2 Method aliases](#332-method-aliases)
    - [3.4 Class and modules](#34-class-and-modules)
      - [3.4.1 Definining a class](#341-definining-a-class)
      - [3.4.2 Accessors and Attributes](#342-accessors-and-attributes)
      - [3.4.3 Method visibility](#343-method-visibility)
      - [3.4.4 Mixins](#344-mixins)
      - [3.4.5 Metaprogramming](#345-metaprogramming)
  - [4. Implementation](#4-implementation)
  - [5. Application](#5-application)
  - [References](#references)

## **1. Introduction**  

### **1.1 History**  

Conceived in 1993 during a talk between creator Yukihiro Matsumoto (“Matz”) and a colleague. Matz wanted a true object-oriented programming language, and created one when there wasn’t any suiting his need.
After several months writing an interpreter, Matz published Ruby 0.95 as the first public version on Japanese domestic newsgroups, already having many familiar features in later releases of Ruby.
Current latest version (until end of 2019) is 2.7.1, with a 3.0 version planned to release in 2020.  

**The name "Ruby**  
Matz chooses "Ruby" as the name for the language because it is originated from the online chat session between Matsumoto and Keiju Ishitsuka before writting any code. At first, two names are proposed: "Coral" and "Ruby". Matsumoto decided to choose the second one because "Ruby" is gemstone that represents one of his colleaguaes month of birth (July specifically).  

**Motivation for creating Ruby**   
Matz mentioned that both Perl and Python didn’t appeal to him because they weren’t a true object-oriented programming language.
He wanted a language for his needs:  
- Syntactically simple.
- Truly object-oriented.
- Having iterators and closures.
- Exception Handling.
- Garbage collection.
- Portable.  

Matz created Ruby because he wanted a new language that focuses on people, not focuses on programming. It makes people code faster, easier and feel happy while coding. This is a famous oft-quoted remark of philosophy for designing Ruby:  

> *"Ruby is designed to make programmers happy." - Yukihiro Matsumoto*  

### **1.2 Setup and Installation**  

#### **1.2.1 Installation**  

Ruby for **Windows**:
- Download an installation package from rubyinstaller.org.
- Run the resulting installer of the desired version with a single click.
- You’ll get RubyGems along with this package.
- You can run pure Ruby with the non-Devkit version, but if you need Ruby on Rails and RubyGems that requires compilation, then you’ll need the Devkit (install the MSYS2 system).  

Ruby for **Linux** and **Windows Subsystem** for Linux:
- Enable WSL: Control Panel -> Programs -> Turn Windows features on or off -> scroll down and check “Windows Subsystem for Linux” then reboot. Then you can install Linux distro from Microsoft.
- Open terminal and update Ubuntu (fetch packages then remove some needed)
- Install Ruby by package “ruby-full”  

Ruby on **Mac**: 
- There’s an interpreter built in the Mac operating system already.
- To check version: open Terminal -> type “ruby -v”.
- If the version is below 2.2.1, install Ruby Version Manager (RVM) then install Ruby.  

When finished instalment, type “irb” into command line to open Interactive Ruby Environment to start basic Ruby coding. Check gems installed by

#### **1.2.2 How to run**  
We can try Ruby code by two ways:  

- Run a Ruby code file from terminal: “ruby code.rb”
- Run small snippets of code in IRB: start typing Ruby after typing “irb” in terminal.  

### **1.3 Ruby paradigm**  
Ruby is general-purpose programming language so it supports multiple paradigms:  

#### **1.3.1** Object-oriented programming  
Ruby is pure object-oriented programming language. Every value in Ruby is an object and every object is an instance of a class, even simple numeric literals and the values `true`, `false` and `nil`. Ruby's objects are strictly encapsulated: their state can be accessed only through the methods they define.  

```rb
1.class     # Fixnum: the number 1 is a Fixnum
0.0.class   # Float: floating-point numbers have class float
true.clas   # TrueClass: true is the singleton instance of TrueClass
false.class # FalseClass
nil.clas    # NilClass
```  

Ruby supports inheritance but does not support multiple inheritance. The inheritance characteristic in Ruby is represented through Dynamic dispatch, mixins and singleton methods:  
- **Dynamic dispatch**: the mechanism that supports polymorphism. It is the way of selecting the implementation of polymorphic operations at run-time.  
- **Mixins**: mixins is a way that replaces multiple inheritance in Ruby. Simply, mixins is a set of class definition, modules, constant variables... that can be added to one or more classes to add additional functionalities without using inheritance.  

Ruby also supports `reflection` and `metaprogramming`:  
- **reflection**: also called `introspection`. That means a program can check its state and its structure, such as obtaining a list of methods defined by a class, getting the value of named instance variables, define new classes and new methods.  
- **metaprogramming**: this is an interesting and very strong feature in Ruby. With metaprogramming, we can define methods and classes during run-time like: reopen and modify classes, check if methods not exist and create them dynamically. In general, we can **make code to write code by itself** at run-time.  

More examples about object-oriented programming can be see [here](#34-class-and-modules).  

#### **1.3.2** Functional programming  

We can do functional programming in Ruby because it supports anonymous functions, lamda functions, closures and continutations.  

**lambdas**  

Blocks are syntatic structures and it can be represented as an object in Ruby. Blocks that have method-like behavior are called *lambda* and blocks that have block-like behavior are called *procs*. Both are instances of class `Proc`. In general, lambda is a function which has no name and it can be assigned to a variable for later uses.  

```rb
succ1 = lambda {|x| x + 1 }

# In ruby 1.9, lambda keyword can be replaced by '->'
succ1 = ->(x) { x + 1 }
succ1.call(2)          # return 3
```  

**closures**  

In Ruby, *procs* and *lambda* are *closures*. Closures is an object which is both invocable function and a variable binding for that function. That means, closures can bind variables used by a block. For example:  

```rb
def multiplier(n)
  lambda {|data| data.collect{|x| x*n}}
end
doubler = multiplier(2)     # Get lambda that "double" the list because we pass value 2
puts doubler.call([1,2,3])  # Prints 2,4,6
```  

Now, we want to alter the behavior of doubler. For example, binding value 3 with doubler using sepcial `eval` function.  

```rb
eval("n=3", doubler.binding)
puts doubler.call([1,2,3]) # Prints 3,6,9
```

#### **1.3.3** Procedural programming  
This paradigm is based on the concepts of procedure calls. Usually, a procedure call can be seen as a function call and function is different from a method because function can be defined outside classes. In Ruby, functions do not exist but we can create methods outside classes. Thus, Ruby does support procedural programming:  

```rb
def procedure1
  x = 2
  puts x * 3
end

def procedure2
  y = 4
  puts y * 5
end

procedure1 #=> print 6
procedure2 #=> print 20
```  

Actually, those two methods are still defined within an object: the `main` object.  


## **2. Syntax and Semantic**  

### **2.1 Indentifiers**  

- *Local variable*: A local varible name starts with `lowercase` letter, underscore followed by combination of any letters, digits and underscore. Method name has the same naming rule with local varibale's  
  ```
  abc   _abc    pi_variable     deTermination
  ```
- *Global variable*: A global varible name starts with dollar sign `$` followed by combination of any letters, digits and underscore.  
  ```
  $CONNECTION   $params     $_.     $!
  ```  
- *Constant*: A constant varible name starts with `uppercase` letter followed by combination of any letters, digits and underscore.  
  ```
  PI    Classname
  ```
- *Class varible*: A class variable name starts with `@@` followed by combination of any letters, digits and underscore.  
  ```
  @@name    @@_     @@TT
  ```
- **Instance variable*: An instance variable of a class starts with `@` followed by combination of any letters, digits and underscore.  
  ```
  @name     @_size
  ```  

In general, the regular expression of indentifiers in Ruby is:  

```rb
^(\$|\@{1,2}|[a-zA-Z_])\w*$
```  

### **2.2 Keywords**  

The following are keywords in Ruby:  

<div align="center">
    <img src="media/reserved_kw.PNG">
</div>  

Beside that, there are three tokens that are treated specially by Ruby parser when they appear at the beginning of a file: `=begin`, `=end`, `_END_`.  

In others programming language, reserved words are not allowed to be indentifiers. However, Ruby parser treats them flexibly. It allows us to use reserved words as indentifiers if we prefix them with `@`, `@@`, `$` and use them as instance, class, global variable names. Moreover, we can those reserved words as method names if the method is explicitly invoked by an object.  

### **2.3 BNF**  

```rb
PROGRAM:    : COMPSTMT
T           : ";" | "\n" # a new line can terminate a statement

COMPSTMT    : STMT {T EXPR} [T]

STMT        : undef FNAME
            | alias FNAME FNAME
            | STMT if EXPR
            | STMT while EXPR
            | STMT unless EXPR
            | STMT until EXPR
            | "BEGIN" "{" COMPSTMT "}"
            | "END" "{" COMPSTMT "}"
            | EXPR

EXPR        : EXPR and EXPR
            | EXPR or EXPR
            | not EXPR
            | ARG

ARG         : LHS = ARG
            | LHS OP_ASGN ARG
            | ARG > ARG | ARG >= ARG | ARG < ARG | ARG <= ARG
            | ARG == ARG | ARG === ARG | ARG != ARG
            | ARG + ARG | ARG - ARG | ARG * ARG | ARG / ARG
            | ARG % ARG | ARG ** ARG
            | + ARG | - ARG
            | ARG << ARG | ARG >> ARG
            | ARG && ARG | ARG || ARG
            | PRIMARY

LHS         : VARIABLE
            | PRIMARY.IDENTIFIER

OP_ASGN     : += | -= | *= | /= | %= | **=
            | &= | |= | ^= | <<= | >>=
            | &&= | ||=

PRIMARY     : "(" COMPSTMT ")"
            | VARIABLE
            | LITERAL
            | IDENTIFIER
            | if EXPR THEN
                COMPSTMT
              {elsif EXPR THEN
                COMPSTMT}
              [else
                COMPSTMT]
            | unless EXPR THEN
                COMPSTMT
              [else
                COMPSTMT]
              end
            | while EXPR DO COMPSTMT end
            | until EXPR DO COMPSTMt end

THEN        : T | then | T then
DO          : T | do | T do

FNAME       : IDENTIFIER | .. | "|" | ^ | & | <=> | == | === | =~
            | > | >= | < | <= | + | - | * | / | % | **
            | << | >> | ~ | +@ | -@ | [] | []=

VARIABLE    : VARNAME | nil | self

VARNAME     : GLOBAL | "@"IDENTIFIER | "@@"IDENTIFIER | IDENTIFIER

GLOBAL      : "$"IDENTIFIER | "$"any_char

IDENTIFIER  : /[a-zA-Z_]{a-zA-Z0-9_}/

LITERAL     : numeric | SYMBOL | STRING

SYMBOL      : :FNAME | :VARNAME

STRING      : " {any_char} "
            | ` {any_char} `
```  

## **3. Examples**  

### **3.1 Conditional statements**  

The conditional statements in Ruby has the following format:  

```rb
if expression1
  code1
elsif expression2
  code2
.
.
.
elsif expressionN
  codeN
else
  code
end
```  

As we can see, parentheses are not required. The delimiter for conditional expression are newline, semicolon or `then` keyword.  
The `end` keyword is required.  

For example:  

```rb
# newline seperator
if x < 10
  x += 1
end  

# then seperator
if x < 10 then x += 1 end

if x < 10 then
  x += 1
end

# if-else
if x == 1
  name = "one"
elsif x == 2
  name = "two"
else
  name = "many"
end
```  

In normal statement form above, the `end` keyword is required even with the single-line code. We can use `if as modifier` that use `if` keyword as delimiter and remove the `end` keyword:  

```md
*code* if *expression*
```  

For example:  

```ruby
puts message if message
```  

Note that, in Ruby everything is an expression even a statement. Therefore, a `if` statement also has a return value so we can assign value in multiway conditional like this:  

```rb
name = if x == 1 then "one"
       elsif x == 2 then "two"
       elsif x == 3 then "three"
       elsif x == 4 then "four"
       else "many"
       end
```  

### **3.2 Loops**  
#### **3.2.1 Normal loop**  
We can write simple looping statement in Ruby with a familiar syntax like in other programming languages using `while`, `until` and `for`:  

```rb
# Use while
x = 10
while x >= 0 do
  puts x
  x = x - 1
end

# Use until
x = 0
until x > 10 do
  puts x
  x = x + 1
end

# Use for
arr = [1,2,3,4,5]
for element in array
  puts element
end
```  

However, in Ruby, developers usually write loops using special methods know as *iterators*. That feature makes Ruby code more elegant and closer to natural language.  
Because in Ruby, everything is an object and they all have their own methods so we can use some supported methods to write a loop, i.e using methods of a class number like this:  
```rb
# Use methods of clas number
3.times { puts "thank you" } # => print 'thank you` three times

# Compute the factorial of n
factorial = 1
2.upto(n) {|x| factorial *= x}
```  

#### **3.2.2 Process over Array**  

An `Array` class has some useful methods that allow processing over a list without writting loop-like. All of those methods also use `iterator` to iterate over a list:  

- **each**: invokes the associated block once for each element in the array.  
  ```rb
  a = [1,2,3]
  a.each do |elt|
    print elt + 1
  end
  ```  

- **map**: takes an enumerable object and a block. Each invocation of a block is passed a single element from the array and output a returned value:  
  ```rb
  a = [1,2,3]
  b = a.map { |x| x * x} # Square elements: b is [1,4,9]
  ```  

- **select**: works as a filter based on specific conditions:  
  ```rb
  a = [1,2,3]
  c = a.select {|x| x % 2 == 0} # select even numbers: c is [2]
  ```  

### **3.3 Method**  

#### **3.3.1 Method invocation**  

The format for defining a method is:  

```rb
def function_name
  ... some code ...
end
```  

Ruby's grammar allows the paranthese around method invocations to be omitted. This allows Ruby methods to be used as if they were a statements.  

Let's consider following example. Suppose we have a method named `func` which has one parameter as a integer:  

```rb
def func(num):  
  puts num
end  

# Case 1: call func method normally
func(3+2)+1

# Case 2: call func method without paranthese
func (3+2)+1
```  

In case 1, the function is passed a value 5 and the result returned result of the function is added by 1.  
In case 2, there are a space after function name. Therefore, the entire expression (3+2)+1 is used as the method argument.  

#### **3.3.2 Method aliases**  

Method aliasing is an interesting feature in Ruby that makes Ruby more expressive and natural language. In the case where there are multiple name for a method, we can choose the one that most natural in our code.  
A keyword `alias` that serves to define a new name for an existing method:  

```rb
alias new_name original_name
```  

Moreover, method aliasing can be used to insert new functionality into a method, for example:  

```rb
def hello
  puts "Hello world"
end

alias original_hello hello	# Give another name for a method

def hello
  puts "Do some stuff"
  original_hello		# Call original method in the function  
  puts "Test"
end
```  

### **3.4 Class and modules**  

#### 3.4.1 Definining a class  

Suppose we have a class `Rectangle` which has attributes as width, height. Its methods are calculating square and and perimeter:  

```rb
class Rectangle
  def initialize(w, h)
    @w = w
    @h = h
  end

  def square
    @w * @h
  end

  def perimeter
    2 * (@w + @h)
  end
end
```  

To create a new instance of a class, we use `new` method:  

```rb
r = Rectangle.new(3,4)
r.square()  # => Call square method, return 12
```  

The `initialize` method is special when defining a class in Ruby. The `new` method creates a new instance of a class and then it automatically invokes the `initialize` method on that instance. Arguments which are passed to `new` are also passed to `initialize`. Therefore, in the above example, the `initialize` method takes two argument which assigns initial values for two instance variables `@w` and `@h` so we have to pass two arguments in the `new` method.  

In other programming languages like C++ or Java, we have to declare instance varibles and assign defautl value at the declaration step. However, in Ruby, that practice is wrong:  

```rb
class Rectangle
  @w = 0    # WRONG!
  @h = 0    # WRONG!

  def initialize(w, h)
    @w = w
    @h = h
  end

  ...
end
```  

Notice that, in Ruby, instance variables are always resolved in the context of `self`. That means when defining a class, `self` refers to the `Rectangle` class and the first two assignments is executed as a part of the definition of a class. During this time, `self` does not hold an instance of a class but only after `initialize` method is invoked. Thus, in the above case, the `@w` and `@h` variables inside the `initialize` method are completely different from those outside it.  

#### 3.4.2 Accessors and Attributes  

In Ruby, instance variables and class variables are strictly encapsulated as private. Thus, to access value of those variables, we have to define accessor methods like `get`, `set` methods in other programming languages:  

```rb
class Rectangle
  def initialize(w, h); @w, @h = w, h; end

  def w; @w; end
  def h; @h; end

  def w=(value)
    @w = value
  end

  def h=(value)
    @h = value
  end
end
```  

After that, we can access values of `@w` and `@h` and modify those values. Because I use **assignment method** for setting value so I can call it like this:  

```rb
r = Rectangle.new(1,2)
r.w = 3           # set method write as assignment method
r.h = 4           # set method write as assignment method
puts r.square()   # => return 12
```  

However, if our class has many instance varibles and defining get/set methods for each of them is not convenient. Ruby provides a way for faster creating getter and setter by using `attr_reader`, `attr_writer`, `attr_accessor` defined by the `Module` class. All classes are modules so we can invoke these method in any class definition.  
- **attr_reader**: create getter methods.  
- **attr_writer**: create setter methods.
- **attr_accessor**: create both getter/setter methods.  

For example:  

```rb
class Rectangle
  attr_accessor :w, :h
  def initialize(w, h)
    @w = w
    @h = h
  end
end

r = Rectangle.new(3,4) # initially set w=3, h=4
puts r.h               # print 4
r.w = 4
puts r.w               # print 4
```  

#### 3.4.3 Method visibility  

Instance methods may be *public*, *private* or *protected*. In Ruby, methods are normally public unless they are explicitly declared to be private or protected. One exception is the `initialize` method, which is always implicitly private.  
A private method can only be called inside other instance methods of the class. It can also be implicitly invoked on `self` that we discussed earlier.  
A protected method is like private method that it can only be invoked from within the implementation of a class or its subclasses.  

For example:  

```rb
class Widget
  def x                     # Accesor method for @x
    @x
  end
  protected :x              # Make it protected

  def utility_method        # Define a method
    nil
  end
  private :utility_method   # Make it private
end
```  

#### 3.4.4 Mixins  
There are two ways to do a mixins:  
- **include**: import module code as instance methods.  
- **extends**: import module code as class methods.  

For example:  

```rb
module A
  PI = 3.14
  def cal
    puts PI
  end
end

class B
  include A
end

class C
  extend A
end

B.new.cal #=> print 3.14
C.cal     #=> print 3.14
B.cal     #=> undefined method `cal' for B:Class (NoMethodError)
```  

If we want to import instance methods and class methods of a class, we can use `include` and `extend` at the same time.  

```rb
class D
  include A
  extend A
end

D.new.cal #=> print 3.14
D.cal     #=> print 3.14
```  

#### 3.4.5 Metaprogramming  

Let's consider an example:  

```rb
my_obj = Object.New
my_other_obj = Object.New

def my_obj.set_my_variable=(var)
  @my_instance_variable = var
end

def my_obj.get_my_variable
  @my_instance_variable
end

my_obj.set_my_variable = "Hello"
my_obj.get_my_variable # => Hello

my_other_obj.set_my_variable = "Hello" #=> NoMethodError
```  

In the above example, we add new methods to the `my_obj` at run time dynamically. However, we do not apply that on `my_other_obj` so it cannot call method `set_my_variable`.  

Another example, suppose we have a class which has two methods:  

```rb
class Developer
  def coding_frontend
    p "Writting frontend"
  end

  def coding_backend
    p "Writting backend"
  end
end
```  

As you can see, those two methods is somehow the same, which make code repetition. Ruby has `define_method` which is a method defined in `Mdodule` class that helps us create methods dynamically and reduce code repetition. For example, we just create a template for a method and pass a method names to it to create our desired method:  

```rb
class Developer
  ["frontend", "backend"].each do |method|
    define_method "coding_#{method}" do
      p "Writting #{method}"
    end
  end
end
```

## **4. Implementation**  

There are three intepreter implementation in Ruby:  

- **Ruby MRI (Matz's RUby Intepreter)**: This is the core implementation that is used most by developer. It aslo has another name as "CRuby" because it was written entirely in C. Ruby MRI was created and still maintained by Yukihiro Matsumoto (Matz) in 1995. The most important difference between Ruby MRI and other intepreters is that MRI has something called GIL (Glocal Intepreter Lock). GIL prevents multithreading programming which allows only one thread to run at a time. The reason is at the time Ruby was created, concurrency is hard which makes our code easily goes wrong. Therefore, Matz decided to include MRI to avoid potenial issues. If we want true parallelism, let's try two below intepreters.  
- **JRuby**: is written in Java and runs on the JVM (Java virtual machine). The advantages of JRuby is that it allows we to use Java libraries in our code.  
- **Rubinius**: The goal of Rubinius is to write Ruby intepreter in Ruby itself. This is useful when developer do not want to deal with C or Java code.  

## **5. Application**  

Ruby is General-purpose like Python, but it is mostly used for web application (both front-end and back-end). Has many other uses like data analysis, prototyping and proof of concepts.  
Most prominent implementation in Ruby is Rails web – a development framework built with Ruby (example of Ruby on Rails: AirBnB, Hulu, Github, Goodreads etc).  
Other softwares include:  
- Homebrew – a tool for installing software packages on macOS.  
- Metasploit – security software for testing websites and applications to show how easy they are to break into.  

## **References**  

[The Ruby Programming Language - Oreilly](https://www.oreilly.com/library/view/the-ruby-programming/9780596516178/)  

[Wikipedia - Ruby (programming language)](https://en.wikipedia.org/wiki/Ruby_(programming_language))  