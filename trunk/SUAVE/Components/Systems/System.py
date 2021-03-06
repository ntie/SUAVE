## @ingroup Components-Systems
# System.py
# 
# Created:  
# Modified: Feb 2016, T. MacDonald

# ----------------------------------------------------------------------
#  Imports
# ----------------------------------------------------------------------

from SUAVE.Components import Component

# ----------------------------------------------------------------------
#  Payload Base Class
# ----------------------------------------------------------------------
        
## @ingroup Components-Systems
class System(Component):
    """ SUAVE.Components.Systems.System()
    
        The Top Level System Class
        
            Assumptions:
            None
            
            Source:
            N/A
    """    
    
    
    def __defaults__(self):

        """ This sets the default values for the system.
        
                Assumptions:
                None
                
                Source:
                N/A
                
                Inputs:
                None
                
                Outputs:
                None
                
                Properties Used:
                N/A
        """        
        
        self.tag             = 'System'
        self.mass_properties = mass_properties()
        self.position        = [0.0,0.0,0.0]
        self.control         = None
        self.accessories     = None

## @ingroup Components-Systems
class Container(Component.Container):

    """ SUAVE.Components.Systems.Container()
    
        The Systems Container Class
        
            Assumptions:
            None
            
            Source:
            N/A
    """    
    
    pass

System.Container = Container