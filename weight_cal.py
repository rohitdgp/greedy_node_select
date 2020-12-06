import os

def main():
    f=open("max_sum_wts.txt","r")
    maxsum=map(int,f.readline().strip().split())
    print maxsum
    f.close()
    f=open("newalgo_wts.txt","r")
    newalgo=map(int,f.readline().strip().split())
    print newalgo
    f.close()

    f=open("output.txt","a+")
    f.write("\n\nMax Sum message passing - \n\nTotal Message passed through all nodes - "+str(sum(maxsum)))
    f.write("\nMax message transfer by a single node - "+str(max(maxsum)))
    f.write("\n\nOur Algorithm message passing - \n\nTotal Message passed through all nodes - "+str(sum(newalgo)))
    f.write("\nMax message transfer by a single node - "+str(max(newalgo)))
    f.close()



if __name__=="__main__":
    main()