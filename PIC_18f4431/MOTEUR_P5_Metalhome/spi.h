/* 
 * File:   spi.h
 * Author: sam
 *
 * Created on 18 septembre 2018, 14:20
 */

#ifndef SPI_H
#define	SPI_H

#ifdef	__cplusplus
extern "C" {
#endif

void Init_SPI(void);
void SPI_ISR(void);
void SPI_Check_Buffer(void);

#ifdef	__cplusplus
}
#endif

#endif	/* SPI_H */

