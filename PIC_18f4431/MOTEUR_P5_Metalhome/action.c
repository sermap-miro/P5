

#include <xc.h>

#include "Variables.h"
#include "adc.h"
#include "pwm.h"
#include "timer.h"
#include <string.h> 
#include <stdio.h> 
#include <stdlib.h>
#include "eusart.h"
#include "spi.h"
#include "horloge.h"

#include "action.h"
#include "variable_extern.h"
#include "interrupt.h"
#include "alarme.h"
#include "pion.h"

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

unsigned char Etat_Get(unsigned char Etat_Indice) {
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

    return Etat_Log[(unsigned char) ((NB_ACTION_LOG - 1 - Etat_Indice + Etat_Precedent_Index) % NB_ACTION_LOG)];



}

unsigned char Etat_Precedent_Get(void) {
    if (Etat_Precedent_Index == 0) return Etat_Log[NB_ACTION_LOG - 1];
    else return Etat_Log[(unsigned char) (Etat_Precedent_Index - 1)];

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
    //    Capteur_Capot_Nb_Evenement = Capteur_Capot_Nb_Evenement_Autoriser;
    //    Patinage_Nb_Essai = Patinage_Nb_Essai_Autoriser;




    Capteur_Capot_Compteur_Temps_S = 0; //


    nb_s_fonctionnement = 0;
    nb_Pion = 0;
    nb_100ms_Timer_5 = 0;
    //nb_Pion_Objectif=0;//redondant
    TIMER0_On();//Permet l'activation retardé de la surveillance de la surconsommation de courant

    //INTCON3bits.INT1IE = 1; // Autorisation d'interruption sur surconsommation de courant <= se fait désormais dans la fonction Surveillance_Consommation_Moteur_1_Activer()
    Compteur_IRQ_I_Moteur_1 = 0;
}

void Stop_Moteur_1(void) {

    TIMER0_Off();

    //INTCON3bits.INT1IE =0; // Autorisation d'interruption sur surconsommation de courant
}

void Check_List_Moteur_Metalhome(void) {

    
    if(MOT1_COURANT == 0){
     Compteur_IRQ_I_Moteur_1 = 0;
    }
    
    
    EUSART1_Check_Buffer();
        SPI_Check_Buffer();

//    if (nb_s_fonctionnement > nb_s_patinage) {
//
//        //         Etat_Update(ETAT_INACTIF);
//        //        Etat_Update(ETAT_ALARME);
//        //        Alarme = ALARME_PATINAGE;
//        Alarme_On(ALARME_PATINAGE);
//
//    }


//    if (Capteur_Capot_Compteur_Temps_S > 180) {//si on a pas d'évenement capot depuis 3 min
//        Capteur_Capot_Nb_Evenement = Capteur_Capot_Nb_Evenement_Autoriser;
//        Capteur_Capot_Compteur_Temps_S = 0;
//    }

        if ((direction == AVANT) && (CAPOT == 1)) {
            Etat_Update(ETAT_INACTIF);
        }
        if ((direction == ARRIERE) && (PION == 1)) {
            Etat_Update(ETAT_INACTIF);
        }
//  ((direction == AVANT) && (Etat == ETAT_AVANCE) )
//                    |
//                    ((direction == ARRIERE) && (Etat == ETAT_RECULE))
  
  

}

void Check_List_Moteur_1(void) {

    
    if(MOT1_COURANT == 0){
     Compteur_IRQ_I_Moteur_1 = 0;
    }
    
    
    EUSART1_Check_Buffer();
        SPI_Check_Buffer();

    if (nb_s_fonctionnement > nb_s_patinage) {

        //         Etat_Update(ETAT_INACTIF);
        //        Etat_Update(ETAT_ALARME);
        //        Alarme = ALARME_PATINAGE;
        Alarme_On(ALARME_PATINAGE);

    }


    if (Capteur_Capot_Compteur_Temps_S > 180) {//si on a pas d'évenement capot depuis 3 min
        Capteur_Capot_Nb_Evenement = Capteur_Capot_Nb_Evenement_Autoriser;
        Capteur_Capot_Compteur_Temps_S = 0;
    }



}

void Init_Moteur_2(void) {

    //    nb_s_fonctionnement = 0;
    //    nb_Pion = 0;
    //    nb_100ms_Timer_5 = 0;
    nb_s_fonctionnement = 0;
    nb_Pion = 0;
    nb_100ms_Timer_5 = 0;
    TIMER0_On();

    //INTCON3bits.INT2IE = 1; //Autorisation d'interruption sur surconsommation de courant <= se fait désormais dans la fonction Surveillance_Consommation_Moteur_2_Activer()
    Compteur_IRQ_I_Moteur_2 = 0;
    LED=0;
}

void Stop_Moteur_2(void) {

    TIMER0_Off();
   // INTCON3bits.INT2IE = 0; //Autorisation d'interruption sur surconsommation de courant

}

