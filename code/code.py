import CameraTimerV3 as CT
# import _thread
# import time


# #Yank out the key in case of problems with the loop.
# key = digitalio.DigitalInOut(board.GP0)
# key.direction = digitalio.Direction.INPUT
# key.pull = digitalio.Pull.UP

# def keyChecker():
#     print("CheckingTheKey")
#     time.sleep(5)
#     print("CheckingTheKey")

if(CT.getKey()):
    print("Key out.")
    print("Editing mode. You may edit the run.camera file now.")
else:
    print("Key in.")
    print("Run mode. Your camera will start taking pictures now. Remove the key at any time to stop it.")
    # new_thread = _thread.start_new_thread(keyChecker,())
    CT.run()