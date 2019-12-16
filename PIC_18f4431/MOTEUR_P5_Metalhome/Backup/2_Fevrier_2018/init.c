

#include <xc.h>

#include "Variables.h"


#include "variable_extern.h"

//****************************************************************************** 
//	FONCTION INITIALISATION ENTREE SORTIE
//******************************************************************************

void Init_Port(void) {
    /*sortie 0 entree 1*/


    TRISA = 0b11111111;
    TRISB = 0b11111010;
    TRISC = 0b11011100;
    TRISD = 0b00001111;
    TRISE = 0b00000111;

    
    //Pions
//    TRISAbits.
    
    
    
    LATA = 0b00000000;
    LATB = 0b00000000;
    LATC = 0b00000000;
    LATD = 0b00000001;
    LATE = 0b00000000;
    
    
    
    

}
