

#include <xc.h>

#include "Variables.h"

#include "variable_extern.h"


//****************************************************************************** 
//	FONCTION INITIALISATION ADC
//******************************************************************************

void Init_ADC(void) {
    ADCON0 = 0b00000000;
    ADCON1 = 0b00000000; /*ENTREE SORTIE DIGITALE */
    ADCON2 = 0b10010100; // TAD = 1 us F:4 TACQ = 4*TAD
    ADCON2bits.ADCS = 0b001; // Fosc/8
    ADCON3 = 0b11000000;
    ADCHS = 0b00000000;
    ANSEL0 = 0b00000011;
    //ANSEL0 = 0b00001111; // + DAC
    ANSEL1 = 0b00000000;
    ADON = 1;

}


//****************************************************************************** 
//	FONCTION INITIALISATION ADC
//******************************************************************************

void Init_ADC_PWM_Trig(void) {
    
    
    ADCON0bits.ACONV = 1; // 1 = Continuous Loop mode enabled - 0 = Single-Shoot mode enabled
    ADCON0bits.ACSCH = 0; // 1 = Multi-Channel mode enabled, Single Channel mode disabled - 0 = Single Channel mode enabled, Multi-Channel mode disabled
    ADCON0bits.ACMOD = 0b00; // If ACSCH = 0, Auto-Conversion Single Channel Sequence Mode Enabled: 00 = Single Channel Mode 1 (SCM1); Group A is taken and converted
    //ADCON0bits.GODONE = 0;
    ADCON0bits.ADON = 0; // AD Converter disabled
    
    
//    ADCON0 = 0b00100000;//
    //ADCON0 = 0b00100000;//Single Shot
    
    //ADCON0 = 0b10100000;//Continuous
    
    ADCON1bits.VCFG = 0b00; // 00 = V REF + = AV DD , V REF - = AV SS (AN2 and AN3 are analog inputs or digital I/O)
    ADCON1bits.FIFOEN = 0; // FIFO disabled
    //ADCON1bits.BFEMT = 0; // 0 = FIFO is not empty (at least one of four locations has unread A/D result data)
    
    
    ADCON1 = 0b00000000; /*ENTREE SORTIE DIGITALE */
    
    ADCON2bits.ADFM = 0; // A/D Result Format Select bit: 1 = Right justified - 0 = Left justified
    ADCON2bits.ACQT = 0b0010; // A/D Acquisition Time Select bits: 0010 = 4 T AD
    ADCON2bits.ADCS = 0b100; // A/D Conversion Clock Select bits: 100 = F OSC /4
    
    ADCON2 = 0b00010100; // TAD = 1 us F:4 TACQ = 4*TAD
//    ADCON3 = 0b11010000;
    ADCON2bits.ADCS = 0b001; // Fosc/8
    
    ADCON3bits.ADRS = 0b00; // A/D Result Buffer Depth Interrupt Select Control for Continuous Loop Mode bits
                            // The ADRS bits are ignored in Single-Shot mode.
                            // 00 = Interrupt is generated when each word is written to the buffer
    
    ADCON3bits.SSRC = 0b10000; // A/D Trigger Source Select bits: 1xxxx = Power Control PWM module rising edge starts A/D sequence
//                        Note 1:
//The SSRC<4:0> bits can be set such that any of the triggers will start a conversion (e.g., SSRC<4:0> = 00101
//will trigger the A/D conversion sequence when RC3/INT0 or Input Capture 1 event occurs).    
    
    
    
    ADCON3 = 0b00010000;
    ADCON3 = 0x00;//On lancera les ADC a la mains (depuis l'interruption du timer 2)
    //ADCON3 = 0b00010000;
    
    //ADCHSbits.GASEL = 
    
    ADCHS = 0b00000000; // A/D CHANNEL SELECT REGISTER
    ANSEL0 = 0b00000011;
    //ANSEL0 = 0b00001111; // + DAC
    ANSEL1 = 0b00000000;
    
    
//    
//    PIE1bits.ADIE = 1;
//    IPR1bits.ADIP = 1;
//    IPR3bits.PTIP = 1;
//    RCONbits.IPEN = 1;
//    
    PIE1bits.ADIE = 1;
    ADIF=0;
    IPR1bits.ADIP = 0;
    //IPR3bits.PTIP = 1;
    
    
    ADON = 1;
Nouvelle_Valeur_ADC = 0;
//ADIF=0;

}



