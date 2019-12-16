#include <xc.h>
//#include "eusart1.h"
#include <string.h> 
#include <stdio.h> 
//#include "define_mot.h"
//#include "relais.h"
//#include "lora.h"
//#include "eusart2.h"
//pour la fonction atoi()
#include <stdlib.h>

#include "variable_extern.h"
#include "Variables.h"

#include "horloge.h"

#include "eusart.h"
#include "spi.h"

#include "action.h"
#include "interrupt.h"
#include "alarme.h"

void Init_SPI(void) {



    TRISDbits.TRISD3 = 1; //CLK
    TRISDbits.TRISD2 = 1; //MOSI - DI
    TRISDbits.TRISD1 = 0; //MISO - DO



    //SSPSTAT: SYNCHRONOUS SERIAL PORT STATUS REGISTER   
    /*
     bit 7 SMP: Sample bit
 SPI Master mode:
 1 = Input data sampled at end of data output time
 0 = Input data sampled at middle of data output time
 SPI Slave mode:
 SMP must be cleared when SPI is used in Slave mode.
 bit 6 CKE: SPI Clock Edge Select bit (Figure 19-2, Figure 19-3 and Figure 19-4)
 SPI mode, CKP = 0:
 1 = Data transmitted on rising edge of SCK
 0 = Data transmitted on falling edge of SCK
 SPI mode, CKP = 1:
 1 = Data transmitted on falling edge of SCK
 0 = Data transmitted on rising edge of SCK
 I 2 CTM mode:
 This bit must be maintained clear.
 bit 5 D/A: Data/Address bit (I 2 C mode only)
 1 = Indicates that the last byte received or transmitted was data
 0 = Indicates that the last byte received or transmitted was address
 bit 4 P: Stop bit (I 2 C mode only)
 This bit is cleared when the SSP module is disabled or when the Start bit is detected last; SSPEN is
 cleared.
 1 = Indicates that a Stop bit has been detected last (this bit is ?0? on Reset)
 0 = Stop bit was not detected last
 bit 3 S: Start bit (I 2 C mode only)
 This bit is cleared when the SSP module is disabled or when the Stop bit is detected last; SSPEN is
 cleared.
 1 = Indicates that a Start bit has been detected last (this bit is ?0? on Reset)
 0 = Start bit was not detected last
 bit 2 R/W: Read/Write Information bit (I 2 C mode only)
 This bit holds the R/W bit information following the last address match. This bit is only valid from the
 address match to the next Start bit, Stop bit or ACK bit.
 1 = Read
 0 = Write
 bit 1 UA: Update Address bit (10-Bit I 2 C mode only)
 1 = Indicates that the user needs to update the address in the SSPADD register
 0 = Address does not need to be updated
 bit 0 BF: Buffer Full Status bit
 Receive (SPI and I 2 C modes):
 1 = Receive complete, SSPBUF is full
 0 = Receive not complete, SSPBUF is empty
 Transmit (I 2 C mode only):
 1 = Transmit in progress, SSPBUF is full
 0 = Transmit complete, SSPBUF is empty
     */

    SSPSTATbits.SMP = 0; // Mode Esclave
    SSPSTATbits.CKE = 0;
    SSPSTATbits.CKE = 1; //Semble marché
    //SSPSTATbits.D_NOT_A = 0;



    //   SSPCON: SYNCHRONOUS SERIAL PORT CONTROL REGISTER

    /*
bit 7    WCOL: Write Collision Detect bit
1 = The SSPBUF register is written while it is still transmitting the previous word (must be cleared in
software)
0 = No collision
bit 6  SSPOV: Receive Overflow Indicator bit (1)
In SPI mode:
1 = A new byte is received while the SSPBUF register is still holding the previous data. In case
of overflow, the data in SSPSR is lost. Overflow can only occur in Slave mode. The user
must read the SSPBUF, even if only transmitting data, to avoid setting overflow. In
Master mode, the overflow bit is not set since each new reception (and transmission) is
initiated by writing to the SSPBUF register.
0 = No overflow
In I 2 CTM mode:
1 = A byte is received while the SSPBUF register is still holding the previous byte. SSPOV
is a ?don?t care? in Transmit mode. SSPOV must be cleared in software in either mode.
0 = No overflow
bit 5 SSPEN: Synchronous Serial Port Enable bit (2)
In SPI mode:
1 = Enables serial port and configures SCK, SDO and SDI as serial port pins
0 = Disables serial port and configures these pins as I/O port pins
In I 2 C mode:
1 = Enables the serial port and configures the SDA and SCL pins as serial port pins
0 = Disables serial port and configures these pins as I/O port pins
In both modes, when enabled, these pins must be properly configured as input or output.
bit 4 CKP: Clock Polarity Select bit
In SPI mode:
1 = Idle state for clock is a high level
0 = Idle state for clock is a low level
In I 2 C mode:
SCK release control.
1 = Enables clock
0 = Holds clock low (clock stretch). (Used to ensure data setup time.)
        
Note 1:
2:
3:
In Master mode, the overflow bit is not set since each new reception (and transmission) is initiated by
writing to the SSPBUF register.
When enabled, these pins must be properly configured as inputs or outputs.
Bit combinations not specifically listed here are either reserved or implemented in I 2 CTM mode only.
    
 bit 3-0   SSPM<3:0>: Synchronous Serial Port Mode Select bits (3)
0000 = SPI Master mode, Clock = F OSC /4
0001 = SPI Master mode, Clock = F OSC /16
0010 = SPI Master mode, Clock = F OSC /64
0011 = SPI Master mode, Clock = TMR2 output/2
0100 = SPI Slave mode, Clock = SCK pin, SS pin control enabled
0101 = SPI Slave mode, Clock = SCK pin, SS pin control disabled, SS can be used as I/O pin
0110 = I 2 C Slave mode, 7-bit address
0111 = I 2 C Slave mode, 10-bit address
1011 = I 2 C Firmware Controlled Master mode (slave Idle)
1110 = I 2 C Slave mode, 7-bit address with Start and Stop bit interrupts enabled
1111 = I 2 C Slave mode, 10-bit address with Start and Stop bit interrupts enabled

Note 1:
2:
3:
In Master mode, the overflow bit is not set since each new reception (and transmission) is initiated by
writing to the SSPBUF register.
When enabled, these pins must be properly configured as inputs or outputs.
Bit combinations not specifically listed here are either reserved or implemented in I 2 CTM mode only.
     */

    SSPCONbits.WCOL = 0; // Pas de collision détecté
    SSPCONbits.SSPOV = 0; // Pas de débordement du buffer de réception
    SSPCONbits.SSPEN = 1; // Active les broche SCK SDO et SDI comme broches pour le SPI
    SSPCONbits.CKP = 1; //1 = Idle state for clock is a high level
    SSPCONbits.CKP = 0; //0 = Idle state for clock is a low level
    SSPCONbits.SSPM = 0b0101; //0101 = SPI Slave mode, Clock = SCK pin, SS pin control disabled, SS can be used as I/O pin



    PIR1bits.SSPIF = 0; // Flash du SPI
    PIE1bits.SSPIE = 1; // Activation de l'interruption


}

