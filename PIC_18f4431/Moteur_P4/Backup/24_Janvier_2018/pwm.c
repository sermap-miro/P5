

#include <xc.h>

#include "Variables.h"


#include "variable_extern.h"

//****************************************************************************** 
//	FONCTION INIT PWM
//******************************************************************************

void Init_PWM(void) {
    PTPERL = 99;
    PTPERH = 0;

    PTCON0 = 0b00000000; // POSTSCALE 1,PRESCALE 1,MODE 
    
    PTCON1 = 0b10000000; // PWM TIME BASE,DIRECTION

    PWMCON0 = 0b00111111;
    PWMCON1 = 0b00000000;

    DTCON = 0b00000000;
    OVDCOND = 0b00000101;
    OVDCONS = 0b00000000;



    //    void Init_PWM(void)
    //{   
    //    int duty;
    //   
    //   
    //    PDC0L  =(char)(duty << 2);
    //    PDC0H  =(char)((duty << 2)>>8);
    //           
    //    duty = 20;
    //    PDC1L  =(char)(duty << 2);
    //    duty =  30;
    //    PDC1H  =(char)((duty << 2)>>8);
    // while();
    //}




}


//****************************************************************************** 
//	FONCTION INIT PWM
//******************************************************************************

void u_Init_PWM(void) {
    
    PTCON1bits.PTEN = 0; // On désactive le module PWM avant toute modification
    
    
    //PTPERL = 99;
    //PTPERL = 0x0f;
    //PTPERL = 0x7f;
    PDC0L = 1 << 2;
    PDC0H = 0;

    //    PTPERL = 0x63;
    //    PTPERL = 0x0f; //marche - 16
    //    PTPERL = 50;
    //    PTPERL = 250; //marche
    //    PTPERL = 0x20; //marche pas
    //    PTPERL = 255;
    //consigne_pwm_max = 
    PTPERL = (0xff) >> PWM_SHIFT; // = 0x1F = 32
    PTPERL = (0xff) >> 2; // = 0x1F = 32
//    PTPERL = 127;
    
    consigne_pwm_max = PTPERL + 1;
    
//erreur_accumulator_max = PTPERL << I_SHIFT;//24 bit
erreur_accumulator_max = (consigne_pwm_max << I_SHIFT) - 1;//24 bit
    // PTPERL = (0xff) >> 2; // = 0x1F = 32
    //PTMRL = PTPERL;
    //PTPERL = 0x0f;
    //PTPERL = 0xff;
    //PTPERL = 0x15;
    PTPERH = 0;
    // PTMRH = PTPERH;

    //PTCON0 = 0b00000000; // POSTSCALE 1,PRESCALE 1,MODE 
    //    PTCON0bits.PTMOD0 = 1
    //    PTCON0bits.PTMOD1 = 1

    PTCON0 = 0b00000011; // POSTSCALE 1,PRESCALE 1,MODE 
    
    
    
    PTCON0bits.PTOPS = 0b0000; // 1:1 Postcale
    //PTCON0bits.PTOPS = 0b0001; // 1:2 Postcale
    PTCON0bits.PTCKPS = 0b00;//00 = PWM time base input clock is F OSC /4 (1:1 prescale)
   // PTCON0bits.PTCKPS = 0b01;//01 = PWM time base input clock is F OSC /16 (1:4 prescale)
    //PTCON0bits.PTCKPS = 0b01;//10 = PWM time base input clock is F OSC /64 (1:16 prescale)
   // PTCON0bits.PTCKPS = 0b11;//11 = PWM time base input clock is F OSC /256 (1:64 prescale)
    
    //PTCON0bits.PTMOD = 0b11; //
    PTCON0bits.PTMOD = 0b10; //
//    bit 1-0 PTMOD<1:0>: PWM Time Base Mode Select bits
//11 = PWM time base operates in a Continuous Up/Down Count mode with interrupts for double PWM
//updates
//10 = PWM time base operates in a Continuous Up/Down Count mode
//01 = PWM time base configured for Single-Shot mode
//00 = PWM time base operates in a Free-Running mode
    


    PTCON1 = 0b10000000; // PWM TIME BASE,DIRECTION

    
    PWMCON0bits.PWMEN = 0b001; // PWM Module Enable bits:
//111 = All odd PWM I/O pins are enabled for PWM output (2)
//110 = PWM1, PWM3 pins are enabled for PWM output
//101 = All PWM I/O pins are enabled for PWM output (2)
//100 = PWM0, PWM1, PWM2, PWM3, PWM4 and PWM5 pins are enabled for PWM output
//011 = PWM0, PWM1, PWM2 and PWM3 I/O pins are enabled for PWM output
//010 = PWM0 and PWM1 pins are enabled for PWM output
//001 = PWM1 pin is enabled for PWM output
//000 = PWM module is disabled; all PWM I/O pins are general purpose I/O
    
    PWMCON0bits.PMOD = 0b1111; // PWM Output Pair Mode bits:
//For PMOD0:
//1 = PWM I/O pin pair (PWM0, PWM1) is in the Independent mode
//0 = PWM I/O pin pair (PWM0, PWM1) is in the Complementary mode
//For PMOD1:
//1 = PWM I/O pin pair (PWM2, PWM3) is in the Independent mode
//0 = PWM I/O pin pair (PWM2, PWM3) is in the Complementary mode
//For PMOD2:
//1 = PWM I/O pin pair (PWM4, PWM5) is in the Independent mode
//0 = PWM I/O pin pair (PWM4, PWM5) is in the Complementary mode
//For PMOD3: (3)
//1 = PWM I/O pin pair (PWM6, PWM7) is in the Independent mode
//0 = PWM I/O pin pair (PWM6, PWM7) is in the Complementary mode
//    
    
    PWMCON0 = 0b00111111;


    
    
    
    
    
    PWMCON1 = 0b00000000;
    PWMCON1 = 0b00000001; //

    DTCON = 0b00000000;
    OVDCOND = 0b00000101;
   //OVDCOND = 0b00000001;
    OVDCONS = 0b00000000;



    // PIE3bits.PTIE = 1; // interruption autorisé pour la pwm

    SEVTDIR = 0;
    //SEVTDIR = 1;
    SEVTCMPH = 0;
    SEVTCMPL = 10;//!!! SI on met 0 ca nne marche pas!








}