


#include <xc.h>

#include "eusart.h"

#include "spi.h"

#include "Variables.h"

#include "variable_extern.h"

#include "action.h"

#include "interrupt.h"

#include "timer.h"

#include "alarme.h"


//Active les interruptions sur les surconsommation de courant par les moteurs
#define CURRENT_HARD_IRQ
//Désactive les interruptions sur les surconsommation de courant par les moteurs
//#undef CURRENT_HARD_IRQ


void Buzzer_Etat(unsigned char Activation) {
    if (Activation == 1) {
        BUZZER = 1;
      //  LED = 1;
    } else {
        BUZZER = 0;
      //  LED = 0;
    }

}

void IRQ_Execution(unsigned char IRQ_Indice) {
    switch (IRQ_Indice) {

        case INDICE_IRQ_CAPOT:IRQ_CAPOT();
            break;
        case INDICE_IRQ_I_MOTEUR_1:IRQ_I_MOTEUR_1();
            break;
        case INDICE_IRQ_I_MOTEUR_2:IRQ_I_MOTEUR_2();
            break;
        case INDICE_IRQ_METAL_APPARAIT:IRQ_PION_Metal_Apparait();
            break;
        case INDICE_IRQ_METAL_DISPARAIT:IRQ_PION_Metal_Disparait();
            break;
        case INDICE_IRQ_TIMER_0:IRQ_TIMER_0();
            break;
        case INDICE_IRQ_TIMER_2:IRQ_TIMER2();
            break;
        case INDICE_IRQ_TIMER_5:IRQ_TIMER_5();
            break;
        case INDICE_IRQ_ADC:IRQ_ADC();
            break;
        case INDICE_IRQ_PWM: IRQ_PWM();
            break;
        default: break;


    }

}

void Init_IT(void) {
    INTCONbits.GIE = 1;
    INTCONbits.PEIE = 1;
    INTCONbits.TMR0IE = 0;
    INTCONbits.INT0IE = 0; //1
    INTCONbits.RBIE = 0;
    INTCONbits.TMR0IF = 0;
    INTCONbits.INT0IF = 0;
    INTCONbits.RBIF = 0;

    // INTCON = 0b11010000; //GLOBAL IT,PERIPHERAL IT,TMROIE,INT0IE,RBIETMR0IF,INT0IF,RBIF

    INTCON2bits.RBPU = 1;
    INTCON2bits.INTEDG0 = 1; // Front Montant
    INTCON2bits.INTEDG0 = 0; // Front Descendant // Modification du 18 Avril
    INTCON2bits.INTEDG1 = 1;
    INTCON2bits.INTEDG2 = 1;
    //INTCON2bits.Unimplented =0;
    INTCON2bits.TMR0IP = 0;
    //INTCON2bits.Unimplented =0;
    INTCON2bits.RBIP = 0;


    //  INTCON2 = 0b11100000; //PULL UP, INTEDG0,INTEDG1,TMR0IP,RBIP

    INTCON3bits.INT2IP = 1; //1
    INTCON3bits.INT1IP = 1; //1
    //INTCON3bits.Unimplented =0;
    INTCON3bits.INT2IE = 0; //On activera la détection surconsommation par moteur à chaque utilisation
    INTCON3bits.INT1IE = 0; //On activera la détection surconsommation par moteur à chaque utilisation
    //INTCON3bits.Unimplented =0;
    INTCON3bits.INT2IF = 0;
    INTCON3bits.INT1IF = 0;


    //#ifdef DEBUG
    //    INTCON3bits.INT2IE = 0;
    //    INTCON3bits.INT1IE = 0;
    //#endif

    //    INTCON3 = 0b11011000; //  
    //    INTCON3 = 0b01001000; //  
    //PIR1= 0b01000000

    //    INTCONbits.GIEH=1;//GIEH
    //    INTCONbits.GIEL=1;
    //    //équivaut à
    //    INTCONbits.GIE=1;//GIEH
    //    INTCONbits.PEIE=1;


    RCONbits.IPEN = 1; // 1 = Enable priority levels on interrupts


    //    PIE1bits.TMR2IE = 1;
    Init_Input_Capture_0();


    // IPR3bits.IC2QEIP = 0;//IC2 interrupt low priority

//SPI
    IPR1bits.SSPIP = 0; // Low priority SPI


}


