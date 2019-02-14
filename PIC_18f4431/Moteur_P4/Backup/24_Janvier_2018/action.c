

#include <xc.h>

#include "Variables.h"
#include "adc.h"
#include "pwm.h"
#include "timer.h"
#include <string.h> 
#include <stdio.h> 
#include <stdlib.h>
#include "eusart.h"
#include "horloge.h"

#include "action.h"
#include "variable_extern.h"



void Coupe_Moteur(void){
       TIMER2_Off();

    //PIE3bits.PTIE = 0;
    //PIE1bits.ADIE = 0;
//    LED = 0;
    DRIVER_M1 = 0;
    DRIVER_M2 = 0;
    OVDCOND = 0b00000000;
    STOP_M1;
    STOP_M2;
    delay_ms(50);
}


void Etat_Update(unsigned char etat_new_value) {
    Etat_Precedent = Etat;
    Etat = etat_new_value;


}

//
//void action_EUSART1_Check_Buffer(void) {
//
//    if (RX1_full == 1) {//Le Wipy à parler
//        EUSART1_RX_T3_LOCAL(UART_RX_TEXT[0],
//                UART_RX_TEXT[1],
//                UART_RX_TEXT[2],
//                UART_RX_TEXT[3],
//                UART_RX_TEXT[4],
//                UART_RX_TEXT[5],
//                UART_RX_TEXT[6],
//                UART_RX_TEXT[7]);
//
//        RX1_full = 0;
//    }
//}
//