//****************************************************************************** 
//	FONCTION INITIALISATION ADC
//******************************************************************************

void Init_ADC_Single_Shoot_I_Moteur_1(void) {
    
    
    ADCON0bits.ACONV = 0; // 1 = Continuous Loop mode enabled - 0 = Single-Shoot mode enabled
    ADCON0bits.ACSCH = 0; // 1 = Multi-Channel mode enabled, Single Channel mode disabled - 0 = Single Channel mode enabled, Multi-Channel mode disabled
    ADCON0bits.ACMOD = 0b00; // If ACSCH = 0, Auto-Conversion Single Channel Sequence Mode Enabled: 00 = Single Channel Mode 1 (SCM1); Group A is taken and converted
    //ADCON0bits.GODONE = 0;
    ADCON0bits.ADON = 0; // AD Converter disabled
    
    
//    ADCON0 = 0b00100000;//
    //ADCON0 = 0b00100000;//Single Shot
    
    //ADCON0 = 0b10100000;//Continuous
    
    ADCON1bits.VCFG = 0b00; // 00 = V REF + = AV DD , V REF - = AV SS (AN2 and AN3 are analog inputs or digital I/O)
    ADCON1bits.FIFOEN = 0; // FIFO disabled
    //ADCON1bits.BFEMT = 0; // 0 = FIFO is not empty (at least one of four locations has unread A/D result data)
    
    
    ADCON1 = 0b00000000; /*ENTREE SORTIE DIGITALE */
    
    ADCON2bits.ADFM = 0; // A/D Result Format Select bit: 1 = Right justified - 0 = Left justified
    ADCON2bits.ACQT = 0b0010; // A/D Acquisition Time Select bits: 0010 = 4 T AD
    ADCON2bits.ADCS = 0b100; // A/D Conversion Clock Select bits: 100 = F OSC /4
    ADCON2bits.ADCS = 0b001; // Fosc/8
    
    ADCON2 = 0b00010100; // TAD = 1 us F:4 TACQ = 4*TAD
//    ADCON3 = 0b11010000;
    ADCON2bits.ADCS = 0b001; // Fosc/8
    
    ADCON3bits.ADRS = 0b00; // A/D Result Buffer Depth Interrupt Select Control for Continuous Loop Mode bits
                            // The ADRS bits are ignored in Single-Shot mode.
                            // 00 = Interrupt is generated when each word is written to the buffer
    
    ADCON3bits.SSRC = 0b10000; // A/D Trigger Source Select bits: 1xxxx = Power Control PWM module rising edge starts A/D sequence
//                        Note 1:
//The SSRC<4:0> bits can be set such that any of the triggers will start a conversion (e.g., SSRC<4:0> = 00101
//will trigger the A/D conversion sequence when RC3/INT0 or Input Capture 1 event occurs).    
       ADCON3bits.SSRC = 0b00000; // Pas de trig externe

    
    
    ADCON3 = 0b00010000;
    ADCON3 = 0x00;//On lancera les ADC a la mains (depuis l'interruption du timer 2)
    //ADCON3 = 0b00010000;
    
    //ADCHSbits.GASEL = 
    
    ADCHS = 0b00000000; // A/D CHANNEL SELECT REGISTER
    ANSEL0 = 0b00000011;
    //ANSEL0 = 0b00001111; // + DAC
    ANSEL1 = 0b00000000;
    
    
//    
//    PIE1bits.ADIE = 1;
//    IPR1bits.ADIP = 1;
//    IPR3bits.PTIP = 1;
//    RCONbits.IPEN = 1;
//    
    PIE1bits.ADIE = 1;
    ADIF=0;
    IPR1bits.ADIP = 0;
    //IPR1bits.ADIP = 1;
    //IPR3bits.PTIP = 1;
    
    
    ADON = 1;
Nouvelle_Valeur_ADC = 0;
//ADIF=0;

}





//****************************************************************************** 
//	FONCTION INITIALISATION ADC
//******************************************************************************

