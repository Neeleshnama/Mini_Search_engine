from django.shortcuts import render
import requests
import sys
from subprocess import run,PIPE

def button(request):
    return render(request, 'home.html')

def output(request):
    
    data = requests.get("https://www.google.com/")
    print(data.text)
    data = data.text
    return render(request, 'home.html', {'data':data})
# new

def external(request):
    inp = request.POST.get('param')
    out = run([sys.executable, 'C://Users//hp//Documents//IR//P40-MiniProject-MOTOR//sourcecode//main.py',inp],shell=False, stdout=PIPE)
    str1 = out.stdout.decode('utf-8').splitlines()
    
    # divide str1 into parts when you get -----------
    def  partition(lst, condition):
        result = []
        current = []
        def send(request):
            print("send")
        for item in lst:
            if condition(item):
                if current:
                    result.append(current)
                    current = []
            else:
                current.append(item)
        if current:
            result.append(current)
        return result

    #str1 = str1.splitlines()
    str1 = partition(str1, lambda x: x == '--------------------------------------------------')
    str1 = str1[:len(str1)-1]

    return render(request, 'home.html', {'data1':str1})


def send(request):
    inp = request.POST.get('param')
    inp = inp[7:]
    import pandas as pd
    df = pd.read_csv('C://Users//hp//Documents//IR//P40-MiniProject-MOTOR//sourcecode//data//feedback.csv')
    if df.loc[df['index'] == int(inp)].empty:
        df = df.append({'index': int(inp), 'feedback': 1}, ignore_index=True)
        df.to_csv('C://Users//hp//Documents//IR//P40-MiniProject-MOTOR//sourcecode//data//feedback.csv', index=False)
    else:
        df.loc[df['index'] == int(inp), 'feedback'] = df.loc[df['index'] == int(inp), 'feedback'].values[0] + 1
        df.to_csv('C://Users//hp//Documents//IR//P40-MiniProject-MOTOR//sourcecode//data//feedback.csv', index=False)
  