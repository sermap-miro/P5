//******************************************************************************
//	PROGRAMME RSMM CHAINE CORDE CABLE
//  DATE LE 27/03/2017
//	FAIT PAR BERGER OLIVIER 
//******************************************************************************


    
#pragma warning disable 752

// CONFIG1H
#pragma config OSC = IRCIO      // Oscillator Selection bits (Internal oscillator block, port function on RA6 and port function on RA7)
#pragma config FCMEN = ON       // Fail-Safe Clock Monitor Enable bit (Fail-Safe Clock Monitor enabled)
#pragma config IESO = ON        // Internal External Oscillator Switchover bit (Internal External Switchover mode enabled)

// CONFIG2L
#pragma config PWRTEN = ON      // Power-up Timer Enable bit (PWRT enabled)
#pragma config BOREN = OFF       // Brown-out Reset Enable bits (Brown-out Reset enabled)
#pragma config BORV = 27        // Brown Out Reset Voltage bits (VBOR set to 2.7V)

// CONFIG2H
#pragma config WDTEN = OFF      // Watchdog Timer Enable bit (WDT disabled (control is placed on the SWDTEN bit))
#pragma config WDPS = 32768     // Watchdog Timer Postscale Select bits (1:32768)
#pragma config WINEN = OFF      // Watchdog Timer Window Enable bit (WDT window disabled)

// CONFIG3L
#pragma config PWMPIN = OFF     // PWM output pins Reset state control (PWM outputs disabled upon Reset (default))
#pragma config LPOL = HIGH      // Low-Side Transistors Polarity (PWM0, 2, 4 and 6 are active-high)
#pragma config HPOL = HIGH      // High-Side Transistors Polarity (PWM1, 3, 5 and 7 are active-high)
#pragma config T1OSCMX = OFF    // Timer1 Oscillator MUX (Standard (legacy) Timer1 oscillator operation)

// CONFIG3H
#pragma config FLTAMX = RC1     // FLTA MUX bit (FLTA input is multiplexed with RC1)
#pragma config SSPMX = RC7      // SSP I/O MUX bit (SCK/SCL clocks and SDA/SDI data are multiplexed with RC5 and RC4, respectively. SDO output is multiplexed with RC7.)
#pragma config PWM4MX = RB5     // PWM4 MUX bit (PWM4 output is multiplexed with RB5)
#pragma config EXCLKMX = RC3    // TMR0/T5CKI External clock MUX bit (TMR0/T5CKI external clock input is multiplexed with RC3)
#pragma config MCLRE = OFF      // MCLR Pin Enable bit (Disabled)

// CONFIG4L
#pragma config STVREN = ON      // Stack Full/Underflow Reset Enable bit (Stack full/underflow will cause Reset)
#pragma config LVP = OFF        // Low-Voltage ICSP Enable bit (Low-voltage ICSP disabled)

// CONFIG5L
#pragma config CP0 = OFF        // Code Protection bit (Block 0 (000200-000FFFh) not code-protected)
#pragma config CP1 = OFF        // Code Protection bit (Block 1 (001000-001FFF) not code-protected)
#pragma config CP2 = OFF        // Code Protection bit (Block 2 (002000-002FFFh) not code-protected)
#pragma config CP3 = OFF        // Code Protection bit (Block 3 (003000-003FFFh) not code-protected)

// CONFIG5H
#pragma config CPB = OFF        // Boot Block Code Protection bit (Boot Block (000000-0001FFh) not code-protected)
#pragma config CPD = OFF        // Data EEPROM Code Protection bit (Data EEPROM not code-protected)

// CONFIG6L
#pragma config WRT0 = OFF       // Write Protection bit (Block 0 (000200-000FFFh) not write-protected)
#pragma config WRT1 = OFF       // Write Protection bit (Block 1 (001000-001FFF) not write-protected)
#pragma config WRT2 = OFF       // Write Protection bit (Block 2 (002000-002FFFh) not write-protected)
#pragma config WRT3 = OFF       // Write Protection bit (Block 3 (003000-003FFFh) not write-protected)

// CONFIG6H
#pragma config WRTC = OFF       // Configuration Register Write Protection bit (Configuration registers (300000-3000FFh) not write-protected)
#pragma config WRTB = OFF       // Boot Block Write Protection bit (Boot Block (000000-0001FFh) not write-protected)
#pragma config WRTD = OFF       // Data EEPROM Write Protection bit (Data EEPROM not write-protected)

// CONFIG7L
#pragma config EBTR0 = OFF      // Table Read Protection bit (Block 0 (000200-000FFFh) not protected from table reads executed in other blocks)
#pragma config EBTR1 = OFF      // Table Read Protection bit (Block 1 (001000-001FFF) not protected from table reads executed in other blocks)
#pragma config EBTR2 = OFF      // Table Read Protection bit (Block 2 (002000-002FFFh) not protected from table reads executed in other blocks)
#pragma config EBTR3 = OFF      // Table Read Protection bit (Block 3 (003000-003FFFh) not protected from table reads executed in other blocks)

// CONFIG7H
#pragma config EBTRB = OFF      // Boot Block Table Read Protection bit (Boot Block (000000-0001FFh) not protected from table reads executed in other blocks)




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

    nb_100ms_pion = NB_100MS_PION;//1
    nb_100ms_platine = NB_100MS_PLATINE;//10

    nb_s_pelle = 30;
    nb_s_bequille = 30;

    Detecteur_Pion = 0;
    nb_Pion = 0;
    nb_Pion_Objectif = 0;
    Mouvement_Startup = 0;

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
    
consigne_moteur_1=20;//4 ampères (4 * 5)
consigne_moteur_2=50;//10 ampères (10 * 5)
consigne_moteur_3=50;//10 ampères (10 * 5)



/* Pailleux */
Pailleux_Valeur = 0;

Pailleux_Compteur = 0;

Pailleux_Nb_S = 30;

/* DVT */
DVT_Temps_Pause = 0;

DVT_Compteur = 0;

DVT_Tableau_Pause[0]=9;
DVT_Tableau_Pause[1]=7;
DVT_Tableau_Pause[2]=6;
DVT_Tableau_Pause[3]=5;
DVT_Tableau_Pause[4]=4;
DVT_Tableau_Pause[5]=3;


/* Multitas */

Multitas_Temps = 0;

Multitas_Compteur = 0;

Multitas_Courant_Max = 20 /* Ampères */ * 5 /* coefficient de conversion Ampères -> uchar */;

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
    consigne = (char) (Consigne_en_A * 5);

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
  //TIMER0_On();
//    while(1){
//        //TIMER0_On();
//        LED^=1;
//        EUSART1_Check_Buffer();
//       // delay_s(1);
//        //NOP();
//    }
    Cycle();

}
//******************************************************************************



