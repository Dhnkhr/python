import time
import multiprocessing

def square_num():
    for i in range (5):
        time.sleep(1)
        print(i**2)

def cube_num():
    for i in range (5):
        time.sleep(0.5)
        print(i*i*i)
if __name__ == "__main__":
    p1=multiprocessing.Process(target= square_num)
    p2=multiprocessing.Process(target= cube_num)

    t=time.time()

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    t3=time.time()-t

    print(t3)