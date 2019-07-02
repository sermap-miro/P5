

#include <xc.h>

#include <string.h> 
#include <stdio.h> 
#include <stdlib.h>


#include "Variables.h"


#include "variable_extern.h"

#include "action.h"


void Alarme_On(unsigned char alarme_new_value){
    
    
        Etat_Update(ETAT_ALARME);
        Alarme = alarme_new_value;
        Coupe_Moteur();
    
    
}