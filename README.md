# Backen-Engineer-Exercise

### 1. Please implement a string function in a numeric format in a language that you are good at. And mark every three digits with a comma. Please attach unit test.
```
f(9527) => "9,527", f(3345678) => "3,345,678", f(-1234.45) => "-1,234.45"
```
#### Answer: solution1.py unittest_for_solution1.py

### 2. Please implement a pipe function in a language that you are good at. The function parameter is of indefinite length, the first parameter is a variable of any type, and the following parameter is the function pointer. Please attach unit test.
```
def increment (int value) {
return value + 1
}
pipe(5, increment) => 6, pipe(5, increment, increment, increment) => 8
```
#### Answer: solution2.py unittest_for_solution2.py

### 3. With the expansion of business, the number of website users is increasing. The original data table has grown to the point where it is very slow to read and write data. Please describe how you will handle this from the two aspects of reading and writing.


### 4. Your job is to design and create a CLI application that will parser www.alexa.com data. The application signature should look like the following:

```
$ ./clawer <action> <arg1> [<arg2>...]
```
The application must be able to accept these actions as param and perform
the corresponding tasks:
1. top <number> : show top <number> sites URL on www.alexa.com/topsites/
2. country <country> : show top 20 sites URL on www.alexa.com/topsites/ by country

```
e.g.
$ ./clawer top <number>
$ ./clawer country <country>
```
The application needs to have an extensible interface where adding a new
action is just a matter of adding more files and should not require any
modifications to the existing code base.
ps. If anything is unclear, you may set a reasonable assumption and state it at
the beginning of the situation.

#### Answer: solution4.py
```
ex:
$ ./solution4.py top 2
--> top 25 url: xxx.xxxx.xxxx/xxxx/xxx

$ ./solution4.py country Taiwan
--> top 20 in Taiwan:
https://xxx.xxxx.xxx/xxxx/xxxx
https://xxx.xxxx.xxx/xxxx/xxxx
https://xxx.xxxx.xxx/xxxx/xxxx
...
```
