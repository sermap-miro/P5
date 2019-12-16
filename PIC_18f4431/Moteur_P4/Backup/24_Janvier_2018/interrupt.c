


#include <xc.h>

#include "eusart.h"

#include "Variables.h"

#include "variable_extern.h"

#include "action.h"

void Init_IT(void) {
    INTCONbits.GIE = 1;
    INTCONbits.PEIE = 1;
    INTCONbits.TMR0IE = 0;
    INTCONbits.INT0IE = 0; //1
    INTCONbits.RBIE = 0;
    INTCONbits.TMR0IF = 0;
    INTCONbits.INT0IF = 0;
    INTCONbits.RBIF = 0;

    INTCON = 0b11010000; //GLOBAL IT,PERIPHERAL IT,TMROIE,INT0IE,RBIETMR0IF,INT0IF,RBIF

    INTCON2bits.RBPU = 1;
    INTCON2bits.INTEDG0 = 1;
    INTCON2bits.INTEDG1 = 1;
    INTCON2bits.INTEDG2 = 0;
    //INTCON2bits.Unimplented =0;
    INTCON2bits.TMR0IP = 0;
    //INTCON2bits.Unimplented =0;
    INTCON2bits.RBIP = 0;


    INTCON2 = 0b11100000; //PULL UP, INTEDG0,INTEDG1,TMR0IP,RBIP

    INTCON3bits.INT2IP = 1; //1
    INTCON3bits.INT1IP = 1; //1
    //INTCON3bits.Unimplented =0;
    INTCON3bits.INT2IE = 1;
    INTCON3bits.INT1IE = 1;
    //INTCON3bits.Unimplented =0;
    INTCON3bits.INT2IF = 0;
    INTCON3bits.INT1IF = 0;




    INTCON3 = 0b11011000; //  
    INTCON3 = 0b01001000; //  
    //PIR1= 0b01000000

    //    INTCONbits.GIEH=1;//GIEH
    //    INTCONbits.GIEL=1;
    //    //équivaut à
    //    INTCONbits.GIE=1;//GIEH
    //    INTCONbits.PEIE=1;


    RCONbits.IPEN = 1; // 1 = Enable priority levels on interrupts


    //    PIE1bits.TMR2IE = 1;


}