void Init_ADC_Single_Shoot_I_Moteur_2(void) {
    
    
    ADCON0bits.ACONV = 0; // 1 = Continuous Loop mode enabled - 0 = Single-Shoot mode enabled
    ADCON0bits.ACSCH = 0; // 1 = Multi-Channel mode enabled, Single Channel mode disabled - 0 = Single Channel mode enabled, Multi-Channel mode disabled
    ADCON0bits.ACMOD = 0b01; // If ACSCH = 0, Auto-Conversion Single Channel Sequence Mode Enabled: 01 = Single Channel Mode 2 (SCM2); Group B is taken and converted
    //ADCON0bits.GODONE = 0;
    ADCON0bits.ADON = 0; // AD Converter disabled
    
    
//    ADCON0 = 0b00100000;//
    //ADCON0 = 0b00100000;//Single Shot
    
    //ADCON0 = 0b10100000;//Continuous
    
    ADCON1bits.VCFG = 0b00; // 00 = V REF + = AV DD , V REF - = AV SS (AN2 and AN3 are analog inputs or digital I/O)
    ADCON1bits.FIFOEN = 0; // FIFO disabled
    //ADCON1bits.BFEMT = 0; // 0 = FIFO is not empty (at least one of four locations has unread A/D result data)
    
    
    ADCON1 = 0b00000000; /*ENTREE SORTIE DIGITALE */
    
    ADCON2bits.ADFM = 0; // A/D Result Format Select bit: 1 = Right justified - 0 = Left justified
    ADCON2bits.ACQT = 0b0010; // A/D Acquisition Time Select bits: 0010 = 4 T AD
    ADCON2bits.ADCS = 0b100; // A/D Conversion Clock Select bits: 100 = F OSC /4
    ADCON2bits.ADCS = 0b001; // Fosc/8
    
    ADCON2 = 0b00010100; // TAD = 1 us F:4 TACQ = 4*TAD
//    ADCON3 = 0b11010000;
    ADCON2bits.ADCS = 0b001; // Fosc/8
    
    ADCON3bits.ADRS = 0b00; // A/D Result Buffer Depth Interrupt Select Control for Continuous Loop Mode bits
                            // The ADRS bits are ignored in Single-Shot mode.
                            // 00 = Interrupt is generated when each word is written to the buffer
    
    ADCON3bits.SSRC = 0b10000; // A/D Trigger Source Select bits: 1xxxx = Power Control PWM module rising edge starts A/D sequence
//                        Note 1:
//The SSRC<4:0> bits can be set such that any of the triggers will start a conversion (e.g., SSRC<4:0> = 00101
//will trigger the A/D conversion sequence when RC3/INT0 or Input Capture 1 event occurs).    
       ADCON3bits.SSRC = 0b00000; // Pas de trig externe

    
    
    ADCON3 = 0b00010000;
    ADCON3 = 0x00;//On lancera les ADC a la mains (depuis l'interruption du timer 2)
    //ADCON3 = 0b00010000;
    
    //ADCHSbits.GASEL = 
    
    ADCHS = 0b00000000; // A/D CHANNEL SELECT REGISTER
    ANSEL0 = 0b00000011;
    //ANSEL0 = 0b00001111; // + DAC
    ANSEL1 = 0b00000000;
    
    
//    
//    PIE1bits.ADIE = 1;
//    IPR1bits.ADIP = 1;
//    IPR3bits.PTIP = 1;
//    RCONbits.IPEN = 1;
//    
    PIE1bits.ADIE = 1;
    ADIF=0;
    IPR1bits.ADIP = 0;
    //IPR1bits.ADIP = 1;
    //IPR3bits.PTIP = 1;
    
    
    ADON = 1;
Nouvelle_Valeur_ADC = 0;
//ADIF=0;

}
//****************************************************************************** 
//	FONCTION INITIALISATION ADC
//******************************************************************************