void Check_List_Moteur_2(void) {

    
//    
//    if(MOT2_COURANT == 0){
//     Compteur_IRQ_I_Moteur_2 = 0;
//    }
//    
    
    EUSART1_Check_Buffer();
        SPI_Check_Buffer();

    //if (nb_s_fonctionnement > nb_s_pelle) {
    //if( (nb_s_fonctionnement > nb_s_pelle) |  (Image_Courant_Moteur_2 >= Pelle_I_Max))    {
//    if ((nb_s_fonctionnement >= nb_s_pelle) | ((nb_s_fonctionnement > 2) &&((Image_Courant_Moteur_2   ) >= Pelle_I_Max))) {// 19 Avril (nb_s_fonctionnement >= nb_s_pelle) au lieu de (nb_s_fonctionnement > nb_s_pelle)
//    //if ((nb_s_fonctionnement >= nb_s_pelle) | ((nb_s_fonctionnement > 2) &&((Image_Courant_Moteur_2   ) >= Pelle_I_Max))) {// 19 Avril (nb_s_fonctionnement >= nb_s_pelle) au lieu de (nb_s_fonctionnement > nb_s_pelle)
        //if( (nb_s_fonctionnement > nb_s_pelle) |  (  (nb_s_fonctionnement > 4)              &&(Image_Courant_Moteur_2 >= Pelle_I_Max)   )        )    {

        //         Etat_Update(ETAT_INACTIF);
    
    
     if ((nb_s_fonctionnement >= nb_s_pelle) | ((nb_s_fonctionnement > 2) &&((Image_Courant_Moteur_2   ) >= Pelle_I_Max))) {// 19 Avril (nb_s_fonctionnement >= nb_s_pelle) au lieu de (nb_s_fonctionnement > nb_s_pelle)
   //if (nb_s_fonctionnement >= nb_s_pelle) {// 19 Avril (nb_s_fonctionnement >= nb_s_pelle) au lieu de (nb_s_fonctionnement > nb_s_pelle)
  
    
        P4_busy = P4_BUSY_LIBRE;
        Etat_Update(ETAT_INACTIF);
        //Alarme = ALARME_PATINAGE;


    }
}

void Init_Moteur_Bequille(void) {

    //    nb_s_fonctionnement = 0;
    //    nb_Pion = 0;
    //    nb_100ms_Timer_5 = 0;
    nb_s_fonctionnement = 0;
    nb_Pion = 0;
    nb_100ms_Timer_5 = 0;
    TIMER0_On();

    INTCON3bits.INT2IE = 1; //Autorisation d'interruption sur surconsommation de courant
    Compteur_IRQ_I_Moteur_2 = 0;

}

void Stop_Moteur_Bequille(void) {

    TIMER0_Off();
    INTCON3bits.INT2IE = 0; //Autorisation d'interruption sur surconsommation de courant

}

void Check_List_Moteur_Bequille(void) {

    
    
    if(MOT2_COURANT == 0){
     Compteur_IRQ_I_Moteur_2 = 0;
    }
    
    
    
    EUSART1_Check_Buffer();
        SPI_Check_Buffer();

    //if (nb_s_fonctionnement > nb_s_bequille) {
    // if( (nb_s_fonctionnement > nb_s_bequille) |  (  (nb_s_fonctionnement > 4)              &&(Image_Courant_Moteur_2 >= Bequille_I_Max)   )        )    {
    if ((nb_s_fonctionnement >= nb_s_bequille) | ((nb_s_fonctionnement > 2) &&(Image_Courant_Moteur_2 /5 >= Bequille_I_Max))) {//19 Avril

        //         Etat_Update(ETAT_INACTIF);
        P4_busy = P4_BUSY_LIBRE;
        Etat_Update(ETAT_INACTIF);
        //Alarme = ALARME_PATINAGE;


    }
}

void Coupe_Moteur(void) {
    TIMER2_Off();


#ifdef PROTO_2

    RELAIS = 0; //Relaxation du relais s'il était en cours d'utilisation

#endif

    //PIE3bits.PTIE = 0;
    //PIE1bits.ADIE = 0;
    //    LED = 0;
    DRIVER_M1 = 0;
    DRIVER_M2 = 0;
    OVDCOND = 0b00000000;
    STOP_M1;
    STOP_M2;
    //delay_ms(100);
}

void Init_Moteur_Pelle(void) {

    //    nb_s_fonctionnement = 0;
    //    nb_Pion = 0;
    //    nb_100ms_Timer_5 = 0;
    TIMER0_On();

    INTCON3bits.INT2IE = 1; //Autorisation d'interruption sur surconsommation de courant
    Compteur_IRQ_I_Moteur_2 = 0;
    
}

void Stop_Moteur_Pelle(void) {

    TIMER0_Off();
    INTCON3bits.INT2IE = 0; //Autorisation d'interruption sur surconsommation de courant

}

