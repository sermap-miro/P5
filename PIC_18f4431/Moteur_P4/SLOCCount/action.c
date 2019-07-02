

#include <xc.h>

#include "Variables.h"
#include "adc.h"
#include "pwm.h"
#include "timer.h"
#include <string.h> 
#include <stdio.h> 
#include <stdlib.h>
#include "eusart.h"
#include "horloge.h"

#include "action.h"
#include "variable_extern.h"

unsigned char Etat_Intitule(unsigned char Etat_Number) {

    switch (Etat_Number) {

        case 0: return 'I'; //Inactif
        case 1: return '!'; //Alarme
        case 2: return 'A'; //Avance
        case 3: return 'R'; //Recule
        case 4: return 'L'; //Lève la pelle
        case 5: return 'B'; //Baisse la pelle
        case 6: return 'P'; //Platine
        case 255: return 'H'; // Hard reboot

        default: return ' ';

    }
    //return ' ';

}

unsigned char Etat_Get(unsigned char Etat_Indice){
//    unsigned char Reponse;
//    unsigned char Indice;
//    Indice = NB_ACTION_LOG - 1 - Etat_Indice + Etat_Precedent_Index;
//    Indice = NB_ACTION_LOG;
//    Indice = Indice - 1;
//    Indice = Indice - Etat_Indice;
//    Indice = Indice + Etat_Precedent_Index;
//    
//    //Reponse = Etat_Log[NB_ACTION_LOG - 1 - Etat_Indice + Etat_Precedent_Index];
//    Reponse = Etat_Log[Indice];
//    return Reponse;
    
    return Etat_Log[(NB_ACTION_LOG - 1 - Etat_Indice + Etat_Precedent_Index)%NB_ACTION_LOG];
    
    
    
}

unsigned char Etat_Precedent_Get(void) {
    if (Etat_Precedent_Index == 0) return Etat_Log[NB_ACTION_LOG - 1];
    else return Etat_Log[Etat_Precedent_Index - 1];

}

void Etat_Update(unsigned char etat_new_value) {
    Etat_Log[Etat_Precedent_Index] = etat_new_value;
    Etat = etat_new_value;
    Etat_Precedent_Index++;
    if (Etat_Precedent_Index == NB_ACTION_LOG) {
        Etat_Precedent_Index = 0;
    }

}

void Init_Moteur_1(void) {

    nb_s_fonctionnement = 0;
    nb_Pion = 0;
    nb_100ms_Timer_5 = 0;
    TIMER0_On();
}

void Stop_Moteur_1(void) {

    TIMER0_Off();

}

void Check_List_Moteur_1(void) {

    EUSART1_Check_Buffer();

    if (nb_s_fonctionnement > nb_s_patinage) {

        //         Etat_Update(ETAT_INACTIF);
        Etat_Update(ETAT_ALARME);
        Alarme = ALARME_PATINAGE;


    }







}

void Init_Moteur_2(void) {

    nb_s_fonctionnement = 0;
    nb_Pion = 0;
    nb_100ms_Timer_5 = 0;
    TIMER0_On();
}

void Stop_Moteur_2(void) {

    TIMER0_Off();

}

void Check_List_Moteur_2(void) {

    EUSART1_Check_Buffer();

    if (nb_s_fonctionnement > nb_s_pelle) {

        //         Etat_Update(ETAT_INACTIF);
        Etat_Update(ETAT_INACTIF);
        //Alarme = ALARME_PATINAGE;


    }
}

void Coupe_Moteur(void) {
    TIMER2_Off();

    //PIE3bits.PTIE = 0;
    //PIE1bits.ADIE = 0;
    //    LED = 0;
    DRIVER_M1 = 0;
    DRIVER_M2 = 0;
    OVDCOND = 0b00000000;
    STOP_M1;
    STOP_M2;
    delay_ms(100);
}


//******************************************************************************
// FONCTION  MOTEUR1 AV
//******************************************************************************