//Gestion du capteur Pion 

void Init_Input_Capture_0(void) {

    // Front Montant  CAP1
    // CAPxREN: Time Base Reset Enable bit
    CAP1CONbits.CAP1REN = 0; // 0 = Disable selected time base Reset on capture
    // 1 = Enabled

    // CAPxM<3:0>: Input Capture x (ICx) Mode Select bits
    //CAP1CONbits.CAP1M = 0b1111; // 1111 = Special Event Trigger mode; the trigger occurs on every rising edge on CAP1 input
    // CAP1CONbits.CAP1M = 0b1110; // 1110 = Special Event Trigger mode; the trigger occurs on every falling edge on CAP1 input
    CAP1CONbits.CAP1M = 0b1000; // 1110 = Special Event Trigger mode; the trigger occurs on every falling edge on CAP1 input
    //        CAP1CONbits.CAP1M = 0b0000; // 1111 = Special Event Trigger mode; the trigger occurs on every rising edge on CAP1 input


    PIE3bits.IC1IE = 0; //  0 = IC1 interrupt disabled
    IPR3bits.IC1IP = 0; // 0 = Low priority
    PIR3bits.IC1IF = 0;



    // Front Descendant  CAP2
    // CAPxREN: Time Base Reset Enable bit
    CAP2CONbits.CAP2REN = 0; // 0 = Disable selected time base Reset on capture
    // 1 = Enabled

    // CAPxM<3:0>: Input Capture x (ICx) Mode Select bits
    //CAP2CONbits.CAP2M = 0b1111; // Config impossible pour CAP2 et CAP3
    CAP2CONbits.CAP2M = 0b1000; // 1000 = Capture on every CAPx input state change
    //    CAP2CONbits.CAP2M = 0b0000; // 1000 = Capture on every CAPx input state change



    PIE3bits.IC2QEIE = 0;
    IPR3bits.IC2QEIP = 0; // 0 = Low priority
    PIR3bits.IC2QEIF = 0;
}

void Capteur_Capot_On(void) {
    INTCONbits.INT0IE = 1;
    INTCONbits.INT0IF = 0;

    
    
    //6 Septembre 2018
    if    (PORTCbits.RC3==0) { //Le capot n'est pas en place! On arrete tout
                        //P4_busy = P4_BUSY_OCCUPER;
                        P4_busy = P4_BUSY_LIBRE;
                        Etat_Update(ETAT_BLOQUER_DEFINITIVEMENT);
                        //Etat_Update(ETAT_BLOQUER_IMPOSSIBLE);
    
}
    
    
}

void Capteur_Capot_Off(void) {
    INTCONbits.INT0IE = 0;

}

void IRQ_PION_CHANGEMENT_ETAT(void) {
    PIR3bits.IC1IF = 0;
    //Alarme = ALARME_OVERLOAD_CAP_1_2;

    switch (Surveillance_Capteur_Pion) {
        case METAL_ABSENT:



            if (PION == METAL_PRESENT) {//Normalement on est dans ce cas la
                Surveillance_Capteur_Pion = METAL_PRESENT;
                TIMER5_On();
                //BUZZER = 1;
                Buzzer_Etat(BUZZER_ON);
            } else {//Ne devrais pas arriver (a moins qu'il n'y ai des parasites sur le signal du capteur pion)  000000001000000000
                Surveillance_Capteur_Pion = METAL_ABSENT;
                Alarme = ALARME_OVERLOAD_CAP_1_1;

                TIMER5_Off();
                //Buzzer_Etat(BUZZER_OFF);
                nb_100ms_Timer_5 = 0;
                //nb_100ms_platine = NB_100MS_PLATINE; //permet de charger la valeur réelle de ce paramètre après le démarrage (ou on double ce temps)
                
                nb_100ms_platine = nb_100ms_platine_backup; // 18 Juin 2018
                Mouvement_Startup = 0;

            }



            break;


        case METAL_PRESENT:

            if (PION == METAL_PRESENT) {//Ne devrais pas arriver (a moins qu'il n'y ai des parasites sur le signal du capteur pion)   11111111110111111111111
                Surveillance_Capteur_Pion = METAL_PRESENT;
                Alarme = ALARME_OVERLOAD_CAP_1_2;

                Buzzer_Etat(BUZZER_ON);
            } else {
                Surveillance_Capteur_Pion = METAL_ABSENT;

                Buzzer_Etat(BUZZER_OFF);
                TIMER5_Off();

                nb_100ms_Timer_5 = 0;
                //nb_100ms_platine = NB_100MS_PLATINE; //permet de charger la valeur réelle de ce paramètre après le démarrage (ou on double ce temps)
                nb_100ms_platine = nb_100ms_platine_backup; // 18 Juin 2018
                Mouvement_Startup = 0;

            }


            break;
        default: break;
    }





}