void interrupt low_priority test2(void) {
    if (PIE1bits.TX1IE == 1 && PIR1bits.TX1IF == 1) {
        EUSART1_Transmit_ISR();
        //  IDLE_Enable();
    } else if (PIE1bits.RC1IE == 1 && PIR1bits.RC1IF == 1) {
        EUSART1_Receive_ISR();
        //  IDLE_Enable();
    }
    else


        //Timer 1
        if (INTCONbits.TMR0IE == 1 && INTCONbits.TMR0IF == 1) {
        INTCONbits.TMR0IF = 0;


    } else

        //Timer 5
        if (PIE3bits.TMR5IE == 1 && PIR3bits.TMR5IF == 1) {
        PIR3bits.TMR5IF = 0;
        //        //NOP();
        //           LED=1;
        //           LED=0;
        //GODONE=1;

    } else

        if (PTIF == 1) {
        PTIF = 0;
        //        LED=1;
        //        LED=0;
    }
        //          else
        //    
        //       if (PIE1bits.TMR2IE == 1 && PIR1bits.TMR2IF == 1) {
        //           PIR1bits.TMR2IF = 0;
        ////        //NOP();
        //           LED=1;
        //           LED=0;
        //        GODONE=1;
        //        
        //       }
        //    
    else




        if (ADIF == 1) {
        //    PIE1bits.ADIE = 0;
        //ADIF=0;
        //LED = 1;
        LED = 1;
        Image_Courant_Moteur_1 = ADRESH;
        Nouvelle_Valeur_ADC = 1;

        ADIF = 0;


        erreur = consigne - Image_Courant_Moteur_1;
        if (erreur >= 10) duty++;
        else if (erreur < 0) duty--;
        //            erreur = erreur >> 4;
        //            duty =  erreur + duty;

        if (duty > PTPERL) duty = PTPERL;
        else if (duty < 0) duty = 0;
        PDC0L = (char) (duty << 2);
        PDC0H = (char) ((duty << 2) >> 8);

        LED = 0;

    }

    //else


    ////    
    //    if (ADIF == 1) {
    //    //    PIE1bits.ADIE = 0;
    //        //ADIF=0;
    //        //LED = 1;
    //        LED = 1;
    //        Image_Courant_Moteur_1 = ADRESH;
    //        Nouvelle_Valeur_ADC=1;






    //////////
    //////////
    //////////        //i = Image_Courant_Moteur_1;
    ////////////                erreur = consigne - Image_Courant_Moteur_1;
    //////////
    //////////        
    //////////        
    //////////        
    //////////        //erreur = consigne - Image_Courant_Moteur_1;
    //////////        
    ////////////        if (consigne > Image_Courant_Moteur_1)
    ////////////        {
    //////////////            //erreur = 1; 
    //////////////            //if (erreur_accumulator<0xff) erreur_accumulator += 1;//erreur_accumulator = 8 bit
    //////////////            //if (erreur_accumulator<0xffff) erreur_accumulator += 1;//erreur_accumulator = 16 bit
    ////////////           // if (erreur_accumulator<0xffffff) erreur_accumulator += 1;//erreur_accumulator = 24 bit
    ////////////            if (erreur_accumulator<erreur_accumulator_max) erreur_accumulator += 1;//erreur_accumulator = 24 bit
    //////////////            //if (erreur_accumulator<0xffffffff) erreur_accumulator += 1;//erreur_accumulator = 32 bit
    ////////////        }
    ////////////        else {
    ////////////            //erreur = -1;
    ////////////            if (erreur_accumulator>0) 
    ////////////                erreur_accumulator -= 1;
    ////////////        }
    ////////////        
    //////////        
    //////////        
    //////////        
    //////////        
    //////////        //erreur_accumulator += erreur;
    ////////////        erreur_accumulator += erreur >> 4;
    //////////        
    //////////        
    //////////        
    ////////////////        
    ////////////////        erreur = consigne - Image_Courant_Moteur_1;
    ////////////////        
    ////////////////        
    ////////////////        erreur_accumulator += erreur >> 4;
    ////////////////        
    //////////        
    //////////
    ////////////        erreur_accumulator = erreur_accumulator + erreur >> 2;
    //////////        //erreur_accumulator = erreur_accumulator;
    //////////        //erreur_accumulator += erreur >> 3;
    ////////////        if (   
    ////////////                ((erreur>=0) &&
    ////////////                ((0xff-erreur)>=erreur_accumulator))
    ////////////                  
    ////////////                )
    ////////////        {
    ////////////        erreur_accumulator += erreur >> 5;
    ////////////        }
    ////////////        else if (   
    ////////////                ((erreur<0) &&
    ////////////                (erreur<=erreur_accumulator))
    ////////////                  
    ////////////                )
    ////////////        {
    ////////////        erreur_accumulator += erreur >> 5;
    ////////////        }
    //////////        
    //////////        
    //////////           
    //////////        if (consigne > Image_Courant_Moteur_1)
    //////////        {
    //////////            erreur = consigne - Image_Courant_Moteur_1;
    //////////            if (0xff-erreur>=erreur_accumulator) erreur_accumulator = erreur_accumulator + erreur;// >> 3;
    //////////        }
    //////////        else {
    //////////            
    ////////////            erreur = 0;
    //////////        /* - */ erreur = Image_Courant_Moteur_1 - consigne; /* > 0 */
    //////////            if (0x00+erreur_accumulator>=erreur)  erreur_accumulator = erreur_accumulator - /* - */ erreur;// >> 3;
    //////////            erreur = 0;
    //////////            
    //////////        }
    //////////        
    //////////        
    //////////        //Pour la consigne PWM
    //////////        //erreur = erreur >> 3; //P(ID)
    //////////
    //////////        //
    //////////        //erreur = erreur + erreur_accumulator >> 3; // + (P)I(D)
    //////////
    //////////        //if(erreur > )
    ////////////        consigne_pwm = erreur >> P_SHIFT;
    ////////////        consigne_pwm += erreur_accumulator >> I_SHIFT; // + (P)I(D)
    //////////        
    ////////////                   erreur = consigne - Image_Courant_Moteur_1;
    ////////////                    erreur_accumulator = erreur_accumulator + erreur;
    //////////        
    //////////        
    //////////        
    ////////////        consigne_pwm = erreur >> P_SHIFT;
    ////////////        
    ////////////        consigne_pwm += (unsigned char) (erreur_accumulator >> I_SHIFT); // + (P)I(D)
    //////////        
    //////////        
    //////////        
    //////////        
    //////////        
    //////////        
    //////////        PID_out = erreur >> P_SHIFT;// P(ID))
    ////////////        PID_out += (erreur_accumulator-0x8fff) >> I_SHIFT;// + (P)I(D)
    //////////        //PID_out += erreur_accumulator >> I_SHIFT;// + (P)I(D)
    //////////        //PID_out += (erreur_accumulator-0x8fff) >> I_SHIFT;// + (P)I(D)
    //////////        if ( erreur_accumulator >= 0x8fff) {
    //////////        PID_out += (erreur_accumulator-0x8fff) >> I_SHIFT;// + (P)I(D)
    //////////        }
    //////////        else
    //////////        {
    ////////////            PID_out -= (0x8fff-erreur_accumulator) >> I_SHIFT;// + (P)I(D)
    //////////            PID_out -= (0x8fff-erreur_accumulator) >> I_SHIFT;// + (P)I(D)
    //////////        }
    //////////        
    //////////        
    //////////        
    ////////////        consigne_pwm = erreur >> P_SHIFT;
    ////////////        consigne_pwm = (unsigned char) (erreur_accumulator >> I_SHIFT); // + (P)I(D)
    //////////        
    //////////        consigne_pwm = (unsigned char) (PID_out >> PID_SHIFT);
    //////////        
    //////////        //consigne_pwm = erreur_accumulator;// >> I_SHIFT; // + (P)I(D)
    //////////
    //////////
    //////////
    //////////
    //////////        //if (consigne_pwm >= ((0xff >> PWM_SHIFT) + 1)) {
    //////////        if (consigne_pwm >= consigne_pwm_max) {
    ////////////            consigne_pwm = 0xff >> PWM_SHIFT;
    //////////            consigne_pwm = 0x1f;// >> PWM_SHIFT;
    //////////        }
    //////////
    //////////        if (consigne_pwm <= 0) {
    //////////            consigne_pwm = 0x01;
    //////////        }
    //////////
    //////////        
    //////////        consigne_pwm = consigne_pwm & 0x1f;
    //////////        
    //////////        
    //////////        

    // erreur = 31;//Test pleine onde //DEBUG
    //////////////        PDC0L = ((unsigned char) consigne_pwm) << 2;
    //////////////        PDC0H = ((unsigned char) consigne_pwm) >> 6;

    //        if (AV_1 == 0) PIE1bits.ADIE = 0;
    //         if (AV_1 == 1) PIE1bits.ADIE = 1;


    //        ADIF = 0;
    //        
    //        
    //        LED = 0;
    //        
    //    }

    //    NOP();
}

