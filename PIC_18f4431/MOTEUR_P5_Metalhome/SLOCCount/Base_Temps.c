//******************************************************************************
// GESTION BASE TEMPS
//******************************************************************************

    #include <xc.h>
    #include <stdbool.h>
    #include "Base_Temps.h"
    #include "Variables.h"
 
//******************************************************************************
//  TIMER 0 UTILISE POUR MEMOIRE
//******************************************************************************

//******************************************************************************
//	FONCTION INIT TIMER 1 
//******************************************************************************

// BASE DE TEMPS 0.2US

void Init_Timer1(void)
{
	T1CON = 0b10010001; // ok
}
//******************************************************************************
//	FONCTION INIT TIMER 2 
//******************************************************************************

// BASE DE TEMPS POUR FILTRE NUMERIQUE
// BASE 5ms 2* fmax
void Init_Timer2(void)
{   
    T2CON = 0b00100101; // ok 5ms
    //T2CON = 0b00011101; // ok 4ms 
	PR2 = 250;
}
//******************************************************************************
//	FONCTION INIT TIMER 3 
//******************************************************************************

void Init_Timer3(void)
{
	T3CON = 0b10000101;
}
//******************************************************************************
//	FONCTION INIT TIMER 4 BASE DE TEMPS 10 ms 
//******************************************************************************

void Init_Timer4(void)
{
	T4CON = 0b00000101;
	PR4 = 250;  
}
//******************************************************************************
//	FONCTION Delay_Ms 
//******************************************************************************

void Delay_Ms(long Ms)
{
	while(Ms > 0)
	{
		TMR4 = 0;
		TMR4IF = 0;
		while(TMR4IF == 0);
		Ms = Ms - 1;
	}
}
//******************************************************************************
//	FONCTION Delay_Ms 
//******************************************************************************

void Delay_Ms_Stop_Rep(long Ms)
{
	while(Ms > 0)
	{
		TMR4 = 0;
		TMR4IF = 0;
		while(TMR4IF == 0);
        Ms = Ms - 1;
        if( (TEL == 1)||(BP_1 == 1)||(BP_2 == 1)||(BP_3 == 1) ) break;
        if( REPRISE == 1) 
        {
            if( temp1_5ms >= duree_reprise ) REPRISE = 0;
        }
	}
}
//******************************************************************************

