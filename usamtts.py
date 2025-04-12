"""USAMTTS

A Python port of Software Automatic Mouth Test-To-Speech program.

- Ported by: Quan Lin
- License: None
"""

__version__ = "0.2.0"


tab36376 = b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x02\x02\x02\x02\x02\x82\x00\x00\x02\x02\x02\x02\x02\x02\x03\x03\x03\x03\x03\x03\x03\x03\x03\x03\x02\x02\x02\x02\x02\x02\x02\xc0\xa8\xb0\xac\xc0\xa0\xb8\xa0\xc0\xbc\xa0\xac\xa8\xac\xc0\xa0\xa0\xac\xb4\xa4\xc0\xa8\xa8\xb0\xc0\xbc\x00\x00\x00\x02\x00  \x9b \xc0\xb9 \xcd\xa3L\x8a\x8e"
rules = b"]\xc1 (A.)=EH4Y.\xa0(A) =A\xc8 (ARE) =AA\xd2 (AR)O=AX\xd2(AR)#=EH4\xd2 ^(AS)#=EY4\xd3(A)WA=A\xd8(AW)=AO\xb5 :(ANY)=EH4NI\xd9(A)^+#=EY\xb5#:(ALLY)=ULI\xd9 (AL)#=U\xcc(AGAIN)=AXGEH4\xce#:(AG)E=IH\xca(A)^%=E\xd9(A)^+:#=A\xc5 :(A)^+ =EY\xb4 (ARR)=AX\xd2(ARR)=AE4\xd2 ^(AR) =AA5\xd2(AR)=AA5\xd2(AIR)=EH4\xd2(AI)=EY\xb4(AY)=EY\xb5(AU)=AO\xb4#:(AL) =U\xcc#:(ALS) =UL\xda(ALK)=AO4\xcb(AL)^=AO\xcc :(ABLE)=EY4BU\xcc(ABLE)=AXBU\xcc(A)VO=EY\xb4(ANG)+=EY4N\xca(ATARI)=AHTAA4RI\xd9(A)TOM=A\xc5(A)TTI=A\xc5 (AT) =AE\xd4 (A)T=A\xc8(A)=A\xc5]\xc2 (B) =BIY\xb4 (BE)^#=BI\xc8(BEING)=BIY4IHN\xd8 (BOTH) =BOW4T\xc8 (BUS)#=BIH4\xda(BREAK)=BREY5\xcb(BUIL)=BIH4\xcc(B)=\xc2]\xc3 (C) =SIY\xb4 (CH)^=\xcb^E(CH)=\xcb(CHA)R#=KEH\xb5(CH)=C\xc8 S(CI)#=SAY\xb4(CI)A=S\xc8(CI)O=S\xc8(CI)EN=S\xc8(CITY)=SIHTI\xd9(C)+=\xd3(CK)=\xcb(COMMODORE)=KAA4MAHDOH\xd2(COM)=KAH\xcd(CUIT)=KIH\xd4(CREA)=KRIYE\xd9(C)=\xcb]\xc4 (D) =DIY\xb4 (DR.) =DAA4KTE\xd2#:(DED) =DIH\xc4.E(D) =\xc4#:^E(D) =\xd4 (DE)^#=DI\xc8 (DO) =DU\xd7 (DOES)=DAH\xda(DONE) =DAH5\xce(DOING)=DUW4IHN\xd8 (DOW)=DA\xd7#(DU)A=JU\xd7#(DU)^#=JA\xd8(D)=\xc4]\xc5 (E) =IYIY\xb4#:(E) \xbd':^(E) \xbd :(E) =I\xd9#(ED) =\xc4#:(E)D \xbd(EV)ER=EH4\xd6(E)^%=IY\xb4(ERI)#=IY4RI\xd9(ERI)=EH4RI\xc8#:(ER)#=E\xd2(ERROR)=EH4ROH\xd2(ERASE)=IHREY5\xd3(ER)#=EH\xd2(ER)=E\xd2 (EVEN)=IYVEH\xce#:(E)W\xbd@(EW)=U\xd7(EW)=YU\xd7(E)O=I\xd9#:&(ES) =IH\xda#:(E)S \xbd#:(ELY) =LI\xd9#:(EMENT)=MEHN\xd4(EFUL)=FUH\xcc(EE)=IY\xb4(EARN)=ER5\xce (EAR)^=ER\xb5(EAD)=EH\xc4#:(EA) =IYA\xd8(EA)SU=EH\xb5(EA)=IY\xb5(EIGH)=EY\xb4(EI)=IY\xb4 (EYE)=AY\xb4(EY)=I\xd9(EU)=YUW\xb5(EQUAL)=IY4KWU\xcc(E)=E\xc8]\xc6 (F) =EH4\xc6(FUL)=FUH\xcc(FRIEND)=FREH5N\xc4(FATHER)=FAA4DHE\xd2(F)F\xbd(F)=\xc6]\xc7 (G) =JIY\xb4(GIV)=GIH5\xd6 (G)I^=\xc7(GE)T=GEH\xb5SU(GGES)=GJEH4\xd3(GG)=\xc7 B#(G)=\xc7(G)+=\xca(GREAT)=GREY4\xd4(GON)E=GAO5\xce#(GH)\xbd (GN)=\xce(G)=\xc7]\xc8 (H) =EY4C\xc8 (HAV)=/HAE6\xd6 (HERE)=/HIY\xd2 (HOUR)=AW5E\xd2(HOW)=/HA\xd7(H)#=/\xc8(H)\xbd]\xc9 (IN)=IH\xce (I) =AY\xb4(I) =A\xd9(IN)D=AY5\xceSEM(I)=I\xd9 ANT(I)=A\xd9(IER)=IYE\xd2#:R(IED) =IY\xc4(IED) =AY5\xc4(IEN)=IYEH\xce(IE)T=AY4E\xc8(I')=AY\xb5 :(I)^%=AY\xb5 :(IE) =AY\xb4(I)%=I\xd9(IE)=IY\xb4 (IDEA)=AYDIY5A\xc8(I)^+:#=I\xc8(IR)#=AY\xd2(IZ)%=AY\xda(IS)%=AY\xdaI^(I)^#=I\xc8+^(I)^+=A\xd9#:^(I)^+=I\xc8(I)^+=A\xd9(IR)=E\xd2(IGH)=AY\xb4(ILD)=AY5L\xc4 (IGN)=IHG\xce(IGN) =AY4\xce(IGN)^=AY4\xce(IGN)%=AY4\xce(ICRO)=AY4KRO\xc8(IQUE)=IY4\xcb(I)=I\xc8]\xca (J) =JEY\xb4(J)=\xca]\xcb (K) =KEY\xb4 (K)N\xbd(K)=\xcb]\xcc (L) =EH4\xcc(LO)C#=LO\xd7L(L)\xbd#:^(L)%=U\xcc(LEAD)=LIY\xc4 (LAUGH)=LAE4\xc6(L)=\xcc]\xcd (M) =EH4\xcd (MR.) =MIH4STE\xd2 (MS.)=MIH5\xda (MRS.) =MIH4SIX\xda(MOV)=MUW4\xd6(MACHIN)=MAHSHIY5\xceM(M)\xbd(M)=\xcd]\xce (N) =EH4\xceE(NG)+=N\xca(NG)R=NX\xc7(NG)#=NX\xc7(NGL)%=NXGU\xcc(NG)=N\xd8(NK)=NX\xcb (NOW) =NAW\xb4N(N)\xbd(NON)E=NAH4\xce(N)=\xce]\xcf (O) =OH4\xd7(OF) =AH\xd6 (OH) =OW\xb5(OROUGH)=ER4O\xd7#:(OR) =E\xd2#:(ORS) =ER\xda(OR)=AO\xd2 (ONE)=WAH\xce#(ONE) =WAH\xce(OW)=O\xd7 (OVER)=OW5VE\xd2PR(O)V=UW\xb4(OV)=AH4\xd6(O)^%=OW\xb5(O)^EN=O\xd7(O)^I#=OW\xb5(OL)D=OW4\xcc(OUGHT)=AO5\xd4(OUGH)=AH5\xc6 (OU)=A\xd7H(OU)S#=AW\xb4(OUS)=AX\xd3(OUR)=OH\xd2(OULD)=UH5\xc4(OU)^L=AH\xb5(OUP)=UW5\xd0(OU)=A\xd7(OY)=O\xd9(OING)=OW4IHN\xd8(OI)=OY\xb5(OOR)=OH5\xd2(OOK)=UH5\xcbF(OOD)=UW5\xc4L(OOD)=AH5\xc4M(OOD)=UW5\xc4(OOD)=UH5\xc4F(OOT)=UH5\xd4(OO)=UW\xb5(O')=O\xc8(O)E=O\xd7(O) =O\xd7(OA)=OW\xb4 (ONLY)=OW4NLI\xd9 (ONCE)=WAH4N\xd3(ON'T)=OW4N\xd4C(O)N=A\xc1(O)NG=A\xcf :^(O)N=A\xc8I(ON)=U\xce#:(ON)=U\xce#^(ON)=U\xce(O)ST=O\xd7(OF)^=AO4\xc6(OTHER)=AH5DHE\xd2R(O)B=RA\xc1^R(O):#=OW\xb5(OSS) =AO5\xd3#:^(OM)=AH\xcd(O)=A\xc1]\xd0 (P) =PIY\xb4(PH)=\xc6(PEOPL)=PIY5PU\xcc(POW)=PAW\xb4(PUT) =PUH\xd4(P)P\xbd(P)S\xbd(P)N\xbd(PROF.)=PROHFEH4SE\xd2(P)=\xd0]\xd1 (Q) =KYUW\xb4(QUAR)=KWOH5\xd2(QU)=K\xd7(Q)=\xcb]\xd2 (R) =AA5\xd2 (RE)^#=RI\xd9(R)R\xbd(R)=\xd2]\xd3 (S) =EH4\xd3(SH)=S\xc8#(SION)=ZHU\xce(SOME)=SAH\xcd#(SUR)#=ZHE\xd2(SUR)#=SHE\xd2#(SU)#=ZHU\xd7#(SSU)#=SHU\xd7#(SED)=Z\xc4#(S)#=\xda(SAID)=SEH\xc4^(SION)=SHU\xce(S)S\xbd.(S) =\xda#:.E(S) =\xda#:^#(S) =\xd3U(S) =\xd3 :#(S) =\xda##(S) =\xda (SCH)=S\xcb(S)C+\xbd#(SM)=ZU\xcd#(SN)'=ZU\xcd(STLE)=SU\xcc(S)=\xd3]\xd4 (T) =TIY\xb4 (THE) #=DHI\xd9 (THE) =DHA\xd8(TO) =TU\xd8 (THAT)=DHAE\xd4 (THIS) =DHIH\xd3 (THEY)=DHE\xd9 (THERE)=DHEH\xd2(THER)=DHE\xd2(THEIR)=DHEH\xd2 (THAN) =DHAE\xce (THEM) =DHAE\xce(THESE) =DHIY\xda (THEN)=DHEH\xce(THROUGH)=THRUW\xb4(THOSE)=DHOH\xda(THOUGH) =DHO\xd7(TODAY)=TUXDE\xd9(TOMO)RROW=TUMAA\xb5(TO)TAL=TOW\xb5 (THUS)=DHAH4\xd3(TH)=T\xc8#:(TED)=TIX\xc4S(TI)#N=C\xc8(TI)O=S\xc8(TI)A=S\xc8(TIEN)=SHU\xce(TUR)#=CHE\xd2(TU)A=CHU\xd7 (TWO)=TU\xd7&(T)EN \xbd(T)=\xd4]\xd5 (U) =YUW\xb4 (UN)I=YUW\xce (UN)=AH\xce (UPON)=AXPAO\xce@(UR)#=UH4\xd2(UR)#=YUH4\xd2(UR)=E\xd2(U)^ =A\xc8(U)^^=AH\xb5(UY)=AY\xb5 G(U)#\xbdG(U)%\xbdG(U)#=\xd7#N(U)=YU\xd7@(U)=U\xd7(U)=YU\xd7]\xd6 (V) =VIY\xb4(VIEW)=VYUW\xb5(V)=\xd6]\xd7 (W) =DAH4BULYU\xd7 (WERE)=WE\xd2(WA)SH=WA\xc1(WA)ST=WE\xd9(WA)S=WA\xc8(WA)T=WA\xc1(WHERE)=WHEH\xd2(WHAT)=WHAH\xd4(WHOL)=/HOW\xcc(WHO)=/HU\xd7(WH)=W\xc8(WAR)#=WEH\xd2(WAR)=WAO\xd2(WOR)^=WE\xd2(WR)=\xd2(WOM)A=WUH\xcd(WOM)E=WIH\xcd(WEA)R=WE\xc8(WANT)=WAA5N\xd4ANS(WER)=E\xd2(W)=\xd7]\xd8 (X) =EH4K\xd2 (X)=\xda(X)=K\xd3]\xd9 (Y) =WAY\xb4(YOUNG)=YAHN\xd8 (YOUR)=YOH\xd2 (YOU)=YU\xd7 (YES)=YEH\xd3 (Y)=\xd9F(Y)=A\xd9PS(YCH)=AY\xcb#:^(Y)=I\xd9#:^(Y)I=I\xd9 :(Y) =A\xd9 :(Y)#=A\xd9 :(Y)^+:#=I\xc8 :(Y)^#=A\xd9(Y)=I\xc8]\xda (Z) =ZIY\xb4(Z)=\xda\xea"
rules2 = b'(A)\xbd(!)=\xae(") =-AH5NKWOWT\xad(")=KWOW4T\xad(#)= NAH4MBE\xd2($)= DAA4LE\xd2(%)= PERSEH4N\xd4(&)= AEN\xc4(\')\xbd(*)= AE4STERIHS\xcb(+)= PLAH4\xd3(,)=\xac (-) =\xad(-)\xbd(.)= POYN\xd4(/)= SLAE4S\xc8(0)= ZIY4RO\xd7 (1ST)=FER4S\xd4 (10TH)=TEH4NT\xc8(1)= WAH4\xce (2ND)=SEH4KUN\xc4(2)= TUW\xb4 (3RD)=THER4\xc4(3)= THRIY\xb4(4)= FOH4\xd2 (5TH)=FIH4FT\xc8(5)= FAY4\xd6 (64) =SIH4KSTIY FOH\xd2(6)= SIH4K\xd3(7)= SEH4VU\xce (8TH)=EY4T\xc8(8)= EY4\xd4(9)= NAY4\xce(:)=\xae(;)=\xae(<)= LEH4S DHAE\xce(=)= IY4KWUL\xda(>)= GREY4TER DHAE\xce(?)=\xbf(@)= AE6\xd4(^)= KAE4RIX\xd4]\xc1'
tab37489 = b"\x00\x95\xf7\xa29\xc5\x06~\xc7&7N\x91\xf1U\xa1\xfe$E-\xa76S.G\xda"
tab37515 = b"}~~\x7f\x80\x81\x82\x82\x82\x84\x84\x84\x84\x84\x85\x87\x87\x88\x88\x89\x8a\x8b\x8b\x8c\x8c\x8c"