//
//void IRQ_PION_RISING_EDGE(void) {

void IRQ_PION_Metal_Apparait(void) {

//    Buzzer_Etat(BUZZER_ON);
    PIR3bits.IC1IF = 0;
    
    if(CAPOT==0){
      Etat_Update(ETAT_RECULE);  
    }
    
    
//    //On active l'interruption de CAP2 afin de capter le front descendant
//    PIR3bits.IC2QEIF = 0;
//    if (PIE3bits.IC2QEIE == 1) {//Si l'interruption de CAP2 est déjà autorisé, alors cela veut dire qu'il n'auras pas déclenché sur le front descendant suivant la précédente interruption de cette meme fonction
//        Alarme = ALARME_OVERLOAD_CAP_1_3;
//    } else {
//        //PIR3bits.IC2QEIF = 0;
//        PIE3bits.IC2QEIE = 1;
//    }
//    // LED=1;
//    TIMER5_On();

}

//void IRQ_PION_FALLING_EDGE(void) {

void IRQ_PION_Metal_Disparait(void) {

//    Buzzer_Etat(BUZZER_OFF);
    PIE3bits.IC2QEIE = 0; //On désactive l'interruption du prochaine front montant
    PIR3bits.IC2QEIF = 0;

//    TIMER5_Off();
//
//    nb_100ms_Timer_5 = 0;
//    //Modif du 19 avril
//    //nb_100ms_platine = NB_100MS_PLATINE; //permet de charger la valeur réelle de ce paramètre après le démarrage (ou on double ce temps)
//    
//    nb_100ms_platine = nb_100ms_platine_backup;
//    
//    Mouvement_Startup = 0;
}


//
////de métal présent on passe a métal absent
//
//void IRQ_PION_RISING_EDGE(void) {
//
//    PIE3bits.IC1IE = 0; //PIE3bits.IC2QEIE = 0; //On désactive l'interruption du prochaine front montant
//    PIR3bits.IC1IF = 0; //PIR3bits.IC2QEIF = 0;
//
//    TIMER5_Off();
//
//    nb_100ms_Timer_5 = 0;
//    nb_100ms_platine = NB_100MS_PLATINE; //permet de charger la valeur réelle de ce paramètre après le démarrage (ou on double ce temps)
//    Mouvement_Startup = 0;
//
//
//
//}
//
//
//
///*   if ((PIE3bits.IC1IE == 1)&&(PIR3bits.IC1IF == 1)) {
//        IRQ_PION_RISING_EDGE();
// * 
//        if ((PIE3bits.IC2QEIE == 1)&&(PIR3bits.IC2QEIF == 1)) {
//        IRQ_PION_FALLING_EDGE();*/
//
////Du métal  vient d'apparaitre devant le capteur à induction
//
//void IRQ_PION_FALLING_EDGE(void) {
//
//    PIR3bits.IC2QEIF = 0; //PIR3bits.IC1IF = 0;
//    //On active l'interruption de CAP2 afin de capter le front descendant
//    PIR3bits.IC1IF = 0; //PIR3bits.IC2QEIF = 0;
//    //if (PIE3bits.IC2QEIE == 1) {//Si l'interruption de CAP2 est déjà autorisé, alors cela veut dire qu'il n'auras pas déclenché sur le front descendant suivant la précédente interruption de cette meme fonction
//    if (PIE3bits.IC1IE == 1) {//Si l'interruption de CAP2 est déjà autorisé, alors cela veut dire qu'il n'auras pas déclenché sur le front descendant suivant la précédente interruption de cette meme fonction
//        Alarme = ALARME_OVERLOAD_CAP_1_2;
//    } else {
//        PIR3bits.IC1IF = 0;
//        PIE3bits.IC1IE = 1;
//    }
//
//
//
//    LED = 1;
//
//    TIMER5_On();
//}
//






