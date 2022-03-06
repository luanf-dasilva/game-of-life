OBJECTIVE: 

This is Conway's simple and functional game of life! The inspiration for this small project is to take Jack Diederich's implementation of GOL in his Stop Writing Classes talk from Pycon US in 2012 and actually implement it in something, i.e. pygame.

It was surprising to see such clean code implement Conway's game. The very talk was called Stop Writing Classes, and all I could I fnd when searching how to code up the GOL were classes
So in the spirit of the talk, and the Zen of Python, I prefer easy things. So I sought out to make the game of life simple.

But I like classes and I want to use them for their best use cases; and on above that I want to use each of Python's features for their best use cases. The amount of functionality that can be cooked up with so little lines of code is startling sometimes. Look at dataclasses for example. Type python main.py --help from the root of the repo and see the enormous amount of effort that went on behind the scenes from me importing typer, making the parse_cli_args function with type hints + typer.Argument(...), and then starting the GOL with typer.run(parse_cli_args).

Besides Jack Deiderich, I take inspiration from two other talks to familiarize myself with Python features and use cases for them: James Powel's 'So You Want to Be a Python Expert' and Raymond Hettinger's 'Build Powerful, New Data Structures With Python's Abstract Base Classes'. Powel demonstrates a nice implementation of decorators to time functions, and Hettinger has a Validator which I use to check if the inputs given to the program via command line are meaningful.  

SETUP (or equivalent depending on your operating system):

0. Install python, pip and virtualenv
1. Clone the repo
2. Go to app's root directory 
3. Create a virtual environment: virtualenv -p python3 venv
4. Activate virtual environment: source ./venv/Scripts/activate
5. Download dependencies: pip install -r requirements.txt
6. Run: python main.py --help or python main.py

SOURCES:

Jack Diederich's Stop Writing Classes: 
https://www.youtube.com/watch?v=o9pEzgHorH0

James Powel's 'So You Want to Be a Python Expert?': 
https://www.youtube.com/watch?v=cKPlPJyQrt4

Raymond Hettinger's 'Build Powerful, New Data Structures With Python's Abstract Base Classes':
https://www.youtube.com/watch?v=S_ipdVNSFlo