class Reciter:
    def __init__(self, debug=False):
        self._a = 0
        self._x = 0
        self._y = 0
        self.debug = debug

    def _code37055(self, m):
        self._x = m
        self._x = (self._x - 1) & 0xFF
        self._a = self.input_copy[self._x]
        self._y = self._a
        self._a = tab36376[self._y]

    def _code37066(self, m):
        self._x = m
        self._x = (self._x + 1) & 0xFF
        self._a = self.input_copy[self._x]
        self._y = self._a
        self._a = tab36376[self._y]

    def _get_rule_byte(self, m, y):
        address = m

        if m >= 37541:
            address -= 37541
            return rules2[address + y]

        address -= 32000
        return rules[address + y]

    def _print_rule(self, offset):
        i = 1
        a = 0

        print("Applying rule: ", end="")

        a = self._get_rule_byte(offset, i)
        if (a & 127) == ord("="):
            print(" -> ", end="")
        else:
            print(chr(a & 127), end="")
        i += 1
        while (a & 128) == 0:
            a = self._get_rule_byte(offset, i)
            if (a & 127) == ord("="):
                print(" -> ", end="")
            else:
                print(chr(a & 127), end="")
            i += 1

        print()

    def text_to_phonemes(self, input_text):
        self._a = 0
        self._x = 0
        self._y = 0

        m = 0

        self.input_copy = bytearray(256)

        if isinstance(input_text, str):
            input_text = input_text.encode("utf-8")
        elif not isinstance(input_text, (bytes, bytearray)):
            raise Exception("The type of input text must be str, bytes or bytearray.")

        temp_input = input_text + b"["

        input_text = bytearray(256)
        input_text[: len(temp_input)] = bytearray(temp_input)
        if len(input_text) > 256:
            input_text = input_text[:256]
            input_text[255] = ord("[")

        self.input_copy[0] = 32

        self._x = 1
        self._y = 0
        while self._y != 255:
            self._a = input_text[self._y] & 127
            if self._a >= 112:
                self._a = self._a & 95
            elif self._a >= 96:
                self._a = self._a & 79

            self.input_copy[self._x] = self._a
            self._x = (self._x + 1) & 0xFF
            self._y = (self._y + 1) & 0xFF

        self._x = 255
        self.input_copy[self._x] = 27
        n = 255

        state = 36550
        while True:
            if state == 36550:
                self._a = 255
                j = 255
                state = 36554
                continue

            elif state == 36554:
                while True:
                    n = (n + 1) & 0xFF
                    self._x = n
                    self._a = self.input_copy[self._x]
                    k = self._a
                    if self._a == ord("["):
                        j = (j + 1) & 0xFF
                        self._x = j
                        self._a = 155
                        input_text[self._x] = 155
                        return input_text[: input_text.find(b"\x9b")]

                    if self._a != ord("."):
                        break

                    self._x = (self._x + 1) & 0xFF
                    self._y = self.input_copy[self._x]
                    self._a = tab36376[self._y] & 1

                    if self._a != 0:
                        break

                    j = (j + 1) & 0xFF
                    self._x = j
                    self._a = ord(".")
                    input_text[self._x] = ord(".")

                self._a = k
                self._y = self._a
                self._a = tab36376[self._a]
                h = self._a
                if (self._a & 2) != 0:
                    g = 37541
                    state = 36700
                    continue

                self._a = h
                if self._a != 0:
                    state = 36677
                    continue

                self._a = 32
                self.input_copy[self._x] = ord(" ")
                j = (j + 1) & 0xFF
                self._x = j
                if self._x > 120:
                    state = 36654
                    continue

                input_text[self._x] = self._a
                state = 36554
                continue

            elif state == 36654:
                input_text[self._x] = 155
                self._a = n
                return input_text[: input_text.find(b"\x9b")]

            elif state == 36677:
                self._a = h & 128
                if self._a == 0:
                    return None

                self._x = (k - ord("A")) & 0xFF
                g = tab37489[self._x] | (tab37515[self._x] << 8)

                state = 36700
                continue

            elif state == 36700:
                self._y = 0
                g = (g + 1) % 65536
                self._a = self._get_rule_byte(g, self._y)
                while (self._a & 128) == 0:
                    g = (g + 1) % 65536
                    self._a = self._get_rule_byte(g, self._y)
                self._y = (self._y + 1) & 0xFF

                while True:
                    self._a = self._get_rule_byte(g, self._y)
                    if self._a == ord("("):
                        break
                    self._y = (self._y + 1) & 0xFF
                p = self._y

                self._y = (self._y + 1) & 0xFF
                self._a = self._get_rule_byte(g, self._y)
                while self._a != ord(")"):
                    self._y = (self._y + 1) & 0xFF
                    self._a = self._get_rule_byte(g, self._y)
                q = self._y

                self._y = (self._y + 1) & 0xFF
                self._a = self._get_rule_byte(g, self._y)
                self._a = self._a & 127
                while self._a != ord("="):
                    self._y = (self._y + 1) & 0xFF
                    self._a = self._get_rule_byte(g, self._y)
                    self._a = self._a & 127
                k = self._y

                self._x = n
                r = self._x

                self._y = p
                self._y = (self._y + 1) & 0xFF
                flag_goto_36700 = False
                while True:
                    h = self.input_copy[self._x]
                    self._a = self._get_rule_byte(g, self._y)
                    if self._a != h:
                        state = 36700
                        flag_goto_36700 = True
                        break

                    self._y = (self._y + 1) & 0xFF
                    if self._y == q:
                        break

                    self._x = (self._x + 1) & 0xFF
                    r = self._x

                if flag_goto_36700:
                    continue

                self._a = n
                t = n

                state = 36791
                continue

            elif state == 36791:
                flag_goto_37180 = False
                flag_goto_36700 = False
                while True:
                    p = (p - 1) & 0xFF
                    self._y = p
                    self._a = self._get_rule_byte(g, self._y)
                    h = self._a
                    if (self._a & 128) != 0:
                        state = 37180
                        flag_goto_37180 = True
                        break

                    self._x = self._a & 127
                    self._a = tab36376[self._x] & 128
                    if self._a == 0:
                        break
                    self._x = (t - 1) & 0xFF
                    self._a = self.input_copy[self._x]
                    if self._a != h:
                        state = 36700
                        flag_goto_36700 = True
                        break
                    t = self._x

                if flag_goto_37180:
                    continue

                if flag_goto_36700:
                    continue

                self._a = h
                if self._a == ord(" "):
                    state = 36895
                    continue
                if self._a == ord("#"):
                    state = 36910
                    continue
                if self._a == ord("."):
                    state = 36920
                    continue
                if self._a == ord("&"):
                    state = 36935
                    continue
                if self._a == ord("@"):
                    state = 36967
                    continue
                if self._a == ord("^"):
                    state = 37004
                    continue
                if self._a == ord("+"):
                    state = 37019
                    continue
                if self._a == ord(":"):
                    state = 37040
                    continue

                return None

            elif state == 36895:
                self._code37055(t)
                self._a = self._a & 128
                if self._a != 0:
                    state = 36700
                    continue

                state = 36905
                continue

            elif state == 36905:
                t = self._x
                state = 36791
                continue

            elif state == 36910:
                self._code37055(t)
                self._a = self._a & 64
                if self._a != 0:
                    state = 36905
                    continue

                state = 36700
                continue

            elif state == 36920:
                self._code37055(t)
                self._a = self._a & 8
                if self._a == 0:
                    state = 36700
                    continue

                state = 36930
                continue

            elif state == 36930:
                t = self._x
                state = 36791
                continue

            elif state == 36935:
                self._code37055(t)
                self._a = self._a & 16
                if self._a != 0:
                    state = 36930
                    continue

                self._a = self.input_copy[self._x]
                if self._a != 72:
                    state = 36700
                    continue

                self._x = (self._x - 1) & 0xFF
                self._a = self.input_copy[self._x]
                if (self._a == 67) or (self._a == 83):
                    state = 36930
                    continue

                state = 36700
                continue

            elif state == 36967:
                self._code37055(t)
                self._a = self._a & 4
                if self._a != 0:
                    state = 36930
                    continue

                self._a = self.input_copy[self._x]
                if self._a != 72:
                    state = 36700
                    continue

                if (self._a != 84) and (self._a != 67) and (self._a != 83):
                    state = 36700
                    continue

                t = self._x
                state = 36791
                continue

            elif state == 37004:
                self._code37055(t)
                self._a = self._a & 32
                if self._a == 0:
                    state = 36700
                    continue

                state = 37014
                continue

            elif state == 37014:
                t = self._x
                state = 36791
                continue

            elif state == 37019:
                self._x = t
                self._x = (self._x - 1) & 0xFF
                self._a = self.input_copy[self._x]
                if (
                    (self._a == ord("E"))
                    or (self._a == ord("I"))
                    or (self._a == ord("Y"))
                ):
                    state = 37014
                    continue

                state = 36700
                continue

            elif state == 37040:
                self._code37055(t)
                self._a = self._a & 32
                if self._a == 0:
                    state = 36791
                    continue

                t = self._x
                state = 37040
                continue

            elif state == 37077:
                self._x = (m + 1) & 0xFF
                self._a = self.input_copy[self._x]
                if self._a != ord("E"):
                    state = 37157
                    continue

                self._x = (self._x + 1) & 0xFF
                self._y = self.input_copy[self._x]
                self._x = (self._x - 1) & 0xFF
                self._a = tab36376[self._y] & 128
                if self._a == 0:
                    state = 37108
                    continue

                self._x = (self._x + 1) & 0xFF
                self._a = self.input_copy[self._x]
                if self._a != ord("R"):
                    state = 37113
                    continue

                state = 37108
                continue

            elif state == 37108:
                m = self._x
                state = 37184
                continue

            elif state == 37113:
                if (self._a == 83) or (self._a == 68):
                    state = 37108
                    continue

                if self._a != 76:
                    state = 37135
                    continue

                self._x = (self._x + 1) & 0xFF
                self._a = self.input_copy[self._x]
                if self._a != 89:
                    state = 36700
                    continue

                state = 37108
                continue

            elif state == 37135:
                if self._a != 70:
                    state = 36700
                    continue

                self._x = (self._x + 1) & 0xFF
                self._a = self.input_copy[self._x]
                if self._a != 85:
                    state = 36700
                    continue

                self._x = (self._x + 1) & 0xFF
                self._a = self.input_copy[self._x]
                if self._a == 76:
                    state = 37108
                    continue

                state = 36700
                continue

            elif state == 37157:
                if self._a != 73:
                    state = 36700
                    continue

                self._x = (self._x + 1) & 0xFF
                self._a = self.input_copy[self._x]
                if self._a != 78:
                    state = 36700
                    continue

                self._x = (self._x + 1) & 0xFF
                self._a = self.input_copy[self._x]
                if self._a == 71:
                    state = 37108
                    continue

                state = 36700
                continue

            elif state == 37180:
                self._a = r
                m = self._a
                state = 37184
                continue

            elif state == 37184:
                self._y = (q + 1) & 0xFF
                if self._y == k:
                    state = 37455
                    continue

                q = self._y
                self._a = self._get_rule_byte(g, self._y)
                h = self._a
                self._x = self._a
                self._a = tab36376[self._x] & 128
                if self._a == 0:
                    state = 37226
                    continue

                self._x = (m + 1) & 0xFF
                self._a = self.input_copy[self._x]
                if self._a != h:
                    state = 36700
                    continue

                m = self._x
                state = 37184
                continue

            elif state == 37226:
                self._a = h
                if self._a == 32:
                    state = 37295
                    continue
                if self._a == 35:
                    state = 37310
                    continue
                if self._a == 46:
                    state = 37320
                    continue
                if self._a == 38:
                    state = 37335
                    continue
                if self._a == 64:
                    state = 37367
                    continue
                if self._a == 94:
                    state = 37404
                    continue
                if self._a == 43:
                    state = 37419
                    continue
                if self._a == 58:
                    state = 37440
                    continue
                if self._a == 37:
                    state = 37077
                    continue

                return None

            elif state == 37295:
                self._code37066(m)
                self._a = self._a & 128
                if self._a != 0:
                    state = 36700
                    continue

                state = 37305
                continue

            elif state == 37305:
                m = self._x
                state = 37184
                continue

            elif state == 37310:
                self._code37066(m)
                self._a = self._a & 64
                if self._a != 0:
                    state = 37305
                    continue

                state = 36700
                continue

            elif state == 37320:
                self._code37066(m)
                self._a = self._a & 8
                if self._a == 0:
                    state = 36700
                    continue

                state = 37330
                continue

            elif state == 37330:
                m = self._x
                state = 37184
                continue

            elif state == 37335:
                self._code37066(m)
                self._a = self._a & 16
                if self._a != 0:
                    state = 37330
                    continue

                self._a = self.input_copy[self._x]
                if self._a != 72:
                    state = 36700
                    continue

                self._x = (self._x + 1) & 0xFF
                self._a = self.input_copy[self._x]
                if (self._a == 67) or (self._a == 83):
                    state = 37330
                    continue

                state = 36700
                continue

            elif state == 37367:
                self._code37066(m)
                self._a = self._a & 4
                if self._a != 0:
                    state = 37330
                    continue

                self._a = self.input_copy[self._x]
                if self._a != 72:
                    state = 36700
                    continue

                if (self._a != 84) and (self._a != 67) and (self._a != 83):
                    state = 36700
                    continue

                m = self._x
                state = 37184
                continue

            elif state == 37404:
                self._code37066(m)
                self._a = self._a & 32
                if self._a == 0:
                    state = 36700
                    continue

                state = 37414
                continue

            elif state == 37414:
                m = self._x
                state = 37184
                continue

            elif state == 37419:
                self._x = m
                self._x = (self._x + 1) & 0xFF
                self._a = self.input_copy[self._x]
                if (self._a == 69) or (self._a == 73) or (self._a == 89):
                    state = 37414
                    continue

                state = 36700
                continue

            elif state == 37440:
                self._code37066(m)
                self._a = self._a & 32
                if self._a == 0:
                    state = 37184
                    continue

                m = self._x
                state = 37440
                continue

            elif state == 37455:
                self._y = k
                n = r

                if self.debug:
                    self._print_rule(g)

                state = 37461
                continue

            elif state == 37461:
                self._a = self._get_rule_byte(g, self._y)
                h = self._a
                self._a = self._a & 127
                if self._a != ord("="):
                    j = (j + 1) & 0xFF
                    self._x = j
                    input_text[self._x] = self._a

                if (h & 128) == 0:
                    state = 37485
                    continue

                state = 36554
                continue

            elif state == 37485:
                self._y = (self._y + 1) & 0xFF
                state = 37461
                continue


