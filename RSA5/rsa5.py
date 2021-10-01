# in this challenge we can notice that e is small and c is very small compared to N so we can assume that m < N ** (1/e) (m is the flag) 
# which implies that C = m**e < N which means that computing the cubic root of C should reveal the flag because C didn't change with the modular operation

from gmpy2 import iroot

N = 26052240516901362680945914012671713520282228014546358237363539031302825820262427534680806690950328616799330257513127158053406244874555511818119614815195710003517034356191527155272102303800630225540847496043672606816054223112404544809108187525420903554386938676534575636432987307915949422934065327409039770174607453708719810082806646394566597572726908919755712323985824778225681829526168286528456240676576984791756869795750785327185047108905225453115741697781734851516773854189127354977153171584452782977316949691801380569322585893884451339841911787679811344246230410180680909906566816074515147673202234231021156511421
e = 3
c = 40378828974014904250461375807391623250836371513419979274604071664462283627670084932635739741200783088455028809037375333474730451028597375932756791521321188386269524130121217192249424704880735333
m = int(iroot(c,e)[0]) # the complete output for iroot should be a tuple (value , True)  True means that the cubic root is exact : no remainder
print(f"Flag is {long_to_bytes(m)}")