void SPI_ISR(void) {

    unsigned char i;
    
    //LED ^= 1;

    PIR1bits.SSPIF = 0; // Flash du SPI
    
    
    i = (unsigned char) SSPBUF; // Lecture du caractère recu par SPI
    
    switch(SPI_MODE){
        
        
        case SPI_MODE_ECRITURE:
            
            
//                    spiTxIndex++;
//
//    if (spiTxBuffer[spiTxIndex] != '\0') {
//        SSPBUF = spiTxBuffer[spiTxIndex];
//    } else {
//        SPI_MODE = SPI_MODE_LECTURE;//il n'y a plus de caractère à transmettre
//    }

            
            
            if (i!=0x0D){
              spiTxIndex++;

    if (spiTxBuffer[spiTxIndex] != '\0') {
        SSPBUF = spiTxBuffer[spiTxIndex];
    } else {
        SPI_MODE = SPI_MODE_LECTURE;//il n'y a plus de caractère à transmettre
    }

            }else{
                SPI_MODE = SPI_MODE_LECTURE;
            }
            
            
            
            
            
            
            break;
            
        case SPI_MODE_LECTURE:
    
    
 //   i = (unsigned char) SSPBUF; // Lecture du caractère recu par SPI
    spiRxBuffer[spiRxIndex] = i;

    if ((spiRxBuffer[spiRxIndex] == 0x0d) | (spiRxBuffer[spiRxIndex] == 0x00)) {
        if (spiRxIndex != 0) {
            for (i = 0; i < spiRxIndex; i++) {
                SPI_RX_TEXT[i] = spiRxBuffer[i];
            }
            SPI_full = 1;
        }
        SPI_RX_TEXT[spiRxIndex] = '\0';
        spiRxIndex = 0;
    } else {
        switch (SPI_full) {
            case 0:
                if (spiRxIndex + 1 == SPI_RX_BUFFER_SIZE) {//Si le buffer est plein alors on le vide (ne devrais jamais se produire)
                    SPI_RX_TEXT[0] = '\0';
                    spiRxIndex = 0;
                    //LED=1;//Erreur
                    //EUSART1_Erreur_Get();
                } else {
                    spiRxIndex++;
                }
                break;
            case 1:
                //LED=1;//Erreur
                //EUSART1_Erreur_Get();
                break;
            default:
                break;
        }
    }
    break;
        default: break;}




    //    if(SSPSTATbits.BF)
    //    SSPBUF = (unsigned char) (i + 1);
    //  else
    //    
    //    
    //  SSPBUF = 0x50;

}

