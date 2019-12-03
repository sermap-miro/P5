
/**
  EUSART1 Generated Driver File

  @Company
    Microchip Technology Inc.

  @File Name
    eusart1.c

  @Summary
    This is the generated driver implementation file for the EUSART1 driver using MPLAB(c) Code Configurator

  @Description
    This header file provides implementations for driver APIs for EUSART1.
    Generation Information :
        Product Revision  :  MPLAB(c) Code Configurator - 3.15.0
        Device            :  PIC18F87K22
        Driver Version    :  2.00
    The generated drivers are tested against the following:
        Compiler          :  XC8 1.35
        MPLAB             :  MPLAB X 3.20
 */

/*
    (c) 2016 Microchip Technology Inc. and its subsidiaries. You may use this
    software and any derivatives exclusively with Microchip products.

    THIS SOFTWARE IS SUPPLIED BY MICROCHIP "AS IS". NO WARRANTIES, WHETHER
    EXPRESS, IMPLIED OR STATUTORY, APPLY TO THIS SOFTWARE, INCLUDING ANY IMPLIED
    WARRANTIES OF NON-INFRINGEMENT, MERCHANTABILITY, AND FITNESS FOR A
    PARTICULAR PURPOSE, OR ITS INTERACTION WITH MICROCHIP PRODUCTS, COMBINATION
    WITH ANY OTHER PRODUCTS, OR USE IN ANY APPLICATION.

    IN NO EVENT WILL MICROCHIP BE LIABLE FOR ANY INDIRECT, SPECIAL, PUNITIVE,
    INCIDENTAL OR CONSEQUENTIAL LOSS, DAMAGE, COST OR EXPENSE OF ANY KIND
    WHATSOEVER RELATED TO THE SOFTWARE, HOWEVER CAUSED, EVEN IF MICROCHIP HAS
    BEEN ADVISED OF THE POSSIBILITY OR THE DAMAGES ARE FORESEEABLE. TO THE
    FULLEST EXTENT ALLOWED BY LAW, MICROCHIP'S TOTAL LIABILITY ON ALL CLAIMS IN
    ANY WAY RELATED TO THIS SOFTWARE WILL NOT EXCEED THE AMOUNT OF FEES, IF ANY,
    THAT YOU HAVE PAID DIRECTLY TO MICROCHIP FOR THIS SOFTWARE.

    MICROCHIP PROVIDES THIS SOFTWARE CONDITIONALLY UPON YOUR ACCEPTANCE OF THESE
    TERMS.
 */

/**
  Section: Included Files
 */
#define EUSART_FILE
#include <xc.h>
//#include "eusart1.h"
#include <string.h> 
#include <stdio.h> 
//#include "define_mot.h"
//#include "relais.h"
//#include "lora.h"
//#include "eusart2.h"
//pour la fonction atoi()
#include <stdlib.h>

#include "variable_extern.h"
#include "Variables.h"

#include "horloge.h"

#include "eusart.h"

#include "action.h"
#include "interrupt.h"


//static unsigned char UART_TX_TEXT[EUSART1_TX_BUFFER_SIZE];

//
//static unsigned char UART_TX_TEXT[EUSART1_TX_BUFFER_SIZE];
//volatile unsigned char UART_RX_TEXT[EUSART1_RX_BUFFER_SIZE];


//volatile unsigned char eusart1TxIndex; //index du buffer de transmission
////static unsigned char eusart1TxBuffer[EUSART1_TX_BUFFER_SIZE]; //Buffer de transmission
//volatile unsigned char eusart1TxBuffer[EUSART1_TX_BUFFER_SIZE]; //Buffer de transmission
//
//volatile unsigned char eusart1RxIndex; //index du buffer de r�ception
////static unsigned char eusart1RxBuffer[EUSART1_RX_BUFFER_SIZE]; //Buffer d'�mission
//volatile unsigned char eusart1RxBuffer[EUSART1_RX_BUFFER_SIZE]; //Buffer d'�mission
//
//











//#include "conversion.h"
//#include "pid.h"
//#include "tmr0_mot.h"
/**
  Section: Macro Declarations
 */
//#define EUSART1_TX_BUFFER_SIZE 64
//#define EUSART1_RX_BUFFER_SIZE 64

/**
  Section: Global Variables
 */

/*
 Actuellement, c'est un traitement brute des donn�es qui sont effectu�.
 
 * Il n'y � aucun controle quand au d�passement de buffer, ni au contenu des donn�es
 * 
 * 
 => A FAIRE:
 * controle des datas (checksum, accus� de reception, controle du d�passement de buffer)
 
 
 */


