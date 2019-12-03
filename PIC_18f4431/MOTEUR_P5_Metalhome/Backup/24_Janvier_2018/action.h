/* 
 * File:   action.h
 * Author: sam
 *
 * Created on January 15, 2018, 3:52 PM
 */

#ifndef ACTION_H
#define	ACTION_H

#ifdef	__cplusplus
extern "C" {
#endif
    
void Etat_Update(unsigned char etat_new_value);
void Coupe_Moteur(void);

//
////void action_EUSART1_Check_Buffer(void);
//
//
////void Moteur1_AV(int consigne);
////void u_Moteur1_AV(unsigned char consigne);
////void Moteur1_AR(int consigne);
//void Moteur2_AV(int consigne);
//void Moteur2_AR(int consigne);
//
//
//
//
//void Moteur1(unsigned char direction, unsigned char consigne);

void Moteur(unsigned char moteur_indice, unsigned char direction, unsigned char consigne, unsigned char option);
//void uMoteur(unsigned char moteur_indice, unsigned char direction, unsigned char consigne, unsigned char option);


#ifdef	__cplusplus
}
#endif

#endif	/* ACTION_H */

