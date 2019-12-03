//******************************************************************************
//  File:   Variables.h
//******************************************************************************

#ifndef VARIABLE_H
#define	VARIABLE_H



#define PROTO_1
//#undef PROTO_1
//#define PROTO_2
//#undef PROTO_2


#define DEBUG 1
//#undef DEBUG


//#define TEMPS_DEGAGEMENT 4




//#define INDICE_SIGMOIDE 15
//#define INDICE_SIGMOIDE 15
#define INDICE_SIGMOIDE 15

////Ok
#define PWM_SHIFT 3
//#define P_SHIFT 3//Normal
#define P_SHIFT 3
//#define I_SHIFT 5
//SHIFT de 8 à 9 on double le temps de gestion de l'interruption 
//#define I_SHIFT 8// Normal
#define I_SHIFT 11
#define PID_SHIFT 0
//P faible
//#define I_SHIFT 10

//#define PWM_SHIFT 2
//#define P_SHIFT 2
//#define I_SHIFT 2















#ifdef PROTO_1



//#define LED LATD6
#define LED LATC5
//#define B0 LATB0

#define DRIVER_M1 LATC0
#define DRIVER_M2 LATC1


//#define AV_1 0
//#define AR_1 0
//#define AV_2 1
//#define AR_2 0

#define AV_1 (PORTDbits.RD3)^1
#define AR_1 (PORTDbits.RD2)^1
#define AV_2 (PORTDbits.RD1)^1
#define AR_2 (PORTDbits.RD0)^1

#define AV_M1   LATD5 = 0;LATD4 = 1
#define AR_M1   LATD4 = 0;LATD5 = 1
#define STOP_M1 LATD4 = 0;LATD5 = 0


#define AV_M2   LATD7 = 0;LATD6 = 1
#define AR_M2   LATD6 = 0;LATD7 = 1
#define STOP_M2 LATD6 = 0;LATD7 = 0
     

#endif









#ifdef PROTO_2

#define PION PORTAbits.RA2
#define CAPOT PORTCbits.RC3
#define RELAIS LATEbits.RE2

//#define LED LATD6
#define LED LATC2
//#define B0 LATB0

#define DRIVER_M1 LATC0
#define DRIVER_M2 LATC1


//#define AV_1 0
//#define AR_1 0
//#define AV_2 1
//#define AR_2 0

#define AV_1 (PORTDbits.RD3)^1
#define AR_1 (PORTDbits.RD2)^1
#define AV_2 (PORTDbits.RD1)^1
#define AR_2 (PORTDbits.RD0)^1

#define AV_M1   LATD5 = 0;LATD4 = 1
#define AR_M1   LATD4 = 0;LATD5 = 1
#define STOP_M1 LATD4 = 0;LATD5 = 0


#define AV_M2   LATD7 = 0;LATD6 = 1
#define AR_M2   LATD6 = 0;LATD7 = 1
#define STOP_M2 LATD6 = 0;LATD7 = 0
     

#endif






#endif

//******************************************************************************