void Check_List_Moteur_Pelle(void) {

    
    
    EUSART1_Check_Buffer();
        SPI_Check_Buffer();

    if(MOT2_COURANT == 0){
     Compteur_IRQ_I_Moteur_2 = 0;
    }
    
    if (nb_s_fonctionnement >= nb_s_pelle) {//19 Avril

        //         Etat_Update(ETAT_INACTIF);
        Etat_Update(ETAT_INACTIF);
        //Alarme = ALARME_PATINAGE;


    }
}
//
//void Moteur_Pelle(unsigned char direction, unsigned char option) {
//
//    u_Init_PWM();
//
//    TMR2 = 0;
//    TMR2IF = 0;
//
//
//
//#ifdef PROTO_2
//
//    RELAIS = 1;
//
//#endif
//
//
//    moteur_indice = MOTEUR_PELLE;
//    Init_ADC_Single_Shoot_I_Moteur_2();
//
//
//    if (direction == MONTE) {
//        AV_M2;
//    } else {
//        AR_M2;
//    }
//    PDC1L = 1 << 2;
//    PDC1H = 0;
//    OVDCOND = 0b00000100;
//    DRIVER_M2 = 1;
//
//    erreur = 1; //erreur entre la consigne et la mesure
//    PDC1L = (unsigned char) (((unsigned char) erreur) << 2);
//    PDC1H = (unsigned char) (((unsigned char) erreur) >> 6);
//
//
//    erreur_accumulator = 0;
//
//
//    Nouvelle_Valeur_ADC = 0; //Initialisation du drapeau de fin de conversion (nouvelle image du courant disponible)
//
//
//
//    PIE3bits.PTIE = 0;
//    PIE1bits.ADIE = 1;
//    PIE1bits.ADIE = 1;
//
//    PEIE = 1;
//    GIE = 1;
//    TIMER2_On(); //fréquence d'echantillonnage
//    ADIF = 0;
//
//
//    //            do {
//    //
//    //
//    //            } while ((AV_2 == 1) | (AR_2 == 1)); //AV_1
//
//    //            if (direction == MONTE) {
//    //                do {
//    //                    EUSART1_Check_Buffer();
//    //                } while (Etat == ETAT_PELLE_LEVE);
//    //            } else {
//    //                do {
//    //                    EUSART1_Check_Buffer();
//    //                } while (Etat == ETAT_PELLE_BAISSE);
//    //            }
//    Init_Moteur_Pelle();
//    do {
//        //Check_List_Moteur_1();
//        //EUSART1_Check_Buffer();
//        Check_List_Moteur_Pelle();
//    } while (((direction == MONTE) && (Etat == ETAT_PELLE_LEVE)) | ((direction == DESCEND) && (Etat == ETAT_PELLE_BAISSE)));
//
//    Stop_Moteur_Pelle();
//
//
//}
//
//
//
//






