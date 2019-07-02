/* 
 * File:   eusart.h
 * Author: sam
 *
 * Created on 17 janvier 2018, 16:57
 */

#ifndef EUSART_H
#define	EUSART_H

#ifdef	__cplusplus
extern "C" {
#endif
//#include "variable_extern.h"
//
//static unsigned char UART_TX_TEXT[EUSART1_TX_BUFFER_SIZE];
//static unsigned char UART_RX_TEXT[EUSART1_RX_BUFFER_SIZE];
//
//
//volatile unsigned char eusart1TxIndex; //index du buffer de transmission
//static unsigned char eusart1TxBuffer[EUSART1_TX_BUFFER_SIZE]; //Buffer de transmission
//
//volatile unsigned char eusart1RxIndex; //index du buffer de r�ception
//static unsigned char eusart1RxBuffer[EUSART1_RX_BUFFER_SIZE]; //Buffer d'�mission

void EUSART1_Send_Test(void);
void EUSART1_Check_Buffer(void);

    /**
      Section: EUSART1 APIs
     */

    /**
      @Summary
        Initialization routine that takes inputs from the EUSART1 GUI.

      @Description
        This routine initializes the EUSART1 driver.
        This routine must be called before any other EUSART1 routine is called.

      @Preconditions
        None

      @Param
        None

      @Returns
        None

      @Comment

      @Example
     */
    void EUSART1_Initialize(void);

    /**
      @Summary
        Read a byte of data from the EUSART1.

      @Description
        This routine reads a byte of data from the EUSART1.

      @Preconditions
        EUSART1_Initialize() function should have been called
        before calling this function. The transfer status should be checked to see
        if the receiver is not empty before calling this function.
	
        EUSART1_DataReady is a macro which checks if any byte is received.
        Call this macro before using this function.

      @Param
        None

      @Returns
        A data byte received by the driver.
	
      @Example
        <code>
                void main(void) {
                                    // initialize the device
                                    SYSTEM_Initialize();
                                    uint8_t data;
								
                                    // Enable the Global Interrupts
                                    INTERRUPT_GlobalInterruptEnable();
								
                                    // Enable the Peripheral Interrupts
                                    INTERRUPT_PeripheralInterruptEnable();
								
                                    printf("\t\tTEST CODE\n\r");		//Enable redirect STDIO to USART before using printf statements
                                    printf("\t\t---- ----\n\r");
                                    printf("\t\tECHO TEST\n\r");
                                    printf("\t\t---- ----\n\n\r");
                                    printf("Enter any string: ");
                                    do{
                                    data = EUSART1_Read();		// Read data received
                                    EUSART_Write(data);			// Echo back the data received
                                    }while(!EUSART1_DataReady);		//check if any data is received
								
                                }
        </code>
     */
    //uint8_t EUSART1_Read(void);

    /**
     @Summary
       Writes a byte of data to the EUSART1.

     @Description
       This routine writes a byte of data to the EUSART1.

     @Preconditions
       EUSART1_Initialize() function should have been called
       before calling this function. The transfer status should be checked to see
       if transmitter is not busy before calling this function.

     @Param
       txData  - Data byte to write to the EUSART1

     @Returns
       None
  
     @Example
         <code>
             Refer to EUSART1_Read() for an example	
         </code>
     */
    //void EUSART1_Write(uint8_t txData);
    //void EUSART1_Write_And_Forget(void);
    //void EUSART1_Write_Text(char *text);
    void EUSART1_Buffer_Send(char *text);
    //void EUSART1_Buffer_Send(void);
    /**
      @Summary
        Maintains the driver's transmitter state machine and implements its ISR.

      @Description
        This routine is used to maintain the driver's internal transmitter state
        machine.This interrupt service routine is called when the state of the
        transmitter needs to be maintained in a non polled manner.

      @Preconditions
        EUSART1_Initialize() function should have been called
        for the ISR to execute correctly.

      @Param
        None

      @Returns
        None
     */
    void EUSART1_Transmit_ISR(void);

    /**
      @Summary
        Maintains the driver's receiver state machine and implements its ISR

      @Description
        This routine is used to maintain the driver's internal receiver state
        machine.This interrupt service routine is called when the state of the
        receiver needs to be maintained in a non polled manner.

      @Preconditions
        EUSART1_Initialize() function should have been called
        for the ISR to execute correctly.

      @Param
        None

      @Returns
        None
     */
    void EUSART1_Receive_ISR(void);

    /**
      @Summary
        Maintains the driver's transmitter state machine and implements its ISR.

      @Description
        This routine is used to maintain the driver's internal transmitter state
        machine.This interrupt service routine is called when the state of the
        transmitter needs to be maintained in a non polled manner.

      @Preconditions
        EUSART1_Initialize() function should have been called
        for the ISR to execute correctly.

      @Param
        None

      @Returns
        None
     */

    void EUSART1_Receive_ISR(void);
void EUSART1_RX_T3_LOCAL(unsigned char Ad, unsigned char Da, unsigned char A, unsigned char B, unsigned char C, unsigned char D, unsigned char E, unsigned char F);
//void EUSART1_RX_T3_LOCAL(unsigned char Ad, unsigned char Da, unsigned char A, unsigned char B, unsigned char C, unsigned char D, unsigned char E, unsigned char F);

void EUSART1_RX_T3(void);


#ifdef	__cplusplus
}
#endif

#endif	/* EUSART_H */

