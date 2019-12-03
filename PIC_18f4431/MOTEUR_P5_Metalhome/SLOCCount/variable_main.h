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

    unsigned char Version;

    unsigned char Etat;
    unsigned char Etat_Log[NB_ACTION_LOG];
    unsigned char Alarme;
    //unsigned char Action;

    unsigned char Etat_Precedent_Index;


    // Paramètres de déplacement  


    unsigned char nb_s_fonctionnement; //Sauvegarde le temps entre pions
    unsigned char nb_s_patinage; //consigne de seconde qui défini le temps maximal avant de déclarer le mouvement en patinage


    unsigned char nb_100ms_Timer_5;

    unsigned char nb_100ms_pion; //
    unsigned char nb_100ms_platine;


    unsigned char nb_s_pelle;



    //Detection des pions
    volatile bit Detecteur_Pion;


    unsigned char nb_Pion; // Nombre de pion vu lors du deplacement



    volatile int duty;

    volatile int erreur; //volatile char erreur;



    //8 bit
    volatile unsigned char Image_Courant_Moteur_1;
    volatile unsigned char Image_Courant_Moteur_2;
    volatile bit Nouvelle_Valeur_ADC;
    //volatile unsigned char erreur_accumulator;//8bit
    //volatile unsigned int erreur_accumulator;//16bit
    volatile int erreur_accumulator; //16 bit
    //volatile unsigned int erreur_accumulator;//16 bit
    volatile unsigned int PID_out;
    volatile unsigned int erreur_accumulator_max; //16 bit
    //volatile unsigned short long erreur_accumulator;//32 bit
    //
    //volatile unsigned short long erreur_accumulator;//24 bit
    //volatile unsigned short long erreur_accumulator_max;//24 bit
    volatile char moteur_indice;
    unsigned char Consigne_en_A;
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



#define EUSART1_TX_BUFFER_SIZE 96
#define EUSART1_RX_BUFFER_SIZE 96

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

    
    
    
#ifdef	__cplusplus
}
#endif

#endif	/* VARIABLE_MAIN_H */

