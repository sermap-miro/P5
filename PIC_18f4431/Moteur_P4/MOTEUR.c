//ajout


//******************************************************************************
//	PROGRAMME RSMM CHAINE CORDE CABLE
//  DATE LE 27/03/2017
//	FAIT PAR BERGER OLIVIER 
//******************************************************************************
/*
 
 MCLRE = ON <= permet de programmer sans soucis les cartes
 
 
 
 */

#define 	BV(bit)   (1<<(bit))
#define 	cbi(reg, bit)   reg &= ~(BV(bit))
#define 	sbi(reg, bit)   reg |= (BV(bit))

#pragma warning disable 752
/*
 
 Register 1H to select one of these
1. LP: Low-Power Crystal
2. XT: Crystal/Resonator
3. HS: High-Speed Crystal/Resonator
4. HSPLL: High-Speed Crystal/Resonator with PLL Enabled
5. RC: External Resistor/Capacitor with F OSC /4 Output on RA6
6. RCIO: External Resistor/Capacitor with I/O on RA6
7. INTIO1: Internal Oscillator with F OSC /4 Output on RA6 and I/O on RA7
8. INTIO2: Internal Oscillator with I/O on RA6 and RA7
9. EC: External Clock with F OSC /4 Output
10. ECIO: External Clock with I/O on RA6
 
 */
// CONFIG1H
#pragma config OSC = IRCIO      // Oscillator Selection bits (Internal oscillator block, port function on RA6 and port function on RA7)
//#pragma config OSC = XT      // Semble fonctionner
//#pragma config OSC = LP      // Semble fonctionner
//#pragma config OSC = INTIO2      // Oscillator Selection bits (Internal oscillator block, port function on RA6 and port function on RA7)
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
//#pragma config SSPMX = RC7      // SSP I/O MUX bit (SCK/SCL clocks and SDA/SDI data are multiplexed with RC5 and RC4, respectively. SDO output is multiplexed with RC7.)
#pragma config SSPMX = RD1      // SSP I/O MUX bit (SCK/SCL clocks and SDA/SDI data are multiplexed with RD3 and RD2, respectively. SDO output is multiplexed with RD1.)