//
////******************************************************************************
//// FONCTION  MOTEUR1 AV
////******************************************************************************
//
//void Moteur1_AV(/*int consigne*/) {
//    /*unsigned */int i;
//    //int erreur;
////    int duty = 0;
//
//
//    //Init_PWM();
//
//
//    AV_M1;
//    PDC0L = 0;
//    PDC0H = 0;
//    OVDCOND = 0b00000001;
//    DRIVER_M1 = 1;
//
//
//    TMR2 = 0;
//    TMR2IF = 0;
//    do {
//        if (TMR2IF == 1) {
//            TMR2IF = 0;
//            i = lecture_I_Mot1();
//            erreur = consigne - i;
//            //   erreur = erreur * 3;
//            //erreur = erreur >> 4;
//            erreur = erreur >> 3;
//            duty = erreur;
//            //            if (erreur > 0){
//            //            duty =  100;}
//            if (duty > 100) duty = 100;
//            else if (duty < 0) duty = 0;
//            PDC0L = (char) (duty << 2);
//            PDC0H = (char) ((duty << 2) >> 8);
//        }
//    } while (AV_1 == 1); //AV_1
//    DRIVER_M1 = 0;
//    OVDCOND = 0b00000000;
//    STOP_M1;
//    //  LED = 0;
//}
//
////******************************************************************************
//// FONCTION  MOTEUR1 AV
////******************************************************************************
//
//void u_Moteur1_AV(unsigned char consigne) {
//    //unsigned char i; //, i_min, i_max;
//    unsigned char i, i_min, i_max;
//    //    unsigned int erreur;
//    //    //unsigned char erreur;
//    //    unsigned int erreur_accumulator;
//
//#define ACCUMULATOR_SHIFT 2
//    //    unsigned int duty = 0;
////    unsigned char duty;
//    unsigned int index;
//    unsigned char direction;
//    // bit Unique;
//
//    //unsigned char 
//
//    u_Init_PWM();
//    u_lecture_I_Mot1_init();
//    //Init_ADC_PWM();
//    //Init_ADC_PWM_Trig();
//    //Init_ADC_PWM_Trig();
//Init_ADC_Single_Shoot_I_Moteur_1();
//    index = 0;
//
//    TMR2 = 0;
//    TMR2IF = 0;
//
//
//
//    AV_M1;
//    PDC0L = 1 << 2;
//    PDC0H = 0;
//    OVDCOND = 0b00000001;
//    DRIVER_M1 = 1;
//
//    /*
//     Ajout seconde PWM
//     */
//    //    
//    //    PDC1L = 1<<2;
//    //    PDC1H = 0;
//    //    
//    //        i = 25;
//    //        i = 15;
//    //            PDC1L = (char) (25 << 2);
//    //            PDC1H = 25 >> 6;
//    //    //OVDCOND = 0b00000101; 
//    //    AV_M2;
//    //    OVDCOND = 0b00000101; 
//    //    DRIVER_M2 = 1;
//    //    
//    //    while(1){
//    //        LED =1;
//    //        LED =0;
//    //        
//    //    }
//
//    /*
//     Ajout seconde PWM
//     */
//
//
//    //    //erreur=3;
//    //    erreur = 31;
//    //    //erreur = 0;
//    //    u_lecture_I_Mot1_init();
//    //    PTIF = 0;
//    //    while (PTIF == 0) NOP();
//    //    PTIF = 0;
//
//    //erreur = 31;
//    //erreur = 5;
//    erreur = 31;
//    erreur = 31;
//    erreur = 7;
//    erreur = 1;
//    PDC0L = ((unsigned char) erreur) << 2;
//    PDC0H = ((unsigned char) erreur) >> 6;
//
//    ////////     PIE3bits.PTIE = 1;
//    //////    do{
//    //////    
//    //////        //LED = ADIF;
//    //////       // ADIF=0;
//    ////////        if(ADIF == 1){
//    ////////        LED = 1;
//    ////////        ADIF=0;
//    ////////        }else{
//    ////////            LED=0;
//    ////////        }
//    //////         LED=0;
//    //////          LED=1;
//    //////////////        if(PTIF == 1){
//    //////////////        LED = 1;
//    //////////////        PTIF=0;
//    //////////////        }else{
//    //////////////            LED=0;
//    //////////////        }
//    ////////        LED = 1;
//    ////////        LED = 0;
//    //////    }
//    //////    while(AV_1 == 1);
//    //////    
//    //////    
//    //////    
//    ////////     while (AV_1 == 1); //AV_1
//    //////     
//    //////    DRIVER_M1 = 0;
//    //////    OVDCOND = 0b00000000;
//    //////    STOP_M1;
//    ////////    PDC0L = 0;
//    ////////    PDC0H = 0;
//    //////    //while(1);//
//    //////     return;
//    //////    
//    //////    //    do{
//    //////    //    LED=PTIF;
//    //////    //    PTIF=0;
//    //////    ////    LED=PTDIR;
//    //////    //////    PTIF=0;
//    //////    //    }while (AV_1 == 1);
//    //////    GODONE = 1;
//    //////    PIE3bits.PTIE = 1;
//    //////    do{
//    //////    
//    //////        //LED = ADIF;
//    //////       // ADIF=0;
//    ////////        if(ADIF == 1){
//    ////////        LED = 1;
//    ////////        ADIF=0;
//    ////////        }else{
//    ////////            LED=0;
//    ////////        }
//    //////        if(PTIF == 1){
//    //////        LED = 1;
//    //////        PTIF=0;
//    //////        }else{
//    //////            LED=0;
//    //////        }
//    ////////        LED = 1;
//    ////////        LED = 0;
//    //////    }
//    //////    while(1);
//    //////        
//    //////        
//    //////        
//
//
//    //    
//    //    do {
//    //    
//    //        while(Nouvelle_Valeur_ADC==0);
//    //        Nouvelle_Valeur_ADC=0;
//    //        
//    //    
//    //    } while (AV_1 == 1); //AV_1
//    //    
//    //RB0 = 1;
//    
//  //      consigne_pwm_max = 101;//((0xff >> PWM_SHIFT) + 1);
//    erreur_accumulator = 0;
////    erreur_accumulator = 0x8fff;
//    
//    
////    
////    consigne_pwm_max = ((0xff >> PWM_SHIFT) + 1);
////    erreur_accumulator = 0;
////    erreur_accumulator = 0x8fff;
//    
//    
//    
//    
//    
//    
//    
//    Nouvelle_Valeur_ADC = 0; //Initialisation du drapeau de fin de conversion (nouvelle image du courant disponible)
//    direction = 0;
//    i_min = 31;
//    i_max = 0;
//    while (PTDIR == 1) NOP();
//    while (PTDIR == 0) NOP();
//
//
//    LED = 1;
//
//    PIE3bits.PTIE = 0;
//    PIE1bits.ADIE = 1;
//    PIE1bits.ADIE = 1;
//
//    PEIE = 1;
//    GIE = 1;
//    TIMER2_On();
//    ADIF = 0;
//    do {
//
//        
//        
////        if(Nouvelle_Valeur_ADC==1){
////        Nouvelle_Valeur_ADC=0;
////        
////           // i = lecture_I_Mot1();
////      //  LED=1;
////           // erreur  = consigne - i;
////            erreur  = consigne - Image_Courant_Moteur_1;
////            if( erreur >= 10   ) duty++;
////            else if (erreur < 0 ) duty --;
//////            erreur = erreur >> 4;
//////            duty =  erreur + duty;
////            
////            if (duty > 100 ) duty = 100;
////            else if (duty < 0) duty = 0;  
////            PDC0L  =(char)(duty << 2);
////            PDC0H  =(char)((duty << 2)>>8);
////       //    LED = 0;
////
////        }
//        
//        
//        
//        
////        if (ADIF == 1) {
////            ADIF = 0;
////            LED = 1;
////            LED = 0;
////
////
////        }
//
//        ////////        
//        ////////        
//        ////////        delay_1s();
//        ////////        
//        ////////        
//        ////////            sprintf(UART_TX_TEXT, "m.bip(0.1)");
//        ////////                    //On transmet la réponse
//        ////////                    EUSART1_Buffer_Send();
//        ////////                  delay_1s();  
//        ////////        //          delay_1s();  
//        ////////        //          delay_1s();  
//        ////////        //          delay_1s();  
//        ////////        //          delay_1s();  
//        ////////        //    sprintf(UART_TX_TEXT, "print('Capteur 1Capot Pid out = %d')",PID_out);
//        ////////        sprintf(UART_TX_TEXT, "m.Nb_Pion=%d", 47);
//        ////////        //On transmet la réponse
//        ////////        EUSART1_Buffer_Send();
//        ////////        delay_1s();
//        //////////        if(RX1_full == 1){
//        //////////              sprintf(UART_TX_TEXT, "print(\"UART RX TEXT = %s\")", UART_RX_TEXT);
//        ////////////        On transmet la réponse
//        //////////        EUSART1_Buffer_Send();
//        //////////        }
//        ////////        //sprintf(UART_TX_TEXT, "print('m.Nb_Pion')");
//        ////////        sprintf(UART_TX_TEXT, "m.Nb_Pion");
//        ////////        //On transmet la réponse
//        ////////        EUSART1_Buffer_Send();
//        ////////        delay_1s();
//        ////////        if(RX1_full == 1){
//        ////////              //sprintf(UART_TX_TEXT, "print(\"UART RX TEXT = %s\")", UART_RX_TEXT);
//        ////////              sprintf(UART_TX_TEXT, "%s", UART_RX_TEXT);
//        //////////        On transmet la réponse
//        ////////        EUSART1_Buffer_Send();
//        ////////        }
//        //////////      
//        //////////        eusart1RxIndex = 0;
//        //////////        eusart1RxBuffer[eusart1RxIndex] = '\0';
//        ////////
//        ////////        delay_1s();
//        ////////        delay_1s();
//        //////////        delay_1s(); 
//        //////////        delay_1s();
//        //////////        delay_1s();
//        //////////        delay_1s();
//        //////////        delay_1s();
//        //////////        delay_1s();
//        //////////        delay_1s();
//        //////////        delay_1s();
//        ////////
//        ////////        
//
//        //     while(Nouvelle_Valeur_ADC==0) NOP();   
//        //        Nouvelle_Valeur_ADC=0;
//
//
//        //i = u_lecture_I_Mot1();
//        //GODONE = 1;
//        /////        //while(BFEMT==1) NOP();
//        //while(Nouvelle_Valeur_ADC==0) NOP();
//        //Nouvelle_Valeur_ADC=0;
//        //NOP();
//
//        //
//        //        if (PTDIR == 1) {
//        //        //if (PTDIR == 0) {
//        //            if (erreur > INDICE_SIGMOIDE){
//        //            while (PTDIR == 1) NOP();
//        //            }
//        //        } else {
//        //            if (erreur <= INDICE_SIGMOIDE){
//        //            while (PTDIR == 0) NOP();
//        //            }
//        //        }
//        //direction=1;
//        //LED^=1;
//        //        LED=1;
//        //        LED=0;
//        //        //while (PTDIR == 0) NOP();
//        //        while (PTDIR == direction) NOP();
//        //        direction^=1;
//        // LED=0;
//
//
//        //        i = u_lecture_I_Mot1();
//        //        Image_Courant_Moteur_1
//        //        if (i>i_max) i_max=i;
//        //        if (i<i_min) i_min=i;
//        //
//        //        if (i >= consigne) {
//        //            //erreur = 0;//Consigne atteinte ou dépassé => On n'envoi pas de courant
//        //            erreur_accumulator = 0;
//        //            
//        //            //erreur = 1; //Consigne atteinte ou dépassé => On n'envoi pas de courant
//        //        } else {
//        //            erreur = consigne - i;
//        //            //erreur = erreur >> 3;//Fonctionnement attendu
//        //           // erreur = erreur >> 3;//Fonctionnement attendu
//        //            //erreur = erreur >> 4;
//        //            erreur = erreur >> 1; //P(ID)
//        //            //erreur = erreur >> 2;//Fonctionnement test pleine onde
//        //            if (erreur >= 32) erreur = 31; // Vakeur max pour le registre de la PWM => on maximise sans atteindre
//        //            //if (erreur >= 31) erreur = 30; // Vakeur max pour le registre de la PWM => on maximise sans atteindre
//        // 
//        //        erreur_accumulator = erreur_accumulator + erreur;
//        //        ACCUMULATOR_SHIFT
//        //                
//        //               }
//        //        while(BFEMT==0) NOP();
//        //        while(BFEMT==1) NOP();
//        //        i = Image_Courant_Moteur_1;
//        //        erreur = consigne - i;
//        //        erreur_accumulator = erreur_accumulator + erreur;
//        //        
//        //        //Pour la consigne PWM
//        //        erreur = erreur + erreur_accumulator; //(P)I(D)
//        //        erreur = erreur >> 1; //P(ID)
//        //        
//        //   // erreur = 31;//Test pleine onde //DEBUG
//        //        PDC0L = ((unsigned char) erreur) << 2;
//        //        PDC0H = ((unsigned char) erreur) >> 6;
//
//
//        //i = i>>3;
//        //i = 15;
//        // i=i>>3;//Normal
//        //i=i>>2;//X2
//        //            PDC1L = (char) (i << 2);
//        //            PDC1H = i >> 6;
//
//        //        if(erreur>15){
//        //            
//        //            
//        //        }else{
//        //            
//        //        }
//        //        
//
//
//        //    PTIF = 0;
//        //    while (PTIF == 0) NOP();
//        //    PTIF = 0;
//
//
//        //PDC0L = 0x02;
//        //        if (TMR2IF == 1) {
//        //            TMR2IF = 0;
//        //while(PTDIR==0) PTIF = 0;
//        //        while(PTDIR==0) NOP();
//        //        if ((PTIF == 1) && (PTDIR=1) ){
//        ////////        while(PTDIR==1) NOP();
//        ////////        if ((PTIF == 1) && (PTDIR==0)){
//        //        while(PTDIR==0) NOP();
//        //        if ((PTIF == 1) && (PTDIR==1)){
//
//        //if(erreur>2) direction = 0; else direction =1;
//        //if (erreur > 16) direction = 0; else direction = 1; //permet un déclenchement de la mesure suivant la valeur de duty cycle de la PWM
//        //if (erreur > 20) {direction = 0; }else{ direction = 1;} //permet un déclenchement de la mesure suivant la valeur de duty cycle de la PWM
//        //direction = 1;//PWM == Etat Bas
//        //direction = 0;//PWM == Etat Haut
//        // if(erreur>4) direction = 1; else direction =0;
//        //while(PTDIR==direction) NOP();
//        //direction=1;
//
//        //        if (PTDIR != direction) {
//        //            // while(PTDIR!=direction) PTIF = 0;
//        //            while (PTIF == 0) NOP();
//        //            while (PTIF == 0) NOP();
//        //        } else {
//        //            while (PTIF == 0) NOP();
//        //        }
//        //
//        //        if (erreur > 16) {
//        //
//        //        } else {
//        //
//        //        }
//
//
//        //
//        //        if (PTDIR == 1) {//décrémente le compteur
//        //            // while(PTDIR!=direction) PTIF = 0;
//        //            if (erreur > 16) {
//        //                while (PTIF == 0) NOP();
//        //                PTIF = 0;
//        //                while (PTIF == 0) NOP();
//        //                PTIF = 0;
//        //            } else {
//        ////                while (PTIF == 0) NOP();
//        ////                PTIF = 0;
//        //                while (PTIF == 0) NOP();
//        //                PTIF = 0;
//        //            }
//        //        } else {
//        //            if (erreur > 16) {
//        ////                while (PTIF == 0) NOP();
//        ////                PTIF = 0;
//        //                while (PTIF == 0) NOP();
//        //                PTIF = 0;
//        //            } else
//        //                while (PTIF == 0) NOP();
//        //                PTIF = 0;
//        //                while (PTIF == 0) NOP();
//        //                PTIF = 0;
//        //        }
//
//        //
//        //        if (PTDIR == 1) {//décrémente le compteur
//        //            // while(PTDIR!=direction) PTIF = 0;
//        //            if (erreur > 16) {
//        //                while (PTDIR == 1) NOP();
//        //                //PTIF = 0;
//        ////                while (PTIF == 0) NOP();
//        ////                PTIF = 0;
//        //            } 
//        ////            else {
//        //////                while (PTIF == 0) NOP();
//        //////                PTIF = 0;
//        ////                while (PTIF == 0) NOP();
//        ////                PTIF = 0;
//        ////            }
//        //        } else {
//        //            if (erreur > 16) {
//        ////                while (PTIF == 0) NOP();
//        ////                PTIF = 0;
//        //                while (PTIF == 0) NOP();
//        //                PTIF = 0;
//        //            } else
//        //                while (PTIF == 0) NOP();
//        //                PTIF = 0;
//        //                while (PTIF == 0) NOP();
//        //                PTIF = 0;
//        //        }
//
//        //                while (PTIF == 0) NOP();
//        //                PTIF = 0;
//
//        //if (PTDIR == direction) {
//        //while (PTDIR == direction) PTIF = 0;
//        //if ((PTIF == 1) && (PTDIR != direction)) {
//        //        
//        //        while(PTDIR==1) NOP();
//        //        if ((PTIF == 1) && (PTDIR==0)){
//
//
//        // index+=1;
//        //if ((PTIF == 1) && (PTDIR=0) ){
//        //PTIF = 0;
//
//        //            LED = 1;
//        //index+=1;
//        //        i = u_lecture_I_Mot1();
//        //            LED = 0;
//        // i = (i>>1)<<1;
//        //i = i>>4;
//        //i = i>>2;
//
//
//        //i = i>>2;
//
//
//
//        //            if (i>i_max) i_max=i;
//        //            if (i<i_min) i_min=i;
//
//        //        if (i >= consigne) {
//        //            //erreur = 0;//Consigne atteinte ou dépassé => On n'envoi pas de courant
//        //            erreur = 1; //Consigne atteinte ou dépassé => On n'envoi pas de courant
//        //        } else {
//        //            erreur = consigne - i;
//        //            erreur = erreur >> 3;
//        //            //if (erreur >= 32) erreur = 31; // Vakeur max pour le registre de la PWM => on maximise sans atteindre
//        //            //if (erreur >= 31) erreur = 30; // Vakeur max pour le registre de la PWM => on maximise sans atteindre
//        //        }
//        //PDC0L = erreur;
//
//        // i ^= i;
//
//        //PDC0L = 0x32;//50
//        //PDC0L = 0x64;//100
//
//        //PDC0L = 0x08;
//        //PDC0L = 0x0A;
//
//        //PDC0L = (~i)>>4;
//        //PDC0L = (0xff-i)>>6;
//        //PDC0L = (0xff-i);
//        ////////            i=0xff-i;
//        ////////            i=0xff-i;
//        //i=i>>3;//
//        //i=i>>4;//
//        //i = i & 0x1f;
//        ////////            i = i & 0x1f;
//        //PDC0L = i  & 0x0f;
//        ////////            PDC0L = i;//  & 0x0f;
//        //            PDC0L = 3;//  & 0x0f;
//        ////////            duty = (0xff)>>4;
//        ////////            
//        ////////            PDC0L = (char) (duty << 2);
//        ////////            PDC0H = (char) ((duty << 2) >> 8);
//        //            duty = erreur;
//        //            //duty = duty & 0x1f;
//        //            PDC0L = (duty | 0x01)<<2;
//        //            PDC0H = duty >> 6;
//
//
//        //PDC0L = (erreur | 0x01)<<2;
//        //erreur  = 0xff >> 3;
//        //erreur = 30;
//        //        PDC0L = erreur << 2;
//        //        PDC0H = erreur >> 6;
//        // PDC0L = 0xc4;
//        // PDC0H = 0;
//        //PDC0L = 0x1f;
//        //////            PDC0L = 0x08;
//        //PDC0L = (~i);
//        // PDC0L =~(i>>2);
//        //PDC0L = 0x1F;
//        //PDC0L = 0x20;
//        //PDC0L = 0xff;
//        // PDC0L = 0x07;
//        //PDC0H = 0x01;
//        // PDC0L = 0x0f;
//        //PDC0L = index >> 4;
//        //PDC0L += 1;
//        //PTPERL = 0x0F;
//        //PTPERL = ~i;
//        //PTPERL = 0x0f;
//        //PTMRL = 0x1F;
//
//
//        // }
//
//
//        // LED = 0;
//        //PTIF = 0;
//        //            PDC0L = (char) (duty << 2);
//        //            PDC0H = (char) ((duty << 2) >> 8);
//        //    }
//        // }
//
//
//        // } while (1); //AV_1
//    } while (AV_1 == 1); //AV_1
//
//    TIMER2_Off();
//
//    PIE3bits.PTIE = 0;
//    PIE1bits.ADIE = 0;
//    LED = 0;
//    DRIVER_M1 = 0;
//    OVDCOND = 0b00000000;
//    STOP_M1;
//    //  LED = 0;
//}
//
////******************************************************************************
//// FONCTION  MOTEUR1 AR
////******************************************************************************
//
//void Moteur1_AR(int consigne) {
//    /*unsigned */ int i;
//    //    int erreur;
////    int duty = 0;
//
//
//    Init_PWM();
//    AR_M1;
//    PDC0L = 0;
//    PDC0H = 0;
//    OVDCOND = 0b00000001;
//    DRIVER_M1 = 1;
//    TMR2 = 0;
//    TMR2IF = 0;
//    do {
//        if (TMR2IF == 1) {
//            TMR2IF = 0;
//            LED = 1;
//            i = lecture_I_Mot1();
//            erreur = consigne - i;
//            //  erreur = erreur * 3;
//            erreur = erreur >> 2;
//            duty = erreur;
//            if (duty > 100) duty = 100;
//            else if (duty < 0) duty = 0;
//            //duty = 100;//DEBUG
//            PDC0L = (char) (duty << 2);
//            PDC0H = (char) ((duty << 2) >> 8);
//            LED = 0;
//        }
//    } while (AR_1 == 1);
//    DRIVER_M1 = 0;
//    OVDCOND = 0b00000000;
//    STOP_M1;
//}
//******************************************************************************
// FONCTION  MOTEUR1 AV
//******************************************************************************
//
//void Moteur2_AV(int consigne) {
//    int i;
//    //    int erreur;
//    //    int duty = 0;
//    PDC1L = 0;
//    PDC1H = 0;
//    AV_M2;
//
//    OVDCOND = 0b00000100;
//    DRIVER_M2 = 1;
//    TMR2 = 0;
//    TMR2IF = 0;
//    do {
//        if (TMR2IF == 1) {
//            i = lecture_I_Mot2();
//            erreur = consigne - i;
//            erreur = erreur * 3;
//            erreur = erreur >> 5;
//            duty = erreur;
//            if (duty > 100) duty = 100;
//            else if (duty < 0) duty = 0;
//            PDC1L = (char) (duty << 2);
//            PDC1H = (char) ((duty << 2) >> 8);
//        }
//    } while (AV_2 == 1);
//    DRIVER_M2 = 0;
//    OVDCOND = 0b00000000;
//    STOP_M2;
//
//}
////******************************************************************************
//// FONCTION  MOTEUR1 AV
////******************************************************************************
//
//void Moteur2_AR(int consigne) {
//    int i;
//    //    int erreur;
//    //    int duty = 0;
//    PDC1L = 0;
//    PDC1H = 0;
//    AR_M2;
//
//    OVDCOND = 0b00000100;
//    DRIVER_M2 = 1;
//    TMR2 = 0;
//    TMR2IF = 0;
//    do {
//        if (TMR2IF == 1) {
//            i = lecture_I_Mot2();
//            erreur = consigne - i;
//            erreur = erreur * 3;
//            erreur = erreur >> 5;
//            duty = erreur;
//            if (duty > 100) duty = 100;
//            else if (duty < 0) duty = 0;
//            PDC1L = (char) (duty << 2);
//            PDC1H = (char) ((duty << 2) >> 8);
//        }
//
//    } while (AR_2 == 1);
//    DRIVER_M2 = 0;
//    OVDCOND = 0b00000000;
//    STOP_M1;
//}
//
//
//
////******************************************************************************
//// FONCTION  MOTEUR1 AV
////******************************************************************************
//
//void Moteur1_old(unsigned char direction, unsigned char consigne) {
//    //unsigned char i; //, i_min, i_max;
//    unsigned char i, i_min, i_max;
//    //    unsigned int erreur;
//    //    //unsigned char erreur;
//    //    unsigned int erreur_accumulator;
//
//#define ACCUMULATOR_SHIFT 2
//    //    unsigned int duty = 0;
//    //    unsigned char duty;
//    unsigned int index;
//    // unsigned char direction;
//    // bit Unique;
//
//    //unsigned char 
//
//    u_Init_PWM();
//    // u_lecture_I_Mot1_init();
//    //Init_ADC_PWM();
//    //Init_ADC_PWM_Trig();
//    //Init_ADC_PWM_Trig();
//
//
//
//    Init_ADC_Single_Shoot_I_Moteur_1();
//
//
//
//    index = 0;
//
//    TMR2 = 0;
//    TMR2IF = 0;
//
//
//    if (direction == AVANT) {
//        AV_M1;
//    } else {
//        AR_M1;
//    }
//    PDC0L = 1 << 2;
//    PDC0H = 0;
//    OVDCOND = 0b00000001;
//    DRIVER_M1 = 1;
//
//
//    erreur = 31;
//    erreur = 31;
//    erreur = 7;
//    erreur = 1;
//    PDC0L = ((unsigned char) erreur) << 2;
//    PDC0H = ((unsigned char) erreur) >> 6;
//
//
//    erreur_accumulator = 0;
//
//
//
//
//    Nouvelle_Valeur_ADC = 0; //Initialisation du drapeau de fin de conversion (nouvelle image du courant disponible)
//    direction = 0;
//    i_min = 31;
//    i_max = 0;
//    while (PTDIR == 1) NOP();
//    while (PTDIR == 0) NOP();
//
//
//    LED = 1;
//
//    PIE3bits.PTIE = 0;
//    PIE1bits.ADIE = 1;
//    PIE1bits.ADIE = 1;
//
//    PEIE = 1;
//    GIE = 1;
//    TIMER2_On(); //fréquence d'echantillonnage
//    ADIF = 0;
//    do {
//
//        //        sprintf(UART_TX_TEXT, "m.I_Moteur_1=%d", Image_Courant_Moteur_1);
//        //        EUSART1_Buffer_Send();
//        ////        delay_10ms();
//        ////        delay_10ms();
//        ////        delay_10ms();
//        //        sprintf(UART_TX_TEXT, "m.duty=%d", duty);
//        //        EUSART1_Buffer_Send();
//        ////        delay_10ms();
//        ////        delay_10ms();
//        ////        delay_10ms();
//        //        sprintf(UART_TX_TEXT, "m.erreur=%d", erreur);
//        //        EUSART1_Buffer_Send();
//        //        sprintf(UART_TX_TEXT, "print('i={}\\tduty={}\\terreur={}'.format(m.I_Moteur_1, m.duty, m.erreur))");
//        //        EUSART1_Buffer_Send();
//        //        sprintf(UART_TX_TEXT, "'i={0:<10} duty={1:<10} erreur={2:<10}'.format(%d, %d, %d)", Image_Courant_Moteur_1, duty, erreur);
//        //        EUSART1_Buffer_Send();
//
//
//        //        delay_1s(); 
//        //        delay_1s(); 
//        //        delay_1s(); 
//        //        delay_1s(); 
//        ////////        
//        ////////        
//        ////////        delay_1s();
//        ////////        
//        ////////        
//        ////////            sprintf(UART_TX_TEXT, "m.bip(0.1)");
//        ////////                    //On transmet la réponse
//        ////////                    EUSART1_Buffer_Send();
//        ////////                  delay_1s();  
//        ////////        //          delay_1s();  
//        ////////        //          delay_1s();  
//        ////////        //          delay_1s();  
//        ////////        //          delay_1s();  
//        ////////        //    sprintf(UART_TX_TEXT, "print('Capteur 1Capot Pid out = %d')",PID_out);
//        ////////        sprintf(UART_TX_TEXT, "m.Nb_Pion=%d", 47);
//        ////////        //On transmet la réponse
//        ////////        EUSART1_Buffer_Send();
//        ////////        delay_1s();
//        //////////        if(RX1_full == 1){
//        //////////              sprintf(UART_TX_TEXT, "print(\"UART RX TEXT = %s\")", UART_RX_TEXT);
//        ////////////        On transmet la réponse
//        //////////        EUSART1_Buffer_Send();
//        //////////        }
//        ////////        //sprintf(UART_TX_TEXT, "print('m.Nb_Pion')");
//        ////////        sprintf(UART_TX_TEXT, "m.Nb_Pion");
//        ////////        //On transmet la réponse
//        ////////        EUSART1_Buffer_Send();
//        ////////        delay_1s();
//        ////////        if(RX1_full == 1){
//        ////////              //sprintf(UART_TX_TEXT, "print(\"UART RX TEXT = %s\")", UART_RX_TEXT);
//        ////////              sprintf(UART_TX_TEXT, "%s", UART_RX_TEXT);
//        //////////        On transmet la réponse
//        ////////        EUSART1_Buffer_Send();
//        ////////        }
//        //////////      
//        //////////        eusart1RxIndex = 0;
//        //////////        eusart1RxBuffer[eusart1RxIndex] = '\0';
//        ////////
//        ////////        delay_1s();
//        ////////        delay_1s();
//        //////////        delay_1s(); 
//        //////////        delay_1s();
//        //////////        delay_1s();
//        //////////        delay_1s();
//        //////////        delay_1s();
//        //////////        delay_1s();
//        //////////        delay_1s();
//        //////////        delay_1s();
//        ////////
//        ////////        
//
//
//    } while ((AV_1 == 1) | (AR_1 == 1)); //AV_1
//
//    TIMER2_Off();
//
//    PIE3bits.PTIE = 0;
//    PIE1bits.ADIE = 0;
//    LED = 0;
//    DRIVER_M1 = 0;
//    OVDCOND = 0b00000000;
//    STOP_M1;
//    //  LED = 0;
//}
//
//
////******************************************************************************
//// FONCTION  MOTEUR1 AV
////******************************************************************************
//
//void Moteur1(unsigned char direction, unsigned char consigne) {
//    //unsigned char i; //, i_min, i_max;
//    unsigned char i, i_min, i_max;
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
//
//
//    Init_ADC_Single_Shoot_I_Moteur_1();
//
//
//
//
//    index = 0;
//    TMR2 = 0;
//    TMR2IF = 0;
//
//
//    if (direction == AVANT) {
//        AV_M1;
//    } else {
//        AR_M1;
//    }
//    PDC0L = 1 << 2;
//    PDC0H = 0;
//    OVDCOND = 0b00000001;
//    DRIVER_M1 = 1;
//
//
//    erreur = 31;
//    erreur = 31;
//    erreur = 7;
//    erreur = 1;
//    PDC0L = ((unsigned char) erreur) << 2;
//    PDC0H = ((unsigned char) erreur) >> 6;
//
//
//    erreur_accumulator = 0;
//
//
//
//
//    Nouvelle_Valeur_ADC = 0; //Initialisation du drapeau de fin de conversion (nouvelle image du courant disponible)
//    direction = 0;
//    i_min = 31;
//    i_max = 0;
//    while (PTDIR == 1) NOP();
//    while (PTDIR == 0) NOP();
//
//
//    LED = 1;
//
//    PIE3bits.PTIE = 0;
//    PIE1bits.ADIE = 1;
//    PIE1bits.ADIE = 1;
//
//    PEIE = 1;
//    GIE = 1;
//    TIMER2_On(); //fréquence d'echantillonnage
//    ADIF = 0;
//    do {
//
//        //        sprintf(UART_TX_TEXT, "m.I_Moteur_1=%d", Image_Courant_Moteur_1);
//        //        EUSART1_Buffer_Send();
//        ////        delay_10ms();
//        ////        delay_10ms();
//        ////        delay_10ms();
//        //        sprintf(UART_TX_TEXT, "m.duty=%d", duty);
//        //        EUSART1_Buffer_Send();
//        ////        delay_10ms();
//        ////        delay_10ms();
//        ////        delay_10ms();
//        //        sprintf(UART_TX_TEXT, "m.erreur=%d", erreur);
//        //        EUSART1_Buffer_Send();
//        //        sprintf(UART_TX_TEXT, "print('i={}\\tduty={}\\terreur={}'.format(m.I_Moteur_1, m.duty, m.erreur))");
//        //        EUSART1_Buffer_Send();
//        //        sprintf(UART_TX_TEXT, "'i={0:<10} duty={1:<10} erreur={2:<10}'.format(%d, %d, %d)", Image_Courant_Moteur_1, duty, erreur);
//        //        EUSART1_Buffer_Send();
//
//
//        //        delay_1s(); 
//        //        delay_1s(); 
//        //        delay_1s(); 
//        //        delay_1s(); 
//        ////////        
//        ////////        
//        ////////        delay_1s();
//        ////////        
//        ////////        
//        ////////            sprintf(UART_TX_TEXT, "m.bip(0.1)");
//        ////////                    //On transmet la réponse
//        ////////                    EUSART1_Buffer_Send();
//        ////////                  delay_1s();  
//        ////////        //          delay_1s();  
//        ////////        //          delay_1s();  
//        ////////        //          delay_1s();  
//        ////////        //          delay_1s();  
//        ////////        //    sprintf(UART_TX_TEXT, "print('Capteur 1Capot Pid out = %d')",PID_out);
//        ////////        sprintf(UART_TX_TEXT, "m.Nb_Pion=%d", 47);
//        ////////        //On transmet la réponse
//        ////////        EUSART1_Buffer_Send();
//        ////////        delay_1s();
//        //////////        if(RX1_full == 1){
//        //////////              sprintf(UART_TX_TEXT, "print(\"UART RX TEXT = %s\")", UART_RX_TEXT);
//        ////////////        On transmet la réponse
//        //////////        EUSART1_Buffer_Send();
//        //////////        }
//        ////////        //sprintf(UART_TX_TEXT, "print('m.Nb_Pion')");
//        ////////        sprintf(UART_TX_TEXT, "m.Nb_Pion");
//        ////////        //On transmet la réponse
//        ////////        EUSART1_Buffer_Send();
//        ////////        delay_1s();
//        ////////        if(RX1_full == 1){
//        ////////              //sprintf(UART_TX_TEXT, "print(\"UART RX TEXT = %s\")", UART_RX_TEXT);
//        ////////              sprintf(UART_TX_TEXT, "%s", UART_RX_TEXT);
//        //////////        On transmet la réponse
//        ////////        EUSART1_Buffer_Send();
//        ////////        }
//        //////////      
//        //////////        eusart1RxIndex = 0;
//        //////////        eusart1RxBuffer[eusart1RxIndex] = '\0';
//        ////////
//        ////////        delay_1s();
//        ////////        delay_1s();
//        //////////        delay_1s(); 
//        //////////        delay_1s();
//        //////////        delay_1s();
//        //////////        delay_1s();
//        //////////        delay_1s();
//        //////////        delay_1s();
//        //////////        delay_1s();
//        //////////        delay_1s();
//        ////////
//        ////////        
//
//
//    } while ((AV_1 == 1) | (AR_1 == 1)); //AV_1
//
//    TIMER2_Off();
//
//    PIE3bits.PTIE = 0;
//    PIE1bits.ADIE = 0;
//    LED = 0;
//    DRIVER_M1 = 0;
//    OVDCOND = 0b00000000;
//    STOP_M1;
//    //  LED = 0;
//}
//



