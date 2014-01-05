import time
import sys

class ProgressBar():
    max_value = 0
    steps = 0
    cur_value = 0
    def __init__(self, max_value, message):
        self.max_value = max_value
        self.steps = max_value/10
        print 'Processing %d %s [          ]'% (max_value, message) +' %3d%%'% 0,
        sys.stdout.flush()
        
    def increment(self):
        self.cur_value += 1
        if self.cur_value % self.steps == 0:
           completed = (self.cur_value/self.steps)
           print '\b'*17 + '.'*completed +' '*(10-completed)+ ']'+' %3d%%'%(completed*10),
           sys.stdout.flush()
    

def main():	 
    pb = ProgressBar(n, 'files')
    for i in range(n):
        #here do something
        time.sleep(0.1)
        pb.increment()
     
if __name__ == "__main__":
    main()
