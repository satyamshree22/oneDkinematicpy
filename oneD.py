
import math

def final_velocity(initial_velocity=0,acceleration=0,time=0,final_position=0,initial_position=0):
    # when time is t given
    if time != 0 and  acceleration !=0 :

        # vx=vox +ax*t

        final_velocity = initial_velocity +  acceleration * (time)

        return final_velocity

    elif time == 0 and acceleration != 0:


        # vx^2=v0x^2 +2ax(x-xo)

        final_velocity =math.sqrt((pow(initial_velocity,2)+ 2*acceleration*(final_position-initial_velocity)))

        return final_velocity


    elif  time != 0 and acceleration == 0:

            final_velocity =2*(final_position-initial_position)/time  - initial_velocity    

            return final_velocity

def initial_velocity(final_velocity = 0,acceleration = 0,time = 0,final_position = 0,initial_position = 0):
    # when time is t given
    if time != 0 and  acceleration != 0 :

        # vx=vox +ax*t

        initial_velocity= acceleration * pow(time,2)-initial_velocity

        return initial_velocity

    elif time == 0 and acceleration !=0:


        # vx^2=v0x^2 +2ax(x-xo)

        initial_velocity =math.sqrt((2*acceleration*(final_position-initial_velocity))-pow(final_velocity,2))
        

        return initial_velocity


    elif  time != 0 and acceleration == 0:

            initial_velocity =2*(final_position-initial_position)/time  - final_velocity    

            return initial_velocity



def find_acceleration(initial_velocity=0,final_velocity=0,initial_position=0,final_position=0,time=0):

        if time==0:

            acceleration=(pow(final_velocity,2)-pow(initial_velocity,2))/(2*(final_position-initial_position))
        
        else:
        
            if final_position == 0 and initial_position ==0:
        
                acceleration=(final_velocity-initial_velocity)/time
                
                return acceleration
        
            else:
        
                acceleration=(2*(final_position-initial_position) - initial_velocity*time)/(time*time)
        
                return acceleration

def find_displacement(initial_velocity=0,final_velocity=0,acceleration=0,time=0):

    if time == 0 and acceleration !=0:
   
        displacement= (pow(final_velocity,2)-pow(initial_velocity,2))/(2*acceleration)   
   
        return displacement
   
    elif time!=0 and acceleration == 0:
   
        displacement = ((initial_velocity+final_velocity)*time)/2
   
        return displacement
   
    else:
   
        displacement =((initial_velocity*time + .5*acceleration*time*time))
   
        return displacement    

def kmph_mps(velocity):
    return 5*velocity/18

def mps_kmph(velocity):
    return 18*velocity/5