#pragma config PWM4MX = RB5     // PWM4 MUX bit (PWM4 output is multiplexed with RB5)
#pragma config EXCLKMX = RC3    // TMR0/T5CKI External clock MUX bit (TMR0/T5CKI external clock input is multiplexed with RC3)
//#pragma config MCLRE = OFF      // MCLR Pin Enable bit (Disabled)
#pragma config MCLRE = ON      // MCLR Pin Enable bit (Disabled) // 

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
//#include "init.h"
#include "action.h"
#include "timer.h"
#include "eusart.h"
#include "spi.h"
#include "horloge.h"
#include "pion.h"
#include "alarme.h"


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
    
    /*
     
     Version 11:
     * Etat de Fumière pleine lors d'un patinage sur la platine de multitas
     
     */
    
    /*
     Version 10:
     * Ajout d'un temps de dead time (le dead time hard ne semble pas suffisant => Quentin à cramer un MOS)
     * Apparement une fonction soft de dead time existait auparavant pour le moteur de déplacement
     * Ajout de la meme fonction pour le moteur de la pelle et la fonction béquille
     * 
     * 
     Version 9:
     * Ajout de nouveau intitulé d'alarme: 
     * 
#define ALARME_OVERLOAD_CAP_1_1 9
#define ALARME_OVERLOAD_CAP_1_3 10
     * 
    
     * 
     * 
     * 
     * 
     * 
     * 
    */
      
      /*
     Version 8: Mis en fonction de l'affichage des numéros de version
 
 
 
     */
    Version = 11;
    //Version = 10;

    //Compteur_Fonctionnement=0;
    Batterie_mV = 0;


    unsigned char i;

    for (i = 0; i < NB_ACTION_LOG; i++) {
        Etat_Log[i] = ETAT_BOOT; // Normal

        //  Etat_Log[i] = i; // DEBUG
    }

    Etat_Precedent_Index = 0;
    Etat = ETAT_BOOT;
    //Etat_Update(ETAT_BOOT);

    Alarme = ALARME_NULLE;

    nb_s_fonctionnement_souhaiter = 0;
    nb_s_fonctionnement = 0;


    nb_s_patinage = 90;
    nb_s_patinage = 45;//Modification 17 Avril 
    nb_s_patinage = 50;//Modification 17 Avril 
    // nb_s_patinage = 10;

    nb_100ms_Timer_5 = 0;

    nb_100ms_pion = NB_100MS_PION; //1
    nb_100ms_platine = NB_100MS_PLATINE; //10

    nb_s_pelle = NB_S_PELLE;
    nb_s_bequille = NB_S_BEQUILLE;

    Detecteur_Pion = SURVEILLANCE_DESACTIVER;
    nb_Pion = 0;
    nb_Pion_Objectif = 0;
    Mouvement_Startup = 0;

    delay_s_counter = 0;

    moteur_indice = MOTEUR_1;
    consigne = 0;
    direction = 0;
    mouvement_option = 0;
    Option_Multitas = 0;
    type_consigne = TYPE_MOUVEMENT_PION;
    Consigne_Max = CONSIGNE_MAX; //20 * 5;//20 ampères
    Consigne_Max_Moteur_X = CONSIGNE_MAX_X;
    Consigne_Max_Moteur_Z = CONSIGNE_MAX_Z;
    Consigne_Max_Moteur_Bequille = CONSIGNE_MAX_BEQUILLE;

    Moteur_I_Max = MOTEUR_I_MAX;
    Pelle_I_Max = PELLE_I_MAX;
    Bequille_I_Max = BEQUILLE_I_MAX;


    Consigne_en_A = 4;
    consigne = (char) (Consigne_en_A * 5);


    Patinage_Nb_Essai_Autoriser = 3;
    Capteur_Capot_Nb_Evenement_Autoriser = 3;
    Capteur_Capot_Compteur_Temps_S = 0;
    Patinage_Nb_Essai = 0;
    Capteur_Capot_Nb_Evenement = 0;

    TIMER0_Etat = OFF;

    consigne_moteur_1 = 20; //4 ampères (4 * 5)
    consigne_moteur_2 = 50; //10 ampères (10 * 5)
    consigne_moteur_3 = 50; //10 ampères (10 * 5)

    Surveillance_Consommation_Moteur_1 = SURVEILLANCE_DESACTIVER;
    Surveillance_Consommation_Moteur_2 = SURVEILLANCE_DESACTIVER;

    Detection_Pion_Init();
    //if (PION == METAL_PRESENT){
    //    Surveillance_Capteur_Pion = METAL_PRESENT;
    //}else{
    //    Surveillance_Capteur_Pion = METAL_ABSENT;
    //    
    //}

    Compteur_IRQ_I_Moteur_1 = 0;
    Compteur_IRQ_I_Moteur_2 = 0;


    P4_busy = P4_BUSY_LIBRE;



    /* Pailleux */
    Pailleux_Valeur = 0;

    Pailleux_Compteur = 0;

    Pailleux_Nb_S = 30;

    /* DVT */
    DVT_Temps_Pause = 0;

    DVT_Compteur = 0;

    DVT_Tableau_Pause[0] = 9;
    DVT_Tableau_Pause[1] = 7;
    DVT_Tableau_Pause[2] = 6;
    DVT_Tableau_Pause[3] = 5;
    DVT_Tableau_Pause[4] = 4;
    DVT_Tableau_Pause[5] = 3;


    /* Multitas */

    Multitas_Temps = 0;

    Multitas_Compteur = 0;

    Multitas_Courant_Max = 20 /* Ampères */ * 5 /* coefficient de conversion Ampères -> uchar */;

    /*  UART TEST  */
    UART_TEST = 0;
    RX1_ABR = 0;
    RX1_full = 0;
    SPI_full = 0;
    
    spiRxIndex = 0;
    spiTxIndex = 0;
    SPI_MODE = SPI_MODE_LECTURE;
}



//******************************************************************************
// FONCTION CYCLE MOTEUR
//******************************************************************************

