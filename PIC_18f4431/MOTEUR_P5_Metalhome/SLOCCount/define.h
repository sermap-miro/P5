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

    
#define NB_ACTION_LOG 10
    
    
    
#define AVANT 1
#define ARRIERE 0
#define MONTE 1
#define DESCEND 0

    
  
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
#define ETAT_PELLE_LEVE 4
    //avance
#define ETAT_PELLE_BAISSE 5
    //Platine
#define ETAT_PLATINE 6
    
#define ETAT_BOOT 255
    //
    
    
  //Alarme
    
#define ALARME_NULLE 0
#define ALARME_I_MOTEUR_1 1
#define ALARME_I_MOTEUR_2 2
#define ALARME_PATINAGE 3
#define ALARME_CAPOT 4
#define ALARME_OVERLOAD_CAP_1_2 5
    
    
    
#define OPTION_NULLE 0
//#define OPTION_    
    
    
#define MOTEUR_1 1
#define MOTEUR_2 2
    
    
    
#define PARAMETER_CONSIGNE 0
#define PARAMETER_PATINAGE_S 1
#define PARAMETER_PION_100MS 2
#define PARAMETER_PLATINE_100MS 3
#define PARAMETER_PELLE_S 4
    
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

