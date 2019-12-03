/* 
 * File:   adc.h
 * Author: sam
 *
 * Created on January 15, 2018, 3:36 PM
 */

#ifndef ADC_H
#define	ADC_H

#ifdef	__cplusplus
extern "C" {
#endif

void Init_ADC(void);
void Init_ADC_PWM_Trig(void);
void Init_ADC_PWM(void);
//void Init_ADC_Single_Shoot(void);
void Init_ADC_Single_Shoot_I_Moteur_1(void);
void Init_ADC_Single_Shoot_I_Moteur_2(void);
 int lecture_I_Mot1(void);
 void u_lecture_I_Mot1_init(void);
 unsigned char u_lecture_I_Mot1(void);
 int lecture_I_Mot2(void);
 

#ifdef	__cplusplus
}
#endif

#endif	/* ADC_H */

