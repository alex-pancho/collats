import os
import logging

logname = 'cc.log'
here = os.path.dirname(os.path.abspath(__file__))
if os.path.exists(os.path.join(here, logname)):
    os.remove(os.path.join(here, logname))
filename = os.path.join(here, logname)
logging.basicConfig(
        level=logging.INFO,
        format="%(message)s",
        handlers=[
            logging.FileHandler(filename, encoding='utf8'),
            logging.StreamHandler()
        ]
    )

def backward(n, y=0, start_odd=""):
    if y>=10:
        logging.info(odd_list)
        return
    if n%3==0:
        x = n
        if (x//3)%3==0 and x not in bk_list:
            bk_list.append(x)
        elif x not in bk_list:
            while (x // 3) != 1 and x not in bk_list:
                x = x // 3
                bk_list.append(x)
        logging.info(f"BK:({len(bk_list)}): {bk_list}")
        return
    else:
        y = y+1
        if start_odd not in odd_list:
            odd_list[start_odd] = []
        if n not in odd_list[start_odd]:
            odd_list[start_odd].append(n)
        backward(n*2-1, y, start_odd)
        
        

def forward(n):
    if n == 4:
        logging.info(f"FW:({len(fv_list)}): {fv_list}")
        return
    if n % 2 == 0:
        n = n // 2
    else:
        if n not in fv_list:
            fv_list.append(n)
        n = (3*n + 1) // 2
    forward(n)

def main():
    for n in range (3, 244):
        fv_list = []
        bk_list = []
        logging.info(f"-{n}-")
        forward(n)
        backward(n, 0, n)

bk_list = []
odd_list = {}
fv_list = []
main()