

#include <xc.h>

#include <string.h> 
#include <stdio.h> 
#include <stdlib.h>


#include "Variables.h"


#include "variable_extern.h"

#include "action.h"


void Alarme_On(unsigned char alarme_new_value){
    
            //P4_busy = P4_BUSY_LIBRE;
    
        Etat_Update(ETAT_ALARME);
        Alarme = alarme_new_value;
        Coupe_Moteur();
    
    
}