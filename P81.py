
import os
from multiprocessing import Process

def child_process():
    print("Child Process:")
    print("PID:", os.getpid())
    print("Parent PID:", os.getppid())

def main():
    # Create a child process
    p = Process(target=child_process)
    p.start()

    print("Parent Process:")
    print("PID:", os.getpid())
    print("Child PID:", p.pid)

    p.join()  # Wait for child to finish

if __name__ == "__main__":
    main()
