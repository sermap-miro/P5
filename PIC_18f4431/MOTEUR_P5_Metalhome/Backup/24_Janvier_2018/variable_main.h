/* 
 * File:   variable_main.h
 * Author: sam
 *
 * Created on 17 janvier 2018, 16:59
 */

#ifndef VARIABLE_MAIN_H
#define	VARIABLE_MAIN_H

#ifdef	__cplusplus
extern "C" {
#endif

#include "define.h"
//16 bit
//volatile unsigned char Image_Courant_Moteur_1;
//volatile bit Nouvelle_Valeur_ADC;
//volatile int erreur;
//volatile signed int erreur_accumulator;
//volatile int consigne;
//volatile int consigne_pwm;
//volatile int consigne_pwm_max;


    
    unsigned char Etat;
    unsigned char Etat_Precedent;
    unsigned char Alarme;
    //unsigned char Action;
    
    
    
    
    
    
    
    
 volatile int duty; 
    
volatile int erreur;//volatile char erreur;

    

//8 bit
volatile unsigned char Image_Courant_Moteur_1;
volatile bit Nouvelle_Valeur_ADC;
//volatile unsigned char erreur_accumulator;//8bit
//volatile unsigned int erreur_accumulator;//16bit
volatile int erreur_accumulator;//16 bit
//volatile unsigned int erreur_accumulator;//16 bit
volatile unsigned int PID_out;
volatile unsigned int erreur_accumulator_max;//16 bit
//volatile unsigned short long erreur_accumulator;//32 bit
//
//volatile unsigned short long erreur_accumulator;//24 bit
//volatile unsigned short long erreur_accumulator_max;//24 bit
volatile char moteur_indice;
volatile char consigne;
volatile char direction;
volatile char consigne_pwm;
volatile char consigne_pwm_max;


    
    
//    
//
////8 bit
//volatile unsigned char Image_Courant_Moteur_1;
//volatile bit Nouvelle_Valeur_ADC;
//volatile char erreur;
////volatile unsigned char erreur_accumulator;//8bit
////volatile unsigned int erreur_accumulator;//16bit
//volatile unsigned int erreur_accumulator;//16 bit
//volatile unsigned int PID_out;
//volatile unsigned int erreur_accumulator_max;//16 bit
////volatile unsigned short long erreur_accumulator;//32 bit
////
////volatile unsigned short long erreur_accumulator;//24 bit
////volatile unsigned short long erreur_accumulator_max;//24 bit
//volatile char consigne;
//volatile char consigne_pwm;
//volatile char consigne_pwm_max;


volatile bit RX1_full;



#define EUSART1_TX_BUFFER_SIZE 128
#define EUSART1_RX_BUFFER_SIZE 128

extern unsigned char UART_TX_TEXT[EUSART1_TX_BUFFER_SIZE];
extern unsigned char UART_RX_TEXT[EUSART1_RX_BUFFER_SIZE];

//extern static unsigned char UART_TX_TEXT[EUSART1_TX_BUFFER_SIZE];
//extern static unsigned char UART_RX_TEXT[EUSART1_RX_BUFFER_SIZE];
//
//
//extern volatile unsigned char eusart1TxIndex; //index du buffer de transmission
//extern static unsigned char eusart1TxBuffer[EUSART1_TX_BUFFER_SIZE]; //Buffer de transmission
//
//extern volatile unsigned char eusart1RxIndex; //index du buffer de réception
//extern static unsigned char eusart1RxBuffer[EUSART1_RX_BUFFER_SIZE]; //Buffer d'émission



//
//
// unsigned char UART_TX_TEXT[EUSART1_TX_BUFFER_SIZE];
// unsigned char UART_RX_TEXT[EUSART1_RX_BUFFER_SIZE];
//
//
//volatile unsigned char eusart1TxIndex; //index du buffer de transmission
// unsigned char eusart1TxBuffer[EUSART1_TX_BUFFER_SIZE]; //Buffer de transmission
//
//volatile unsigned char eusart1RxIndex; //index du buffer de réception
// unsigned char eusart1RxBuffer[EUSART1_RX_BUFFER_SIZE]; //Buffer d'émission


//static unsigned char UART_TX_TEXT[EUSART1_TX_BUFFER_SIZE];
//static unsigned char UART_RX_TEXT[EUSART1_RX_BUFFER_SIZE];
//
//
//volatile unsigned char eusart1TxIndex; //index du buffer de transmission
//static unsigned char eusart1TxBuffer[EUSART1_TX_BUFFER_SIZE]; //Buffer de transmission
//
//volatile unsigned char eusart1RxIndex; //index du buffer de réception
//static unsigned char eusart1RxBuffer[EUSART1_RX_BUFFER_SIZE]; //Buffer d'émission


//volatile unsigned char UART_TX_TEXT[EUSART1_TX_BUFFER_SIZE];
//volatile unsigned char UART_RX_TEXT[EUSART1_RX_BUFFER_SIZE];
//
//
//volatile unsigned char eusart1TxIndex; //index du buffer de transmission
//volatile unsigned char eusart1TxBuffer[EUSART1_TX_BUFFER_SIZE]; //Buffer de transmission
//
//volatile unsigned char eusart1RxIndex; //index du buffer de réception
//volatile unsigned char eusart1RxBuffer[EUSART1_RX_BUFFER_SIZE]; //Buffer d'émission

#ifdef	__cplusplus
}
#endif

#endif	/* VARIABLE_MAIN_H */

