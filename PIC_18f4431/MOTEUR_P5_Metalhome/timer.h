/* 
 * File:   timer.h
 * Author: sam
 *
 * Created on January 15, 2018, 4:50 PM
 */

#ifndef TIMER_H
#define	TIMER_H

#ifdef	__cplusplus
extern "C" {
#endif

void Init_TIMER0(void);
void TIMER0_On(void);
void TIMER0_Off(void);
void Init_TIMER2(void);
void TIMER2_On(void);
void TIMER2_Off(void);
void Init_TIMER5(void);
void TIMER5_On(void);
void TIMER5_Off(void);

#ifdef	__cplusplus
}
#endif

#endif	/* TIMER_H */

