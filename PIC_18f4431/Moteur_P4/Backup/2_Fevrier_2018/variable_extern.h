/* 
 * File:   variable_extern.h
 * Author: sam
 *
 * Created on 16 janvier 2018, 16:06
 */

#ifndef VARIABLE_EXTERN_H
#define	VARIABLE_EXTERN_H

#ifdef	__cplusplus
extern "C" {
#endif
#include "define.h"

    extern unsigned char Version;


    extern unsigned char Etat;
    //extern unsigned char Etat_Precedent;
    extern unsigned char Etat_Log[NB_ACTION_LOG];
    extern unsigned char Alarme;
    //extern unsigned char Action;



    extern unsigned char Etat_Precedent_Index;



    // Paramètres de déplacement  


    extern unsigned char nb_s_fonctionnement; //Sauvegarde le temps entre pions
    extern unsigned char nb_s_patinage; //consigne de seconde qui défini le temps maximal avant de déclarer le mouvement en patinage


    extern unsigned char nb_100ms_Timer_5;

    extern unsigned char nb_100ms_pion; //
    extern unsigned char nb_100ms_platine;
//    extern unsigned char nb_100ms_platine_fin;


    extern unsigned char nb_s_pelle;
    extern unsigned char nb_s_bequille;



    //Detection des pions
    extern volatile bit Detecteur_Pion;


    extern unsigned char nb_Pion; // Nombre de pion vu lors du deplacement




    extern unsigned char Capteur_Capot_Nb_Evenement;
    extern unsigned char Capteur_Capot_Nb_Evenement_Autoriser;
    extern unsigned char Capteur_Capot_Compteur_Temps_S;
    extern unsigned char Patinage_Nb_Essai;
    extern unsigned char Patinage_Nb_Essai_Autoriser;




    extern volatile int duty;

    extern volatile int erreur; //volatile char erreur;



    //16 bit
    //extern volatile unsigned char Image_Courant_Moteur_1;
    //extern volatile bit Nouvelle_Valeur_ADC;
    //extern volatile int erreur;
    //extern volatile signed int erreur_accumulator;
    //extern volatile int consigne;
    //extern volatile int consigne_pwm;
    //extern volatile int consigne_pwm_max;

    //8 bit
    extern volatile unsigned char Image_Courant_Moteur_1;
    extern volatile unsigned char Image_Courant_Moteur_2;
    extern volatile bit Nouvelle_Valeur_ADC;
    //////extern volatile char erreur;

    //extern volatile unsigned char erreur_accumulator;//8bit
    //extern volatile unsigned int erreur_accumulator;//16bit
    //extern volatile unsigned short long erreur_accumulator;//24 bit
    //extern volatile unsigned short long erreur_accumulator;//32 bit

    extern volatile int erreur_accumulator; //16 bit
    //extern volatile unsigned int erreur_accumulator;//16 bit

    extern volatile unsigned int erreur_accumulator_max; //16 bit
    //extern volatile unsigned short long erreur_accumulator;//24 bit
    //extern volatile unsigned short long erreur_accumulator_max;//24 bit
    extern volatile unsigned int PID_out;

    extern volatile char moteur_indice;
    extern volatile char consigne;
    extern unsigned char Consigne_en_A;
    extern volatile char direction;
    extern volatile char consigne_pwm;
    extern volatile char consigne_pwm_max;

   extern unsigned char delay_s_counter;

      extern bit TIMER0_Etat;
    
      
      
      
      
      
      
      
      
      
    extern volatile bit RX1_full;
    //extern unsigned char COMMANDE1[64];
    //unsigned char COMMANDE1_buffer[64];


#define EUSART1_TX_BUFFER_SIZE 96
#define EUSART1_RX_BUFFER_SIZE 96

    extern unsigned char UART_TX_TEXT[EUSART1_TX_BUFFER_SIZE];
    extern unsigned char UART_RX_TEXT[EUSART1_RX_BUFFER_SIZE];

    //extern  unsigned char UART_TX_TEXT[EUSART1_TX_BUFFER_SIZE];
    //extern  unsigned char UART_RX_TEXT[EUSART1_RX_BUFFER_SIZE];
    //
    //
    //extern volatile unsigned char eusart1TxIndex; //index du buffer de transmission
    //extern  unsigned char eusart1TxBuffer[EUSART1_TX_BUFFER_SIZE]; //Buffer de transmission
    //
    //extern volatile unsigned char eusart1RxIndex; //index du buffer de réception
    //extern  unsigned char eusart1RxBuffer[EUSART1_RX_BUFFER_SIZE]; //Buffer d'émission

    //
    //extern static unsigned char UART_TX_TEXT[EUSART1_TX_BUFFER_SIZE];
    //extern static unsigned char UART_RX_TEXT[EUSART1_RX_BUFFER_SIZE];
    //
    //
    //extern volatile unsigned char eusart1TxIndex; //index du buffer de transmission
    //extern static unsigned char eusart1TxBuffer[EUSART1_TX_BUFFER_SIZE]; //Buffer de transmission
    //
    //extern volatile unsigned char eusart1RxIndex; //index du buffer de réception
    //extern static unsigned char eusart1RxBuffer[EUSART1_RX_BUFFER_SIZE]; //Buffer d'émission


    //extern volatile unsigned char UART_TX_TEXT[EUSART1_TX_BUFFER_SIZE];
    //extern volatile unsigned char UART_RX_TEXT[EUSART1_RX_BUFFER_SIZE];
    //
    //
    //extern volatile unsigned char eusart1TxIndex; //index du buffer de transmission
    //extern volatile unsigned char eusart1TxBuffer[EUSART1_TX_BUFFER_SIZE]; //Buffer de transmission
    //
    //extern volatile unsigned char eusart1RxIndex; //index du buffer de réception
    //extern volatile unsigned char eusart1RxBuffer[EUSART1_RX_BUFFER_SIZE]; //Buffer d'émission

#ifdef	__cplusplus
}
#endif

#endif	/* VARIABLE_EXTERN_H */

