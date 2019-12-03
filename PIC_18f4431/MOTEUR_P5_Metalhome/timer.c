


#include <xc.h>

#include "Variables.h"
#include "timer.h"


#include "variable_extern.h"






//****************************************************************************** 
//	FONCTION INIT TIMER5
//******************************************************************************

void Init_TIMER0(void) {

    
    // TMR0ON: Timer0 On/Off Control bit
    T0CONbits.TMR0ON = 0;   // 0 = Timer0 is disabled
                            // 1 = Timer0 is enabled
    
    // T016BIT: Timer0 16-Bit Control bit
    T0CONbits.T016BIT = 0;  // 0 = Timer0 is configured as a 16-bit timer/counter
                            // 1 = Timer0 is configured as an 8-bit timer/counter
    
    // T0CS: Timer0 Clock Source Select bit
    T0CONbits.T0CS = 0;     // 0 = Internal clock (F OSC /4)
                            // 1 = Transition on T0CKI pin input edge
    
    // T0SE: Timer0 Source Edge Select bit
    T0CONbits.T0SE = 0;     // 0 = Increment on low-to-high transition on T0CKI pin
                            // 1 = Increment on high-to-low transition on T0CKI pin
    
    // PSA: Timer0 Prescaler Assignment bit
    T0CONbits.PSA = 0;      // 0 = Timer0 prescaler is assigned. Timer0 clock input comes from prescaler output.
                            // 1 = TImer0 prescaler is not assigned. Timer0 clock input bypasses prescaler.
    
    // T0PS<2:0>: Timer0 Prescaler Select bits
    T0CONbits.T0PS = 0b111; // 000 = 1:2 Prescale value
                            // 001 = 1:4 Prescale value
                            // 010 = 1:8 Prescale value
                            // 011 = 1:16 Prescale value
                            // 100 = 1:32 Prescale value
                            // 101 = 1:64 Prescale value
                            // 110 = 1:128 Prescale value
                            // 111 = 1:256 Prescale value
    T0CONbits.T0PS = 0b111; // 8.42 s de période
    T0CONbits.T0PS = 0b100; // 1.06 s de période
    //T0CONbits.T0PS = 0b000; //DEBUG
    
    
//    
//    PR2 = 200;
//    
//  //  PR2 = 200;
//        IPR1bits.TMR2IP = 0;//Interrupt with low Priority
//        IPR1bits.TMR2IP = 1;//Interrupt with high Priority
    
    
    INTCON2bits.TMR0IP = 0; // Low Priority
    
    
   // PIE3bits.TMR5IE = 1;
    INTCONbits.TMR0IE = 0;
    INTCONbits.TMR0IF = 0;
   // PIR3bits.TMR5IF = 0;
    
    
    /*DEBUG*/
//    INTCONbits.TMR0IE = 1;
//    INTCONbits.TMR0IF = 0;
//    
//    T0CONbits.TMR0ON = 1;
//    while(1);
    /*DEBUG*/
    
}



void TIMER0_On(void){
    TMR0H=0;
    TMR0L=0;
    //if(TIMER0_Etat == OFF){
    if(T0CONbits.TMR0ON == 0){
    INTCONbits.TMR0IE = 1;
    INTCONbits.TMR0IF = 0;
    LATC5=1; // LED 
    T0CONbits.TMR0ON = 1;
      
    }
    TIMER0_Etat = ON;
//    else
//        
//    {
//       //LATC5=1; // LED 
//        NOP();
//    }
    
//        PIE1bits.TMR2IE = 1;
//        PIR1bits.TMR2IF = 0;
}


void TIMER0_Off(void){
    
    T0CONbits.TMR0ON = 0;
    INTCONbits.TMR0IE = 0;
    INTCONbits.TMR0IF = 0;
    
    TIMER0_Etat = OFF;
//        PIE1bits.TMR2IE = 0;
//        PIR1bits.TMR2IF = 0;
    
}







