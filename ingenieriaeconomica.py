#! /usr/bin/env python
# -*- coding: utf-8 -*-
import re


DIC = {
    # 'F/P': lambda P=0, i=0, n=0: P*(1+i)**n,
    'F/P': lambda data: data[0]*(1+data[1])**data[2],

    # 'A/F': lambda F=0, i=0, n=0: F*(i/((1+i)**n)-1),
    'A/F': lambda data: data[0]*(data[1]/((1+data[1])**data[2])-1),

    # 'A/P': lambda P=0, i=0, n=0: P*((i*(1+i)**n)/(((1+i)**n)-1)),
    'A/P': lambda data: data[0]*((data[1]*(1+data[1])**data[2])/(((1+data[1])**data[2])-1)),

    # 'F/A': lambda A=0, i=0, n=0: A*((((1+i)**n)-1)/i),
    'F/A': lambda data: data[0]*((((1+data[1])**data[2])-1)/data[1]),

    # 'P/A': lambda A=0, i=0, n=0: A*((((1+i)**n)-1)/(i*(1+i)**n)),
    'P/A': lambda data: data[0]*((((1+data[1])**data[2])-1)/(data[1]*(1+data[1])**data[2])),

    # 'P/F': lambda F=0, i=0, n=0: F*(1/(1+i))**n,
    'P/F': lambda data: data[0]*(1/(1+data[1]))**data[2],

    # 'P/G': lambda G=0, i=0, n=0: G*((1/i)*(((((1+i)**n)-1)/(i*(1+i)**n))-(n/(1+i)**n))),
    'P/G': lambda data: data[0]*((1/data[1])*(((((1+data[1])**data[2])-1)/(data[1]*(1+data[1])**data[2]))-(data[2]/(1+data[1])**data[2]))),

    # 'Pg/A1': lambda A1=0, g=0, i=0, n=0: A1*(1-((((1+g)/(1+i))**n)/(i-g))),  # g != i
    #'Pg/A1': lambda data: data[0]*(1-((((1+data[1])/(1+data[2]))**data[3])/(data[2]-data[1]))),  # g != i

    # 'Pg/A1i': lambda A1=0, i=0, n=0: A1*(n/(1+i)),  # g == i
    #'Pg/A1i': lambda data: data[0]*(data[2]/(1+data[1])),  # g == i

    'Pg/A': lambda data: data[0]*(1-((((1+data[1])/(1+data[2]))**data[3])/(data[2]-data[1]))) if data[1] != data[2] else data[0]*(data[3]/(1+data[2]))
}

def main():
    while True:
        try:
            cadena = input('Introduce la notación estándar\n>>')
            m = re.search('(\d+)\((\w\w?\/\w),(\d+\.?\d+),(\d+)', cadena)
            arguments = list(m.groups())
            method = arguments.pop(1)
            arguments = list(map(float, arguments))
            print('Resultado: %f \n' % DIC[method](arguments))
        except KeyboardInterrupt:
            print('\nTerminando programa...\n')
            break

if __name__ == '__main__':
    main()