////Indicateur du mode de fonctionnement
//extern unsigned char Mode_Fonctionnement;
////Consigne en vitesse
////extern int Vitesse_Consigne;
//extern float Vitesse_Consigne;


//extern unsigned int Seuil_Detection_Signal_Bobine;
//
//volatile unsigned char eusart1TxIndex; //index du buffer de transmission
//static unsigned char eusart1TxBuffer[EUSART1_TX_BUFFER_SIZE]; //Buffer de transmission
//
//volatile unsigned char eusart1RxIndex; //index du buffer de r�ception
//static unsigned char eusart1RxBuffer[EUSART1_RX_BUFFER_SIZE]; //Buffer d'�mission

//Indicateur:
//RX1_full = 1 => le buffer de r�ception contient une nouvelle commande
//RX1_full = 0 => le buffer de r�ception est vide ou en remplissage
//extern volatile bit RX1_full;
//extern unsigned char COMMANDE1[64];

//unsigned char COMMANDE1_buffer[64];
//extern unsigned char COMMANDE2[64];
//extern volatile long int ADCValue;

//extern int Vitesse_Mesure;
//extern float Vitesse_Mesure;
//
//extern float Position_K_p, Position_K_i, Position_K_d, Vitesse_K_p, Vitesse_K_i, Vitesse_K_d;

//unsigned int Variable_Debug;

void EUSART1_Check_Buffer(void) {

    if (RX1_full == 1) {//Le Wipy � parler
        
        //LED=1;
        EUSART1_RX_T3_LOCAL(UART_RX_TEXT[0],
                UART_RX_TEXT[1],
                UART_RX_TEXT[2],
                UART_RX_TEXT[3],
                UART_RX_TEXT[4],
                UART_RX_TEXT[5],
                UART_RX_TEXT[6],
                UART_RX_TEXT[7]);
       // LED=0;
        RX1_full = 0;
    }
}








/**
  Section: EUSART1 APIs
 */
//****************************************************************
//Fonction d'initialisation du port UART num�ro 1

void EUSART1_Initialize(void) {
    // Set the EUSART1 module to the options selected in the user interface.

    // disable interrupts before changing states
    PIE1bits.RC1IE = 0;
    PIE1bits.TX1IE = 0;

    // ABDOVF no_overflow; TXCKP async_noninverted_sync_fallingedge; RCIDL idle; BRG16 16bit_generator; WUE disabled; ABDEN disabled; RXDTP not_inverted; 
    BAUDCON = 0x48;
    BAUDCONbits.BRG16 = 1;

    //BAUDCONbits.TXCKP = 1;//Existe pas sur ce PIC!!!!

    // SPEN enabled; RX9 8-bit; RX9D 0; CREN disabled; ADDEN disabled; SREN disabled; 
    RCSTA1 = 0x80;

    // TX9 8-bit; TX9D 0; SENDB sync_break_complete; TXEN enabled; SYNC asynchronous; BRGH hi_speed; CSRC slave_mode; 
    TXSTA1 = 0x24;
    TXSTA1bits.SYNC = 0;
    TXSTA1bits.BRGH = 1;

    // Baud Rate = 57600; SPBRG1 34; 
    SPBRG = 0x22;
    SPBRG = 0x11; //115200??? presque
    SPBRG = 0x12; //115200??? non pas dans ce sens la
    SPBRG = 0x10; //115200 - Da
    // SPBRG = 0x67;

    // Baud Rate = 57600; SPBRGH1 0; 
    SPBRGH = 0x00;


    // initializing the driver state
    eusart1TxIndex = 0;
    eusart1RxIndex = 0;


    //Activation de la r�ception des caract�res par la mise � 1 du bit CREN

    RCSTA1bits.CREN = 1;
    // enable receive interrupt
    PIE1bits.RC1IE = 0;
    PIE1bits.RC1IE = 1;

    PIE1bits.TX1IE = 1;


    IPR1bits.TX1IP = 0;
    IPR1bits.RC1IP = 0;

    //Variable_Debug=0;
    RX1_full = 0;
}



//////
//////
//////        sprintf(UART_TX_TEXT, "m.Nb_Pion");
//////        //On transmet la r�ponse
//////        EUSART1_Buffer_Send();
//////        delay_1s();
//////        if(RX1_full == 1){
//////              //sprintf(UART_TX_TEXT, "print(\"UART RX TEXT = %s\")", UART_RX_TEXT);
//////              sprintf(UART_TX_TEXT, "%s", UART_RX_TEXT);
////////        On transmet la r�ponse
//////        EUSART1_Buffer_Send();
//////        }
//////
//////
//////
//////















