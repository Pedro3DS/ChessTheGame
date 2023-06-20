from peças import*
def tabuleiro():
    linha1 = {"A1":torre_P1(),"B1":cavalo_P1(),"C1":bispo_P1(),"D1":rainha_P(),"E1":rei_P(),"F1":bispo_P2(),"G1":cavalo_P2(),"H1":torre_P2()}
    linha2 = {"A2":peao_P1(),"B2":peao_P2(),"C2":peao_P3(),"D2":peao_P4(),"E2":peao_P5(),"F2":peao_P6(),"G2":peao_P7(),"H2":peao_P8()}
    linha3 = {"A3":print(""),"B3":" ","C3":" ","D3":" ","E3":" ","F3":" ","G3":" ","H3":" "}
    linha4 = {"A4":print(""),"B4":" ","C4":" ","D4":" ","E4":" ","F4":" ","G4":" ","H4":" "}
    linha5 = {"A5":print(""),"B5":"","C5":"","D5":"","E5":"","F5":"","G5":"","H5":""}
    linha6 = {"A6":print(""),"B6":" ","C6":" ","D6":" ","E6":" ","F6":" ","G6":" ","H6":" "}
    linha7 = {"A7":peao_B1(),"B7":peao_B2(),"C7":peao_B3(),"D7":peao_B4(),"E7":peao_B5(),"F7":peao_B6(),"G7":peao_B7(),"H7":peao_B8()}
    linha8 = {"A8":torre_B1(),"B8":cavalo_B1(),"C8":bispo_B1(),"D8":rainha_B(),"E8":rei_B(),"F8":bispo_B2(),"G8":cavalo_B2(),"H8":torre_B2()}
    return linha1, linha2, linha3, linha4, linha5, linha6, linha7, linha8
tabuleiro()