void Cycle(void) {
    //unsigned int duty;
    //   unsigned char Consigne_en_A;
    unsigned char i, j; //local variable (for loop)
//
//    Consigne_en_A = 2;
//    //    Consigne_en_A = 4;
//    Consigne_en_A = 8;
//    Consigne_en_A = 16;
//    Consigne_en_A = 4;
//    //Consigne_en_A = 25;

    //    consigne = 8;
    //    consigne = 10;
    //    consigne = 20;
    //    consigne = 40;
    //consigne = 80;
    //consigne = (char) (Consigne_en_A * 5);
//
//    while(1){
//        BUZZER = 1;
//        delay_1s();
//        delay_1s();
//        delay_1s();
//        BUZZER = 0;
//        delay_1s();
//        delay_1s();
//        delay_1s();
//        
//    }
//    
    
    
    while (1) {
        EUSART1_Check_Buffer();
        //   LED = 0;
        SPI_Check_Buffer();

        
       if (BTN_ARRET_URGENCE==0){ //Les entrées sont inversées
        
        
        
        
        switch (Etat) {
            case ETAT_ALARME:
                /*vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv*/
                switch (Alarme) {
                    case ALARME_PATINAGE:
                        switch (Etat_Get(1)) {//Suivant l'état précédent
                            case ETAT_AVANCE:
                                delay_s(TEMPS_ATTENTE_ALARME);
                                //Moteur(MOTEUR_1, MARCHE_ARRIERE, consigne, OPTION_TEMPS | OPTION_MARCHE_FORCER | OPTION_TEMPS_3_s);


                                if (Option_Multitas == 0) {


                                    Mouvement_X(MARCHE_ARRIERE, TYPE_MOUVEMENT_TEMPS, OPTION_MARCHE_FORCER | OPTION_TEMPS_ALARME_PATINAGE); // Modif du 17 Avril



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
                                        //Etat_Update(ETAT_ALARME);
                                        P4_busy = P4_BUSY_LIBRE;
                                        Etat_Update(ETAT_BLOQUER);
                                    }

                                } else {

                                    Etat_Update(ETAT_INACTIF);
                                    //Etat_Update(ETAT_ALARME);
                                    P4_busy = P4_BUSY_LIBRE;

                                }



                                break;
                            case ETAT_RECULE:
                                delay_s(TEMPS_ATTENTE_ALARME);
                                //Moteur(MOTEUR_1, MARCHE_AVANT, consigne, OPTION_TEMPS | OPTION_MARCHE_FORCER | OPTION_TEMPS_3_s);

                                Mouvement_X(MARCHE_AVANT, TYPE_MOUVEMENT_TEMPS, OPTION_MARCHE_FORCER | OPTION_TEMPS_ALARME_PATINAGE); // Modif du 17 Avril
                                Patinage_Nb_Essai -= 1;
                                if (Patinage_Nb_Essai > 0) {
                                    nb_s_fonctionnement = 0;
                                    delay_s(TEMPS_ATTENTE_APRES_ALARME);
                                    Etat_Update(ETAT_RECULE);
                                } else {
                                    Etat_Update(ETAT_RECULE);
                                    //Etat_Update(ETAT_ALARME);
                                    P4_busy = P4_BUSY_LIBRE;
                                    Etat_Update(ETAT_BLOQUER);
                                }
                                break;
                            default:
                                P4_busy = P4_BUSY_LIBRE;
                                Etat_Update(ETAT_BLOQUER_IMPOSSIBLE); //Pas normal (ne devrait jamais se produire)... mais au cas ou
                                break;
                        }




                        break;
                    case ALARME_CAPOT:
                        /*^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^*/

/*
 
 GESTION DU CAPTEUR CAPOT:
 * - Nouveau bug relevé par Elie: Lors d'une manoeuvre de capteur capot à proximité d'une platine,
        le mirobot détecte de nouveau la platine, arrête son action, et passe à la suivante
        
 
 */

                        switch (Etat_Get(1)) {//Suivant l'état précédent
                            case ETAT_AVANCE:
                                delay_s(TEMPS_ATTENTE_ALARME);
                                //      Moteur(MOTEUR_1, MARCHE_ARRIERE, consigne, OPTION_TEMPS | OPTION_MARCHE_FORCER | OPTION_TEMPS_3_s);

                                Mouvement_X(MARCHE_ARRIERE, TYPE_MOUVEMENT_TEMPS, OPTION_MARCHE_FORCER | OPTION_TEMPS_ALARME_CAPOT); // Modif du 17 Avril
                                Capteur_Capot_Nb_Evenement -= 1;
                                if (Capteur_Capot_Nb_Evenement > 0) {
                                    Capteur_Capot_Compteur_Temps_S = 0;
                                    delay_s(TEMPS_ATTENTE_APRES_ALARME);
                                    Etat_Update(ETAT_AVANCE);
                                } else {
                                    Etat_Update(ETAT_AVANCE);
                                    //Etat_Update(ETAT_ALARME);
                                    //Etat_Update(ETAT_INACTIF); 
                                    P4_busy = P4_BUSY_LIBRE;
                                    Etat_Update(ETAT_BLOQUER);
                                    //Etat_Update(ETAT_INACTIF);
                                }
                                break;
                            case ETAT_RECULE:
                                delay_s(TEMPS_ATTENTE_ALARME);
                                //Moteur(MOTEUR_1, MARCHE_AVANT, consigne, OPTION_TEMPS | OPTION_MARCHE_FORCER | OPTION_TEMPS_3_s);
                                //Mouvement_X(MARCHE_AVANT, TYPE_MOUVEMENT_TEMPS, OPTION_MARCHE_FORCER | OPTION_TEMPS_3_s);
                                Mouvement_X(MARCHE_AVANT, TYPE_MOUVEMENT_TEMPS, OPTION_MARCHE_FORCER | OPTION_TEMPS_ALARME_CAPOT); // Modif du 17 Avril
                                Capteur_Capot_Nb_Evenement -= 1;
                                if (Capteur_Capot_Nb_Evenement > 0) {
                                    Capteur_Capot_Compteur_Temps_S = 0;
                                    delay_s(TEMPS_ATTENTE_APRES_ALARME);
                                    Etat_Update(ETAT_RECULE);
                                } else {
                                    Etat_Update(ETAT_RECULE);
                                    //Etat_Update(ETAT_ALARME);
                                    P4_busy = P4_BUSY_LIBRE;
                                    //Etat_Update(ETAT_BLOQUER);

                                    Etat_Update(ETAT_BLOQUER_DEFINITIVEMENT); //On bloque definitivement lorsque l'on recule
                                    //Etat_Update(ETAT_INACTIF);
                                }
                                break;
                            default://Empeche les faux démarrage (avec capot ouvert)
                                P4_busy = P4_BUSY_LIBRE;
                                Etat_Update(ETAT_BLOQUER_IMPOSSIBLE); //Semble etre  normal finalement { (Pas normal (ne devrait jamais se produire)... mais au cas ou}
                                break;
                        }





                        /*vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv*/
                        break; // case ALARME_PATINAGE




                    case ALARME_I_MOTEUR_1:
                        P4_busy = P4_BUSY_OCCUPER;
                        Etat_Update(ETAT_BLOQUER_DEFINITIVEMENT);
                        for (i = 0; i < 4; i++) {
                            Buzzer_Etat(BUZZER_ON);
                            delay_n_100ms(4);
                            Buzzer_Etat(BUZZER_OFF);
                            delay_n_100ms(2);
                        }
                        break;
                    case ALARME_I_MOTEUR_2:

                        P4_busy = P4_BUSY_OCCUPER;
                        Etat_Update(ETAT_BLOQUER_DEFINITIVEMENT);



                        for (i = 0; i < 4; i++) {
                            Buzzer_Etat(BUZZER_ON);
                            delay_n_100ms(4);
                            Buzzer_Etat(BUZZER_OFF);
                            delay_n_100ms(2);
                        }
                        break;

                    default: break;
                }// switch (Alarme)

                /*^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^*/

                break; // case ETAT_ALARME








            case ETAT_AVANCE:
                //Moteur(MOTEUR_1, AVANT, consigne, OPTION_TEMPS + OPTION_MARCHE_FORCER + OPTION_TEMPS_3_s);

                // P4_busy = P4_BUSY_OCCUPER;
                Mouvement_X(direction, type_consigne, mouvement_option);
                break;
                //                //Moteur(MOTEUR_1, AVANT, consigne, OPTION_NULLE);
                //                break;
            case ETAT_RECULE:
                //P4_busy = P4_BUSY_OCCUPER;
                Mouvement_X(direction, type_consigne, mouvement_option);
                // Moteur(MOTEUR_1, ARRIERE, consigne, OPTION_NULLE);
                break;

            case ETAT_PELLE_LEVE:
                // P4_busy = P4_BUSY_OCCUPER;
                Mouvement_Z(direction, type_consigne, mouvement_option);
                break;
                //               // Moteur(MOTEUR_PELLE, MONTE, consigne, OPTION_NULLE);//Moteur(MOTEUR_2, MONTE, consigne, OPTION_NULLE);
                //                break;
            case ETAT_PELLE_BAISSE:
                //  P4_busy = P4_BUSY_OCCUPER;
                Mouvement_Z(direction, type_consigne, mouvement_option);
                // Moteur(MOTEUR_PELLE, DESCEND, consigne, OPTION_NULLE);
                break;

            case ETAT_SORT_BEQUILLE:
                //  P4_busy = P4_BUSY_OCCUPER;
                //LED = 1;
                Mouvement_Bequille(direction, type_consigne, mouvement_option);
                //LED = 0;
                break;
                // //               Moteur(MOTEUR_BEQUILLE, SORT, consigne, OPTION_NULLE);
                //                break;
            case ETAT_RENTRE_BEQUILLE:
                //  P4_busy = P4_BUSY_OCCUPER;
                //LED = 1;
                Mouvement_Bequille(direction, type_consigne, mouvement_option);
                //LED = 0;
                //Moteur(MOTEUR_BEQUILLE, RENTRE, consigne, OPTION_NULLE);
                break;


            default:
                //LED ^= 1;
                break;


        }
        
        
       }else{//Le bouton d'arret d'urgence est en position URGENCE
           
            Coupe_Moteur();
            Alarme_On(ALARME_AU);
            //Etat_Update(ETAT_BLOQUER_DEFINITIVEMENT); //On bloque definitivement lorsque l'on recule
        }

    }

}




