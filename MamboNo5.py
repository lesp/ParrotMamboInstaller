from pyparrot.Minidrone import Mambo

mamboAddr1 = "D0:3A:90:EB:E6:21"
mamboAddr2 = "d0:3a:bf:42:e6:3a"

mambo1 = Mambo(mamboAddr1, use_wifi=False)
mambo2 = Mambo(mamboAddr2, use_wifi=False)

print("trying to connect")
success1 = mambo1.connect(num_retries=3)
success2 = mambo2.connect(num_retries=3)
print("connected: %s" % success1)
print("connected: %s" % success2)
if (success1 and success2 == True):
    # get the state information
    print("sleeping")
    mambo1.smart_sleep(2)
    mambo2.smart_sleep(2)
    mambo1.ask_for_state_update()
    mambo2.ask_for_state_update()
    mambo1.smart_sleep(2)
    mambo2.smart_sleep(2)

    print("taking off!")
    mambo1.safe_takeoff(1)
    mambo2.safe_takeoff(1)
    mambo1.turn_degrees(180)
    mambo2.turn_degrees(180)
    mambo1.safe_land(5)
    mambo2.safe_land(5)
    mambo1.smart_sleep(5)
    mambo2.smart_sleep(5)
    mambo1.disconnect()
    mambo2.disconnect()
"""
    if (mambo.sensors.flying_state != "emergency"):
        print("flying state is %s" % mambo.sensors.flying_state)
        print("Flying direct: going up")
        mambo.fly_direct(roll=0, pitch=0, yaw=0, vertical_movement=20, duration=1)
        
        print("Showing turning (in place) using turn_degrees")
        mambo.turn_degrees(180)
        mambo.smart_sleep(2)
        mambo.turn_degrees(-180)
        mambo.smart_sleep(2)
        
        print("landing")
        print("flying state is %s" % mambo.sensors.flying_state)
        mambo.safe_land(5)
        mambo.smart_sleep(5)

        print("disconnect")
        mambo.disconnect()
"""