stress_input_table = b"*12345678"
sign_input_table1 = (
    b" .?,-IIEAAAAUAIEUORLWYWRLWYMNNDQSSFT//ZZVDC*J***EAOAOUB**D**G**G**P**T**K**K**UUU"
)
sign_input_table2 = (
    b"*****YHHEAHOHXXRXHXXXXH******XX**H*HHX*H*HH*****YYYWWW*********X***********X**LMN"
)

FLAG_PLOSIVE = 0x0001
FLAG_STOPCONS = 0x0002
FLAG_VOICED = 0x0004
FLAG_DIPTHONG = 0x0010
FLAG_DIP_YX = 0x0020
FLAG_CONSONANT = 0x0040
FLAG_VOWEL = 0x0080
FLAG_PUNCT = 0x0100
FLAG_ALVEOLAR = 0x0400
FLAG_NASAL = 0x0800
FLAG_LIQUIC = 0x1000
FLAG_FRICATIVE = 0x2000

flags = [
    0x8000, 0xC100, 0xC100, 0xC100, 0xC100, 0x00A4, 0x00A4, 0x00A4,
    0x00A4, 0x00A4, 0x00A4, 0x0084, 0x0084, 0x00A4, 0x00A4, 0x0084,
    0x0084, 0x0084, 0x0084, 0x0084, 0x0084, 0x0084, 0x0044, 0x1044,
    0x1044, 0x1044, 0x1044, 0x084C, 0x0C4C, 0x084C, 0x0448, 0x404C,
    0x2440, 0x2040, 0x2040, 0x2440, 0x0040, 0x0040, 0x2444, 0x2044,
    0x2044, 0x2444, 0x2048, 0x2040, 0x004C, 0x2044, 0x0000, 0x0000,
    0x00B4, 0x00B4, 0x00B4, 0x0094, 0x0094, 0x0094, 0x004E, 0x004E,
    0x004E, 0x044E, 0x044E, 0x044E, 0x004E, 0x004E, 0x004E, 0x004E,
    0x004E, 0x004E, 0x004B, 0x004B, 0x004B, 0x044B, 0x044B, 0x044B,
    0x004B, 0x004B, 0x004B, 0x004B, 0x004B, 0x004B, 0x0080, 0x00C1,
    0x00C1,
]