void Moteur(unsigned char moteur_indice, unsigned char direction, unsigned char consigne, unsigned char option) {
    //unsigned char i; //, i_min, i_max;
    unsigned char i, i_min, i_max;
    //    unsigned int erreur;
    //    //unsigned char erreur;
    //    unsigned int erreur_accumulator;

#define ACCUMULATOR_SHIFT 2
    //    unsigned int duty = 0;
    //    unsigned char duty;
    unsigned int index;


    u_Init_PWM();

    index = 0;
    TMR2 = 0;
    TMR2IF = 0;


    switch (moteur_indice) {

        case MOTEUR_1:
            
            nb_Pion = 0;
            
            
            moteur_indice = MOTEUR_1;
            Init_ADC_Single_Shoot_I_Moteur_1();


            if (direction == AVANT) {
                AV_M1;
            } else {
                AR_M1;
            }
            PDC0L = 1 << 2;
            PDC0H = 0;
            OVDCOND = 0b00000001;
            DRIVER_M1 = 1;


            erreur = 1;
            PDC0L = ((unsigned char) erreur) << 2;
            PDC0H = ((unsigned char) erreur) >> 6;


            erreur_accumulator = 0;


            Nouvelle_Valeur_ADC = 0; //Initialisation du drapeau de fin de conversion (nouvelle image du courant disponible)
            //    direction = 0;
            //    i_min = 31;
            //    i_max = 0;
            //    while (PTDIR == 1) NOP();
            //    while (PTDIR == 0) NOP();


            //    LED = 1;

            PIE3bits.PTIE = 0;
            PIE1bits.ADIE = 1;
            PIE1bits.ADIE = 1;

            PEIE = 1;
            GIE = 1;
            TIMER2_On(); //fréquence d'echantillonnage
            ADIF = 0;

            //
            //            nb_s_fonctionnement = 0;
            Init_Moteur_1();
            do {
                Check_List_Moteur_1();
            } while (((direction == AVANT) && (Etat == ETAT_AVANCE)) | ((direction == ARRIERE) && (Etat == ETAT_RECULE)));
            Stop_Moteur_1();




            //            if (direction == AVANT) {
            //                do {
            ////                    LED = 1;
            ////                    LED = 0;
            //                    /*delay_10ms();*
            //                     */
            //                    EUSART1_Check_Buffer();
            //                    //action_EUSART1_Check_Buffer();
            //                    Check_List_Moteur_1();
            ////                    NOP();
            //                } while (Etat == ETAT_AVANCE);
            //            } else {
            //                do {
            ////                    LED = 1;
            ////                    LED = 0;
            //                    EUSART1_Check_Buffer();
            //                    Check_List_Moteur_1();
            //                    //action_EUSART1_Check_Buffer();
            //                    /*delay_10ms();*/
            ////                    NOP();
            //                } while (Etat == ETAT_RECULE);
            //            }

            //            do {
            //
            //
            //            } while ((AV_1 == 1) | (AR_1 == 1)); //AV_1


            break;

        case MOTEUR_2:

            moteur_indice = MOTEUR_2;
            Init_ADC_Single_Shoot_I_Moteur_2();


            if (direction == AVANT) {
                AV_M2;
            } else {
                AR_M2;
            }
            PDC1L = 1 << 2;
            PDC1H = 0;
            OVDCOND = 0b00000100;
            DRIVER_M2 = 1;

            erreur = 1;
            PDC1L = ((unsigned char) erreur) << 2;
            PDC1H = ((unsigned char) erreur) >> 6;


            erreur_accumulator = 0;


            Nouvelle_Valeur_ADC = 0; //Initialisation du drapeau de fin de conversion (nouvelle image du courant disponible)



            PIE3bits.PTIE = 0;
            PIE1bits.ADIE = 1;
            PIE1bits.ADIE = 1;

            PEIE = 1;
            GIE = 1;
            TIMER2_On(); //fréquence d'echantillonnage
            ADIF = 0;


            //            do {
            //
            //
            //            } while ((AV_2 == 1) | (AR_2 == 1)); //AV_1

            //            if (direction == MONTE) {
            //                do {
            //                    EUSART1_Check_Buffer();
            //                } while (Etat == ETAT_PELLE_LEVE);
            //            } else {
            //                do {
            //                    EUSART1_Check_Buffer();
            //                } while (Etat == ETAT_PELLE_BAISSE);
            //            }

            do {
                //Check_List_Moteur_1();
                //EUSART1_Check_Buffer();
                Check_List_Moteur_2();
            } while (((direction == MONTE) && (Etat == ETAT_PELLE_LEVE)) | ((direction == DESCEND) && (Etat == ETAT_PELLE_BAISSE)));



            break;

        default:
            break;
    }



    PIE3bits.PTIE = 0;
    PIE1bits.ADIE = 0;


    Coupe_Moteur();

    //    TIMER2_Off();
    //
    //    LED = 0;
    //    DRIVER_M1 = 0;
    //    DRIVER_M2 = 0;
    //    OVDCOND = 0b00000000;
    //    STOP_M1;
    //    STOP_M2;
    //  LED = 0;

    //    DRIVER_M2 = 0;
    //    OVDCOND = 0b00000000;
    //    STOP_M1;
}


