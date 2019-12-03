
 /*
 * File:   horloge.c
 * Author: sam
 *
 * Created on 12 juillet 2016, 17:08
 */


#include <xc.h>


#define _XTAL_FREQ 8000000 //The speed of your internal(or)external oscillator
//Mesure pour une fréquence de clock à 8 MHz (18f87K22)
//1 = 13.5 us
//10 = 49.4 us
//100 = 410 us
//1000 = 4.04 ms
//5000 = 20.1 ms
void delay_ms(unsigned int ms){
    unsigned int i;
    for (i=0;i<ms;i++){__delay_ms(1);}
}



//Temporisation de 10 µs

void delay_10us(void) {
    __delay_us(10);
}

//Temporisation de 10 ms

void delay_10ms(void) {
    __delay_ms(10);
}



//Temporisation de 100 ms

void delay_100ms(void) {
    __delay_ms(10);
    __delay_ms(10);
    __delay_ms(10);
    __delay_ms(10);
    __delay_ms(10);
    __delay_ms(10);
    __delay_ms(10);
    __delay_ms(10);
    __delay_ms(10);
    __delay_ms(10);
}



//Temporisation d'1 s

void delay_1s(void) {
    delay_100ms();
    delay_100ms();
    delay_100ms();
    delay_100ms();
    delay_100ms();
    delay_100ms();
    delay_100ms();
    delay_100ms();
    delay_100ms();
    delay_100ms();
}


