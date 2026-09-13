import argparse,json

def schedule(retries,base=1.0,cap=60.0):
 if retries<0 or base<0 or cap<0: raise ValueError('values must be non-negative')
 return [min(cap,base*(2**n)) for n in range(retries)]

def main():
 p=argparse.ArgumentParser();p.add_argument('retries',type=int);p.add_argument('--base',type=float,default=1);p.add_argument('--cap',type=float,default=60);a=p.parse_args()
 print(json.dumps(schedule(a.retries,a.base,a.cap)))
if __name__=='__main__': main()
