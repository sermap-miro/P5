/* 
 * File:   interrupt.h
 * Author: sam
 *
 * Created on January 15, 2018, 3:37 PM
 */

#ifndef INTERRUPT_H
#define	INTERRUPT_H

#ifdef	__cplusplus
extern "C" {
#endif


    void IRQ_Execution(unsigned char IRQ_Indice);
    void Init_IT(void);
    void Init_Input_Capture_0(void);


    void Capteur_Capot_On(void);
    void Capteur_Capot_Off(void);

    void IRQ_PION_RISING_EDGE(void);
    void IRQ_PION_FALLING_EDGE(void);
    void IRQ_TIMER_0(void);
    void IRQ_TIMER_5(void);
    void IRQ_PWM(void);
    void IRQ_ADC(void);

    void interrupt low_priority LOW_PRIORITY_IRQ(void);

    void IRQ_TIMER2(void);
    void IRQ_CAPOT(void);
    void IRQ_I_MOTEUR_1(void);
    void IRQ_I_MOTEUR_2(void);

    void interrupt high_priority HIGH_PRIORITY_IRQ(void);


#ifdef	__cplusplus
}
#endif

#endif	/* INTERRUPT_H */

