/* 
 * File:   define.h
 * Author: sam
 *
 * Created on 19 janvier 2018, 15:52
 */

#ifndef DEFINE_H
#define	DEFINE_H

#ifdef	__cplusplus
extern "C" {
#endif

    
   #define TEMPS_ATTENTE_APRES_ALARME 2 
    
    
    
#define NB_ACTION_LOG 10
    
    
    
#define MARCHE_AVANT 1
#define MARCHE_ARRIERE 0
#define AVANT 1
#define ARRIERE 0
#define MONTE 1
#define DESCEND 0
#define SORT 1
#define RENTRE 0

  
#define ON 1
#define OFF 0
    
  
    //État du Mirobot

    //inactivité
#define ETAT_INACTIF 0

    //alarme
#define ETAT_ALARME 1
    
    
    
    //avance
#define ETAT_AVANCE 2
    //avance
#define ETAT_RECULE 3
    //avance
#define ETAT_PELLE_LEVE 5
    //avance
#define ETAT_PELLE_BAISSE 4
    //Platine
#define ETAT_PLATINE 6
    //BLOQUER
#define ETAT_BLOQUER 7
    
#define ETAT_RENTRE_BEQUILLE 8
#define ETAT_SORT_BEQUILLE 9
    
#define ETAT_BOOT 255
    //
    
    
  //Alarme
    
#define ALARME_NULLE 0
#define ALARME_I_MOTEUR_1 1
#define ALARME_I_MOTEUR_2 2
#define ALARME_PATINAGE 3
#define ALARME_CAPOT 4
#define ALARME_OVERLOAD_CAP_1_2 5
    
    
    
#define OPTION_NULLE 0x00
#define OPTION_TEMPS 0x01
#define OPTION_MARCHE_FORCER 0x02
//#define OPTION_ 0x04
//#define OPTION_ 0x08
    
#define OPTION_TEMPS_1_s 0x10
#define OPTION_TEMPS_2_s 0x20
#define OPTION_TEMPS_3_s 0x30
#define OPTION_TEMPS_4_s 0x40
#define OPTION_TEMPS_5_s 0x50
#define OPTION_TEMPS_6_s 0x60
#define OPTION_TEMPS_7_s 0x70
#define OPTION_TEMPS_8_s 0x80
    
    
    
#define MOTEUR_1 1
#define MOTEUR_2 2
#define MOTEUR_PELLE 2
#define MOTEUR_BEQUILLE 3
    
    
    
#define PARAMETER_CONSIGNE 0
#define PARAMETER_PATINAGE_S 1
#define PARAMETER_PION_100MS 2
#define PARAMETER_PLATINE_100MS 3
#define PARAMETER_PELLE_S 4
#define PARAMETER_CAPOT_NB_ESSAI 5
#define PARAMETER_PATINAGE_NB_ESSAI 6
    
    
    
#define VIEW_CONSIGNE 0
#define VIEW_DEBUG 1
    
    
    
#define INDICE_IRQ_CAPOT 0
#define INDICE_IRQ_I_MOTEUR_1 1
#define INDICE_IRQ_I_MOTEUR_2 2
#define INDICE_IRQ_PION_RISING_EDGE 3
#define INDICE_IRQ_PION_FALLING_EDGE 4
#define INDICE_IRQ_TIMER_0 5
#define INDICE_IRQ_TIMER_2 6
#define INDICE_IRQ_TIMER_5 7
#define INDICE_IRQ_ADC 8
#define INDICE_IRQ_PWM 9
    
    
    

    
    
    
//    //continu sa tache
//#define ETAT_OK 1
//    //arret urgence
//#define ETAT_AU 2
//    //attente instruction
//#define ETAT_AI 3
//    //panne
//#define ETAT_FILO_ABSENT 4
//    //panne
//
//    //en marche avant
//#define ETAT_FILO_AVANT 5
//    //en marche arrière
//#define ETAT_FILO_ARRIERE 6
//
//
//#define ETAT_PATINAGE 7   
//    //Verin 1
//    //#define ETAT_VERIN1 7
//#define ETAT_VERIN1_UP 8
//#define ETAT_VERIN1_DOWN 9
//    //Verin 2
//#define ETAT_VERIN2 10
//#define ETAT_VERIN2_UP 11
//#define ETAT_VERIN2_DOWN 12
//#define ETAT_SECU 13
//#define ETAT_PLATINE 14
//#define ETAT_DEMMARAGE 15

  
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

#ifdef	__cplusplus
}
#endif

#endif	/* DEFINE_H */

