//******************************************************************************
//	PROGRAMME RSMM CHAINE CORDE CABLE
//  DATE LE 27/03/2017
//	FAIT PAR BERGER OLIVIER 
//******************************************************************************
#include <stdbool.h>
#include <xc.h>
//#include <time.h>
#include <string.h> 
#include <stdio.h> 
#include <stdlib.h>
#include "MOTEUR.h"
#include "Variables.h"

#include "adc.h"
#include "init.h"
#include "interrupt.h"
#include "pwm.h"
#include "init.h"
#include "action.h"
#include "timer.h"
#include "eusart.h"
#include "horloge.h"


//
////#define INDICE_SIGMOIDE 15
//#define INDICE_SIGMOIDE 15

// #pragma config statements should precede project file includes.
// Use project enums instead of #define for ON and OFF.

//****************************************************************************** 
//	FONCTION INITIALISATION IT
//******************************************************************************

#include "variable_main.h"

void Init_Variable(void) {

    Version = 1;


    unsigned char i;

    for (i = 0; i < NB_ACTION_LOG; i++) {
        Etat_Log[i] = ETAT_BOOT; // Normal

        //  Etat_Log[i] = i; // DEBUG
    }

    Etat_Precedent_Index = 0;
    Etat = ETAT_BOOT;
    //Etat_Update(ETAT_BOOT);

    Alarme = ALARME_NULLE;


    nb_s_fonctionnement = 0;


    nb_s_patinage = 90;
    // nb_s_patinage = 10;

    nb_100ms_Timer_5 = 0;

    nb_100ms_pion = 1;
    nb_100ms_platine = 10;

    nb_s_pelle = 30;
    nb_s_bequille = 30;

    Detecteur_Pion = 0;
    nb_Pion = 0;

delay_s_counter =  0;

    moteur_indice = MOTEUR_1;
    consigne = 0;
    direction = 0;

    Patinage_Nb_Essai_Autoriser = 3;
    Capteur_Capot_Nb_Evenement_Autoriser = 3;
    Capteur_Capot_Compteur_Temps_S = 0;
    Patinage_Nb_Essai = 0;
    Capteur_Capot_Nb_Evenement = 0;
    
    TIMER0_Etat = OFF;
}



//******************************************************************************
// FONCTION CYCLE MOTEUR
//******************************************************************************