//******************************************************************************
// FONCTION MAIN  OK
//******************************************************************************
//#define EUSART1_RX_BUFFER_SIZE 64
//extern static unsigned char eusart1RxBuffer[EUSART1_RX_BUFFER_SIZE]; //Buffer d'émission

void main(void) {
    //OSCCON = 0b01100000; // 4 MHZ 
    OSCCON = 0b01110000; // 8 MHz
//    
//    TRISCbits.TRISC2 = 0;// LED
//    LED = 1;
    //OSCCON = 0b01100000;// 4 MHz
    while (IOFS != 1);
//    LED = 0;
    
    
    
    
    Init_Variable();



    Init_Port();

//    while(1){LED^=1;}
    //LED=1;
    //    while(1){
    //        //TIMER0_On();
    //        LED=1;
    //        RELAIS=1;
    //    }
    
//    
//#asm
//    mloop:
//#endasm
////    LED^=1;
//        LED = 1;
//    LED = 0;
//    //LED ^= 1;
////    LED = 1;
////    LED = 0;
//#asm
//    GOTO mloop
//#endasm
    
    
    
//        while(1){//ABDEN
//    //LED ^= 1;
//    LED = 1;
//    LED = 0;
//    //LED ^= 1;
//    LED = 1;
//    LED = 0;
//    }
    
    Init_IT();
              
//    
//        while(1){
//        
//        
//        BUZZER=1;
//        delay_1s();
//        
//        BUZZER=0;
//        delay_1s();
//        delay_1s();
//        delay_1s();
//        delay_1s();
//    }
//    
//    
    
    
    EUSART1_Initialize();
    Init_SPI();

    //Init_IT();
              
    Init_ADC();

    Init_TIMER0();
    Init_TIMER2();
    Init_TIMER5();
    //TIMER0_On();
    //LED = 1;
    Init_PWM();
    // Init_IT();


    //    while(1) LED^=1;
    //Init_TIMER0();
    //    TIMER0_On();
    //TIMER0_On();
    //    while(1){
    //        //TIMER0_On();
    //        LED=1;
    //        EUSART1_Check_Buffer();
    //       // delay_s(1);
    //        //NOP();
    //    }

//    while(1){
//RELAIS ^= 1;
//delay_s(1);
//    }

    //PIR3bits.IC2QEIF = 0;
    //PIE3bits.IC2QEIE = 1;
    //PIR3bits.IC2QEIF = 0;

    //
    //Init_Input_Capture_0();
    //PIR3bits.IC1IF = 0;
    //PIE3bits.IC1IE = 1; 
    //PIR3bits.IC1IF = 0;
    //    TRISEbits.TRISE2 = 0;// RELAIS
    //    while(1) {
    //        LED=0;
    //        delay_s(1);
    //        RELAIS^=1;
    //        //LED=PION;
    //       // LED=PION;
    //    }
    //RESET;
//    delay_1s();
//    delay_1s();
//                
//                asm("reset");
//    while(1){LED^=1;}

//    unsigned char i;
//    i=0;
//    while(1){
//        i=(unsigned char) (i+1);
//    sprintf(UART_TX_TEXT, "%u", i);
//     sprintf(UART_TX_TEXT, "%02X %02X %02X %02X %02X %02X %02X %02X %02X %02X %02X %01X %01X %01X %02X", Etat_Get(0), Etat_Get(1), Alarme, nb_Pion, Image_Courant_Moteur_1, Image_Courant_Moteur_2, consigne, nb_s_patinage, nb_100ms_pion, nb_100ms_platine, nb_s_pelle, PION, CAPOT, RELAIS, Version);
//           
//            //sprintf(UART_TX_TEXT, "%02X%02X%02X", Reponse, Etat_Get(1), Alarme);
//            EUSART1_Buffer_Send(UART_TX_TEXT);
//    //delay_1s();
//    __delay_ms(10);
//    
//    
//    }
//    

    
    Cycle();

}
//******************************************************************************