//******************************************************************************
//	FONCTION INTERRUPTION HIGH PRIORITY 
//******************************************************************************

void interrupt high_priority test1(void) {

    //        if (PIE1bits.TX1IE == 1 && PIR1bits.TX1IF == 1) {
    //        EUSART1_Transmit_ISR();
    //        //  IDLE_Enable();
    //    } else if (PIE1bits.RC1IE == 1 && PIR1bits.RC1IF == 1) {
    //        EUSART1_Receive_ISR();
    //        //  IDLE_Enable();
    //    }
    //    
    //        
    //    else
    //        if (ADIF == 1) {
    //    //    PIE1bits.ADIE = 0;
    //        ADIF=0;
    //        }

    //        else

    if (PIE1bits.TMR2IE == 1 && PIR1bits.TMR2IF == 1) {
        PIR1bits.TMR2IF = 0;
        //        //NOP();
        //           LED=1;
        //           LED=0;
        GODONE = 1;

    }
        //       else

        //        PIE1bits.TMR2IE = 1;
        //        PIR1bits.TMR2IF = 0;
        //       if (PIE1bits.TMR2IE == 1 && PIR1bits.TMR2IF == 1) {
        //        //NOP();
        ////           LED=1;
        ////           LED=0;
        //        GODONE=1;
        //       }

        //if((INT0IF ==  1)||(INT1IF ==  1)) // IT COUPURE SECTEUR BLOQUANT 

        //    if(PIR1bits.ADIF==1){
        //////    if(ADIF==1){
        //////        LED=1;
        //////        ADIF=0;
        //////Nouvelle_Valeur_ADC = 1;
        //////        Image_Courant_Moteur_1 = ADRESH;
        //////        LED=0;
        //////    }
        //////    
        ////////    else if(PTIF == 1){
        ////////        //PTIF=0;
        ////////        
        ////////        
        ////////    }
        //////    
        //////    
        //////    else 
        //////        
        //////        

        //    if(PTIF == 1){
        //        PTIF=0;
        ////        LED=1;
        ////        LED=0;
        //    }
        //    else
        // if(PIR1bits.ADIF==1){
        //    if(ADIF==1){
        //        ADIF=0;
        //        LED=1;
        //        LED=0;
        ////        Image_Courant_Moteur_1 = ADRESH;
        ////        Nouvelle_Valeur_ADC=1;
        //    }
        //    
    else
        //            
        //    if (ADIF == 1) {
        //    //    PIE1bits.ADIE = 0;
        //        //ADIF=0;
        //        //LED = 1;
        //        LED = 1;
        //        Image_Courant_Moteur_1 = ADRESH;
        //        Nouvelle_Valeur_ADC=1;
        //
        //            ADIF = 0;
        //        
        //        
        //        LED = 0;
        //        
        //    }   
        //        
        //    else
        //if (INT0IF == 1) // IT COUPURE SECTEUR BLOQUANT 
        if (INT0IF == 1) // Capteur Capot
    {
        INT0IF = 0;
        Alarme = ALARME_CAPOT;
                Coupe_Moteur();
        //        DRIVER_M1 = 0;
        //        DRIVER_M2 = 0;
        //        OVDCOND = 0b00000000;
        //        LED = 0;
        //        while (1)
        //            
        //        {LED = 0;
        //        LED = 0;
        //        LED = 0;
        //        LED = 0;
        //        LED = 1;}
    }
    
    
        else 
//        //INTCON3bits.Unimplented =0;
//    INTCON3bits.INT2IE = 1;
//    INTCON3bits.INT1IE = 1;
//    //INTCON3bits.Unimplented =0;
//    INTCON3bits.INT2IF = 0;
//    INTCON3bits.INT1IF = 0;
            if((INTCON3bits.INT1IE == 1)&&(INTCON3bits.INT1IF == 1)){//Surconsommation du Moteur 1
                INTCON3bits.INT1IF = 0;
                Alarme = ALARME_I_MOTEUR_1;
                Coupe_Moteur();
            }
            else
            if((INTCON3bits.INT2IE == 1)&&(INTCON3bits.INT2IF == 1)){//Surconsommation du Moteur 2
                INTCON3bits.INT2IF = 0;
                Alarme = ALARME_I_MOTEUR_2;
                Coupe_Moteur();
                
                
            }
                
    
    

}
