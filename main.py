# Test Client 2020-09-23
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import socket
import datetime

HOST = '127.0.0.1'
PORT = 20550


def sendmes(mes) -> None:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    s.send(mes)
    s.close()


print(f'Run Client mode.Testing HOST={HOST}:{PORT}')
prefix = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#msg = f'test DTM= {prefix}'.encode()  # .encode('ascii', errors='ignore')
#msg = "11 clock".encode()
# 2020-10-05
d1 = b'H|\\^&|||    XN-350^00-20^16411^^^^AW618382||||||||E1394-97\rP|1|||43000|^\xd5\xe0\xf0\xf7\xe5\xed\xea\xee^\xc3|||M|||||^||||||||||||^^^\xc3\xeb\xe0\xe7\xed\xee\xe5 \xee\xf2\xe4\rC|1||\rO|1||^^                     1^M|^^^^WBC\\^^^^RBC\\^^^^HGB\\^^^^HCT\\^^^^MCV\\^^^^MCH\\^^^^MCHC\\^^^^PLT\\^^^^RDW-SD\\^^^^RDW-CV\\^^^^PDW\\^^^^MPV\\^^^^P-LCR\\^^^^PCT\\^^^^NEUT#\\^^^^LYMPH#\\^^^^MONO#\\^^^^EO#\\^^^^BASO#\\^^^^NEUT%\\^^^^LYMPH%\\^^^^MONO%\\^^^^EO%\\^^^^BASO%\\^^^^IG#\\^^^^IG%\\^^^^MICROR\\^^^^MACROR\\^^^^OPEN|||||||N||||||||||||||F\rC|1||\rR|1|^^^^WBC^1|16,92|10*3/uL||H||F||||20200908110303\rR|2|^^^^RBC^1|4,70|10*6/uL||N||F||||20200908110303\rR|3|^^^^HGB^1|14,2|g/dL||N||F||||20200908110303\rR|4|^^^^HCT^1|42,8|%||N||F||||20200908110303\rR|5|^^^^MCV^1|91,1|fL||N||F||||20200908110303\rR|6|^^^^MCH^1|30,2|pg||N||F||||20200908110303\rR|7|^^^^MCHC^1|33,2|g/dL||N||F||||20200908110303\rR|8|^^^^PLT^1|348|10*3/uL||N||F||||20200908110303\rR|9|^^^^NEUT%^1|82,4|%||H||F||||20200908110303\rR|10|^^^^LYMPH%^1|13,2|%||L||F||||20200908110303\rR|11|^^^^MONO%^1|3,3|%||N||F||||20200908110303\rR|12|^^^^EO%^1|0,8|%||N||F||||202009081103'
d2 = b'03\rR|13|^^^^BASO%^1|0,3|%||N||F||||20200908110303\rR|14|^^^^NEUT#^1|13,94|10*3/uL||H||F||||20200908110303\rR|15|^^^^LYMPH#^1|2,24|10*3/uL||N||F||||20200908110303\rR|16|^^^^MONO#^1|0,56|10*3/uL||N||F||||20200908110303\rR|17|^^^^EO#^1|0,13|10*3/uL||N||F||||20200908110303\rR|18|^^^^BASO#^1|0,05|10*3/uL||N||F||||20200908110303\rR|19|^^^^IG%^1|1,0|%||N||F||||20200908110303\rR|20|^^^^IG#^1|0,17|10*3/uL||N||F||||20200908110303\rR|21|^^^^RDW-SD^1|44,3|fL||N||F||||20200908110303\rR|22|^^^^RDW-CV^1|13,0|%||N||F||||20200908110303\rR|23|^^^^MICROR^1|1,0|%||N||F||||20200908110303\rR|24|^^^^MACROR^1|4,2|%||N||F||||20200908110303\rR|25|^^^^PDW^1|10,4|fL||N||F||||20200908110303\rR|26|^^^^MPV^1|9,7|fL||N||F||||20200908110303\rR|27|^^^^P-LCR^1|22,0|%||N||F||||20200908110303\rR|28|^^^^PCT^1|0,34|%||N||F||||20200908110303\rR|29|^^^^Neutrophilia||||A||F||||20200908110303\rR|30|^^^^IG_Present||||A||F||||20200908110303\rR|31|^^^^Blasts/Abn_Lympho?|80|||||F||||20200908110303\rR|32|^^^^Left_Shift?|0|||||F||||20200908110303\rR|33|^^^^Atypical_Lympho?|0||'
d3 = b'|||F||||20200908110303\rR|34|^^^^NRBC?|0|||||F||||20200908110303\rR|35|^^^^RBC_Agglutination?|70|||||F||||20200908110303\rR|36|^^^^Turbidity/HGB_Interference?|90|||||F||||20200908110303\rR|37|^^^^Iron_Deficiency?|80|||||F||||20200908110303\rR|38|^^^^HGB_Defect?|80|||||F||||20200908110303\rR|39|^^^^Fragments?|0|||||F||||20200908110303\rR|40|^^^^IRBC?|0|||||F||||20200908110303\rR|41|^^^^PLT_Clumps?|0|||||F||||20200908110303\rR|42|^^^^Positive_Diff||||A||F||||20200908110303\rR|43|^^^^Positive_Morph||||A||F||||20200908110303\rR|44|^^^^Positive_Count||||A||F||||20200908110303\rR|45|^^^^SCAT_WDF|PNG&R&20201005&R&2020_09_08_11_03_1_WDF.PNG|||N||F||||20200908110303\rR|46|^^^^SCAT_WDF-CBC|PNG&R&20201005&R&2020_09_08_11_03_1_WDF_CBC.PNG|||N||F||||20200908110303\rR|47|^^^^DIST_RBC|PNG&R&20201005&R&2020_09_08_11_03_1_RBC.PNG|||N||F||||20200908110303\rR|48|^^^^DIST_PLT|PNG&R&20201005&R&2020_09_08_11_03_1_PLT.PNG|||N||F||||20200908110303\rC|1||\rL|1|N\r'
msg = d1 + d2 + d3
sendmes(msg)
print(f'send {msg}')
