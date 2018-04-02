import time
import matplotlib.pyplot as plt


# viz from rcviz needs no timing import because of the graphic styles

# calculates function execution time
def execution_time(func, *args, n_iter=20):
    full_time = 0

    for i in range(n_iter):
        t0 = time.perf_counter()
        func(*args)
        full_time += (time.perf_counter() - t0)

    return full_time / n_iter


# draws timelines for functions from the funcs_list
def functions_timelines(funcs_list, args):
    for func in funcs_list:
        plt.plot(args, [execution_time(func, arg) for arg in args], label=func.__name__)

    plt.legend()
    plt.grid(True)
    plt.show()
