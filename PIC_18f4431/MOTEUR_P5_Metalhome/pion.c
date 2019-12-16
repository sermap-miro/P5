


#include <xc.h>

#include "variable_extern.h"
#include "Variables.h"

#include "pion.h"

#include "interrupt.h"

void Detection_Pion_Init(void) {

    if (PION == METAL_PRESENT) {
        Surveillance_Capteur_Pion = METAL_PRESENT;
        Mouvement_Startup = 1;
    } else {
        Surveillance_Capteur_Pion = METAL_ABSENT;
        Mouvement_Startup = 0;

    }

}


//Gestion du capteur Pion 

void Detection_Pion_On(void) {

    // // Front Montant  CAP1
    //    // CAPxREN: Time Base Reset Enable bit
    //    CAP1CONbits.CAP1REN = 0;    // 0 = Disable selected time base Reset on capture
    //                                // 1 = Enabled
    //    
    //    // CAPxM<3:0>: Input Capture x (ICx) Mode Select bits
    //    CAP1CONbits.CAP1M = 0b1111; // 1111 = Special Event Trigger mode; the trigger occurs on every rising edge on CAP1 input
    //
    //    
    //// Front Descendant  CAP2
    //    // CAPxREN: Time Base Reset Enable bit
    //    CAP2CONbits.CAP2REN = 1;    // 0 = Disable selected time base Reset on capture
    //                                // 1 = Enabled
    //    
    //    // CAPxM<3:0>: Input Capture x (ICx) Mode Select bits
    //    CAP2CONbits.CAP2M = 0b1110; // 1000 = Capture on every CAPx input state change
    //    CAP2CONbits.CAP2M = 0b0000; // 1000 = Capture on every CAPx input state change




#ifdef PROTO_2   

    //PIR3bits.IC2QEIF = 0;
    //PIE3bits.IC2QEIE = 1;
    //PIR3bits.IC2QEIF = 0;

    
    
    PIR3bits.IC1IF = 0;
    PIE3bits.IC1IE = 1; //  0 = IC1 interrupt disabled
    PIR3bits.IC1IF = 0;

    Detecteur_Pion = SURVEILLANCE_ACTIVER;

    
    
    if (Option_Pailleux != 1) {

//    PIR3bits.IC1IF = 0;
//    PIE3bits.IC1IE = 1; //  0 = IC1 interrupt disabled
//    PIR3bits.IC1IF = 0;
//
//    Detecteur_Pion = SURVEILLANCE_ACTIVER;

        if (PION == METAL_PRESENT) {//Si lors du démarrage du moteur
            //le capteur PION est activé, alors on défini le temps d'une platine comme
            //étant le double de celui d'origine
            //pour ne pas prendre une fausse platine, par
//Modif du 18 Avril
//////            nb_100ms_platine = 2 * NB_100MS_PLATINE; //*2
//////            
//////            nb_100ms_platine = NB_100MS_PLATINE << 2; //*4
//////            
//////            
//            nb_100ms_platine = NB_100MS_PLATINE << 3; //*8

//nb_100ms_platine = 8 * nb_100ms_platine_backup;

                    if (nb_100ms_platine_backup>=32){
                      nb_100ms_platine = 255;  
                    }else{
                    nb_100ms_platine = (unsigned char) (NB_PLATINE_POUR_FAUX_DEPART * nb_100ms_platine_backup);
                    }


            //TIMER5_On();//Et on démarre
            IRQ_PION_Metal_Apparait(); //On simule un front de détection du métal
            //IRQ_PION_FALLING_EDGE();//On simule un front de détection du métal
            
            
        }
    }

    //                else{
    //            
    //            
    //                }



#else

    PIE3bits.IC1IE = 1; //  1 = IC1 interrupt enabled
    PIR3bits.IC1IF = 0;
#endif







}

void Detection_Pion_Off(void) {

//
//#ifdef PROTO_2   
//    PIE3bits.IC2QEIE = 0;
//    PIR3bits.IC2QEIF = 0;
//#else
//
//
//    PIE3bits.IC1IE = 0; //  1 = IC1 interrupt enabled
//    PIR3bits.IC1IF = 0;
//#endif

    
    
    Detecteur_Pion = SURVEILLANCE_DESACTIVER;
    
    PIE3bits.IC1IE = 0; //  1 = IC1 interrupt enabled
    PIR3bits.IC1IF = 0;
    
    
    


}