void Cycle(void) {
    //unsigned int duty;
    //   unsigned char Consigne_en_A;


    Consigne_en_A = 2;
    //    Consigne_en_A = 4;
    Consigne_en_A = 8;
    Consigne_en_A = 16;
    Consigne_en_A = 4;
    //Consigne_en_A = 25;

    //    consigne = 8;
    //    consigne = 10;
    //    consigne = 20;
    //    consigne = 40;
    //consigne = 80;
    consigne = Consigne_en_A * 5;

    while (1) {
        EUSART1_Check_Buffer();



        switch (Etat) {
            case ETAT_ALARME:
                /*vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv*/
                switch (Alarme) {
                    case ALARME_PATINAGE:


                        switch (Etat_Get(1)) {//Suivant l'état précédent
                            case ETAT_AVANCE:
                                Moteur(MOTEUR_1, MARCHE_ARRIERE, consigne, OPTION_TEMPS | OPTION_MARCHE_FORCER | OPTION_TEMPS_3_s);
                                    Patinage_Nb_Essai -= 1;
                                if (Patinage_Nb_Essai > 0) {
                                    nb_s_fonctionnement = 0;
//                                        delay_1s();
//                                        delay_1s();
//                                        delay_1s();
//                                        delay_1s();
                                        delay_s(TEMPS_ATTENTE_APRES_ALARME);
                                    Etat_Update(ETAT_AVANCE);
                                } else {
                                    Etat_Update(ETAT_AVANCE);
                                    Etat_Update(ETAT_BLOQUER);
                                }
                                break;
                            case ETAT_RECULE:
                                Moteur(MOTEUR_1, MARCHE_AVANT, consigne, OPTION_TEMPS | OPTION_MARCHE_FORCER | OPTION_TEMPS_3_s);
                                    Patinage_Nb_Essai -= 1;
                                if (Patinage_Nb_Essai > 0) {
                                    nb_s_fonctionnement = 0;
                                        delay_s(TEMPS_ATTENTE_APRES_ALARME);
                                    Etat_Update(ETAT_RECULE);
                                } else {
                                    Etat_Update(ETAT_RECULE);
                                    Etat_Update(ETAT_BLOQUER);
                                }
                                break;
                            default: break;
                        }




                        break;
                    case ALARME_CAPOT:
                        /*^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^*/

                        switch (Etat_Get(1)) {//Suivant l'état précédent
                            case ETAT_AVANCE:
                                Moteur(MOTEUR_1, MARCHE_ARRIERE, consigne, OPTION_TEMPS | OPTION_MARCHE_FORCER | OPTION_TEMPS_3_s);
                                    Capteur_Capot_Nb_Evenement -= 1;
                                if (Capteur_Capot_Nb_Evenement > 0) {
                                    Capteur_Capot_Compteur_Temps_S = 0;
                                        delay_s(TEMPS_ATTENTE_APRES_ALARME);
                                    Etat_Update(ETAT_AVANCE);
                                } else {
                                    Etat_Update(ETAT_AVANCE);
                                    Etat_Update(ETAT_INACTIF);
                                }
                                break;
                            case ETAT_RECULE:
                                Moteur(MOTEUR_1, MARCHE_AVANT, consigne, OPTION_TEMPS | OPTION_MARCHE_FORCER | OPTION_TEMPS_3_s);
                                    Capteur_Capot_Nb_Evenement -= 1;
                                if (Capteur_Capot_Nb_Evenement > 0) {
                                    Capteur_Capot_Compteur_Temps_S = 0;
                                        delay_s(TEMPS_ATTENTE_APRES_ALARME);
                                    Etat_Update(ETAT_RECULE);
                                } else {
                                    Etat_Update(ETAT_RECULE);
                                    Etat_Update(ETAT_INACTIF);
                                }
                                break;
                            default: break;
                        }





                        /*vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv*/
                        break; // case ALARME_PATINAGE

                    default: break;
                }// switch (Alarme)

                /*^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^*/

                break; // case ETAT_ALARME








            case ETAT_AVANCE:
                //Moteur(MOTEUR_1, AVANT, consigne, OPTION_TEMPS + OPTION_MARCHE_FORCER + OPTION_TEMPS_3_s);

                Moteur(MOTEUR_1, AVANT, consigne, OPTION_NULLE);
                break;
            case ETAT_RECULE:
                Moteur(MOTEUR_1, ARRIERE, consigne, OPTION_NULLE);
                break;
                
            case ETAT_PELLE_LEVE:
                Moteur(MOTEUR_PELLE, MONTE, consigne, OPTION_NULLE);//Moteur(MOTEUR_2, MONTE, consigne, OPTION_NULLE);
                break;
            case ETAT_PELLE_BAISSE:
                Moteur(MOTEUR_PELLE, DESCEND, consigne, OPTION_NULLE);
                break;

            case ETAT_SORT_BEQUILLE:
                Moteur(MOTEUR_BEQUILLE, SORT, consigne, OPTION_NULLE);
                break;
            case ETAT_RENTRE_BEQUILLE:
                Moteur(MOTEUR_BEQUILLE, RENTRE, consigne, OPTION_NULLE);
                break;


            default:
                //LED ^= 1;
                break;


        }

    }

}




//******************************************************************************
// FONCTION MAIN  OK
//******************************************************************************
//#define EUSART1_RX_BUFFER_SIZE 64
//extern static unsigned char eusart1RxBuffer[EUSART1_RX_BUFFER_SIZE]; //Buffer d'émission

void main(void) {
    OSCCON = 0b01100000; // 4 MHZ 
    OSCCON = 0b01110000; // 8 MHz
    //OSCCON = 0b01100000;// 4 MHz
    while (IOFS != 1);

    Init_Variable();



    Init_Port();

    Init_IT();

    EUSART1_Initialize();


    Init_ADC();

    Init_TIMER0();
    Init_TIMER2();
    Init_TIMER5();
    //TIMER0_On();
    //LED = 1;
    Init_PWM();
    // Init_IT();


    //Init_TIMER0();
    //    TIMER0_On();

    while(1){
        LED^=1;
        delay_s(1);
    }
    Cycle();

}
//******************************************************************************



