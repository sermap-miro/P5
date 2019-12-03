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
    unsigned char Etat_Intitule(unsigned char Etat_Number);
    unsigned char Etat_Get(unsigned char Etat_Indice);
    unsigned char Etat_Precedent_Get(void);
    void Etat_Update(unsigned char etat_new_value);
    void Coupe_Moteur(void);


    void Init_Moteur_Pelle(void);
    void Stop_Moteur_Pelle(void);
    void Check_List_Moteur_Pelle(void);
//    void Moteur_Pelle(unsigned char direction, unsigned char option);

void Check_List_Moteur_Metalhome(void);
    void Check_List_Moteur_1(void);
    void Init_Moteur_1(void);
    void Stop_Moteur_1(void);

//    void Moteur(unsigned char moteur_indice, unsigned char direction, unsigned char consigne, unsigned char option);

    void Mouvement_X(unsigned char direction, unsigned char type_consigne, unsigned char option);
    void Mouvement_Z(unsigned char direction, unsigned char type_consigne, unsigned char option);
    void Mouvement_Bequille(unsigned char direction, unsigned char type_consigne, unsigned char option);
    
    void Mouvement_X_Metalhome(unsigned char direction);
#ifdef	__cplusplus
}
#endif

#endif	/* ACTION_H */

