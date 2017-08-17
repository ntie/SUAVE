## @ingroup Methods-Missions-Segments-Cruise
# Constant_Mach_Constant_Altitude_Loiter.py
# 
# Created:  Jul 2014, SUAVE Team
# Modified: Jan 2016, E. Botero

# ----------------------------------------------------------------------
#  Imports
# ----------------------------------------------------------------------

import SUAVE

# ----------------------------------------------------------------------
#  Initialize Conditions
# ----------------------------------------------------------------------

## @ingroup Methods-Missions-Segments-Cruise
def initialize_conditions(segment,state):
    """Sets the specified conditions which are given for the segment type.

    Assumptions:
    Constant speed and constant altitude with set loiter time

    Source:
    N/A

    Inputs:
    segment.altitude                [meters]
    segment.time                    [seconds]
    segment.speed                   [meters/second]

    Outputs:
    conditions.frames.inertial.velocity_vector  [meters/second]
    conditions.frames.inertial.position_vector  [meters]
    conditions.freestream.altitude              [meters]
    conditions.frames.inertial.time             [seconds]

    Properties Used:
    N/A
    """     
    
    # unpack
    alt        = segment.altitude
    final_time = segment.time
    air_speed  = segment.air_speed 
    conditions = state.conditions   
    
    # check for initial altitude
    if alt is None:
        if not state.initials: raise AttributeError('altitude not set')
        alt = -1.0 * state.initials.conditions.frames.inertial.position_vector[-1,2]
        segment.altitude = alt        
    
    # dimensionalize time
    t_initial = conditions.frames.inertial.time[0,0]
    t_final   = final_time + t_initial
    t_nondim  = state.numerics.dimensionless.control_points
    time      =  t_nondim * (t_final-t_initial) + t_initial
    
    # pack
    state.conditions.freestream.altitude[:,0]             = alt # Update for AD
    state.conditions.frames.inertial.position_vector[:,2] = -alt # z points down # Update for AD
    state.conditions.frames.inertial.velocity_vector[:,0] = air_speed # Update for AD
    state.conditions.frames.inertial.time[:,0]            = time[:,0] # Update for AD
    