phoneme_stressed_length_table = b"\x00\x12\x12\x12\x08\x0b\t\x0b\x0e\x0f\x0b\x10\x0c\x06\x06\x0e\x0c\x0e\x0c\x0b\x08\x08\x0b\n\t\x08\x08\x08\x08\x08\x03\x05\x02\x02\x02\x02\x02\x02\x06\x06\x08\x06\x06\x02\t\x04\x02\x01\x0e\x0f\x0f\x0f\x0e\x0e\x08\x02\x02\x07\x02\x01\x07\x02\x02\x07\x02\x02\x08\x02\x02\x06\x02\x02\x07\x02\x04\x07\x01\x04\x05\x05"
phoneme_length_table = b"\x00\x12\x12\x12\x08\x08\x08\x08\x08\x0b\x06\x0c\n\x05\x05\x0b\n\n\n\t\x08\x07\t\x07\x06\x08\x06\x07\x07\x07\x02\x05\x02\x02\x02\x02\x02\x02\x06\x06\x07\x06\x06\x02\x08\x03\x01\x1e\r\x0c\x0c\x0c\x0e\t\x06\x01\x02\x05\x01\x01\x06\x01\x02\x06\x01\x02\x08\x02\x02\x04\x02\x02\x06\x01\x04\x06\x01\x04\xc7\xff"

PR = 23
PD = 57
PT = 69
BREAK = 254
END = 255