//
//
//
////******************************************************************************
//// FONCTION  MOTEUR
////******************************************************************************
//
//void Moteur(unsigned char moteur_indice, unsigned char direction, unsigned char consigne, unsigned char option) {
//    //unsigned char i; //, i_min, i_max;
//    unsigned char i, i_min, i_max;
//    unsigned char Option_Temps_S;
//    //    unsigned int erreur;
//    //    //unsigned char erreur;
//    //    unsigned int erreur_accumulator;
//
//#define ACCUMULATOR_SHIFT 2
//    //    unsigned int duty = 0;
//    //    unsigned char duty;
//    unsigned int index;
//
//
//    u_Init_PWM();
//
//    index = 0;
//    TMR2 = 0;
//    TMR2IF = 0;
//
//
//    switch (moteur_indice) {
//
//        case MOTEUR_1:
//
//            if ((!(option & OPTION_MARCHE_FORCER))
//                    //|
//                    //(!(option & OPTION_MARCHE_FORCER))
//                    ) {//On active le détecteur de capot (sauf si option activé)
//
//                Capteur_Capot_On();
//
//            }
//            //if (option == OPTION_MARCHE_FORCER){
//            //    
//            //}else{
//            //            Capteur_Capot_On();
//            //}
//
//
//            moteur_indice = MOTEUR_1;
//            Init_ADC_Single_Shoot_I_Moteur_1();
//
//
//            if (direction == AVANT) {
//                AV_M1;
//            } else {
//                AR_M1;
//            }
//            PDC0L = 1 << 2;
//            PDC0H = 0;
//            OVDCOND = 0b00000001;
//            DRIVER_M1 = 1;
//
//
//            erreur = 1;
//            PDC0L = (unsigned char) (((unsigned char) erreur) << 2);
//            PDC0H = (unsigned char) (((unsigned char) erreur) >> 6);
//
//
//            erreur_accumulator = 0;
//
//
//            Nouvelle_Valeur_ADC = 0; //Initialisation du drapeau de fin de conversion (nouvelle image du courant disponible)
//            //    direction = 0;
//            //    i_min = 31;
//            //    i_max = 0;
//            //    while (PTDIR == 1) NOP();
//            //    while (PTDIR == 0) NOP();
//
//
//            //    LED = 1;
//
//            PIE3bits.PTIE = 0;
//            PIE1bits.ADIE = 1;
//
//            PEIE = 1;
//            GIE = 1;
//            TIMER2_On(); //fréquence d'echantillonnage
//            ADIF = 0;
//
//            //
//            //            nb_s_fonctionnement = 0;
//            Init_Moteur_1();
//
//            if (option & OPTION_TEMPS) {//On demande un mouvement basé sur le temps
//                do {
//                    EUSART1_Check_Buffer();
//                    //LED^=1;
//                } while (nb_s_fonctionnement < (option >> 4)); //les quatres bit de poid fort de l'option détermine le temps a fonctionner en dure
//                Stop_Moteur_1();
//                Capteur_Capot_Off();
//
//
//                Etat_Update(ETAT_INACTIF);
//#ifndef DEBUG
//                //    delay_1s();
//                //    delay_1s();
//                //    delay_1s();
//#endif
//
//
//
//            } else {//On demande d'avancer jusqu'à la prochaine platine
//
//                nb_Pion = 0;
//
//                Mouvement_Startup = 1;
//#ifdef PROTO_2      
//                if (PION == METAL_PRESENT) {//Si lors du démarrage du moteur
//                    //le capteur PION est activé, alors on défini le temps d'une platine comme
//                    //étant le double de celui d'origine
//                    //pour ne pas prendre une fausse platine, par
//                    nb_100ms_platine = 2 * NB_100MS_PLATINE;
//                    
//                TIMER5_On();//Et on démarre
//                }
//#endif
//                do {
//                    //LED^=1;
//                    Check_List_Moteur_1();
//                } while (
//                        ((direction == AVANT) && (Etat == ETAT_AVANCE))
//                        |
//                        ((direction == ARRIERE) && (Etat == ETAT_RECULE))
//
//                        );
//
//
//#ifdef PROTO_2
////                if (Mouvement_Startup == 1) {
////                    Alarme_On(ALARME_START);
////                }
//#endif      
//
//                Stop_Moteur_1();
//                Capteur_Capot_Off();
//
//
//
//
//            }
//
//            //            Stop_Moteur_1();
//            //            Capteur_Capot_Off();
//
//
//
//            //            if (direction == AVANT) {
//            //                do {
//            ////                    LED = 1;
//            ////                    LED = 0;
//            //                    /*delay_10ms();*
//            //                     */
//            //                    EUSART1_Check_Buffer();
//            //                    //action_EUSART1_Check_Buffer();
//            //                    Check_List_Moteur_1();
//            ////                    NOP();
//            //                } while (Etat == ETAT_AVANCE);
//            //            } else {
//            //                do {
//            ////                    LED = 1;
//            ////                    LED = 0;
//            //                    EUSART1_Check_Buffer();
//            //                    Check_List_Moteur_1();
//            //                    //action_EUSART1_Check_Buffer();
//            //                    /*delay_10ms();*/
//            ////                    NOP();
//            //                } while (Etat == ETAT_RECULE);
//            //            }
//
//            //            do {
//            //
//            //
//            //            } while ((AV_1 == 1) | (AR_1 == 1)); //AV_1
//
//
//            break;
//
//        case MOTEUR_PELLE://MOTEUR_2
//
//
//#ifdef PROTO_2
//
//            RELAIS = 1;
//
//#endif
//
//
//            moteur_indice = MOTEUR_PELLE;
//            Init_ADC_Single_Shoot_I_Moteur_2();
//
//
//            if (direction == MONTE) {
//                AV_M2;
//            } else {
//                AR_M2;
//            }
//            PDC1L = 1 << 2;
//            PDC1H = 0;
//            OVDCOND = 0b00000100;
//            DRIVER_M2 = 1;
//
//            erreur = 1; //erreur entre la consigne et la mesure
//            PDC1L = (unsigned char) (((unsigned char) erreur) << 2);
//            PDC1H = (unsigned char) (((unsigned char) erreur) >> 6);
//
//
//            erreur_accumulator = 0;
//
//
//            Nouvelle_Valeur_ADC = 0; //Initialisation du drapeau de fin de conversion (nouvelle image du courant disponible)
//
//
//
//            PIE3bits.PTIE = 0;
//            PIE1bits.ADIE = 1;
//            PIE1bits.ADIE = 1;
//
//            PEIE = 1;
//            GIE = 1;
//            TIMER2_On(); //fréquence d'echantillonnage
//            ADIF = 0;
//
//
//            //            do {
//            //
//            //
//            //            } while ((AV_2 == 1) | (AR_2 == 1)); //AV_1
//
//            //            if (direction == MONTE) {
//            //                do {
//            //                    EUSART1_Check_Buffer();
//            //                } while (Etat == ETAT_PELLE_LEVE);
//            //            } else {
//            //                do {
//            //                    EUSART1_Check_Buffer();
//            //                } while (Etat == ETAT_PELLE_BAISSE);
//            //            }
//            Init_Moteur_2();
//            do {
//                //Check_List_Moteur_1();
//                //EUSART1_Check_Buffer();
//                Check_List_Moteur_2();
//            } while (((direction == MONTE) && (Etat == ETAT_PELLE_LEVE)) | ((direction == DESCEND) && (Etat == ETAT_PELLE_BAISSE)));
//
//
//
//            break;
//
//
//
//
//
//
//
//
//        case MOTEUR_BEQUILLE:
//
//
//#ifdef PROTO_2
//
//            RELAIS = 0;
//
//#endif
//
//
//            moteur_indice = MOTEUR_BEQUILLE;
//            Init_ADC_Single_Shoot_I_Moteur_2();
//
//
//            if (direction == MONTE) {
//                AV_M2;
//            } else {
//                AR_M2;
//            }
//            PDC1L = 1 << 2;
//            PDC1H = 0;
//            OVDCOND = 0b00000100;
//            DRIVER_M2 = 1;
//
//            erreur = 1; //erreur entre la consigne et la mesure
//            PDC1L = (unsigned char) (((unsigned char) erreur) << 2);
//            PDC1H = (unsigned char) (((unsigned char) erreur) >> 6);
//
//
//            erreur_accumulator = 0;
//
//
//            Nouvelle_Valeur_ADC = 0; //Initialisation du drapeau de fin de conversion (nouvelle image du courant disponible)
//
//
//
//            PIE3bits.PTIE = 0;
//            PIE1bits.ADIE = 1;
//            PIE1bits.ADIE = 1;
//
//            PEIE = 1;
//            GIE = 1;
//            TIMER2_On(); //fréquence d'echantillonnage
//            ADIF = 0;
//
//
//            //            do {
//            //
//            //
//            //            } while ((AV_2 == 1) | (AR_2 == 1)); //AV_1
//
//            //            if (direction == MONTE) {
//            //                do {
//            //                    EUSART1_Check_Buffer();
//            //                } while (Etat == ETAT_PELLE_LEVE);
//            //            } else {
//            //                do {
//            //                    EUSART1_Check_Buffer();
//            //                } while (Etat == ETAT_PELLE_BAISSE);
//            //            }
//            Init_Moteur_Bequille();
//            do {
//                //Check_List_Moteur_1();
//                //EUSART1_Check_Buffer();
//                Check_List_Moteur_Bequille();
//            } while (((direction == MONTE) && (Etat == ETAT_PELLE_LEVE)) | ((direction == DESCEND) && (Etat == ETAT_PELLE_BAISSE)));
//
//
//
//            break;
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//        default:
//            break;
//    }
//
//
//
//    PIE3bits.PTIE = 0;
//    PIE1bits.ADIE = 0;
//
//
//    Coupe_Moteur();
//    delay_s(1);
//    //delay_1s();
//#ifndef DEBUG
//    //    delay_1s();
//    //    delay_1s();
//#endif
//
//
//}
//




