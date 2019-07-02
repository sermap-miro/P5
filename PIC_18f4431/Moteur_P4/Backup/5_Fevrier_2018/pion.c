


#include <xc.h>

#include "variable_extern.h"
#include "Variables.h"

#include "pion.h"






//Gestion du capteur Pion 

void Detection_Pion_On(void) {

    // // Front Montant  CAP1
    //    // CAPxREN: Time Base Reset Enable bit
    //    CAP1CONbits.CAP1REN = 0;    // 0 = Disable selected time base Reset on capture
    //                                // 1 = Enabled
    //    
    //    // CAPxM<3:0>: Input Capture x (ICx) Mode Select bits
    //    CAP1CONbits.CAP1M = 0b1111; // 1111 = Special Event Trigger mode; the trigger occurs on every rising edge on CAP1 input
    //
    //    
    //// Front Descendant  CAP2
    //    // CAPxREN: Time Base Reset Enable bit
    //    CAP2CONbits.CAP2REN = 1;    // 0 = Disable selected time base Reset on capture
    //                                // 1 = Enabled
    //    
    //    // CAPxM<3:0>: Input Capture x (ICx) Mode Select bits
    //    CAP2CONbits.CAP2M = 0b1110; // 1000 = Capture on every CAPx input state change
    //    CAP2CONbits.CAP2M = 0b0000; // 1000 = Capture on every CAPx input state change

    PIE3bits.IC1IE = 1; //  1 = IC1 interrupt enabled
    PIR3bits.IC1IF = 0;



}



void Detection_Pion_Off(void) {

    PIE3bits.IC1IE = 0; //  1 = IC1 interrupt enabled
    PIR3bits.IC1IF = 0;
    
}

