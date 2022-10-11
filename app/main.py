import socket
import datetime
from fastapi import FastAPI
from time import time, strftime
from decimal import Decimal, getcontext

docker_short_id = socket.gethostname()
app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": docker_short_id}


@app.get("/pi/{nb_digits}")
def read_digits_number(nb_digits: int):
    return {pi(nb_digits), f"on container {docker_short_id}"}


# arccot function using power formula arccot = 1/x - 1/(3x^3) + 1/(5x^5) ...
def arccot(x, digits):
    # set precision and starting values
    getcontext().prec = digits
    total = 0
    n = 1
    # loop while new term is large enough to actually change the total
    while Decimal((2 * n - 1) * x ** (2 * n - 1)) < Decimal(10 ** digits):
        # find value of new term
        term = ((-1)**(n - 1)) * 1 / Decimal((2 * n - 1) * x ** (2 * n - 1))
        # add the new term to the total
        total += term
        # next n
        n += 1
    # return the sum
    return total

# pi function
def pi(decimals):
    timestart = time()
    Decimal(4 * (4 * arccot(5, decimals + 3) - arccot(239, decimals + 3))).quantize(Decimal(10) ** (-decimals))
    timeelapsedint = round(time() - timestart, 2)
    timeelapsedstr = str(datetime.timedelta(seconds = round(timeelapsedint, 0)))
    return("runtime: " + timeelapsedstr + " or " + str(timeelapsedint) + " seconds.")