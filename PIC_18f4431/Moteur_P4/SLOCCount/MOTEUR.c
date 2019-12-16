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


void Init_Variable(void){
    
    Version = 1;
    
    
    unsigned char i;
    
    for (i=0; i < NB_ACTION_LOG; i++){
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
    
    nb_100ms_Timer_5=0;
    
    nb_100ms_pion = 1;
    nb_100ms_platine = 10;
    
    nb_s_pelle = 30;
    
    Detecteur_Pion =0;
    nb_Pion = 0;
    
    
    
    moteur_indice = MOTEUR_1;
    consigne = 0;
    direction = 0;
}



//******************************************************************************
// FONCTION CYCLE MOTEUR
//******************************************************************************

void Cycle_Moteur(void) {
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
        
        
        
        switch(Etat){
            case ETAT_AVANCE: 
                 Moteur(MOTEUR_1, AVANT, consigne, OPTION_NULLE);
                break;
            case ETAT_RECULE: 
                 Moteur(MOTEUR_1, ARRIERE, consigne, OPTION_NULLE);
                break;
            case ETAT_PELLE_LEVE: 
                 Moteur(MOTEUR_2, AVANT, consigne, OPTION_NULLE);
                break;
            case ETAT_PELLE_BAISSE: 
                 Moteur(MOTEUR_2, ARRIERE, consigne, OPTION_NULLE);
                break;
                
            
            default: break;
            
            
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
    
    Cycle_Moteur();

}
//******************************************************************************