//****************************************************************************** 
//	FONCTION INIT TIMER2
//******************************************************************************
// Environ 1,111 kHz
void Init_TIMER2(void) {
//    T2CON = 0b00000100;
//    PR2 = 200;
    
    //T2CON = 0b00000100;
    T2CON = 0b00100100; // N <TOUTPS<3:0>> <TMR2ON> <T2CKPS>
//    
//    T2CONbits.TOUTPS = 0b1111;
    T2CONbits.TOUTPS = 0b1000;
//    T2CONbits.TMR2ON = 0b0;
    T2CONbits.T2CKPS = 0b00;
    
     //   T2CON = 0b00100100;
        
        
        
    PR2 = 200;
    
  //  PR2 = 200;
        IPR1bits.TMR2IP = 0;//Interrupt with low Priority
        IPR1bits.TMR2IP = 1;//Interrupt with high Priority
}



void TIMER2_On(void){
    
        PIE1bits.TMR2IE = 1;
        PIR1bits.TMR2IF = 0;
}


void TIMER2_Off(void){
    
        PIE1bits.TMR2IE = 0;
        PIR1bits.TMR2IF = 0;
    
}








//****************************************************************************** 
//	FONCTION INIT TIMER5
//******************************************************************************

void Init_TIMER5(void) {

    // T5SEN: Timer5 Sleep Enable bit
    T5CONbits.T5SEN = 0;    // 0 = Timer5 is disabled during Sleep
                            // 1 = Timer5 is enabled during Sleep
        
    // RESEN: Special Event Trigger Reset Enable bit
    T5CONbits.RESEN = 1;    // 1 = Special Event Trigger Reset is disabled
                            // 0 = Special Event Trigger Reset is enabled
    
    // T5MOD: Timer5 Mode bit
    T5CONbits.T5MOD = 0;    // 1 = Single-Shot mode is enabled
                            // 0 = Continuous Count mode is enabled
    
    // T5PS<1:0>: Timer5 Input Clock Prescale Select bits
    T5CONbits.T5PS = 0b11;  // 00 = 1:1
                            // 01 = 1:2
                            // 10 = 1:4
                            // 11 = 1:8
    
    //Avec fosc = 8 MHz => fosc / ( 4 * 2^16 * 4) => 7.6 Hz
    
    
    // T5SYNC: Timer5 External Clock Input Synchronization Select bit
    T5CONbits.T5SYNC = 1;   // When TMR5CS = 1:
                            // 1 = Do not synchronize external clock input
                            // 0 = Synchronize external clock input
                            // When TMR5CS = 0:
                            // This bit is ignored. Timer5 uses the internal clock when TMR5CS = 0
    
    // TMR5CS: Timer5 Clock Source Select bit
    T5CONbits.TMR5CS = 0;   // 0 = Internal clock (T CY )
                            // 1 = External clock from the T5CKI pin
    
    
    TMR5L = 0;
    TMR5H = 0;
    
    PR5H = 0x61;
    PR5L = 0xA8;
    
    // TMR5ON: Timer5 On bit
    T5CONbits.TMR5ON = 0;   // 0 = Timer5 is disabled
                            // 1 = Timer5 is enabled
    
    TMR5L = 0;
    TMR5H = 0;
    
    
//    
//    PR2 = 200;
//    
//  //  PR2 = 200;
//        IPR1bits.TMR2IP = 0;//Interrupt with low Priority
//        IPR1bits.TMR2IP = 1;//Interrupt with high Priority
    
    IPR3bits.TMR5IP = 0; // Low Priority
    
    
    
    PIE3bits.TMR5IE = 1;
    PIR3bits.TMR5IF = 0;
    
    
    
    
}



void TIMER5_On(void){
    
    
   // PIE3bits.TMR5IE = 1;
    T5CONbits.TMR5ON = 1;
//        PIE1bits.TMR2IE = 1;
//        PIR1bits.TMR2IF = 0;
}


void TIMER5_Off(void){
    
    //PIE3bits.TMR5IE = 0;
    T5CONbits.TMR5ON = 0;
    PIR3bits.TMR5IF = 0;
    TMR5L = 0;
    TMR5H = 0;
//        PIE1bits.TMR2IE = 0;
//        PIR1bits.TMR2IF = 0;
    
}