void EUSART1_Send_Test(void){
    
 eusart1TxBuffer[0] = 0x31;
 eusart1TxBuffer[1] = 0x32;
 eusart1TxBuffer[2] = 0x33;
 eusart1TxBuffer[3] = 0x34; 
 eusart1TxBuffer[4] = 0x0D;   
 eusart1TxBuffer[5] = 0x00;   
    eusart1TxIndex = 0;
    TXREG1 = eusart1TxBuffer[eusart1TxIndex];
    PIE1bits.TX1IE = 1;
    
}




//****************************************************************
//Fonction qui se charge de transmettre le *text pass� en param�tre
//en lui rajoutant les caract�res de contr�le suivant:
// caract�re Carriage Return (Retour chariot): 13 (d�cimal) 0D (h�xad�cimal)
// caract�re line feed (nouvelle ligne): 10 (d�cimal) 0A (h�xad�cimal)

void EUSART1_Buffer_Send(char *text) {
//void EUSART1_Buffer_Send() {

    unsigned int i;

    while (!TRMT1); // On attend la fin de l'envoi pr�c�dent
    //for (i = 0; text[i] != '\0'; i++) {
    for (i = 0; (i< EUSART1_TX_BUFFER_SIZE) && (UART_TX_TEXT[i] != '\0'); i++) {
//UART_TX_TEXT
        //eusart1TxBuffer[i] = text[i];
        eusart1TxBuffer[i] = UART_TX_TEXT[i];
        //    for (i = 0; UART_TX_TEXT[i] != '\0'; i++) {
        //
        //        eusart1TxBuffer[i] = UART_TX_TEXT[i];
    }
    //    eusart1TxBuffer[i] = 0x0D; //caract�re 13 (CR)
    //    eusart1TxBuffer[i + 1] = 0x0A; //caract�re 10 (CR)
    //    eusart1TxBuffer[i + 2] = 0x00; //caract�re NULL (CR)
    eusart1TxBuffer[i] = 0x0D; //caract�re 13 (CR)
    //eusart1TxBuffer[i] = 0x0A; //caract�re 13 (CR)
    //    eusart1TxBuffer[i + 1] = 0x0A; //caract�re 10 (CR)
    eusart1TxBuffer[i + 1] = 0x00; //caract�re 10 (CR)
    //    eusart1TxBuffer[i + 2] = 0x00; //caract�re NULL (CR)
    eusart1TxIndex = 0;
    TXREG1 = eusart1TxBuffer[eusart1TxIndex];
    PIE1bits.TX1IE = 1;
    // TXREG1 = txData;    // Write the data byte to the USART.
}

//****************************************************************
//Fonction d'interruption de fin de transmission d'un caract�re par
//l'UART 1

void EUSART1_Transmit_ISR(void) {

    eusart1TxIndex++;
    if (eusart1TxBuffer[eusart1TxIndex] != '\0') {
        //PIR1bits.TX1IF = 0;
        //delay_ms(25);
        TXREG1 = eusart1TxBuffer[eusart1TxIndex];
    } else {
        PIE1bits.TX1IE = 0; //On d�sactive l'interruption 
        //de fin de transmission de caract�re
        //s'il n'y a plus de caract�re � transmettre
    }
}

//****************************************************************
//Fonction d'interruption de fin de r�ception d'un caract�re par
//l'UART 1

void EUSART1_Receive_ISR(void) {
    //    LATB3^=1;
    unsigned char i;
    // SORTIE_1 ^= 1; //Pour d�bug IHM
    if (1 == RCSTA1bits.OERR) {
        // EUSART1 error - restart
        RCSTA1bits.SPEN = 0;
        RCSTA1bits.SPEN = 1;
        RCSTA1bits.CREN = 0;
        RCSTA1bits.CREN = 1;
    }
    //LED=1;
    // buffer overruns are ignored
    eusart1RxBuffer[eusart1RxIndex] = RCREG1;

    //On attend de recevoir le caract�re <LF> (line feed)
    //qui correspond au dernier caract�re pr�sent dans les commandes
    //� traiter
    //if (eusart1RxBuffer[eusart1RxIndex] == '\r') {
    if ((RX1_full == 0)&&(eusart1RxBuffer[eusart1RxIndex] == 0x0d)) {

        //        eusart1RxIndex = 0;
        //        
        ////        if PIE1bits.TX1IE == 0
        //        RX1_full = 1;



        //On backup les donn�es UART
        for (i = 0; i < eusart1RxIndex; i++) {
            UART_RX_TEXT[i] = eusart1RxBuffer[i];
        }

        //        //On backup les donn�es UART
        //        for (i = 0; eusart1RxBuffer[i] != '\r' && eusart1RxBuffer[i] != '\n' && eusart1RxBuffer[i] != '\0'; i++) {
        //            UART_RX_TEXT[i] = eusart1RxBuffer[i];
        //        }

        UART_RX_TEXT[eusart1RxIndex] = '\0';
        //        UART_RX_TEXT[i] = '\0';


        eusart1RxIndex = 0;
        RX1_full = 1;



        //        EUSART1_RX_T3_LOCAL(UART_RX_TEXT[0],
        //                UART_RX_TEXT[1],
        //                UART_RX_TEXT[2],
        //                UART_RX_TEXT[3],
        //                UART_RX_TEXT[4],
        //                UART_RX_TEXT[5],
        //                UART_RX_TEXT[6],
        //                UART_RX_TEXT[7]);




    } else {
        if (eusart1RxIndex + 1 == EUSART1_RX_BUFFER_SIZE) {//Si le buffer est plein alors on le vide
            eusart1RxIndex = 0;
        } else {//Sinon on incr�mente l'index du buffer de reception
            eusart1RxIndex++;
        }
    }
}






