#!/usr/bin/python
import numpy
import math

max_iters = 2

def print_scheme_table():
    step_size  = [1.0, 0.1, 0.01, 0.001]

    print "      {0} ".format(
          "---------------------------------------------------------")

    print "     {0}          {1}        {2}".format(
          " |    Forward "," Backward ","  Central      |")

    print "      {0} ".format(
          "---------------------------------------------------------")

    for j in range(len(step_size)):

        ''' Initialise with zeros '''
        fn_forward      = numpy.zeros(max_iters)
        fn_backward     = numpy.zeros(max_iters)

        dfdx_forward    = numpy.zeros(max_iters)
        dfdx_backward   = numpy.zeros(max_iters)
        dfdx_central    = numpy.zeros(max_iters)

        for i in range(max_iters):
            fn_forward[i]            =    1.0 / math.exp(forward(i, step_size[j]))
            dfdx_forward             =    1.0 * first_diff(fn_forward[i - 1], fn_forward[i], step_size[j])

            fn_backward[i]           =    1.0 / math.exp(backward(i, step_size[j]))
            dfdx_backward            =    first_diff(fn_backward[i - 1], fn_backward[i], step_size[j])

            dfdx_central             =    0.5 * first_diff(fn_forward[i-1],  fn_backward[i] , step_size[j])

            if i != 0:
                print "      {0} {1}       {2}      {3} {4}".format(
                                                        "|",
                                                        float(dfdx_forward),
                                                        float(dfdx_backward),
                                                        float(dfdx_central),
                                                        "|")
    print "      {0} ".format(
          "--------------------------------------------------------")

def forward(i, step):
    return step * (i - 1)

def backward(i, step):
    return step * i

''' @first_diff()  Works out the first differential for Taylor expansion
                   for function f[x],
    @return        double value of (f[i - 1] - f[i]) / step_size[j] '''
def first_diff(f1, f0, step):
    return (f1 - f0) / step

print_scheme_table()