class Processor:
    def __init__(self, debug=False):
        self.phoneme_index = bytearray(256)
        self.phoneme_index[255] = 32
        self.phoneme_length = bytearray(256)
        self.stress = bytearray(256)
        self.debug = debug

    def _print_phonemes(self):
        print("===========================================")
        print("Internal Phoneme presentation:")
        print()
        print(" idx    phoneme  length  stress")
        print("------------------------------")

        i = 0
        while (self.phoneme_index[i] != 255) and (i < 255):
            if self.phoneme_index[i] < 81:
                print(
                    f" {self.phoneme_index[i]:3}      {chr(sign_input_table1[self.phoneme_index[i]])}{chr(sign_input_table2[self.phoneme_index[i]])}      {self.phoneme_length[i]:3}       {self.stress[i]}"
                )
            else:
                print(
                    f" {self.phoneme_index[i]:3}      ??      {self.phoneme_length[i]:3}       {self.stress[i]}"
                )

            i += 1

        print("===========================================")
        print()

    def _insert(self, position, x, y, z):
        i = 253
        while i >= position:
            self.phoneme_index[i + 1] = self.phoneme_index[i]
            self.phoneme_length[i + 1] = self.phoneme_length[i]
            self.stress[i + 1] = self.stress[i]
            i -= 1

        self.phoneme_index[position] = x
        self.phoneme_length[position] = y
        self.stress[position] = z

    def _insert_breath(self):
        x = 255
        len = 0
        pos = 0

        index = self.phoneme_index[pos]
        while index != END:
            len = (len + self.phoneme_length[pos]) & 0xFF
            if len < 232:
                if index == BREAK:
                    pass
                elif not (flags[index] & FLAG_PUNCT):
                    if index == 0:
                        x = pos
                else:
                    len = 0
                    pos = (pos + 1) & 0xFF
                    self._insert(pos, BREAK, 0, 0)
            else:
                pos = x
                self.phoneme_index[pos] = 31
                self.phoneme_length[pos] = 4
                self.stress[pos] = 0

                len = 0
                pos = (pos + 1) & 0xFF
                self._insert(pos, BREAK, 0, 0)

            pos = (pos + 1) & 0xFF
            index = self.phoneme_index[pos]

    def _copy_stress(self):
        pos = 0

        y = self.phoneme_index[pos]
        while y != END:
            if flags[y] & 64:
                y = self.phoneme_index[(pos + 1) & 0xFF]

                if (y != END) and ((flags[y] & 128) != 0):
                    y = self.stress[(pos + 1) & 0xFF]
                    if y and not (y & 128):
                        self.stress[pos] = (y + 1) & 0xFF

            pos = (pos + 1) & 0xFF
            y = self.phoneme_index[pos]

    def _full_match(self, sign1, sign2):
        y = 0

        flag_loop_init = True
        while (y != 81) or flag_loop_init:
            flag_loop_init = False

            a = sign_input_table1[y]

            if a == sign1:
                a = sign_input_table2[y]
                if (a != ord("*")) and (a == sign2):
                    return y

            y = (y + 1) & 0xFF

        return None

    def _wild_match(self, sign1):
        y = 0

        flag_loop_init = True
        while (y != 81) or flag_loop_init:
            flag_loop_init = False

            if sign_input_table2[y] == ord("*"):
                if sign_input_table1[y] == sign1:
                    return y

            y = (y + 1) & 0xFF

        return None

    def _parser1(self, input_buf):
        position = 0
        srcpos = 0

        sign1 = input_buf[srcpos]
        while sign1 != 155:
            srcpos = (srcpos + 1) & 0xFF
            sign2 = input_buf[srcpos]

            match_f = self._full_match(sign1, sign2)
            match_w = self._wild_match(sign1)
            if match_f is not None:
                self.phoneme_index[position] = match_f
                position = (position + 1) & 0xFF
                srcpos = (srcpos + 1) & 0xFF
            elif match_w is not None:
                self.phoneme_index[position] = match_w
                position = (position + 1) & 0xFF
            else:
                match_t = 8
                while (sign1 != stress_input_table[match_t]) and (match_t > 0):
                    match_t -= 1

                if match_t == 0:
                    return 0

                self.stress[(position - 1) & 0xFF] = match_t

            sign1 = input_buf[srcpos]

        self.phoneme_index[position] = END
        return 1

    def _set_phoneme_length(self):
        position = 0
        while self.phoneme_index[position] != 255:
            a = self.stress[position]
            if (a == 0) or ((a & 128) != 0):
                self.phoneme_length[position] = phoneme_length_table[
                    self.phoneme_index[position]
                ]
            else:
                self.phoneme_length[position] = phoneme_stressed_length_table[
                    self.phoneme_index[position]
                ]

            position += 1

    def _code41240(self):
        pos = 0

        while self.phoneme_index[pos] != END:
            index = self.phoneme_index[pos]

            if flags[index] & FLAG_STOPCONS:
                if flags[index] & FLAG_PLOSIVE:
                    x = pos
                    x = (x + 1) & 0xFF
                    while not self.phoneme_index[x]:
                        x = (x + 1) & 0xFF

                    a = self.phoneme_index[x]
                    if a != END:
                        if (flags[a] & 8) or (a == 36) or (a == 37):
                            pos = (pos + 1) & 0xFF
                            continue

                self._insert(
                    (pos + 1) & 0xFF,
                    (index + 1) & 0xFF,
                    phoneme_length_table[(index + 1) & 0xFF],
                    self.stress[pos],
                )
                self._insert(
                    (pos + 2) & 0xFF,
                    (index + 2) & 0xFF,
                    phoneme_length_table[(index + 2) & 0xFF],
                    self.stress[pos],
                )
                pos = (pos + 2) & 0xFF

            pos = (pos + 1) & 0xFF

    def _change_rule(self, position, m, descr):
        if self.debug:
            print(f"RULE: {descr}")

        self.phoneme_index[position] = 13
        self._insert(position + 1, m, 0, self.stress[position])

    def _drule(self, string):
        if self.debug:
            print(f"RULE: {string}")

    def _drule_pre(self, descr, x):
        self._drule(descr)
        if self.debug:
            print("PRE")
            print(
                f"phoneme {x} ({chr(sign_input_table1[self.phoneme_index[x]])}{chr(sign_input_table2[self.phoneme_index[x]])}) length {self.phoneme_length[x]}"
            )

    def _drule_post(self, x):
        if self.debug:
            print("POST")
            print(
                f"phoneme {x} ({chr(sign_input_table1[self.phoneme_index[x]])}{chr(sign_input_table2[self.phoneme_index[x]])}) length {self.phoneme_length[x]}"
            )

    def _rule_alveolar_uw(self, x):
        if flags[self.phoneme_index[x - 1]] & FLAG_ALVEOLAR:
            self._drule("<ALVEOLAR> UW -> <ALVEOLAR> UX")
            self.phoneme_index[x] = 16

    def _rule_ch(self, x):
        self._drule("CH -> CH CH+1")
        self._insert(x + 1, 43, 0, self.stress[x])

    def _rule_j(self, x):
        self._drule("J -> J J+1")
        self._insert(x + 1, 45, 0, self.stress[x])

    def _rule_g(self, pos):
        index = self.phoneme_index[pos + 1]

        if (index != END) and ((flags[index] & FLAG_DIP_YX) == 0):
            self._drule(
                "G <VOWEL OR DIPTHONG NOT ENDING WITH IY> -> GX <VOWEL OR DIPTHONG NOT ENDING WITH IY>"
            )
            self.phoneme_index[pos] = 63

    def _change(self, pos, val, rule):
        self._drule(rule)
        self.phoneme_index[pos] = val

    def _rule_dipthong(self, p, pf, pos):
        a = 21 if pf & FLAG_DIP_YX else 20

        if a == 20:
            self._drule("insert WX following dipthong NOT ending in IY sound")
        elif a == 21:
            self._drule("insert YX following dipthong ending in IY sound")

        self._insert(pos + 1, a, 0, self.stress[pos])

        if p == 53:
            self._rule_alveolar_uw(pos)
        elif p == 42:
            self._rule_ch(pos)
        elif p == 44:
            self._rule_j(pos)

    def _parser2(self):
        pos = 0

        if self.debug:
            print("Parser2")

        p = self.phoneme_index[pos]
        while p != END:
            if self.debug:
                print(f"{pos}: {chr(sign_input_table1[p])}{chr(sign_input_table2[p])}")

            if p == 0:
                pos = (pos + 1) & 0xFF
                p = self.phoneme_index[pos]
                continue

            pf = flags[p]
            prior = self.phoneme_index[pos - 1]

            if pf & FLAG_DIPTHONG:
                self._rule_dipthong(p, pf, pos)
            elif p == 78:
                self._change_rule(pos, 24, "UL -> AX L")
            elif p == 79:
                self._change_rule(pos, 27, "UM -> AX M")
            elif p == 80:
                self._change_rule(pos, 28, "UN -> AX N")
            elif (pf & FLAG_VOWEL) and self.stress[pos]:
                if not self.phoneme_index[pos + 1]:
                    p = self.phoneme_index[pos + 2]
                    if (p != END) and (flags[p] & FLAG_VOWEL) and self.stress[pos + 2]:
                        self._drule(
                            "Insert glottal stop between two stressed vowels with space between them"
                        )
                        self._insert(pos + 2, 31, 0, 0)
            elif p == PR:
                if prior == PT:
                    self._change(pos - 1, 42, "T R -> CH R")
                elif prior == PD:
                    self._change(pos - 1, 44, "D R -> J R")
                elif flags[prior] & FLAG_VOWEL:
                    self._change(pos, 18, "<VOWEL> R -> <VOWEL> RX")
            elif (p == 24) and (flags[prior] & FLAG_VOWEL):
                self._change(pos, 19, "<VOWEL> L -> <VOWEL> LX")
            elif prior == 60 and p == 32:
                self._change(pos, 38, "G S -> G Z")
            elif p == 60:
                self._rule_g(pos)
            else:
                if p == 72:
                    y = self.phoneme_index[pos + 1]
                    if (y == END) or (flags[y] & FLAG_DIP_YX) == 0:
                        self._change(
                            pos,
                            75,
                            "K <VOWEL OR DIPTHONG NOT ENDING WITH IY> -> KX <VOWEL OR DIPTHONG NOT ENDING WITH IY>",
                        )
                        p = 75
                        pf = flags[p]

                if (flags[p] & FLAG_PLOSIVE) and (prior == 32):
                    if self.debug:
                        print(
                            f"RULE: S* {chr(sign_input_table1[p])}{chr(sign_input_table2[p])} -> S* {chr(sign_input_table1[p-12])}{chr(sign_input_table2[p-12])}"
                        )

                    self.phoneme_index[pos] = p - 12
                elif not (pf & FLAG_PLOSIVE):
                    p = self.phoneme_index[pos]
                    if p == 53:
                        self._rule_alveolar_uw(pos)
                    elif p == 42:
                        self._rule_ch(pos)
                    elif p == 44:
                        self._rule_j(pos)

                if p == 69 or p == 57:
                    if flags[self.phoneme_index[pos - 1]] & FLAG_VOWEL:
                        p = self.phoneme_index[pos + 1]
                        if not p:
                            p = self.phoneme_index[pos + 2]

                        if p == END:
                            break

                        if (
                            (p != END)
                            and (flags[p] & FLAG_VOWEL)
                            and not self.stress[pos + 1]
                        ):
                            self._change(
                                pos,
                                30,
                                "Soften T or D following vowel or ER and preceding a pause -> DX",
                            )

            pos = (pos + 1) & 0xFF
            p = self.phoneme_index[pos]

    def _adjust_lengths(self):
        x = 0
        index = self.phoneme_index[x]
        while index != END:
            if (flags[index] & FLAG_PUNCT) == 0:
                x = (x + 1) & 0xFF
                index = self.phoneme_index[x]
                continue

            loopIndex = x

            x = (x - 1) & 0xFF
            while x and not (flags[self.phoneme_index[x]] & FLAG_VOWEL):
                x = (x - 1) & 0xFF

            if x == 0:
                break

            flag_loop_init = True
            while (x != loopIndex) or flag_loop_init:
                flag_loop_init = False

                index = self.phoneme_index[x]

                if (not (flags[index] & FLAG_FRICATIVE)) or (
                    flags[index] & FLAG_VOICED
                ):
                    a = self.phoneme_length[x]
                    self._drule_pre(
                        "Lengthen <FRICATIVE> or <VOICED> between <VOWEL> and <PUNCTUATION> by 1.5",
                        x,
                    )
                    self.phoneme_length[x] = (a >> 1) + a + 1
                    self._drule_post(x)

                x = (x + 1) & 0xFF

            x = (x + 1) & 0xFF
            index = self.phoneme_index[x]

        loopIndex = 0
        index = self.phoneme_index[loopIndex]
        while index != END:
            x = loopIndex

            if flags[index] & FLAG_VOWEL:
                index = self.phoneme_index[loopIndex + 1]

                if (index != END) and not (flags[index] & FLAG_CONSONANT):
                    if (index == 18) or (index == 19):
                        index = self.phoneme_index[loopIndex + 2]

                        if (index != END) and (flags[index] & FLAG_CONSONANT):
                            self._drule_pre(
                                "<VOWEL> <RX | LX> <CONSONANT> - decrease length of vowel by 1",
                                loopIndex,
                            )
                            self.phoneme_length[loopIndex] = (
                                self.phoneme_length[loopIndex] - 1
                            ) & 0xFF
                            self._drule_post(loopIndex)
                else:
                    flag = 65 if index == END else flags[index]

                    if not (flag & FLAG_VOICED):
                        if flag & FLAG_PLOSIVE:
                            self._drule_pre(
                                "<VOWEL> <UNVOICED PLOSIVE> - decrease vowel by 1/8th",
                                loopIndex,
                            )
                            self.phoneme_length[loopIndex] -= (
                                self.phoneme_length[loopIndex] >> 3
                            )
                            self._drule_post(loopIndex)
                    else:
                        self._drule_pre(
                            "<VOWEL> <VOICED CONSONANT> - increase vowel by 1/2 + 1", x
                        )
                        a = self.phoneme_length[loopIndex]
                        self.phoneme_length[loopIndex] = (a >> 2) + a + 1
                        self._drule_post(loopIndex)
            elif (flags[index] & FLAG_NASAL) != 0:
                x = (x + 1) & 0xFF
                index = self.phoneme_index[x]
                if index != END and (flags[index] & FLAG_STOPCONS):
                    self._drule(
                        "<NASAL> <STOP CONSONANT> - set nasal = 5, consonant = 6"
                    )
                    self.phoneme_length[x] = 6
                    self.phoneme_length[x - 1] = 5
            elif flags[index] & FLAG_STOPCONS:
                x = (x + 1) & 0xFF
                index = self.phoneme_index[x]
                while index == 0:
                    x = (x + 1) & 0xFF
                    index = self.phoneme_index[x]

                if (index != END) and (flags[index] & FLAG_STOPCONS):
                    self._drule(
                        "<UNVOICED STOP CONSONANT> {optional silence} <STOP CONSONANT> - shorten both to 1/2 + 1"
                    )
                    self.phoneme_length[x] = (self.phoneme_length[x] >> 1) + 1
                    self.phoneme_length[loopIndex] = (
                        self.phoneme_length[loopIndex] >> 1
                    ) + 1
                    x = loopIndex
            elif flags[index] & FLAG_LIQUIC:
                index = self.phoneme_index[x - 1]

                self._drule_pre("<LIQUID CONSONANT> <DIPTHONG> - decrease by 2", x)

                self.phoneme_length[x] -= 2
                self._drule_post(x)

            loopIndex = (loopIndex + 1) & 0xFF
            index = self.phoneme_index[loopIndex]

    def process(self, input_phonemes):
        if isinstance(input_phonemes, str):
            input_phonemes = input_phonemes.encode("utf-8")
        elif not isinstance(input_phonemes, (bytes, bytearray)):
            raise Exception("The type of input text must be str, bytes or bytearray.")

        input_phonemes = bytearray(input_phonemes) + bytearray(b"\x9b")

        x = 0

        if not self._parser1(input_phonemes):
            return False

        if self.debug:
            self._print_phonemes()

        self._parser2()
        self._copy_stress()
        self._set_phoneme_length()
        self._adjust_lengths()
        self._code41240()

        flag_loop_init = True
        while (x != 0) or flag_loop_init:
            flag_loop_init = False

            if self.phoneme_index[x] > 80:
                self.phoneme_index[x] = 255
                break

            x += 1

        self._insert_breath()

        if self.debug:
            self._print_phonemes()

        return True


PHONEME_PERIOD = 1
PHONEME_QUESTION = 2

RISING_INFLECTION = 1
FALLING_INFLECTION = 255

