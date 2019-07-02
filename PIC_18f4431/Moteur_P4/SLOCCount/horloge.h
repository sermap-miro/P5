/* 
 * File:   horloge.h
 * Author: sam
 *
 * Created on 17 janvier 2018, 17:08
 */

#ifndef HORLOGE_H
#define	HORLOGE_H

#ifdef	__cplusplus
extern "C" {
#endif

    void delay_ms(unsigned int ms);
    //Temporise de 10 µs
    void delay_10us(void); 
    //Temporise de 10 ms
    void delay_10ms(void);
    //Temporise de 100 ms
    void delay_100ms(void);
    //Temporise d'1 s
    void delay_1s(void);




#ifdef	__cplusplus
}
#endif

#endif	/* HORLOGE_H */