//Timer 0 => Compteur de seconde

void IRQ_TIMER_0(void) {
    INTCONbits.TMR0IF = 0;
    //LED^=1;
    nb_s_fonctionnement += 1;
    Capteur_Capot_Compteur_Temps_S += 1;
    delay_s_counter += 1;

    // if (consigne < Consigne_Max) {//???? a supprimer ou à insérer dans le switch plus bas  ????
    //if    
    //consigne += 1;
    if (nb_s_fonctionnement == 2) {//activation retardé de la surveillance de la surconsommation de courant au bout de 2 secondes

    //if (nb_s_fonctionnement == 0) {//activation retardé de la surveillance de la surconsommation de courant au bout de 2 secondes

        // consigne = Consigne_Max;

        switch (moteur_indice) {
            case MOTEUR_1:
                Surveillance_Consommation_Moteur_1_Activer(); // Supprime les fausses détection de surconsommation au démarrage des moteurs
                if (Consigne_Max_Moteur_X > Consigne_Max) {
                    consigne = Consigne_Max;
                } else {
                    consigne = Consigne_Max_Moteur_X;
                }
                break;
            case MOTEUR_PELLE:
                Surveillance_Consommation_Moteur_2_Activer(); // Supprime les fausses détection de surconsommation au démarrage des moteurs
                //Surveillance_Consommation_Moteur_2_Desactiver();
                if (Consigne_Max_Moteur_Z > Consigne_Max) {
                    consigne = Consigne_Max;
                } else {
                    consigne = Consigne_Max_Moteur_Z;
                }
                break;
            case MOTEUR_BEQUILLE:
                Surveillance_Consommation_Moteur_2_Activer(); // Supprime les fausses détection de surconsommation au démarrage des moteurs
                if (Consigne_Max_Moteur_Bequille > Consigne_Max) {
                    consigne = Consigne_Max;
                } else {
                    consigne = Consigne_Max_Moteur_Bequille;
                }
                break;
            default: break;
        }
        //      }
    }
}

void IRQ_TIMER_5(void) {
    PIR3bits.TMR5IF = 0;


    nb_100ms_Timer_5 += 1;


    if (nb_100ms_Timer_5 == nb_100ms_pion) {
        if (Mouvement_Startup != 1) {
            nb_Pion += 1;
        }

        //        LED=1;
        nb_s_fonctionnement = 0; //on réinitialise le compteur de temps entre pion


        //Condition de libération de l'action de déplacement en cours
        if ((Option_Pailleux == 1) | ((nb_Pion_Objectif != 0) && (nb_Pion_Objectif <= nb_Pion))) {


            Buzzer_Etat(BUZZER_OFF);
            P4_busy = P4_BUSY_LIBRE;
            TIMER5_Off();
            Etat_Update(ETAT_INACTIF);
        }


        //        if (Option_Pailleux==1){
        //            
        //            
        //            P4_busy = P4_BUSY_LIBRE;
        //            TIMER5_Off();
        //            Etat_Update(ETAT_INACTIF);
        //            
        //        }
        //        else{
        //        if ((nb_Pion_Objectif != 0) && (nb_Pion_Objectif <= nb_Pion)) {
        //            P4_busy = P4_BUSY_LIBRE;
        //            TIMER5_Off();
        //            Etat_Update(ETAT_INACTIF);
        //        }
        //        }



    } else if (nb_100ms_Timer_5 == nb_100ms_platine) {
        // Etat = ETAT_PLATINE;
        //         Etat_Update(ETAT_PLATINE);

        //        LED = 0;
        if ((moteur_indice == MOTEUR_1) &&(PION == METAL_PRESENT) && (Mouvement_Startup == 1)) {
            Alarme_On(ALARME_START);
            //            TIMER5_Off();
        } else {
            P4_busy = P4_BUSY_LIBRE;
            Etat_Update(ETAT_PLATINE);

            //            TIMER5_Off();
        }

        Buzzer_Etat(BUZZER_OFF);
        TIMER5_Off();
    } else {
     //   Buzzer_Etat(BUZZER_OFF);
    }

}

