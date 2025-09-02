"""
welcome to the main python file for the ai engineer course on campus.
what i'll find here?
the basics to get started with python.
at the end of the course, let's create a program that will be a summarization of everything i've seen.
let's get started.
"""
# first lesson - comments.
#this is a comment, a single line comment.
"""
also a comment.
multiple lines of comments.
"""
print("this is a print statement") # i can duplicate this by pressing command + D

variables_lesson = "variables"
print("this is a " + variables_lesson + " lesson. don't copy and paste, you're human, you're prone to errors. so, create a variable.")

syntax_lesson = "syntax"
print("this is a " + syntax_lesson + " lesson. python has very strict syntax, so if you type X or x, will be two different things. watch it:")
X = 1
x = 2
print(X)
print(x)
print("see how X and x are two different things?")

constant_lesson = "CONSTANT"
print("this is a " + constant_lesson + " lesson. a constant it's something you can't change, for example, an API key. it has to stay the same and in uppercase. why? because it's important.")
API_KEY = "lkjo20u04943mflijg" # important example of a constant, you can't change an API key. it has to stay the same.

# learning_log.py content
import datetime

hoje = datetime.date.today()
print(f"Iniciando jornada em {hoje}")
print("Meta: Dominar Python para AI Engineering!")

# MEU ROADMAP PESSOAL
"""
Status: Fundamentos Python
Próximo: Estruturas de Dados
Meta Q1: NumPy/Pandas
Meta Q2: Primeiro modelo ML
Meta Q3: Projeto AIOps simples
Sonho: AI Agent autônomo para investigação e AI Evals
"""