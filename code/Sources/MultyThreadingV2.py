import time, _thread,sys,machine

def work():
    for i in range(50):
        print('Hello')
        time.sleep(0.1)

def stopper(sec):
    time.sleep(sec)
    print('Exiting...')
    #_thread.interrupt_main()
    #_thread.exit()
    #sys.exit()
    #machine.sotf_reset()
    machine.soft_reset()

#_thread.start_new_thread(stopper, (2, ))

#long_running()
    
_thread.start_new_thread(work,())
stopper(2)