//******************************************************************************
// FONCTION  DEPLACEMENT SUIVANT Z
//******************************************************************************

void Mouvement_Bequille(unsigned char direction, unsigned char type_consigne, unsigned char option) {
    unsigned char i, i_min, i_max;
    unsigned char Option_Temps_S;
    //    unsigned int erreur;
    //    //unsigned char erreur;
    //    unsigned int erreur_accumulator;
    //    LED=1;
    //INTCON3bits.INT2IE = 1; //On activera la détection surconsommation par moteur à chaque utilisation
   // Surveillance_Consommation_Moteur_2_Activer();// Supprime les fausses détection de surconsommation au démarrage des moteurs
Surveillance_Consommation_Moteur_2_Desactiver();

Detection_Pion_Off();


    nb_s_bequille = option;


    consigne = 10; //Permet de simuler une rampe d'accélération


#define ACCUMULATOR_SHIFT 2
    //    unsigned int duty = 0;
    //    unsigned char duty;
    unsigned int index;


    u_Init_PWM();

    index = 0;
    TMR2 = 0;
    TMR2IF = 0;


#ifdef PROTO_2

    RELAIS = 1;

#endif


    moteur_indice = MOTEUR_BEQUILLE;
    Init_ADC_Single_Shoot_I_Moteur_2();


    if (direction == RENTRE) {
        AV_M2;
    } else {
        AR_M2;
    }
    PDC1L = 1 << 2;
    PDC1H = 0;
    OVDCOND = 0b00000100;
    DRIVER_M2 = 1;

    erreur = 1; //erreur entre la consigne et la mesure
    PDC1L = (unsigned char) (((unsigned char) erreur) << 2);
    PDC1H = (unsigned char) (((unsigned char) erreur) >> 6);


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
    Init_Moteur_Bequille();
    do {
        //Check_List_Moteur_1();
        //EUSART1_Check_Buffer();
        Check_List_Moteur_Bequille();
    } while (((direction == RENTRE) && (Etat == ETAT_RENTRE_BEQUILLE)) | ((direction == SORT) && (Etat == ETAT_SORT_BEQUILLE)));



    PIE3bits.PTIE = 0;
    PIE1bits.ADIE = 0;



#ifdef PROTO_2

    RELAIS = 0;

#endif

    //INTCON3bits.INT2IE = 0; //On activera la détection surconsommation par moteur à chaque utilisation
    Surveillance_Consommation_Moteur_2_Desactiver();

    Coupe_Moteur();
    delay_s(1);
    //delay_1s();
#ifndef DEBUG
    //    delay_1s();
    //    delay_1s();
#endif

    //    LED=0;

}





//******************************************************************************
// FONCTION  DEPLACEMENT SUIVANT Z
//******************************************************************************