tab48426 = b"\x18\x1a\x17\x17\x17"
tab47492 = b"\x00\x00\xe0\xe6\xec\xf3\xf9\x00\x06\x0c\x06"
amplitude_rescale = b"\x00\x01\x02\x02\x02\x03\x03\x04\x04\x05\x06\x08\t\x0b\r\x0f\x00"
blend_rank = b"\x00\x1f\x1f\x1f\x1f\x02\x02\x02\x02\x02\x02\x02\x02\x02\x05\x05\x02\n\x02\x08\x05\x05\x0b\n\t\x08\x08\xa0\x08\x08\x17\x1f\x12\x12\x12\x12\x1e\x1e\x14\x14\x14\x14\x17\x17\x1a\x1a\x1d\x1d\x02\x02\x02\x02\x02\x02\x1a\x1d\x1b\x1a\x1d\x1b\x1a\x1d\x1b\x1a\x1d\x1b\x17\x1d\x17\x17\x1d\x17\x17\x1d\x17\x17\x1d\x17\x17\x17"
out_blend_length = b"\x00\x02\x02\x02\x02\x04\x04\x04\x04\x04\x04\x04\x04\x04\x04\x04\x04\x04\x03\x02\x04\x04\x02\x02\x02\x02\x02\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x02\x02\x02\x01\x00\x01\x00\x01\x00\x05\x05\x05\x05\x05\x04\x04\x02\x00\x01\x02\x00\x01\x02\x00\x01\x02\x00\x01\x02\x00\x02\x02\x00\x01\x03\x00\x02\x03\x00\x02\xa0\xa0"
in_blend_length = b"\x00\x02\x02\x02\x02\x04\x04\x04\x04\x04\x04\x04\x04\x04\x04\x04\x04\x04\x03\x03\x04\x04\x03\x03\x03\x03\x03\x01\x02\x03\x02\x01\x03\x03\x03\x03\x01\x01\x03\x03\x03\x02\x02\x03\x02\x03\x00\x00\x05\x05\x05\x05\x04\x04\x02\x00\x02\x02\x00\x03\x02\x00\x04\x02\x00\x03\x02\x00\x02\x02\x00\x02\x03\x00\x03\x03\x00\x03\xb0\xa0"
sampled_consonant_flags = b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xf1\xe2\xd3\xbb|\x95\x01\x02\x03\x03\x00r\x00\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x1b\x00\x00\x19\x00\x00\x00\x00\x00\x00\x00\x00\x00"
freq3data = b"\x00[[[[n][XYWXRY]>RX>nP]Z<nZnQyey[cjQy]R]gL]eeyey\x00ZXXXXRQQQyyypnn^^^QQQyyyeep^^^\x08\x01"
ampl1data = b"\x00\x00\x00\x00\x00\r\r\x0e\x0f\x0f\x0f\x0f\x0f\x0c\r\x0c\x0f\x0f\r\r\r\x0e\r\x0c\r\r\r\x0c\t\t\x00\x00\x00\x00\x00\x00\x00\x00\x0b\x0b\x0b\x0b\x00\x00\x01\x0b\x00\x02\x0e\x0f\x0f\x0f\x0f\r\x02\x04\x00\x02\x04\x00\x01\x04\x00\x01\x04\x00\x00\x00\x00\x00\x00\x00\x00\x0c\x00\x00\x00\x00\x0f\x0f"
ampl2data = b"\x00\x00\x00\x00\x00\n\x0b\r\x0e\r\x0c\x0c\x0b\t\x0b\x0b\x0c\x0c\x0c\x08\x08\x0c\x08\n\x08\x08\n\x03\t\x06\x00\x00\x00\x00\x00\x00\x00\x00\x03\x05\x03\x04\x00\x00\x00\x05\n\x02\x0e\r\x0c\r\x0c\x08\x00\x01\x00\x00\x01\x00\x00\x01\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\n\x00\x00\n\x00\x00\x00"
ampl3data = b"\x00\x00\x00\x00\x00\x08\x07\x08\x08\x01\x01\x00\x01\x00\x07\x05\x01\x00\x06\x01\x00\x07\x00\x05\x01\x00\x08\x00\x00\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x01\x0e\x01\t\x01\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x07\x00\x00\x05\x00\x13\x10"
sinus = b"\x00\x00\x00\x10\x10\x10\x10\x10\x10      0000000@@@@@@@PPPPPPPP````````````ppppppppppppppppppppppppppppppp````````````PPPPPPPP@@@@@@@0000000      \x10\x10\x10\x10\x10\x10\x00\x00\x00\x00\x00\xf0\xf0\xf0\xf0\xf0\xf0\xe0\xe0\xe0\xe0\xe0\xe0\xd0\xd0\xd0\xd0\xd0\xd0\xd0\xc0\xc0\xc0\xc0\xc0\xc0\xc0\xb0\xb0\xb0\xb0\xb0\xb0\xb0\xb0\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xb0\xb0\xb0\xb0\xb0\xb0\xb0\xb0\xc0\xc0\xc0\xc0\xc0\xc0\xc0\xd0\xd0\xd0\xd0\xd0\xd0\xd0\xe0\xe0\xe0\xe0\xe0\xe0\xf0\xf0\xf0\xf0\xf0\xf0\x00\x00"
rectangle = b"\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90pppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppp"
mult_table = b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x01\x02\x02\x03\x03\x04\x04\x05\x05\x06\x06\x07\x07\x00\x01\x02\x03\x04\x05\x06\x07\x08\t\n\x0b\x0c\r\x0e\x0f\x00\x01\x03\x04\x06\x07\t\n\x0c\r\x0f\x10\x12\x13\x15\x16\x00\x02\x04\x06\x08\n\x0c\x0e\x10\x12\x14\x16\x18\x1a\x1c\x1e\x00\x02\x05\x07\n\x0c\x0f\x11\x14\x16\x19\x1b\x1e #%\x00\x03\x06\t\x0c\x0f\x12\x15\x18\x1b\x1e!$'*-\x00\x03\x07\n\x0e\x11\x15\x18\x1c\x1f#&*-14\x00\xfc\xf8\xf4\xf0\xec\xe8\xe4\xe0\xdc\xd8\xd4\xd0\xcc\xc8\xc4\x00\xfc\xf9\xf5\xf2\xee\xeb\xe7\xe4\xe0\xdd\xd9\xd6\xd2\xcf\xcb\x00\xfd\xfa\xf7\xf4\xf1\xee\xeb\xe8\xe5\xe2\xdf\xdc\xd9\xd6\xd3\x00\xfd\xfb\xf8\xf6\xf3\xf1\xee\xec\xe9\xe7\xe4\xe2\xdf\xdd\xda\x00\xfe\xfc\xfa\xf8\xf6\xf4\xf2\xf0\xee\xec\xea\xe8\xe6\xe4\xe2\x00\xfe\xfd\xfb\xfa\xf8\xf7\xf5\xf4\xf2\xf1\xef\xee\xec\xeb\xe9\x00\xff\xfe\xfd\xfc\xfb\xfa\xf9\xf8\xf7\xf6\xf5\xf4\xf3\xf2\xf1\x00\xff\xff\xfe\xfe\xfd\xfd\xfc\xfc\xfb\xfb\xfa\xfa\xf9\xf9\xf8"
sample_table = b'8\x84k\x19\xc6c\x18\x86s\x98\xc6\xb1\x1c\xca1\x8c\xc71\x88\xc20\x98F1\x18\xc65\x0c\xca1\x0c\xc6!\x10$i\x12\xc21\x14\xc4q\x08J"I\xabj\xa8\xacIQ2\xd5R\x88\x93l\x94"\x15T\xd2%\x96\xd4P\xa5F!\x08\x85k\x18\xc4c\x10\xcek\x18\x8cq\x19\x8cc5\x0c\xc63\x99\xccl\xb5N\xa2\x99F!(\x82\x95.\xe30\x9c\xc50\x9c\xa2\xb1\x9cg1\x88fY,S\x18\x84gP\xca\xe3\n\xac\xab0\xacb0\x8cc\x10\x94b\xb1\x8c\x82(\x963\x98\xd6\xb5Lb)\xa5J\xb5\x9c\xc61\x14\xd68\x9cK\xb4\x86e\x18\xaeg\x1c\xa6c\x19\x96#\x19\x84\x13\x08\xa6R\xac\xca"\x89n\xab\x19\x8cb4\xc4b\x19\x86c\x18\xc4#X\xd6\xa3PBTJ\xadJ%\x11kd\x89Jc9\x8a#1*\xea\xa2\xa9D\xc5\x12\xcdB4\x8cb\x18\x8cc\x11Hf1\x9dD3\x1dF1\x9c\xc6\xb1\x0c\xcd2\x88\xc4s\x18\x86s\x08\xd6cX\x07\x81\xe0\xf0<\x07\x87\x90<|\x0f\xc7\xc0\xc0\xf0|\x1e\x07\x80\x80\x00\x1cxp\xf1\xc7\x1f\xc0\x0c\xfe\x1c\x1f\x1f\x0e\nz\xc0q\xf2\x83\x8f\x03\x0f\x0f\x0c\x00y\xf8a\xe0C\x0f\x83\xe7\x18\xf9\xc1\x13\xda\xe9c\x8f\x0f\x83\x83\x87\xc3\x1f<p\xf0\xe1\xe1\xe3\x87\xb8q\x0e \xe3\x8dHx\x1c\x93\x870\xe1\xc1\xc1\xe4x!\x83\x83\xc3\x87\x069\xe5\xc3\x87\x07\x0e\x1c\x1cp\xf4q\x9c`62\xc3\x1e<\xf3\x8f\x0e<p\xe3\xc7\x8f\x0f\x0f\x0e<x\xf0\xe3\x87\x06\xf0\xe3\x07\xc1\x99\x87\x0f\x18xpp\xfc\xf3\x10\xb1\x8c\x8c1|p\xe1\x86<dl\xb0\xe1\xe3\x0f#\x8f\x0f\x1e>8<8{\x8f\x07\x0e<\xf4\x17\x1e<x\xf2\x9erI\xe3%68X9\xe2\xde<xx\xe1\xc7a\xe1\xe1\xb0\xf0\xf0\xc3\xc7\x0e8\xc0\xf0\xcess\x184\xb0\xe1\xc7\x8e\x1c<\xf88\xf0\xe1\xc1\x8b\x86\x8f\x1cxp\xf0x\xac\xb1\x8f91\xdb8a\xc3\x0e\x0e8xs\x17\x1e9\x1e8d\xe1\xf1\xc1N\x0f@\xa2\x02\xc5\x8f\x81\xa1\xfc\x12\x08d\xe0<"\xe0E\x07\x8e\x0c2\x90\xf0\x1f I\xe0\xf8\x0c`\xf0\x17\x1aA\xaa\xa4\xd0\x8d\x12\x82\x1e\x1e\x03\xf8>\x03\x0cs\x80pD&\x03$\xe1>\x04N\x04\x1c\xc1\t\xcc\x9e\x90!\x07\x90Cd\xc0\x0f\xc6\x90\x9c\xc1[\x03\xe2\x1d\x81\xe0^\x1d\x03\x84\xb8,\x0f\x80\xb1\x83\xe00A\x1eC\x89\x83P\xfc$.\x13\x83\xf1|L,\xc9\r\x83\xb0\xb5\x82\xe4\xe8\x06\x9c\x07\xa0\x99\x1d\x07>\x82\x8fp0t@\xca\x10\xe4\xe8\x0f\x92\x14?\x06\xf8\x84\x88C\x81\n49A\xc6\xe3\x1cG\x03\xb0\xb8\x13\n\xc2d\xf8\x18\xf9`\xb3\xc0e `\xa6\x8c\xc3\x81 0&\x1e\x1c8\xd3\x01\xb0&@\xf4\x0b\xc3B\x1f\x852&`@\xc9\xcb\x01\xec\x11(@\xfa\x044\xe0pL\x8c\x1d\x07i\x03\x16\xc8\x04#\xe8\xc6\x9a\x0b\x1a\x03\xe0v\x06\x05\xcf\x1e\xbcX1qf\x00\xf8?\x04\xfc\x0ct\'\x8a\x80q\xc2:&\x06\xc0\x1f\x05\x0f\x98@\xae\x01\x7f\xc0\x07\xff\x00\x0e\xfe\x00\x03\xdf\x80\x03\xef\x80\x1b\xf1\xc2\x00\xe7\xe0\x18\xfc\xe0!\xfc\x80<\xfc@\x0e~\x00?>\x00\x0f\xfe\x00\x1f\xff\x00>\xf0\x07\xfc\x00~\x10?\xff\x00?8\x0e|\x01\x87\x0c\xfc\xc7\x00>\x04\x0f>\x1f\x0f\x0f\x1f\x0f\x02\x83\x87\xcf\x03\x87\x0f?\xc0\x07\x9e`?\xc0\x03\xfe\x00?\xe0w\xe1\xc0\xfe\xe0\xc3\xe0\x01\xdf\xf8\x03\x07\x00~p\x00|8\x18\xfe\x0c\x1ex\x1c|>\x0e\x1f\x1e\x1e>\x00\x7f\x83\x07\xdb\x87\x83\x07\xc7\x07\x10q\xff\x00?\xe2\x01\xe0\xc1\xc3\xe1\x00\x7f\xc0\x05\xf0 \xf8\xf0p\xfexy\xf8\x02?\x0c\x8f\x03\x0f\x9f\xe0\xc1\xc7\x87\x03\xc3\xc3\xb0\xe1\xe1\xc1\xe3\xe0q\xf0\x00\xfcp|\x0c>8\x0e\x1cp\xc3\xc7\x03\x81\xc1\xc7\xe7\x00\x0f\xc7\x87\x19\t\xef\xc43\xe0\xc1\xfc\xf8p\xf0x\xf8\xf0a\xc7\x00\x1f\xf8\x01|\xf8\xf0xp<|\xce\x0e!\x83\xcf\x08\x07\x8f\x08\xc1\x87\x8f\x80\xc7\xe3\x00\x07\xf8\xe0\xef\x009\xf7\x80\x0e\xf8\xe1\xe3\xf8!\x9f\xc0\xff\x03\xf8\x07\xc0\x1f\xf8\xc4\x04\xfc\xc4\xc1\xbc\x87\xf0\x0f\xc0\x7f\x05\xe0%\xec\xc0>\x84G\xf0\x8e\x03\xf8\x03\xfb\xc0\x19\xf8\x07\x9c\x0c\x17\xf8\x07\xe0\x1f\xa1\xfc\x0f\xfc\x01\xf0?\x00\xfe\x03\xf0\x1f\x00\xfd\x00\xff\x88\r\xf9\x01\xff\x00p\x07\xc0>B\xf3\r\xc4\x7f\x80\xfc\x07\xf0^\xc0?\x00x?\x81\xff\x01\xf8\x01\xc3\xe8\x0c\xe4d\x8f\xe4\x0f\xf0\x07\xf0\xc2\x1f\x00\x7f\xc0o\x80~\x03\xf8\x07\xf0?\xc0x\x0f\x82\x07\xfe"wp\x02v\x03\xfe\x00\xfeg\x00|\xc7\xf1\x8e\xc6;\xe0?\x84\xf3\x19\xd8\x03\x99\xfc\t\xb8\x0f\xf8\x00\x9d$a\xf9\r\x00\xfd\x03\xf0\x1f\x90?\x01\xf8\x1f\xd0\x0f\xf87\x01\xf8\x07\xf0\x0f\xc0?\x00\xfe\x03\xf8\x0f\xc0?\x00\xfa\x03\xf0\x0f\x80\xff\x01\xb8\x07\xf0\x01\xfc\x01\xbc\x80\x13\x1e\x00\x7f\xe1@\x7f\xa0\x7f\xb0\x00?\xc0\x1f\xc08\x0f\xf0\x1f\x80\xff\x01\xfc\x03\xf1~\x01\xfe\x01\xf0\xff\x00\x7f\xc0\x1d\x07\xf0\x0f\xc0~\x06\xe0\x07\xe0\x0f\xf8\x06\xc1\xfe\x01\xfc\x03\xe0\x0f\x00\xfc'

