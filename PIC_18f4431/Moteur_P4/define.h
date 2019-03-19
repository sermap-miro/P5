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

#define P4_BUSY_OCCUPER 1
#define P4_BUSY_LIBRE 0
    
   #define TEMPS_ATTENTE_ALARME 1 
   //#define TEMPS_ATTENTE_APRES_ALARME 2 
//Modif du 17 Avril
   #define TEMPS_ATTENTE_APRES_ALARME 3 
    
#define NB_100MS_PION 2
//#define NB_100MS_PLATINE 30
    //Montechroux 18 Juin 2018
//#define NB_100MS_PLATINE 22
    //19 Juin 2018
#define NB_100MS_PLATINE 30
    
#define NB_S_PELLE 30
#define NB_S_BEQUILLE 10
    
    
#define CONSIGNE_MAX 20 * 5
#define CONSIGNE_MAX_X 20 * 5
//#define CONSIGNE_MAX_Z 4 * 5
#define CONSIGNE_MAX_Z 20 * 5
#define CONSIGNE_MAX_BEQUILLE 20 * 5
    
    //Unité CAN
#define MOTEUR_I_MAX 100
//#define PELLE_I_MAX 22
#define PELLE_I_MAX 45
#define BEQUILLE_I_MAX 22
    
    
#define NB_ACTION_LOG 10
   
#define DVT_TABLEAU_TAILLE 6 
    
    
#define NB_PLATINE_POUR_FAUX_DEPART 8
    
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
  
#define SURVEILLANCE_DESACTIVER 0
#define SURVEILLANCE_ACTIVER 1
    

  
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
#define ETAT_PAILLEUX 10
#define ETAT_DVT 11
#define ETAT_MULTITAS 12
#define ETAT_BLOQUER_IMPOSSIBLE 70
#define ETAT_BLOQUER_DEFINITIVEMENT 77
    
#define ETAT_BOOT 255
    //
    
    
  //Alarme
    
#define ALARME_NULLE 0
#define ALARME_I_MOTEUR_1 1
#define ALARME_I_MOTEUR_2 2
#define ALARME_PATINAGE 3
#define ALARME_CAPOT 4
    //Alarme qui ne devrait en théorie que rarement apparaitre
#define ALARME_OVERLOAD_CAP_1_2 5
#define ALARME_START 6
#define ALARME_AU 7
#define ALARME_BATTERIE_FAIBLE 8
#define ALARME_OVERLOAD_CAP_1_1 9
#define ALARME_OVERLOAD_CAP_1_3 10
//Ajout d'un <E9>tat d'alamrme avec la fumi<E8>re pleine
#define ALARME_FUMIERE_PLEINE 11
  
    
    
#define OPTION_NULLE 0x00
#define OPTION_TEMPS 0x01
#define OPTION_MARCHE_FORCER 0x02
//#define OPTION_DVT 0x04
#define OPTION_TRIPLE 0x04
#define OPTION_MULTITAS 0x08
    
    
#define OPTION_TEMPS_1_s 0x10
#define OPTION_TEMPS_2_s 0x20
#define OPTION_TEMPS_3_s 0x30
#define OPTION_TEMPS_4_s 0x40
#define OPTION_TEMPS_5_s 0x50
#define OPTION_TEMPS_6_s 0x60
#define OPTION_TEMPS_7_s 0x70
#define OPTION_TEMPS_8_s 0x80
    
    // Modif du 17 Avril
#define OPTION_TEMPS_ALARME_CAPOT OPTION_TEMPS_6_s
#define OPTION_TEMPS_ALARME_PATINAGE OPTION_TEMPS_6_s
    
    
#define OPTION_CODE_MOTEUR_1_MULTITAS 1
#define OPTION_CODE_MOTEUR_1_PAILLEUX 2
    
    
    
   #define MOTEUR_1_TYPE_PLATINE 0
   #define MOTEUR_1_TYPE_TEMPS 1
    
    
    
    
#define MOTEUR_1 1
#define MOTEUR_2 2
#define MOTEUR_PELLE 2
#define MOTEUR_BEQUILLE 3
    
    
    
#define LIMIT_MAX_MOTEUR_X 1
#define LIMIT_MAX_MOTEUR_Z 2
#define LIMIT_MAX_MOTEUR_BEQUILLE 3
    
    
#define PARAMETER_CONSIGNE 0
#define PARAMETER_PATINAGE_S 1
#define PARAMETER_PION_100MS 2
#define PARAMETER_PLATINE_100MS 3
#define PARAMETER_PELLE_S 4
#define PARAMETER_CAPOT_NB_ESSAI 5
#define PARAMETER_PATINAGE_NB_ESSAI 6
#define PARAMETER_CONSIGNE_MAX_X 7
#define PARAMETER_CONSIGNE_MAX_Z 8
#define PARAMETER_CONSIGNE_MAX_BEQUILLE 9
//#define PARAMETER_PELLE_I_MAX 8
//#define PARAMETER_BEQUILLE_I_MAX 9
    
    
    
#define VIEW_CONSIGNE 0
#define VIEW_DEBUG 1
#define VIEW_ECHO 9
    
    
    
#define INDICE_IRQ_CAPOT 0
#define INDICE_IRQ_I_MOTEUR_1 1
#define INDICE_IRQ_I_MOTEUR_2 2
#define INDICE_IRQ_METAL_APPARAIT 3
#define INDICE_IRQ_METAL_DISPARAIT 4
#define INDICE_IRQ_TIMER_0 5
#define INDICE_IRQ_TIMER_2 6
#define INDICE_IRQ_TIMER_5 7
#define INDICE_IRQ_ADC 8
#define INDICE_IRQ_PWM 9
    
    
#define TYPE_MOUVEMENT_PION 0
#define TYPE_MOUVEMENT_TEMPS 1

    
    
    
#define METAL_PRESENT 0
#define METAL_ABSENT 1
    
    
#define CAPOT_EN_DEFAUT 0
#define CAPOT_EN_PLACE 1    
    
    
#define BUZZER_ON (unsigned char) 1
#define BUZZER_OFF (unsigned char) 0
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

  
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
#define EUSART1_TX_BUFFER_SIZE 64
#define EUSART1_RX_BUFFER_SIZE 64
#define SPI_TX_BUFFER_SIZE 64
#define SPI_RX_BUFFER_SIZE 64
    
#define SPI_MODE_LECTURE 0
#define SPI_MODE_ECRITURE 1
    
//#define EUSART1_TX_BUFFER_SIZE 72
//#define EUSART1_RX_BUFFER_SIZE 72
    
//#define EUSART1_TX_BUFFER_SIZE 96
//#define EUSART1_RX_BUFFER_SIZE 96

//#define EUSART1_TX_BUFFER_SIZE 128
//#define EUSART1_RX_BUFFER_SIZE 128
    
    
    

#ifdef	__cplusplus
}
#endif

#endif	/* DEFINE_H */