//****************************************************************
//Fonction qui traite les donn�es re�us par l'UART 2 pour une commande locale
//On lui passe une adresse de commande: Ad
//Avec des donn�es (data): Da

void EUSART1_RX_T3_LOCAL(unsigned char Ad, unsigned char Da, unsigned char A, unsigned char B, unsigned char C, unsigned char D, unsigned char E, unsigned char F) {//SORTIE_1 ^= 1;
    int i;
    unsigned char Reponse;
    //On v�rifie que le message est destin�
    //� la carte �lectronique Armoire
    //=> le message re�u d�bute par MIR_ID
    //LATB3^=1;
    switch (Ad) {
        case 'L':
            LED = Da - 0x30;
            //On modifie la commutation des voies 1 � 7
            sprintf(UART_TX_TEXT, "LED = %d", (int) (Da - 0x30));
            EUSART1_Buffer_Send(UART_TX_TEXT);
            break;
        case 'i'://publication de l'image du courant
            sprintf(UART_TX_TEXT, "%d", Image_Courant_Moteur_1);
            EUSART1_Buffer_Send(UART_TX_TEXT);
            break;

        case 'p': //publication du statut
            sprintf(UART_TX_TEXT, "consigne=%d i_1=%d i_2=%d duty=%d erreur=%d Patinage_Nb_Essai=%d Capteur_Capot_Nb_Evenement=%d", consigne, Image_Courant_Moteur_1, Image_Courant_Moteur_2, duty, erreur, Patinage_Nb_Essai, Capteur_Capot_Nb_Evenement);
            //sprintf(UART_TX_TEXT, "abcdefghijklmnopqrstuvwxyz0123");
            //sprintf(UART_TX_TEXT, "0123abcdefghi");
            EUSART1_Buffer_Send(UART_TX_TEXT);
            break;

        case 's': // statut
            //sprintf(UART_TX_TEXT, "%02X%02X%02X", Etat, Etat_Precedent, Alarme);
            //sprintf(UART_TX_TEXT, "%02X%02X%02X", Etat, Etat_Precedent, Alarme);
            //sprintf(UART_TX_TEXT, "%02X%02X%02X", Etat, Etat_Precedent_Get(), Alarme);
            //Reponse = Etat_Get(0);
            sprintf(UART_TX_TEXT, "%02X%02X%02X", Etat_Get(0), Etat_Get(1), Alarme);
            //sprintf(UART_TX_TEXT, "%02X%02X%02X", Reponse, Etat_Get(1), Alarme);
            EUSART1_Buffer_Send(UART_TX_TEXT);
            break;



        case 'l': // log
            //sprintf(UART_TX_TEXT, "%02X%02X%02X", Etat, Etat_Precedent, Alarme);
            //sprintf(UART_TX_TEXT, "%02X%02X%02X", Etat, Etat_Precedent, Alarme);
            //sprintf(UART_TX_TEXT, "%02X%02X%02X", Etat, Etat_Precedent_Get(), Alarme);

            for (i = 0; i < NB_ACTION_LOG; i++) {
                //Etat_Precedent_Index
                //UART_TX_TEXT[i*3+0]= 
                //UART_TX_TEXT[i]= Etat_Intitule(Etat_Log[0]);
                UART_TX_TEXT[(unsigned char) (NB_ACTION_LOG - 1 - i)] = Etat_Intitule(Etat_Log[(unsigned char) ((Etat_Precedent_Index + i) % NB_ACTION_LOG)]);
            }

            UART_TX_TEXT[NB_ACTION_LOG] = 0x00;
            EUSART1_Buffer_Send(UART_TX_TEXT);
            break;


        case 'q': //publication du statut
            sprintf(UART_TX_TEXT, "nb_s=%d nb_Pion=%d nb_Timer_5=%d", nb_s_fonctionnement, nb_Pion, nb_100ms_Timer_5);
            //sprintf(UART_TX_TEXT, "abcdefghijklmnopqrstuvwxyz0123");
            //sprintf(UART_TX_TEXT, "0123abcdefghi");
            EUSART1_Buffer_Send(UART_TX_TEXT);
            break;

        case 'c': //Consigne

            consigne = (char)  (5 * Da);

            break;

        case 'E':
            sprintf(UART_TX_TEXT, "%d", Etat_Get((unsigned char) (Da - 0x30)));
            EUSART1_Buffer_Send(UART_TX_TEXT);
            break;


        case 'e':


            //            Etat = Da;
            Etat_Update(Da);



            break;


        case 'P'://Update Parameter
            //consigne = (unsigned char) (Da * 5);
            //            consigne = (unsigned char) (Da);
            //            nb_s_patinage = (unsigned char) A;
            //            nb_100ms_pion = (unsigned char) B;
            //            nb_100ms_platine = (unsigned char) C;
            //            nb_s_pelle = (unsigned char) D;
            switch (Da - 0x30) {
                case PARAMETER_CONSIGNE:
                    Consigne_en_A = (unsigned char) ((A - 0x30)*100 + (B - 0x30)*10 + (C - 0x30)*1);
                    consigne = (char) (Consigne_en_A * 5);
                    break;
                case PARAMETER_PATINAGE_S:
                    nb_s_patinage = (unsigned char) ((A - 0x30)*100 + (B - 0x30)*10 + (C - 0x30)*1);
                    break;
                case PARAMETER_PION_100MS:
                    nb_100ms_pion = (unsigned char) ((A - 0x30)*100 + (B - 0x30)*10 + (C - 0x30)*1);
                    break;
                case PARAMETER_PLATINE_100MS:
                    nb_100ms_platine = (unsigned char) ((A - 0x30)*100 + (B - 0x30)*10 + (C - 0x30)*1);
                    break;
                case PARAMETER_PELLE_S:
                    nb_s_pelle = (unsigned char) ((A - 0x30)*100 + (B - 0x30)*10 + (C - 0x30)*1);
                    break;
                case PARAMETER_CAPOT_NB_ESSAI:
                    Capteur_Capot_Nb_Evenement_Autoriser = (unsigned char) (A - 0x30);
                    break;
                case PARAMETER_PATINAGE_NB_ESSAI:
                    Patinage_Nb_Essai = (unsigned char) (A - 0x30);
                    break;



                default: break;



            }



        case 'V'://View Parameter
            //            nb_s_patinage = (unsigned char) Da;
            //            nb_100ms_pion = (unsigned char) A;
            //            nb_100ms_platine = (unsigned char) B;
            //            nb_s_pelle = (unsigned char) C;


            switch (Da - 0x30) {
                case VIEW_CONSIGNE:
                    sprintf(UART_TX_TEXT, "consigne=%d patin=%d pion=%d platine=%d pelle=%d", consigne, nb_s_patinage, nb_100ms_pion, nb_100ms_platine, nb_s_pelle);
                    //sprintf(UART_TX_TEXT, "abcdefghijklmnopqrstuvwxyz0123");
                    //sprintf(UART_TX_TEXT, "0123abcdefghi");
                    EUSART1_Buffer_Send(UART_TX_TEXT);
                    break;
                case VIEW_DEBUG:
                    sprintf(UART_TX_TEXT, "Etat=%d nb_s_fonctionnement=%d", Etat, nb_s_fonctionnement);
                    //sprintf(UART_TX_TEXT, "abcdefghijklmnopqrstuvwxyz0123");
                    //sprintf(UART_TX_TEXT, "0123abcdefghi");
                    EUSART1_Buffer_Send(UART_TX_TEXT);
                    break;
                case VIEW_ECHO:
                    //sprintf(UART_TX_TEXT, "%d", A);
                    UART_TX_TEXT[0]= A;
                    UART_TX_TEXT[1]= 0x00;
                    
                    //sprintf(UART_TX_TEXT, "abcdefghijklmnopqrstuvwxyz0123");
                    //sprintf(UART_TX_TEXT, "0123abcdefghi");
                    EUSART1_Buffer_Send(UART_TX_TEXT);
                    break;

                default: break;
            }

            break;


        case 'v'://version
            sprintf(UART_TX_TEXT, "%d", Version);
            EUSART1_Buffer_Send(UART_TX_TEXT);
            break;

        case 'S'://Show Status
            //            nb_s_patinage = (unsigned char) Da;
            //            nb_100ms_pion = (unsigned char) A;
            //            nb_100ms_platine = (unsigned char) B;
            //            nb_s_pelle = (unsigned char) C;
           // LED=1;
//#define PROTO_1
            //#undef PROTO_1
            //#define PROTO_2
            //#undef PROTO_2



#ifdef PROTO_1

            sprintf(UART_TX_TEXT, "%d %d %d %d %d %d %d %d %d %d %d", Etat_Get(0), Etat_Get(1), Alarme, nb_Pion, Image_Courant_Moteur_1, Image_Courant_Moteur_2, consigne, nb_s_patinage, nb_100ms_pion, nb_100ms_platine, nb_s_pelle);


//
// UART_TX_TEXT[0] = 0x31;
// UART_TX_TEXT[1] = 0x32;
// UART_TX_TEXT[2] = 0x33;
// UART_TX_TEXT[3] = 0x34; 
// UART_TX_TEXT[4] = 0x0D;   
// UART_TX_TEXT[5] = 0x00; 




#endif

#ifdef PROTO_2

            sprintf(UART_TX_TEXT, "%d %d %d %d %d %d %d %d %d %d %d %d %d %d", Etat_Get(0), Etat_Get(1), Alarme, nb_Pion, Image_Courant_Moteur_1, Image_Courant_Moteur_2, consigne, nb_s_patinage, nb_100ms_pion, nb_100ms_platine, nb_s_pelle, PION, CAPOT, RELAIS);
#endif

            //sprintf(UART_TX_TEXT, "%d %d %d %d %d %d %d %d %d %d %d", Etat, Etat_Precedent_Get(), Alarme, nb_Pion, Image_Courant_Moteur_1, Image_Courant_Moteur_2, consigne, nb_s_patinage, nb_100ms_pion, nb_100ms_platine, nb_s_pelle);
            //sprintf(UART_TX_TEXT, "abcdefghijklmnopqrstuvwxyz0123");
            //sprintf(UART_TX_TEXT, "0123abcdefghi");
            EUSART1_Buffer_Send(UART_TX_TEXT);
            break;



            //        case 'S'://Show Status
            ////            nb_s_patinage = (unsigned char) Da;
            ////            nb_100ms_pion = (unsigned char) A;
            ////            nb_100ms_platine = (unsigned char) B;
            ////            nb_s_pelle = (unsigned char) C;
            //            sprintf(UART_TX_TEXT, "%d %d %d %d %d %d %d", Image_Courant_Moteur_1, Image_Courant_Moteur_2, consigne, nb_s_patinage, nb_100ms_pion, nb_100ms_platine, nb_s_pelle);
            //            //sprintf(UART_TX_TEXT, "abcdefghijklmnopqrstuvwxyz0123");
            //            //sprintf(UART_TX_TEXT, "0123abcdefghi");
            //            EUSART1_Buffer_Send(UART_TX_TEXT);
            //            break;
            //            
            //            
            //        case 'T': // statut
            //            //sprintf(UART_TX_TEXT, "%02X%02X%02X", Etat, Etat_Precedent, Alarme);
            //            //sprintf(UART_TX_TEXT, "%02X%02X%02X", Etat, Etat_Precedent, Alarme);
            //            sprintf(UART_TX_TEXT, "%d %d %d", Etat, Etat_Precedent_Get(), Alarme);
            //            EUSART1_Buffer_Send(UART_TX_TEXT);
            //            break;



        case 'A':// arret

            Coupe_Moteur();
            // sortie(Ad - 'A' + '1', Da);
            break;



        case 'M':
            //Moteur((unsigned char) (Da-0x30), (unsigned char) (A-0x30), (unsigned char) ((B-0x30)*100+(C-0x30)*10+(D-0x30)*1), OPTION_NULLE); //Moteur(MOTEUR_1, AVANT, consigne, OPTION_NULLE); //256 // 13 A
            //  Moteur(MOTEUR_1, AVANT, 30, OPTION_NULLE); //Moteur(MOTEUR_1, AVANT, consigne, OPTION_NULLE); //256 // 13 A
            //  Moteur(MOTEUR_1, AVANT, 30, OPTION_NULLE);      
            //Moteur(MOTEUR_1, AVANT, 30, OPTION_NULLE);
           // LED=1;
           // EUSART1_Send_Test();
            moteur_indice = (unsigned char) (Da - 0x30);
            direction = (unsigned char) (A - 0x30);
            //consigne = (unsigned char) ((B - 0x30)*100 + (C - 0x30)*10 + (D - 0x30)*1);
            nb_Pion_Objectif = (unsigned char) ((B - 0x30)*100 + (C - 0x30)*10 + (D - 0x30)*1);

            switch (moteur_indice) {
                case MOTEUR_1:
                    Alarme=ALARME_NULLE;
                    Capteur_Capot_Nb_Evenement = Capteur_Capot_Nb_Evenement_Autoriser;
                    Patinage_Nb_Essai = Patinage_Nb_Essai_Autoriser;

                    switch (direction) {
                        case AVANT:
//                            LED=1;
                            if (Etat == ETAT_INACTIF) {
                                //                            Etat = ETAT_AVANCE;

                                Etat_Update(ETAT_AVANCE);
                            } else {
                                //Coupe_Moteur();
                                Etat_Update(ETAT_AVANCE);
                            }
                            break;

                        case ARRIERE:
                            if (Etat == ETAT_INACTIF) {
                                Etat_Update(ETAT_RECULE);
                            } else {
                                //Coupe_Moteur();
                                Etat_Update(ETAT_RECULE);
                            }
                            break;



                        default: break;
                    }


                    break;


                case MOTEUR_PELLE:
                    switch (direction) {
                        case MONTE:
                            //                            Etat = ETAT_PELLE_LEVE;
                            Etat_Update(ETAT_PELLE_LEVE);
                            break;

                        case DESCEND:
                            //                            Etat = ETAT_PELLE_BAISSE;
                            Etat_Update(ETAT_PELLE_BAISSE);
                            break;



                        default: break;
                    }


                    break;



                case MOTEUR_BEQUILLE:
                    switch (direction) {
                        case SORT:
                            //                            Etat = ETAT_PELLE_LEVE;
                            Etat_Update(ETAT_SORT_BEQUILLE);
                            break;

                        case RENTRE:
                            //                            Etat = ETAT_PELLE_BAISSE;
                            Etat_Update(ETAT_RENTRE_BEQUILLE);
                            break;



                        default: break;
                    }


                    break;


                default:
                    break;



            }



            break;


#ifdef PROTO_2
        case 'R': //Consigne

            RELAIS = Da;

            break;
#endif


        case 'f': //Consigne

            nb_s_fonctionnement = Da;

            break;



        case 'I': //Consigne

            IRQ_Execution(Da);

            break;



        case '0':
            //Etat = ETAT_INACTIF;
            Etat_Update(ETAT_INACTIF);
            break;

        case '1':
            //            Etat = ETAT_ALARME;

            // voie(Ad, Da); //EUSART2_RX_T3_LOCAL('1','1');
            break;
        case '2':
            // voie(Ad, Da); //EUSART2_RX_T3_LOCAL('1','1');
            break;
        case '3':
            // voie(Ad, Da); //EUSART2_RX_T3_LOCAL('1','1');
            break;
        case '4':
            // voie(Ad, Da); //EUSART2_RX_T3_LOCAL('1','1');
            break;
        case '5':
            // voie(Ad, Da); //EUSART2_RX_T3_LOCAL('1','1');
            break;
        case '6':
            // voie(Ad, Da); //EUSART2_RX_T3_LOCAL('1','1');
            break;
        case '7':
            // voie(Ad, Da); //EUSART2_RX_T3_LOCAL('1','1');
            break;
            //On modifie la commutation des sorties 1 � 3
        case 'B':
            //  sortie(Ad - 'A' + '1', Da);
            break;
            //        case 'V'://Pour Vitesse
            //            // sortie(Ad - 'A' + '1', Da);
            //            //break;
            //            //On re�oit l'ordre de lecture de la vitesse
            //            /*case 'T':
            //                //On demande la lecture de la temp�rature
            //                ADC_Start();
            //                //On attend la fin de la conversion anologique/num�rique
            //                while (!ADC_Ready());*/
            //            //On formate la r�ponse
            //            //sprintf(COMMANDE1, "%c%0.3d",0x30+lateralite, Vitesse_Mesure);
            //            sprintf(COMMANDE1, "M%c%03f", 0x30 + lateralite, Vitesse_Mesure);
            //            //On transmet la r�ponse
            //            EUSART1_Write_Text(COMMANDE1);
            //            break;
        case 'D'://Pour d�tection
            // sortie(Ad - 'A' + '1', Da);
            //break;
            //On re�oit l'ordre de lecture de la vitesse
            /*case 'T':
                //On demande la lecture de la temp�rature
                ADC_Start();
                //On attend la fin de la conversion anologique/num�rique
                while (!ADC_Ready());*/
            //On formate la r�ponse
            //                sprintf(COMMANDE1, "M%c%d",0x30+lateralite, Signal_Filoguidage);
            //On transmet la r�ponse
            //              EUSART1_Write_Text(COMMANDE1);
            break;

            //On peut modifier l'�tat de la led connect� au module LORA
            //        case 'D':
            //           // lora_Set_Led(Da);
            //            break;
            //Module Active Ecoute
            //        case 'E':
            //            // lora_Active_Ecoute();
            //            break;
            //Module Echo
        case 'F':
            // delay_100ms();
            //  sprintf(COMMANDE2, "radio tx %c%c%c%c%c%c", A, B, C, D, E, F);
            //On transmet la r�ponse
            //  EUSART2_Write_Text(COMMANDE2);
            //sprintf(COMMANDE1, "radio tx %c%c%c%c%c%c", A, B, C, D, E, F);
            //On transmet la r�ponse
            //EUSART1_Write_Text(COMMANDE1);
            break;
            //        case 'M':
            //            Mode_Fonctionnement = Da;
            //            break;
            //        case 'N':
            //            //Mode_Fonctionnement = Da;
            //            
            //            Seuil_Detection_Signal_Bobine = 0;
            //            Seuil_Detection_Signal_Bobine = (unsigned int) (valeur_caractere(Da)<<8);
            //            Seuil_Detection_Signal_Bobine += (unsigned int) (valeur_caractere(A)<<4);
            //            Seuil_Detection_Signal_Bobine += (unsigned int) (valeur_caractere(B));
            //    
            //            break;
            //        case 'S':
            //            Vitesse_Consigne = Da;
            //            break;
            //        case 'P':
            //            TMR0_StopTimer();
            //            PID_update(Da, A, valeur_caractere(B), valeur_caractere(C));
            //            TMR0_Initialize();
            //            TMR0_Reload16bit();
            //            TMR0_StartTimer();
            //            break;
        default:
            /*  ADC start  */
            /* Accus� de r�ception:
             * contiendras hypoth�tiquement la valeur de la temp�rature 
             * l'�tat du bouton d'urgence
             * 
             * 
             * 
             * 
             */


            break;
    }

    //On abaisse le drapeau de fin de reception de commande
    //RX1_full = 0;
}