time_table = [
    b"\xa2\xa7\xa7\x7f\x80",
    b"\xe2<<\x00\x00",
    b"\xe1<;\x00\x00",
    b"\xc8\x00\x0067",
    b"\xc7\x00\x0066",
]

mouth_formants_5_29 = b"\x00\x00\x00\x00\x00\n\x0e\x13\x18\x1b\x17\x15\x10\x14\x0e\x12\x0e\x12\x12\x10\r\x0f\x0b\x12\x0e\x0b\t\x06\x06\x06"
throat_formants_5_29 = (
    b"\xff\xff\xff\xff\xffTIC?(,\x1f%-I1$\x1e3%\x1dE\x182\x1e\x18S.6V"
)
mouth_formants_48_53 = b"\x13\x1b\x15\x1b\x12\r"
throat_formants_48_53 = b"H'\x1f+\x1e\""


class Renderer:
    def __init__(
        self,
        speed=72,
        pitch=64,
        mouth=128,
        throat=128,
        sing_mode=False,
        buffer_size=220500,
        debug=False,
    ):
        self.speed = speed
        self.pitch = pitch
        self.mouth = mouth
        self.throat = throat
        self.sing_mode = sing_mode

        self.buffer_size = buffer_size
        self.debug = debug

        self.freq1data = bytearray(
            [
                0x00, 0x13, 0x13, 0x13, 0x13, 0x0a, 0x0e, 0x12,
                0x18, 0x1a, 0x16, 0x14, 0x10, 0x14, 0x0e, 0x12,
                0x0e, 0x12, 0x12, 0x10, 0x0c, 0x0e, 0x0a, 0x12,
                0x0e, 0x0a, 0x08, 0x06, 0x06, 0x06, 0x06, 0x11,
                0x06, 0x06, 0x06, 0x06, 0x0e, 0x10, 0x09, 0x0a,
                0x08, 0x0a, 0x06, 0x06, 0x06, 0x05, 0x06, 0x00,
                0x12, 0x1a, 0x14, 0x1a, 0x12, 0x0c, 0x06, 0x06,
                0x06, 0x06, 0x06, 0x06, 0x06, 0x06, 0x06, 0x06,
                0x06, 0x06, 0x06, 0x06, 0x06, 0x06, 0x06, 0x06,
                0x06, 0x0a, 0x0a, 0x06, 0x06, 0x06, 0x2c, 0x13,
            ]
        )

        self.freq2data = bytearray(
            [
                0x00, 0x43, 0x43, 0x43, 0x43, 0x54, 0x48, 0x42,
                0x3e, 0x28, 0x2c, 0x1e, 0x24, 0x2c, 0x48, 0x30,
                0x24, 0x1e, 0x32, 0x24, 0x1c, 0x44, 0x18, 0x32,
                0x1e, 0x18, 0x52, 0x2e, 0x36, 0x56, 0x36, 0x43,
                0x49, 0x4f, 0x1a, 0x42, 0x49, 0x25, 0x33, 0x42,
                0x28, 0x2f, 0x4f, 0x4f, 0x42, 0x4f, 0x6e, 0x00,
                0x48, 0x26, 0x1e, 0x2a, 0x1e, 0x22, 0x1a, 0x1a,
                0x1a, 0x42, 0x42, 0x42, 0x6e, 0x6e, 0x6e, 0x54,
                0x54, 0x54, 0x1a, 0x1a, 0x1a, 0x42, 0x42, 0x42,
                0x6d, 0x56, 0x6d, 0x54, 0x54, 0x54, 0x7f, 0x7f,
            ]
        )

        self.phoneme_index_output = bytearray(60)
        self.stress_output = bytearray(60)
        self.phoneme_length_output = bytearray(60)

        self.pitches = bytearray(256)

        self.frequency1 = bytearray(256)
        self.frequency2 = bytearray(256)
        self.frequency3 = bytearray(256)

        self.amplitude1 = bytearray(256)
        self.amplitude2 = bytearray(256)
        self.amplitude3 = bytearray(256)

        self.sampled_consonant_flag = bytearray(256)

        self.old_time_table_index = 0

        self.buffer_pos = 0
        self.buffer = bytearray(self.buffer_size)
        self.buffer_end = 0

        self.config()

    def _print_output(self, flag, f1, f2, f3, a1, a2, a3, p):
        print("===========================================")
        print("Final data for speech output:\n")
        print(" flags ampl1 freq1 ampl2 freq2 ampl3 freq3 pitch")
        print("------------------------------------------------")
        i = 0
        while i < 255:
            print(
                f"{flag[i]:5} {a1[i]:5} {f1[i]:5} {a2[i]:5} {f2[i]:5} {a3[i]:5} {f3[i]:5} {p[i]:5}"
            )
            i += 1
        print("===========================================")

    def _add_inflection(self, inflection, pos):
        end = pos

        if pos < 30:
            pos = 0
        else:
            pos -= 30

        a = self.pitches[pos]
        while a == 127:
            pos = (pos + 1) & 0xFF
            a = self.pitches[pos]

        while pos != end:
            a = (a + inflection) & 0xFF

            self.pitches[pos] = a

            pos = (pos + 1) & 0xFF
            while (pos != end) and (self.pitches[pos] == 255):
                pos = (pos + 1) & 0xFF

    def _assign_pitch_contour(self):
        for i in range(256):
            self.pitches[i] = (self.pitches[i] - (self.frequency1[i] >> 1)) & 0xFF

    def _rescale_amplitude(self):
        for i in range(255, -1, -1):
            self.amplitude1[i] = amplitude_rescale[self.amplitude1[i]]
            self.amplitude2[i] = amplitude_rescale[self.amplitude2[i]]
            self.amplitude3[i] = amplitude_rescale[self.amplitude3[i]]

    def _create_frames(self):
        x = 0
        for i in range(256):
            phoneme = self.phoneme_index_output[i]

            if phoneme == 255:
                break

            if phoneme == PHONEME_PERIOD:
                self._add_inflection(RISING_INFLECTION, x)
            elif phoneme == PHONEME_QUESTION:
                self._add_inflection(FALLING_INFLECTION, x)

            temp_stress = self.stress_output[i] + 1
            temp_stress = (
                len(tab47492) - 1 if temp_stress >= len(tab47492) else temp_stress
            )
            phase1 = tab47492[temp_stress]

            phase2 = self.phoneme_length_output[i]

            flag_loop_init = True
            while (phase2 != 0) or flag_loop_init:
                flag_loop_init = False

                self.frequency1[x] = self.freq1data[phoneme]
                self.frequency2[x] = self.freq2data[phoneme]
                self.frequency3[x] = freq3data[phoneme]
                self.amplitude1[x] = ampl1data[phoneme]
                self.amplitude2[x] = ampl2data[phoneme]
                self.amplitude3[x] = ampl3data[phoneme]
                self.sampled_consonant_flag[x] = sampled_consonant_flags[phoneme]
                self.pitches[x] = (self.pitch + phase1) & 0xFF
                x += 1
                phase2 -= 1

    def _output(self, index, a):
        self.buffer_pos += time_table[self.old_time_table_index][index]
        self.old_time_table_index = index

        self.buffer_end = self.buffer_pos // 50
        for k in range(5):
            self.buffer[self.buffer_end + k] = (a & 15) * 16

    def _render_voiced_sample(self, hi, off, phase1):
        flag_loop_init_1 = True
        while (phase1 != 0) or flag_loop_init_1:
            flag_loop_init_1 = False

            bit = 8
            sample = sample_table[hi + off]

            flag_loop_init_2 = True
            while (bit != 0) or flag_loop_init_2:
                flag_loop_init_2 = False

                if (sample & 128) != 0:
                    self._output(3, 26)
                else:
                    self._output(4, 6)

                sample = (sample << 1) & 0xFF
                bit = (bit - 1) & 0xFF

            off = (off + 1) & 0xFF
            phase1 = (phase1 + 1) & 0xFF

        return off

    def _render_unvoiced_sample(self, hi, off, m):
        flag_loop_init_1 = True
        while (off != 0) or flag_loop_init_1:
            flag_loop_init_1 = False

            bit = 8
            sample = sample_table[hi + off]

            flag_loop_init_2 = True
            while (bit != 0) or flag_loop_init_2:
                flag_loop_init_2 = False

                if (sample & 128) != 0:
                    self._output(2, 5)
                else:
                    self._output(1, m)

                sample = (sample << 1) & 0xFF
                bit = (bit - 1) & 0xFF

            off = (off + 1) & 0xFF

    def _render_sample(self, m, consonant_flag, n):
        hibyte = ((consonant_flag & 7) - 1) & 0xFF

        hi = hibyte * 256
        pitchl = consonant_flag & 248
        if pitchl == 0:
            pitchl = self.pitches[n] >> 4
            m[0] = self._render_voiced_sample(hi, m[0], pitchl ^ 255)
        else:
            self._render_unvoiced_sample(hi, pitchl ^ 255, tab48426[hibyte])

    def _combine_glottal_and_formants(self, phase1, phase2, phase3, y):
        tmp = mult_table[sinus[phase1] | self.amplitude1[y]]
        tmp += mult_table[sinus[phase2] | self.amplitude2[y]]
        tmp += 1 if tmp > 255 else 0
        tmp += mult_table[rectangle[phase3] | self.amplitude3[y]]
        tmp += 136
        tmp >>= 4

        self._output(0, tmp & 0xF)

    def _process_frames(self, k):
        speedcounter = 72
        phase1 = 0
        phase2 = 0
        phase3 = 0
        m = bytearray(1)

        y = 0

        glottal_pulse = self.pitches[0]
        n = glottal_pulse - (glottal_pulse >> 2)

        while k:
            flags = self.sampled_consonant_flag[y]

            if flags & 248:
                self._render_sample(m, flags, y)
                y = (y + 2) & 0xFF
                k = (k - 2) & 0xFF
                speedcounter = self.speed
            else:
                self._combine_glottal_and_formants(phase1, phase2, phase3, y)

                speedcounter = (speedcounter - 1) & 0xFF
                if speedcounter == 0:
                    y = (y + 1) & 0xFF
                    k = (k - 1) & 0xFF
                    if k == 0:
                        return

                    speedcounter = self.speed

                glottal_pulse = (glottal_pulse - 1) & 0xFF

                if glottal_pulse != 0:

                    n = (n - 1) & 0xFF
                    if (n != 0) or (flags == 0):
                        phase1 = (phase1 + self.frequency1[y]) & 0xFF
                        phase2 = (phase2 + self.frequency2[y]) & 0xFF
                        phase3 = (phase3 + self.frequency3[y]) & 0xFF
                        continue

                    self._render_sample(m, flags, y)

            glottal_pulse = self.pitches[y]
            n = glottal_pulse - (glottal_pulse >> 2)

            phase1 = 0
            phase2 = 0
            phase3 = 0

    def _read(self, p, y):
        if p == 168:
            return self.pitches[y]
        elif p == 169:
            return self.frequency1[y]
        elif p == 170:
            return self.frequency2[y]
        elif p == 171:
            return self.frequency3[y]
        elif p == 172:
            return self.amplitude1[y]
        elif p == 173:
            return self.amplitude2[y]
        elif p == 174:
            return self.amplitude3[y]

        print("Error reading to tables")
        return 0

    def _write(self, p, y, value):
        if p == 168:
            self.pitches[y] = value
        elif p == 169:
            self.frequency1[y] = value
        elif p == 170:
            self.frequency2[y] = value
        elif p == 171:
            self.frequency3[y] = value
        elif p == 172:
            self.amplitude1[y] = value
        elif p == 173:
            self.amplitude2[y] = value
        elif p == 174:
            self.amplitude3[y] = value
        else:
            print("Error writing to tables")

    def _interpolate(self, width, table, frame, m):
        sign = m < 0
        remainder = abs(m) % width
        div = int(m / width) & 0xFF

        error = 0
        pos = width
        val = (self._read(table, frame) + div) & 0xFF

        pos = (pos - 1) & 0xFF
        while pos:
            error = (error + remainder) & 0xFF
            if error >= width:
                error = (error - width) & 0xFF
                if sign:
                    val = (val - 1) & 0xFF
                elif val:
                    val = (val + 1) & 0xFF

            frame = (frame + 1) & 0xFF
            self._write(table, frame, val)
            val = (val + div) & 0xFF

            pos = (pos - 1) & 0xFF

    def _interpolate_pitch(self, pos, m, phase3):
        cur_width = self.phoneme_length_output[pos] // 2
        next_width = self.phoneme_length_output[pos + 1] // 2
        width = (cur_width + next_width) & 0xFF
        pitch = self.pitches[next_width + m] - self.pitches[m - cur_width]
        self._interpolate(width, 168, phase3, pitch)

    def _create_transitions(self):
        m = 0
        pos = 0
        while True:
            phoneme = self.phoneme_index_output[pos]
            next_phoneme = self.phoneme_index_output[pos + 1]

            if next_phoneme == 255:
                break

            next_rank = blend_rank[next_phoneme]
            rank = blend_rank[phoneme]

            if rank == next_rank:
                phase1 = out_blend_length[phoneme]
                phase2 = out_blend_length[next_phoneme]
            elif rank < next_rank:
                phase1 = in_blend_length[next_phoneme]
                phase2 = out_blend_length[next_phoneme]
            else:
                phase1 = out_blend_length[phoneme]
                phase2 = in_blend_length[phoneme]

            m = (m + self.phoneme_length_output[pos]) & 0xFF

            speedcounter = (m + phase2) & 0xFF
            phase3 = (m - phase1) & 0xFF
            transition = (phase1 + phase2) & 0xFF

            if (((transition - 2) & 0xFF) & 128) == 0:
                table = 169
                self._interpolate_pitch(pos, m, phase3)
                while table < 175:

                    value = self._read(table, speedcounter) - self._read(table, phase3)
                    self._interpolate(transition, table, phase3, value)

                    table = (table + 1) & 0xFF

            pos = (pos + 1) & 0xFF

        return (m + self.phoneme_length_output[pos]) & 0xFF

    def _render_batch(self):
        if self.phoneme_index_output[0] == 255:
            return

        self._create_frames()
        t = self._create_transitions()

        if not self.sing_mode:
            self._assign_pitch_contour()

        self._rescale_amplitude()

        if self.debug:
            self._print_output(
                self.sampled_consonant_flag,
                self.frequency1,
                self.frequency2,
                self.frequency3,
                self.amplitude1,
                self.amplitude2,
                self.amplitude3,
                self.pitches,
            )

        self._process_frames(t)

    def _trans(self, a, b):
        return (((a * b) >> 8) << 1) & 0xFF

    def config(
        self,
        speed=None,
        pitch=None,
        mouth=None,
        throat=None,
        sing_mode=None,
    ):
        if speed is not None:
            self.speed = speed
        if pitch is not None:
            self.pitch = pitch
        if mouth is not None:
            self.mouth = mouth
        if throat is not None:
            self.throat = throat
        if sing_mode is not None:
            self.sing_mode = sing_mode

        new_frequency = 0

        pos = 5
        while pos != 30:
            initial_frequency = mouth_formants_5_29[pos]
            if initial_frequency != 0:
                new_frequency = self._trans(self.mouth, initial_frequency)

            self.freq1data[pos] = new_frequency

            initial_frequency = throat_formants_5_29[pos]
            if initial_frequency != 0:
                new_frequency = self._trans(self.throat, initial_frequency)

            self.freq2data[pos] = new_frequency

            pos += 1

        pos = 0
        while pos < 6:
            initial_frequency = mouth_formants_48_53[pos]
            new_frequency = self._trans(self.mouth, initial_frequency)
            self.freq1data[pos + 48] = new_frequency

            initial_frequency = throat_formants_48_53[pos]
            new_frequency = self._trans(self.throat, initial_frequency)
            self.freq2data[pos + 48] = new_frequency

            pos += 1

    def render(
        self,
        processor,
    ):
        self.buffer_end = self.buffer_pos = 0
        srcpos = 0
        destpos = 0

        while True:
            A = processor.phoneme_index[srcpos]
            self.phoneme_index_output[destpos] = A

            if A == 255:
                self._render_batch()
                return True
            elif A == 254:
                self.phoneme_index_output[destpos] = 255
                self._render_batch()
                destpos = 0
            elif A == 0:
                pass
            else:
                self.phoneme_length_output[destpos] = processor.phoneme_length[srcpos]
                self.stress_output[destpos] = processor.stress[srcpos]
                destpos = (destpos + 1) & 0xFF

            srcpos = (srcpos + 1) & 0xFF