void cf_EUSART1_Receive_ISR(void) {
    //    LATB3^=1;
    //LED=1;
    unsigned char i;

    PIR1bits.RC1IF = 0;
    // SORTIE_1 ^= 1; //Pour débug IHM
    if (1 == RCSTA1bits.OERR) {
        // EUSART1 error - restart
        RCSTA1bits.SPEN = 0;
        RCSTA1bits.SPEN = 1;
        RCSTA1bits.CREN = 0;
        RCSTA1bits.CREN = 1;
    }
    //LED=1;
    // buffer overruns are ignored

    eusart1RxBuffer[eusart1RxIndex] = RCREG1;

    // if (eusart1RxBuffer[eusart1RxIndex] == 0x0d) {

    if ((eusart1RxBuffer[eusart1RxIndex] == 0x0d) | (eusart1RxBuffer[eusart1RxIndex] == 0x00)) {

        if (eusart1RxIndex != 0) {
            for (i = 0; i < eusart1RxIndex; i++) {
                UART_RX_TEXT[i] = eusart1RxBuffer[i];
            }
            RX1_full = 1;
        }


        UART_RX_TEXT[eusart1RxIndex] = '\0';
        eusart1RxIndex = 0;

    } else {
        switch (RX1_full) {
            case 0:
                if (eusart1RxIndex + 1 == EUSART1_RX_BUFFER_SIZE) {//Si le buffer est plein alors on le vide (ne devrais jamais se produire)
                    UART_RX_TEXT[0] = '\0';
                    eusart1RxIndex = 0;
                    //LED=1;//Erreur
                    EUSART1_Erreur_Get();
                } else {
                    eusart1RxIndex++;
                }
                break;


            case 1:
                //LED=1;//Erreur
                EUSART1_Erreur_Get();
                break;

            default:

                break;





        }




    }


}







//void spiWrite(char dat) //Write data to SPI bus
//{
//    SSPBUF = dat;
//}

void SPI_Check_Buffer(void) {
//////
//////    //    
//////    //    if(SSPSTATbits.BF){
//////    //    SSPBUF = 0x50;}
//////    //    else{
//////    //        
//////    //        if (eusart1RxIndex == 0){
//////    //            SSPBUF = eusart1RxBuffer[eusart1RxIndex];
//////    //            
//////    //        }else{
//////    //            SSPBUF = eusart1RxBuffer[eusart1RxIndex-1];
//////    //            
//////    //        }
//////    //        
//////    //        
//////    //    }
//////    //    
//////    //       if (eusart1RxIndex > 0){
//////    ////            SSPBUF = eusart1RxBuffer[eusart1RxIndex];
//////    ////            
//////    ////        }else{
//////    //            SSPBUF = eusart1RxBuffer[eusart1RxIndex-1];
//////    //            
//////    //        }
//////
//////    if (spiRxIndex > 0) {
//////
//////        if (spiRxBuffer[spiRxIndex - 1] == 0x54) {// "T"
//////            if (spiRxIndex >= 2) {
//////                //SSPBUF = 0x39;
//////                SSPBUF = spiRxBuffer[spiRxIndex - 2];
//////            } else {
//////                SSPBUF = 0x39;
//////            }
//////            spiRxIndex = 0;
//////        }
//////    }
//////    //    eusart1RxBuffer[eusart1RxIndex]
//////
//////
//////
//////    //  else
//////    //    
//////    //    
//////    //  SSPBUF = 0x50;
//////

    if (SPI_full == 1) {//Le Wipy à parler

        //LED=1;
        EUSART1_RX_T3_LOCAL(SPI_RX_TEXT[0],
                SPI_RX_TEXT[1],
                SPI_RX_TEXT[2],
                SPI_RX_TEXT[3],
                SPI_RX_TEXT[4],
                SPI_RX_TEXT[5],
                SPI_RX_TEXT[6],
                SPI_RX_TEXT[7]);
        // LED=0;
        SPI_full = 0;
    }
}



void cf_EUSART1_Check_Buffer(void) {

    if (RX1_full == 1) {//Le Wipy à parler

        //LED=1;
        EUSART1_RX_T3_LOCAL(UART_RX_TEXT[0],
                UART_RX_TEXT[1],
                UART_RX_TEXT[2],
                UART_RX_TEXT[3],
                UART_RX_TEXT[4],
                UART_RX_TEXT[5],
                UART_RX_TEXT[6],
                UART_RX_TEXT[7]);
        // LED=0;
        RX1_full = 0;
    }
}
