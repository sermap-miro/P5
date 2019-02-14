

#include <xc.h>

#include "Variables.h"


#include "variable_extern.h"

//****************************************************************************** 
//	FONCTION INITIALISATION ENTREE SORTIE
//******************************************************************************

void Init_Port(void) {
    /*sortie 0 entree 1*/

//    TRISA = 0xFF; //état d'origine au démarrage du PIC
//    TRISB = 0xFF; //état d'origine au démarrage du PIC
//    TRISC = 0xFF; //état d'origine au démarrage du PIC
//    TRISD = 0xFF; //état d'origine au démarrage du PIC
//    TRISE = 0xFF; //état d'origine au démarrage du PIC


    TRISA = 0b11111111;
    TRISAbits.TRISA0 = 1;// AN0
    TRISAbits.TRISA1 = 1;// AN1
    TRISAbits.TRISA2 = 1;// PION
    TRISAbits.TRISA3 = 1;// PION
    TRISAbits.TRISA4 = 1;// NC
    TRISAbits.TRISA5 = 1;// DAC 1
    TRISAbits.TRISA6 = 0;// BUZZER
    TRISAbits.TRISA7 = 1;// NC
    TRISB = 0b11111010;
    TRISBbits.TRISB0 = 0;// PWM M1
    TRISBbits.TRISB1 = 1;// NC
    TRISBbits.TRISB2 = 0;// PWM M2
    TRISBbits.TRISB3 = 1;// NC
    TRISBbits.TRISB4 = 1;// BP - URGENCE
    TRISBbits.TRISB5 = 1;// NC
    TRISBbits.TRISB6 = 1;// RB6 (ICD3)
    TRISBbits.TRISB7 = 1;// RB7 (ICD3)
    TRISC = 0b11011100;
    TRISCbits.TRISC0 = 0;// BLOCAGE M1
    TRISCbits.TRISC1 = 0;// BLOCAGE M2
    TRISCbits.TRISC2 = 0;// LED
    TRISCbits.TRISC3 = 1;// CAPOT
    TRISCbits.TRISC4 = 1;// I MOT 1
    TRISCbits.TRISC5 = 1;// I MOT 2
    TRISCbits.TRISC6 = 0;// RX1
    TRISCbits.TRISC7 = 1;// TX1
    TRISD = 0b00001111;
    TRISD = 0b00000111;
    TRISDbits.TRISD0 = 1;// AR 2
    TRISDbits.TRISD1 = 1;// AV 2
    TRISDbits.TRISD2 = 1;// AR 1
    //TRISDbits.TRISD3 = 1;// AV 1
    TRISDbits.TRISD3 = 0;// BUZZER
    TRISDbits.TRISD4 = 0;// AV M1
    TRISDbits.TRISD5 = 0;// AR M1
    TRISDbits.TRISD6 = 0;// AV M2
    TRISDbits.TRISD7 = 0;// AR M2
    TRISE = 0b00000111;
    TRISEbits.TRISE0 = 1;// DAC 2
    TRISEbits.TRISE1 = 1;// NC
    TRISEbits.TRISE2 = 0;// RELAIS
//    TRISEbits.TRISE3 = 1;// Inexistant
//    TRISEbits.TRISE4 = 1;// Inexistant
//    TRISEbits.TRISE5 = 1;// Inexistant
//    TRISEbits.TRISE6 = 1;// Inexistant
//    TRISEbits.TRISE7 = 1;// Inexistant

    
    //Pions
//    TRISAbits.
    
    
    
    LATA = 0b00000000;
    LATB = 0b00000000;
    LATC = 0b00000000;
    LATD = 0b00000000;
    LATE = 0b00000000;
    
    
    
    

}