void Init_ADC_PWM(void) {
    
//    ADCON0 = 0b00000000;
//    ADCON1 = 0b00000000; /*ENTREE SORTIE DIGITALE */
//    ADCON2 = 0b10010100; // TAD = 1 us F:4 TACQ = 4*TAD
//    ADCON3 = 0b11000000;
//    ADCHS = 0b00000000;
//    ANSEL0 = 0b00000011;
//    //ANSEL0 = 0b00001111; // + DAC
//    ANSEL1 = 0b00000000;
//    ADON = 1;
    
    
//    ADCON0 = 0b00100000;//
    ADCON0 = 0b00000000;//Single Shot
   // ADCON0 = 0b10100000;//Continuous
    ADCON1 = 0b00000000; /*ENTREE SORTIE DIGITALE */
    ADCON2 = 0b00010100; // TAD = 1 us F:4 TACQ = 4*TAD
    ADCON2bits.ADCS = 0b001; // Fosc/8
//    ADCON3 = 0b11010000;
    ADCON3 = 0b11000000;
    //ADCON3 = 0b00010000;
    ADCHS = 0b00000000;
    ANSEL0 = 0b00000011;
    //ANSEL0 = 0b00001111; // + DAC
    ANSEL1 = 0b00000000;
    
    
//    
//    PIE1bits.ADIE = 1;
//    IPR1bits.ADIP = 1;
//    IPR3bits.PTIP = 1;
//    RCONbits.IPEN = 1;
//    
    
    
    
    
    ADON = 1;
Nouvelle_Valeur_ADC = 0;
ADIF=0;

}




//******************************************************************************
//		FONCTION LECTURE AN0 GA
//******************************************************************************

             /*unsigned*/ int lecture_I_Mot1(void) {
    volatile static /* unsigned */ int Resul;

    ADCON0 = 0b00000001; //  RA0
    ADCON2 = 0b10010100; // TAD = 1 us F:4 TACQ = 4*TAD
    ADCON2bits.ADCS = 0b001; // Fosc/8
    //ADCON3 = 0b11000000;
    //ADON = 1;
    GODONE = 1;
    while (GODONE == 1);
    Resul = ADRESH;
    Resul = (Resul << 8) + ADRESL;
    NOP();
    NOP();
    NOP();
    NOP();
    NOP();
    NOP();
    return Resul;
}

void u_lecture_I_Mot1_init(void) {

    ADCON0 = 0b00000001; //  RA0
    //ADCON2 = 0b10010100; // TAD = 1 us F:4 TACQ = 4*TAD //Rigth justified
    ADCON2 = 0b00010100; // TAD = 1 us F:4 TACQ = 4*TAD // Left justified

}

unsigned char u_lecture_I_Mot1(void) {
    // volatile static unsigned char Resul;

    //    ADCON0 = 0b00000001; //  RA0
    //    ADCON2 = 0b10010100; // TAD = 1 us F:4 TACQ = 4*TAD

    //    ADCON0 = 0b00000001; //  RA0
    //    //ADCON2 = 0b10010100; // TAD = 1 us F:4 TACQ = 4*TAD //Rigth justified
    //    ADCON2 = 0b00010100; // TAD = 1 us F:4 TACQ = 4*TAD // Left justified
    // ADCON2 = 0b00001000; // TAD = 1 us F:4 TACQ = 4*TAD // Left justified
    //ADCON3 = 0b11000000;
    //ADON = 1;
    //LED = 1;
    GODONE = 1;
    //LED = 1;
    while (GODONE == 1);
    //LED = 0;
    //    Resul = ADRESH;
    //    Resul = (Resul << 8) + ADRESL;
    //    NOP();
    //    NOP();
    //    NOP();
    //    NOP();
    //    NOP();
    //    NOP();
    //return Resul;
    return ADRESH;
}


//******************************************************************************
//		FONCTION LECTURE AN1 GB
//******************************************************************************

int lecture_I_Mot2(void) {
    volatile static int Resul;

    ADCON0 = 0b00000100; //  RA0
    ADCON2 = 0b10010100; // TAD = 1 us F:4 TACQ = 4*TAD // Fosc / 4
    ADCON2bits.ADCS = 0b001; // Fosc/8
    
    ADON = 1;
    GODONE = 1;
    while (GODONE == 1);
    Resul = ADRESH;
    Resul = (Resul << 8) + ADRESL;
    NOP();
    NOP();
    NOP();
    NOP();
    NOP();
    NOP();
    return Resul;
}