void IRQ_PWM(void) {

    PTIF = 0;
}

void IRQ_ADC(void) {
    switch (moteur_indice) {
        case MOTEUR_1:
            Image_Courant_Moteur_1 = ADRESH;
            Nouvelle_Valeur_ADC = 1;

            ADIF = 0;


            erreur = consigne - Image_Courant_Moteur_1;
            if (erreur >= 10) duty++;
                //else if (erreur < 0) duty--;
            else if (erreur < 0) duty += erreur;
            //else if (erreur < 0) duty=0;
            //            erreur = erreur >> 4;
            //            duty =  erreur + duty;

            if (duty > PTPERL) duty = PTPERL;
            else if (duty < 0) duty = 0;
            PDC0L = (char) (duty << 2);
            PDC0H = (char) ((duty << 2) >> 8);

            break;



            //case MOTEUR_2:
        case MOTEUR_PELLE:

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

        case MOTEUR_BEQUILLE:

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
}

void interrupt low_priority LOW_PRIORITY_IRQ(void) {

    //Detection du front montant sur le capteur pion
    if ((PIE3bits.IC1IE == 1)&&(PIR3bits.IC1IF == 1)) {
        //BUZZER = 1;
        //IRQ_PION_CHANGEMENT_ETAT();
        
           PIR3bits.IC1IF = 0;
    
    if(CAPOT==1){
      Etat_Update(ETAT_RECULE);  
    }
    
     
        
        
        //IRQ_PION_Metal_Apparait();
        //IRQ_PION_RISING_EDGE();
        //        PIR3bits.IC1IF = 0;
        //        //On active l'interruption de CAP2 afin de capter le front descendant
        //        PIR3bits.IC2QEIF = 0;
        //        if (PIE3bits.IC2QEIE == 1) {//Si l'interruption de CAP2 est déjà autorisé, alors cela veut dire qu'il n'auras pas déclenché sur le front descendant suivant la précédente interruption de cette meme fonction
        //            Alarme = ALARME_OVERLOAD_CAP_1_2;
        //        } else {
        //            PIE3bits.IC2QEIE = 1;
        //        }
        //
        //        TIMER5_On();


    } else
        //Detection du front descendant sur le capteur pion
        if ((PIE3bits.IC2QEIE == 1)&&(PIR3bits.IC2QEIF == 1)) {
        PIR3bits.IC2QEIF = 0;

        //Buzzer_Etat(BUZZER_OFF);
        //    IRQ_PION_Metal_Disparait();
        //IRQ_PION_FALLING_EDGE();
        //        PIE3bits.IC2QEIE = 0; //On désactive l'interruption du prochaine front montant
        //        PIR3bits.IC2QEIF = 0;
        //
        //        TIMER5_Off();
        //
        //        nb_100ms_Timer_5 = 0;

    } else
        if (PIE1bits.SSPIE == 1 && PIR1bits.SSPIF == 1) {
        SPI_ISR();
        //  IDLE_Enable();
    }  else
        if (PIE1bits.TX1IE == 1 && PIR1bits.TX1IF == 1) {
        EUSART1_Transmit_ISR();
        //  IDLE_Enable();
    } else if (PIE1bits.RC1IE == 1 && PIR1bits.RC1IF == 1) {
        if (RX1_ABR==0){
        EUSART1_Receive_ISR();
        }else{
    eusart1RxIndex = RCREG; // Doit etre lu pour abaisser le flag
    eusart1RxIndex = 0;
    PIR1bits.RC1IF = 0;
    RX1_ABR = 0;}
        //  IDLE_Enable();
    } else


        //Timer 0
        if (INTCONbits.TMR0IE == 1 && INTCONbits.TMR0IF == 1) {
        IRQ_TIMER_0();
        //        INTCONbits.TMR0IF = 0;
        //        //LED^=1;
        //        nb_s_fonctionnement += 1;
        //        Capteur_Capot_Compteur_Temps_S +=1;

    } else

        //Timer 5
        if (PIE3bits.TMR5IE == 1 && PIR3bits.TMR5IF == 1) {//période d'environ 130 ms
        IRQ_TIMER_5();
        //        PIR3bits.TMR5IF = 0;
        //
        //
        //        nb_100ms_Timer_5 += 1;
        //
        //
        //        if (nb_100ms_Timer_5 == nb_100ms_pion) {
        //            nb_Pion += 1;
        //            nb_s_fonctionnement = 0; //on réinitialise le compteur de temps entre pion
        //        } else if (nb_100ms_Timer_5 == nb_100ms_platine) {
        //            Etat = ETAT_PLATINE;
        //        }
        //


        //        //NOP();
        //           LED=1;
        //           LED=0;
        //        LED^=1;
        //GODONE=1;

    } else

        if ((PIE3bits.PTIE == 1) && (PIR3bits.PTIF == 1)) {
        IRQ_PWM();
        //        PTIF = 0;
        //        LED=1;
        //        LED=0;
    } else




        if ((PIE1bits.ADIE == 1) && (PIR1bits.ADIF == 1)) {
        //    PIE1bits.ADIE = 0;
        //ADIF=0;
        //LED = 1;
        //        LED = 1;

        //        LED = 0;
        IRQ_ADC();
    }


    // else{LED=1;}

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

void Surveillance_Consommation_Moteur_1_Activer(void) {
    if (Surveillance_Consommation_Moteur_1 != SURVEILLANCE_ACTIVER) {
        Surveillance_Consommation_Moteur_1 = SURVEILLANCE_ACTIVER;
        INTCON3bits.INT1IF = 0;
        INTCON3bits.INT1IE = 1; //On activera la détection surconsommation par moteur à chaque utilisation
    }
}

void Surveillance_Consommation_Moteur_1_Desactiver(void) {

    if (Surveillance_Consommation_Moteur_1 != SURVEILLANCE_DESACTIVER) {
        Surveillance_Consommation_Moteur_1 = SURVEILLANCE_DESACTIVER;
        INTCON3bits.INT1IE = 0; //On activera la détection surconsommation par moteur à chaque utilisation 
    }
}

void Surveillance_Consommation_Moteur_2_Activer(void) {
    if (Surveillance_Consommation_Moteur_2 != SURVEILLANCE_ACTIVER) {
        Surveillance_Consommation_Moteur_2 = SURVEILLANCE_ACTIVER;
        INTCON3bits.INT2IF = 0;
        INTCON3bits.INT2IE = 1; //On activera la détection surconsommation par moteur à chaque utilisation
    }
}

void Surveillance_Consommation_Moteur_2_Desactiver(void) {
    if (Surveillance_Consommation_Moteur_2 != SURVEILLANCE_DESACTIVER) {
        Surveillance_Consommation_Moteur_2 = SURVEILLANCE_DESACTIVER;
        INTCON3bits.INT2IE = 0; //On activera la détection surconsommation par moteur à chaque utilisation
    }
}

void IRQ_TIMER2(void) {
    PIR1bits.TMR2IF = 0;
    //  LED ^= 1;
    //    LED=0;
    GODONE = 1;
}

void IRQ_CAPOT(void) {
    INT0IF = 0;
//    Alarme_On(ALARME_CAPOT);
    if(PION==1){
    Etat_Update(ETAT_AVANCE);
    }
}

void IRQ_I_MOTEUR_1(void) {
        INTCON3bits.INT1IF = 0;
    Compteur_IRQ_I_Moteur_1 += 1;
    if (Compteur_IRQ_I_Moteur_1 == 0) {// <= il faut 255 évenement pour que cette condition se produise
        LED = 1;
        //INTCON3bits.INT1IF = 0;
        DRIVER_M1 = 0; //Redondant mais immédiat
        DRIVER_M2 = 0; //Redondant mais immédiat

        Alarme_On(ALARME_I_MOTEUR_1);

    }
}

void IRQ_I_MOTEUR_2(void) {
    //    if(Surveillance_Consommation_Moteur_2 == SURVEILLANCE_DESACTIVER){
    //        LED=1;
    //    }

    DRIVER_M2 = 0;
    
    while(TMR2 > 0) NOP();
    
    DRIVER_M2 = 1;
    
//    
//    duty = 0;
//    PDC1L = 0;
//    PDC1H = 0;
//
//
//nb_s_fonctionnement = 1;
//Surveillance_Consommation_Moteur_2_Desactiver();
//
//    consigne = 10; //Permet de simuler une rampe d'accélération
//

    LED^=1;
    INTCON3bits.INT2IF = 0;
    //Compteur_IRQ_I_Moteur_2 += 1;
    //Compteur_IRQ_I_Moteur_2 ++;
    
    Compteur_IRQ_I_Moteur_2 = (unsigned char) (Compteur_IRQ_I_Moteur_2 +1);
//    Compteur_IRQ_I_Moteur_2 = Compteur_IRQ_I_Moteur_2 +1;
    // Compteur_IRQ_I_Moteur_2 = 0;
//    if (Compteur_IRQ_I_Moteur_2 == 0) {// <= il faut 255 évenement pour que cette condition se produise
////////    if (Compteur_IRQ_I_Moteur_2 >= 250) {// <= il faut 255 évenement pour que cette condition se produise
////////         //LED=1;
////////        Compteur_IRQ_I_Moteur_2 = 0;
////////        //Compteur_IRQ_I_Moteur_2 = 0;
////////        //INTCON3bits.INT2IF = 0;
////////        DRIVER_M1 = 0; //Redondant mais immédiat
////////        DRIVER_M2 = 0; //Redondant mais immédiat
////////        Alarme_On(ALARME_I_MOTEUR_2);
////////    }
}
//******************************************************************************
//	FONCTION INTERRUPTION HIGH PRIORITY 
//******************************************************************************

void interrupt high_priority HIGH_PRIORITY_IRQ(void) {


    if (PIE1bits.TMR2IE == 1 && PIR1bits.TMR2IF == 1) {
        IRQ_TIMER2();
        //        PIR1bits.TMR2IF = 0;
        //        //        //NOP();
        //        //           LED=1;
        //        //           LED=0;
        //        GODONE = 1;
    }//    
    else
        if ((INTCONbits.INT0IE == 1) && (INTCONbits.INT0IF == 1)) // Capteur Capot
    {
        IRQ_CAPOT();
        //        INT0IF = 0;
        //        Alarme_On(ALARME_CAPOT);

        //        //Etat = ETAT_ALARME;
        //        Etat_Update(ETAT_ALARME);
        //        Alarme = ALARME_CAPOT;
        //        
        //        
        //        
        //        Coupe_Moteur();




    } else
        if ((INTCON3bits.INT1IE == 1)&&(INTCON3bits.INT1IF == 1)) {//Surconsommation du Moteur 1
           // INTCON3bits.INT1IF =0;
        //IRQ_I_MOTEUR_1();
        
        
#ifdef CURRENT_HARD_IRQ
         IRQ_I_MOTEUR_1();
#else
       INTCON3bits.INT1IF =0;
#endif
        
        
        //        INTCON3bits.INT1IF = 0;
        //        //Etat = ETAT_ALARME;
        //        Alarme_On(ALARME_I_MOTEUR_1);
        //        Etat_Update(ETAT_ALARME);
        //        Alarme = ALARME_I_MOTEUR_1;
        //        Coupe_Moteur();
    } else
        if ((INTCON3bits.INT2IE == 1)&&(INTCON3bits.INT2IF == 1)) {//Surconsommation du Moteur 2
        //    INTCON3bits.INT2IF = 0;
       // IRQ_I_MOTEUR_2();
        
        
#ifdef CURRENT_HARD_IRQ
IRQ_I_MOTEUR_2();
#else
       INTCON3bits.INT2IF = 0;
#endif
        //        INTCON3bits.INT2IF = 0;
        //        //Etat = ETAT_ALARME;
        //        Alarme_On(ALARME_I_MOTEUR_2);
        //        Etat_Update(ETAT_ALARME);
        //        Alarme = ALARME_I_MOTEUR_2;
        //        Coupe_Moteur();
    }


    //   else{LED=1;}


}







