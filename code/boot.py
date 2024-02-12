import CameraTimerV5 as CT
import _thread
import machine


if(CT.getKey()):
    print("Key in.")
    print("Run mode. Your camera will start taking pictures now. Remove the key at any time to stop it.")
#     try:
#         state=[True]
#         print("In boot")
#         _thread.start_new_thread(CT.run,(state,))
#         CT.keyChecker(state)
#     except:
#         print("Key was removed and the program was finished permaturely.")
#         machine.soft_reset()
    
    state=[True]
    _thread.start_new_thread(CT.run,(state,))
    CT.keyChecker(state)
        
else:
    print("Key out.")
    print("Editing mode. You may edit the run.camera file now.")