void Mouvement_Z(unsigned char direction, unsigned char type_consigne, unsigned char option) {
    unsigned char i, i_min, i_max;
    unsigned char Option_Temps_S;
    //    unsigned int erreur;
    //    //unsigned char erreur;
    //    unsigned int erreur_accumulator;


    //INTCON3bits.INT2IE = 1; //On activera la détection surconsommation par moteur à chaque utilisation
    //Surveillance_Consommation_Moteur_2_Activer();// Supprime les fausses détection de surconsommation au démarrage des moteurs
Surveillance_Consommation_Moteur_2_Desactiver();

Detection_Pion_Off();


    nb_s_pelle = option;


    consigne = 10; //Permet de simuler une rampe d'accélération


#define ACCUMULATOR_SHIFT 2
    //    unsigned int duty = 0;
    //    unsigned char duty;
    unsigned int index;


    u_Init_PWM();

    index = 0;
    TMR2 = 0;
    TMR2IF = 0;



#ifdef PROTO_2

    RELAIS = 0;

#endif


    moteur_indice = MOTEUR_PELLE;
    Init_ADC_Single_Shoot_I_Moteur_2();


    if (direction == MONTE) {
        AV_M2;
    } else {
        AR_M2;
    }
    PDC1L = 1 << 2;
    PDC1H = 0;
    OVDCOND = 0b00000100;
    DRIVER_M2 = 1;

    erreur = 1; //erreur entre la consigne et la mesure
    PDC1L = (unsigned char) (((unsigned char) erreur) << 2);
    PDC1H = (unsigned char) (((unsigned char) erreur) >> 6);


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
    Init_Moteur_2();
    do {
        //Check_List_Moteur_1();
        //EUSART1_Check_Buffer();
        Check_List_Moteur_2();
    } while (((direction == MONTE) && (Etat == ETAT_PELLE_LEVE)) | ((direction == DESCEND) && (Etat == ETAT_PELLE_BAISSE)));



    PIE3bits.PTIE = 0;
    PIE1bits.ADIE = 0;


#ifdef PROTO_2

    RELAIS = 0;

#endif



    //INTCON3bits.INT2IE = 0; //On activera la détection surconsommation par moteur à chaque utilisation
    Surveillance_Consommation_Moteur_2_Desactiver();

    Coupe_Moteur();
    delay_s(1);
    //delay_1s();
#ifndef DEBUG
    //    delay_1s();
    //    delay_1s();
#endif



}

//void X(unsigned char direction, unsigned char type_consigne, unsigned char option) {
//
//Mouvement(direction, type_consigne, option); }
//******************************************************************************
// FONCTION  DEPLACEMENT SUIVANT X
//******************************************************************************