//****************************************************************
//Fonction qui traite les donn�es re�us par l'UART 1
//et observe si le message est destin� au pr�sent PIC moteur

void EUSART1_RX_T3(void) {
    int i;




    unsigned char Redirection;
    //LATB3^=1;
    //
    //    //On backup les donn�es UART
    //    for (i = 0; eusart1RxBuffer[i] != '\0' && eusart1RxBuffer[i] != '\n' && eusart1RxBuffer[i] != '\r'; i++) {
    //        COMMANDE1_buffer[i] = eusart1RxBuffer[i];
    //    }
    //
    //    COMMANDE1_buffer[i] = '\0';
    //    



    //On se sert de la variable Redirection comme indicateur s'il faut ou non rediriger
    //le buffer de reception de l'UART 2 sur le buffer d'�mission de l'UART 1
    Redirection = 0;




    //    if (//la commande est destin� au microcontrolleur du moteur de la bonne lat�ralit�
    //
    //            // COMMANDE1_buffer[0] == lateralite // lateralit�
    //
    //            COMMANDE1_buffer[0] & (1 << lateralite)
    //
    //            ) {
    //        
    //        TRISCbits.RC6 = 0;

    EUSART1_RX_T3_LOCAL(UART_RX_TEXT[0],
            UART_RX_TEXT[1],
            UART_RX_TEXT[2],
            UART_RX_TEXT[3],
            UART_RX_TEXT[4],
            UART_RX_TEXT[5],
            UART_RX_TEXT[6],
            UART_RX_TEXT[7]);
    //        delay_1s();
    //        Redirection = 1;
    //On repositionne le module lora en mode �coute
    //lora_Active_Ecoute();
    //    } else {
    //        
    //        TRISCbits.RC6 = 1;
    //
    //        Redirection = 1;
    //    }






    //
    //    if (Redirection == 1) {
    //        for (i = 0; COMMANDE1_buffer[i] != '\0' && COMMANDE1_buffer[i] != '\n' && COMMANDE1_buffer[i] != '\r'; i++) {
    //            COMMANDE1[i] = COMMANDE1_buffer[i];
    //        }
    //
    //        COMMANDE1[i] = '\r';
    //        COMMANDE1[i + 1] = '\n';
    //        COMMANDE1[i + 2] = '\0';
    //        EUSART1_Write_Text((char *) COMMANDE1);
    //    }
    //    









    //    else{
    //        COMMANDE1[0] = '\0';
    //    }










    //On abaisse le drapeau de fin de reception de commande
    RX1_full = 0;
}



/**
  End of File
 */