//******************************************************************************
// FONCTION  MOTEUR1 AV
//******************************************************************************

void Moteur(unsigned char moteur_indice, unsigned char direction, unsigned char consigne, unsigned char option) {
    //unsigned char i; //, i_min, i_max;
    unsigned char i, i_min, i_max;
    //    unsigned int erreur;
    //    //unsigned char erreur;
    //    unsigned int erreur_accumulator;

#define ACCUMULATOR_SHIFT 2
    //    unsigned int duty = 0;
    //    unsigned char duty;
    unsigned int index;


    u_Init_PWM();

    index = 0;
    TMR2 = 0;
    TMR2IF = 0;


    switch (moteur_indice) {

        case MOTEUR_1:

            Init_ADC_Single_Shoot_I_Moteur_1();


            if (direction == AVANT) {
                AV_M1;
                //Etat = ETAT_AVANCE;
                Etat_Update(ETAT_AVANCE);
            } else {
                AR_M1;
                //Etat = ETAT_RECULE;
                Etat_Update(ETAT_RECULE);
            }
            PDC0L = 1 << 2;
            PDC0H = 0;
            OVDCOND = 0b00000001;
            DRIVER_M1 = 1;


            erreur = 1;
            PDC0L = ((unsigned char) erreur) << 2;
            PDC0H = ((unsigned char) erreur) >> 6;


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
            PIE1bits.ADIE = 1;

            PEIE = 1;
            GIE = 1;
            TIMER2_On(); //fréquence d'echantillonnage
            ADIF = 0;




            if (direction == AVANT) {
                do {
//                    LED = 1;
//                    LED = 0;
                    /*delay_10ms();*
                     */
                    EUSART1_Check_Buffer();
                    //action_EUSART1_Check_Buffer();
                    NOP();
                } while (Etat == ETAT_AVANCE);
            } else {
                do {
//                    LED = 1;
//                    LED = 0;
                    EUSART1_Check_Buffer();
                    //action_EUSART1_Check_Buffer();
                    /*delay_10ms();*/
                    NOP();
                } while (Etat == ETAT_RECULE);
            }

            //            do {
            //
            //
            //            } while ((AV_1 == 1) | (AR_1 == 1)); //AV_1


            break;

        case MOTEUR_2:

            Init_ADC_Single_Shoot_I_Moteur_2();


            if (direction == AVANT) {
                AV_M2;
                //Etat = ETAT_PELLE_LEVE;
                Etat_Update(ETAT_PELLE_LEVE);
            } else {
                AR_M2;
                //Etat = ETAT_PELLE_BAISSE;
                Etat_Update(ETAT_PELLE_BAISSE);
            }
            PDC1L = 1 << 2;
            PDC1H = 0;
            OVDCOND = 0b00000100;
            DRIVER_M2 = 1;

            erreur = 1;
            PDC1L = ((unsigned char) erreur) << 2;
            PDC1H = ((unsigned char) erreur) >> 6;


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
            PIE1bits.ADIE = 1;

            PEIE = 1;
            GIE = 1;
            TIMER2_On(); //fréquence d'echantillonnage
            ADIF = 0;


            //            do {
            //
            //
            //            } while ((AV_2 == 1) | (AR_2 == 1)); //AV_1

            if (direction == AVANT) {
                do {
                    NOP();
                } while (Etat == ETAT_PELLE_LEVE);
            } else {
                do {
                    NOP();
                } while (Etat == ETAT_PELLE_BAISSE);
            }

            break;

        default:
            break;
    }

    
    
    PIE3bits.PTIE = 0;
    PIE1bits.ADIE = 0;


    Coupe_Moteur();
    
//    TIMER2_Off();
//
//    LED = 0;
//    DRIVER_M1 = 0;
//    DRIVER_M2 = 0;
//    OVDCOND = 0b00000000;
//    STOP_M1;
//    STOP_M2;
    //  LED = 0;

    //    DRIVER_M2 = 0;
    //    OVDCOND = 0b00000000;
    //    STOP_M1;
}