void Mouvement_X(unsigned char direction, unsigned char type_consigne, unsigned char option) {
    //unsigned char i; //, i_min, i_max;
    unsigned char i, i_min, i_max;
    unsigned char Option_Temps_S;
    
    //bit Detection_Pion_Activation;
    //    unsigned int erreur;
    //    //unsigned char erreur;
    //    unsigned int erreur_accumulator;
    //char Consigne_Backup;
    //char Consigne_

    //Consigne_Max = consigne;
    consigne = 10; //Permet de simuler une rampe d'accélération
    //consigne = 14;//Permet de simuler une rampe d'accélération



    //INTCON3bits.INT1IE = 1; //On activera la détection surconsommation par moteur à chaque utilisation 
   // Surveillance_Consommation_Moteur_1_Activer(); // Supprime les fausses détection de surconsommation au démarrage des moteurs
Surveillance_Consommation_Moteur_1_Desactiver();


#define ACCUMULATOR_SHIFT 2
    //    unsigned int duty = 0;
    //    unsigned char duty;
    unsigned int index;


    u_Init_PWM();

    index = 0;
    TMR2 = 0;
    TMR2IF = 0;




    if ((!(option & OPTION_MARCHE_FORCER))
            //|
            //(!(option & OPTION_MARCHE_FORCER))
            ) {//On active le détecteur de capot (sauf si option activé)

        Capteur_Capot_On();

    }
    //if (option == OPTION_MARCHE_FORCER){
    //    
    //}else{
    //            Capteur_Capot_On();
    //}


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
    PDC0L = (unsigned char) (((unsigned char) erreur) << 2);
    PDC0H = (unsigned char) (((unsigned char) erreur) >> 6);


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

    PEIE = 1;
    GIE = 1;
    TIMER2_On(); //fréquence d'echantillonnage
    ADIF = 0;

    //
    //            nb_s_fonctionnement = 0;
    Init_Moteur_1();


    switch (type_consigne) {
        case TYPE_MOUVEMENT_TEMPS:
            nb_Pion_Objectif = 2;
            //nb_s_fonctionnement_souhaiter = option;
            nb_s_fonctionnement_souhaiter = (unsigned char) (option >> 4);



            if (option & OPTION_TRIPLE) {//On active le détecteur de capot (sauf si option activé)

                nb_s_fonctionnement_souhaiter *= 3;

            }
            
            if (Option_Pailleux==1){
//                
//            Detection_Pion_Init();
//            Detection_Pion_On();
//            
            
            

            //nb_s_fonctionnement_souhaiter = (unsigned char) (option);
            //  if (option & OPTION_TEMPS) {//On demande un mouvement basé sur le temps
            do {
                EUSART1_Check_Buffer();
        SPI_Check_Buffer();
                
                
             //   if(nb_s_fonctionnement)
//            Detection_Pion_Init();
//            Detection_Pion_On();
            
                
                
                //LED^=1;
                // } while (nb_s_fonctionnement < (option >> 4)); //les quatres bit de poid fort de l'option détermine le temps a fonctionner en dure
            } while(
            ((Etat == ETAT_AVANCE) | (Etat == ETAT_RECULE))
            &&
             (nb_s_fonctionnement < nb_s_fonctionnement_souhaiter)
                    )
                    ; 
            
                 
            }
            else{
                
                      //nb_s_fonctionnement_souhaiter = (unsigned char) (option);
            //  if (option & OPTION_TEMPS) {//On demande un mouvement basé sur le temps
            do {
                EUSART1_Check_Buffer();
        SPI_Check_Buffer();
                //LED^=1;
                // } while (nb_s_fonctionnement < (option >> 4)); //les quatres bit de poid fort de l'option détermine le temps a fonctionner en dure
            } while(nb_s_fonctionnement < nb_s_fonctionnement_souhaiter); 
            }

           
                    
            Stop_Moteur_1();
            Capteur_Capot_Off();


            if ((Etat == ETAT_AVANCE) | (Etat == ETAT_RECULE)) {

            Etat_Update(ETAT_INACTIF);
            P4_busy = P4_BUSY_LIBRE;
            
            }
            
            
            
            
#ifndef DEBUG
            //    delay_1s();
            //    delay_1s();
            //    delay_1s();
#endif

            break;

            //} else {//On demande d'avancer jusqu'à la prochaine platine
        case TYPE_MOUVEMENT_PION:
            nb_Pion_Objectif = option;
            nb_Pion = 0;

            //            if(PION == METAL_PRESENT){
            //            Mouvement_Startup = 1;
            //            }else{
            //            Mouvement_Startup = 0; 
            //            }

            Detection_Pion_Init();
            Detection_Pion_On();



#ifdef DEBUG  
            //            TRISCbits.TRISC4 = 1;// I MOT 1
            //            TRISCbits.TRISC5 = 1;// I MOT 1
#endif






            //LED=0;
            do {
                //LED=TRISCbits.TRISC4 ;
                //LED^=1;
                //LED=PORTCbits.RC4;
                //LED=PORTCbits.RC5;
                // LED=RC4;
                //LED=RC5;
                //LED^=1;
                Check_List_Moteur_1();
            } while (
                    ((direction == AVANT) && (Etat == ETAT_AVANCE))
                    |
                    ((direction == ARRIERE) && (Etat == ETAT_RECULE))

                    );


            Detection_Pion_Off();

#ifdef PROTO_2
            //            if (Mouvement_Startup == 1) {
            //                Alarme_On(ALARME_START);
            //            }
#endif      

            Stop_Moteur_1();
            Capteur_Capot_Off();

            break;


        default: break;


    }





    //            Stop_Moteur_1();
    //            Capteur_Capot_Off();



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



    PIE3bits.PTIE = 0;
    PIE1bits.ADIE = 0;

    Surveillance_Consommation_Moteur_1_Desactiver(); //On activera la détection surconsommation par moteur à chaque utilisation
    //INTCON3bits.INT1IE = 0; //On activera la détection surconsommation par moteur à chaque utilisation 
    Coupe_Moteur();
    //delay_s(1);//A utiliser de préférence (scrute le tampon RS232)
    //delay_1s();//A éviter
#ifndef DEBUG
    //    delay_1s();
    //    delay_1s();
#endif


}



//void X(unsigned char direction, unsigned char type_consigne, unsigned char option) {
//
//Mouvement(direction, type_consigne, option); }
//******************************************************************************
// FONCTION  DEPLACEMENT SUIVANT X
//******************************************************************************

