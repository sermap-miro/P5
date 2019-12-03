


#include <xc.h>

#include "eusart.h"

#include "Variables.h"

#include "variable_extern.h"

#include "action.h"

#include "interrupt.h"

#include "timer.h"

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
    Init_Input_Capture_0();

}


//Gestion du capteur Pion 

void Init_Input_Capture_0(void) {

    // Front Montant  CAP1
    // CAPxREN: Time Base Reset Enable bit
    CAP1CONbits.CAP1REN = 0; // 0 = Disable selected time base Reset on capture
    // 1 = Enabled

    // CAPxM<3:0>: Input Capture x (ICx) Mode Select bits
    CAP1CONbits.CAP1M = 0b1111; // 1111 = Special Event Trigger mode; the trigger occurs on every rising edge on CAP1 input
    //        CAP1CONbits.CAP1M = 0b0000; // 1111 = Special Event Trigger mode; the trigger occurs on every rising edge on CAP1 input


    PIE3bits.IC1IE = 0; //  0 = IC1 interrupt disabled
    IPR3bits.IC1IP = 0; // 0 = Low priority
    PIR3bits.IC1IF = 0;



    // Front Descendant  CAP2
    // CAPxREN: Time Base Reset Enable bit
    CAP2CONbits.CAP2REN = 1; // 0 = Disable selected time base Reset on capture
    // 1 = Enabled

    // CAPxM<3:0>: Input Capture x (ICx) Mode Select bits
    CAP2CONbits.CAP2M = 0b1110; // 1000 = Capture on every CAPx input state change
    //    CAP2CONbits.CAP2M = 0b0000; // 1000 = Capture on every CAPx input state change



    PIE3bits.IC2QEIE = 0;
    IPR3bits.IC2QEIP = 0; // 0 = Low priority
    PIR3bits.IC2QEIF = 0;
}

void interrupt low_priority test2(void) {

    //Detection du front montant sur le capteur pion
    if ((PIE3bits.IC1IE == 1)&&(PIR3bits.IC1IF == 1)) {
        PIR3bits.IC1IF = 0;
        //On active l'interruption de CAP2 afin de capter le front descendant
        PIR3bits.IC2QEIF = 0;
        if (PIE3bits.IC2QEIE == 1) {//Si l'interruption de CAP2 est déjà autorisé, alors cela veut dire qu'il n'auras pas déclenché sur le front descendant suivant la précédente interruption de cette meme fonction
            Alarme = ALARME_OVERLOAD_CAP_1_2;
        } else {
            PIE3bits.IC2QEIE = 1;
        }

        TIMER5_On();


    } else
        //Detection du front descendant sur le capteur pion
        if ((PIE3bits.IC2QEIE == 1)&&(PIR3bits.IC2QEIF == 1)) {
        PIE3bits.IC2QEIE = 0; //On désactive l'interruption du prochaine front montant
        PIR3bits.IC2QEIF = 0;

        TIMER5_Off();

        nb_100ms_Timer_5 = 0;

    } else
        if (PIE1bits.TX1IE == 1 && PIR1bits.TX1IF == 1) {
        EUSART1_Transmit_ISR();
        //  IDLE_Enable();
    } else if (PIE1bits.RC1IE == 1 && PIR1bits.RC1IF == 1) {
        EUSART1_Receive_ISR();
        //  IDLE_Enable();
    } else


        //Timer 0
        if (INTCONbits.TMR0IE == 1 && INTCONbits.TMR0IF == 1) {
        INTCONbits.TMR0IF = 0;
        //LED^=1;
        nb_s_fonctionnement += 1;
    } else

        //Timer 5
        if (PIE3bits.TMR5IE == 1 && PIR3bits.TMR5IF == 1) {//période d'environ 130 ms
        PIR3bits.TMR5IF = 0;


        nb_100ms_Timer_5 += 1;


        if (nb_100ms_Timer_5 == nb_100ms_pion) {
            nb_Pion += 1;
            nb_s_fonctionnement = 0; //on réinitialise le compteur de temps entre pion
        } else if (nb_100ms_Timer_5 == nb_100ms_platine) {
            Etat = ETAT_PLATINE;
        }



        //        //NOP();
        //           LED=1;
        //           LED=0;
        //        LED^=1;
        //GODONE=1;

    } else

        if (PTIF == 1) {
        PTIF = 0;
        //        LED=1;
        //        LED=0;
    } else




        if (ADIF == 1) {
        //    PIE1bits.ADIE = 0;
        //ADIF=0;
        //LED = 1;
//        LED = 1;
            
            switch(moteur_indice){
                case MOTEUR_1:
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

        break;
        
        
        
                case MOTEUR_2:
                    
        Image_Courant_Moteur_2 = ADRESH;
        Nouvelle_Valeur_ADC = 1;

        ADIF = 0;


        erreur = consigne - Image_Courant_Moteur_2;
        if (erreur >= 10) duty++;
        else if (erreur < 0) duty--;
        //            erreur = erreur >> 4;
        //            duty =  erreur + duty;

        if (duty > PTPERL) duty = PTPERL;
        else if (duty < 0) duty = 0;
        PDC1L = (char) (duty << 2);
        PDC1H = (char) ((duty << 2) >> 8);

        break;
                default: break;
        
            }
        
//        LED = 0;

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


    if (PIE1bits.TMR2IE == 1 && PIR1bits.TMR2IF == 1) {
        PIR1bits.TMR2IF = 0;
        //        //NOP();
        //           LED=1;
        //           LED=0;
        GODONE = 1;

    }        //    
    else

        if (INT0IF == 1) // Capteur Capot
    {
        INT0IF = 0;
        Etat = ETAT_ALARME;
        Alarme = ALARME_CAPOT;
        Coupe_Moteur();
    }
    else

        if ((INTCON3bits.INT1IE == 1)&&(INTCON3bits.INT1IF == 1)) {//Surconsommation du Moteur 1
        INTCON3bits.INT1IF = 0;
        Etat = ETAT_ALARME;
        Alarme = ALARME_I_MOTEUR_1;
        Coupe_Moteur();
    } else
        if ((INTCON3bits.INT2IE == 1)&&(INTCON3bits.INT2IF == 1)) {//Surconsommation du Moteur 2
        INTCON3bits.INT2IF = 0;
        Etat = ETAT_ALARME;
        Alarme = ALARME_I_MOTEUR_2;
        Coupe_Moteur();


    }




}
