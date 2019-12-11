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

      
    
    
    extern unsigned char Etat;
    extern unsigned char Etat_Precedent;
    extern unsigned char Alarme;
    //extern unsigned char Action;
    
    
extern  volatile int duty; 
    
extern volatile int erreur;//volatile char erreur;
  
    
    
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
extern volatile bit Nouvelle_Valeur_ADC;
//////extern volatile char erreur;

//extern volatile unsigned char erreur_accumulator;//8bit
//extern volatile unsigned int erreur_accumulator;//16bit
//extern volatile unsigned short long erreur_accumulator;//24 bit
//extern volatile unsigned short long erreur_accumulator;//32 bit

extern volatile int erreur_accumulator;//16 bit
//extern volatile unsigned int erreur_accumulator;//16 bit

extern volatile unsigned int erreur_accumulator_max;//16 bit
//extern volatile unsigned short long erreur_accumulator;//24 bit
//extern volatile unsigned short long erreur_accumulator_max;//24 bit
extern volatile unsigned int PID_out;

extern volatile char moteur_indice;
extern volatile char consigne;
extern volatile char direction;
extern volatile char consigne_pwm;
extern volatile char consigne_pwm_max;


extern volatile bit RX1_full;
//extern unsigned char COMMANDE1[64];
//unsigned char COMMANDE1_buffer[64];


#define EUSART1_TX_BUFFER_SIZE 64
#define EUSART1_RX_BUFFER_SIZE 64

extern unsigned char UART_TX_TEXT[EUSART1_TX_BUFFER_SIZE];
extern unsigned char UART_RX_TEXT[EUSART1_RX_BUFFER_SIZE];

//extern  unsigned char UART_TX_TEXT[EUSART1_TX_BUFFER_SIZE];
//extern  unsigned char UART_RX_TEXT[EUSART1_RX_BUFFER_SIZE];
//
//
//extern volatile unsigned char eusart1TxIndex; //index du buffer de transmission
//extern  unsigned char eusart1TxBuffer[EUSART1_TX_BUFFER_SIZE]; //Buffer de transmission
//
//extern volatile unsigned char eusart1RxIndex; //index du buffer de r�ception
//extern  unsigned char eusart1RxBuffer[EUSART1_RX_BUFFER_SIZE]; //Buffer d'�mission

//
//extern static unsigned char UART_TX_TEXT[EUSART1_TX_BUFFER_SIZE];
//extern static unsigned char UART_RX_TEXT[EUSART1_RX_BUFFER_SIZE];
//
//
//extern volatile unsigned char eusart1TxIndex; //index du buffer de transmission
//extern static unsigned char eusart1TxBuffer[EUSART1_TX_BUFFER_SIZE]; //Buffer de transmission
//
//extern volatile unsigned char eusart1RxIndex; //index du buffer de r�ception
//extern static unsigned char eusart1RxBuffer[EUSART1_RX_BUFFER_SIZE]; //Buffer d'�mission


//extern volatile unsigned char UART_TX_TEXT[EUSART1_TX_BUFFER_SIZE];
//extern volatile unsigned char UART_RX_TEXT[EUSART1_RX_BUFFER_SIZE];
//
//
//extern volatile unsigned char eusart1TxIndex; //index du buffer de transmission
//extern volatile unsigned char eusart1TxBuffer[EUSART1_TX_BUFFER_SIZE]; //Buffer de transmission
//
//extern volatile unsigned char eusart1RxIndex; //index du buffer de r�ception
//extern volatile unsigned char eusart1RxBuffer[EUSART1_RX_BUFFER_SIZE]; //Buffer d'�mission

#ifdef	__cplusplus
}
#endif

#endif	/* VARIABLE_EXTERN_H */