void Mouvement_X_Metalhome(unsigned char direction) {
    //unsigned char i; //, i_min, i_max;
    unsigned char i, i_min, i_max;
    unsigned char Option_Temps_S;
    
    //bit Detection_Pion_Activation;
    //    unsigned int erreur;
    //    //unsigned char erreur;
    //    unsigned int erreur_accumulator;
    //char Consigne_Backup;
    //char Consigne_

    //Consigne_Max = consigne;
    consigne = 10; //Permet de simuler une rampe d'accélération
    //consigne = 14;//Permet de simuler une rampe d'accélération



    //INTCON3bits.INT1IE = 1; //On activera la détection surconsommation par moteur à chaque utilisation 
   // Surveillance_Consommation_Moteur_1_Activer(); // Supprime les fausses détection de surconsommation au démarrage des moteurs
Surveillance_Consommation_Moteur_1_Desactiver();


#define ACCUMULATOR_SHIFT 2
    //    unsigned int duty = 0;
    //    unsigned char duty;
    unsigned int index;


    u_Init_PWM();

    index = 0;
    TMR2 = 0;
    TMR2IF = 0;




//    if ((!(option & OPTION_MARCHE_FORCER))
//            //|
//            //(!(option & OPTION_MARCHE_FORCER))
//            ) {//On active le détecteur de capot (sauf si option activé)
//
//        Capteur_Capot_On();
//
//    }
    //if (option == OPTION_MARCHE_FORCER){
    //    
    //}else{
    //            Capteur_Capot_On();
    //}


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
    PDC0L = (unsigned char) (((unsigned char) erreur) << 2);
    PDC0H = (unsigned char) (((unsigned char) erreur) >> 6);


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

    PEIE = 1;
    GIE = 1;
    TIMER2_On(); //fréquence d'echantillonnage
    ADIF = 0;

    //
    //            nb_s_fonctionnement = 0;
    Init_Moteur_1();


//    switch (type_consigne) {
//        case TYPE_MOUVEMENT_TEMPS:
////            nb_Pion_Objectif = 2;
//            //nb_s_fonctionnement_souhaiter = option;
////            nb_s_fonctionnement_souhaiter = (unsigned char) (option >> 4);
//
//
//
////            if (option & OPTION_TRIPLE) {//On active le détecteur de capot (sauf si option activé)
////
////                nb_s_fonctionnement_souhaiter *= 3;
////
////            }
//            
////            if (Option_Pailleux==1){
//////                
//////            Detection_Pion_Init();
//////            Detection_Pion_On();
//////            
////            
////            
////
////            //nb_s_fonctionnement_souhaiter = (unsigned char) (option);
////            //  if (option & OPTION_TEMPS) {//On demande un mouvement basé sur le temps
////            do {
////                EUSART1_Check_Buffer();
////        SPI_Check_Buffer();
////                
////                
////             //   if(nb_s_fonctionnement)
//////            Detection_Pion_Init();
//////            Detection_Pion_On();
////            
////                
////                
////                //LED^=1;
////                // } while (nb_s_fonctionnement < (option >> 4)); //les quatres bit de poid fort de l'option détermine le temps a fonctionner en dure
////            } while(
////            ((Etat == ETAT_AVANCE) | (Etat == ETAT_RECULE))
////            &&
////             (nb_s_fonctionnement < nb_s_fonctionnement_souhaiter)
////                    )
////                    ; 
////            
////                 
////            }
////            else{
//                
//                      //nb_s_fonctionnement_souhaiter = (unsigned char) (option);
//            //  if (option & OPTION_TEMPS) {//On demande un mouvement basé sur le temps
//            do {
//                EUSART1_Check_Buffer();
//        SPI_Check_Buffer();
//                //LED^=1;
//                // } while (nb_s_fonctionnement < (option >> 4)); //les quatres bit de poid fort de l'option détermine le temps a fonctionner en dure
//            } while(nb_s_fonctionnement < nb_s_fonctionnement_souhaiter); 
////            }
//
//           
//                    
//            Stop_Moteur_1();
//            Capteur_Capot_Off();
//
//
//            if ((Etat == ETAT_AVANCE) | (Etat == ETAT_RECULE)) {
//
//            Etat_Update(ETAT_INACTIF);
//            P4_busy = P4_BUSY_LIBRE;
//            
//            }
//            
//            
//            
//            
//#ifndef DEBUG
//            //    delay_1s();
//            //    delay_1s();
//            //    delay_1s();
//#endif
//
//            break;

            //} else {//On demande d'avancer jusqu'à la prochaine platine
//        case TYPE_MOUVEMENT_PION:
//            nb_Pion_Objectif = option;
//            nb_Pion = 0;
//
//            //            if(PION == METAL_PRESENT){
//            //            Mouvement_Startup = 1;
//            //            }else{
//            //            Mouvement_Startup = 0; 
//            //            }
//
//            Detection_Pion_Init();
//            Detection_Pion_On();



#ifdef DEBUG  
            //            TRISCbits.TRISC4 = 1;// I MOT 1
            //            TRISCbits.TRISC5 = 1;// I MOT 1
#endif






            //LED=0;
            do {
                //LED=TRISCbits.TRISC4 ;
                //LED^=1;
                //LED=PORTCbits.RC4;
                //LED=PORTCbits.RC5;
                // LED=RC4;
                //LED=RC5;
                //LED^=1;
                Check_List_Moteur_Metalhome();
            } while (
                    ((direction == AVANT) && (Etat == ETAT_AVANCE) )
                    |
                    ((direction == ARRIERE) && (Etat == ETAT_RECULE))

                    );

//Etat_Update(ETAT_INACTIF);
//            Detection_Pion_Off();

#ifdef PROTO_2
            //            if (Mouvement_Startup == 1) {
            //                Alarme_On(ALARME_START);
            //            }
#endif      

            Stop_Moteur_1();
//            Capteur_Capot_Off();

//            break;
//
//
//        default: break;
//
//
//    }





    //            Stop_Moteur_1();
    //            Capteur_Capot_Off();



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



    PIE3bits.PTIE = 0;
    PIE1bits.ADIE = 0;

    Surveillance_Consommation_Moteur_1_Desactiver(); //On activera la détection surconsommation par moteur à chaque utilisation
    //INTCON3bits.INT1IE = 0; //On activera la détection surconsommation par moteur à chaque utilisation 
    Coupe_Moteur();
    //delay_s(1);//A utiliser de préférence (scrute le tampon RS232)
    //delay_1s();//A éviter
#ifndef DEBUG
    //    delay_1s();
    //    delay_1s();
#endif


}


