'''
eand.py package (Easy Algebraic Numerical Differentiation for Python)
Copyright (C) 2013 Tu-Hoa Pham

This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <http://www.gnu.org/licenses/>.
'''

class DerivativesGxy():
    '''
    Partial derivatives of Gxy for (many) parameter combinations
    '''
    n1Max = 2
    alpha1Max = 4
    beta1Max = 4
    n2Max = 2
    alpha2Max = 4
    beta2Max = 4
    a = 0
    b = 0
    c = 0
    d = 0
    
    def __init__(self,halfWindowVec,case):
        '''
        Initialization of method partialGxy in function of the parameter combination number
        once and for all to avoid repeated tests
        '''
        self.a = -halfWindowVec[0]
        self.b = halfWindowVec[0]
        if len(halfWindowVec) >= 2:
            self.c = -halfWindowVec[1]
            self.d = halfWindowVec[1]
        self.partialGxy = getattr(self,'partialGxy%d' % case)
    
    

    def partialGxy0(self,coord):

        return 1

    def partialGxy1(self,coord):

        return -coord[1]+self.c

    def partialGxy2(self,coord):

        return (-coord[1]+self.c)^2

    def partialGxy3(self,coord):

        return (-coord[1]+self.c)^3

    def partialGxy4(self,coord):

        return (-coord[1]+self.c)^4

    def partialGxy5(self,coord):

        return -coord[1]+self.d

    def partialGxy6(self,coord):

        return (-coord[1]+self.c)*(-coord[1]+self.d)

    def partialGxy7(self,coord):

        return (-coord[1]+self.c)^2*(-coord[1]+self.d)

    def partialGxy8(self,coord):

        return (-coord[1]+self.c)^3*(-coord[1]+self.d)

    def partialGxy9(self,coord):

        return (-coord[1]+self.c)^4*(-coord[1]+self.d)

    def partialGxy10(self,coord):

        return (-coord[1]+self.d)^2

    def partialGxy11(self,coord):

        return (-coord[1]+self.c)*(-coord[1]+self.d)^2

    def partialGxy12(self,coord):

        return (-coord[1]+self.c)^2*(-coord[1]+self.d)^2

    def partialGxy13(self,coord):

        return (-coord[1]+self.c)^3*(-coord[1]+self.d)^2

    def partialGxy14(self,coord):

        return (-coord[1]+self.c)^4*(-coord[1]+self.d)^2

    def partialGxy15(self,coord):

        return (-coord[1]+self.d)^3

    def partialGxy16(self,coord):

        return (-coord[1]+self.c)*(-coord[1]+self.d)^3

    def partialGxy17(self,coord):

        return (-coord[1]+self.c)^2*(-coord[1]+self.d)^3

    def partialGxy18(self,coord):

        return (-coord[1]+self.c)^3*(-coord[1]+self.d)^3

    def partialGxy19(self,coord):

        return (-coord[1]+self.c)^4*(-coord[1]+self.d)^3

    def partialGxy20(self,coord):

        return (-coord[1]+self.d)^4

    def partialGxy21(self,coord):

        return (-coord[1]+self.c)*(-coord[1]+self.d)^4

    def partialGxy22(self,coord):

        return (-coord[1]+self.c)^2*(-coord[1]+self.d)^4

    def partialGxy23(self,coord):

        return (-coord[1]+self.c)^3*(-coord[1]+self.d)^4

    def partialGxy24(self,coord):

        return (-coord[1]+self.c)^4*(-coord[1]+self.d)^4

    def partialGxy31(self,coord):

        return -2*coord[1]+self.c+self.d

    def partialGxy32(self,coord):

        return (-coord[1]+self.c)^2+2*(-coord[1]+self.c)*(-coord[1]+self.d)

    def partialGxy33(self,coord):

        return (-coord[1]+self.c)^3+3*(-coord[1]+self.c)^2*(-coord[1]+self.d)

    def partialGxy34(self,coord):

        return (-coord[1]+self.c)^4+4*(-coord[1]+self.c)^3*(-coord[1]+self.d)

    def partialGxy36(self,coord):

        return 2*(-coord[1]+self.c)*(-coord[1]+self.d)+(-coord[1]+self.d)^2

    def partialGxy37(self,coord):

        return 2*(-coord[1]+self.c)^2*(-coord[1]+self.d)+2*(-coord[1]+self.c)*(-coord[1]+self.d)^2

    def partialGxy38(self,coord):

        return 2*(-coord[1]+self.c)^3*(-coord[1]+self.d)+3*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2

    def partialGxy39(self,coord):

        return 2*(-coord[1]+self.c)^4*(-coord[1]+self.d)+4*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2

    def partialGxy41(self,coord):

        return 3*(-coord[1]+self.c)*(-coord[1]+self.d)^2+(-coord[1]+self.d)^3

    def partialGxy42(self,coord):

        return 3*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2+2*(-coord[1]+self.c)*(-coord[1]+self.d)^3

    def partialGxy43(self,coord):

        return 3*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2+3*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3

    def partialGxy44(self,coord):

        return 3*(-coord[1]+self.c)^4*(-coord[1]+self.d)^2+4*(-coord[1]+self.c)^3*(-coord[1]+self.d)^3

    def partialGxy46(self,coord):

        return 4*(-coord[1]+self.c)*(-coord[1]+self.d)^3+(-coord[1]+self.d)^4

    def partialGxy47(self,coord):

        return 4*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3+2*(-coord[1]+self.c)*(-coord[1]+self.d)^4

    def partialGxy48(self,coord):

        return 4*(-coord[1]+self.c)^3*(-coord[1]+self.d)^3+3*(-coord[1]+self.c)^2*(-coord[1]+self.d)^4

    def partialGxy49(self,coord):

        return 4*(-coord[1]+self.c)^4*(-coord[1]+self.d)^3+4*(-coord[1]+self.c)^3*(-coord[1]+self.d)^4

    def partialGxy62(self,coord):

        return 2*(-coord[1]+self.c)^2+8*(-coord[1]+self.c)*(-coord[1]+self.d)+2*(-coord[1]+self.d)^2

    def partialGxy63(self,coord):

        return 2*(-coord[1]+self.c)^3+12*(-coord[1]+self.c)^2*(-coord[1]+self.d)+6*(-coord[1]+self.c)*(-coord[1]+self.d)^2

    def partialGxy64(self,coord):

        return 2*(-coord[1]+self.c)^4+16*(-coord[1]+self.c)^3*(-coord[1]+self.d)+12*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2

    def partialGxy67(self,coord):

        return 6*(-coord[1]+self.c)^2*(-coord[1]+self.d)+12*(-coord[1]+self.c)*(-coord[1]+self.d)^2+2*(-coord[1]+self.d)^3

    def partialGxy68(self,coord):

        return 6*(-coord[1]+self.c)^3*(-coord[1]+self.d)+18*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2+6*(-coord[1]+self.c)*(-coord[1]+self.d)^3

    def partialGxy69(self,coord):

        return 6*(-coord[1]+self.c)^4*(-coord[1]+self.d)+24*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2+12*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3

    def partialGxy72(self,coord):

        return 12*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2+16*(-coord[1]+self.c)*(-coord[1]+self.d)^3+2*(-coord[1]+self.d)^4

    def partialGxy73(self,coord):

        return 12*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2+24*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3+6*(-coord[1]+self.c)*(-coord[1]+self.d)^4

    def partialGxy74(self,coord):

        return 12*(-coord[1]+self.c)^4*(-coord[1]+self.d)^2+32*(-coord[1]+self.c)^3*(-coord[1]+self.d)^3+12*(-coord[1]+self.c)^2*(-coord[1]+self.d)^4

    def partialGxy75(self,coord):

        return -coord[0]+self.a

    def partialGxy76(self,coord):

        return (-coord[0]+self.a)*(-coord[1]+self.c)

    def partialGxy77(self,coord):

        return (-coord[0]+self.a)*(-coord[1]+self.c)^2

    def partialGxy78(self,coord):

        return (-coord[0]+self.a)*(-coord[1]+self.c)^3

    def partialGxy79(self,coord):

        return (-coord[0]+self.a)*(-coord[1]+self.c)^4

    def partialGxy80(self,coord):

        return (-coord[0]+self.a)*(-coord[1]+self.d)

    def partialGxy81(self,coord):

        return (-coord[0]+self.a)*(-coord[1]+self.c)*(-coord[1]+self.d)

    def partialGxy82(self,coord):

        return (-coord[0]+self.a)*(-coord[1]+self.c)^2*(-coord[1]+self.d)

    def partialGxy83(self,coord):

        return (-coord[0]+self.a)*(-coord[1]+self.c)^3*(-coord[1]+self.d)

    def partialGxy84(self,coord):

        return (-coord[0]+self.a)*(-coord[1]+self.c)^4*(-coord[1]+self.d)

    def partialGxy85(self,coord):

        return (-coord[0]+self.a)*(-coord[1]+self.d)^2

    def partialGxy86(self,coord):

        return (-coord[0]+self.a)*(-coord[1]+self.c)*(-coord[1]+self.d)^2

    def partialGxy87(self,coord):

        return (-coord[0]+self.a)*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2

    def partialGxy88(self,coord):

        return (-coord[0]+self.a)*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2

    def partialGxy89(self,coord):

        return (-coord[0]+self.a)*(-coord[1]+self.c)^4*(-coord[1]+self.d)^2

    def partialGxy90(self,coord):

        return (-coord[0]+self.a)*(-coord[1]+self.d)^3

    def partialGxy91(self,coord):

        return (-coord[0]+self.a)*(-coord[1]+self.c)*(-coord[1]+self.d)^3

    def partialGxy92(self,coord):

        return (-coord[0]+self.a)*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3

    def partialGxy93(self,coord):

        return (-coord[0]+self.a)*(-coord[1]+self.c)^3*(-coord[1]+self.d)^3

    def partialGxy94(self,coord):

        return (-coord[0]+self.a)*(-coord[1]+self.c)^4*(-coord[1]+self.d)^3

    def partialGxy95(self,coord):

        return (-coord[0]+self.a)*(-coord[1]+self.d)^4

    def partialGxy96(self,coord):

        return (-coord[0]+self.a)*(-coord[1]+self.c)*(-coord[1]+self.d)^4

    def partialGxy97(self,coord):

        return (-coord[0]+self.a)*(-coord[1]+self.c)^2*(-coord[1]+self.d)^4

    def partialGxy98(self,coord):

        return (-coord[0]+self.a)*(-coord[1]+self.c)^3*(-coord[1]+self.d)^4

    def partialGxy99(self,coord):

        return (-coord[0]+self.a)*(-coord[1]+self.c)^4*(-coord[1]+self.d)^4

    def partialGxy106(self,coord):

        return (-coord[0]+self.a)*(-coord[1]+self.c)+(-coord[0]+self.a)*(-coord[1]+self.d)

    def partialGxy107(self,coord):

        return (-coord[0]+self.a)*(-coord[1]+self.c)^2+2*(-coord[0]+self.a)*(-coord[1]+self.c)*(-coord[1]+self.d)

    def partialGxy108(self,coord):

        return (-coord[0]+self.a)*(-coord[1]+self.c)^3+3*(-coord[0]+self.a)*(-coord[1]+self.c)^2*(-coord[1]+self.d)

    def partialGxy109(self,coord):

        return (-coord[0]+self.a)*(-coord[1]+self.c)^4+4*(-coord[0]+self.a)*(-coord[1]+self.c)^3*(-coord[1]+self.d)

    def partialGxy111(self,coord):

        return 2*(-coord[0]+self.a)*(-coord[1]+self.c)*(-coord[1]+self.d)+(-coord[0]+self.a)*(-coord[1]+self.d)^2

    def partialGxy112(self,coord):

        return 2*(-coord[0]+self.a)*(-coord[1]+self.c)^2*(-coord[1]+self.d)+2*(-coord[0]+self.a)*(-coord[1]+self.c)*(-coord[1]+self.d)^2

    def partialGxy113(self,coord):

        return 2*(-coord[0]+self.a)*(-coord[1]+self.c)^3*(-coord[1]+self.d)+3*(-coord[0]+self.a)*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2

    def partialGxy114(self,coord):

        return 2*(-coord[0]+self.a)*(-coord[1]+self.c)^4*(-coord[1]+self.d)+4*(-coord[0]+self.a)*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2

    def partialGxy116(self,coord):

        return 3*(-coord[0]+self.a)*(-coord[1]+self.c)*(-coord[1]+self.d)^2+(-coord[0]+self.a)*(-coord[1]+self.d)^3

    def partialGxy117(self,coord):

        return 3*(-coord[0]+self.a)*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2+2*(-coord[0]+self.a)*(-coord[1]+self.c)*(-coord[1]+self.d)^3

    def partialGxy118(self,coord):

        return 3*(-coord[0]+self.a)*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2+3*(-coord[0]+self.a)*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3

    def partialGxy119(self,coord):

        return 3*(-coord[0]+self.a)*(-coord[1]+self.c)^4*(-coord[1]+self.d)^2+4*(-coord[0]+self.a)*(-coord[1]+self.c)^3*(-coord[1]+self.d)^3

    def partialGxy121(self,coord):

        return 4*(-coord[0]+self.a)*(-coord[1]+self.c)*(-coord[1]+self.d)^3+(-coord[0]+self.a)*(-coord[1]+self.d)^4

    def partialGxy122(self,coord):

        return 4*(-coord[0]+self.a)*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3+2*(-coord[0]+self.a)*(-coord[1]+self.c)*(-coord[1]+self.d)^4

    def partialGxy123(self,coord):

        return 4*(-coord[0]+self.a)*(-coord[1]+self.c)^3*(-coord[1]+self.d)^3+3*(-coord[0]+self.a)*(-coord[1]+self.c)^2*(-coord[1]+self.d)^4

    def partialGxy124(self,coord):

        return 4*(-coord[0]+self.a)*(-coord[1]+self.c)^4*(-coord[1]+self.d)^3+4*(-coord[0]+self.a)*(-coord[1]+self.c)^3*(-coord[1]+self.d)^4

    def partialGxy137(self,coord):

        return 2*(-coord[0]+self.a)*(-coord[1]+self.c)^2+8*(-coord[0]+self.a)*(-coord[1]+self.c)*(-coord[1]+self.d)+2*(-coord[0]+self.a)*(-coord[1]+self.d)^2

    def partialGxy138(self,coord):

        return 2*(-coord[0]+self.a)*(-coord[1]+self.c)^3+12*(-coord[0]+self.a)*(-coord[1]+self.c)^2*(-coord[1]+self.d)+6*(-coord[0]+self.a)*(-coord[1]+self.c)*(-coord[1]+self.d)^2

    def partialGxy139(self,coord):

        return 2*(-coord[0]+self.a)*(-coord[1]+self.c)^4+16*(-coord[0]+self.a)*(-coord[1]+self.c)^3*(-coord[1]+self.d)+12*(-coord[0]+self.a)*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2

    def partialGxy142(self,coord):

        return 6*(-coord[0]+self.a)*(-coord[1]+self.c)^2*(-coord[1]+self.d)+12*(-coord[0]+self.a)*(-coord[1]+self.c)*(-coord[1]+self.d)^2+2*(-coord[0]+self.a)*(-coord[1]+self.d)^3

    def partialGxy143(self,coord):

        return 6*(-coord[0]+self.a)*(-coord[1]+self.c)^3*(-coord[1]+self.d)+18*(-coord[0]+self.a)*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2+6*(-coord[0]+self.a)*(-coord[1]+self.c)*(-coord[1]+self.d)^3

    def partialGxy144(self,coord):

        return 6*(-coord[0]+self.a)*(-coord[1]+self.c)^4*(-coord[1]+self.d)+24*(-coord[0]+self.a)*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2+12*(-coord[0]+self.a)*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3

    def partialGxy147(self,coord):

        return 12*(-coord[0]+self.a)*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2+16*(-coord[0]+self.a)*(-coord[1]+self.c)*(-coord[1]+self.d)^3+2*(-coord[0]+self.a)*(-coord[1]+self.d)^4

    def partialGxy148(self,coord):

        return 12*(-coord[0]+self.a)*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2+24*(-coord[0]+self.a)*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3+6*(-coord[0]+self.a)*(-coord[1]+self.c)*(-coord[1]+self.d)^4

    def partialGxy149(self,coord):

        return 12*(-coord[0]+self.a)*(-coord[1]+self.c)^4*(-coord[1]+self.d)^2+32*(-coord[0]+self.a)*(-coord[1]+self.c)^3*(-coord[1]+self.d)^3+12*(-coord[0]+self.a)*(-coord[1]+self.c)^2*(-coord[1]+self.d)^4

    def partialGxy150(self,coord):

        return (-coord[0]+self.a)^2

    def partialGxy151(self,coord):

        return (-coord[0]+self.a)^2*(-coord[1]+self.c)

    def partialGxy152(self,coord):

        return (-coord[0]+self.a)^2*(-coord[1]+self.c)^2

    def partialGxy153(self,coord):

        return (-coord[0]+self.a)^2*(-coord[1]+self.c)^3

    def partialGxy154(self,coord):

        return (-coord[0]+self.a)^2*(-coord[1]+self.c)^4

    def partialGxy155(self,coord):

        return (-coord[0]+self.a)^2*(-coord[1]+self.d)

    def partialGxy156(self,coord):

        return (-coord[0]+self.a)^2*(-coord[1]+self.c)*(-coord[1]+self.d)

    def partialGxy157(self,coord):

        return (-coord[0]+self.a)^2*(-coord[1]+self.c)^2*(-coord[1]+self.d)

    def partialGxy158(self,coord):

        return (-coord[0]+self.a)^2*(-coord[1]+self.c)^3*(-coord[1]+self.d)

    def partialGxy159(self,coord):

        return (-coord[0]+self.a)^2*(-coord[1]+self.c)^4*(-coord[1]+self.d)

    def partialGxy160(self,coord):

        return (-coord[0]+self.a)^2*(-coord[1]+self.d)^2

    def partialGxy161(self,coord):

        return (-coord[0]+self.a)^2*(-coord[1]+self.c)*(-coord[1]+self.d)^2

    def partialGxy162(self,coord):

        return (-coord[0]+self.a)^2*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2

    def partialGxy163(self,coord):

        return (-coord[0]+self.a)^2*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2

    def partialGxy164(self,coord):

        return (-coord[0]+self.a)^2*(-coord[1]+self.c)^4*(-coord[1]+self.d)^2

    def partialGxy165(self,coord):

        return (-coord[0]+self.a)^2*(-coord[1]+self.d)^3

    def partialGxy166(self,coord):

        return (-coord[0]+self.a)^2*(-coord[1]+self.c)*(-coord[1]+self.d)^3

    def partialGxy167(self,coord):

        return (-coord[0]+self.a)^2*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3

    def partialGxy168(self,coord):

        return (-coord[0]+self.a)^2*(-coord[1]+self.c)^3*(-coord[1]+self.d)^3

    def partialGxy169(self,coord):

        return (-coord[0]+self.a)^2*(-coord[1]+self.c)^4*(-coord[1]+self.d)^3

    def partialGxy170(self,coord):

        return (-coord[0]+self.a)^2*(-coord[1]+self.d)^4

    def partialGxy171(self,coord):

        return (-coord[0]+self.a)^2*(-coord[1]+self.c)*(-coord[1]+self.d)^4

    def partialGxy172(self,coord):

        return (-coord[0]+self.a)^2*(-coord[1]+self.c)^2*(-coord[1]+self.d)^4

    def partialGxy173(self,coord):

        return (-coord[0]+self.a)^2*(-coord[1]+self.c)^3*(-coord[1]+self.d)^4

    def partialGxy174(self,coord):

        return (-coord[0]+self.a)^2*(-coord[1]+self.c)^4*(-coord[1]+self.d)^4

    def partialGxy181(self,coord):

        return (-coord[0]+self.a)^2*(-coord[1]+self.c)+(-coord[0]+self.a)^2*(-coord[1]+self.d)

    def partialGxy182(self,coord):

        return (-coord[0]+self.a)^2*(-coord[1]+self.c)^2+2*(-coord[0]+self.a)^2*(-coord[1]+self.c)*(-coord[1]+self.d)

    def partialGxy183(self,coord):

        return (-coord[0]+self.a)^2*(-coord[1]+self.c)^3+3*(-coord[0]+self.a)^2*(-coord[1]+self.c)^2*(-coord[1]+self.d)

    def partialGxy184(self,coord):

        return (-coord[0]+self.a)^2*(-coord[1]+self.c)^4+4*(-coord[0]+self.a)^2*(-coord[1]+self.c)^3*(-coord[1]+self.d)

    def partialGxy186(self,coord):

        return 2*(-coord[0]+self.a)^2*(-coord[1]+self.c)*(-coord[1]+self.d)+(-coord[0]+self.a)^2*(-coord[1]+self.d)^2

    def partialGxy187(self,coord):

        return 2*(-coord[0]+self.a)^2*(-coord[1]+self.c)^2*(-coord[1]+self.d)+2*(-coord[0]+self.a)^2*(-coord[1]+self.c)*(-coord[1]+self.d)^2

    def partialGxy188(self,coord):

        return 2*(-coord[0]+self.a)^2*(-coord[1]+self.c)^3*(-coord[1]+self.d)+3*(-coord[0]+self.a)^2*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2

    def partialGxy189(self,coord):

        return 2*(-coord[0]+self.a)^2*(-coord[1]+self.c)^4*(-coord[1]+self.d)+4*(-coord[0]+self.a)^2*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2

    def partialGxy191(self,coord):

        return 3*(-coord[0]+self.a)^2*(-coord[1]+self.c)*(-coord[1]+self.d)^2+(-coord[0]+self.a)^2*(-coord[1]+self.d)^3

    def partialGxy192(self,coord):

        return 3*(-coord[0]+self.a)^2*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2+2*(-coord[0]+self.a)^2*(-coord[1]+self.c)*(-coord[1]+self.d)^3

    def partialGxy193(self,coord):

        return 3*(-coord[0]+self.a)^2*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2+3*(-coord[0]+self.a)^2*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3

    def partialGxy194(self,coord):

        return 3*(-coord[0]+self.a)^2*(-coord[1]+self.c)^4*(-coord[1]+self.d)^2+4*(-coord[0]+self.a)^2*(-coord[1]+self.c)^3*(-coord[1]+self.d)^3

    def partialGxy196(self,coord):

        return 4*(-coord[0]+self.a)^2*(-coord[1]+self.c)*(-coord[1]+self.d)^3+(-coord[0]+self.a)^2*(-coord[1]+self.d)^4

    def partialGxy197(self,coord):

        return 4*(-coord[0]+self.a)^2*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3+2*(-coord[0]+self.a)^2*(-coord[1]+self.c)*(-coord[1]+self.d)^4

    def partialGxy198(self,coord):

        return 4*(-coord[0]+self.a)^2*(-coord[1]+self.c)^3*(-coord[1]+self.d)^3+3*(-coord[0]+self.a)^2*(-coord[1]+self.c)^2*(-coord[1]+self.d)^4

    def partialGxy199(self,coord):

        return 4*(-coord[0]+self.a)^2*(-coord[1]+self.c)^4*(-coord[1]+self.d)^3+4*(-coord[0]+self.a)^2*(-coord[1]+self.c)^3*(-coord[1]+self.d)^4

    def partialGxy212(self,coord):

        return 2*(-coord[0]+self.a)^2*(-coord[1]+self.c)^2+8*(-coord[0]+self.a)^2*(-coord[1]+self.c)*(-coord[1]+self.d)+2*(-coord[0]+self.a)^2*(-coord[1]+self.d)^2

    def partialGxy213(self,coord):

        return 2*(-coord[0]+self.a)^2*(-coord[1]+self.c)^3+12*(-coord[0]+self.a)^2*(-coord[1]+self.c)^2*(-coord[1]+self.d)+6*(-coord[0]+self.a)^2*(-coord[1]+self.c)*(-coord[1]+self.d)^2

    def partialGxy214(self,coord):

        return 2*(-coord[0]+self.a)^2*(-coord[1]+self.c)^4+16*(-coord[0]+self.a)^2*(-coord[1]+self.c)^3*(-coord[1]+self.d)+12*(-coord[0]+self.a)^2*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2

    def partialGxy217(self,coord):

        return 6*(-coord[0]+self.a)^2*(-coord[1]+self.c)^2*(-coord[1]+self.d)+12*(-coord[0]+self.a)^2*(-coord[1]+self.c)*(-coord[1]+self.d)^2+2*(-coord[0]+self.a)^2*(-coord[1]+self.d)^3

    def partialGxy218(self,coord):

        return 6*(-coord[0]+self.a)^2*(-coord[1]+self.c)^3*(-coord[1]+self.d)+18*(-coord[0]+self.a)^2*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2+6*(-coord[0]+self.a)^2*(-coord[1]+self.c)*(-coord[1]+self.d)^3

    def partialGxy219(self,coord):

        return 6*(-coord[0]+self.a)^2*(-coord[1]+self.c)^4*(-coord[1]+self.d)+24*(-coord[0]+self.a)^2*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2+12*(-coord[0]+self.a)^2*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3

    def partialGxy222(self,coord):

        return 12*(-coord[0]+self.a)^2*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2+16*(-coord[0]+self.a)^2*(-coord[1]+self.c)*(-coord[1]+self.d)^3+2*(-coord[0]+self.a)^2*(-coord[1]+self.d)^4

    def partialGxy223(self,coord):

        return 12*(-coord[0]+self.a)^2*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2+24*(-coord[0]+self.a)^2*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3+6*(-coord[0]+self.a)^2*(-coord[1]+self.c)*(-coord[1]+self.d)^4

    def partialGxy224(self,coord):

        return 12*(-coord[0]+self.a)^2*(-coord[1]+self.c)^4*(-coord[1]+self.d)^2+32*(-coord[0]+self.a)^2*(-coord[1]+self.c)^3*(-coord[1]+self.d)^3+12*(-coord[0]+self.a)^2*(-coord[1]+self.c)^2*(-coord[1]+self.d)^4

    def partialGxy225(self,coord):

        return (-coord[0]+self.a)^3

    def partialGxy226(self,coord):

        return (-coord[0]+self.a)^3*(-coord[1]+self.c)

    def partialGxy227(self,coord):

        return (-coord[0]+self.a)^3*(-coord[1]+self.c)^2

    def partialGxy228(self,coord):

        return (-coord[0]+self.a)^3*(-coord[1]+self.c)^3

    def partialGxy229(self,coord):

        return (-coord[0]+self.a)^3*(-coord[1]+self.c)^4

    def partialGxy230(self,coord):

        return (-coord[0]+self.a)^3*(-coord[1]+self.d)

    def partialGxy231(self,coord):

        return (-coord[0]+self.a)^3*(-coord[1]+self.c)*(-coord[1]+self.d)

    def partialGxy232(self,coord):

        return (-coord[0]+self.a)^3*(-coord[1]+self.c)^2*(-coord[1]+self.d)

    def partialGxy233(self,coord):

        return (-coord[0]+self.a)^3*(-coord[1]+self.c)^3*(-coord[1]+self.d)

    def partialGxy234(self,coord):

        return (-coord[0]+self.a)^3*(-coord[1]+self.c)^4*(-coord[1]+self.d)

    def partialGxy235(self,coord):

        return (-coord[0]+self.a)^3*(-coord[1]+self.d)^2

    def partialGxy236(self,coord):

        return (-coord[0]+self.a)^3*(-coord[1]+self.c)*(-coord[1]+self.d)^2

    def partialGxy237(self,coord):

        return (-coord[0]+self.a)^3*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2

    def partialGxy238(self,coord):

        return (-coord[0]+self.a)^3*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2

    def partialGxy239(self,coord):

        return (-coord[0]+self.a)^3*(-coord[1]+self.c)^4*(-coord[1]+self.d)^2

    def partialGxy240(self,coord):

        return (-coord[0]+self.a)^3*(-coord[1]+self.d)^3

    def partialGxy241(self,coord):

        return (-coord[0]+self.a)^3*(-coord[1]+self.c)*(-coord[1]+self.d)^3

    def partialGxy242(self,coord):

        return (-coord[0]+self.a)^3*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3

    def partialGxy243(self,coord):

        return (-coord[0]+self.a)^3*(-coord[1]+self.c)^3*(-coord[1]+self.d)^3

    def partialGxy244(self,coord):

        return (-coord[0]+self.a)^3*(-coord[1]+self.c)^4*(-coord[1]+self.d)^3

    def partialGxy245(self,coord):

        return (-coord[0]+self.a)^3*(-coord[1]+self.d)^4

    def partialGxy246(self,coord):

        return (-coord[0]+self.a)^3*(-coord[1]+self.c)*(-coord[1]+self.d)^4

    def partialGxy247(self,coord):

        return (-coord[0]+self.a)^3*(-coord[1]+self.c)^2*(-coord[1]+self.d)^4

    def partialGxy248(self,coord):

        return (-coord[0]+self.a)^3*(-coord[1]+self.c)^3*(-coord[1]+self.d)^4

    def partialGxy249(self,coord):

        return (-coord[0]+self.a)^3*(-coord[1]+self.c)^4*(-coord[1]+self.d)^4

    def partialGxy256(self,coord):

        return (-coord[0]+self.a)^3*(-coord[1]+self.c)+(-coord[0]+self.a)^3*(-coord[1]+self.d)

    def partialGxy257(self,coord):

        return (-coord[0]+self.a)^3*(-coord[1]+self.c)^2+2*(-coord[0]+self.a)^3*(-coord[1]+self.c)*(-coord[1]+self.d)

    def partialGxy258(self,coord):

        return (-coord[0]+self.a)^3*(-coord[1]+self.c)^3+3*(-coord[0]+self.a)^3*(-coord[1]+self.c)^2*(-coord[1]+self.d)

    def partialGxy259(self,coord):

        return (-coord[0]+self.a)^3*(-coord[1]+self.c)^4+4*(-coord[0]+self.a)^3*(-coord[1]+self.c)^3*(-coord[1]+self.d)

    def partialGxy261(self,coord):

        return 2*(-coord[0]+self.a)^3*(-coord[1]+self.c)*(-coord[1]+self.d)+(-coord[0]+self.a)^3*(-coord[1]+self.d)^2

    def partialGxy262(self,coord):

        return 2*(-coord[0]+self.a)^3*(-coord[1]+self.c)^2*(-coord[1]+self.d)+2*(-coord[0]+self.a)^3*(-coord[1]+self.c)*(-coord[1]+self.d)^2

    def partialGxy263(self,coord):

        return 2*(-coord[0]+self.a)^3*(-coord[1]+self.c)^3*(-coord[1]+self.d)+3*(-coord[0]+self.a)^3*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2

    def partialGxy264(self,coord):

        return 2*(-coord[0]+self.a)^3*(-coord[1]+self.c)^4*(-coord[1]+self.d)+4*(-coord[0]+self.a)^3*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2

    def partialGxy266(self,coord):

        return 3*(-coord[0]+self.a)^3*(-coord[1]+self.c)*(-coord[1]+self.d)^2+(-coord[0]+self.a)^3*(-coord[1]+self.d)^3

    def partialGxy267(self,coord):

        return 3*(-coord[0]+self.a)^3*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2+2*(-coord[0]+self.a)^3*(-coord[1]+self.c)*(-coord[1]+self.d)^3

    def partialGxy268(self,coord):

        return 3*(-coord[0]+self.a)^3*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2+3*(-coord[0]+self.a)^3*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3

    def partialGxy269(self,coord):

        return 3*(-coord[0]+self.a)^3*(-coord[1]+self.c)^4*(-coord[1]+self.d)^2+4*(-coord[0]+self.a)^3*(-coord[1]+self.c)^3*(-coord[1]+self.d)^3

    def partialGxy271(self,coord):

        return 4*(-coord[0]+self.a)^3*(-coord[1]+self.c)*(-coord[1]+self.d)^3+(-coord[0]+self.a)^3*(-coord[1]+self.d)^4

    def partialGxy272(self,coord):

        return 4*(-coord[0]+self.a)^3*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3+2*(-coord[0]+self.a)^3*(-coord[1]+self.c)*(-coord[1]+self.d)^4

    def partialGxy273(self,coord):

        return 4*(-coord[0]+self.a)^3*(-coord[1]+self.c)^3*(-coord[1]+self.d)^3+3*(-coord[0]+self.a)^3*(-coord[1]+self.c)^2*(-coord[1]+self.d)^4

    def partialGxy274(self,coord):

        return 4*(-coord[0]+self.a)^3*(-coord[1]+self.c)^4*(-coord[1]+self.d)^3+4*(-coord[0]+self.a)^3*(-coord[1]+self.c)^3*(-coord[1]+self.d)^4

    def partialGxy287(self,coord):

        return 2*(-coord[0]+self.a)^3*(-coord[1]+self.c)^2+8*(-coord[0]+self.a)^3*(-coord[1]+self.c)*(-coord[1]+self.d)+2*(-coord[0]+self.a)^3*(-coord[1]+self.d)^2

    def partialGxy288(self,coord):

        return 2*(-coord[0]+self.a)^3*(-coord[1]+self.c)^3+12*(-coord[0]+self.a)^3*(-coord[1]+self.c)^2*(-coord[1]+self.d)+6*(-coord[0]+self.a)^3*(-coord[1]+self.c)*(-coord[1]+self.d)^2

    def partialGxy289(self,coord):

        return 2*(-coord[0]+self.a)^3*(-coord[1]+self.c)^4+16*(-coord[0]+self.a)^3*(-coord[1]+self.c)^3*(-coord[1]+self.d)+12*(-coord[0]+self.a)^3*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2

    def partialGxy292(self,coord):

        return 6*(-coord[0]+self.a)^3*(-coord[1]+self.c)^2*(-coord[1]+self.d)+12*(-coord[0]+self.a)^3*(-coord[1]+self.c)*(-coord[1]+self.d)^2+2*(-coord[0]+self.a)^3*(-coord[1]+self.d)^3

    def partialGxy293(self,coord):

        return 6*(-coord[0]+self.a)^3*(-coord[1]+self.c)^3*(-coord[1]+self.d)+18*(-coord[0]+self.a)^3*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2+6*(-coord[0]+self.a)^3*(-coord[1]+self.c)*(-coord[1]+self.d)^3

    def partialGxy294(self,coord):

        return 6*(-coord[0]+self.a)^3*(-coord[1]+self.c)^4*(-coord[1]+self.d)+24*(-coord[0]+self.a)^3*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2+12*(-coord[0]+self.a)^3*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3

    def partialGxy297(self,coord):

        return 12*(-coord[0]+self.a)^3*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2+16*(-coord[0]+self.a)^3*(-coord[1]+self.c)*(-coord[1]+self.d)^3+2*(-coord[0]+self.a)^3*(-coord[1]+self.d)^4

    def partialGxy298(self,coord):

        return 12*(-coord[0]+self.a)^3*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2+24*(-coord[0]+self.a)^3*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3+6*(-coord[0]+self.a)^3*(-coord[1]+self.c)*(-coord[1]+self.d)^4

    def partialGxy299(self,coord):

        return 12*(-coord[0]+self.a)^3*(-coord[1]+self.c)^4*(-coord[1]+self.d)^2+32*(-coord[0]+self.a)^3*(-coord[1]+self.c)^3*(-coord[1]+self.d)^3+12*(-coord[0]+self.a)^3*(-coord[1]+self.c)^2*(-coord[1]+self.d)^4

    def partialGxy300(self,coord):

        return (-coord[0]+self.a)^4

    def partialGxy301(self,coord):

        return (-coord[0]+self.a)^4*(-coord[1]+self.c)

    def partialGxy302(self,coord):

        return (-coord[0]+self.a)^4*(-coord[1]+self.c)^2

    def partialGxy303(self,coord):

        return (-coord[0]+self.a)^4*(-coord[1]+self.c)^3

    def partialGxy304(self,coord):

        return (-coord[0]+self.a)^4*(-coord[1]+self.c)^4

    def partialGxy305(self,coord):

        return (-coord[0]+self.a)^4*(-coord[1]+self.d)

    def partialGxy306(self,coord):

        return (-coord[0]+self.a)^4*(-coord[1]+self.c)*(-coord[1]+self.d)

    def partialGxy307(self,coord):

        return (-coord[0]+self.a)^4*(-coord[1]+self.c)^2*(-coord[1]+self.d)

    def partialGxy308(self,coord):

        return (-coord[0]+self.a)^4*(-coord[1]+self.c)^3*(-coord[1]+self.d)

    def partialGxy309(self,coord):

        return (-coord[0]+self.a)^4*(-coord[1]+self.c)^4*(-coord[1]+self.d)

    def partialGxy310(self,coord):

        return (-coord[0]+self.a)^4*(-coord[1]+self.d)^2

    def partialGxy311(self,coord):

        return (-coord[0]+self.a)^4*(-coord[1]+self.c)*(-coord[1]+self.d)^2

    def partialGxy312(self,coord):

        return (-coord[0]+self.a)^4*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2

    def partialGxy313(self,coord):

        return (-coord[0]+self.a)^4*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2

    def partialGxy314(self,coord):

        return (-coord[0]+self.a)^4*(-coord[1]+self.c)^4*(-coord[1]+self.d)^2

    def partialGxy315(self,coord):

        return (-coord[0]+self.a)^4*(-coord[1]+self.d)^3

    def partialGxy316(self,coord):

        return (-coord[0]+self.a)^4*(-coord[1]+self.c)*(-coord[1]+self.d)^3

    def partialGxy317(self,coord):

        return (-coord[0]+self.a)^4*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3

    def partialGxy318(self,coord):

        return (-coord[0]+self.a)^4*(-coord[1]+self.c)^3*(-coord[1]+self.d)^3

    def partialGxy319(self,coord):

        return (-coord[0]+self.a)^4*(-coord[1]+self.c)^4*(-coord[1]+self.d)^3

    def partialGxy320(self,coord):

        return (-coord[0]+self.a)^4*(-coord[1]+self.d)^4

    def partialGxy321(self,coord):

        return (-coord[0]+self.a)^4*(-coord[1]+self.c)*(-coord[1]+self.d)^4

    def partialGxy322(self,coord):

        return (-coord[0]+self.a)^4*(-coord[1]+self.c)^2*(-coord[1]+self.d)^4

    def partialGxy323(self,coord):

        return (-coord[0]+self.a)^4*(-coord[1]+self.c)^3*(-coord[1]+self.d)^4

    def partialGxy324(self,coord):

        return (-coord[0]+self.a)^4*(-coord[1]+self.c)^4*(-coord[1]+self.d)^4

    def partialGxy331(self,coord):

        return (-coord[0]+self.a)^4*(-coord[1]+self.c)+(-coord[0]+self.a)^4*(-coord[1]+self.d)

    def partialGxy332(self,coord):

        return (-coord[0]+self.a)^4*(-coord[1]+self.c)^2+2*(-coord[0]+self.a)^4*(-coord[1]+self.c)*(-coord[1]+self.d)

    def partialGxy333(self,coord):

        return (-coord[0]+self.a)^4*(-coord[1]+self.c)^3+3*(-coord[0]+self.a)^4*(-coord[1]+self.c)^2*(-coord[1]+self.d)

    def partialGxy334(self,coord):

        return (-coord[0]+self.a)^4*(-coord[1]+self.c)^4+4*(-coord[0]+self.a)^4*(-coord[1]+self.c)^3*(-coord[1]+self.d)

    def partialGxy336(self,coord):

        return 2*(-coord[0]+self.a)^4*(-coord[1]+self.c)*(-coord[1]+self.d)+(-coord[0]+self.a)^4*(-coord[1]+self.d)^2

    def partialGxy337(self,coord):

        return 2*(-coord[0]+self.a)^4*(-coord[1]+self.c)^2*(-coord[1]+self.d)+2*(-coord[0]+self.a)^4*(-coord[1]+self.c)*(-coord[1]+self.d)^2

    def partialGxy338(self,coord):

        return 2*(-coord[0]+self.a)^4*(-coord[1]+self.c)^3*(-coord[1]+self.d)+3*(-coord[0]+self.a)^4*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2

    def partialGxy339(self,coord):

        return 2*(-coord[0]+self.a)^4*(-coord[1]+self.c)^4*(-coord[1]+self.d)+4*(-coord[0]+self.a)^4*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2

    def partialGxy341(self,coord):

        return 3*(-coord[0]+self.a)^4*(-coord[1]+self.c)*(-coord[1]+self.d)^2+(-coord[0]+self.a)^4*(-coord[1]+self.d)^3

    def partialGxy342(self,coord):

        return 3*(-coord[0]+self.a)^4*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2+2*(-coord[0]+self.a)^4*(-coord[1]+self.c)*(-coord[1]+self.d)^3

    def partialGxy343(self,coord):

        return 3*(-coord[0]+self.a)^4*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2+3*(-coord[0]+self.a)^4*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3

    def partialGxy344(self,coord):

        return 3*(-coord[0]+self.a)^4*(-coord[1]+self.c)^4*(-coord[1]+self.d)^2+4*(-coord[0]+self.a)^4*(-coord[1]+self.c)^3*(-coord[1]+self.d)^3

    def partialGxy346(self,coord):

        return 4*(-coord[0]+self.a)^4*(-coord[1]+self.c)*(-coord[1]+self.d)^3+(-coord[0]+self.a)^4*(-coord[1]+self.d)^4

    def partialGxy347(self,coord):

        return 4*(-coord[0]+self.a)^4*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3+2*(-coord[0]+self.a)^4*(-coord[1]+self.c)*(-coord[1]+self.d)^4

    def partialGxy348(self,coord):

        return 4*(-coord[0]+self.a)^4*(-coord[1]+self.c)^3*(-coord[1]+self.d)^3+3*(-coord[0]+self.a)^4*(-coord[1]+self.c)^2*(-coord[1]+self.d)^4

    def partialGxy349(self,coord):

        return 4*(-coord[0]+self.a)^4*(-coord[1]+self.c)^4*(-coord[1]+self.d)^3+4*(-coord[0]+self.a)^4*(-coord[1]+self.c)^3*(-coord[1]+self.d)^4

    def partialGxy362(self,coord):

        return 2*(-coord[0]+self.a)^4*(-coord[1]+self.c)^2+8*(-coord[0]+self.a)^4*(-coord[1]+self.c)*(-coord[1]+self.d)+2*(-coord[0]+self.a)^4*(-coord[1]+self.d)^2

    def partialGxy363(self,coord):

        return 2*(-coord[0]+self.a)^4*(-coord[1]+self.c)^3+12*(-coord[0]+self.a)^4*(-coord[1]+self.c)^2*(-coord[1]+self.d)+6*(-coord[0]+self.a)^4*(-coord[1]+self.c)*(-coord[1]+self.d)^2

    def partialGxy364(self,coord):

        return 2*(-coord[0]+self.a)^4*(-coord[1]+self.c)^4+16*(-coord[0]+self.a)^4*(-coord[1]+self.c)^3*(-coord[1]+self.d)+12*(-coord[0]+self.a)^4*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2

    def partialGxy367(self,coord):

        return 6*(-coord[0]+self.a)^4*(-coord[1]+self.c)^2*(-coord[1]+self.d)+12*(-coord[0]+self.a)^4*(-coord[1]+self.c)*(-coord[1]+self.d)^2+2*(-coord[0]+self.a)^4*(-coord[1]+self.d)^3

    def partialGxy368(self,coord):

        return 6*(-coord[0]+self.a)^4*(-coord[1]+self.c)^3*(-coord[1]+self.d)+18*(-coord[0]+self.a)^4*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2+6*(-coord[0]+self.a)^4*(-coord[1]+self.c)*(-coord[1]+self.d)^3

    def partialGxy369(self,coord):

        return 6*(-coord[0]+self.a)^4*(-coord[1]+self.c)^4*(-coord[1]+self.d)+24*(-coord[0]+self.a)^4*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2+12*(-coord[0]+self.a)^4*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3

    def partialGxy372(self,coord):

        return 12*(-coord[0]+self.a)^4*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2+16*(-coord[0]+self.a)^4*(-coord[1]+self.c)*(-coord[1]+self.d)^3+2*(-coord[0]+self.a)^4*(-coord[1]+self.d)^4

    def partialGxy373(self,coord):

        return 12*(-coord[0]+self.a)^4*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2+24*(-coord[0]+self.a)^4*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3+6*(-coord[0]+self.a)^4*(-coord[1]+self.c)*(-coord[1]+self.d)^4

    def partialGxy374(self,coord):

        return 12*(-coord[0]+self.a)^4*(-coord[1]+self.c)^4*(-coord[1]+self.d)^2+32*(-coord[0]+self.a)^4*(-coord[1]+self.c)^3*(-coord[1]+self.d)^3+12*(-coord[0]+self.a)^4*(-coord[1]+self.c)^2*(-coord[1]+self.d)^4

    def partialGxy375(self,coord):

        return -coord[0]+self.b

    def partialGxy376(self,coord):

        return (-coord[0]+self.b)*(-coord[1]+self.c)

    def partialGxy377(self,coord):

        return (-coord[0]+self.b)*(-coord[1]+self.c)^2

    def partialGxy378(self,coord):

        return (-coord[0]+self.b)*(-coord[1]+self.c)^3

    def partialGxy379(self,coord):

        return (-coord[0]+self.b)*(-coord[1]+self.c)^4

    def partialGxy380(self,coord):

        return (-coord[0]+self.b)*(-coord[1]+self.d)

    def partialGxy381(self,coord):

        return (-coord[0]+self.b)*(-coord[1]+self.c)*(-coord[1]+self.d)

    def partialGxy382(self,coord):

        return (-coord[0]+self.b)*(-coord[1]+self.c)^2*(-coord[1]+self.d)

    def partialGxy383(self,coord):

        return (-coord[0]+self.b)*(-coord[1]+self.c)^3*(-coord[1]+self.d)

    def partialGxy384(self,coord):

        return (-coord[0]+self.b)*(-coord[1]+self.c)^4*(-coord[1]+self.d)

    def partialGxy385(self,coord):

        return (-coord[0]+self.b)*(-coord[1]+self.d)^2

    def partialGxy386(self,coord):

        return (-coord[0]+self.b)*(-coord[1]+self.c)*(-coord[1]+self.d)^2

    def partialGxy387(self,coord):

        return (-coord[0]+self.b)*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2

    def partialGxy388(self,coord):

        return (-coord[0]+self.b)*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2

    def partialGxy389(self,coord):

        return (-coord[0]+self.b)*(-coord[1]+self.c)^4*(-coord[1]+self.d)^2

    def partialGxy390(self,coord):

        return (-coord[0]+self.b)*(-coord[1]+self.d)^3

    def partialGxy391(self,coord):

        return (-coord[0]+self.b)*(-coord[1]+self.c)*(-coord[1]+self.d)^3

    def partialGxy392(self,coord):

        return (-coord[0]+self.b)*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3

    def partialGxy393(self,coord):

        return (-coord[0]+self.b)*(-coord[1]+self.c)^3*(-coord[1]+self.d)^3

    def partialGxy394(self,coord):

        return (-coord[0]+self.b)*(-coord[1]+self.c)^4*(-coord[1]+self.d)^3

    def partialGxy395(self,coord):

        return (-coord[0]+self.b)*(-coord[1]+self.d)^4

    def partialGxy396(self,coord):

        return (-coord[0]+self.b)*(-coord[1]+self.c)*(-coord[1]+self.d)^4

    def partialGxy397(self,coord):

        return (-coord[0]+self.b)*(-coord[1]+self.c)^2*(-coord[1]+self.d)^4

    def partialGxy398(self,coord):

        return (-coord[0]+self.b)*(-coord[1]+self.c)^3*(-coord[1]+self.d)^4

    def partialGxy399(self,coord):

        return (-coord[0]+self.b)*(-coord[1]+self.c)^4*(-coord[1]+self.d)^4

    def partialGxy406(self,coord):

        return (-coord[0]+self.b)*(-coord[1]+self.c)+(-coord[0]+self.b)*(-coord[1]+self.d)

    def partialGxy407(self,coord):

        return (-coord[0]+self.b)*(-coord[1]+self.c)^2+2*(-coord[0]+self.b)*(-coord[1]+self.c)*(-coord[1]+self.d)

    def partialGxy408(self,coord):

        return (-coord[0]+self.b)*(-coord[1]+self.c)^3+3*(-coord[0]+self.b)*(-coord[1]+self.c)^2*(-coord[1]+self.d)

    def partialGxy409(self,coord):

        return (-coord[0]+self.b)*(-coord[1]+self.c)^4+4*(-coord[0]+self.b)*(-coord[1]+self.c)^3*(-coord[1]+self.d)

    def partialGxy411(self,coord):

        return 2*(-coord[0]+self.b)*(-coord[1]+self.c)*(-coord[1]+self.d)+(-coord[0]+self.b)*(-coord[1]+self.d)^2

    def partialGxy412(self,coord):

        return 2*(-coord[0]+self.b)*(-coord[1]+self.c)^2*(-coord[1]+self.d)+2*(-coord[0]+self.b)*(-coord[1]+self.c)*(-coord[1]+self.d)^2

    def partialGxy413(self,coord):

        return 2*(-coord[0]+self.b)*(-coord[1]+self.c)^3*(-coord[1]+self.d)+3*(-coord[0]+self.b)*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2

    def partialGxy414(self,coord):

        return 2*(-coord[0]+self.b)*(-coord[1]+self.c)^4*(-coord[1]+self.d)+4*(-coord[0]+self.b)*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2

    def partialGxy416(self,coord):

        return 3*(-coord[0]+self.b)*(-coord[1]+self.c)*(-coord[1]+self.d)^2+(-coord[0]+self.b)*(-coord[1]+self.d)^3

    def partialGxy417(self,coord):

        return 3*(-coord[0]+self.b)*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2+2*(-coord[0]+self.b)*(-coord[1]+self.c)*(-coord[1]+self.d)^3

    def partialGxy418(self,coord):

        return 3*(-coord[0]+self.b)*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2+3*(-coord[0]+self.b)*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3

    def partialGxy419(self,coord):

        return 3*(-coord[0]+self.b)*(-coord[1]+self.c)^4*(-coord[1]+self.d)^2+4*(-coord[0]+self.b)*(-coord[1]+self.c)^3*(-coord[1]+self.d)^3

    def partialGxy421(self,coord):

        return 4*(-coord[0]+self.b)*(-coord[1]+self.c)*(-coord[1]+self.d)^3+(-coord[0]+self.b)*(-coord[1]+self.d)^4

    def partialGxy422(self,coord):

        return 4*(-coord[0]+self.b)*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3+2*(-coord[0]+self.b)*(-coord[1]+self.c)*(-coord[1]+self.d)^4

    def partialGxy423(self,coord):

        return 4*(-coord[0]+self.b)*(-coord[1]+self.c)^3*(-coord[1]+self.d)^3+3*(-coord[0]+self.b)*(-coord[1]+self.c)^2*(-coord[1]+self.d)^4

    def partialGxy424(self,coord):

        return 4*(-coord[0]+self.b)*(-coord[1]+self.c)^4*(-coord[1]+self.d)^3+4*(-coord[0]+self.b)*(-coord[1]+self.c)^3*(-coord[1]+self.d)^4

    def partialGxy437(self,coord):

        return 2*(-coord[0]+self.b)*(-coord[1]+self.c)^2+8*(-coord[0]+self.b)*(-coord[1]+self.c)*(-coord[1]+self.d)+2*(-coord[0]+self.b)*(-coord[1]+self.d)^2

    def partialGxy438(self,coord):

        return 2*(-coord[0]+self.b)*(-coord[1]+self.c)^3+12*(-coord[0]+self.b)*(-coord[1]+self.c)^2*(-coord[1]+self.d)+6*(-coord[0]+self.b)*(-coord[1]+self.c)*(-coord[1]+self.d)^2

    def partialGxy439(self,coord):

        return 2*(-coord[0]+self.b)*(-coord[1]+self.c)^4+16*(-coord[0]+self.b)*(-coord[1]+self.c)^3*(-coord[1]+self.d)+12*(-coord[0]+self.b)*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2

    def partialGxy442(self,coord):

        return 6*(-coord[0]+self.b)*(-coord[1]+self.c)^2*(-coord[1]+self.d)+12*(-coord[0]+self.b)*(-coord[1]+self.c)*(-coord[1]+self.d)^2+2*(-coord[0]+self.b)*(-coord[1]+self.d)^3

    def partialGxy443(self,coord):

        return 6*(-coord[0]+self.b)*(-coord[1]+self.c)^3*(-coord[1]+self.d)+18*(-coord[0]+self.b)*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2+6*(-coord[0]+self.b)*(-coord[1]+self.c)*(-coord[1]+self.d)^3

    def partialGxy444(self,coord):

        return 6*(-coord[0]+self.b)*(-coord[1]+self.c)^4*(-coord[1]+self.d)+24*(-coord[0]+self.b)*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2+12*(-coord[0]+self.b)*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3

    def partialGxy447(self,coord):

        return 12*(-coord[0]+self.b)*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2+16*(-coord[0]+self.b)*(-coord[1]+self.c)*(-coord[1]+self.d)^3+2*(-coord[0]+self.b)*(-coord[1]+self.d)^4

    def partialGxy448(self,coord):

        return 12*(-coord[0]+self.b)*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2+24*(-coord[0]+self.b)*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3+6*(-coord[0]+self.b)*(-coord[1]+self.c)*(-coord[1]+self.d)^4

    def partialGxy449(self,coord):

        return 12*(-coord[0]+self.b)*(-coord[1]+self.c)^4*(-coord[1]+self.d)^2+32*(-coord[0]+self.b)*(-coord[1]+self.c)^3*(-coord[1]+self.d)^3+12*(-coord[0]+self.b)*(-coord[1]+self.c)^2*(-coord[1]+self.d)^4

    def partialGxy450(self,coord):

        return (-coord[0]+self.a)*(-coord[0]+self.b)

    def partialGxy451(self,coord):

        return (-coord[0]+self.a)*(-coord[0]+self.b)*(-coord[1]+self.c)

    def partialGxy452(self,coord):

        return (-coord[0]+self.a)*(-coord[0]+self.b)*(-coord[1]+self.c)^2

    def partialGxy453(self,coord):

        return (-coord[0]+self.a)*(-coord[0]+self.b)*(-coord[1]+self.c)^3

    def partialGxy454(self,coord):

        return (-coord[0]+self.a)*(-coord[0]+self.b)*(-coord[1]+self.c)^4

    def partialGxy455(self,coord):

        return (-coord[0]+self.a)*(-coord[0]+self.b)*(-coord[1]+self.d)

    def partialGxy456(self,coord):

        return (-coord[0]+self.a)*(-coord[0]+self.b)*(-coord[1]+self.c)*(-coord[1]+self.d)

    def partialGxy457(self,coord):

        return (-coord[0]+self.a)*(-coord[0]+self.b)*(-coord[1]+self.c)^2*(-coord[1]+self.d)

    def partialGxy458(self,coord):

        return (-coord[0]+self.a)*(-coord[0]+self.b)*(-coord[1]+self.c)^3*(-coord[1]+self.d)

    def partialGxy459(self,coord):

        return (-coord[0]+self.a)*(-coord[0]+self.b)*(-coord[1]+self.c)^4*(-coord[1]+self.d)

    def partialGxy460(self,coord):

        return (-coord[0]+self.a)*(-coord[0]+self.b)*(-coord[1]+self.d)^2

    def partialGxy461(self,coord):

        return (-coord[0]+self.a)*(-coord[0]+self.b)*(-coord[1]+self.c)*(-coord[1]+self.d)^2

    def partialGxy462(self,coord):

        return (-coord[0]+self.a)*(-coord[0]+self.b)*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2

    def partialGxy463(self,coord):

        return (-coord[0]+self.a)*(-coord[0]+self.b)*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2

    def partialGxy464(self,coord):

        return (-coord[0]+self.a)*(-coord[0]+self.b)*(-coord[1]+self.c)^4*(-coord[1]+self.d)^2

    def partialGxy465(self,coord):

        return (-coord[0]+self.a)*(-coord[0]+self.b)*(-coord[1]+self.d)^3

    def partialGxy466(self,coord):

        return (-coord[0]+self.a)*(-coord[0]+self.b)*(-coord[1]+self.c)*(-coord[1]+self.d)^3

    def partialGxy467(self,coord):

        return (-coord[0]+self.a)*(-coord[0]+self.b)*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3

    def partialGxy468(self,coord):

        return (-coord[0]+self.a)*(-coord[0]+self.b)*(-coord[1]+self.c)^3*(-coord[1]+self.d)^3

    def partialGxy469(self,coord):

        return (-coord[0]+self.a)*(-coord[0]+self.b)*(-coord[1]+self.c)^4*(-coord[1]+self.d)^3

    def partialGxy470(self,coord):

        return (-coord[0]+self.a)*(-coord[0]+self.b)*(-coord[1]+self.d)^4

    def partialGxy471(self,coord):

        return (-coord[0]+self.a)*(-coord[0]+self.b)*(-coord[1]+self.c)*(-coord[1]+self.d)^4

    def partialGxy472(self,coord):

        return (-coord[0]+self.a)*(-coord[0]+self.b)*(-coord[1]+self.c)^2*(-coord[1]+self.d)^4

    def partialGxy473(self,coord):

        return (-coord[0]+self.a)*(-coord[0]+self.b)*(-coord[1]+self.c)^3*(-coord[1]+self.d)^4

    def partialGxy474(self,coord):

        return (-coord[0]+self.a)*(-coord[0]+self.b)*(-coord[1]+self.c)^4*(-coord[1]+self.d)^4

    def partialGxy481(self,coord):

        return (-coord[0]+self.a)*(-coord[0]+self.b)*(-coord[1]+self.c)+(-coord[0]+self.a)*(-coord[0]+self.b)*(-coord[1]+self.d)

    def partialGxy482(self,coord):

        return (-coord[0]+self.a)*(-coord[0]+self.b)*(-coord[1]+self.c)^2+2*(-coord[0]+self.a)*(-coord[0]+self.b)*(-coord[1]+self.c)*(-coord[1]+self.d)

    def partialGxy483(self,coord):

        return (-coord[0]+self.a)*(-coord[0]+self.b)*(-coord[1]+self.c)^3+3*(-coord[0]+self.a)*(-coord[0]+self.b)*(-coord[1]+self.c)^2*(-coord[1]+self.d)

    def partialGxy484(self,coord):

        return (-coord[0]+self.a)*(-coord[0]+self.b)*(-coord[1]+self.c)^4+4*(-coord[0]+self.a)*(-coord[0]+self.b)*(-coord[1]+self.c)^3*(-coord[1]+self.d)

    def partialGxy486(self,coord):

        return 2*(-coord[0]+self.a)*(-coord[0]+self.b)*(-coord[1]+self.c)*(-coord[1]+self.d)+(-coord[0]+self.a)*(-coord[0]+self.b)*(-coord[1]+self.d)^2

    def partialGxy487(self,coord):

        return 2*(-coord[0]+self.a)*(-coord[0]+self.b)*(-coord[1]+self.c)^2*(-coord[1]+self.d)+2*(-coord[0]+self.a)*(-coord[0]+self.b)*(-coord[1]+self.c)*(-coord[1]+self.d)^2

    def partialGxy488(self,coord):

        return 2*(-coord[0]+self.a)*(-coord[0]+self.b)*(-coord[1]+self.c)^3*(-coord[1]+self.d)+3*(-coord[0]+self.a)*(-coord[0]+self.b)*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2

    def partialGxy489(self,coord):

        return 2*(-coord[0]+self.a)*(-coord[0]+self.b)*(-coord[1]+self.c)^4*(-coord[1]+self.d)+4*(-coord[0]+self.a)*(-coord[0]+self.b)*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2

    def partialGxy491(self,coord):

        return 3*(-coord[0]+self.a)*(-coord[0]+self.b)*(-coord[1]+self.c)*(-coord[1]+self.d)^2+(-coord[0]+self.a)*(-coord[0]+self.b)*(-coord[1]+self.d)^3

    def partialGxy492(self,coord):

        return 3*(-coord[0]+self.a)*(-coord[0]+self.b)*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2+2*(-coord[0]+self.a)*(-coord[0]+self.b)*(-coord[1]+self.c)*(-coord[1]+self.d)^3

    def partialGxy493(self,coord):

        return 3*(-coord[0]+self.a)*(-coord[0]+self.b)*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2+3*(-coord[0]+self.a)*(-coord[0]+self.b)*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3

    def partialGxy494(self,coord):

        return 3*(-coord[0]+self.a)*(-coord[0]+self.b)*(-coord[1]+self.c)^4*(-coord[1]+self.d)^2+4*(-coord[0]+self.a)*(-coord[0]+self.b)*(-coord[1]+self.c)^3*(-coord[1]+self.d)^3

    def partialGxy496(self,coord):

        return 4*(-coord[0]+self.a)*(-coord[0]+self.b)*(-coord[1]+self.c)*(-coord[1]+self.d)^3+(-coord[0]+self.a)*(-coord[0]+self.b)*(-coord[1]+self.d)^4

    def partialGxy497(self,coord):

        return 4*(-coord[0]+self.a)*(-coord[0]+self.b)*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3+2*(-coord[0]+self.a)*(-coord[0]+self.b)*(-coord[1]+self.c)*(-coord[1]+self.d)^4

    def partialGxy498(self,coord):

        return 4*(-coord[0]+self.a)*(-coord[0]+self.b)*(-coord[1]+self.c)^3*(-coord[1]+self.d)^3+3*(-coord[0]+self.a)*(-coord[0]+self.b)*(-coord[1]+self.c)^2*(-coord[1]+self.d)^4

    def partialGxy499(self,coord):

        return 4*(-coord[0]+self.a)*(-coord[0]+self.b)*(-coord[1]+self.c)^4*(-coord[1]+self.d)^3+4*(-coord[0]+self.a)*(-coord[0]+self.b)*(-coord[1]+self.c)^3*(-coord[1]+self.d)^4

    def partialGxy512(self,coord):

        return (-coord[0]+self.a)*(-coord[0]+self.b)*(2*(-coord[1]+self.c)^2+8*(-coord[1]+self.c)*(-coord[1]+self.d)+2*(-coord[1]+self.d)^2)

    def partialGxy513(self,coord):

        return (-coord[0]+self.a)*(-coord[0]+self.b)*(2*(-coord[1]+self.c)^3+12*(-coord[1]+self.c)^2*(-coord[1]+self.d)+6*(-coord[1]+self.c)*(-coord[1]+self.d)^2)

    def partialGxy514(self,coord):

        return (-coord[0]+self.a)*(-coord[0]+self.b)*(2*(-coord[1]+self.c)^4+16*(-coord[1]+self.c)^3*(-coord[1]+self.d)+12*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2)

    def partialGxy517(self,coord):

        return (-coord[0]+self.a)*(-coord[0]+self.b)*(6*(-coord[1]+self.c)^2*(-coord[1]+self.d)+12*(-coord[1]+self.c)*(-coord[1]+self.d)^2+2*(-coord[1]+self.d)^3)

    def partialGxy518(self,coord):

        return (-coord[0]+self.a)*(-coord[0]+self.b)*(6*(-coord[1]+self.c)^3*(-coord[1]+self.d)+18*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2+6*(-coord[1]+self.c)*(-coord[1]+self.d)^3)

    def partialGxy519(self,coord):

        return (-coord[0]+self.a)*(-coord[0]+self.b)*(6*(-coord[1]+self.c)^4*(-coord[1]+self.d)+24*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2+12*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3)

    def partialGxy522(self,coord):

        return (-coord[0]+self.a)*(-coord[0]+self.b)*(12*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2+16*(-coord[1]+self.c)*(-coord[1]+self.d)^3+2*(-coord[1]+self.d)^4)

    def partialGxy523(self,coord):

        return (-coord[0]+self.a)*(-coord[0]+self.b)*(12*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2+24*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3+6*(-coord[1]+self.c)*(-coord[1]+self.d)^4)

    def partialGxy524(self,coord):

        return (-coord[0]+self.a)*(-coord[0]+self.b)*(12*(-coord[1]+self.c)^4*(-coord[1]+self.d)^2+32*(-coord[1]+self.c)^3*(-coord[1]+self.d)^3+12*(-coord[1]+self.c)^2*(-coord[1]+self.d)^4)

    def partialGxy525(self,coord):

        return (-coord[0]+self.a)^2*(-coord[0]+self.b)

    def partialGxy526(self,coord):

        return (-coord[0]+self.a)^2*(-coord[0]+self.b)*(-coord[1]+self.c)

    def partialGxy527(self,coord):

        return (-coord[0]+self.a)^2*(-coord[0]+self.b)*(-coord[1]+self.c)^2

    def partialGxy528(self,coord):

        return (-coord[0]+self.a)^2*(-coord[0]+self.b)*(-coord[1]+self.c)^3

    def partialGxy529(self,coord):

        return (-coord[0]+self.a)^2*(-coord[0]+self.b)*(-coord[1]+self.c)^4

    def partialGxy530(self,coord):

        return (-coord[0]+self.a)^2*(-coord[0]+self.b)*(-coord[1]+self.d)

    def partialGxy531(self,coord):

        return (-coord[0]+self.a)^2*(-coord[0]+self.b)*(-coord[1]+self.c)*(-coord[1]+self.d)

    def partialGxy532(self,coord):

        return (-coord[0]+self.a)^2*(-coord[0]+self.b)*(-coord[1]+self.c)^2*(-coord[1]+self.d)

    def partialGxy533(self,coord):

        return (-coord[0]+self.a)^2*(-coord[0]+self.b)*(-coord[1]+self.c)^3*(-coord[1]+self.d)

    def partialGxy534(self,coord):

        return (-coord[0]+self.a)^2*(-coord[0]+self.b)*(-coord[1]+self.c)^4*(-coord[1]+self.d)

    def partialGxy535(self,coord):

        return (-coord[0]+self.a)^2*(-coord[0]+self.b)*(-coord[1]+self.d)^2

    def partialGxy536(self,coord):

        return (-coord[0]+self.a)^2*(-coord[0]+self.b)*(-coord[1]+self.c)*(-coord[1]+self.d)^2

    def partialGxy537(self,coord):

        return (-coord[0]+self.a)^2*(-coord[0]+self.b)*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2

    def partialGxy538(self,coord):

        return (-coord[0]+self.a)^2*(-coord[0]+self.b)*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2

    def partialGxy539(self,coord):

        return (-coord[0]+self.a)^2*(-coord[0]+self.b)*(-coord[1]+self.c)^4*(-coord[1]+self.d)^2

    def partialGxy540(self,coord):

        return (-coord[0]+self.a)^2*(-coord[0]+self.b)*(-coord[1]+self.d)^3

    def partialGxy541(self,coord):

        return (-coord[0]+self.a)^2*(-coord[0]+self.b)*(-coord[1]+self.c)*(-coord[1]+self.d)^3

    def partialGxy542(self,coord):

        return (-coord[0]+self.a)^2*(-coord[0]+self.b)*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3

    def partialGxy543(self,coord):

        return (-coord[0]+self.a)^2*(-coord[0]+self.b)*(-coord[1]+self.c)^3*(-coord[1]+self.d)^3

    def partialGxy544(self,coord):

        return (-coord[0]+self.a)^2*(-coord[0]+self.b)*(-coord[1]+self.c)^4*(-coord[1]+self.d)^3

    def partialGxy545(self,coord):

        return (-coord[0]+self.a)^2*(-coord[0]+self.b)*(-coord[1]+self.d)^4

    def partialGxy546(self,coord):

        return (-coord[0]+self.a)^2*(-coord[0]+self.b)*(-coord[1]+self.c)*(-coord[1]+self.d)^4

    def partialGxy547(self,coord):

        return (-coord[0]+self.a)^2*(-coord[0]+self.b)*(-coord[1]+self.c)^2*(-coord[1]+self.d)^4

    def partialGxy548(self,coord):

        return (-coord[0]+self.a)^2*(-coord[0]+self.b)*(-coord[1]+self.c)^3*(-coord[1]+self.d)^4

    def partialGxy549(self,coord):

        return (-coord[0]+self.a)^2*(-coord[0]+self.b)*(-coord[1]+self.c)^4*(-coord[1]+self.d)^4

    def partialGxy556(self,coord):

        return (-coord[0]+self.a)^2*(-coord[0]+self.b)*(-coord[1]+self.c)+(-coord[0]+self.a)^2*(-coord[0]+self.b)*(-coord[1]+self.d)

    def partialGxy557(self,coord):

        return (-coord[0]+self.a)^2*(-coord[0]+self.b)*(-coord[1]+self.c)^2+2*(-coord[0]+self.a)^2*(-coord[0]+self.b)*(-coord[1]+self.c)*(-coord[1]+self.d)

    def partialGxy558(self,coord):

        return (-coord[0]+self.a)^2*(-coord[0]+self.b)*(-coord[1]+self.c)^3+3*(-coord[0]+self.a)^2*(-coord[0]+self.b)*(-coord[1]+self.c)^2*(-coord[1]+self.d)

    def partialGxy559(self,coord):

        return (-coord[0]+self.a)^2*(-coord[0]+self.b)*(-coord[1]+self.c)^4+4*(-coord[0]+self.a)^2*(-coord[0]+self.b)*(-coord[1]+self.c)^3*(-coord[1]+self.d)

    def partialGxy561(self,coord):

        return 2*(-coord[0]+self.a)^2*(-coord[0]+self.b)*(-coord[1]+self.c)*(-coord[1]+self.d)+(-coord[0]+self.a)^2*(-coord[0]+self.b)*(-coord[1]+self.d)^2

    def partialGxy562(self,coord):

        return 2*(-coord[0]+self.a)^2*(-coord[0]+self.b)*(-coord[1]+self.c)^2*(-coord[1]+self.d)+2*(-coord[0]+self.a)^2*(-coord[0]+self.b)*(-coord[1]+self.c)*(-coord[1]+self.d)^2

    def partialGxy563(self,coord):

        return 2*(-coord[0]+self.a)^2*(-coord[0]+self.b)*(-coord[1]+self.c)^3*(-coord[1]+self.d)+3*(-coord[0]+self.a)^2*(-coord[0]+self.b)*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2

    def partialGxy564(self,coord):

        return 2*(-coord[0]+self.a)^2*(-coord[0]+self.b)*(-coord[1]+self.c)^4*(-coord[1]+self.d)+4*(-coord[0]+self.a)^2*(-coord[0]+self.b)*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2

    def partialGxy566(self,coord):

        return 3*(-coord[0]+self.a)^2*(-coord[0]+self.b)*(-coord[1]+self.c)*(-coord[1]+self.d)^2+(-coord[0]+self.a)^2*(-coord[0]+self.b)*(-coord[1]+self.d)^3

    def partialGxy567(self,coord):

        return 3*(-coord[0]+self.a)^2*(-coord[0]+self.b)*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2+2*(-coord[0]+self.a)^2*(-coord[0]+self.b)*(-coord[1]+self.c)*(-coord[1]+self.d)^3

    def partialGxy568(self,coord):

        return 3*(-coord[0]+self.a)^2*(-coord[0]+self.b)*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2+3*(-coord[0]+self.a)^2*(-coord[0]+self.b)*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3

    def partialGxy569(self,coord):

        return 3*(-coord[0]+self.a)^2*(-coord[0]+self.b)*(-coord[1]+self.c)^4*(-coord[1]+self.d)^2+4*(-coord[0]+self.a)^2*(-coord[0]+self.b)*(-coord[1]+self.c)^3*(-coord[1]+self.d)^3

    def partialGxy571(self,coord):

        return 4*(-coord[0]+self.a)^2*(-coord[0]+self.b)*(-coord[1]+self.c)*(-coord[1]+self.d)^3+(-coord[0]+self.a)^2*(-coord[0]+self.b)*(-coord[1]+self.d)^4

    def partialGxy572(self,coord):

        return 4*(-coord[0]+self.a)^2*(-coord[0]+self.b)*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3+2*(-coord[0]+self.a)^2*(-coord[0]+self.b)*(-coord[1]+self.c)*(-coord[1]+self.d)^4

    def partialGxy573(self,coord):

        return 4*(-coord[0]+self.a)^2*(-coord[0]+self.b)*(-coord[1]+self.c)^3*(-coord[1]+self.d)^3+3*(-coord[0]+self.a)^2*(-coord[0]+self.b)*(-coord[1]+self.c)^2*(-coord[1]+self.d)^4

    def partialGxy574(self,coord):

        return 4*(-coord[0]+self.a)^2*(-coord[0]+self.b)*(-coord[1]+self.c)^4*(-coord[1]+self.d)^3+4*(-coord[0]+self.a)^2*(-coord[0]+self.b)*(-coord[1]+self.c)^3*(-coord[1]+self.d)^4

    def partialGxy587(self,coord):

        return (-coord[0]+self.a)^2*(-coord[0]+self.b)*(2*(-coord[1]+self.c)^2+8*(-coord[1]+self.c)*(-coord[1]+self.d)+2*(-coord[1]+self.d)^2)

    def partialGxy588(self,coord):

        return (-coord[0]+self.a)^2*(-coord[0]+self.b)*(2*(-coord[1]+self.c)^3+12*(-coord[1]+self.c)^2*(-coord[1]+self.d)+6*(-coord[1]+self.c)*(-coord[1]+self.d)^2)

    def partialGxy589(self,coord):

        return (-coord[0]+self.a)^2*(-coord[0]+self.b)*(2*(-coord[1]+self.c)^4+16*(-coord[1]+self.c)^3*(-coord[1]+self.d)+12*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2)

    def partialGxy592(self,coord):

        return (-coord[0]+self.a)^2*(-coord[0]+self.b)*(6*(-coord[1]+self.c)^2*(-coord[1]+self.d)+12*(-coord[1]+self.c)*(-coord[1]+self.d)^2+2*(-coord[1]+self.d)^3)

    def partialGxy593(self,coord):

        return (-coord[0]+self.a)^2*(-coord[0]+self.b)*(6*(-coord[1]+self.c)^3*(-coord[1]+self.d)+18*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2+6*(-coord[1]+self.c)*(-coord[1]+self.d)^3)

    def partialGxy594(self,coord):

        return (-coord[0]+self.a)^2*(-coord[0]+self.b)*(6*(-coord[1]+self.c)^4*(-coord[1]+self.d)+24*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2+12*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3)

    def partialGxy597(self,coord):

        return (-coord[0]+self.a)^2*(-coord[0]+self.b)*(12*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2+16*(-coord[1]+self.c)*(-coord[1]+self.d)^3+2*(-coord[1]+self.d)^4)

    def partialGxy598(self,coord):

        return (-coord[0]+self.a)^2*(-coord[0]+self.b)*(12*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2+24*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3+6*(-coord[1]+self.c)*(-coord[1]+self.d)^4)

    def partialGxy599(self,coord):

        return (-coord[0]+self.a)^2*(-coord[0]+self.b)*(12*(-coord[1]+self.c)^4*(-coord[1]+self.d)^2+32*(-coord[1]+self.c)^3*(-coord[1]+self.d)^3+12*(-coord[1]+self.c)^2*(-coord[1]+self.d)^4)

    def partialGxy600(self,coord):

        return (-coord[0]+self.a)^3*(-coord[0]+self.b)

    def partialGxy601(self,coord):

        return (-coord[0]+self.a)^3*(-coord[0]+self.b)*(-coord[1]+self.c)

    def partialGxy602(self,coord):

        return (-coord[0]+self.a)^3*(-coord[0]+self.b)*(-coord[1]+self.c)^2

    def partialGxy603(self,coord):

        return (-coord[0]+self.a)^3*(-coord[0]+self.b)*(-coord[1]+self.c)^3

    def partialGxy604(self,coord):

        return (-coord[0]+self.a)^3*(-coord[0]+self.b)*(-coord[1]+self.c)^4

    def partialGxy605(self,coord):

        return (-coord[0]+self.a)^3*(-coord[0]+self.b)*(-coord[1]+self.d)

    def partialGxy606(self,coord):

        return (-coord[0]+self.a)^3*(-coord[0]+self.b)*(-coord[1]+self.c)*(-coord[1]+self.d)

    def partialGxy607(self,coord):

        return (-coord[0]+self.a)^3*(-coord[0]+self.b)*(-coord[1]+self.c)^2*(-coord[1]+self.d)

    def partialGxy608(self,coord):

        return (-coord[0]+self.a)^3*(-coord[0]+self.b)*(-coord[1]+self.c)^3*(-coord[1]+self.d)

    def partialGxy609(self,coord):

        return (-coord[0]+self.a)^3*(-coord[0]+self.b)*(-coord[1]+self.c)^4*(-coord[1]+self.d)

    def partialGxy610(self,coord):

        return (-coord[0]+self.a)^3*(-coord[0]+self.b)*(-coord[1]+self.d)^2

    def partialGxy611(self,coord):

        return (-coord[0]+self.a)^3*(-coord[0]+self.b)*(-coord[1]+self.c)*(-coord[1]+self.d)^2

    def partialGxy612(self,coord):

        return (-coord[0]+self.a)^3*(-coord[0]+self.b)*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2

    def partialGxy613(self,coord):

        return (-coord[0]+self.a)^3*(-coord[0]+self.b)*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2

    def partialGxy614(self,coord):

        return (-coord[0]+self.a)^3*(-coord[0]+self.b)*(-coord[1]+self.c)^4*(-coord[1]+self.d)^2

    def partialGxy615(self,coord):

        return (-coord[0]+self.a)^3*(-coord[0]+self.b)*(-coord[1]+self.d)^3

    def partialGxy616(self,coord):

        return (-coord[0]+self.a)^3*(-coord[0]+self.b)*(-coord[1]+self.c)*(-coord[1]+self.d)^3

    def partialGxy617(self,coord):

        return (-coord[0]+self.a)^3*(-coord[0]+self.b)*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3

    def partialGxy618(self,coord):

        return (-coord[0]+self.a)^3*(-coord[0]+self.b)*(-coord[1]+self.c)^3*(-coord[1]+self.d)^3

    def partialGxy619(self,coord):

        return (-coord[0]+self.a)^3*(-coord[0]+self.b)*(-coord[1]+self.c)^4*(-coord[1]+self.d)^3

    def partialGxy620(self,coord):

        return (-coord[0]+self.a)^3*(-coord[0]+self.b)*(-coord[1]+self.d)^4

    def partialGxy621(self,coord):

        return (-coord[0]+self.a)^3*(-coord[0]+self.b)*(-coord[1]+self.c)*(-coord[1]+self.d)^4

    def partialGxy622(self,coord):

        return (-coord[0]+self.a)^3*(-coord[0]+self.b)*(-coord[1]+self.c)^2*(-coord[1]+self.d)^4

    def partialGxy623(self,coord):

        return (-coord[0]+self.a)^3*(-coord[0]+self.b)*(-coord[1]+self.c)^3*(-coord[1]+self.d)^4

    def partialGxy624(self,coord):

        return (-coord[0]+self.a)^3*(-coord[0]+self.b)*(-coord[1]+self.c)^4*(-coord[1]+self.d)^4

    def partialGxy631(self,coord):

        return (-coord[0]+self.a)^3*(-coord[0]+self.b)*(-coord[1]+self.c)+(-coord[0]+self.a)^3*(-coord[0]+self.b)*(-coord[1]+self.d)

    def partialGxy632(self,coord):

        return (-coord[0]+self.a)^3*(-coord[0]+self.b)*(-coord[1]+self.c)^2+2*(-coord[0]+self.a)^3*(-coord[0]+self.b)*(-coord[1]+self.c)*(-coord[1]+self.d)

    def partialGxy633(self,coord):

        return (-coord[0]+self.a)^3*(-coord[0]+self.b)*(-coord[1]+self.c)^3+3*(-coord[0]+self.a)^3*(-coord[0]+self.b)*(-coord[1]+self.c)^2*(-coord[1]+self.d)

    def partialGxy634(self,coord):

        return (-coord[0]+self.a)^3*(-coord[0]+self.b)*(-coord[1]+self.c)^4+4*(-coord[0]+self.a)^3*(-coord[0]+self.b)*(-coord[1]+self.c)^3*(-coord[1]+self.d)

    def partialGxy636(self,coord):

        return 2*(-coord[0]+self.a)^3*(-coord[0]+self.b)*(-coord[1]+self.c)*(-coord[1]+self.d)+(-coord[0]+self.a)^3*(-coord[0]+self.b)*(-coord[1]+self.d)^2

    def partialGxy637(self,coord):

        return 2*(-coord[0]+self.a)^3*(-coord[0]+self.b)*(-coord[1]+self.c)^2*(-coord[1]+self.d)+2*(-coord[0]+self.a)^3*(-coord[0]+self.b)*(-coord[1]+self.c)*(-coord[1]+self.d)^2

    def partialGxy638(self,coord):

        return 2*(-coord[0]+self.a)^3*(-coord[0]+self.b)*(-coord[1]+self.c)^3*(-coord[1]+self.d)+3*(-coord[0]+self.a)^3*(-coord[0]+self.b)*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2

    def partialGxy639(self,coord):

        return 2*(-coord[0]+self.a)^3*(-coord[0]+self.b)*(-coord[1]+self.c)^4*(-coord[1]+self.d)+4*(-coord[0]+self.a)^3*(-coord[0]+self.b)*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2

    def partialGxy641(self,coord):

        return 3*(-coord[0]+self.a)^3*(-coord[0]+self.b)*(-coord[1]+self.c)*(-coord[1]+self.d)^2+(-coord[0]+self.a)^3*(-coord[0]+self.b)*(-coord[1]+self.d)^3

    def partialGxy642(self,coord):

        return 3*(-coord[0]+self.a)^3*(-coord[0]+self.b)*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2+2*(-coord[0]+self.a)^3*(-coord[0]+self.b)*(-coord[1]+self.c)*(-coord[1]+self.d)^3

    def partialGxy643(self,coord):

        return 3*(-coord[0]+self.a)^3*(-coord[0]+self.b)*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2+3*(-coord[0]+self.a)^3*(-coord[0]+self.b)*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3

    def partialGxy644(self,coord):

        return 3*(-coord[0]+self.a)^3*(-coord[0]+self.b)*(-coord[1]+self.c)^4*(-coord[1]+self.d)^2+4*(-coord[0]+self.a)^3*(-coord[0]+self.b)*(-coord[1]+self.c)^3*(-coord[1]+self.d)^3

    def partialGxy646(self,coord):

        return 4*(-coord[0]+self.a)^3*(-coord[0]+self.b)*(-coord[1]+self.c)*(-coord[1]+self.d)^3+(-coord[0]+self.a)^3*(-coord[0]+self.b)*(-coord[1]+self.d)^4

    def partialGxy647(self,coord):

        return 4*(-coord[0]+self.a)^3*(-coord[0]+self.b)*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3+2*(-coord[0]+self.a)^3*(-coord[0]+self.b)*(-coord[1]+self.c)*(-coord[1]+self.d)^4

    def partialGxy648(self,coord):

        return 4*(-coord[0]+self.a)^3*(-coord[0]+self.b)*(-coord[1]+self.c)^3*(-coord[1]+self.d)^3+3*(-coord[0]+self.a)^3*(-coord[0]+self.b)*(-coord[1]+self.c)^2*(-coord[1]+self.d)^4

    def partialGxy649(self,coord):

        return 4*(-coord[0]+self.a)^3*(-coord[0]+self.b)*(-coord[1]+self.c)^4*(-coord[1]+self.d)^3+4*(-coord[0]+self.a)^3*(-coord[0]+self.b)*(-coord[1]+self.c)^3*(-coord[1]+self.d)^4

    def partialGxy662(self,coord):

        return (-coord[0]+self.a)^3*(-coord[0]+self.b)*(2*(-coord[1]+self.c)^2+8*(-coord[1]+self.c)*(-coord[1]+self.d)+2*(-coord[1]+self.d)^2)

    def partialGxy663(self,coord):

        return (-coord[0]+self.a)^3*(-coord[0]+self.b)*(2*(-coord[1]+self.c)^3+12*(-coord[1]+self.c)^2*(-coord[1]+self.d)+6*(-coord[1]+self.c)*(-coord[1]+self.d)^2)

    def partialGxy664(self,coord):

        return (-coord[0]+self.a)^3*(-coord[0]+self.b)*(2*(-coord[1]+self.c)^4+16*(-coord[1]+self.c)^3*(-coord[1]+self.d)+12*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2)

    def partialGxy667(self,coord):

        return (-coord[0]+self.a)^3*(-coord[0]+self.b)*(6*(-coord[1]+self.c)^2*(-coord[1]+self.d)+12*(-coord[1]+self.c)*(-coord[1]+self.d)^2+2*(-coord[1]+self.d)^3)

    def partialGxy668(self,coord):

        return (-coord[0]+self.a)^3*(-coord[0]+self.b)*(6*(-coord[1]+self.c)^3*(-coord[1]+self.d)+18*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2+6*(-coord[1]+self.c)*(-coord[1]+self.d)^3)

    def partialGxy669(self,coord):

        return (-coord[0]+self.a)^3*(-coord[0]+self.b)*(6*(-coord[1]+self.c)^4*(-coord[1]+self.d)+24*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2+12*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3)

    def partialGxy672(self,coord):

        return (-coord[0]+self.a)^3*(-coord[0]+self.b)*(12*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2+16*(-coord[1]+self.c)*(-coord[1]+self.d)^3+2*(-coord[1]+self.d)^4)

    def partialGxy673(self,coord):

        return (-coord[0]+self.a)^3*(-coord[0]+self.b)*(12*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2+24*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3+6*(-coord[1]+self.c)*(-coord[1]+self.d)^4)

    def partialGxy674(self,coord):

        return (-coord[0]+self.a)^3*(-coord[0]+self.b)*(12*(-coord[1]+self.c)^4*(-coord[1]+self.d)^2+32*(-coord[1]+self.c)^3*(-coord[1]+self.d)^3+12*(-coord[1]+self.c)^2*(-coord[1]+self.d)^4)

    def partialGxy675(self,coord):

        return (-coord[0]+self.a)^4*(-coord[0]+self.b)

    def partialGxy676(self,coord):

        return (-coord[0]+self.a)^4*(-coord[0]+self.b)*(-coord[1]+self.c)

    def partialGxy677(self,coord):

        return (-coord[0]+self.a)^4*(-coord[0]+self.b)*(-coord[1]+self.c)^2

    def partialGxy678(self,coord):

        return (-coord[0]+self.a)^4*(-coord[0]+self.b)*(-coord[1]+self.c)^3

    def partialGxy679(self,coord):

        return (-coord[0]+self.a)^4*(-coord[0]+self.b)*(-coord[1]+self.c)^4

    def partialGxy680(self,coord):

        return (-coord[0]+self.a)^4*(-coord[0]+self.b)*(-coord[1]+self.d)

    def partialGxy681(self,coord):

        return (-coord[0]+self.a)^4*(-coord[0]+self.b)*(-coord[1]+self.c)*(-coord[1]+self.d)

    def partialGxy682(self,coord):

        return (-coord[0]+self.a)^4*(-coord[0]+self.b)*(-coord[1]+self.c)^2*(-coord[1]+self.d)

    def partialGxy683(self,coord):

        return (-coord[0]+self.a)^4*(-coord[0]+self.b)*(-coord[1]+self.c)^3*(-coord[1]+self.d)

    def partialGxy684(self,coord):

        return (-coord[0]+self.a)^4*(-coord[0]+self.b)*(-coord[1]+self.c)^4*(-coord[1]+self.d)

    def partialGxy685(self,coord):

        return (-coord[0]+self.a)^4*(-coord[0]+self.b)*(-coord[1]+self.d)^2

    def partialGxy686(self,coord):

        return (-coord[0]+self.a)^4*(-coord[0]+self.b)*(-coord[1]+self.c)*(-coord[1]+self.d)^2

    def partialGxy687(self,coord):

        return (-coord[0]+self.a)^4*(-coord[0]+self.b)*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2

    def partialGxy688(self,coord):

        return (-coord[0]+self.a)^4*(-coord[0]+self.b)*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2

    def partialGxy689(self,coord):

        return (-coord[0]+self.a)^4*(-coord[0]+self.b)*(-coord[1]+self.c)^4*(-coord[1]+self.d)^2

    def partialGxy690(self,coord):

        return (-coord[0]+self.a)^4*(-coord[0]+self.b)*(-coord[1]+self.d)^3

    def partialGxy691(self,coord):

        return (-coord[0]+self.a)^4*(-coord[0]+self.b)*(-coord[1]+self.c)*(-coord[1]+self.d)^3

    def partialGxy692(self,coord):

        return (-coord[0]+self.a)^4*(-coord[0]+self.b)*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3

    def partialGxy693(self,coord):

        return (-coord[0]+self.a)^4*(-coord[0]+self.b)*(-coord[1]+self.c)^3*(-coord[1]+self.d)^3

    def partialGxy694(self,coord):

        return (-coord[0]+self.a)^4*(-coord[0]+self.b)*(-coord[1]+self.c)^4*(-coord[1]+self.d)^3

    def partialGxy695(self,coord):

        return (-coord[0]+self.a)^4*(-coord[0]+self.b)*(-coord[1]+self.d)^4

    def partialGxy696(self,coord):

        return (-coord[0]+self.a)^4*(-coord[0]+self.b)*(-coord[1]+self.c)*(-coord[1]+self.d)^4

    def partialGxy697(self,coord):

        return (-coord[0]+self.a)^4*(-coord[0]+self.b)*(-coord[1]+self.c)^2*(-coord[1]+self.d)^4

    def partialGxy698(self,coord):

        return (-coord[0]+self.a)^4*(-coord[0]+self.b)*(-coord[1]+self.c)^3*(-coord[1]+self.d)^4

    def partialGxy699(self,coord):

        return (-coord[0]+self.a)^4*(-coord[0]+self.b)*(-coord[1]+self.c)^4*(-coord[1]+self.d)^4

    def partialGxy706(self,coord):

        return (-coord[0]+self.a)^4*(-coord[0]+self.b)*(-coord[1]+self.c)+(-coord[0]+self.a)^4*(-coord[0]+self.b)*(-coord[1]+self.d)

    def partialGxy707(self,coord):

        return (-coord[0]+self.a)^4*(-coord[0]+self.b)*(-coord[1]+self.c)^2+2*(-coord[0]+self.a)^4*(-coord[0]+self.b)*(-coord[1]+self.c)*(-coord[1]+self.d)

    def partialGxy708(self,coord):

        return (-coord[0]+self.a)^4*(-coord[0]+self.b)*(-coord[1]+self.c)^3+3*(-coord[0]+self.a)^4*(-coord[0]+self.b)*(-coord[1]+self.c)^2*(-coord[1]+self.d)

    def partialGxy709(self,coord):

        return (-coord[0]+self.a)^4*(-coord[0]+self.b)*(-coord[1]+self.c)^4+4*(-coord[0]+self.a)^4*(-coord[0]+self.b)*(-coord[1]+self.c)^3*(-coord[1]+self.d)

    def partialGxy711(self,coord):

        return 2*(-coord[0]+self.a)^4*(-coord[0]+self.b)*(-coord[1]+self.c)*(-coord[1]+self.d)+(-coord[0]+self.a)^4*(-coord[0]+self.b)*(-coord[1]+self.d)^2

    def partialGxy712(self,coord):

        return 2*(-coord[0]+self.a)^4*(-coord[0]+self.b)*(-coord[1]+self.c)^2*(-coord[1]+self.d)+2*(-coord[0]+self.a)^4*(-coord[0]+self.b)*(-coord[1]+self.c)*(-coord[1]+self.d)^2

    def partialGxy713(self,coord):

        return 2*(-coord[0]+self.a)^4*(-coord[0]+self.b)*(-coord[1]+self.c)^3*(-coord[1]+self.d)+3*(-coord[0]+self.a)^4*(-coord[0]+self.b)*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2

    def partialGxy714(self,coord):

        return 2*(-coord[0]+self.a)^4*(-coord[0]+self.b)*(-coord[1]+self.c)^4*(-coord[1]+self.d)+4*(-coord[0]+self.a)^4*(-coord[0]+self.b)*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2

    def partialGxy716(self,coord):

        return 3*(-coord[0]+self.a)^4*(-coord[0]+self.b)*(-coord[1]+self.c)*(-coord[1]+self.d)^2+(-coord[0]+self.a)^4*(-coord[0]+self.b)*(-coord[1]+self.d)^3

    def partialGxy717(self,coord):

        return 3*(-coord[0]+self.a)^4*(-coord[0]+self.b)*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2+2*(-coord[0]+self.a)^4*(-coord[0]+self.b)*(-coord[1]+self.c)*(-coord[1]+self.d)^3

    def partialGxy718(self,coord):

        return 3*(-coord[0]+self.a)^4*(-coord[0]+self.b)*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2+3*(-coord[0]+self.a)^4*(-coord[0]+self.b)*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3

    def partialGxy719(self,coord):

        return 3*(-coord[0]+self.a)^4*(-coord[0]+self.b)*(-coord[1]+self.c)^4*(-coord[1]+self.d)^2+4*(-coord[0]+self.a)^4*(-coord[0]+self.b)*(-coord[1]+self.c)^3*(-coord[1]+self.d)^3

    def partialGxy721(self,coord):

        return 4*(-coord[0]+self.a)^4*(-coord[0]+self.b)*(-coord[1]+self.c)*(-coord[1]+self.d)^3+(-coord[0]+self.a)^4*(-coord[0]+self.b)*(-coord[1]+self.d)^4

    def partialGxy722(self,coord):

        return 4*(-coord[0]+self.a)^4*(-coord[0]+self.b)*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3+2*(-coord[0]+self.a)^4*(-coord[0]+self.b)*(-coord[1]+self.c)*(-coord[1]+self.d)^4

    def partialGxy723(self,coord):

        return 4*(-coord[0]+self.a)^4*(-coord[0]+self.b)*(-coord[1]+self.c)^3*(-coord[1]+self.d)^3+3*(-coord[0]+self.a)^4*(-coord[0]+self.b)*(-coord[1]+self.c)^2*(-coord[1]+self.d)^4

    def partialGxy724(self,coord):

        return 4*(-coord[0]+self.a)^4*(-coord[0]+self.b)*(-coord[1]+self.c)^4*(-coord[1]+self.d)^3+4*(-coord[0]+self.a)^4*(-coord[0]+self.b)*(-coord[1]+self.c)^3*(-coord[1]+self.d)^4

    def partialGxy737(self,coord):

        return (-coord[0]+self.a)^4*(-coord[0]+self.b)*(2*(-coord[1]+self.c)^2+8*(-coord[1]+self.c)*(-coord[1]+self.d)+2*(-coord[1]+self.d)^2)

    def partialGxy738(self,coord):

        return (-coord[0]+self.a)^4*(-coord[0]+self.b)*(2*(-coord[1]+self.c)^3+12*(-coord[1]+self.c)^2*(-coord[1]+self.d)+6*(-coord[1]+self.c)*(-coord[1]+self.d)^2)

    def partialGxy739(self,coord):

        return (-coord[0]+self.a)^4*(-coord[0]+self.b)*(2*(-coord[1]+self.c)^4+16*(-coord[1]+self.c)^3*(-coord[1]+self.d)+12*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2)

    def partialGxy742(self,coord):

        return (-coord[0]+self.a)^4*(-coord[0]+self.b)*(6*(-coord[1]+self.c)^2*(-coord[1]+self.d)+12*(-coord[1]+self.c)*(-coord[1]+self.d)^2+2*(-coord[1]+self.d)^3)

    def partialGxy743(self,coord):

        return (-coord[0]+self.a)^4*(-coord[0]+self.b)*(6*(-coord[1]+self.c)^3*(-coord[1]+self.d)+18*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2+6*(-coord[1]+self.c)*(-coord[1]+self.d)^3)

    def partialGxy744(self,coord):

        return (-coord[0]+self.a)^4*(-coord[0]+self.b)*(6*(-coord[1]+self.c)^4*(-coord[1]+self.d)+24*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2+12*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3)

    def partialGxy747(self,coord):

        return (-coord[0]+self.a)^4*(-coord[0]+self.b)*(12*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2+16*(-coord[1]+self.c)*(-coord[1]+self.d)^3+2*(-coord[1]+self.d)^4)

    def partialGxy748(self,coord):

        return (-coord[0]+self.a)^4*(-coord[0]+self.b)*(12*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2+24*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3+6*(-coord[1]+self.c)*(-coord[1]+self.d)^4)

    def partialGxy749(self,coord):

        return (-coord[0]+self.a)^4*(-coord[0]+self.b)*(12*(-coord[1]+self.c)^4*(-coord[1]+self.d)^2+32*(-coord[1]+self.c)^3*(-coord[1]+self.d)^3+12*(-coord[1]+self.c)^2*(-coord[1]+self.d)^4)

    def partialGxy750(self,coord):

        return (-coord[0]+self.b)^2

    def partialGxy751(self,coord):

        return (-coord[0]+self.b)^2*(-coord[1]+self.c)

    def partialGxy752(self,coord):

        return (-coord[0]+self.b)^2*(-coord[1]+self.c)^2

    def partialGxy753(self,coord):

        return (-coord[0]+self.b)^2*(-coord[1]+self.c)^3

    def partialGxy754(self,coord):

        return (-coord[0]+self.b)^2*(-coord[1]+self.c)^4

    def partialGxy755(self,coord):

        return (-coord[0]+self.b)^2*(-coord[1]+self.d)

    def partialGxy756(self,coord):

        return (-coord[0]+self.b)^2*(-coord[1]+self.c)*(-coord[1]+self.d)

    def partialGxy757(self,coord):

        return (-coord[0]+self.b)^2*(-coord[1]+self.c)^2*(-coord[1]+self.d)

    def partialGxy758(self,coord):

        return (-coord[0]+self.b)^2*(-coord[1]+self.c)^3*(-coord[1]+self.d)

    def partialGxy759(self,coord):

        return (-coord[0]+self.b)^2*(-coord[1]+self.c)^4*(-coord[1]+self.d)

    def partialGxy760(self,coord):

        return (-coord[0]+self.b)^2*(-coord[1]+self.d)^2

    def partialGxy761(self,coord):

        return (-coord[0]+self.b)^2*(-coord[1]+self.c)*(-coord[1]+self.d)^2

    def partialGxy762(self,coord):

        return (-coord[0]+self.b)^2*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2

    def partialGxy763(self,coord):

        return (-coord[0]+self.b)^2*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2

    def partialGxy764(self,coord):

        return (-coord[0]+self.b)^2*(-coord[1]+self.c)^4*(-coord[1]+self.d)^2

    def partialGxy765(self,coord):

        return (-coord[0]+self.b)^2*(-coord[1]+self.d)^3

    def partialGxy766(self,coord):

        return (-coord[0]+self.b)^2*(-coord[1]+self.c)*(-coord[1]+self.d)^3

    def partialGxy767(self,coord):

        return (-coord[0]+self.b)^2*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3

    def partialGxy768(self,coord):

        return (-coord[0]+self.b)^2*(-coord[1]+self.c)^3*(-coord[1]+self.d)^3

    def partialGxy769(self,coord):

        return (-coord[0]+self.b)^2*(-coord[1]+self.c)^4*(-coord[1]+self.d)^3

    def partialGxy770(self,coord):

        return (-coord[0]+self.b)^2*(-coord[1]+self.d)^4

    def partialGxy771(self,coord):

        return (-coord[0]+self.b)^2*(-coord[1]+self.c)*(-coord[1]+self.d)^4

    def partialGxy772(self,coord):

        return (-coord[0]+self.b)^2*(-coord[1]+self.c)^2*(-coord[1]+self.d)^4

    def partialGxy773(self,coord):

        return (-coord[0]+self.b)^2*(-coord[1]+self.c)^3*(-coord[1]+self.d)^4

    def partialGxy774(self,coord):

        return (-coord[0]+self.b)^2*(-coord[1]+self.c)^4*(-coord[1]+self.d)^4

    def partialGxy781(self,coord):

        return (-coord[0]+self.b)^2*(-coord[1]+self.c)+(-coord[0]+self.b)^2*(-coord[1]+self.d)

    def partialGxy782(self,coord):

        return (-coord[0]+self.b)^2*(-coord[1]+self.c)^2+2*(-coord[0]+self.b)^2*(-coord[1]+self.c)*(-coord[1]+self.d)

    def partialGxy783(self,coord):

        return (-coord[0]+self.b)^2*(-coord[1]+self.c)^3+3*(-coord[0]+self.b)^2*(-coord[1]+self.c)^2*(-coord[1]+self.d)

    def partialGxy784(self,coord):

        return (-coord[0]+self.b)^2*(-coord[1]+self.c)^4+4*(-coord[0]+self.b)^2*(-coord[1]+self.c)^3*(-coord[1]+self.d)

    def partialGxy786(self,coord):

        return 2*(-coord[0]+self.b)^2*(-coord[1]+self.c)*(-coord[1]+self.d)+(-coord[0]+self.b)^2*(-coord[1]+self.d)^2

    def partialGxy787(self,coord):

        return 2*(-coord[0]+self.b)^2*(-coord[1]+self.c)^2*(-coord[1]+self.d)+2*(-coord[0]+self.b)^2*(-coord[1]+self.c)*(-coord[1]+self.d)^2

    def partialGxy788(self,coord):

        return 2*(-coord[0]+self.b)^2*(-coord[1]+self.c)^3*(-coord[1]+self.d)+3*(-coord[0]+self.b)^2*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2

    def partialGxy789(self,coord):

        return 2*(-coord[0]+self.b)^2*(-coord[1]+self.c)^4*(-coord[1]+self.d)+4*(-coord[0]+self.b)^2*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2

    def partialGxy791(self,coord):

        return 3*(-coord[0]+self.b)^2*(-coord[1]+self.c)*(-coord[1]+self.d)^2+(-coord[0]+self.b)^2*(-coord[1]+self.d)^3

    def partialGxy792(self,coord):

        return 3*(-coord[0]+self.b)^2*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2+2*(-coord[0]+self.b)^2*(-coord[1]+self.c)*(-coord[1]+self.d)^3

    def partialGxy793(self,coord):

        return 3*(-coord[0]+self.b)^2*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2+3*(-coord[0]+self.b)^2*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3

    def partialGxy794(self,coord):

        return 3*(-coord[0]+self.b)^2*(-coord[1]+self.c)^4*(-coord[1]+self.d)^2+4*(-coord[0]+self.b)^2*(-coord[1]+self.c)^3*(-coord[1]+self.d)^3

    def partialGxy796(self,coord):

        return 4*(-coord[0]+self.b)^2*(-coord[1]+self.c)*(-coord[1]+self.d)^3+(-coord[0]+self.b)^2*(-coord[1]+self.d)^4

    def partialGxy797(self,coord):

        return 4*(-coord[0]+self.b)^2*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3+2*(-coord[0]+self.b)^2*(-coord[1]+self.c)*(-coord[1]+self.d)^4

    def partialGxy798(self,coord):

        return 4*(-coord[0]+self.b)^2*(-coord[1]+self.c)^3*(-coord[1]+self.d)^3+3*(-coord[0]+self.b)^2*(-coord[1]+self.c)^2*(-coord[1]+self.d)^4

    def partialGxy799(self,coord):

        return 4*(-coord[0]+self.b)^2*(-coord[1]+self.c)^4*(-coord[1]+self.d)^3+4*(-coord[0]+self.b)^2*(-coord[1]+self.c)^3*(-coord[1]+self.d)^4

    def partialGxy812(self,coord):

        return 2*(-coord[0]+self.b)^2*(-coord[1]+self.c)^2+8*(-coord[0]+self.b)^2*(-coord[1]+self.c)*(-coord[1]+self.d)+2*(-coord[0]+self.b)^2*(-coord[1]+self.d)^2

    def partialGxy813(self,coord):

        return 2*(-coord[0]+self.b)^2*(-coord[1]+self.c)^3+12*(-coord[0]+self.b)^2*(-coord[1]+self.c)^2*(-coord[1]+self.d)+6*(-coord[0]+self.b)^2*(-coord[1]+self.c)*(-coord[1]+self.d)^2

    def partialGxy814(self,coord):

        return 2*(-coord[0]+self.b)^2*(-coord[1]+self.c)^4+16*(-coord[0]+self.b)^2*(-coord[1]+self.c)^3*(-coord[1]+self.d)+12*(-coord[0]+self.b)^2*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2

    def partialGxy817(self,coord):

        return 6*(-coord[0]+self.b)^2*(-coord[1]+self.c)^2*(-coord[1]+self.d)+12*(-coord[0]+self.b)^2*(-coord[1]+self.c)*(-coord[1]+self.d)^2+2*(-coord[0]+self.b)^2*(-coord[1]+self.d)^3

    def partialGxy818(self,coord):

        return 6*(-coord[0]+self.b)^2*(-coord[1]+self.c)^3*(-coord[1]+self.d)+18*(-coord[0]+self.b)^2*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2+6*(-coord[0]+self.b)^2*(-coord[1]+self.c)*(-coord[1]+self.d)^3

    def partialGxy819(self,coord):

        return 6*(-coord[0]+self.b)^2*(-coord[1]+self.c)^4*(-coord[1]+self.d)+24*(-coord[0]+self.b)^2*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2+12*(-coord[0]+self.b)^2*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3

    def partialGxy822(self,coord):

        return 12*(-coord[0]+self.b)^2*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2+16*(-coord[0]+self.b)^2*(-coord[1]+self.c)*(-coord[1]+self.d)^3+2*(-coord[0]+self.b)^2*(-coord[1]+self.d)^4

    def partialGxy823(self,coord):

        return 12*(-coord[0]+self.b)^2*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2+24*(-coord[0]+self.b)^2*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3+6*(-coord[0]+self.b)^2*(-coord[1]+self.c)*(-coord[1]+self.d)^4

    def partialGxy824(self,coord):

        return 12*(-coord[0]+self.b)^2*(-coord[1]+self.c)^4*(-coord[1]+self.d)^2+32*(-coord[0]+self.b)^2*(-coord[1]+self.c)^3*(-coord[1]+self.d)^3+12*(-coord[0]+self.b)^2*(-coord[1]+self.c)^2*(-coord[1]+self.d)^4

    def partialGxy825(self,coord):

        return (-coord[0]+self.a)*(-coord[0]+self.b)^2

    def partialGxy826(self,coord):

        return (-coord[0]+self.a)*(-coord[0]+self.b)^2*(-coord[1]+self.c)

    def partialGxy827(self,coord):

        return (-coord[0]+self.a)*(-coord[0]+self.b)^2*(-coord[1]+self.c)^2

    def partialGxy828(self,coord):

        return (-coord[0]+self.a)*(-coord[0]+self.b)^2*(-coord[1]+self.c)^3

    def partialGxy829(self,coord):

        return (-coord[0]+self.a)*(-coord[0]+self.b)^2*(-coord[1]+self.c)^4

    def partialGxy830(self,coord):

        return (-coord[0]+self.a)*(-coord[0]+self.b)^2*(-coord[1]+self.d)

    def partialGxy831(self,coord):

        return (-coord[0]+self.a)*(-coord[0]+self.b)^2*(-coord[1]+self.c)*(-coord[1]+self.d)

    def partialGxy832(self,coord):

        return (-coord[0]+self.a)*(-coord[0]+self.b)^2*(-coord[1]+self.c)^2*(-coord[1]+self.d)

    def partialGxy833(self,coord):

        return (-coord[0]+self.a)*(-coord[0]+self.b)^2*(-coord[1]+self.c)^3*(-coord[1]+self.d)

    def partialGxy834(self,coord):

        return (-coord[0]+self.a)*(-coord[0]+self.b)^2*(-coord[1]+self.c)^4*(-coord[1]+self.d)

    def partialGxy835(self,coord):

        return (-coord[0]+self.a)*(-coord[0]+self.b)^2*(-coord[1]+self.d)^2

    def partialGxy836(self,coord):

        return (-coord[0]+self.a)*(-coord[0]+self.b)^2*(-coord[1]+self.c)*(-coord[1]+self.d)^2

    def partialGxy837(self,coord):

        return (-coord[0]+self.a)*(-coord[0]+self.b)^2*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2

    def partialGxy838(self,coord):

        return (-coord[0]+self.a)*(-coord[0]+self.b)^2*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2

    def partialGxy839(self,coord):

        return (-coord[0]+self.a)*(-coord[0]+self.b)^2*(-coord[1]+self.c)^4*(-coord[1]+self.d)^2

    def partialGxy840(self,coord):

        return (-coord[0]+self.a)*(-coord[0]+self.b)^2*(-coord[1]+self.d)^3

    def partialGxy841(self,coord):

        return (-coord[0]+self.a)*(-coord[0]+self.b)^2*(-coord[1]+self.c)*(-coord[1]+self.d)^3

    def partialGxy842(self,coord):

        return (-coord[0]+self.a)*(-coord[0]+self.b)^2*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3

    def partialGxy843(self,coord):

        return (-coord[0]+self.a)*(-coord[0]+self.b)^2*(-coord[1]+self.c)^3*(-coord[1]+self.d)^3

    def partialGxy844(self,coord):

        return (-coord[0]+self.a)*(-coord[0]+self.b)^2*(-coord[1]+self.c)^4*(-coord[1]+self.d)^3

    def partialGxy845(self,coord):

        return (-coord[0]+self.a)*(-coord[0]+self.b)^2*(-coord[1]+self.d)^4

    def partialGxy846(self,coord):

        return (-coord[0]+self.a)*(-coord[0]+self.b)^2*(-coord[1]+self.c)*(-coord[1]+self.d)^4

    def partialGxy847(self,coord):

        return (-coord[0]+self.a)*(-coord[0]+self.b)^2*(-coord[1]+self.c)^2*(-coord[1]+self.d)^4

    def partialGxy848(self,coord):

        return (-coord[0]+self.a)*(-coord[0]+self.b)^2*(-coord[1]+self.c)^3*(-coord[1]+self.d)^4

    def partialGxy849(self,coord):

        return (-coord[0]+self.a)*(-coord[0]+self.b)^2*(-coord[1]+self.c)^4*(-coord[1]+self.d)^4

    def partialGxy856(self,coord):

        return (-coord[0]+self.a)*(-coord[0]+self.b)^2*(-coord[1]+self.c)+(-coord[0]+self.a)*(-coord[0]+self.b)^2*(-coord[1]+self.d)

    def partialGxy857(self,coord):

        return (-coord[0]+self.a)*(-coord[0]+self.b)^2*(-coord[1]+self.c)^2+2*(-coord[0]+self.a)*(-coord[0]+self.b)^2*(-coord[1]+self.c)*(-coord[1]+self.d)

    def partialGxy858(self,coord):

        return (-coord[0]+self.a)*(-coord[0]+self.b)^2*(-coord[1]+self.c)^3+3*(-coord[0]+self.a)*(-coord[0]+self.b)^2*(-coord[1]+self.c)^2*(-coord[1]+self.d)

    def partialGxy859(self,coord):

        return (-coord[0]+self.a)*(-coord[0]+self.b)^2*(-coord[1]+self.c)^4+4*(-coord[0]+self.a)*(-coord[0]+self.b)^2*(-coord[1]+self.c)^3*(-coord[1]+self.d)

    def partialGxy861(self,coord):

        return 2*(-coord[0]+self.a)*(-coord[0]+self.b)^2*(-coord[1]+self.c)*(-coord[1]+self.d)+(-coord[0]+self.a)*(-coord[0]+self.b)^2*(-coord[1]+self.d)^2

    def partialGxy862(self,coord):

        return 2*(-coord[0]+self.a)*(-coord[0]+self.b)^2*(-coord[1]+self.c)^2*(-coord[1]+self.d)+2*(-coord[0]+self.a)*(-coord[0]+self.b)^2*(-coord[1]+self.c)*(-coord[1]+self.d)^2

    def partialGxy863(self,coord):

        return 2*(-coord[0]+self.a)*(-coord[0]+self.b)^2*(-coord[1]+self.c)^3*(-coord[1]+self.d)+3*(-coord[0]+self.a)*(-coord[0]+self.b)^2*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2

    def partialGxy864(self,coord):

        return 2*(-coord[0]+self.a)*(-coord[0]+self.b)^2*(-coord[1]+self.c)^4*(-coord[1]+self.d)+4*(-coord[0]+self.a)*(-coord[0]+self.b)^2*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2

    def partialGxy866(self,coord):

        return 3*(-coord[0]+self.a)*(-coord[0]+self.b)^2*(-coord[1]+self.c)*(-coord[1]+self.d)^2+(-coord[0]+self.a)*(-coord[0]+self.b)^2*(-coord[1]+self.d)^3

    def partialGxy867(self,coord):

        return 3*(-coord[0]+self.a)*(-coord[0]+self.b)^2*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2+2*(-coord[0]+self.a)*(-coord[0]+self.b)^2*(-coord[1]+self.c)*(-coord[1]+self.d)^3

    def partialGxy868(self,coord):

        return 3*(-coord[0]+self.a)*(-coord[0]+self.b)^2*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2+3*(-coord[0]+self.a)*(-coord[0]+self.b)^2*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3

    def partialGxy869(self,coord):

        return 3*(-coord[0]+self.a)*(-coord[0]+self.b)^2*(-coord[1]+self.c)^4*(-coord[1]+self.d)^2+4*(-coord[0]+self.a)*(-coord[0]+self.b)^2*(-coord[1]+self.c)^3*(-coord[1]+self.d)^3

    def partialGxy871(self,coord):

        return 4*(-coord[0]+self.a)*(-coord[0]+self.b)^2*(-coord[1]+self.c)*(-coord[1]+self.d)^3+(-coord[0]+self.a)*(-coord[0]+self.b)^2*(-coord[1]+self.d)^4

    def partialGxy872(self,coord):

        return 4*(-coord[0]+self.a)*(-coord[0]+self.b)^2*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3+2*(-coord[0]+self.a)*(-coord[0]+self.b)^2*(-coord[1]+self.c)*(-coord[1]+self.d)^4

    def partialGxy873(self,coord):

        return 4*(-coord[0]+self.a)*(-coord[0]+self.b)^2*(-coord[1]+self.c)^3*(-coord[1]+self.d)^3+3*(-coord[0]+self.a)*(-coord[0]+self.b)^2*(-coord[1]+self.c)^2*(-coord[1]+self.d)^4

    def partialGxy874(self,coord):

        return 4*(-coord[0]+self.a)*(-coord[0]+self.b)^2*(-coord[1]+self.c)^4*(-coord[1]+self.d)^3+4*(-coord[0]+self.a)*(-coord[0]+self.b)^2*(-coord[1]+self.c)^3*(-coord[1]+self.d)^4

    def partialGxy887(self,coord):

        return (-coord[0]+self.a)*(-coord[0]+self.b)^2*(2*(-coord[1]+self.c)^2+8*(-coord[1]+self.c)*(-coord[1]+self.d)+2*(-coord[1]+self.d)^2)

    def partialGxy888(self,coord):

        return (-coord[0]+self.a)*(-coord[0]+self.b)^2*(2*(-coord[1]+self.c)^3+12*(-coord[1]+self.c)^2*(-coord[1]+self.d)+6*(-coord[1]+self.c)*(-coord[1]+self.d)^2)

    def partialGxy889(self,coord):

        return (-coord[0]+self.a)*(-coord[0]+self.b)^2*(2*(-coord[1]+self.c)^4+16*(-coord[1]+self.c)^3*(-coord[1]+self.d)+12*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2)

    def partialGxy892(self,coord):

        return (-coord[0]+self.a)*(-coord[0]+self.b)^2*(6*(-coord[1]+self.c)^2*(-coord[1]+self.d)+12*(-coord[1]+self.c)*(-coord[1]+self.d)^2+2*(-coord[1]+self.d)^3)

    def partialGxy893(self,coord):

        return (-coord[0]+self.a)*(-coord[0]+self.b)^2*(6*(-coord[1]+self.c)^3*(-coord[1]+self.d)+18*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2+6*(-coord[1]+self.c)*(-coord[1]+self.d)^3)

    def partialGxy894(self,coord):

        return (-coord[0]+self.a)*(-coord[0]+self.b)^2*(6*(-coord[1]+self.c)^4*(-coord[1]+self.d)+24*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2+12*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3)

    def partialGxy897(self,coord):

        return (-coord[0]+self.a)*(-coord[0]+self.b)^2*(12*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2+16*(-coord[1]+self.c)*(-coord[1]+self.d)^3+2*(-coord[1]+self.d)^4)

    def partialGxy898(self,coord):

        return (-coord[0]+self.a)*(-coord[0]+self.b)^2*(12*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2+24*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3+6*(-coord[1]+self.c)*(-coord[1]+self.d)^4)

    def partialGxy899(self,coord):

        return (-coord[0]+self.a)*(-coord[0]+self.b)^2*(12*(-coord[1]+self.c)^4*(-coord[1]+self.d)^2+32*(-coord[1]+self.c)^3*(-coord[1]+self.d)^3+12*(-coord[1]+self.c)^2*(-coord[1]+self.d)^4)

    def partialGxy900(self,coord):

        return (-coord[0]+self.a)^2*(-coord[0]+self.b)^2

    def partialGxy901(self,coord):

        return (-coord[0]+self.a)^2*(-coord[0]+self.b)^2*(-coord[1]+self.c)

    def partialGxy902(self,coord):

        return (-coord[0]+self.a)^2*(-coord[0]+self.b)^2*(-coord[1]+self.c)^2

    def partialGxy903(self,coord):

        return (-coord[0]+self.a)^2*(-coord[0]+self.b)^2*(-coord[1]+self.c)^3

    def partialGxy904(self,coord):

        return (-coord[0]+self.a)^2*(-coord[0]+self.b)^2*(-coord[1]+self.c)^4

    def partialGxy905(self,coord):

        return (-coord[0]+self.a)^2*(-coord[0]+self.b)^2*(-coord[1]+self.d)

    def partialGxy906(self,coord):

        return (-coord[0]+self.a)^2*(-coord[0]+self.b)^2*(-coord[1]+self.c)*(-coord[1]+self.d)

    def partialGxy907(self,coord):

        return (-coord[0]+self.a)^2*(-coord[0]+self.b)^2*(-coord[1]+self.c)^2*(-coord[1]+self.d)

    def partialGxy908(self,coord):

        return (-coord[0]+self.a)^2*(-coord[0]+self.b)^2*(-coord[1]+self.c)^3*(-coord[1]+self.d)

    def partialGxy909(self,coord):

        return (-coord[0]+self.a)^2*(-coord[0]+self.b)^2*(-coord[1]+self.c)^4*(-coord[1]+self.d)

    def partialGxy910(self,coord):

        return (-coord[0]+self.a)^2*(-coord[0]+self.b)^2*(-coord[1]+self.d)^2

    def partialGxy911(self,coord):

        return (-coord[0]+self.a)^2*(-coord[0]+self.b)^2*(-coord[1]+self.c)*(-coord[1]+self.d)^2

    def partialGxy912(self,coord):

        return (-coord[0]+self.a)^2*(-coord[0]+self.b)^2*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2

    def partialGxy913(self,coord):

        return (-coord[0]+self.a)^2*(-coord[0]+self.b)^2*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2

    def partialGxy914(self,coord):

        return (-coord[0]+self.a)^2*(-coord[0]+self.b)^2*(-coord[1]+self.c)^4*(-coord[1]+self.d)^2

    def partialGxy915(self,coord):

        return (-coord[0]+self.a)^2*(-coord[0]+self.b)^2*(-coord[1]+self.d)^3

    def partialGxy916(self,coord):

        return (-coord[0]+self.a)^2*(-coord[0]+self.b)^2*(-coord[1]+self.c)*(-coord[1]+self.d)^3

    def partialGxy917(self,coord):

        return (-coord[0]+self.a)^2*(-coord[0]+self.b)^2*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3

    def partialGxy918(self,coord):

        return (-coord[0]+self.a)^2*(-coord[0]+self.b)^2*(-coord[1]+self.c)^3*(-coord[1]+self.d)^3

    def partialGxy919(self,coord):

        return (-coord[0]+self.a)^2*(-coord[0]+self.b)^2*(-coord[1]+self.c)^4*(-coord[1]+self.d)^3

    def partialGxy920(self,coord):

        return (-coord[0]+self.a)^2*(-coord[0]+self.b)^2*(-coord[1]+self.d)^4

    def partialGxy921(self,coord):

        return (-coord[0]+self.a)^2*(-coord[0]+self.b)^2*(-coord[1]+self.c)*(-coord[1]+self.d)^4

    def partialGxy922(self,coord):

        return (-coord[0]+self.a)^2*(-coord[0]+self.b)^2*(-coord[1]+self.c)^2*(-coord[1]+self.d)^4

    def partialGxy923(self,coord):

        return (-coord[0]+self.a)^2*(-coord[0]+self.b)^2*(-coord[1]+self.c)^3*(-coord[1]+self.d)^4

    def partialGxy924(self,coord):

        return (-coord[0]+self.a)^2*(-coord[0]+self.b)^2*(-coord[1]+self.c)^4*(-coord[1]+self.d)^4

    def partialGxy931(self,coord):

        return (-coord[0]+self.a)^2*(-coord[0]+self.b)^2*(-coord[1]+self.c)+(-coord[0]+self.a)^2*(-coord[0]+self.b)^2*(-coord[1]+self.d)

    def partialGxy932(self,coord):

        return (-coord[0]+self.a)^2*(-coord[0]+self.b)^2*(-coord[1]+self.c)^2+2*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2*(-coord[1]+self.c)*(-coord[1]+self.d)

    def partialGxy933(self,coord):

        return (-coord[0]+self.a)^2*(-coord[0]+self.b)^2*(-coord[1]+self.c)^3+3*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2*(-coord[1]+self.c)^2*(-coord[1]+self.d)

    def partialGxy934(self,coord):

        return (-coord[0]+self.a)^2*(-coord[0]+self.b)^2*(-coord[1]+self.c)^4+4*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2*(-coord[1]+self.c)^3*(-coord[1]+self.d)

    def partialGxy936(self,coord):

        return 2*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2*(-coord[1]+self.c)*(-coord[1]+self.d)+(-coord[0]+self.a)^2*(-coord[0]+self.b)^2*(-coord[1]+self.d)^2

    def partialGxy937(self,coord):

        return 2*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2*(-coord[1]+self.c)^2*(-coord[1]+self.d)+2*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2*(-coord[1]+self.c)*(-coord[1]+self.d)^2

    def partialGxy938(self,coord):

        return 2*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2*(-coord[1]+self.c)^3*(-coord[1]+self.d)+3*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2

    def partialGxy939(self,coord):

        return 2*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2*(-coord[1]+self.c)^4*(-coord[1]+self.d)+4*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2

    def partialGxy941(self,coord):

        return 3*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2*(-coord[1]+self.c)*(-coord[1]+self.d)^2+(-coord[0]+self.a)^2*(-coord[0]+self.b)^2*(-coord[1]+self.d)^3

    def partialGxy942(self,coord):

        return 3*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2+2*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2*(-coord[1]+self.c)*(-coord[1]+self.d)^3

    def partialGxy943(self,coord):

        return 3*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2+3*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3

    def partialGxy944(self,coord):

        return 3*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2*(-coord[1]+self.c)^4*(-coord[1]+self.d)^2+4*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2*(-coord[1]+self.c)^3*(-coord[1]+self.d)^3

    def partialGxy946(self,coord):

        return 4*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2*(-coord[1]+self.c)*(-coord[1]+self.d)^3+(-coord[0]+self.a)^2*(-coord[0]+self.b)^2*(-coord[1]+self.d)^4

    def partialGxy947(self,coord):

        return 4*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3+2*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2*(-coord[1]+self.c)*(-coord[1]+self.d)^4

    def partialGxy948(self,coord):

        return 4*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2*(-coord[1]+self.c)^3*(-coord[1]+self.d)^3+3*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2*(-coord[1]+self.c)^2*(-coord[1]+self.d)^4

    def partialGxy949(self,coord):

        return 4*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2*(-coord[1]+self.c)^4*(-coord[1]+self.d)^3+4*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2*(-coord[1]+self.c)^3*(-coord[1]+self.d)^4

    def partialGxy962(self,coord):

        return (-coord[0]+self.a)^2*(-coord[0]+self.b)^2*(2*(-coord[1]+self.c)^2+8*(-coord[1]+self.c)*(-coord[1]+self.d)+2*(-coord[1]+self.d)^2)

    def partialGxy963(self,coord):

        return (-coord[0]+self.a)^2*(-coord[0]+self.b)^2*(2*(-coord[1]+self.c)^3+12*(-coord[1]+self.c)^2*(-coord[1]+self.d)+6*(-coord[1]+self.c)*(-coord[1]+self.d)^2)

    def partialGxy964(self,coord):

        return (-coord[0]+self.a)^2*(-coord[0]+self.b)^2*(2*(-coord[1]+self.c)^4+16*(-coord[1]+self.c)^3*(-coord[1]+self.d)+12*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2)

    def partialGxy967(self,coord):

        return (-coord[0]+self.a)^2*(-coord[0]+self.b)^2*(6*(-coord[1]+self.c)^2*(-coord[1]+self.d)+12*(-coord[1]+self.c)*(-coord[1]+self.d)^2+2*(-coord[1]+self.d)^3)

    def partialGxy968(self,coord):

        return (-coord[0]+self.a)^2*(-coord[0]+self.b)^2*(6*(-coord[1]+self.c)^3*(-coord[1]+self.d)+18*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2+6*(-coord[1]+self.c)*(-coord[1]+self.d)^3)

    def partialGxy969(self,coord):

        return (-coord[0]+self.a)^2*(-coord[0]+self.b)^2*(6*(-coord[1]+self.c)^4*(-coord[1]+self.d)+24*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2+12*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3)

    def partialGxy972(self,coord):

        return (-coord[0]+self.a)^2*(-coord[0]+self.b)^2*(12*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2+16*(-coord[1]+self.c)*(-coord[1]+self.d)^3+2*(-coord[1]+self.d)^4)

    def partialGxy973(self,coord):

        return (-coord[0]+self.a)^2*(-coord[0]+self.b)^2*(12*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2+24*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3+6*(-coord[1]+self.c)*(-coord[1]+self.d)^4)

    def partialGxy974(self,coord):

        return (-coord[0]+self.a)^2*(-coord[0]+self.b)^2*(12*(-coord[1]+self.c)^4*(-coord[1]+self.d)^2+32*(-coord[1]+self.c)^3*(-coord[1]+self.d)^3+12*(-coord[1]+self.c)^2*(-coord[1]+self.d)^4)

    def partialGxy975(self,coord):

        return (-coord[0]+self.a)^3*(-coord[0]+self.b)^2

    def partialGxy976(self,coord):

        return (-coord[0]+self.a)^3*(-coord[0]+self.b)^2*(-coord[1]+self.c)

    def partialGxy977(self,coord):

        return (-coord[0]+self.a)^3*(-coord[0]+self.b)^2*(-coord[1]+self.c)^2

    def partialGxy978(self,coord):

        return (-coord[0]+self.a)^3*(-coord[0]+self.b)^2*(-coord[1]+self.c)^3

    def partialGxy979(self,coord):

        return (-coord[0]+self.a)^3*(-coord[0]+self.b)^2*(-coord[1]+self.c)^4

    def partialGxy980(self,coord):

        return (-coord[0]+self.a)^3*(-coord[0]+self.b)^2*(-coord[1]+self.d)

    def partialGxy981(self,coord):

        return (-coord[0]+self.a)^3*(-coord[0]+self.b)^2*(-coord[1]+self.c)*(-coord[1]+self.d)

    def partialGxy982(self,coord):

        return (-coord[0]+self.a)^3*(-coord[0]+self.b)^2*(-coord[1]+self.c)^2*(-coord[1]+self.d)

    def partialGxy983(self,coord):

        return (-coord[0]+self.a)^3*(-coord[0]+self.b)^2*(-coord[1]+self.c)^3*(-coord[1]+self.d)

    def partialGxy984(self,coord):

        return (-coord[0]+self.a)^3*(-coord[0]+self.b)^2*(-coord[1]+self.c)^4*(-coord[1]+self.d)

    def partialGxy985(self,coord):

        return (-coord[0]+self.a)^3*(-coord[0]+self.b)^2*(-coord[1]+self.d)^2

    def partialGxy986(self,coord):

        return (-coord[0]+self.a)^3*(-coord[0]+self.b)^2*(-coord[1]+self.c)*(-coord[1]+self.d)^2

    def partialGxy987(self,coord):

        return (-coord[0]+self.a)^3*(-coord[0]+self.b)^2*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2

    def partialGxy988(self,coord):

        return (-coord[0]+self.a)^3*(-coord[0]+self.b)^2*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2

    def partialGxy989(self,coord):

        return (-coord[0]+self.a)^3*(-coord[0]+self.b)^2*(-coord[1]+self.c)^4*(-coord[1]+self.d)^2

    def partialGxy990(self,coord):

        return (-coord[0]+self.a)^3*(-coord[0]+self.b)^2*(-coord[1]+self.d)^3

    def partialGxy991(self,coord):

        return (-coord[0]+self.a)^3*(-coord[0]+self.b)^2*(-coord[1]+self.c)*(-coord[1]+self.d)^3

    def partialGxy992(self,coord):

        return (-coord[0]+self.a)^3*(-coord[0]+self.b)^2*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3

    def partialGxy993(self,coord):

        return (-coord[0]+self.a)^3*(-coord[0]+self.b)^2*(-coord[1]+self.c)^3*(-coord[1]+self.d)^3

    def partialGxy994(self,coord):

        return (-coord[0]+self.a)^3*(-coord[0]+self.b)^2*(-coord[1]+self.c)^4*(-coord[1]+self.d)^3

    def partialGxy995(self,coord):

        return (-coord[0]+self.a)^3*(-coord[0]+self.b)^2*(-coord[1]+self.d)^4

    def partialGxy996(self,coord):

        return (-coord[0]+self.a)^3*(-coord[0]+self.b)^2*(-coord[1]+self.c)*(-coord[1]+self.d)^4

    def partialGxy997(self,coord):

        return (-coord[0]+self.a)^3*(-coord[0]+self.b)^2*(-coord[1]+self.c)^2*(-coord[1]+self.d)^4

    def partialGxy998(self,coord):

        return (-coord[0]+self.a)^3*(-coord[0]+self.b)^2*(-coord[1]+self.c)^3*(-coord[1]+self.d)^4

    def partialGxy999(self,coord):

        return (-coord[0]+self.a)^3*(-coord[0]+self.b)^2*(-coord[1]+self.c)^4*(-coord[1]+self.d)^4

    def partialGxy1006(self,coord):

        return (-coord[0]+self.a)^3*(-coord[0]+self.b)^2*(-coord[1]+self.c)+(-coord[0]+self.a)^3*(-coord[0]+self.b)^2*(-coord[1]+self.d)

    def partialGxy1007(self,coord):

        return (-coord[0]+self.a)^3*(-coord[0]+self.b)^2*(-coord[1]+self.c)^2+2*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2*(-coord[1]+self.c)*(-coord[1]+self.d)

    def partialGxy1008(self,coord):

        return (-coord[0]+self.a)^3*(-coord[0]+self.b)^2*(-coord[1]+self.c)^3+3*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2*(-coord[1]+self.c)^2*(-coord[1]+self.d)

    def partialGxy1009(self,coord):

        return (-coord[0]+self.a)^3*(-coord[0]+self.b)^2*(-coord[1]+self.c)^4+4*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2*(-coord[1]+self.c)^3*(-coord[1]+self.d)

    def partialGxy1011(self,coord):

        return 2*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2*(-coord[1]+self.c)*(-coord[1]+self.d)+(-coord[0]+self.a)^3*(-coord[0]+self.b)^2*(-coord[1]+self.d)^2

    def partialGxy1012(self,coord):

        return 2*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2*(-coord[1]+self.c)^2*(-coord[1]+self.d)+2*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2*(-coord[1]+self.c)*(-coord[1]+self.d)^2

    def partialGxy1013(self,coord):

        return 2*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2*(-coord[1]+self.c)^3*(-coord[1]+self.d)+3*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2

    def partialGxy1014(self,coord):

        return 2*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2*(-coord[1]+self.c)^4*(-coord[1]+self.d)+4*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2

    def partialGxy1016(self,coord):

        return 3*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2*(-coord[1]+self.c)*(-coord[1]+self.d)^2+(-coord[0]+self.a)^3*(-coord[0]+self.b)^2*(-coord[1]+self.d)^3

    def partialGxy1017(self,coord):

        return 3*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2+2*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2*(-coord[1]+self.c)*(-coord[1]+self.d)^3

    def partialGxy1018(self,coord):

        return 3*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2+3*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3

    def partialGxy1019(self,coord):

        return 3*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2*(-coord[1]+self.c)^4*(-coord[1]+self.d)^2+4*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2*(-coord[1]+self.c)^3*(-coord[1]+self.d)^3

    def partialGxy1021(self,coord):

        return 4*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2*(-coord[1]+self.c)*(-coord[1]+self.d)^3+(-coord[0]+self.a)^3*(-coord[0]+self.b)^2*(-coord[1]+self.d)^4

    def partialGxy1022(self,coord):

        return 4*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3+2*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2*(-coord[1]+self.c)*(-coord[1]+self.d)^4

    def partialGxy1023(self,coord):

        return 4*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2*(-coord[1]+self.c)^3*(-coord[1]+self.d)^3+3*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2*(-coord[1]+self.c)^2*(-coord[1]+self.d)^4

    def partialGxy1024(self,coord):

        return 4*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2*(-coord[1]+self.c)^4*(-coord[1]+self.d)^3+4*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2*(-coord[1]+self.c)^3*(-coord[1]+self.d)^4

    def partialGxy1037(self,coord):

        return (-coord[0]+self.a)^3*(-coord[0]+self.b)^2*(2*(-coord[1]+self.c)^2+8*(-coord[1]+self.c)*(-coord[1]+self.d)+2*(-coord[1]+self.d)^2)

    def partialGxy1038(self,coord):

        return (-coord[0]+self.a)^3*(-coord[0]+self.b)^2*(2*(-coord[1]+self.c)^3+12*(-coord[1]+self.c)^2*(-coord[1]+self.d)+6*(-coord[1]+self.c)*(-coord[1]+self.d)^2)

    def partialGxy1039(self,coord):

        return (-coord[0]+self.a)^3*(-coord[0]+self.b)^2*(2*(-coord[1]+self.c)^4+16*(-coord[1]+self.c)^3*(-coord[1]+self.d)+12*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2)

    def partialGxy1042(self,coord):

        return (-coord[0]+self.a)^3*(-coord[0]+self.b)^2*(6*(-coord[1]+self.c)^2*(-coord[1]+self.d)+12*(-coord[1]+self.c)*(-coord[1]+self.d)^2+2*(-coord[1]+self.d)^3)

    def partialGxy1043(self,coord):

        return (-coord[0]+self.a)^3*(-coord[0]+self.b)^2*(6*(-coord[1]+self.c)^3*(-coord[1]+self.d)+18*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2+6*(-coord[1]+self.c)*(-coord[1]+self.d)^3)

    def partialGxy1044(self,coord):

        return (-coord[0]+self.a)^3*(-coord[0]+self.b)^2*(6*(-coord[1]+self.c)^4*(-coord[1]+self.d)+24*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2+12*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3)

    def partialGxy1047(self,coord):

        return (-coord[0]+self.a)^3*(-coord[0]+self.b)^2*(12*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2+16*(-coord[1]+self.c)*(-coord[1]+self.d)^3+2*(-coord[1]+self.d)^4)

    def partialGxy1048(self,coord):

        return (-coord[0]+self.a)^3*(-coord[0]+self.b)^2*(12*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2+24*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3+6*(-coord[1]+self.c)*(-coord[1]+self.d)^4)

    def partialGxy1049(self,coord):

        return (-coord[0]+self.a)^3*(-coord[0]+self.b)^2*(12*(-coord[1]+self.c)^4*(-coord[1]+self.d)^2+32*(-coord[1]+self.c)^3*(-coord[1]+self.d)^3+12*(-coord[1]+self.c)^2*(-coord[1]+self.d)^4)

    def partialGxy1050(self,coord):

        return (-coord[0]+self.a)^4*(-coord[0]+self.b)^2

    def partialGxy1051(self,coord):

        return (-coord[0]+self.a)^4*(-coord[0]+self.b)^2*(-coord[1]+self.c)

    def partialGxy1052(self,coord):

        return (-coord[0]+self.a)^4*(-coord[0]+self.b)^2*(-coord[1]+self.c)^2

    def partialGxy1053(self,coord):

        return (-coord[0]+self.a)^4*(-coord[0]+self.b)^2*(-coord[1]+self.c)^3

    def partialGxy1054(self,coord):

        return (-coord[0]+self.a)^4*(-coord[0]+self.b)^2*(-coord[1]+self.c)^4

    def partialGxy1055(self,coord):

        return (-coord[0]+self.a)^4*(-coord[0]+self.b)^2*(-coord[1]+self.d)

    def partialGxy1056(self,coord):

        return (-coord[0]+self.a)^4*(-coord[0]+self.b)^2*(-coord[1]+self.c)*(-coord[1]+self.d)

    def partialGxy1057(self,coord):

        return (-coord[0]+self.a)^4*(-coord[0]+self.b)^2*(-coord[1]+self.c)^2*(-coord[1]+self.d)

    def partialGxy1058(self,coord):

        return (-coord[0]+self.a)^4*(-coord[0]+self.b)^2*(-coord[1]+self.c)^3*(-coord[1]+self.d)

    def partialGxy1059(self,coord):

        return (-coord[0]+self.a)^4*(-coord[0]+self.b)^2*(-coord[1]+self.c)^4*(-coord[1]+self.d)

    def partialGxy1060(self,coord):

        return (-coord[0]+self.a)^4*(-coord[0]+self.b)^2*(-coord[1]+self.d)^2

    def partialGxy1061(self,coord):

        return (-coord[0]+self.a)^4*(-coord[0]+self.b)^2*(-coord[1]+self.c)*(-coord[1]+self.d)^2

    def partialGxy1062(self,coord):

        return (-coord[0]+self.a)^4*(-coord[0]+self.b)^2*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2

    def partialGxy1063(self,coord):

        return (-coord[0]+self.a)^4*(-coord[0]+self.b)^2*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2

    def partialGxy1064(self,coord):

        return (-coord[0]+self.a)^4*(-coord[0]+self.b)^2*(-coord[1]+self.c)^4*(-coord[1]+self.d)^2

    def partialGxy1065(self,coord):

        return (-coord[0]+self.a)^4*(-coord[0]+self.b)^2*(-coord[1]+self.d)^3

    def partialGxy1066(self,coord):

        return (-coord[0]+self.a)^4*(-coord[0]+self.b)^2*(-coord[1]+self.c)*(-coord[1]+self.d)^3

    def partialGxy1067(self,coord):

        return (-coord[0]+self.a)^4*(-coord[0]+self.b)^2*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3

    def partialGxy1068(self,coord):

        return (-coord[0]+self.a)^4*(-coord[0]+self.b)^2*(-coord[1]+self.c)^3*(-coord[1]+self.d)^3

    def partialGxy1069(self,coord):

        return (-coord[0]+self.a)^4*(-coord[0]+self.b)^2*(-coord[1]+self.c)^4*(-coord[1]+self.d)^3

    def partialGxy1070(self,coord):

        return (-coord[0]+self.a)^4*(-coord[0]+self.b)^2*(-coord[1]+self.d)^4

    def partialGxy1071(self,coord):

        return (-coord[0]+self.a)^4*(-coord[0]+self.b)^2*(-coord[1]+self.c)*(-coord[1]+self.d)^4

    def partialGxy1072(self,coord):

        return (-coord[0]+self.a)^4*(-coord[0]+self.b)^2*(-coord[1]+self.c)^2*(-coord[1]+self.d)^4

    def partialGxy1073(self,coord):

        return (-coord[0]+self.a)^4*(-coord[0]+self.b)^2*(-coord[1]+self.c)^3*(-coord[1]+self.d)^4

    def partialGxy1074(self,coord):

        return (-coord[0]+self.a)^4*(-coord[0]+self.b)^2*(-coord[1]+self.c)^4*(-coord[1]+self.d)^4

    def partialGxy1081(self,coord):

        return (-coord[0]+self.a)^4*(-coord[0]+self.b)^2*(-coord[1]+self.c)+(-coord[0]+self.a)^4*(-coord[0]+self.b)^2*(-coord[1]+self.d)

    def partialGxy1082(self,coord):

        return (-coord[0]+self.a)^4*(-coord[0]+self.b)^2*(-coord[1]+self.c)^2+2*(-coord[0]+self.a)^4*(-coord[0]+self.b)^2*(-coord[1]+self.c)*(-coord[1]+self.d)

    def partialGxy1083(self,coord):

        return (-coord[0]+self.a)^4*(-coord[0]+self.b)^2*(-coord[1]+self.c)^3+3*(-coord[0]+self.a)^4*(-coord[0]+self.b)^2*(-coord[1]+self.c)^2*(-coord[1]+self.d)

    def partialGxy1084(self,coord):

        return (-coord[0]+self.a)^4*(-coord[0]+self.b)^2*(-coord[1]+self.c)^4+4*(-coord[0]+self.a)^4*(-coord[0]+self.b)^2*(-coord[1]+self.c)^3*(-coord[1]+self.d)

    def partialGxy1086(self,coord):

        return 2*(-coord[0]+self.a)^4*(-coord[0]+self.b)^2*(-coord[1]+self.c)*(-coord[1]+self.d)+(-coord[0]+self.a)^4*(-coord[0]+self.b)^2*(-coord[1]+self.d)^2

    def partialGxy1087(self,coord):

        return 2*(-coord[0]+self.a)^4*(-coord[0]+self.b)^2*(-coord[1]+self.c)^2*(-coord[1]+self.d)+2*(-coord[0]+self.a)^4*(-coord[0]+self.b)^2*(-coord[1]+self.c)*(-coord[1]+self.d)^2

    def partialGxy1088(self,coord):

        return 2*(-coord[0]+self.a)^4*(-coord[0]+self.b)^2*(-coord[1]+self.c)^3*(-coord[1]+self.d)+3*(-coord[0]+self.a)^4*(-coord[0]+self.b)^2*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2

    def partialGxy1089(self,coord):

        return 2*(-coord[0]+self.a)^4*(-coord[0]+self.b)^2*(-coord[1]+self.c)^4*(-coord[1]+self.d)+4*(-coord[0]+self.a)^4*(-coord[0]+self.b)^2*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2

    def partialGxy1091(self,coord):

        return 3*(-coord[0]+self.a)^4*(-coord[0]+self.b)^2*(-coord[1]+self.c)*(-coord[1]+self.d)^2+(-coord[0]+self.a)^4*(-coord[0]+self.b)^2*(-coord[1]+self.d)^3

    def partialGxy1092(self,coord):

        return 3*(-coord[0]+self.a)^4*(-coord[0]+self.b)^2*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2+2*(-coord[0]+self.a)^4*(-coord[0]+self.b)^2*(-coord[1]+self.c)*(-coord[1]+self.d)^3

    def partialGxy1093(self,coord):

        return 3*(-coord[0]+self.a)^4*(-coord[0]+self.b)^2*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2+3*(-coord[0]+self.a)^4*(-coord[0]+self.b)^2*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3

    def partialGxy1094(self,coord):

        return 3*(-coord[0]+self.a)^4*(-coord[0]+self.b)^2*(-coord[1]+self.c)^4*(-coord[1]+self.d)^2+4*(-coord[0]+self.a)^4*(-coord[0]+self.b)^2*(-coord[1]+self.c)^3*(-coord[1]+self.d)^3

    def partialGxy1096(self,coord):

        return 4*(-coord[0]+self.a)^4*(-coord[0]+self.b)^2*(-coord[1]+self.c)*(-coord[1]+self.d)^3+(-coord[0]+self.a)^4*(-coord[0]+self.b)^2*(-coord[1]+self.d)^4

    def partialGxy1097(self,coord):

        return 4*(-coord[0]+self.a)^4*(-coord[0]+self.b)^2*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3+2*(-coord[0]+self.a)^4*(-coord[0]+self.b)^2*(-coord[1]+self.c)*(-coord[1]+self.d)^4

    def partialGxy1098(self,coord):

        return 4*(-coord[0]+self.a)^4*(-coord[0]+self.b)^2*(-coord[1]+self.c)^3*(-coord[1]+self.d)^3+3*(-coord[0]+self.a)^4*(-coord[0]+self.b)^2*(-coord[1]+self.c)^2*(-coord[1]+self.d)^4

    def partialGxy1099(self,coord):

        return 4*(-coord[0]+self.a)^4*(-coord[0]+self.b)^2*(-coord[1]+self.c)^4*(-coord[1]+self.d)^3+4*(-coord[0]+self.a)^4*(-coord[0]+self.b)^2*(-coord[1]+self.c)^3*(-coord[1]+self.d)^4

    def partialGxy1112(self,coord):

        return (-coord[0]+self.a)^4*(-coord[0]+self.b)^2*(2*(-coord[1]+self.c)^2+8*(-coord[1]+self.c)*(-coord[1]+self.d)+2*(-coord[1]+self.d)^2)

    def partialGxy1113(self,coord):

        return (-coord[0]+self.a)^4*(-coord[0]+self.b)^2*(2*(-coord[1]+self.c)^3+12*(-coord[1]+self.c)^2*(-coord[1]+self.d)+6*(-coord[1]+self.c)*(-coord[1]+self.d)^2)

    def partialGxy1114(self,coord):

        return (-coord[0]+self.a)^4*(-coord[0]+self.b)^2*(2*(-coord[1]+self.c)^4+16*(-coord[1]+self.c)^3*(-coord[1]+self.d)+12*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2)

    def partialGxy1117(self,coord):

        return (-coord[0]+self.a)^4*(-coord[0]+self.b)^2*(6*(-coord[1]+self.c)^2*(-coord[1]+self.d)+12*(-coord[1]+self.c)*(-coord[1]+self.d)^2+2*(-coord[1]+self.d)^3)

    def partialGxy1118(self,coord):

        return (-coord[0]+self.a)^4*(-coord[0]+self.b)^2*(6*(-coord[1]+self.c)^3*(-coord[1]+self.d)+18*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2+6*(-coord[1]+self.c)*(-coord[1]+self.d)^3)

    def partialGxy1119(self,coord):

        return (-coord[0]+self.a)^4*(-coord[0]+self.b)^2*(6*(-coord[1]+self.c)^4*(-coord[1]+self.d)+24*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2+12*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3)

    def partialGxy1122(self,coord):

        return (-coord[0]+self.a)^4*(-coord[0]+self.b)^2*(12*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2+16*(-coord[1]+self.c)*(-coord[1]+self.d)^3+2*(-coord[1]+self.d)^4)

    def partialGxy1123(self,coord):

        return (-coord[0]+self.a)^4*(-coord[0]+self.b)^2*(12*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2+24*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3+6*(-coord[1]+self.c)*(-coord[1]+self.d)^4)

    def partialGxy1124(self,coord):

        return (-coord[0]+self.a)^4*(-coord[0]+self.b)^2*(12*(-coord[1]+self.c)^4*(-coord[1]+self.d)^2+32*(-coord[1]+self.c)^3*(-coord[1]+self.d)^3+12*(-coord[1]+self.c)^2*(-coord[1]+self.d)^4)

    def partialGxy1125(self,coord):

        return (-coord[0]+self.b)^3

    def partialGxy1126(self,coord):

        return (-coord[0]+self.b)^3*(-coord[1]+self.c)

    def partialGxy1127(self,coord):

        return (-coord[0]+self.b)^3*(-coord[1]+self.c)^2

    def partialGxy1128(self,coord):

        return (-coord[0]+self.b)^3*(-coord[1]+self.c)^3

    def partialGxy1129(self,coord):

        return (-coord[0]+self.b)^3*(-coord[1]+self.c)^4

    def partialGxy1130(self,coord):

        return (-coord[0]+self.b)^3*(-coord[1]+self.d)

    def partialGxy1131(self,coord):

        return (-coord[0]+self.b)^3*(-coord[1]+self.c)*(-coord[1]+self.d)

    def partialGxy1132(self,coord):

        return (-coord[0]+self.b)^3*(-coord[1]+self.c)^2*(-coord[1]+self.d)

    def partialGxy1133(self,coord):

        return (-coord[0]+self.b)^3*(-coord[1]+self.c)^3*(-coord[1]+self.d)

    def partialGxy1134(self,coord):

        return (-coord[0]+self.b)^3*(-coord[1]+self.c)^4*(-coord[1]+self.d)

    def partialGxy1135(self,coord):

        return (-coord[0]+self.b)^3*(-coord[1]+self.d)^2

    def partialGxy1136(self,coord):

        return (-coord[0]+self.b)^3*(-coord[1]+self.c)*(-coord[1]+self.d)^2

    def partialGxy1137(self,coord):

        return (-coord[0]+self.b)^3*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2

    def partialGxy1138(self,coord):

        return (-coord[0]+self.b)^3*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2

    def partialGxy1139(self,coord):

        return (-coord[0]+self.b)^3*(-coord[1]+self.c)^4*(-coord[1]+self.d)^2

    def partialGxy1140(self,coord):

        return (-coord[0]+self.b)^3*(-coord[1]+self.d)^3

    def partialGxy1141(self,coord):

        return (-coord[0]+self.b)^3*(-coord[1]+self.c)*(-coord[1]+self.d)^3

    def partialGxy1142(self,coord):

        return (-coord[0]+self.b)^3*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3

    def partialGxy1143(self,coord):

        return (-coord[0]+self.b)^3*(-coord[1]+self.c)^3*(-coord[1]+self.d)^3

    def partialGxy1144(self,coord):

        return (-coord[0]+self.b)^3*(-coord[1]+self.c)^4*(-coord[1]+self.d)^3

    def partialGxy1145(self,coord):

        return (-coord[0]+self.b)^3*(-coord[1]+self.d)^4

    def partialGxy1146(self,coord):

        return (-coord[0]+self.b)^3*(-coord[1]+self.c)*(-coord[1]+self.d)^4

    def partialGxy1147(self,coord):

        return (-coord[0]+self.b)^3*(-coord[1]+self.c)^2*(-coord[1]+self.d)^4

    def partialGxy1148(self,coord):

        return (-coord[0]+self.b)^3*(-coord[1]+self.c)^3*(-coord[1]+self.d)^4

    def partialGxy1149(self,coord):

        return (-coord[0]+self.b)^3*(-coord[1]+self.c)^4*(-coord[1]+self.d)^4

    def partialGxy1156(self,coord):

        return (-coord[0]+self.b)^3*(-coord[1]+self.c)+(-coord[0]+self.b)^3*(-coord[1]+self.d)

    def partialGxy1157(self,coord):

        return (-coord[0]+self.b)^3*(-coord[1]+self.c)^2+2*(-coord[0]+self.b)^3*(-coord[1]+self.c)*(-coord[1]+self.d)

    def partialGxy1158(self,coord):

        return (-coord[0]+self.b)^3*(-coord[1]+self.c)^3+3*(-coord[0]+self.b)^3*(-coord[1]+self.c)^2*(-coord[1]+self.d)

    def partialGxy1159(self,coord):

        return (-coord[0]+self.b)^3*(-coord[1]+self.c)^4+4*(-coord[0]+self.b)^3*(-coord[1]+self.c)^3*(-coord[1]+self.d)

    def partialGxy1161(self,coord):

        return 2*(-coord[0]+self.b)^3*(-coord[1]+self.c)*(-coord[1]+self.d)+(-coord[0]+self.b)^3*(-coord[1]+self.d)^2

    def partialGxy1162(self,coord):

        return 2*(-coord[0]+self.b)^3*(-coord[1]+self.c)^2*(-coord[1]+self.d)+2*(-coord[0]+self.b)^3*(-coord[1]+self.c)*(-coord[1]+self.d)^2

    def partialGxy1163(self,coord):

        return 2*(-coord[0]+self.b)^3*(-coord[1]+self.c)^3*(-coord[1]+self.d)+3*(-coord[0]+self.b)^3*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2

    def partialGxy1164(self,coord):

        return 2*(-coord[0]+self.b)^3*(-coord[1]+self.c)^4*(-coord[1]+self.d)+4*(-coord[0]+self.b)^3*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2

    def partialGxy1166(self,coord):

        return 3*(-coord[0]+self.b)^3*(-coord[1]+self.c)*(-coord[1]+self.d)^2+(-coord[0]+self.b)^3*(-coord[1]+self.d)^3

    def partialGxy1167(self,coord):

        return 3*(-coord[0]+self.b)^3*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2+2*(-coord[0]+self.b)^3*(-coord[1]+self.c)*(-coord[1]+self.d)^3

    def partialGxy1168(self,coord):

        return 3*(-coord[0]+self.b)^3*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2+3*(-coord[0]+self.b)^3*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3

    def partialGxy1169(self,coord):

        return 3*(-coord[0]+self.b)^3*(-coord[1]+self.c)^4*(-coord[1]+self.d)^2+4*(-coord[0]+self.b)^3*(-coord[1]+self.c)^3*(-coord[1]+self.d)^3

    def partialGxy1171(self,coord):

        return 4*(-coord[0]+self.b)^3*(-coord[1]+self.c)*(-coord[1]+self.d)^3+(-coord[0]+self.b)^3*(-coord[1]+self.d)^4

    def partialGxy1172(self,coord):

        return 4*(-coord[0]+self.b)^3*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3+2*(-coord[0]+self.b)^3*(-coord[1]+self.c)*(-coord[1]+self.d)^4

    def partialGxy1173(self,coord):

        return 4*(-coord[0]+self.b)^3*(-coord[1]+self.c)^3*(-coord[1]+self.d)^3+3*(-coord[0]+self.b)^3*(-coord[1]+self.c)^2*(-coord[1]+self.d)^4

    def partialGxy1174(self,coord):

        return 4*(-coord[0]+self.b)^3*(-coord[1]+self.c)^4*(-coord[1]+self.d)^3+4*(-coord[0]+self.b)^3*(-coord[1]+self.c)^3*(-coord[1]+self.d)^4

    def partialGxy1187(self,coord):

        return 2*(-coord[0]+self.b)^3*(-coord[1]+self.c)^2+8*(-coord[0]+self.b)^3*(-coord[1]+self.c)*(-coord[1]+self.d)+2*(-coord[0]+self.b)^3*(-coord[1]+self.d)^2

    def partialGxy1188(self,coord):

        return 2*(-coord[0]+self.b)^3*(-coord[1]+self.c)^3+12*(-coord[0]+self.b)^3*(-coord[1]+self.c)^2*(-coord[1]+self.d)+6*(-coord[0]+self.b)^3*(-coord[1]+self.c)*(-coord[1]+self.d)^2

    def partialGxy1189(self,coord):

        return 2*(-coord[0]+self.b)^3*(-coord[1]+self.c)^4+16*(-coord[0]+self.b)^3*(-coord[1]+self.c)^3*(-coord[1]+self.d)+12*(-coord[0]+self.b)^3*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2

    def partialGxy1192(self,coord):

        return 6*(-coord[0]+self.b)^3*(-coord[1]+self.c)^2*(-coord[1]+self.d)+12*(-coord[0]+self.b)^3*(-coord[1]+self.c)*(-coord[1]+self.d)^2+2*(-coord[0]+self.b)^3*(-coord[1]+self.d)^3

    def partialGxy1193(self,coord):

        return 6*(-coord[0]+self.b)^3*(-coord[1]+self.c)^3*(-coord[1]+self.d)+18*(-coord[0]+self.b)^3*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2+6*(-coord[0]+self.b)^3*(-coord[1]+self.c)*(-coord[1]+self.d)^3

    def partialGxy1194(self,coord):

        return 6*(-coord[0]+self.b)^3*(-coord[1]+self.c)^4*(-coord[1]+self.d)+24*(-coord[0]+self.b)^3*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2+12*(-coord[0]+self.b)^3*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3

    def partialGxy1197(self,coord):

        return 12*(-coord[0]+self.b)^3*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2+16*(-coord[0]+self.b)^3*(-coord[1]+self.c)*(-coord[1]+self.d)^3+2*(-coord[0]+self.b)^3*(-coord[1]+self.d)^4

    def partialGxy1198(self,coord):

        return 12*(-coord[0]+self.b)^3*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2+24*(-coord[0]+self.b)^3*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3+6*(-coord[0]+self.b)^3*(-coord[1]+self.c)*(-coord[1]+self.d)^4

    def partialGxy1199(self,coord):

        return 12*(-coord[0]+self.b)^3*(-coord[1]+self.c)^4*(-coord[1]+self.d)^2+32*(-coord[0]+self.b)^3*(-coord[1]+self.c)^3*(-coord[1]+self.d)^3+12*(-coord[0]+self.b)^3*(-coord[1]+self.c)^2*(-coord[1]+self.d)^4

    def partialGxy1200(self,coord):

        return (-coord[0]+self.a)*(-coord[0]+self.b)^3

    def partialGxy1201(self,coord):

        return (-coord[0]+self.a)*(-coord[0]+self.b)^3*(-coord[1]+self.c)

    def partialGxy1202(self,coord):

        return (-coord[0]+self.a)*(-coord[0]+self.b)^3*(-coord[1]+self.c)^2

    def partialGxy1203(self,coord):

        return (-coord[0]+self.a)*(-coord[0]+self.b)^3*(-coord[1]+self.c)^3

    def partialGxy1204(self,coord):

        return (-coord[0]+self.a)*(-coord[0]+self.b)^3*(-coord[1]+self.c)^4

    def partialGxy1205(self,coord):

        return (-coord[0]+self.a)*(-coord[0]+self.b)^3*(-coord[1]+self.d)

    def partialGxy1206(self,coord):

        return (-coord[0]+self.a)*(-coord[0]+self.b)^3*(-coord[1]+self.c)*(-coord[1]+self.d)

    def partialGxy1207(self,coord):

        return (-coord[0]+self.a)*(-coord[0]+self.b)^3*(-coord[1]+self.c)^2*(-coord[1]+self.d)

    def partialGxy1208(self,coord):

        return (-coord[0]+self.a)*(-coord[0]+self.b)^3*(-coord[1]+self.c)^3*(-coord[1]+self.d)

    def partialGxy1209(self,coord):

        return (-coord[0]+self.a)*(-coord[0]+self.b)^3*(-coord[1]+self.c)^4*(-coord[1]+self.d)

    def partialGxy1210(self,coord):

        return (-coord[0]+self.a)*(-coord[0]+self.b)^3*(-coord[1]+self.d)^2

    def partialGxy1211(self,coord):

        return (-coord[0]+self.a)*(-coord[0]+self.b)^3*(-coord[1]+self.c)*(-coord[1]+self.d)^2

    def partialGxy1212(self,coord):

        return (-coord[0]+self.a)*(-coord[0]+self.b)^3*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2

    def partialGxy1213(self,coord):

        return (-coord[0]+self.a)*(-coord[0]+self.b)^3*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2

    def partialGxy1214(self,coord):

        return (-coord[0]+self.a)*(-coord[0]+self.b)^3*(-coord[1]+self.c)^4*(-coord[1]+self.d)^2

    def partialGxy1215(self,coord):

        return (-coord[0]+self.a)*(-coord[0]+self.b)^3*(-coord[1]+self.d)^3

    def partialGxy1216(self,coord):

        return (-coord[0]+self.a)*(-coord[0]+self.b)^3*(-coord[1]+self.c)*(-coord[1]+self.d)^3

    def partialGxy1217(self,coord):

        return (-coord[0]+self.a)*(-coord[0]+self.b)^3*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3

    def partialGxy1218(self,coord):

        return (-coord[0]+self.a)*(-coord[0]+self.b)^3*(-coord[1]+self.c)^3*(-coord[1]+self.d)^3

    def partialGxy1219(self,coord):

        return (-coord[0]+self.a)*(-coord[0]+self.b)^3*(-coord[1]+self.c)^4*(-coord[1]+self.d)^3

    def partialGxy1220(self,coord):

        return (-coord[0]+self.a)*(-coord[0]+self.b)^3*(-coord[1]+self.d)^4

    def partialGxy1221(self,coord):

        return (-coord[0]+self.a)*(-coord[0]+self.b)^3*(-coord[1]+self.c)*(-coord[1]+self.d)^4

    def partialGxy1222(self,coord):

        return (-coord[0]+self.a)*(-coord[0]+self.b)^3*(-coord[1]+self.c)^2*(-coord[1]+self.d)^4

    def partialGxy1223(self,coord):

        return (-coord[0]+self.a)*(-coord[0]+self.b)^3*(-coord[1]+self.c)^3*(-coord[1]+self.d)^4

    def partialGxy1224(self,coord):

        return (-coord[0]+self.a)*(-coord[0]+self.b)^3*(-coord[1]+self.c)^4*(-coord[1]+self.d)^4

    def partialGxy1231(self,coord):

        return (-coord[0]+self.a)*(-coord[0]+self.b)^3*(-coord[1]+self.c)+(-coord[0]+self.a)*(-coord[0]+self.b)^3*(-coord[1]+self.d)

    def partialGxy1232(self,coord):

        return (-coord[0]+self.a)*(-coord[0]+self.b)^3*(-coord[1]+self.c)^2+2*(-coord[0]+self.a)*(-coord[0]+self.b)^3*(-coord[1]+self.c)*(-coord[1]+self.d)

    def partialGxy1233(self,coord):

        return (-coord[0]+self.a)*(-coord[0]+self.b)^3*(-coord[1]+self.c)^3+3*(-coord[0]+self.a)*(-coord[0]+self.b)^3*(-coord[1]+self.c)^2*(-coord[1]+self.d)

    def partialGxy1234(self,coord):

        return (-coord[0]+self.a)*(-coord[0]+self.b)^3*(-coord[1]+self.c)^4+4*(-coord[0]+self.a)*(-coord[0]+self.b)^3*(-coord[1]+self.c)^3*(-coord[1]+self.d)

    def partialGxy1236(self,coord):

        return 2*(-coord[0]+self.a)*(-coord[0]+self.b)^3*(-coord[1]+self.c)*(-coord[1]+self.d)+(-coord[0]+self.a)*(-coord[0]+self.b)^3*(-coord[1]+self.d)^2

    def partialGxy1237(self,coord):

        return 2*(-coord[0]+self.a)*(-coord[0]+self.b)^3*(-coord[1]+self.c)^2*(-coord[1]+self.d)+2*(-coord[0]+self.a)*(-coord[0]+self.b)^3*(-coord[1]+self.c)*(-coord[1]+self.d)^2

    def partialGxy1238(self,coord):

        return 2*(-coord[0]+self.a)*(-coord[0]+self.b)^3*(-coord[1]+self.c)^3*(-coord[1]+self.d)+3*(-coord[0]+self.a)*(-coord[0]+self.b)^3*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2

    def partialGxy1239(self,coord):

        return 2*(-coord[0]+self.a)*(-coord[0]+self.b)^3*(-coord[1]+self.c)^4*(-coord[1]+self.d)+4*(-coord[0]+self.a)*(-coord[0]+self.b)^3*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2

    def partialGxy1241(self,coord):

        return 3*(-coord[0]+self.a)*(-coord[0]+self.b)^3*(-coord[1]+self.c)*(-coord[1]+self.d)^2+(-coord[0]+self.a)*(-coord[0]+self.b)^3*(-coord[1]+self.d)^3

    def partialGxy1242(self,coord):

        return 3*(-coord[0]+self.a)*(-coord[0]+self.b)^3*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2+2*(-coord[0]+self.a)*(-coord[0]+self.b)^3*(-coord[1]+self.c)*(-coord[1]+self.d)^3

    def partialGxy1243(self,coord):

        return 3*(-coord[0]+self.a)*(-coord[0]+self.b)^3*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2+3*(-coord[0]+self.a)*(-coord[0]+self.b)^3*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3

    def partialGxy1244(self,coord):

        return 3*(-coord[0]+self.a)*(-coord[0]+self.b)^3*(-coord[1]+self.c)^4*(-coord[1]+self.d)^2+4*(-coord[0]+self.a)*(-coord[0]+self.b)^3*(-coord[1]+self.c)^3*(-coord[1]+self.d)^3

    def partialGxy1246(self,coord):

        return 4*(-coord[0]+self.a)*(-coord[0]+self.b)^3*(-coord[1]+self.c)*(-coord[1]+self.d)^3+(-coord[0]+self.a)*(-coord[0]+self.b)^3*(-coord[1]+self.d)^4

    def partialGxy1247(self,coord):

        return 4*(-coord[0]+self.a)*(-coord[0]+self.b)^3*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3+2*(-coord[0]+self.a)*(-coord[0]+self.b)^3*(-coord[1]+self.c)*(-coord[1]+self.d)^4

    def partialGxy1248(self,coord):

        return 4*(-coord[0]+self.a)*(-coord[0]+self.b)^3*(-coord[1]+self.c)^3*(-coord[1]+self.d)^3+3*(-coord[0]+self.a)*(-coord[0]+self.b)^3*(-coord[1]+self.c)^2*(-coord[1]+self.d)^4

    def partialGxy1249(self,coord):

        return 4*(-coord[0]+self.a)*(-coord[0]+self.b)^3*(-coord[1]+self.c)^4*(-coord[1]+self.d)^3+4*(-coord[0]+self.a)*(-coord[0]+self.b)^3*(-coord[1]+self.c)^3*(-coord[1]+self.d)^4

    def partialGxy1262(self,coord):

        return (-coord[0]+self.a)*(-coord[0]+self.b)^3*(2*(-coord[1]+self.c)^2+8*(-coord[1]+self.c)*(-coord[1]+self.d)+2*(-coord[1]+self.d)^2)

    def partialGxy1263(self,coord):

        return (-coord[0]+self.a)*(-coord[0]+self.b)^3*(2*(-coord[1]+self.c)^3+12*(-coord[1]+self.c)^2*(-coord[1]+self.d)+6*(-coord[1]+self.c)*(-coord[1]+self.d)^2)

    def partialGxy1264(self,coord):

        return (-coord[0]+self.a)*(-coord[0]+self.b)^3*(2*(-coord[1]+self.c)^4+16*(-coord[1]+self.c)^3*(-coord[1]+self.d)+12*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2)

    def partialGxy1267(self,coord):

        return (-coord[0]+self.a)*(-coord[0]+self.b)^3*(6*(-coord[1]+self.c)^2*(-coord[1]+self.d)+12*(-coord[1]+self.c)*(-coord[1]+self.d)^2+2*(-coord[1]+self.d)^3)

    def partialGxy1268(self,coord):

        return (-coord[0]+self.a)*(-coord[0]+self.b)^3*(6*(-coord[1]+self.c)^3*(-coord[1]+self.d)+18*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2+6*(-coord[1]+self.c)*(-coord[1]+self.d)^3)

    def partialGxy1269(self,coord):

        return (-coord[0]+self.a)*(-coord[0]+self.b)^3*(6*(-coord[1]+self.c)^4*(-coord[1]+self.d)+24*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2+12*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3)

    def partialGxy1272(self,coord):

        return (-coord[0]+self.a)*(-coord[0]+self.b)^3*(12*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2+16*(-coord[1]+self.c)*(-coord[1]+self.d)^3+2*(-coord[1]+self.d)^4)

    def partialGxy1273(self,coord):

        return (-coord[0]+self.a)*(-coord[0]+self.b)^3*(12*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2+24*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3+6*(-coord[1]+self.c)*(-coord[1]+self.d)^4)

    def partialGxy1274(self,coord):

        return (-coord[0]+self.a)*(-coord[0]+self.b)^3*(12*(-coord[1]+self.c)^4*(-coord[1]+self.d)^2+32*(-coord[1]+self.c)^3*(-coord[1]+self.d)^3+12*(-coord[1]+self.c)^2*(-coord[1]+self.d)^4)

    def partialGxy1275(self,coord):

        return (-coord[0]+self.a)^2*(-coord[0]+self.b)^3

    def partialGxy1276(self,coord):

        return (-coord[0]+self.a)^2*(-coord[0]+self.b)^3*(-coord[1]+self.c)

    def partialGxy1277(self,coord):

        return (-coord[0]+self.a)^2*(-coord[0]+self.b)^3*(-coord[1]+self.c)^2

    def partialGxy1278(self,coord):

        return (-coord[0]+self.a)^2*(-coord[0]+self.b)^3*(-coord[1]+self.c)^3

    def partialGxy1279(self,coord):

        return (-coord[0]+self.a)^2*(-coord[0]+self.b)^3*(-coord[1]+self.c)^4

    def partialGxy1280(self,coord):

        return (-coord[0]+self.a)^2*(-coord[0]+self.b)^3*(-coord[1]+self.d)

    def partialGxy1281(self,coord):

        return (-coord[0]+self.a)^2*(-coord[0]+self.b)^3*(-coord[1]+self.c)*(-coord[1]+self.d)

    def partialGxy1282(self,coord):

        return (-coord[0]+self.a)^2*(-coord[0]+self.b)^3*(-coord[1]+self.c)^2*(-coord[1]+self.d)

    def partialGxy1283(self,coord):

        return (-coord[0]+self.a)^2*(-coord[0]+self.b)^3*(-coord[1]+self.c)^3*(-coord[1]+self.d)

    def partialGxy1284(self,coord):

        return (-coord[0]+self.a)^2*(-coord[0]+self.b)^3*(-coord[1]+self.c)^4*(-coord[1]+self.d)

    def partialGxy1285(self,coord):

        return (-coord[0]+self.a)^2*(-coord[0]+self.b)^3*(-coord[1]+self.d)^2

    def partialGxy1286(self,coord):

        return (-coord[0]+self.a)^2*(-coord[0]+self.b)^3*(-coord[1]+self.c)*(-coord[1]+self.d)^2

    def partialGxy1287(self,coord):

        return (-coord[0]+self.a)^2*(-coord[0]+self.b)^3*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2

    def partialGxy1288(self,coord):

        return (-coord[0]+self.a)^2*(-coord[0]+self.b)^3*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2

    def partialGxy1289(self,coord):

        return (-coord[0]+self.a)^2*(-coord[0]+self.b)^3*(-coord[1]+self.c)^4*(-coord[1]+self.d)^2

    def partialGxy1290(self,coord):

        return (-coord[0]+self.a)^2*(-coord[0]+self.b)^3*(-coord[1]+self.d)^3

    def partialGxy1291(self,coord):

        return (-coord[0]+self.a)^2*(-coord[0]+self.b)^3*(-coord[1]+self.c)*(-coord[1]+self.d)^3

    def partialGxy1292(self,coord):

        return (-coord[0]+self.a)^2*(-coord[0]+self.b)^3*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3

    def partialGxy1293(self,coord):

        return (-coord[0]+self.a)^2*(-coord[0]+self.b)^3*(-coord[1]+self.c)^3*(-coord[1]+self.d)^3

    def partialGxy1294(self,coord):

        return (-coord[0]+self.a)^2*(-coord[0]+self.b)^3*(-coord[1]+self.c)^4*(-coord[1]+self.d)^3

    def partialGxy1295(self,coord):

        return (-coord[0]+self.a)^2*(-coord[0]+self.b)^3*(-coord[1]+self.d)^4

    def partialGxy1296(self,coord):

        return (-coord[0]+self.a)^2*(-coord[0]+self.b)^3*(-coord[1]+self.c)*(-coord[1]+self.d)^4

    def partialGxy1297(self,coord):

        return (-coord[0]+self.a)^2*(-coord[0]+self.b)^3*(-coord[1]+self.c)^2*(-coord[1]+self.d)^4

    def partialGxy1298(self,coord):

        return (-coord[0]+self.a)^2*(-coord[0]+self.b)^3*(-coord[1]+self.c)^3*(-coord[1]+self.d)^4

    def partialGxy1299(self,coord):

        return (-coord[0]+self.a)^2*(-coord[0]+self.b)^3*(-coord[1]+self.c)^4*(-coord[1]+self.d)^4

    def partialGxy1306(self,coord):

        return (-coord[0]+self.a)^2*(-coord[0]+self.b)^3*(-coord[1]+self.c)+(-coord[0]+self.a)^2*(-coord[0]+self.b)^3*(-coord[1]+self.d)

    def partialGxy1307(self,coord):

        return (-coord[0]+self.a)^2*(-coord[0]+self.b)^3*(-coord[1]+self.c)^2+2*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3*(-coord[1]+self.c)*(-coord[1]+self.d)

    def partialGxy1308(self,coord):

        return (-coord[0]+self.a)^2*(-coord[0]+self.b)^3*(-coord[1]+self.c)^3+3*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3*(-coord[1]+self.c)^2*(-coord[1]+self.d)

    def partialGxy1309(self,coord):

        return (-coord[0]+self.a)^2*(-coord[0]+self.b)^3*(-coord[1]+self.c)^4+4*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3*(-coord[1]+self.c)^3*(-coord[1]+self.d)

    def partialGxy1311(self,coord):

        return 2*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3*(-coord[1]+self.c)*(-coord[1]+self.d)+(-coord[0]+self.a)^2*(-coord[0]+self.b)^3*(-coord[1]+self.d)^2

    def partialGxy1312(self,coord):

        return 2*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3*(-coord[1]+self.c)^2*(-coord[1]+self.d)+2*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3*(-coord[1]+self.c)*(-coord[1]+self.d)^2

    def partialGxy1313(self,coord):

        return 2*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3*(-coord[1]+self.c)^3*(-coord[1]+self.d)+3*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2

    def partialGxy1314(self,coord):

        return 2*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3*(-coord[1]+self.c)^4*(-coord[1]+self.d)+4*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2

    def partialGxy1316(self,coord):

        return 3*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3*(-coord[1]+self.c)*(-coord[1]+self.d)^2+(-coord[0]+self.a)^2*(-coord[0]+self.b)^3*(-coord[1]+self.d)^3

    def partialGxy1317(self,coord):

        return 3*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2+2*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3*(-coord[1]+self.c)*(-coord[1]+self.d)^3

    def partialGxy1318(self,coord):

        return 3*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2+3*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3

    def partialGxy1319(self,coord):

        return 3*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3*(-coord[1]+self.c)^4*(-coord[1]+self.d)^2+4*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3*(-coord[1]+self.c)^3*(-coord[1]+self.d)^3

    def partialGxy1321(self,coord):

        return 4*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3*(-coord[1]+self.c)*(-coord[1]+self.d)^3+(-coord[0]+self.a)^2*(-coord[0]+self.b)^3*(-coord[1]+self.d)^4

    def partialGxy1322(self,coord):

        return 4*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3+2*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3*(-coord[1]+self.c)*(-coord[1]+self.d)^4

    def partialGxy1323(self,coord):

        return 4*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3*(-coord[1]+self.c)^3*(-coord[1]+self.d)^3+3*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3*(-coord[1]+self.c)^2*(-coord[1]+self.d)^4

    def partialGxy1324(self,coord):

        return 4*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3*(-coord[1]+self.c)^4*(-coord[1]+self.d)^3+4*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3*(-coord[1]+self.c)^3*(-coord[1]+self.d)^4

    def partialGxy1337(self,coord):

        return (-coord[0]+self.a)^2*(-coord[0]+self.b)^3*(2*(-coord[1]+self.c)^2+8*(-coord[1]+self.c)*(-coord[1]+self.d)+2*(-coord[1]+self.d)^2)

    def partialGxy1338(self,coord):

        return (-coord[0]+self.a)^2*(-coord[0]+self.b)^3*(2*(-coord[1]+self.c)^3+12*(-coord[1]+self.c)^2*(-coord[1]+self.d)+6*(-coord[1]+self.c)*(-coord[1]+self.d)^2)

    def partialGxy1339(self,coord):

        return (-coord[0]+self.a)^2*(-coord[0]+self.b)^3*(2*(-coord[1]+self.c)^4+16*(-coord[1]+self.c)^3*(-coord[1]+self.d)+12*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2)

    def partialGxy1342(self,coord):

        return (-coord[0]+self.a)^2*(-coord[0]+self.b)^3*(6*(-coord[1]+self.c)^2*(-coord[1]+self.d)+12*(-coord[1]+self.c)*(-coord[1]+self.d)^2+2*(-coord[1]+self.d)^3)

    def partialGxy1343(self,coord):

        return (-coord[0]+self.a)^2*(-coord[0]+self.b)^3*(6*(-coord[1]+self.c)^3*(-coord[1]+self.d)+18*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2+6*(-coord[1]+self.c)*(-coord[1]+self.d)^3)

    def partialGxy1344(self,coord):

        return (-coord[0]+self.a)^2*(-coord[0]+self.b)^3*(6*(-coord[1]+self.c)^4*(-coord[1]+self.d)+24*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2+12*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3)

    def partialGxy1347(self,coord):

        return (-coord[0]+self.a)^2*(-coord[0]+self.b)^3*(12*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2+16*(-coord[1]+self.c)*(-coord[1]+self.d)^3+2*(-coord[1]+self.d)^4)

    def partialGxy1348(self,coord):

        return (-coord[0]+self.a)^2*(-coord[0]+self.b)^3*(12*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2+24*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3+6*(-coord[1]+self.c)*(-coord[1]+self.d)^4)

    def partialGxy1349(self,coord):

        return (-coord[0]+self.a)^2*(-coord[0]+self.b)^3*(12*(-coord[1]+self.c)^4*(-coord[1]+self.d)^2+32*(-coord[1]+self.c)^3*(-coord[1]+self.d)^3+12*(-coord[1]+self.c)^2*(-coord[1]+self.d)^4)

    def partialGxy1350(self,coord):

        return (-coord[0]+self.a)^3*(-coord[0]+self.b)^3

    def partialGxy1351(self,coord):

        return (-coord[0]+self.a)^3*(-coord[0]+self.b)^3*(-coord[1]+self.c)

    def partialGxy1352(self,coord):

        return (-coord[0]+self.a)^3*(-coord[0]+self.b)^3*(-coord[1]+self.c)^2

    def partialGxy1353(self,coord):

        return (-coord[0]+self.a)^3*(-coord[0]+self.b)^3*(-coord[1]+self.c)^3

    def partialGxy1354(self,coord):

        return (-coord[0]+self.a)^3*(-coord[0]+self.b)^3*(-coord[1]+self.c)^4

    def partialGxy1355(self,coord):

        return (-coord[0]+self.a)^3*(-coord[0]+self.b)^3*(-coord[1]+self.d)

    def partialGxy1356(self,coord):

        return (-coord[0]+self.a)^3*(-coord[0]+self.b)^3*(-coord[1]+self.c)*(-coord[1]+self.d)

    def partialGxy1357(self,coord):

        return (-coord[0]+self.a)^3*(-coord[0]+self.b)^3*(-coord[1]+self.c)^2*(-coord[1]+self.d)

    def partialGxy1358(self,coord):

        return (-coord[0]+self.a)^3*(-coord[0]+self.b)^3*(-coord[1]+self.c)^3*(-coord[1]+self.d)

    def partialGxy1359(self,coord):

        return (-coord[0]+self.a)^3*(-coord[0]+self.b)^3*(-coord[1]+self.c)^4*(-coord[1]+self.d)

    def partialGxy1360(self,coord):

        return (-coord[0]+self.a)^3*(-coord[0]+self.b)^3*(-coord[1]+self.d)^2

    def partialGxy1361(self,coord):

        return (-coord[0]+self.a)^3*(-coord[0]+self.b)^3*(-coord[1]+self.c)*(-coord[1]+self.d)^2

    def partialGxy1362(self,coord):

        return (-coord[0]+self.a)^3*(-coord[0]+self.b)^3*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2

    def partialGxy1363(self,coord):

        return (-coord[0]+self.a)^3*(-coord[0]+self.b)^3*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2

    def partialGxy1364(self,coord):

        return (-coord[0]+self.a)^3*(-coord[0]+self.b)^3*(-coord[1]+self.c)^4*(-coord[1]+self.d)^2

    def partialGxy1365(self,coord):

        return (-coord[0]+self.a)^3*(-coord[0]+self.b)^3*(-coord[1]+self.d)^3

    def partialGxy1366(self,coord):

        return (-coord[0]+self.a)^3*(-coord[0]+self.b)^3*(-coord[1]+self.c)*(-coord[1]+self.d)^3

    def partialGxy1367(self,coord):

        return (-coord[0]+self.a)^3*(-coord[0]+self.b)^3*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3

    def partialGxy1368(self,coord):

        return (-coord[0]+self.a)^3*(-coord[0]+self.b)^3*(-coord[1]+self.c)^3*(-coord[1]+self.d)^3

    def partialGxy1369(self,coord):

        return (-coord[0]+self.a)^3*(-coord[0]+self.b)^3*(-coord[1]+self.c)^4*(-coord[1]+self.d)^3

    def partialGxy1370(self,coord):

        return (-coord[0]+self.a)^3*(-coord[0]+self.b)^3*(-coord[1]+self.d)^4

    def partialGxy1371(self,coord):

        return (-coord[0]+self.a)^3*(-coord[0]+self.b)^3*(-coord[1]+self.c)*(-coord[1]+self.d)^4

    def partialGxy1372(self,coord):

        return (-coord[0]+self.a)^3*(-coord[0]+self.b)^3*(-coord[1]+self.c)^2*(-coord[1]+self.d)^4

    def partialGxy1373(self,coord):

        return (-coord[0]+self.a)^3*(-coord[0]+self.b)^3*(-coord[1]+self.c)^3*(-coord[1]+self.d)^4

    def partialGxy1374(self,coord):

        return (-coord[0]+self.a)^3*(-coord[0]+self.b)^3*(-coord[1]+self.c)^4*(-coord[1]+self.d)^4

    def partialGxy1381(self,coord):

        return (-coord[0]+self.a)^3*(-coord[0]+self.b)^3*(-coord[1]+self.c)+(-coord[0]+self.a)^3*(-coord[0]+self.b)^3*(-coord[1]+self.d)

    def partialGxy1382(self,coord):

        return (-coord[0]+self.a)^3*(-coord[0]+self.b)^3*(-coord[1]+self.c)^2+2*(-coord[0]+self.a)^3*(-coord[0]+self.b)^3*(-coord[1]+self.c)*(-coord[1]+self.d)

    def partialGxy1383(self,coord):

        return (-coord[0]+self.a)^3*(-coord[0]+self.b)^3*(-coord[1]+self.c)^3+3*(-coord[0]+self.a)^3*(-coord[0]+self.b)^3*(-coord[1]+self.c)^2*(-coord[1]+self.d)

    def partialGxy1384(self,coord):

        return (-coord[0]+self.a)^3*(-coord[0]+self.b)^3*(-coord[1]+self.c)^4+4*(-coord[0]+self.a)^3*(-coord[0]+self.b)^3*(-coord[1]+self.c)^3*(-coord[1]+self.d)

    def partialGxy1386(self,coord):

        return 2*(-coord[0]+self.a)^3*(-coord[0]+self.b)^3*(-coord[1]+self.c)*(-coord[1]+self.d)+(-coord[0]+self.a)^3*(-coord[0]+self.b)^3*(-coord[1]+self.d)^2

    def partialGxy1387(self,coord):

        return 2*(-coord[0]+self.a)^3*(-coord[0]+self.b)^3*(-coord[1]+self.c)^2*(-coord[1]+self.d)+2*(-coord[0]+self.a)^3*(-coord[0]+self.b)^3*(-coord[1]+self.c)*(-coord[1]+self.d)^2

    def partialGxy1388(self,coord):

        return 2*(-coord[0]+self.a)^3*(-coord[0]+self.b)^3*(-coord[1]+self.c)^3*(-coord[1]+self.d)+3*(-coord[0]+self.a)^3*(-coord[0]+self.b)^3*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2

    def partialGxy1389(self,coord):

        return 2*(-coord[0]+self.a)^3*(-coord[0]+self.b)^3*(-coord[1]+self.c)^4*(-coord[1]+self.d)+4*(-coord[0]+self.a)^3*(-coord[0]+self.b)^3*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2

    def partialGxy1391(self,coord):

        return 3*(-coord[0]+self.a)^3*(-coord[0]+self.b)^3*(-coord[1]+self.c)*(-coord[1]+self.d)^2+(-coord[0]+self.a)^3*(-coord[0]+self.b)^3*(-coord[1]+self.d)^3

    def partialGxy1392(self,coord):

        return 3*(-coord[0]+self.a)^3*(-coord[0]+self.b)^3*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2+2*(-coord[0]+self.a)^3*(-coord[0]+self.b)^3*(-coord[1]+self.c)*(-coord[1]+self.d)^3

    def partialGxy1393(self,coord):

        return 3*(-coord[0]+self.a)^3*(-coord[0]+self.b)^3*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2+3*(-coord[0]+self.a)^3*(-coord[0]+self.b)^3*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3

    def partialGxy1394(self,coord):

        return 3*(-coord[0]+self.a)^3*(-coord[0]+self.b)^3*(-coord[1]+self.c)^4*(-coord[1]+self.d)^2+4*(-coord[0]+self.a)^3*(-coord[0]+self.b)^3*(-coord[1]+self.c)^3*(-coord[1]+self.d)^3

    def partialGxy1396(self,coord):

        return 4*(-coord[0]+self.a)^3*(-coord[0]+self.b)^3*(-coord[1]+self.c)*(-coord[1]+self.d)^3+(-coord[0]+self.a)^3*(-coord[0]+self.b)^3*(-coord[1]+self.d)^4

    def partialGxy1397(self,coord):

        return 4*(-coord[0]+self.a)^3*(-coord[0]+self.b)^3*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3+2*(-coord[0]+self.a)^3*(-coord[0]+self.b)^3*(-coord[1]+self.c)*(-coord[1]+self.d)^4

    def partialGxy1398(self,coord):

        return 4*(-coord[0]+self.a)^3*(-coord[0]+self.b)^3*(-coord[1]+self.c)^3*(-coord[1]+self.d)^3+3*(-coord[0]+self.a)^3*(-coord[0]+self.b)^3*(-coord[1]+self.c)^2*(-coord[1]+self.d)^4

    def partialGxy1399(self,coord):

        return 4*(-coord[0]+self.a)^3*(-coord[0]+self.b)^3*(-coord[1]+self.c)^4*(-coord[1]+self.d)^3+4*(-coord[0]+self.a)^3*(-coord[0]+self.b)^3*(-coord[1]+self.c)^3*(-coord[1]+self.d)^4

    def partialGxy1412(self,coord):

        return (-coord[0]+self.a)^3*(-coord[0]+self.b)^3*(2*(-coord[1]+self.c)^2+8*(-coord[1]+self.c)*(-coord[1]+self.d)+2*(-coord[1]+self.d)^2)

    def partialGxy1413(self,coord):

        return (-coord[0]+self.a)^3*(-coord[0]+self.b)^3*(2*(-coord[1]+self.c)^3+12*(-coord[1]+self.c)^2*(-coord[1]+self.d)+6*(-coord[1]+self.c)*(-coord[1]+self.d)^2)

    def partialGxy1414(self,coord):

        return (-coord[0]+self.a)^3*(-coord[0]+self.b)^3*(2*(-coord[1]+self.c)^4+16*(-coord[1]+self.c)^3*(-coord[1]+self.d)+12*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2)

    def partialGxy1417(self,coord):

        return (-coord[0]+self.a)^3*(-coord[0]+self.b)^3*(6*(-coord[1]+self.c)^2*(-coord[1]+self.d)+12*(-coord[1]+self.c)*(-coord[1]+self.d)^2+2*(-coord[1]+self.d)^3)

    def partialGxy1418(self,coord):

        return (-coord[0]+self.a)^3*(-coord[0]+self.b)^3*(6*(-coord[1]+self.c)^3*(-coord[1]+self.d)+18*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2+6*(-coord[1]+self.c)*(-coord[1]+self.d)^3)

    def partialGxy1419(self,coord):

        return (-coord[0]+self.a)^3*(-coord[0]+self.b)^3*(6*(-coord[1]+self.c)^4*(-coord[1]+self.d)+24*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2+12*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3)

    def partialGxy1422(self,coord):

        return (-coord[0]+self.a)^3*(-coord[0]+self.b)^3*(12*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2+16*(-coord[1]+self.c)*(-coord[1]+self.d)^3+2*(-coord[1]+self.d)^4)

    def partialGxy1423(self,coord):

        return (-coord[0]+self.a)^3*(-coord[0]+self.b)^3*(12*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2+24*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3+6*(-coord[1]+self.c)*(-coord[1]+self.d)^4)

    def partialGxy1424(self,coord):

        return (-coord[0]+self.a)^3*(-coord[0]+self.b)^3*(12*(-coord[1]+self.c)^4*(-coord[1]+self.d)^2+32*(-coord[1]+self.c)^3*(-coord[1]+self.d)^3+12*(-coord[1]+self.c)^2*(-coord[1]+self.d)^4)

    def partialGxy1425(self,coord):

        return (-coord[0]+self.a)^4*(-coord[0]+self.b)^3

    def partialGxy1426(self,coord):

        return (-coord[0]+self.a)^4*(-coord[0]+self.b)^3*(-coord[1]+self.c)

    def partialGxy1427(self,coord):

        return (-coord[0]+self.a)^4*(-coord[0]+self.b)^3*(-coord[1]+self.c)^2

    def partialGxy1428(self,coord):

        return (-coord[0]+self.a)^4*(-coord[0]+self.b)^3*(-coord[1]+self.c)^3

    def partialGxy1429(self,coord):

        return (-coord[0]+self.a)^4*(-coord[0]+self.b)^3*(-coord[1]+self.c)^4

    def partialGxy1430(self,coord):

        return (-coord[0]+self.a)^4*(-coord[0]+self.b)^3*(-coord[1]+self.d)

    def partialGxy1431(self,coord):

        return (-coord[0]+self.a)^4*(-coord[0]+self.b)^3*(-coord[1]+self.c)*(-coord[1]+self.d)

    def partialGxy1432(self,coord):

        return (-coord[0]+self.a)^4*(-coord[0]+self.b)^3*(-coord[1]+self.c)^2*(-coord[1]+self.d)

    def partialGxy1433(self,coord):

        return (-coord[0]+self.a)^4*(-coord[0]+self.b)^3*(-coord[1]+self.c)^3*(-coord[1]+self.d)

    def partialGxy1434(self,coord):

        return (-coord[0]+self.a)^4*(-coord[0]+self.b)^3*(-coord[1]+self.c)^4*(-coord[1]+self.d)

    def partialGxy1435(self,coord):

        return (-coord[0]+self.a)^4*(-coord[0]+self.b)^3*(-coord[1]+self.d)^2

    def partialGxy1436(self,coord):

        return (-coord[0]+self.a)^4*(-coord[0]+self.b)^3*(-coord[1]+self.c)*(-coord[1]+self.d)^2

    def partialGxy1437(self,coord):

        return (-coord[0]+self.a)^4*(-coord[0]+self.b)^3*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2

    def partialGxy1438(self,coord):

        return (-coord[0]+self.a)^4*(-coord[0]+self.b)^3*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2

    def partialGxy1439(self,coord):

        return (-coord[0]+self.a)^4*(-coord[0]+self.b)^3*(-coord[1]+self.c)^4*(-coord[1]+self.d)^2

    def partialGxy1440(self,coord):

        return (-coord[0]+self.a)^4*(-coord[0]+self.b)^3*(-coord[1]+self.d)^3

    def partialGxy1441(self,coord):

        return (-coord[0]+self.a)^4*(-coord[0]+self.b)^3*(-coord[1]+self.c)*(-coord[1]+self.d)^3

    def partialGxy1442(self,coord):

        return (-coord[0]+self.a)^4*(-coord[0]+self.b)^3*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3

    def partialGxy1443(self,coord):

        return (-coord[0]+self.a)^4*(-coord[0]+self.b)^3*(-coord[1]+self.c)^3*(-coord[1]+self.d)^3

    def partialGxy1444(self,coord):

        return (-coord[0]+self.a)^4*(-coord[0]+self.b)^3*(-coord[1]+self.c)^4*(-coord[1]+self.d)^3

    def partialGxy1445(self,coord):

        return (-coord[0]+self.a)^4*(-coord[0]+self.b)^3*(-coord[1]+self.d)^4

    def partialGxy1446(self,coord):

        return (-coord[0]+self.a)^4*(-coord[0]+self.b)^3*(-coord[1]+self.c)*(-coord[1]+self.d)^4

    def partialGxy1447(self,coord):

        return (-coord[0]+self.a)^4*(-coord[0]+self.b)^3*(-coord[1]+self.c)^2*(-coord[1]+self.d)^4

    def partialGxy1448(self,coord):

        return (-coord[0]+self.a)^4*(-coord[0]+self.b)^3*(-coord[1]+self.c)^3*(-coord[1]+self.d)^4

    def partialGxy1449(self,coord):

        return (-coord[0]+self.a)^4*(-coord[0]+self.b)^3*(-coord[1]+self.c)^4*(-coord[1]+self.d)^4

    def partialGxy1456(self,coord):

        return (-coord[0]+self.a)^4*(-coord[0]+self.b)^3*(-coord[1]+self.c)+(-coord[0]+self.a)^4*(-coord[0]+self.b)^3*(-coord[1]+self.d)

    def partialGxy1457(self,coord):

        return (-coord[0]+self.a)^4*(-coord[0]+self.b)^3*(-coord[1]+self.c)^2+2*(-coord[0]+self.a)^4*(-coord[0]+self.b)^3*(-coord[1]+self.c)*(-coord[1]+self.d)

    def partialGxy1458(self,coord):

        return (-coord[0]+self.a)^4*(-coord[0]+self.b)^3*(-coord[1]+self.c)^3+3*(-coord[0]+self.a)^4*(-coord[0]+self.b)^3*(-coord[1]+self.c)^2*(-coord[1]+self.d)

    def partialGxy1459(self,coord):

        return (-coord[0]+self.a)^4*(-coord[0]+self.b)^3*(-coord[1]+self.c)^4+4*(-coord[0]+self.a)^4*(-coord[0]+self.b)^3*(-coord[1]+self.c)^3*(-coord[1]+self.d)

    def partialGxy1461(self,coord):

        return 2*(-coord[0]+self.a)^4*(-coord[0]+self.b)^3*(-coord[1]+self.c)*(-coord[1]+self.d)+(-coord[0]+self.a)^4*(-coord[0]+self.b)^3*(-coord[1]+self.d)^2

    def partialGxy1462(self,coord):

        return 2*(-coord[0]+self.a)^4*(-coord[0]+self.b)^3*(-coord[1]+self.c)^2*(-coord[1]+self.d)+2*(-coord[0]+self.a)^4*(-coord[0]+self.b)^3*(-coord[1]+self.c)*(-coord[1]+self.d)^2

    def partialGxy1463(self,coord):

        return 2*(-coord[0]+self.a)^4*(-coord[0]+self.b)^3*(-coord[1]+self.c)^3*(-coord[1]+self.d)+3*(-coord[0]+self.a)^4*(-coord[0]+self.b)^3*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2

    def partialGxy1464(self,coord):

        return 2*(-coord[0]+self.a)^4*(-coord[0]+self.b)^3*(-coord[1]+self.c)^4*(-coord[1]+self.d)+4*(-coord[0]+self.a)^4*(-coord[0]+self.b)^3*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2

    def partialGxy1466(self,coord):

        return 3*(-coord[0]+self.a)^4*(-coord[0]+self.b)^3*(-coord[1]+self.c)*(-coord[1]+self.d)^2+(-coord[0]+self.a)^4*(-coord[0]+self.b)^3*(-coord[1]+self.d)^3

    def partialGxy1467(self,coord):

        return 3*(-coord[0]+self.a)^4*(-coord[0]+self.b)^3*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2+2*(-coord[0]+self.a)^4*(-coord[0]+self.b)^3*(-coord[1]+self.c)*(-coord[1]+self.d)^3

    def partialGxy1468(self,coord):

        return 3*(-coord[0]+self.a)^4*(-coord[0]+self.b)^3*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2+3*(-coord[0]+self.a)^4*(-coord[0]+self.b)^3*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3

    def partialGxy1469(self,coord):

        return 3*(-coord[0]+self.a)^4*(-coord[0]+self.b)^3*(-coord[1]+self.c)^4*(-coord[1]+self.d)^2+4*(-coord[0]+self.a)^4*(-coord[0]+self.b)^3*(-coord[1]+self.c)^3*(-coord[1]+self.d)^3

    def partialGxy1471(self,coord):

        return 4*(-coord[0]+self.a)^4*(-coord[0]+self.b)^3*(-coord[1]+self.c)*(-coord[1]+self.d)^3+(-coord[0]+self.a)^4*(-coord[0]+self.b)^3*(-coord[1]+self.d)^4

    def partialGxy1472(self,coord):

        return 4*(-coord[0]+self.a)^4*(-coord[0]+self.b)^3*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3+2*(-coord[0]+self.a)^4*(-coord[0]+self.b)^3*(-coord[1]+self.c)*(-coord[1]+self.d)^4

    def partialGxy1473(self,coord):

        return 4*(-coord[0]+self.a)^4*(-coord[0]+self.b)^3*(-coord[1]+self.c)^3*(-coord[1]+self.d)^3+3*(-coord[0]+self.a)^4*(-coord[0]+self.b)^3*(-coord[1]+self.c)^2*(-coord[1]+self.d)^4

    def partialGxy1474(self,coord):

        return 4*(-coord[0]+self.a)^4*(-coord[0]+self.b)^3*(-coord[1]+self.c)^4*(-coord[1]+self.d)^3+4*(-coord[0]+self.a)^4*(-coord[0]+self.b)^3*(-coord[1]+self.c)^3*(-coord[1]+self.d)^4

    def partialGxy1487(self,coord):

        return (-coord[0]+self.a)^4*(-coord[0]+self.b)^3*(2*(-coord[1]+self.c)^2+8*(-coord[1]+self.c)*(-coord[1]+self.d)+2*(-coord[1]+self.d)^2)

    def partialGxy1488(self,coord):

        return (-coord[0]+self.a)^4*(-coord[0]+self.b)^3*(2*(-coord[1]+self.c)^3+12*(-coord[1]+self.c)^2*(-coord[1]+self.d)+6*(-coord[1]+self.c)*(-coord[1]+self.d)^2)

    def partialGxy1489(self,coord):

        return (-coord[0]+self.a)^4*(-coord[0]+self.b)^3*(2*(-coord[1]+self.c)^4+16*(-coord[1]+self.c)^3*(-coord[1]+self.d)+12*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2)

    def partialGxy1492(self,coord):

        return (-coord[0]+self.a)^4*(-coord[0]+self.b)^3*(6*(-coord[1]+self.c)^2*(-coord[1]+self.d)+12*(-coord[1]+self.c)*(-coord[1]+self.d)^2+2*(-coord[1]+self.d)^3)

    def partialGxy1493(self,coord):

        return (-coord[0]+self.a)^4*(-coord[0]+self.b)^3*(6*(-coord[1]+self.c)^3*(-coord[1]+self.d)+18*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2+6*(-coord[1]+self.c)*(-coord[1]+self.d)^3)

    def partialGxy1494(self,coord):

        return (-coord[0]+self.a)^4*(-coord[0]+self.b)^3*(6*(-coord[1]+self.c)^4*(-coord[1]+self.d)+24*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2+12*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3)

    def partialGxy1497(self,coord):

        return (-coord[0]+self.a)^4*(-coord[0]+self.b)^3*(12*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2+16*(-coord[1]+self.c)*(-coord[1]+self.d)^3+2*(-coord[1]+self.d)^4)

    def partialGxy1498(self,coord):

        return (-coord[0]+self.a)^4*(-coord[0]+self.b)^3*(12*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2+24*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3+6*(-coord[1]+self.c)*(-coord[1]+self.d)^4)

    def partialGxy1499(self,coord):

        return (-coord[0]+self.a)^4*(-coord[0]+self.b)^3*(12*(-coord[1]+self.c)^4*(-coord[1]+self.d)^2+32*(-coord[1]+self.c)^3*(-coord[1]+self.d)^3+12*(-coord[1]+self.c)^2*(-coord[1]+self.d)^4)

    def partialGxy1500(self,coord):

        return (-coord[0]+self.b)^4

    def partialGxy1501(self,coord):

        return (-coord[0]+self.b)^4*(-coord[1]+self.c)

    def partialGxy1502(self,coord):

        return (-coord[0]+self.b)^4*(-coord[1]+self.c)^2

    def partialGxy1503(self,coord):

        return (-coord[0]+self.b)^4*(-coord[1]+self.c)^3

    def partialGxy1504(self,coord):

        return (-coord[0]+self.b)^4*(-coord[1]+self.c)^4

    def partialGxy1505(self,coord):

        return (-coord[0]+self.b)^4*(-coord[1]+self.d)

    def partialGxy1506(self,coord):

        return (-coord[0]+self.b)^4*(-coord[1]+self.c)*(-coord[1]+self.d)

    def partialGxy1507(self,coord):

        return (-coord[0]+self.b)^4*(-coord[1]+self.c)^2*(-coord[1]+self.d)

    def partialGxy1508(self,coord):

        return (-coord[0]+self.b)^4*(-coord[1]+self.c)^3*(-coord[1]+self.d)

    def partialGxy1509(self,coord):

        return (-coord[0]+self.b)^4*(-coord[1]+self.c)^4*(-coord[1]+self.d)

    def partialGxy1510(self,coord):

        return (-coord[0]+self.b)^4*(-coord[1]+self.d)^2

    def partialGxy1511(self,coord):

        return (-coord[0]+self.b)^4*(-coord[1]+self.c)*(-coord[1]+self.d)^2

    def partialGxy1512(self,coord):

        return (-coord[0]+self.b)^4*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2

    def partialGxy1513(self,coord):

        return (-coord[0]+self.b)^4*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2

    def partialGxy1514(self,coord):

        return (-coord[0]+self.b)^4*(-coord[1]+self.c)^4*(-coord[1]+self.d)^2

    def partialGxy1515(self,coord):

        return (-coord[0]+self.b)^4*(-coord[1]+self.d)^3

    def partialGxy1516(self,coord):

        return (-coord[0]+self.b)^4*(-coord[1]+self.c)*(-coord[1]+self.d)^3

    def partialGxy1517(self,coord):

        return (-coord[0]+self.b)^4*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3

    def partialGxy1518(self,coord):

        return (-coord[0]+self.b)^4*(-coord[1]+self.c)^3*(-coord[1]+self.d)^3

    def partialGxy1519(self,coord):

        return (-coord[0]+self.b)^4*(-coord[1]+self.c)^4*(-coord[1]+self.d)^3

    def partialGxy1520(self,coord):

        return (-coord[0]+self.b)^4*(-coord[1]+self.d)^4

    def partialGxy1521(self,coord):

        return (-coord[0]+self.b)^4*(-coord[1]+self.c)*(-coord[1]+self.d)^4

    def partialGxy1522(self,coord):

        return (-coord[0]+self.b)^4*(-coord[1]+self.c)^2*(-coord[1]+self.d)^4

    def partialGxy1523(self,coord):

        return (-coord[0]+self.b)^4*(-coord[1]+self.c)^3*(-coord[1]+self.d)^4

    def partialGxy1524(self,coord):

        return (-coord[0]+self.b)^4*(-coord[1]+self.c)^4*(-coord[1]+self.d)^4

    def partialGxy1531(self,coord):

        return (-coord[0]+self.b)^4*(-coord[1]+self.c)+(-coord[0]+self.b)^4*(-coord[1]+self.d)

    def partialGxy1532(self,coord):

        return (-coord[0]+self.b)^4*(-coord[1]+self.c)^2+2*(-coord[0]+self.b)^4*(-coord[1]+self.c)*(-coord[1]+self.d)

    def partialGxy1533(self,coord):

        return (-coord[0]+self.b)^4*(-coord[1]+self.c)^3+3*(-coord[0]+self.b)^4*(-coord[1]+self.c)^2*(-coord[1]+self.d)

    def partialGxy1534(self,coord):

        return (-coord[0]+self.b)^4*(-coord[1]+self.c)^4+4*(-coord[0]+self.b)^4*(-coord[1]+self.c)^3*(-coord[1]+self.d)

    def partialGxy1536(self,coord):

        return 2*(-coord[0]+self.b)^4*(-coord[1]+self.c)*(-coord[1]+self.d)+(-coord[0]+self.b)^4*(-coord[1]+self.d)^2

    def partialGxy1537(self,coord):

        return 2*(-coord[0]+self.b)^4*(-coord[1]+self.c)^2*(-coord[1]+self.d)+2*(-coord[0]+self.b)^4*(-coord[1]+self.c)*(-coord[1]+self.d)^2

    def partialGxy1538(self,coord):

        return 2*(-coord[0]+self.b)^4*(-coord[1]+self.c)^3*(-coord[1]+self.d)+3*(-coord[0]+self.b)^4*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2

    def partialGxy1539(self,coord):

        return 2*(-coord[0]+self.b)^4*(-coord[1]+self.c)^4*(-coord[1]+self.d)+4*(-coord[0]+self.b)^4*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2

    def partialGxy1541(self,coord):

        return 3*(-coord[0]+self.b)^4*(-coord[1]+self.c)*(-coord[1]+self.d)^2+(-coord[0]+self.b)^4*(-coord[1]+self.d)^3

    def partialGxy1542(self,coord):

        return 3*(-coord[0]+self.b)^4*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2+2*(-coord[0]+self.b)^4*(-coord[1]+self.c)*(-coord[1]+self.d)^3

    def partialGxy1543(self,coord):

        return 3*(-coord[0]+self.b)^4*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2+3*(-coord[0]+self.b)^4*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3

    def partialGxy1544(self,coord):

        return 3*(-coord[0]+self.b)^4*(-coord[1]+self.c)^4*(-coord[1]+self.d)^2+4*(-coord[0]+self.b)^4*(-coord[1]+self.c)^3*(-coord[1]+self.d)^3

    def partialGxy1546(self,coord):

        return 4*(-coord[0]+self.b)^4*(-coord[1]+self.c)*(-coord[1]+self.d)^3+(-coord[0]+self.b)^4*(-coord[1]+self.d)^4

    def partialGxy1547(self,coord):

        return 4*(-coord[0]+self.b)^4*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3+2*(-coord[0]+self.b)^4*(-coord[1]+self.c)*(-coord[1]+self.d)^4

    def partialGxy1548(self,coord):

        return 4*(-coord[0]+self.b)^4*(-coord[1]+self.c)^3*(-coord[1]+self.d)^3+3*(-coord[0]+self.b)^4*(-coord[1]+self.c)^2*(-coord[1]+self.d)^4

    def partialGxy1549(self,coord):

        return 4*(-coord[0]+self.b)^4*(-coord[1]+self.c)^4*(-coord[1]+self.d)^3+4*(-coord[0]+self.b)^4*(-coord[1]+self.c)^3*(-coord[1]+self.d)^4

    def partialGxy1562(self,coord):

        return 2*(-coord[0]+self.b)^4*(-coord[1]+self.c)^2+8*(-coord[0]+self.b)^4*(-coord[1]+self.c)*(-coord[1]+self.d)+2*(-coord[0]+self.b)^4*(-coord[1]+self.d)^2

    def partialGxy1563(self,coord):

        return 2*(-coord[0]+self.b)^4*(-coord[1]+self.c)^3+12*(-coord[0]+self.b)^4*(-coord[1]+self.c)^2*(-coord[1]+self.d)+6*(-coord[0]+self.b)^4*(-coord[1]+self.c)*(-coord[1]+self.d)^2

    def partialGxy1564(self,coord):

        return 2*(-coord[0]+self.b)^4*(-coord[1]+self.c)^4+16*(-coord[0]+self.b)^4*(-coord[1]+self.c)^3*(-coord[1]+self.d)+12*(-coord[0]+self.b)^4*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2

    def partialGxy1567(self,coord):

        return 6*(-coord[0]+self.b)^4*(-coord[1]+self.c)^2*(-coord[1]+self.d)+12*(-coord[0]+self.b)^4*(-coord[1]+self.c)*(-coord[1]+self.d)^2+2*(-coord[0]+self.b)^4*(-coord[1]+self.d)^3

    def partialGxy1568(self,coord):

        return 6*(-coord[0]+self.b)^4*(-coord[1]+self.c)^3*(-coord[1]+self.d)+18*(-coord[0]+self.b)^4*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2+6*(-coord[0]+self.b)^4*(-coord[1]+self.c)*(-coord[1]+self.d)^3

    def partialGxy1569(self,coord):

        return 6*(-coord[0]+self.b)^4*(-coord[1]+self.c)^4*(-coord[1]+self.d)+24*(-coord[0]+self.b)^4*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2+12*(-coord[0]+self.b)^4*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3

    def partialGxy1572(self,coord):

        return 12*(-coord[0]+self.b)^4*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2+16*(-coord[0]+self.b)^4*(-coord[1]+self.c)*(-coord[1]+self.d)^3+2*(-coord[0]+self.b)^4*(-coord[1]+self.d)^4

    def partialGxy1573(self,coord):

        return 12*(-coord[0]+self.b)^4*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2+24*(-coord[0]+self.b)^4*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3+6*(-coord[0]+self.b)^4*(-coord[1]+self.c)*(-coord[1]+self.d)^4

    def partialGxy1574(self,coord):

        return 12*(-coord[0]+self.b)^4*(-coord[1]+self.c)^4*(-coord[1]+self.d)^2+32*(-coord[0]+self.b)^4*(-coord[1]+self.c)^3*(-coord[1]+self.d)^3+12*(-coord[0]+self.b)^4*(-coord[1]+self.c)^2*(-coord[1]+self.d)^4

    def partialGxy1575(self,coord):

        return (-coord[0]+self.a)*(-coord[0]+self.b)^4

    def partialGxy1576(self,coord):

        return (-coord[0]+self.a)*(-coord[0]+self.b)^4*(-coord[1]+self.c)

    def partialGxy1577(self,coord):

        return (-coord[0]+self.a)*(-coord[0]+self.b)^4*(-coord[1]+self.c)^2

    def partialGxy1578(self,coord):

        return (-coord[0]+self.a)*(-coord[0]+self.b)^4*(-coord[1]+self.c)^3

    def partialGxy1579(self,coord):

        return (-coord[0]+self.a)*(-coord[0]+self.b)^4*(-coord[1]+self.c)^4

    def partialGxy1580(self,coord):

        return (-coord[0]+self.a)*(-coord[0]+self.b)^4*(-coord[1]+self.d)

    def partialGxy1581(self,coord):

        return (-coord[0]+self.a)*(-coord[0]+self.b)^4*(-coord[1]+self.c)*(-coord[1]+self.d)

    def partialGxy1582(self,coord):

        return (-coord[0]+self.a)*(-coord[0]+self.b)^4*(-coord[1]+self.c)^2*(-coord[1]+self.d)

    def partialGxy1583(self,coord):

        return (-coord[0]+self.a)*(-coord[0]+self.b)^4*(-coord[1]+self.c)^3*(-coord[1]+self.d)

    def partialGxy1584(self,coord):

        return (-coord[0]+self.a)*(-coord[0]+self.b)^4*(-coord[1]+self.c)^4*(-coord[1]+self.d)

    def partialGxy1585(self,coord):

        return (-coord[0]+self.a)*(-coord[0]+self.b)^4*(-coord[1]+self.d)^2

    def partialGxy1586(self,coord):

        return (-coord[0]+self.a)*(-coord[0]+self.b)^4*(-coord[1]+self.c)*(-coord[1]+self.d)^2

    def partialGxy1587(self,coord):

        return (-coord[0]+self.a)*(-coord[0]+self.b)^4*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2

    def partialGxy1588(self,coord):

        return (-coord[0]+self.a)*(-coord[0]+self.b)^4*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2

    def partialGxy1589(self,coord):

        return (-coord[0]+self.a)*(-coord[0]+self.b)^4*(-coord[1]+self.c)^4*(-coord[1]+self.d)^2

    def partialGxy1590(self,coord):

        return (-coord[0]+self.a)*(-coord[0]+self.b)^4*(-coord[1]+self.d)^3

    def partialGxy1591(self,coord):

        return (-coord[0]+self.a)*(-coord[0]+self.b)^4*(-coord[1]+self.c)*(-coord[1]+self.d)^3

    def partialGxy1592(self,coord):

        return (-coord[0]+self.a)*(-coord[0]+self.b)^4*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3

    def partialGxy1593(self,coord):

        return (-coord[0]+self.a)*(-coord[0]+self.b)^4*(-coord[1]+self.c)^3*(-coord[1]+self.d)^3

    def partialGxy1594(self,coord):

        return (-coord[0]+self.a)*(-coord[0]+self.b)^4*(-coord[1]+self.c)^4*(-coord[1]+self.d)^3

    def partialGxy1595(self,coord):

        return (-coord[0]+self.a)*(-coord[0]+self.b)^4*(-coord[1]+self.d)^4

    def partialGxy1596(self,coord):

        return (-coord[0]+self.a)*(-coord[0]+self.b)^4*(-coord[1]+self.c)*(-coord[1]+self.d)^4

    def partialGxy1597(self,coord):

        return (-coord[0]+self.a)*(-coord[0]+self.b)^4*(-coord[1]+self.c)^2*(-coord[1]+self.d)^4

    def partialGxy1598(self,coord):

        return (-coord[0]+self.a)*(-coord[0]+self.b)^4*(-coord[1]+self.c)^3*(-coord[1]+self.d)^4

    def partialGxy1599(self,coord):

        return (-coord[0]+self.a)*(-coord[0]+self.b)^4*(-coord[1]+self.c)^4*(-coord[1]+self.d)^4

    def partialGxy1606(self,coord):

        return (-coord[0]+self.a)*(-coord[0]+self.b)^4*(-coord[1]+self.c)+(-coord[0]+self.a)*(-coord[0]+self.b)^4*(-coord[1]+self.d)

    def partialGxy1607(self,coord):

        return (-coord[0]+self.a)*(-coord[0]+self.b)^4*(-coord[1]+self.c)^2+2*(-coord[0]+self.a)*(-coord[0]+self.b)^4*(-coord[1]+self.c)*(-coord[1]+self.d)

    def partialGxy1608(self,coord):

        return (-coord[0]+self.a)*(-coord[0]+self.b)^4*(-coord[1]+self.c)^3+3*(-coord[0]+self.a)*(-coord[0]+self.b)^4*(-coord[1]+self.c)^2*(-coord[1]+self.d)

    def partialGxy1609(self,coord):

        return (-coord[0]+self.a)*(-coord[0]+self.b)^4*(-coord[1]+self.c)^4+4*(-coord[0]+self.a)*(-coord[0]+self.b)^4*(-coord[1]+self.c)^3*(-coord[1]+self.d)

    def partialGxy1611(self,coord):

        return 2*(-coord[0]+self.a)*(-coord[0]+self.b)^4*(-coord[1]+self.c)*(-coord[1]+self.d)+(-coord[0]+self.a)*(-coord[0]+self.b)^4*(-coord[1]+self.d)^2

    def partialGxy1612(self,coord):

        return 2*(-coord[0]+self.a)*(-coord[0]+self.b)^4*(-coord[1]+self.c)^2*(-coord[1]+self.d)+2*(-coord[0]+self.a)*(-coord[0]+self.b)^4*(-coord[1]+self.c)*(-coord[1]+self.d)^2

    def partialGxy1613(self,coord):

        return 2*(-coord[0]+self.a)*(-coord[0]+self.b)^4*(-coord[1]+self.c)^3*(-coord[1]+self.d)+3*(-coord[0]+self.a)*(-coord[0]+self.b)^4*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2

    def partialGxy1614(self,coord):

        return 2*(-coord[0]+self.a)*(-coord[0]+self.b)^4*(-coord[1]+self.c)^4*(-coord[1]+self.d)+4*(-coord[0]+self.a)*(-coord[0]+self.b)^4*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2

    def partialGxy1616(self,coord):

        return 3*(-coord[0]+self.a)*(-coord[0]+self.b)^4*(-coord[1]+self.c)*(-coord[1]+self.d)^2+(-coord[0]+self.a)*(-coord[0]+self.b)^4*(-coord[1]+self.d)^3

    def partialGxy1617(self,coord):

        return 3*(-coord[0]+self.a)*(-coord[0]+self.b)^4*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2+2*(-coord[0]+self.a)*(-coord[0]+self.b)^4*(-coord[1]+self.c)*(-coord[1]+self.d)^3

    def partialGxy1618(self,coord):

        return 3*(-coord[0]+self.a)*(-coord[0]+self.b)^4*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2+3*(-coord[0]+self.a)*(-coord[0]+self.b)^4*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3

    def partialGxy1619(self,coord):

        return 3*(-coord[0]+self.a)*(-coord[0]+self.b)^4*(-coord[1]+self.c)^4*(-coord[1]+self.d)^2+4*(-coord[0]+self.a)*(-coord[0]+self.b)^4*(-coord[1]+self.c)^3*(-coord[1]+self.d)^3

    def partialGxy1621(self,coord):

        return 4*(-coord[0]+self.a)*(-coord[0]+self.b)^4*(-coord[1]+self.c)*(-coord[1]+self.d)^3+(-coord[0]+self.a)*(-coord[0]+self.b)^4*(-coord[1]+self.d)^4

    def partialGxy1622(self,coord):

        return 4*(-coord[0]+self.a)*(-coord[0]+self.b)^4*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3+2*(-coord[0]+self.a)*(-coord[0]+self.b)^4*(-coord[1]+self.c)*(-coord[1]+self.d)^4

    def partialGxy1623(self,coord):

        return 4*(-coord[0]+self.a)*(-coord[0]+self.b)^4*(-coord[1]+self.c)^3*(-coord[1]+self.d)^3+3*(-coord[0]+self.a)*(-coord[0]+self.b)^4*(-coord[1]+self.c)^2*(-coord[1]+self.d)^4

    def partialGxy1624(self,coord):

        return 4*(-coord[0]+self.a)*(-coord[0]+self.b)^4*(-coord[1]+self.c)^4*(-coord[1]+self.d)^3+4*(-coord[0]+self.a)*(-coord[0]+self.b)^4*(-coord[1]+self.c)^3*(-coord[1]+self.d)^4

    def partialGxy1637(self,coord):

        return (-coord[0]+self.a)*(-coord[0]+self.b)^4*(2*(-coord[1]+self.c)^2+8*(-coord[1]+self.c)*(-coord[1]+self.d)+2*(-coord[1]+self.d)^2)

    def partialGxy1638(self,coord):

        return (-coord[0]+self.a)*(-coord[0]+self.b)^4*(2*(-coord[1]+self.c)^3+12*(-coord[1]+self.c)^2*(-coord[1]+self.d)+6*(-coord[1]+self.c)*(-coord[1]+self.d)^2)

    def partialGxy1639(self,coord):

        return (-coord[0]+self.a)*(-coord[0]+self.b)^4*(2*(-coord[1]+self.c)^4+16*(-coord[1]+self.c)^3*(-coord[1]+self.d)+12*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2)

    def partialGxy1642(self,coord):

        return (-coord[0]+self.a)*(-coord[0]+self.b)^4*(6*(-coord[1]+self.c)^2*(-coord[1]+self.d)+12*(-coord[1]+self.c)*(-coord[1]+self.d)^2+2*(-coord[1]+self.d)^3)

    def partialGxy1643(self,coord):

        return (-coord[0]+self.a)*(-coord[0]+self.b)^4*(6*(-coord[1]+self.c)^3*(-coord[1]+self.d)+18*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2+6*(-coord[1]+self.c)*(-coord[1]+self.d)^3)

    def partialGxy1644(self,coord):

        return (-coord[0]+self.a)*(-coord[0]+self.b)^4*(6*(-coord[1]+self.c)^4*(-coord[1]+self.d)+24*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2+12*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3)

    def partialGxy1647(self,coord):

        return (-coord[0]+self.a)*(-coord[0]+self.b)^4*(12*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2+16*(-coord[1]+self.c)*(-coord[1]+self.d)^3+2*(-coord[1]+self.d)^4)

    def partialGxy1648(self,coord):

        return (-coord[0]+self.a)*(-coord[0]+self.b)^4*(12*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2+24*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3+6*(-coord[1]+self.c)*(-coord[1]+self.d)^4)

    def partialGxy1649(self,coord):

        return (-coord[0]+self.a)*(-coord[0]+self.b)^4*(12*(-coord[1]+self.c)^4*(-coord[1]+self.d)^2+32*(-coord[1]+self.c)^3*(-coord[1]+self.d)^3+12*(-coord[1]+self.c)^2*(-coord[1]+self.d)^4)

    def partialGxy1650(self,coord):

        return (-coord[0]+self.a)^2*(-coord[0]+self.b)^4

    def partialGxy1651(self,coord):

        return (-coord[0]+self.a)^2*(-coord[0]+self.b)^4*(-coord[1]+self.c)

    def partialGxy1652(self,coord):

        return (-coord[0]+self.a)^2*(-coord[0]+self.b)^4*(-coord[1]+self.c)^2

    def partialGxy1653(self,coord):

        return (-coord[0]+self.a)^2*(-coord[0]+self.b)^4*(-coord[1]+self.c)^3

    def partialGxy1654(self,coord):

        return (-coord[0]+self.a)^2*(-coord[0]+self.b)^4*(-coord[1]+self.c)^4

    def partialGxy1655(self,coord):

        return (-coord[0]+self.a)^2*(-coord[0]+self.b)^4*(-coord[1]+self.d)

    def partialGxy1656(self,coord):

        return (-coord[0]+self.a)^2*(-coord[0]+self.b)^4*(-coord[1]+self.c)*(-coord[1]+self.d)

    def partialGxy1657(self,coord):

        return (-coord[0]+self.a)^2*(-coord[0]+self.b)^4*(-coord[1]+self.c)^2*(-coord[1]+self.d)

    def partialGxy1658(self,coord):

        return (-coord[0]+self.a)^2*(-coord[0]+self.b)^4*(-coord[1]+self.c)^3*(-coord[1]+self.d)

    def partialGxy1659(self,coord):

        return (-coord[0]+self.a)^2*(-coord[0]+self.b)^4*(-coord[1]+self.c)^4*(-coord[1]+self.d)

    def partialGxy1660(self,coord):

        return (-coord[0]+self.a)^2*(-coord[0]+self.b)^4*(-coord[1]+self.d)^2

    def partialGxy1661(self,coord):

        return (-coord[0]+self.a)^2*(-coord[0]+self.b)^4*(-coord[1]+self.c)*(-coord[1]+self.d)^2

    def partialGxy1662(self,coord):

        return (-coord[0]+self.a)^2*(-coord[0]+self.b)^4*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2

    def partialGxy1663(self,coord):

        return (-coord[0]+self.a)^2*(-coord[0]+self.b)^4*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2

    def partialGxy1664(self,coord):

        return (-coord[0]+self.a)^2*(-coord[0]+self.b)^4*(-coord[1]+self.c)^4*(-coord[1]+self.d)^2

    def partialGxy1665(self,coord):

        return (-coord[0]+self.a)^2*(-coord[0]+self.b)^4*(-coord[1]+self.d)^3

    def partialGxy1666(self,coord):

        return (-coord[0]+self.a)^2*(-coord[0]+self.b)^4*(-coord[1]+self.c)*(-coord[1]+self.d)^3

    def partialGxy1667(self,coord):

        return (-coord[0]+self.a)^2*(-coord[0]+self.b)^4*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3

    def partialGxy1668(self,coord):

        return (-coord[0]+self.a)^2*(-coord[0]+self.b)^4*(-coord[1]+self.c)^3*(-coord[1]+self.d)^3

    def partialGxy1669(self,coord):

        return (-coord[0]+self.a)^2*(-coord[0]+self.b)^4*(-coord[1]+self.c)^4*(-coord[1]+self.d)^3

    def partialGxy1670(self,coord):

        return (-coord[0]+self.a)^2*(-coord[0]+self.b)^4*(-coord[1]+self.d)^4

    def partialGxy1671(self,coord):

        return (-coord[0]+self.a)^2*(-coord[0]+self.b)^4*(-coord[1]+self.c)*(-coord[1]+self.d)^4

    def partialGxy1672(self,coord):

        return (-coord[0]+self.a)^2*(-coord[0]+self.b)^4*(-coord[1]+self.c)^2*(-coord[1]+self.d)^4

    def partialGxy1673(self,coord):

        return (-coord[0]+self.a)^2*(-coord[0]+self.b)^4*(-coord[1]+self.c)^3*(-coord[1]+self.d)^4

    def partialGxy1674(self,coord):

        return (-coord[0]+self.a)^2*(-coord[0]+self.b)^4*(-coord[1]+self.c)^4*(-coord[1]+self.d)^4

    def partialGxy1681(self,coord):

        return (-coord[0]+self.a)^2*(-coord[0]+self.b)^4*(-coord[1]+self.c)+(-coord[0]+self.a)^2*(-coord[0]+self.b)^4*(-coord[1]+self.d)

    def partialGxy1682(self,coord):

        return (-coord[0]+self.a)^2*(-coord[0]+self.b)^4*(-coord[1]+self.c)^2+2*(-coord[0]+self.a)^2*(-coord[0]+self.b)^4*(-coord[1]+self.c)*(-coord[1]+self.d)

    def partialGxy1683(self,coord):

        return (-coord[0]+self.a)^2*(-coord[0]+self.b)^4*(-coord[1]+self.c)^3+3*(-coord[0]+self.a)^2*(-coord[0]+self.b)^4*(-coord[1]+self.c)^2*(-coord[1]+self.d)

    def partialGxy1684(self,coord):

        return (-coord[0]+self.a)^2*(-coord[0]+self.b)^4*(-coord[1]+self.c)^4+4*(-coord[0]+self.a)^2*(-coord[0]+self.b)^4*(-coord[1]+self.c)^3*(-coord[1]+self.d)

    def partialGxy1686(self,coord):

        return 2*(-coord[0]+self.a)^2*(-coord[0]+self.b)^4*(-coord[1]+self.c)*(-coord[1]+self.d)+(-coord[0]+self.a)^2*(-coord[0]+self.b)^4*(-coord[1]+self.d)^2

    def partialGxy1687(self,coord):

        return 2*(-coord[0]+self.a)^2*(-coord[0]+self.b)^4*(-coord[1]+self.c)^2*(-coord[1]+self.d)+2*(-coord[0]+self.a)^2*(-coord[0]+self.b)^4*(-coord[1]+self.c)*(-coord[1]+self.d)^2

    def partialGxy1688(self,coord):

        return 2*(-coord[0]+self.a)^2*(-coord[0]+self.b)^4*(-coord[1]+self.c)^3*(-coord[1]+self.d)+3*(-coord[0]+self.a)^2*(-coord[0]+self.b)^4*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2

    def partialGxy1689(self,coord):

        return 2*(-coord[0]+self.a)^2*(-coord[0]+self.b)^4*(-coord[1]+self.c)^4*(-coord[1]+self.d)+4*(-coord[0]+self.a)^2*(-coord[0]+self.b)^4*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2

    def partialGxy1691(self,coord):

        return 3*(-coord[0]+self.a)^2*(-coord[0]+self.b)^4*(-coord[1]+self.c)*(-coord[1]+self.d)^2+(-coord[0]+self.a)^2*(-coord[0]+self.b)^4*(-coord[1]+self.d)^3

    def partialGxy1692(self,coord):

        return 3*(-coord[0]+self.a)^2*(-coord[0]+self.b)^4*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2+2*(-coord[0]+self.a)^2*(-coord[0]+self.b)^4*(-coord[1]+self.c)*(-coord[1]+self.d)^3

    def partialGxy1693(self,coord):

        return 3*(-coord[0]+self.a)^2*(-coord[0]+self.b)^4*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2+3*(-coord[0]+self.a)^2*(-coord[0]+self.b)^4*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3

    def partialGxy1694(self,coord):

        return 3*(-coord[0]+self.a)^2*(-coord[0]+self.b)^4*(-coord[1]+self.c)^4*(-coord[1]+self.d)^2+4*(-coord[0]+self.a)^2*(-coord[0]+self.b)^4*(-coord[1]+self.c)^3*(-coord[1]+self.d)^3

    def partialGxy1696(self,coord):

        return 4*(-coord[0]+self.a)^2*(-coord[0]+self.b)^4*(-coord[1]+self.c)*(-coord[1]+self.d)^3+(-coord[0]+self.a)^2*(-coord[0]+self.b)^4*(-coord[1]+self.d)^4

    def partialGxy1697(self,coord):

        return 4*(-coord[0]+self.a)^2*(-coord[0]+self.b)^4*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3+2*(-coord[0]+self.a)^2*(-coord[0]+self.b)^4*(-coord[1]+self.c)*(-coord[1]+self.d)^4

    def partialGxy1698(self,coord):

        return 4*(-coord[0]+self.a)^2*(-coord[0]+self.b)^4*(-coord[1]+self.c)^3*(-coord[1]+self.d)^3+3*(-coord[0]+self.a)^2*(-coord[0]+self.b)^4*(-coord[1]+self.c)^2*(-coord[1]+self.d)^4

    def partialGxy1699(self,coord):

        return 4*(-coord[0]+self.a)^2*(-coord[0]+self.b)^4*(-coord[1]+self.c)^4*(-coord[1]+self.d)^3+4*(-coord[0]+self.a)^2*(-coord[0]+self.b)^4*(-coord[1]+self.c)^3*(-coord[1]+self.d)^4

    def partialGxy1712(self,coord):

        return (-coord[0]+self.a)^2*(-coord[0]+self.b)^4*(2*(-coord[1]+self.c)^2+8*(-coord[1]+self.c)*(-coord[1]+self.d)+2*(-coord[1]+self.d)^2)

    def partialGxy1713(self,coord):

        return (-coord[0]+self.a)^2*(-coord[0]+self.b)^4*(2*(-coord[1]+self.c)^3+12*(-coord[1]+self.c)^2*(-coord[1]+self.d)+6*(-coord[1]+self.c)*(-coord[1]+self.d)^2)

    def partialGxy1714(self,coord):

        return (-coord[0]+self.a)^2*(-coord[0]+self.b)^4*(2*(-coord[1]+self.c)^4+16*(-coord[1]+self.c)^3*(-coord[1]+self.d)+12*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2)

    def partialGxy1717(self,coord):

        return (-coord[0]+self.a)^2*(-coord[0]+self.b)^4*(6*(-coord[1]+self.c)^2*(-coord[1]+self.d)+12*(-coord[1]+self.c)*(-coord[1]+self.d)^2+2*(-coord[1]+self.d)^3)

    def partialGxy1718(self,coord):

        return (-coord[0]+self.a)^2*(-coord[0]+self.b)^4*(6*(-coord[1]+self.c)^3*(-coord[1]+self.d)+18*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2+6*(-coord[1]+self.c)*(-coord[1]+self.d)^3)

    def partialGxy1719(self,coord):

        return (-coord[0]+self.a)^2*(-coord[0]+self.b)^4*(6*(-coord[1]+self.c)^4*(-coord[1]+self.d)+24*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2+12*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3)

    def partialGxy1722(self,coord):

        return (-coord[0]+self.a)^2*(-coord[0]+self.b)^4*(12*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2+16*(-coord[1]+self.c)*(-coord[1]+self.d)^3+2*(-coord[1]+self.d)^4)

    def partialGxy1723(self,coord):

        return (-coord[0]+self.a)^2*(-coord[0]+self.b)^4*(12*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2+24*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3+6*(-coord[1]+self.c)*(-coord[1]+self.d)^4)

    def partialGxy1724(self,coord):

        return (-coord[0]+self.a)^2*(-coord[0]+self.b)^4*(12*(-coord[1]+self.c)^4*(-coord[1]+self.d)^2+32*(-coord[1]+self.c)^3*(-coord[1]+self.d)^3+12*(-coord[1]+self.c)^2*(-coord[1]+self.d)^4)

    def partialGxy1725(self,coord):

        return (-coord[0]+self.a)^3*(-coord[0]+self.b)^4

    def partialGxy1726(self,coord):

        return (-coord[0]+self.a)^3*(-coord[0]+self.b)^4*(-coord[1]+self.c)

    def partialGxy1727(self,coord):

        return (-coord[0]+self.a)^3*(-coord[0]+self.b)^4*(-coord[1]+self.c)^2

    def partialGxy1728(self,coord):

        return (-coord[0]+self.a)^3*(-coord[0]+self.b)^4*(-coord[1]+self.c)^3

    def partialGxy1729(self,coord):

        return (-coord[0]+self.a)^3*(-coord[0]+self.b)^4*(-coord[1]+self.c)^4

    def partialGxy1730(self,coord):

        return (-coord[0]+self.a)^3*(-coord[0]+self.b)^4*(-coord[1]+self.d)

    def partialGxy1731(self,coord):

        return (-coord[0]+self.a)^3*(-coord[0]+self.b)^4*(-coord[1]+self.c)*(-coord[1]+self.d)

    def partialGxy1732(self,coord):

        return (-coord[0]+self.a)^3*(-coord[0]+self.b)^4*(-coord[1]+self.c)^2*(-coord[1]+self.d)

    def partialGxy1733(self,coord):

        return (-coord[0]+self.a)^3*(-coord[0]+self.b)^4*(-coord[1]+self.c)^3*(-coord[1]+self.d)

    def partialGxy1734(self,coord):

        return (-coord[0]+self.a)^3*(-coord[0]+self.b)^4*(-coord[1]+self.c)^4*(-coord[1]+self.d)

    def partialGxy1735(self,coord):

        return (-coord[0]+self.a)^3*(-coord[0]+self.b)^4*(-coord[1]+self.d)^2

    def partialGxy1736(self,coord):

        return (-coord[0]+self.a)^3*(-coord[0]+self.b)^4*(-coord[1]+self.c)*(-coord[1]+self.d)^2

    def partialGxy1737(self,coord):

        return (-coord[0]+self.a)^3*(-coord[0]+self.b)^4*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2

    def partialGxy1738(self,coord):

        return (-coord[0]+self.a)^3*(-coord[0]+self.b)^4*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2

    def partialGxy1739(self,coord):

        return (-coord[0]+self.a)^3*(-coord[0]+self.b)^4*(-coord[1]+self.c)^4*(-coord[1]+self.d)^2

    def partialGxy1740(self,coord):

        return (-coord[0]+self.a)^3*(-coord[0]+self.b)^4*(-coord[1]+self.d)^3

    def partialGxy1741(self,coord):

        return (-coord[0]+self.a)^3*(-coord[0]+self.b)^4*(-coord[1]+self.c)*(-coord[1]+self.d)^3

    def partialGxy1742(self,coord):

        return (-coord[0]+self.a)^3*(-coord[0]+self.b)^4*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3

    def partialGxy1743(self,coord):

        return (-coord[0]+self.a)^3*(-coord[0]+self.b)^4*(-coord[1]+self.c)^3*(-coord[1]+self.d)^3

    def partialGxy1744(self,coord):

        return (-coord[0]+self.a)^3*(-coord[0]+self.b)^4*(-coord[1]+self.c)^4*(-coord[1]+self.d)^3

    def partialGxy1745(self,coord):

        return (-coord[0]+self.a)^3*(-coord[0]+self.b)^4*(-coord[1]+self.d)^4

    def partialGxy1746(self,coord):

        return (-coord[0]+self.a)^3*(-coord[0]+self.b)^4*(-coord[1]+self.c)*(-coord[1]+self.d)^4

    def partialGxy1747(self,coord):

        return (-coord[0]+self.a)^3*(-coord[0]+self.b)^4*(-coord[1]+self.c)^2*(-coord[1]+self.d)^4

    def partialGxy1748(self,coord):

        return (-coord[0]+self.a)^3*(-coord[0]+self.b)^4*(-coord[1]+self.c)^3*(-coord[1]+self.d)^4

    def partialGxy1749(self,coord):

        return (-coord[0]+self.a)^3*(-coord[0]+self.b)^4*(-coord[1]+self.c)^4*(-coord[1]+self.d)^4

    def partialGxy1756(self,coord):

        return (-coord[0]+self.a)^3*(-coord[0]+self.b)^4*(-coord[1]+self.c)+(-coord[0]+self.a)^3*(-coord[0]+self.b)^4*(-coord[1]+self.d)

    def partialGxy1757(self,coord):

        return (-coord[0]+self.a)^3*(-coord[0]+self.b)^4*(-coord[1]+self.c)^2+2*(-coord[0]+self.a)^3*(-coord[0]+self.b)^4*(-coord[1]+self.c)*(-coord[1]+self.d)

    def partialGxy1758(self,coord):

        return (-coord[0]+self.a)^3*(-coord[0]+self.b)^4*(-coord[1]+self.c)^3+3*(-coord[0]+self.a)^3*(-coord[0]+self.b)^4*(-coord[1]+self.c)^2*(-coord[1]+self.d)

    def partialGxy1759(self,coord):

        return (-coord[0]+self.a)^3*(-coord[0]+self.b)^4*(-coord[1]+self.c)^4+4*(-coord[0]+self.a)^3*(-coord[0]+self.b)^4*(-coord[1]+self.c)^3*(-coord[1]+self.d)

    def partialGxy1761(self,coord):

        return 2*(-coord[0]+self.a)^3*(-coord[0]+self.b)^4*(-coord[1]+self.c)*(-coord[1]+self.d)+(-coord[0]+self.a)^3*(-coord[0]+self.b)^4*(-coord[1]+self.d)^2

    def partialGxy1762(self,coord):

        return 2*(-coord[0]+self.a)^3*(-coord[0]+self.b)^4*(-coord[1]+self.c)^2*(-coord[1]+self.d)+2*(-coord[0]+self.a)^3*(-coord[0]+self.b)^4*(-coord[1]+self.c)*(-coord[1]+self.d)^2

    def partialGxy1763(self,coord):

        return 2*(-coord[0]+self.a)^3*(-coord[0]+self.b)^4*(-coord[1]+self.c)^3*(-coord[1]+self.d)+3*(-coord[0]+self.a)^3*(-coord[0]+self.b)^4*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2

    def partialGxy1764(self,coord):

        return 2*(-coord[0]+self.a)^3*(-coord[0]+self.b)^4*(-coord[1]+self.c)^4*(-coord[1]+self.d)+4*(-coord[0]+self.a)^3*(-coord[0]+self.b)^4*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2

    def partialGxy1766(self,coord):

        return 3*(-coord[0]+self.a)^3*(-coord[0]+self.b)^4*(-coord[1]+self.c)*(-coord[1]+self.d)^2+(-coord[0]+self.a)^3*(-coord[0]+self.b)^4*(-coord[1]+self.d)^3

    def partialGxy1767(self,coord):

        return 3*(-coord[0]+self.a)^3*(-coord[0]+self.b)^4*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2+2*(-coord[0]+self.a)^3*(-coord[0]+self.b)^4*(-coord[1]+self.c)*(-coord[1]+self.d)^3

    def partialGxy1768(self,coord):

        return 3*(-coord[0]+self.a)^3*(-coord[0]+self.b)^4*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2+3*(-coord[0]+self.a)^3*(-coord[0]+self.b)^4*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3

    def partialGxy1769(self,coord):

        return 3*(-coord[0]+self.a)^3*(-coord[0]+self.b)^4*(-coord[1]+self.c)^4*(-coord[1]+self.d)^2+4*(-coord[0]+self.a)^3*(-coord[0]+self.b)^4*(-coord[1]+self.c)^3*(-coord[1]+self.d)^3

    def partialGxy1771(self,coord):

        return 4*(-coord[0]+self.a)^3*(-coord[0]+self.b)^4*(-coord[1]+self.c)*(-coord[1]+self.d)^3+(-coord[0]+self.a)^3*(-coord[0]+self.b)^4*(-coord[1]+self.d)^4

    def partialGxy1772(self,coord):

        return 4*(-coord[0]+self.a)^3*(-coord[0]+self.b)^4*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3+2*(-coord[0]+self.a)^3*(-coord[0]+self.b)^4*(-coord[1]+self.c)*(-coord[1]+self.d)^4

    def partialGxy1773(self,coord):

        return 4*(-coord[0]+self.a)^3*(-coord[0]+self.b)^4*(-coord[1]+self.c)^3*(-coord[1]+self.d)^3+3*(-coord[0]+self.a)^3*(-coord[0]+self.b)^4*(-coord[1]+self.c)^2*(-coord[1]+self.d)^4

    def partialGxy1774(self,coord):

        return 4*(-coord[0]+self.a)^3*(-coord[0]+self.b)^4*(-coord[1]+self.c)^4*(-coord[1]+self.d)^3+4*(-coord[0]+self.a)^3*(-coord[0]+self.b)^4*(-coord[1]+self.c)^3*(-coord[1]+self.d)^4

    def partialGxy1787(self,coord):

        return (-coord[0]+self.a)^3*(-coord[0]+self.b)^4*(2*(-coord[1]+self.c)^2+8*(-coord[1]+self.c)*(-coord[1]+self.d)+2*(-coord[1]+self.d)^2)

    def partialGxy1788(self,coord):

        return (-coord[0]+self.a)^3*(-coord[0]+self.b)^4*(2*(-coord[1]+self.c)^3+12*(-coord[1]+self.c)^2*(-coord[1]+self.d)+6*(-coord[1]+self.c)*(-coord[1]+self.d)^2)

    def partialGxy1789(self,coord):

        return (-coord[0]+self.a)^3*(-coord[0]+self.b)^4*(2*(-coord[1]+self.c)^4+16*(-coord[1]+self.c)^3*(-coord[1]+self.d)+12*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2)

    def partialGxy1792(self,coord):

        return (-coord[0]+self.a)^3*(-coord[0]+self.b)^4*(6*(-coord[1]+self.c)^2*(-coord[1]+self.d)+12*(-coord[1]+self.c)*(-coord[1]+self.d)^2+2*(-coord[1]+self.d)^3)

    def partialGxy1793(self,coord):

        return (-coord[0]+self.a)^3*(-coord[0]+self.b)^4*(6*(-coord[1]+self.c)^3*(-coord[1]+self.d)+18*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2+6*(-coord[1]+self.c)*(-coord[1]+self.d)^3)

    def partialGxy1794(self,coord):

        return (-coord[0]+self.a)^3*(-coord[0]+self.b)^4*(6*(-coord[1]+self.c)^4*(-coord[1]+self.d)+24*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2+12*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3)

    def partialGxy1797(self,coord):

        return (-coord[0]+self.a)^3*(-coord[0]+self.b)^4*(12*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2+16*(-coord[1]+self.c)*(-coord[1]+self.d)^3+2*(-coord[1]+self.d)^4)

    def partialGxy1798(self,coord):

        return (-coord[0]+self.a)^3*(-coord[0]+self.b)^4*(12*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2+24*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3+6*(-coord[1]+self.c)*(-coord[1]+self.d)^4)

    def partialGxy1799(self,coord):

        return (-coord[0]+self.a)^3*(-coord[0]+self.b)^4*(12*(-coord[1]+self.c)^4*(-coord[1]+self.d)^2+32*(-coord[1]+self.c)^3*(-coord[1]+self.d)^3+12*(-coord[1]+self.c)^2*(-coord[1]+self.d)^4)

    def partialGxy1800(self,coord):

        return (-coord[0]+self.a)^4*(-coord[0]+self.b)^4

    def partialGxy1801(self,coord):

        return (-coord[0]+self.a)^4*(-coord[0]+self.b)^4*(-coord[1]+self.c)

    def partialGxy1802(self,coord):

        return (-coord[0]+self.a)^4*(-coord[0]+self.b)^4*(-coord[1]+self.c)^2

    def partialGxy1803(self,coord):

        return (-coord[0]+self.a)^4*(-coord[0]+self.b)^4*(-coord[1]+self.c)^3

    def partialGxy1804(self,coord):

        return (-coord[0]+self.a)^4*(-coord[0]+self.b)^4*(-coord[1]+self.c)^4

    def partialGxy1805(self,coord):

        return (-coord[0]+self.a)^4*(-coord[0]+self.b)^4*(-coord[1]+self.d)

    def partialGxy1806(self,coord):

        return (-coord[0]+self.a)^4*(-coord[0]+self.b)^4*(-coord[1]+self.c)*(-coord[1]+self.d)

    def partialGxy1807(self,coord):

        return (-coord[0]+self.a)^4*(-coord[0]+self.b)^4*(-coord[1]+self.c)^2*(-coord[1]+self.d)

    def partialGxy1808(self,coord):

        return (-coord[0]+self.a)^4*(-coord[0]+self.b)^4*(-coord[1]+self.c)^3*(-coord[1]+self.d)

    def partialGxy1809(self,coord):

        return (-coord[0]+self.a)^4*(-coord[0]+self.b)^4*(-coord[1]+self.c)^4*(-coord[1]+self.d)

    def partialGxy1810(self,coord):

        return (-coord[0]+self.a)^4*(-coord[0]+self.b)^4*(-coord[1]+self.d)^2

    def partialGxy1811(self,coord):

        return (-coord[0]+self.a)^4*(-coord[0]+self.b)^4*(-coord[1]+self.c)*(-coord[1]+self.d)^2

    def partialGxy1812(self,coord):

        return (-coord[0]+self.a)^4*(-coord[0]+self.b)^4*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2

    def partialGxy1813(self,coord):

        return (-coord[0]+self.a)^4*(-coord[0]+self.b)^4*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2

    def partialGxy1814(self,coord):

        return (-coord[0]+self.a)^4*(-coord[0]+self.b)^4*(-coord[1]+self.c)^4*(-coord[1]+self.d)^2

    def partialGxy1815(self,coord):

        return (-coord[0]+self.a)^4*(-coord[0]+self.b)^4*(-coord[1]+self.d)^3

    def partialGxy1816(self,coord):

        return (-coord[0]+self.a)^4*(-coord[0]+self.b)^4*(-coord[1]+self.c)*(-coord[1]+self.d)^3

    def partialGxy1817(self,coord):

        return (-coord[0]+self.a)^4*(-coord[0]+self.b)^4*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3

    def partialGxy1818(self,coord):

        return (-coord[0]+self.a)^4*(-coord[0]+self.b)^4*(-coord[1]+self.c)^3*(-coord[1]+self.d)^3

    def partialGxy1819(self,coord):

        return (-coord[0]+self.a)^4*(-coord[0]+self.b)^4*(-coord[1]+self.c)^4*(-coord[1]+self.d)^3

    def partialGxy1820(self,coord):

        return (-coord[0]+self.a)^4*(-coord[0]+self.b)^4*(-coord[1]+self.d)^4

    def partialGxy1821(self,coord):

        return (-coord[0]+self.a)^4*(-coord[0]+self.b)^4*(-coord[1]+self.c)*(-coord[1]+self.d)^4

    def partialGxy1822(self,coord):

        return (-coord[0]+self.a)^4*(-coord[0]+self.b)^4*(-coord[1]+self.c)^2*(-coord[1]+self.d)^4

    def partialGxy1823(self,coord):

        return (-coord[0]+self.a)^4*(-coord[0]+self.b)^4*(-coord[1]+self.c)^3*(-coord[1]+self.d)^4

    def partialGxy1824(self,coord):

        return (-coord[0]+self.a)^4*(-coord[0]+self.b)^4*(-coord[1]+self.c)^4*(-coord[1]+self.d)^4

    def partialGxy1831(self,coord):

        return (-coord[0]+self.a)^4*(-coord[0]+self.b)^4*(-coord[1]+self.c)+(-coord[0]+self.a)^4*(-coord[0]+self.b)^4*(-coord[1]+self.d)

    def partialGxy1832(self,coord):

        return (-coord[0]+self.a)^4*(-coord[0]+self.b)^4*(-coord[1]+self.c)^2+2*(-coord[0]+self.a)^4*(-coord[0]+self.b)^4*(-coord[1]+self.c)*(-coord[1]+self.d)

    def partialGxy1833(self,coord):

        return (-coord[0]+self.a)^4*(-coord[0]+self.b)^4*(-coord[1]+self.c)^3+3*(-coord[0]+self.a)^4*(-coord[0]+self.b)^4*(-coord[1]+self.c)^2*(-coord[1]+self.d)

    def partialGxy1834(self,coord):

        return (-coord[0]+self.a)^4*(-coord[0]+self.b)^4*(-coord[1]+self.c)^4+4*(-coord[0]+self.a)^4*(-coord[0]+self.b)^4*(-coord[1]+self.c)^3*(-coord[1]+self.d)

    def partialGxy1836(self,coord):

        return 2*(-coord[0]+self.a)^4*(-coord[0]+self.b)^4*(-coord[1]+self.c)*(-coord[1]+self.d)+(-coord[0]+self.a)^4*(-coord[0]+self.b)^4*(-coord[1]+self.d)^2

    def partialGxy1837(self,coord):

        return 2*(-coord[0]+self.a)^4*(-coord[0]+self.b)^4*(-coord[1]+self.c)^2*(-coord[1]+self.d)+2*(-coord[0]+self.a)^4*(-coord[0]+self.b)^4*(-coord[1]+self.c)*(-coord[1]+self.d)^2

    def partialGxy1838(self,coord):

        return 2*(-coord[0]+self.a)^4*(-coord[0]+self.b)^4*(-coord[1]+self.c)^3*(-coord[1]+self.d)+3*(-coord[0]+self.a)^4*(-coord[0]+self.b)^4*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2

    def partialGxy1839(self,coord):

        return 2*(-coord[0]+self.a)^4*(-coord[0]+self.b)^4*(-coord[1]+self.c)^4*(-coord[1]+self.d)+4*(-coord[0]+self.a)^4*(-coord[0]+self.b)^4*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2

    def partialGxy1841(self,coord):

        return 3*(-coord[0]+self.a)^4*(-coord[0]+self.b)^4*(-coord[1]+self.c)*(-coord[1]+self.d)^2+(-coord[0]+self.a)^4*(-coord[0]+self.b)^4*(-coord[1]+self.d)^3

    def partialGxy1842(self,coord):

        return 3*(-coord[0]+self.a)^4*(-coord[0]+self.b)^4*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2+2*(-coord[0]+self.a)^4*(-coord[0]+self.b)^4*(-coord[1]+self.c)*(-coord[1]+self.d)^3

    def partialGxy1843(self,coord):

        return 3*(-coord[0]+self.a)^4*(-coord[0]+self.b)^4*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2+3*(-coord[0]+self.a)^4*(-coord[0]+self.b)^4*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3

    def partialGxy1844(self,coord):

        return 3*(-coord[0]+self.a)^4*(-coord[0]+self.b)^4*(-coord[1]+self.c)^4*(-coord[1]+self.d)^2+4*(-coord[0]+self.a)^4*(-coord[0]+self.b)^4*(-coord[1]+self.c)^3*(-coord[1]+self.d)^3

    def partialGxy1846(self,coord):

        return 4*(-coord[0]+self.a)^4*(-coord[0]+self.b)^4*(-coord[1]+self.c)*(-coord[1]+self.d)^3+(-coord[0]+self.a)^4*(-coord[0]+self.b)^4*(-coord[1]+self.d)^4

    def partialGxy1847(self,coord):

        return 4*(-coord[0]+self.a)^4*(-coord[0]+self.b)^4*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3+2*(-coord[0]+self.a)^4*(-coord[0]+self.b)^4*(-coord[1]+self.c)*(-coord[1]+self.d)^4

    def partialGxy1848(self,coord):

        return 4*(-coord[0]+self.a)^4*(-coord[0]+self.b)^4*(-coord[1]+self.c)^3*(-coord[1]+self.d)^3+3*(-coord[0]+self.a)^4*(-coord[0]+self.b)^4*(-coord[1]+self.c)^2*(-coord[1]+self.d)^4

    def partialGxy1849(self,coord):

        return 4*(-coord[0]+self.a)^4*(-coord[0]+self.b)^4*(-coord[1]+self.c)^4*(-coord[1]+self.d)^3+4*(-coord[0]+self.a)^4*(-coord[0]+self.b)^4*(-coord[1]+self.c)^3*(-coord[1]+self.d)^4

    def partialGxy1862(self,coord):

        return (-coord[0]+self.a)^4*(-coord[0]+self.b)^4*(2*(-coord[1]+self.c)^2+8*(-coord[1]+self.c)*(-coord[1]+self.d)+2*(-coord[1]+self.d)^2)

    def partialGxy1863(self,coord):

        return (-coord[0]+self.a)^4*(-coord[0]+self.b)^4*(2*(-coord[1]+self.c)^3+12*(-coord[1]+self.c)^2*(-coord[1]+self.d)+6*(-coord[1]+self.c)*(-coord[1]+self.d)^2)

    def partialGxy1864(self,coord):

        return (-coord[0]+self.a)^4*(-coord[0]+self.b)^4*(2*(-coord[1]+self.c)^4+16*(-coord[1]+self.c)^3*(-coord[1]+self.d)+12*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2)

    def partialGxy1867(self,coord):

        return (-coord[0]+self.a)^4*(-coord[0]+self.b)^4*(6*(-coord[1]+self.c)^2*(-coord[1]+self.d)+12*(-coord[1]+self.c)*(-coord[1]+self.d)^2+2*(-coord[1]+self.d)^3)

    def partialGxy1868(self,coord):

        return (-coord[0]+self.a)^4*(-coord[0]+self.b)^4*(6*(-coord[1]+self.c)^3*(-coord[1]+self.d)+18*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2+6*(-coord[1]+self.c)*(-coord[1]+self.d)^3)

    def partialGxy1869(self,coord):

        return (-coord[0]+self.a)^4*(-coord[0]+self.b)^4*(6*(-coord[1]+self.c)^4*(-coord[1]+self.d)+24*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2+12*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3)

    def partialGxy1872(self,coord):

        return (-coord[0]+self.a)^4*(-coord[0]+self.b)^4*(12*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2+16*(-coord[1]+self.c)*(-coord[1]+self.d)^3+2*(-coord[1]+self.d)^4)

    def partialGxy1873(self,coord):

        return (-coord[0]+self.a)^4*(-coord[0]+self.b)^4*(12*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2+24*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3+6*(-coord[1]+self.c)*(-coord[1]+self.d)^4)

    def partialGxy1874(self,coord):

        return (-coord[0]+self.a)^4*(-coord[0]+self.b)^4*(12*(-coord[1]+self.c)^4*(-coord[1]+self.d)^2+32*(-coord[1]+self.c)^3*(-coord[1]+self.d)^3+12*(-coord[1]+self.c)^2*(-coord[1]+self.d)^4)

    def partialGxy2325(self,coord):

        return -2*coord[0]+self.a+self.b

    def partialGxy2326(self,coord):

        return (-coord[0]+self.a)*(-coord[1]+self.c)+(-coord[0]+self.b)*(-coord[1]+self.c)

    def partialGxy2327(self,coord):

        return (-coord[0]+self.a)*(-coord[1]+self.c)^2+(-coord[0]+self.b)*(-coord[1]+self.c)^2

    def partialGxy2328(self,coord):

        return (-coord[0]+self.a)*(-coord[1]+self.c)^3+(-coord[0]+self.b)*(-coord[1]+self.c)^3

    def partialGxy2329(self,coord):

        return (-coord[0]+self.a)*(-coord[1]+self.c)^4+(-coord[0]+self.b)*(-coord[1]+self.c)^4

    def partialGxy2330(self,coord):

        return (-coord[0]+self.a)*(-coord[1]+self.d)+(-coord[0]+self.b)*(-coord[1]+self.d)

    def partialGxy2331(self,coord):

        return (-coord[0]+self.a)*(-coord[1]+self.c)*(-coord[1]+self.d)+(-coord[0]+self.b)*(-coord[1]+self.c)*(-coord[1]+self.d)

    def partialGxy2332(self,coord):

        return (-coord[0]+self.a)*(-coord[1]+self.c)^2*(-coord[1]+self.d)+(-coord[0]+self.b)*(-coord[1]+self.c)^2*(-coord[1]+self.d)

    def partialGxy2333(self,coord):

        return (-coord[0]+self.a)*(-coord[1]+self.c)^3*(-coord[1]+self.d)+(-coord[0]+self.b)*(-coord[1]+self.c)^3*(-coord[1]+self.d)

    def partialGxy2334(self,coord):

        return (-coord[0]+self.a)*(-coord[1]+self.c)^4*(-coord[1]+self.d)+(-coord[0]+self.b)*(-coord[1]+self.c)^4*(-coord[1]+self.d)

    def partialGxy2335(self,coord):

        return (-coord[0]+self.a)*(-coord[1]+self.d)^2+(-coord[0]+self.b)*(-coord[1]+self.d)^2

    def partialGxy2336(self,coord):

        return (-coord[0]+self.a)*(-coord[1]+self.c)*(-coord[1]+self.d)^2+(-coord[0]+self.b)*(-coord[1]+self.c)*(-coord[1]+self.d)^2

    def partialGxy2337(self,coord):

        return (-coord[0]+self.a)*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2+(-coord[0]+self.b)*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2

    def partialGxy2338(self,coord):

        return (-coord[0]+self.a)*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2+(-coord[0]+self.b)*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2

    def partialGxy2339(self,coord):

        return (-coord[0]+self.a)*(-coord[1]+self.c)^4*(-coord[1]+self.d)^2+(-coord[0]+self.b)*(-coord[1]+self.c)^4*(-coord[1]+self.d)^2

    def partialGxy2340(self,coord):

        return (-coord[0]+self.a)*(-coord[1]+self.d)^3+(-coord[0]+self.b)*(-coord[1]+self.d)^3

    def partialGxy2341(self,coord):

        return (-coord[0]+self.a)*(-coord[1]+self.c)*(-coord[1]+self.d)^3+(-coord[0]+self.b)*(-coord[1]+self.c)*(-coord[1]+self.d)^3

    def partialGxy2342(self,coord):

        return (-coord[0]+self.a)*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3+(-coord[0]+self.b)*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3

    def partialGxy2343(self,coord):

        return (-coord[0]+self.a)*(-coord[1]+self.c)^3*(-coord[1]+self.d)^3+(-coord[0]+self.b)*(-coord[1]+self.c)^3*(-coord[1]+self.d)^3

    def partialGxy2344(self,coord):

        return (-coord[0]+self.a)*(-coord[1]+self.c)^4*(-coord[1]+self.d)^3+(-coord[0]+self.b)*(-coord[1]+self.c)^4*(-coord[1]+self.d)^3

    def partialGxy2345(self,coord):

        return (-coord[0]+self.a)*(-coord[1]+self.d)^4+(-coord[0]+self.b)*(-coord[1]+self.d)^4

    def partialGxy2346(self,coord):

        return (-coord[0]+self.a)*(-coord[1]+self.c)*(-coord[1]+self.d)^4+(-coord[0]+self.b)*(-coord[1]+self.c)*(-coord[1]+self.d)^4

    def partialGxy2347(self,coord):

        return (-coord[0]+self.a)*(-coord[1]+self.c)^2*(-coord[1]+self.d)^4+(-coord[0]+self.b)*(-coord[1]+self.c)^2*(-coord[1]+self.d)^4

    def partialGxy2348(self,coord):

        return (-coord[0]+self.a)*(-coord[1]+self.c)^3*(-coord[1]+self.d)^4+(-coord[0]+self.b)*(-coord[1]+self.c)^3*(-coord[1]+self.d)^4

    def partialGxy2349(self,coord):

        return (-coord[0]+self.a)*(-coord[1]+self.c)^4*(-coord[1]+self.d)^4+(-coord[0]+self.b)*(-coord[1]+self.c)^4*(-coord[1]+self.d)^4

    def partialGxy2356(self,coord):

        return (-coord[0]+self.a)*(-coord[1]+self.c)+(-coord[0]+self.b)*(-coord[1]+self.c)+(-coord[0]+self.a)*(-coord[1]+self.d)+(-coord[0]+self.b)*(-coord[1]+self.d)

    def partialGxy2357(self,coord):

        return (-coord[0]+self.a)*(-coord[1]+self.c)^2+(-coord[0]+self.b)*(-coord[1]+self.c)^2+2*(-coord[0]+self.a)*(-coord[1]+self.c)*(-coord[1]+self.d)+2*(-coord[0]+self.b)*(-coord[1]+self.c)*(-coord[1]+self.d)

    def partialGxy2358(self,coord):

        return (-coord[0]+self.a)*(-coord[1]+self.c)^3+(-coord[0]+self.b)*(-coord[1]+self.c)^3+3*(-coord[0]+self.a)*(-coord[1]+self.c)^2*(-coord[1]+self.d)+3*(-coord[0]+self.b)*(-coord[1]+self.c)^2*(-coord[1]+self.d)

    def partialGxy2359(self,coord):

        return (-coord[0]+self.a)*(-coord[1]+self.c)^4+(-coord[0]+self.b)*(-coord[1]+self.c)^4+4*(-coord[0]+self.a)*(-coord[1]+self.c)^3*(-coord[1]+self.d)+4*(-coord[0]+self.b)*(-coord[1]+self.c)^3*(-coord[1]+self.d)

    def partialGxy2361(self,coord):

        return 2*(-coord[0]+self.a)*(-coord[1]+self.c)*(-coord[1]+self.d)+2*(-coord[0]+self.b)*(-coord[1]+self.c)*(-coord[1]+self.d)+(-coord[0]+self.a)*(-coord[1]+self.d)^2+(-coord[0]+self.b)*(-coord[1]+self.d)^2

    def partialGxy2362(self,coord):

        return 2*(-coord[0]+self.a)*(-coord[1]+self.c)^2*(-coord[1]+self.d)+2*(-coord[0]+self.b)*(-coord[1]+self.c)^2*(-coord[1]+self.d)+2*(-coord[0]+self.a)*(-coord[1]+self.c)*(-coord[1]+self.d)^2+2*(-coord[0]+self.b)*(-coord[1]+self.c)*(-coord[1]+self.d)^2

    def partialGxy2363(self,coord):

        return 2*(-coord[0]+self.a)*(-coord[1]+self.c)^3*(-coord[1]+self.d)+2*(-coord[0]+self.b)*(-coord[1]+self.c)^3*(-coord[1]+self.d)+3*(-coord[0]+self.a)*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2+3*(-coord[0]+self.b)*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2

    def partialGxy2364(self,coord):

        return 2*(-coord[0]+self.a)*(-coord[1]+self.c)^4*(-coord[1]+self.d)+2*(-coord[0]+self.b)*(-coord[1]+self.c)^4*(-coord[1]+self.d)+4*(-coord[0]+self.a)*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2+4*(-coord[0]+self.b)*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2

    def partialGxy2366(self,coord):

        return 3*(-coord[0]+self.a)*(-coord[1]+self.c)*(-coord[1]+self.d)^2+3*(-coord[0]+self.b)*(-coord[1]+self.c)*(-coord[1]+self.d)^2+(-coord[0]+self.a)*(-coord[1]+self.d)^3+(-coord[0]+self.b)*(-coord[1]+self.d)^3

    def partialGxy2367(self,coord):

        return 3*(-coord[0]+self.a)*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2+3*(-coord[0]+self.b)*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2+2*(-coord[0]+self.a)*(-coord[1]+self.c)*(-coord[1]+self.d)^3+2*(-coord[0]+self.b)*(-coord[1]+self.c)*(-coord[1]+self.d)^3

    def partialGxy2368(self,coord):

        return 3*(-coord[0]+self.a)*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2+3*(-coord[0]+self.b)*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2+3*(-coord[0]+self.a)*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3+3*(-coord[0]+self.b)*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3

    def partialGxy2369(self,coord):

        return 3*(-coord[0]+self.a)*(-coord[1]+self.c)^4*(-coord[1]+self.d)^2+3*(-coord[0]+self.b)*(-coord[1]+self.c)^4*(-coord[1]+self.d)^2+4*(-coord[0]+self.a)*(-coord[1]+self.c)^3*(-coord[1]+self.d)^3+4*(-coord[0]+self.b)*(-coord[1]+self.c)^3*(-coord[1]+self.d)^3

    def partialGxy2371(self,coord):

        return 4*(-coord[0]+self.a)*(-coord[1]+self.c)*(-coord[1]+self.d)^3+4*(-coord[0]+self.b)*(-coord[1]+self.c)*(-coord[1]+self.d)^3+(-coord[0]+self.a)*(-coord[1]+self.d)^4+(-coord[0]+self.b)*(-coord[1]+self.d)^4

    def partialGxy2372(self,coord):

        return 4*(-coord[0]+self.a)*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3+4*(-coord[0]+self.b)*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3+2*(-coord[0]+self.a)*(-coord[1]+self.c)*(-coord[1]+self.d)^4+2*(-coord[0]+self.b)*(-coord[1]+self.c)*(-coord[1]+self.d)^4

    def partialGxy2373(self,coord):

        return 4*(-coord[0]+self.a)*(-coord[1]+self.c)^3*(-coord[1]+self.d)^3+4*(-coord[0]+self.b)*(-coord[1]+self.c)^3*(-coord[1]+self.d)^3+3*(-coord[0]+self.a)*(-coord[1]+self.c)^2*(-coord[1]+self.d)^4+3*(-coord[0]+self.b)*(-coord[1]+self.c)^2*(-coord[1]+self.d)^4

    def partialGxy2374(self,coord):

        return 4*(-coord[0]+self.a)*(-coord[1]+self.c)^4*(-coord[1]+self.d)^3+4*(-coord[0]+self.b)*(-coord[1]+self.c)^4*(-coord[1]+self.d)^3+4*(-coord[0]+self.a)*(-coord[1]+self.c)^3*(-coord[1]+self.d)^4+4*(-coord[0]+self.b)*(-coord[1]+self.c)^3*(-coord[1]+self.d)^4

    def partialGxy2387(self,coord):

        return (-coord[0]+self.a)*(2*(-coord[1]+self.c)^2+8*(-coord[1]+self.c)*(-coord[1]+self.d)+2*(-coord[1]+self.d)^2)+(-coord[0]+self.b)*(2*(-coord[1]+self.c)^2+8*(-coord[1]+self.c)*(-coord[1]+self.d)+2*(-coord[1]+self.d)^2)

    def partialGxy2388(self,coord):

        return (-coord[0]+self.a)*(2*(-coord[1]+self.c)^3+12*(-coord[1]+self.c)^2*(-coord[1]+self.d)+6*(-coord[1]+self.c)*(-coord[1]+self.d)^2)+(-coord[0]+self.b)*(2*(-coord[1]+self.c)^3+12*(-coord[1]+self.c)^2*(-coord[1]+self.d)+6*(-coord[1]+self.c)*(-coord[1]+self.d)^2)

    def partialGxy2389(self,coord):

        return (-coord[0]+self.a)*(2*(-coord[1]+self.c)^4+16*(-coord[1]+self.c)^3*(-coord[1]+self.d)+12*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2)+(-coord[0]+self.b)*(2*(-coord[1]+self.c)^4+16*(-coord[1]+self.c)^3*(-coord[1]+self.d)+12*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2)

    def partialGxy2392(self,coord):

        return (-coord[0]+self.a)*(6*(-coord[1]+self.c)^2*(-coord[1]+self.d)+12*(-coord[1]+self.c)*(-coord[1]+self.d)^2+2*(-coord[1]+self.d)^3)+(-coord[0]+self.b)*(6*(-coord[1]+self.c)^2*(-coord[1]+self.d)+12*(-coord[1]+self.c)*(-coord[1]+self.d)^2+2*(-coord[1]+self.d)^3)

    def partialGxy2393(self,coord):

        return (-coord[0]+self.a)*(6*(-coord[1]+self.c)^3*(-coord[1]+self.d)+18*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2+6*(-coord[1]+self.c)*(-coord[1]+self.d)^3)+(-coord[0]+self.b)*(6*(-coord[1]+self.c)^3*(-coord[1]+self.d)+18*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2+6*(-coord[1]+self.c)*(-coord[1]+self.d)^3)

    def partialGxy2394(self,coord):

        return (-coord[0]+self.a)*(6*(-coord[1]+self.c)^4*(-coord[1]+self.d)+24*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2+12*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3)+(-coord[0]+self.b)*(6*(-coord[1]+self.c)^4*(-coord[1]+self.d)+24*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2+12*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3)

    def partialGxy2397(self,coord):

        return (-coord[0]+self.a)*(12*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2+16*(-coord[1]+self.c)*(-coord[1]+self.d)^3+2*(-coord[1]+self.d)^4)+(-coord[0]+self.b)*(12*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2+16*(-coord[1]+self.c)*(-coord[1]+self.d)^3+2*(-coord[1]+self.d)^4)

    def partialGxy2398(self,coord):

        return (-coord[0]+self.a)*(12*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2+24*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3+6*(-coord[1]+self.c)*(-coord[1]+self.d)^4)+(-coord[0]+self.b)*(12*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2+24*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3+6*(-coord[1]+self.c)*(-coord[1]+self.d)^4)

    def partialGxy2399(self,coord):

        return (-coord[0]+self.a)*(12*(-coord[1]+self.c)^4*(-coord[1]+self.d)^2+32*(-coord[1]+self.c)^3*(-coord[1]+self.d)^3+12*(-coord[1]+self.c)^2*(-coord[1]+self.d)^4)+(-coord[0]+self.b)*(12*(-coord[1]+self.c)^4*(-coord[1]+self.d)^2+32*(-coord[1]+self.c)^3*(-coord[1]+self.d)^3+12*(-coord[1]+self.c)^2*(-coord[1]+self.d)^4)

    def partialGxy2400(self,coord):

        return (-coord[0]+self.a)^2+2*(-coord[0]+self.a)*(-coord[0]+self.b)

    def partialGxy2401(self,coord):

        return (-coord[0]+self.a)^2*(-coord[1]+self.c)+2*(-coord[0]+self.a)*(-coord[0]+self.b)*(-coord[1]+self.c)

    def partialGxy2402(self,coord):

        return (-coord[0]+self.a)^2*(-coord[1]+self.c)^2+2*(-coord[0]+self.a)*(-coord[0]+self.b)*(-coord[1]+self.c)^2

    def partialGxy2403(self,coord):

        return (-coord[0]+self.a)^2*(-coord[1]+self.c)^3+2*(-coord[0]+self.a)*(-coord[0]+self.b)*(-coord[1]+self.c)^3

    def partialGxy2404(self,coord):

        return (-coord[0]+self.a)^2*(-coord[1]+self.c)^4+2*(-coord[0]+self.a)*(-coord[0]+self.b)*(-coord[1]+self.c)^4

    def partialGxy2405(self,coord):

        return (-coord[0]+self.a)^2*(-coord[1]+self.d)+2*(-coord[0]+self.a)*(-coord[0]+self.b)*(-coord[1]+self.d)

    def partialGxy2406(self,coord):

        return (-coord[0]+self.a)^2*(-coord[1]+self.c)*(-coord[1]+self.d)+2*(-coord[0]+self.a)*(-coord[0]+self.b)*(-coord[1]+self.c)*(-coord[1]+self.d)

    def partialGxy2407(self,coord):

        return (-coord[0]+self.a)^2*(-coord[1]+self.c)^2*(-coord[1]+self.d)+2*(-coord[0]+self.a)*(-coord[0]+self.b)*(-coord[1]+self.c)^2*(-coord[1]+self.d)

    def partialGxy2408(self,coord):

        return (-coord[0]+self.a)^2*(-coord[1]+self.c)^3*(-coord[1]+self.d)+2*(-coord[0]+self.a)*(-coord[0]+self.b)*(-coord[1]+self.c)^3*(-coord[1]+self.d)

    def partialGxy2409(self,coord):

        return (-coord[0]+self.a)^2*(-coord[1]+self.c)^4*(-coord[1]+self.d)+2*(-coord[0]+self.a)*(-coord[0]+self.b)*(-coord[1]+self.c)^4*(-coord[1]+self.d)

    def partialGxy2410(self,coord):

        return (-coord[0]+self.a)^2*(-coord[1]+self.d)^2+2*(-coord[0]+self.a)*(-coord[0]+self.b)*(-coord[1]+self.d)^2

    def partialGxy2411(self,coord):

        return (-coord[0]+self.a)^2*(-coord[1]+self.c)*(-coord[1]+self.d)^2+2*(-coord[0]+self.a)*(-coord[0]+self.b)*(-coord[1]+self.c)*(-coord[1]+self.d)^2

    def partialGxy2412(self,coord):

        return (-coord[0]+self.a)^2*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2+2*(-coord[0]+self.a)*(-coord[0]+self.b)*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2

    def partialGxy2413(self,coord):

        return (-coord[0]+self.a)^2*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2+2*(-coord[0]+self.a)*(-coord[0]+self.b)*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2

    def partialGxy2414(self,coord):

        return (-coord[0]+self.a)^2*(-coord[1]+self.c)^4*(-coord[1]+self.d)^2+2*(-coord[0]+self.a)*(-coord[0]+self.b)*(-coord[1]+self.c)^4*(-coord[1]+self.d)^2

    def partialGxy2415(self,coord):

        return (-coord[0]+self.a)^2*(-coord[1]+self.d)^3+2*(-coord[0]+self.a)*(-coord[0]+self.b)*(-coord[1]+self.d)^3

    def partialGxy2416(self,coord):

        return (-coord[0]+self.a)^2*(-coord[1]+self.c)*(-coord[1]+self.d)^3+2*(-coord[0]+self.a)*(-coord[0]+self.b)*(-coord[1]+self.c)*(-coord[1]+self.d)^3

    def partialGxy2417(self,coord):

        return (-coord[0]+self.a)^2*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3+2*(-coord[0]+self.a)*(-coord[0]+self.b)*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3

    def partialGxy2418(self,coord):

        return (-coord[0]+self.a)^2*(-coord[1]+self.c)^3*(-coord[1]+self.d)^3+2*(-coord[0]+self.a)*(-coord[0]+self.b)*(-coord[1]+self.c)^3*(-coord[1]+self.d)^3

    def partialGxy2419(self,coord):

        return (-coord[0]+self.a)^2*(-coord[1]+self.c)^4*(-coord[1]+self.d)^3+2*(-coord[0]+self.a)*(-coord[0]+self.b)*(-coord[1]+self.c)^4*(-coord[1]+self.d)^3

    def partialGxy2420(self,coord):

        return (-coord[0]+self.a)^2*(-coord[1]+self.d)^4+2*(-coord[0]+self.a)*(-coord[0]+self.b)*(-coord[1]+self.d)^4

    def partialGxy2421(self,coord):

        return (-coord[0]+self.a)^2*(-coord[1]+self.c)*(-coord[1]+self.d)^4+2*(-coord[0]+self.a)*(-coord[0]+self.b)*(-coord[1]+self.c)*(-coord[1]+self.d)^4

    def partialGxy2422(self,coord):

        return (-coord[0]+self.a)^2*(-coord[1]+self.c)^2*(-coord[1]+self.d)^4+2*(-coord[0]+self.a)*(-coord[0]+self.b)*(-coord[1]+self.c)^2*(-coord[1]+self.d)^4

    def partialGxy2423(self,coord):

        return (-coord[0]+self.a)^2*(-coord[1]+self.c)^3*(-coord[1]+self.d)^4+2*(-coord[0]+self.a)*(-coord[0]+self.b)*(-coord[1]+self.c)^3*(-coord[1]+self.d)^4

    def partialGxy2424(self,coord):

        return (-coord[0]+self.a)^2*(-coord[1]+self.c)^4*(-coord[1]+self.d)^4+2*(-coord[0]+self.a)*(-coord[0]+self.b)*(-coord[1]+self.c)^4*(-coord[1]+self.d)^4

    def partialGxy2431(self,coord):

        return (-coord[0]+self.a)^2*(-coord[1]+self.c)+2*(-coord[0]+self.a)*(-coord[0]+self.b)*(-coord[1]+self.c)+(-coord[0]+self.a)^2*(-coord[1]+self.d)+2*(-coord[0]+self.a)*(-coord[0]+self.b)*(-coord[1]+self.d)

    def partialGxy2432(self,coord):

        return (-coord[0]+self.a)^2*(-coord[1]+self.c)^2+2*(-coord[0]+self.a)*(-coord[0]+self.b)*(-coord[1]+self.c)^2+2*(-coord[0]+self.a)^2*(-coord[1]+self.c)*(-coord[1]+self.d)+4*(-coord[0]+self.a)*(-coord[0]+self.b)*(-coord[1]+self.c)*(-coord[1]+self.d)

    def partialGxy2433(self,coord):

        return (-coord[0]+self.a)^2*(-coord[1]+self.c)^3+2*(-coord[0]+self.a)*(-coord[0]+self.b)*(-coord[1]+self.c)^3+3*(-coord[0]+self.a)^2*(-coord[1]+self.c)^2*(-coord[1]+self.d)+6*(-coord[0]+self.a)*(-coord[0]+self.b)*(-coord[1]+self.c)^2*(-coord[1]+self.d)

    def partialGxy2434(self,coord):

        return (-coord[0]+self.a)^2*(-coord[1]+self.c)^4+2*(-coord[0]+self.a)*(-coord[0]+self.b)*(-coord[1]+self.c)^4+4*(-coord[0]+self.a)^2*(-coord[1]+self.c)^3*(-coord[1]+self.d)+8*(-coord[0]+self.a)*(-coord[0]+self.b)*(-coord[1]+self.c)^3*(-coord[1]+self.d)

    def partialGxy2436(self,coord):

        return 2*(-coord[0]+self.a)^2*(-coord[1]+self.c)*(-coord[1]+self.d)+4*(-coord[0]+self.a)*(-coord[0]+self.b)*(-coord[1]+self.c)*(-coord[1]+self.d)+(-coord[0]+self.a)^2*(-coord[1]+self.d)^2+2*(-coord[0]+self.a)*(-coord[0]+self.b)*(-coord[1]+self.d)^2

    def partialGxy2437(self,coord):

        return 2*(-coord[0]+self.a)^2*(-coord[1]+self.c)^2*(-coord[1]+self.d)+4*(-coord[0]+self.a)*(-coord[0]+self.b)*(-coord[1]+self.c)^2*(-coord[1]+self.d)+2*(-coord[0]+self.a)^2*(-coord[1]+self.c)*(-coord[1]+self.d)^2+4*(-coord[0]+self.a)*(-coord[0]+self.b)*(-coord[1]+self.c)*(-coord[1]+self.d)^2

    def partialGxy2438(self,coord):

        return 2*(-coord[0]+self.a)^2*(-coord[1]+self.c)^3*(-coord[1]+self.d)+4*(-coord[0]+self.a)*(-coord[0]+self.b)*(-coord[1]+self.c)^3*(-coord[1]+self.d)+3*(-coord[0]+self.a)^2*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2+6*(-coord[0]+self.a)*(-coord[0]+self.b)*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2

    def partialGxy2439(self,coord):

        return 2*(-coord[0]+self.a)^2*(-coord[1]+self.c)^4*(-coord[1]+self.d)+4*(-coord[0]+self.a)*(-coord[0]+self.b)*(-coord[1]+self.c)^4*(-coord[1]+self.d)+4*(-coord[0]+self.a)^2*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2+8*(-coord[0]+self.a)*(-coord[0]+self.b)*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2

    def partialGxy2441(self,coord):

        return 3*(-coord[0]+self.a)^2*(-coord[1]+self.c)*(-coord[1]+self.d)^2+6*(-coord[0]+self.a)*(-coord[0]+self.b)*(-coord[1]+self.c)*(-coord[1]+self.d)^2+(-coord[0]+self.a)^2*(-coord[1]+self.d)^3+2*(-coord[0]+self.a)*(-coord[0]+self.b)*(-coord[1]+self.d)^3

    def partialGxy2442(self,coord):

        return 3*(-coord[0]+self.a)^2*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2+6*(-coord[0]+self.a)*(-coord[0]+self.b)*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2+2*(-coord[0]+self.a)^2*(-coord[1]+self.c)*(-coord[1]+self.d)^3+4*(-coord[0]+self.a)*(-coord[0]+self.b)*(-coord[1]+self.c)*(-coord[1]+self.d)^3

    def partialGxy2443(self,coord):

        return 3*(-coord[0]+self.a)^2*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2+6*(-coord[0]+self.a)*(-coord[0]+self.b)*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2+3*(-coord[0]+self.a)^2*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3+6*(-coord[0]+self.a)*(-coord[0]+self.b)*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3

    def partialGxy2444(self,coord):

        return 3*(-coord[0]+self.a)^2*(-coord[1]+self.c)^4*(-coord[1]+self.d)^2+6*(-coord[0]+self.a)*(-coord[0]+self.b)*(-coord[1]+self.c)^4*(-coord[1]+self.d)^2+4*(-coord[0]+self.a)^2*(-coord[1]+self.c)^3*(-coord[1]+self.d)^3+8*(-coord[0]+self.a)*(-coord[0]+self.b)*(-coord[1]+self.c)^3*(-coord[1]+self.d)^3

    def partialGxy2446(self,coord):

        return 4*(-coord[0]+self.a)^2*(-coord[1]+self.c)*(-coord[1]+self.d)^3+8*(-coord[0]+self.a)*(-coord[0]+self.b)*(-coord[1]+self.c)*(-coord[1]+self.d)^3+(-coord[0]+self.a)^2*(-coord[1]+self.d)^4+2*(-coord[0]+self.a)*(-coord[0]+self.b)*(-coord[1]+self.d)^4

    def partialGxy2447(self,coord):

        return 4*(-coord[0]+self.a)^2*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3+8*(-coord[0]+self.a)*(-coord[0]+self.b)*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3+2*(-coord[0]+self.a)^2*(-coord[1]+self.c)*(-coord[1]+self.d)^4+4*(-coord[0]+self.a)*(-coord[0]+self.b)*(-coord[1]+self.c)*(-coord[1]+self.d)^4

    def partialGxy2448(self,coord):

        return 4*(-coord[0]+self.a)^2*(-coord[1]+self.c)^3*(-coord[1]+self.d)^3+8*(-coord[0]+self.a)*(-coord[0]+self.b)*(-coord[1]+self.c)^3*(-coord[1]+self.d)^3+3*(-coord[0]+self.a)^2*(-coord[1]+self.c)^2*(-coord[1]+self.d)^4+6*(-coord[0]+self.a)*(-coord[0]+self.b)*(-coord[1]+self.c)^2*(-coord[1]+self.d)^4

    def partialGxy2449(self,coord):

        return 4*(-coord[0]+self.a)^2*(-coord[1]+self.c)^4*(-coord[1]+self.d)^3+8*(-coord[0]+self.a)*(-coord[0]+self.b)*(-coord[1]+self.c)^4*(-coord[1]+self.d)^3+4*(-coord[0]+self.a)^2*(-coord[1]+self.c)^3*(-coord[1]+self.d)^4+8*(-coord[0]+self.a)*(-coord[0]+self.b)*(-coord[1]+self.c)^3*(-coord[1]+self.d)^4

    def partialGxy2462(self,coord):

        return (-coord[0]+self.a)^2*(2*(-coord[1]+self.c)^2+8*(-coord[1]+self.c)*(-coord[1]+self.d)+2*(-coord[1]+self.d)^2)+2*(-coord[0]+self.a)*(-coord[0]+self.b)*(2*(-coord[1]+self.c)^2+8*(-coord[1]+self.c)*(-coord[1]+self.d)+2*(-coord[1]+self.d)^2)

    def partialGxy2463(self,coord):

        return (-coord[0]+self.a)^2*(2*(-coord[1]+self.c)^3+12*(-coord[1]+self.c)^2*(-coord[1]+self.d)+6*(-coord[1]+self.c)*(-coord[1]+self.d)^2)+2*(-coord[0]+self.a)*(-coord[0]+self.b)*(2*(-coord[1]+self.c)^3+12*(-coord[1]+self.c)^2*(-coord[1]+self.d)+6*(-coord[1]+self.c)*(-coord[1]+self.d)^2)

    def partialGxy2464(self,coord):

        return (-coord[0]+self.a)^2*(2*(-coord[1]+self.c)^4+16*(-coord[1]+self.c)^3*(-coord[1]+self.d)+12*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2)+2*(-coord[0]+self.a)*(-coord[0]+self.b)*(2*(-coord[1]+self.c)^4+16*(-coord[1]+self.c)^3*(-coord[1]+self.d)+12*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2)

    def partialGxy2467(self,coord):

        return (-coord[0]+self.a)^2*(6*(-coord[1]+self.c)^2*(-coord[1]+self.d)+12*(-coord[1]+self.c)*(-coord[1]+self.d)^2+2*(-coord[1]+self.d)^3)+2*(-coord[0]+self.a)*(-coord[0]+self.b)*(6*(-coord[1]+self.c)^2*(-coord[1]+self.d)+12*(-coord[1]+self.c)*(-coord[1]+self.d)^2+2*(-coord[1]+self.d)^3)

    def partialGxy2468(self,coord):

        return (-coord[0]+self.a)^2*(6*(-coord[1]+self.c)^3*(-coord[1]+self.d)+18*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2+6*(-coord[1]+self.c)*(-coord[1]+self.d)^3)+2*(-coord[0]+self.a)*(-coord[0]+self.b)*(6*(-coord[1]+self.c)^3*(-coord[1]+self.d)+18*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2+6*(-coord[1]+self.c)*(-coord[1]+self.d)^3)

    def partialGxy2469(self,coord):

        return (-coord[0]+self.a)^2*(6*(-coord[1]+self.c)^4*(-coord[1]+self.d)+24*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2+12*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3)+2*(-coord[0]+self.a)*(-coord[0]+self.b)*(6*(-coord[1]+self.c)^4*(-coord[1]+self.d)+24*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2+12*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3)

    def partialGxy2472(self,coord):

        return (-coord[0]+self.a)^2*(12*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2+16*(-coord[1]+self.c)*(-coord[1]+self.d)^3+2*(-coord[1]+self.d)^4)+2*(-coord[0]+self.a)*(-coord[0]+self.b)*(12*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2+16*(-coord[1]+self.c)*(-coord[1]+self.d)^3+2*(-coord[1]+self.d)^4)

    def partialGxy2473(self,coord):

        return (-coord[0]+self.a)^2*(12*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2+24*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3+6*(-coord[1]+self.c)*(-coord[1]+self.d)^4)+2*(-coord[0]+self.a)*(-coord[0]+self.b)*(12*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2+24*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3+6*(-coord[1]+self.c)*(-coord[1]+self.d)^4)

    def partialGxy2474(self,coord):

        return (-coord[0]+self.a)^2*(12*(-coord[1]+self.c)^4*(-coord[1]+self.d)^2+32*(-coord[1]+self.c)^3*(-coord[1]+self.d)^3+12*(-coord[1]+self.c)^2*(-coord[1]+self.d)^4)+2*(-coord[0]+self.a)*(-coord[0]+self.b)*(12*(-coord[1]+self.c)^4*(-coord[1]+self.d)^2+32*(-coord[1]+self.c)^3*(-coord[1]+self.d)^3+12*(-coord[1]+self.c)^2*(-coord[1]+self.d)^4)

    def partialGxy2475(self,coord):

        return (-coord[0]+self.a)^3+3*(-coord[0]+self.a)^2*(-coord[0]+self.b)

    def partialGxy2476(self,coord):

        return (-coord[0]+self.a)^3*(-coord[1]+self.c)+3*(-coord[0]+self.a)^2*(-coord[0]+self.b)*(-coord[1]+self.c)

    def partialGxy2477(self,coord):

        return (-coord[0]+self.a)^3*(-coord[1]+self.c)^2+3*(-coord[0]+self.a)^2*(-coord[0]+self.b)*(-coord[1]+self.c)^2

    def partialGxy2478(self,coord):

        return (-coord[0]+self.a)^3*(-coord[1]+self.c)^3+3*(-coord[0]+self.a)^2*(-coord[0]+self.b)*(-coord[1]+self.c)^3

    def partialGxy2479(self,coord):

        return (-coord[0]+self.a)^3*(-coord[1]+self.c)^4+3*(-coord[0]+self.a)^2*(-coord[0]+self.b)*(-coord[1]+self.c)^4

    def partialGxy2480(self,coord):

        return (-coord[0]+self.a)^3*(-coord[1]+self.d)+3*(-coord[0]+self.a)^2*(-coord[0]+self.b)*(-coord[1]+self.d)

    def partialGxy2481(self,coord):

        return (-coord[0]+self.a)^3*(-coord[1]+self.c)*(-coord[1]+self.d)+3*(-coord[0]+self.a)^2*(-coord[0]+self.b)*(-coord[1]+self.c)*(-coord[1]+self.d)

    def partialGxy2482(self,coord):

        return (-coord[0]+self.a)^3*(-coord[1]+self.c)^2*(-coord[1]+self.d)+3*(-coord[0]+self.a)^2*(-coord[0]+self.b)*(-coord[1]+self.c)^2*(-coord[1]+self.d)

    def partialGxy2483(self,coord):

        return (-coord[0]+self.a)^3*(-coord[1]+self.c)^3*(-coord[1]+self.d)+3*(-coord[0]+self.a)^2*(-coord[0]+self.b)*(-coord[1]+self.c)^3*(-coord[1]+self.d)

    def partialGxy2484(self,coord):

        return (-coord[0]+self.a)^3*(-coord[1]+self.c)^4*(-coord[1]+self.d)+3*(-coord[0]+self.a)^2*(-coord[0]+self.b)*(-coord[1]+self.c)^4*(-coord[1]+self.d)

    def partialGxy2485(self,coord):

        return (-coord[0]+self.a)^3*(-coord[1]+self.d)^2+3*(-coord[0]+self.a)^2*(-coord[0]+self.b)*(-coord[1]+self.d)^2

    def partialGxy2486(self,coord):

        return (-coord[0]+self.a)^3*(-coord[1]+self.c)*(-coord[1]+self.d)^2+3*(-coord[0]+self.a)^2*(-coord[0]+self.b)*(-coord[1]+self.c)*(-coord[1]+self.d)^2

    def partialGxy2487(self,coord):

        return (-coord[0]+self.a)^3*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2+3*(-coord[0]+self.a)^2*(-coord[0]+self.b)*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2

    def partialGxy2488(self,coord):

        return (-coord[0]+self.a)^3*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2+3*(-coord[0]+self.a)^2*(-coord[0]+self.b)*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2

    def partialGxy2489(self,coord):

        return (-coord[0]+self.a)^3*(-coord[1]+self.c)^4*(-coord[1]+self.d)^2+3*(-coord[0]+self.a)^2*(-coord[0]+self.b)*(-coord[1]+self.c)^4*(-coord[1]+self.d)^2

    def partialGxy2490(self,coord):

        return (-coord[0]+self.a)^3*(-coord[1]+self.d)^3+3*(-coord[0]+self.a)^2*(-coord[0]+self.b)*(-coord[1]+self.d)^3

    def partialGxy2491(self,coord):

        return (-coord[0]+self.a)^3*(-coord[1]+self.c)*(-coord[1]+self.d)^3+3*(-coord[0]+self.a)^2*(-coord[0]+self.b)*(-coord[1]+self.c)*(-coord[1]+self.d)^3

    def partialGxy2492(self,coord):

        return (-coord[0]+self.a)^3*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3+3*(-coord[0]+self.a)^2*(-coord[0]+self.b)*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3

    def partialGxy2493(self,coord):

        return (-coord[0]+self.a)^3*(-coord[1]+self.c)^3*(-coord[1]+self.d)^3+3*(-coord[0]+self.a)^2*(-coord[0]+self.b)*(-coord[1]+self.c)^3*(-coord[1]+self.d)^3

    def partialGxy2494(self,coord):

        return (-coord[0]+self.a)^3*(-coord[1]+self.c)^4*(-coord[1]+self.d)^3+3*(-coord[0]+self.a)^2*(-coord[0]+self.b)*(-coord[1]+self.c)^4*(-coord[1]+self.d)^3

    def partialGxy2495(self,coord):

        return (-coord[0]+self.a)^3*(-coord[1]+self.d)^4+3*(-coord[0]+self.a)^2*(-coord[0]+self.b)*(-coord[1]+self.d)^4

    def partialGxy2496(self,coord):

        return (-coord[0]+self.a)^3*(-coord[1]+self.c)*(-coord[1]+self.d)^4+3*(-coord[0]+self.a)^2*(-coord[0]+self.b)*(-coord[1]+self.c)*(-coord[1]+self.d)^4

    def partialGxy2497(self,coord):

        return (-coord[0]+self.a)^3*(-coord[1]+self.c)^2*(-coord[1]+self.d)^4+3*(-coord[0]+self.a)^2*(-coord[0]+self.b)*(-coord[1]+self.c)^2*(-coord[1]+self.d)^4

    def partialGxy2498(self,coord):

        return (-coord[0]+self.a)^3*(-coord[1]+self.c)^3*(-coord[1]+self.d)^4+3*(-coord[0]+self.a)^2*(-coord[0]+self.b)*(-coord[1]+self.c)^3*(-coord[1]+self.d)^4

    def partialGxy2499(self,coord):

        return (-coord[0]+self.a)^3*(-coord[1]+self.c)^4*(-coord[1]+self.d)^4+3*(-coord[0]+self.a)^2*(-coord[0]+self.b)*(-coord[1]+self.c)^4*(-coord[1]+self.d)^4

    def partialGxy2506(self,coord):

        return (-coord[0]+self.a)^3*(-coord[1]+self.c)+3*(-coord[0]+self.a)^2*(-coord[0]+self.b)*(-coord[1]+self.c)+(-coord[0]+self.a)^3*(-coord[1]+self.d)+3*(-coord[0]+self.a)^2*(-coord[0]+self.b)*(-coord[1]+self.d)

    def partialGxy2507(self,coord):

        return (-coord[0]+self.a)^3*(-coord[1]+self.c)^2+3*(-coord[0]+self.a)^2*(-coord[0]+self.b)*(-coord[1]+self.c)^2+2*(-coord[0]+self.a)^3*(-coord[1]+self.c)*(-coord[1]+self.d)+6*(-coord[0]+self.a)^2*(-coord[0]+self.b)*(-coord[1]+self.c)*(-coord[1]+self.d)

    def partialGxy2508(self,coord):

        return (-coord[0]+self.a)^3*(-coord[1]+self.c)^3+3*(-coord[0]+self.a)^2*(-coord[0]+self.b)*(-coord[1]+self.c)^3+3*(-coord[0]+self.a)^3*(-coord[1]+self.c)^2*(-coord[1]+self.d)+9*(-coord[0]+self.a)^2*(-coord[0]+self.b)*(-coord[1]+self.c)^2*(-coord[1]+self.d)

    def partialGxy2509(self,coord):

        return (-coord[0]+self.a)^3*(-coord[1]+self.c)^4+3*(-coord[0]+self.a)^2*(-coord[0]+self.b)*(-coord[1]+self.c)^4+4*(-coord[0]+self.a)^3*(-coord[1]+self.c)^3*(-coord[1]+self.d)+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)*(-coord[1]+self.c)^3*(-coord[1]+self.d)

    def partialGxy2511(self,coord):

        return 2*(-coord[0]+self.a)^3*(-coord[1]+self.c)*(-coord[1]+self.d)+6*(-coord[0]+self.a)^2*(-coord[0]+self.b)*(-coord[1]+self.c)*(-coord[1]+self.d)+(-coord[0]+self.a)^3*(-coord[1]+self.d)^2+3*(-coord[0]+self.a)^2*(-coord[0]+self.b)*(-coord[1]+self.d)^2

    def partialGxy2512(self,coord):

        return 2*(-coord[0]+self.a)^3*(-coord[1]+self.c)^2*(-coord[1]+self.d)+6*(-coord[0]+self.a)^2*(-coord[0]+self.b)*(-coord[1]+self.c)^2*(-coord[1]+self.d)+2*(-coord[0]+self.a)^3*(-coord[1]+self.c)*(-coord[1]+self.d)^2+6*(-coord[0]+self.a)^2*(-coord[0]+self.b)*(-coord[1]+self.c)*(-coord[1]+self.d)^2

    def partialGxy2513(self,coord):

        return 2*(-coord[0]+self.a)^3*(-coord[1]+self.c)^3*(-coord[1]+self.d)+6*(-coord[0]+self.a)^2*(-coord[0]+self.b)*(-coord[1]+self.c)^3*(-coord[1]+self.d)+3*(-coord[0]+self.a)^3*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2+9*(-coord[0]+self.a)^2*(-coord[0]+self.b)*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2

    def partialGxy2514(self,coord):

        return 2*(-coord[0]+self.a)^3*(-coord[1]+self.c)^4*(-coord[1]+self.d)+6*(-coord[0]+self.a)^2*(-coord[0]+self.b)*(-coord[1]+self.c)^4*(-coord[1]+self.d)+4*(-coord[0]+self.a)^3*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2

    def partialGxy2516(self,coord):

        return 3*(-coord[0]+self.a)^3*(-coord[1]+self.c)*(-coord[1]+self.d)^2+9*(-coord[0]+self.a)^2*(-coord[0]+self.b)*(-coord[1]+self.c)*(-coord[1]+self.d)^2+(-coord[0]+self.a)^3*(-coord[1]+self.d)^3+3*(-coord[0]+self.a)^2*(-coord[0]+self.b)*(-coord[1]+self.d)^3

    def partialGxy2517(self,coord):

        return 3*(-coord[0]+self.a)^3*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2+9*(-coord[0]+self.a)^2*(-coord[0]+self.b)*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2+2*(-coord[0]+self.a)^3*(-coord[1]+self.c)*(-coord[1]+self.d)^3+6*(-coord[0]+self.a)^2*(-coord[0]+self.b)*(-coord[1]+self.c)*(-coord[1]+self.d)^3

    def partialGxy2518(self,coord):

        return 3*(-coord[0]+self.a)^3*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2+9*(-coord[0]+self.a)^2*(-coord[0]+self.b)*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2+3*(-coord[0]+self.a)^3*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3+9*(-coord[0]+self.a)^2*(-coord[0]+self.b)*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3

    def partialGxy2519(self,coord):

        return 3*(-coord[0]+self.a)^3*(-coord[1]+self.c)^4*(-coord[1]+self.d)^2+9*(-coord[0]+self.a)^2*(-coord[0]+self.b)*(-coord[1]+self.c)^4*(-coord[1]+self.d)^2+4*(-coord[0]+self.a)^3*(-coord[1]+self.c)^3*(-coord[1]+self.d)^3+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)*(-coord[1]+self.c)^3*(-coord[1]+self.d)^3

    def partialGxy2521(self,coord):

        return 4*(-coord[0]+self.a)^3*(-coord[1]+self.c)*(-coord[1]+self.d)^3+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)*(-coord[1]+self.c)*(-coord[1]+self.d)^3+(-coord[0]+self.a)^3*(-coord[1]+self.d)^4+3*(-coord[0]+self.a)^2*(-coord[0]+self.b)*(-coord[1]+self.d)^4

    def partialGxy2522(self,coord):

        return 4*(-coord[0]+self.a)^3*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3+2*(-coord[0]+self.a)^3*(-coord[1]+self.c)*(-coord[1]+self.d)^4+6*(-coord[0]+self.a)^2*(-coord[0]+self.b)*(-coord[1]+self.c)*(-coord[1]+self.d)^4

    def partialGxy2523(self,coord):

        return 4*(-coord[0]+self.a)^3*(-coord[1]+self.c)^3*(-coord[1]+self.d)^3+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)*(-coord[1]+self.c)^3*(-coord[1]+self.d)^3+3*(-coord[0]+self.a)^3*(-coord[1]+self.c)^2*(-coord[1]+self.d)^4+9*(-coord[0]+self.a)^2*(-coord[0]+self.b)*(-coord[1]+self.c)^2*(-coord[1]+self.d)^4

    def partialGxy2524(self,coord):

        return 4*(-coord[0]+self.a)^3*(-coord[1]+self.c)^4*(-coord[1]+self.d)^3+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)*(-coord[1]+self.c)^4*(-coord[1]+self.d)^3+4*(-coord[0]+self.a)^3*(-coord[1]+self.c)^3*(-coord[1]+self.d)^4+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)*(-coord[1]+self.c)^3*(-coord[1]+self.d)^4

    def partialGxy2537(self,coord):

        return (-coord[0]+self.a)^3*(2*(-coord[1]+self.c)^2+8*(-coord[1]+self.c)*(-coord[1]+self.d)+2*(-coord[1]+self.d)^2)+3*(-coord[0]+self.a)^2*(-coord[0]+self.b)*(2*(-coord[1]+self.c)^2+8*(-coord[1]+self.c)*(-coord[1]+self.d)+2*(-coord[1]+self.d)^2)

    def partialGxy2538(self,coord):

        return (-coord[0]+self.a)^3*(2*(-coord[1]+self.c)^3+12*(-coord[1]+self.c)^2*(-coord[1]+self.d)+6*(-coord[1]+self.c)*(-coord[1]+self.d)^2)+3*(-coord[0]+self.a)^2*(-coord[0]+self.b)*(2*(-coord[1]+self.c)^3+12*(-coord[1]+self.c)^2*(-coord[1]+self.d)+6*(-coord[1]+self.c)*(-coord[1]+self.d)^2)

    def partialGxy2539(self,coord):

        return (-coord[0]+self.a)^3*(2*(-coord[1]+self.c)^4+16*(-coord[1]+self.c)^3*(-coord[1]+self.d)+12*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2)+3*(-coord[0]+self.a)^2*(-coord[0]+self.b)*(2*(-coord[1]+self.c)^4+16*(-coord[1]+self.c)^3*(-coord[1]+self.d)+12*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2)

    def partialGxy2542(self,coord):

        return (-coord[0]+self.a)^3*(6*(-coord[1]+self.c)^2*(-coord[1]+self.d)+12*(-coord[1]+self.c)*(-coord[1]+self.d)^2+2*(-coord[1]+self.d)^3)+3*(-coord[0]+self.a)^2*(-coord[0]+self.b)*(6*(-coord[1]+self.c)^2*(-coord[1]+self.d)+12*(-coord[1]+self.c)*(-coord[1]+self.d)^2+2*(-coord[1]+self.d)^3)

    def partialGxy2543(self,coord):

        return (-coord[0]+self.a)^3*(6*(-coord[1]+self.c)^3*(-coord[1]+self.d)+18*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2+6*(-coord[1]+self.c)*(-coord[1]+self.d)^3)+3*(-coord[0]+self.a)^2*(-coord[0]+self.b)*(6*(-coord[1]+self.c)^3*(-coord[1]+self.d)+18*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2+6*(-coord[1]+self.c)*(-coord[1]+self.d)^3)

    def partialGxy2544(self,coord):

        return (-coord[0]+self.a)^3*(6*(-coord[1]+self.c)^4*(-coord[1]+self.d)+24*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2+12*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3)+3*(-coord[0]+self.a)^2*(-coord[0]+self.b)*(6*(-coord[1]+self.c)^4*(-coord[1]+self.d)+24*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2+12*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3)

    def partialGxy2547(self,coord):

        return (-coord[0]+self.a)^3*(12*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2+16*(-coord[1]+self.c)*(-coord[1]+self.d)^3+2*(-coord[1]+self.d)^4)+3*(-coord[0]+self.a)^2*(-coord[0]+self.b)*(12*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2+16*(-coord[1]+self.c)*(-coord[1]+self.d)^3+2*(-coord[1]+self.d)^4)

    def partialGxy2548(self,coord):

        return (-coord[0]+self.a)^3*(12*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2+24*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3+6*(-coord[1]+self.c)*(-coord[1]+self.d)^4)+3*(-coord[0]+self.a)^2*(-coord[0]+self.b)*(12*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2+24*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3+6*(-coord[1]+self.c)*(-coord[1]+self.d)^4)

    def partialGxy2549(self,coord):

        return (-coord[0]+self.a)^3*(12*(-coord[1]+self.c)^4*(-coord[1]+self.d)^2+32*(-coord[1]+self.c)^3*(-coord[1]+self.d)^3+12*(-coord[1]+self.c)^2*(-coord[1]+self.d)^4)+3*(-coord[0]+self.a)^2*(-coord[0]+self.b)*(12*(-coord[1]+self.c)^4*(-coord[1]+self.d)^2+32*(-coord[1]+self.c)^3*(-coord[1]+self.d)^3+12*(-coord[1]+self.c)^2*(-coord[1]+self.d)^4)

    def partialGxy2550(self,coord):

        return (-coord[0]+self.a)^4+4*(-coord[0]+self.a)^3*(-coord[0]+self.b)

    def partialGxy2551(self,coord):

        return (-coord[0]+self.a)^4*(-coord[1]+self.c)+4*(-coord[0]+self.a)^3*(-coord[0]+self.b)*(-coord[1]+self.c)

    def partialGxy2552(self,coord):

        return (-coord[0]+self.a)^4*(-coord[1]+self.c)^2+4*(-coord[0]+self.a)^3*(-coord[0]+self.b)*(-coord[1]+self.c)^2

    def partialGxy2553(self,coord):

        return (-coord[0]+self.a)^4*(-coord[1]+self.c)^3+4*(-coord[0]+self.a)^3*(-coord[0]+self.b)*(-coord[1]+self.c)^3

    def partialGxy2554(self,coord):

        return (-coord[0]+self.a)^4*(-coord[1]+self.c)^4+4*(-coord[0]+self.a)^3*(-coord[0]+self.b)*(-coord[1]+self.c)^4

    def partialGxy2555(self,coord):

        return (-coord[0]+self.a)^4*(-coord[1]+self.d)+4*(-coord[0]+self.a)^3*(-coord[0]+self.b)*(-coord[1]+self.d)

    def partialGxy2556(self,coord):

        return (-coord[0]+self.a)^4*(-coord[1]+self.c)*(-coord[1]+self.d)+4*(-coord[0]+self.a)^3*(-coord[0]+self.b)*(-coord[1]+self.c)*(-coord[1]+self.d)

    def partialGxy2557(self,coord):

        return (-coord[0]+self.a)^4*(-coord[1]+self.c)^2*(-coord[1]+self.d)+4*(-coord[0]+self.a)^3*(-coord[0]+self.b)*(-coord[1]+self.c)^2*(-coord[1]+self.d)

    def partialGxy2558(self,coord):

        return (-coord[0]+self.a)^4*(-coord[1]+self.c)^3*(-coord[1]+self.d)+4*(-coord[0]+self.a)^3*(-coord[0]+self.b)*(-coord[1]+self.c)^3*(-coord[1]+self.d)

    def partialGxy2559(self,coord):

        return (-coord[0]+self.a)^4*(-coord[1]+self.c)^4*(-coord[1]+self.d)+4*(-coord[0]+self.a)^3*(-coord[0]+self.b)*(-coord[1]+self.c)^4*(-coord[1]+self.d)

    def partialGxy2560(self,coord):

        return (-coord[0]+self.a)^4*(-coord[1]+self.d)^2+4*(-coord[0]+self.a)^3*(-coord[0]+self.b)*(-coord[1]+self.d)^2

    def partialGxy2561(self,coord):

        return (-coord[0]+self.a)^4*(-coord[1]+self.c)*(-coord[1]+self.d)^2+4*(-coord[0]+self.a)^3*(-coord[0]+self.b)*(-coord[1]+self.c)*(-coord[1]+self.d)^2

    def partialGxy2562(self,coord):

        return (-coord[0]+self.a)^4*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2+4*(-coord[0]+self.a)^3*(-coord[0]+self.b)*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2

    def partialGxy2563(self,coord):

        return (-coord[0]+self.a)^4*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2+4*(-coord[0]+self.a)^3*(-coord[0]+self.b)*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2

    def partialGxy2564(self,coord):

        return (-coord[0]+self.a)^4*(-coord[1]+self.c)^4*(-coord[1]+self.d)^2+4*(-coord[0]+self.a)^3*(-coord[0]+self.b)*(-coord[1]+self.c)^4*(-coord[1]+self.d)^2

    def partialGxy2565(self,coord):

        return (-coord[0]+self.a)^4*(-coord[1]+self.d)^3+4*(-coord[0]+self.a)^3*(-coord[0]+self.b)*(-coord[1]+self.d)^3

    def partialGxy2566(self,coord):

        return (-coord[0]+self.a)^4*(-coord[1]+self.c)*(-coord[1]+self.d)^3+4*(-coord[0]+self.a)^3*(-coord[0]+self.b)*(-coord[1]+self.c)*(-coord[1]+self.d)^3

    def partialGxy2567(self,coord):

        return (-coord[0]+self.a)^4*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3+4*(-coord[0]+self.a)^3*(-coord[0]+self.b)*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3

    def partialGxy2568(self,coord):

        return (-coord[0]+self.a)^4*(-coord[1]+self.c)^3*(-coord[1]+self.d)^3+4*(-coord[0]+self.a)^3*(-coord[0]+self.b)*(-coord[1]+self.c)^3*(-coord[1]+self.d)^3

    def partialGxy2569(self,coord):

        return (-coord[0]+self.a)^4*(-coord[1]+self.c)^4*(-coord[1]+self.d)^3+4*(-coord[0]+self.a)^3*(-coord[0]+self.b)*(-coord[1]+self.c)^4*(-coord[1]+self.d)^3

    def partialGxy2570(self,coord):

        return (-coord[0]+self.a)^4*(-coord[1]+self.d)^4+4*(-coord[0]+self.a)^3*(-coord[0]+self.b)*(-coord[1]+self.d)^4

    def partialGxy2571(self,coord):

        return (-coord[0]+self.a)^4*(-coord[1]+self.c)*(-coord[1]+self.d)^4+4*(-coord[0]+self.a)^3*(-coord[0]+self.b)*(-coord[1]+self.c)*(-coord[1]+self.d)^4

    def partialGxy2572(self,coord):

        return (-coord[0]+self.a)^4*(-coord[1]+self.c)^2*(-coord[1]+self.d)^4+4*(-coord[0]+self.a)^3*(-coord[0]+self.b)*(-coord[1]+self.c)^2*(-coord[1]+self.d)^4

    def partialGxy2573(self,coord):

        return (-coord[0]+self.a)^4*(-coord[1]+self.c)^3*(-coord[1]+self.d)^4+4*(-coord[0]+self.a)^3*(-coord[0]+self.b)*(-coord[1]+self.c)^3*(-coord[1]+self.d)^4

    def partialGxy2574(self,coord):

        return (-coord[0]+self.a)^4*(-coord[1]+self.c)^4*(-coord[1]+self.d)^4+4*(-coord[0]+self.a)^3*(-coord[0]+self.b)*(-coord[1]+self.c)^4*(-coord[1]+self.d)^4

    def partialGxy2581(self,coord):

        return (-coord[0]+self.a)^4*(-coord[1]+self.c)+4*(-coord[0]+self.a)^3*(-coord[0]+self.b)*(-coord[1]+self.c)+(-coord[0]+self.a)^4*(-coord[1]+self.d)+4*(-coord[0]+self.a)^3*(-coord[0]+self.b)*(-coord[1]+self.d)

    def partialGxy2582(self,coord):

        return (-coord[0]+self.a)^4*(-coord[1]+self.c)^2+4*(-coord[0]+self.a)^3*(-coord[0]+self.b)*(-coord[1]+self.c)^2+2*(-coord[0]+self.a)^4*(-coord[1]+self.c)*(-coord[1]+self.d)+8*(-coord[0]+self.a)^3*(-coord[0]+self.b)*(-coord[1]+self.c)*(-coord[1]+self.d)

    def partialGxy2583(self,coord):

        return (-coord[0]+self.a)^4*(-coord[1]+self.c)^3+4*(-coord[0]+self.a)^3*(-coord[0]+self.b)*(-coord[1]+self.c)^3+3*(-coord[0]+self.a)^4*(-coord[1]+self.c)^2*(-coord[1]+self.d)+12*(-coord[0]+self.a)^3*(-coord[0]+self.b)*(-coord[1]+self.c)^2*(-coord[1]+self.d)

    def partialGxy2584(self,coord):

        return (-coord[0]+self.a)^4*(-coord[1]+self.c)^4+4*(-coord[0]+self.a)^3*(-coord[0]+self.b)*(-coord[1]+self.c)^4+4*(-coord[0]+self.a)^4*(-coord[1]+self.c)^3*(-coord[1]+self.d)+16*(-coord[0]+self.a)^3*(-coord[0]+self.b)*(-coord[1]+self.c)^3*(-coord[1]+self.d)

    def partialGxy2586(self,coord):

        return 2*(-coord[0]+self.a)^4*(-coord[1]+self.c)*(-coord[1]+self.d)+8*(-coord[0]+self.a)^3*(-coord[0]+self.b)*(-coord[1]+self.c)*(-coord[1]+self.d)+(-coord[0]+self.a)^4*(-coord[1]+self.d)^2+4*(-coord[0]+self.a)^3*(-coord[0]+self.b)*(-coord[1]+self.d)^2

    def partialGxy2587(self,coord):

        return 2*(-coord[0]+self.a)^4*(-coord[1]+self.c)^2*(-coord[1]+self.d)+8*(-coord[0]+self.a)^3*(-coord[0]+self.b)*(-coord[1]+self.c)^2*(-coord[1]+self.d)+2*(-coord[0]+self.a)^4*(-coord[1]+self.c)*(-coord[1]+self.d)^2+8*(-coord[0]+self.a)^3*(-coord[0]+self.b)*(-coord[1]+self.c)*(-coord[1]+self.d)^2

    def partialGxy2588(self,coord):

        return 2*(-coord[0]+self.a)^4*(-coord[1]+self.c)^3*(-coord[1]+self.d)+8*(-coord[0]+self.a)^3*(-coord[0]+self.b)*(-coord[1]+self.c)^3*(-coord[1]+self.d)+3*(-coord[0]+self.a)^4*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2+12*(-coord[0]+self.a)^3*(-coord[0]+self.b)*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2

    def partialGxy2589(self,coord):

        return 2*(-coord[0]+self.a)^4*(-coord[1]+self.c)^4*(-coord[1]+self.d)+8*(-coord[0]+self.a)^3*(-coord[0]+self.b)*(-coord[1]+self.c)^4*(-coord[1]+self.d)+4*(-coord[0]+self.a)^4*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2+16*(-coord[0]+self.a)^3*(-coord[0]+self.b)*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2

    def partialGxy2591(self,coord):

        return 3*(-coord[0]+self.a)^4*(-coord[1]+self.c)*(-coord[1]+self.d)^2+12*(-coord[0]+self.a)^3*(-coord[0]+self.b)*(-coord[1]+self.c)*(-coord[1]+self.d)^2+(-coord[0]+self.a)^4*(-coord[1]+self.d)^3+4*(-coord[0]+self.a)^3*(-coord[0]+self.b)*(-coord[1]+self.d)^3

    def partialGxy2592(self,coord):

        return 3*(-coord[0]+self.a)^4*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2+12*(-coord[0]+self.a)^3*(-coord[0]+self.b)*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2+2*(-coord[0]+self.a)^4*(-coord[1]+self.c)*(-coord[1]+self.d)^3+8*(-coord[0]+self.a)^3*(-coord[0]+self.b)*(-coord[1]+self.c)*(-coord[1]+self.d)^3

    def partialGxy2593(self,coord):

        return 3*(-coord[0]+self.a)^4*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2+12*(-coord[0]+self.a)^3*(-coord[0]+self.b)*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2+3*(-coord[0]+self.a)^4*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3+12*(-coord[0]+self.a)^3*(-coord[0]+self.b)*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3

    def partialGxy2594(self,coord):

        return 3*(-coord[0]+self.a)^4*(-coord[1]+self.c)^4*(-coord[1]+self.d)^2+12*(-coord[0]+self.a)^3*(-coord[0]+self.b)*(-coord[1]+self.c)^4*(-coord[1]+self.d)^2+4*(-coord[0]+self.a)^4*(-coord[1]+self.c)^3*(-coord[1]+self.d)^3+16*(-coord[0]+self.a)^3*(-coord[0]+self.b)*(-coord[1]+self.c)^3*(-coord[1]+self.d)^3

    def partialGxy2596(self,coord):

        return 4*(-coord[0]+self.a)^4*(-coord[1]+self.c)*(-coord[1]+self.d)^3+16*(-coord[0]+self.a)^3*(-coord[0]+self.b)*(-coord[1]+self.c)*(-coord[1]+self.d)^3+(-coord[0]+self.a)^4*(-coord[1]+self.d)^4+4*(-coord[0]+self.a)^3*(-coord[0]+self.b)*(-coord[1]+self.d)^4

    def partialGxy2597(self,coord):

        return 4*(-coord[0]+self.a)^4*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3+16*(-coord[0]+self.a)^3*(-coord[0]+self.b)*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3+2*(-coord[0]+self.a)^4*(-coord[1]+self.c)*(-coord[1]+self.d)^4+8*(-coord[0]+self.a)^3*(-coord[0]+self.b)*(-coord[1]+self.c)*(-coord[1]+self.d)^4

    def partialGxy2598(self,coord):

        return 4*(-coord[0]+self.a)^4*(-coord[1]+self.c)^3*(-coord[1]+self.d)^3+16*(-coord[0]+self.a)^3*(-coord[0]+self.b)*(-coord[1]+self.c)^3*(-coord[1]+self.d)^3+3*(-coord[0]+self.a)^4*(-coord[1]+self.c)^2*(-coord[1]+self.d)^4+12*(-coord[0]+self.a)^3*(-coord[0]+self.b)*(-coord[1]+self.c)^2*(-coord[1]+self.d)^4

    def partialGxy2599(self,coord):

        return 4*(-coord[0]+self.a)^4*(-coord[1]+self.c)^4*(-coord[1]+self.d)^3+16*(-coord[0]+self.a)^3*(-coord[0]+self.b)*(-coord[1]+self.c)^4*(-coord[1]+self.d)^3+4*(-coord[0]+self.a)^4*(-coord[1]+self.c)^3*(-coord[1]+self.d)^4+16*(-coord[0]+self.a)^3*(-coord[0]+self.b)*(-coord[1]+self.c)^3*(-coord[1]+self.d)^4

    def partialGxy2612(self,coord):

        return (-coord[0]+self.a)^4*(2*(-coord[1]+self.c)^2+8*(-coord[1]+self.c)*(-coord[1]+self.d)+2*(-coord[1]+self.d)^2)+4*(-coord[0]+self.a)^3*(-coord[0]+self.b)*(2*(-coord[1]+self.c)^2+8*(-coord[1]+self.c)*(-coord[1]+self.d)+2*(-coord[1]+self.d)^2)

    def partialGxy2613(self,coord):

        return (-coord[0]+self.a)^4*(2*(-coord[1]+self.c)^3+12*(-coord[1]+self.c)^2*(-coord[1]+self.d)+6*(-coord[1]+self.c)*(-coord[1]+self.d)^2)+4*(-coord[0]+self.a)^3*(-coord[0]+self.b)*(2*(-coord[1]+self.c)^3+12*(-coord[1]+self.c)^2*(-coord[1]+self.d)+6*(-coord[1]+self.c)*(-coord[1]+self.d)^2)

    def partialGxy2614(self,coord):

        return (-coord[0]+self.a)^4*(2*(-coord[1]+self.c)^4+16*(-coord[1]+self.c)^3*(-coord[1]+self.d)+12*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2)+4*(-coord[0]+self.a)^3*(-coord[0]+self.b)*(2*(-coord[1]+self.c)^4+16*(-coord[1]+self.c)^3*(-coord[1]+self.d)+12*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2)

    def partialGxy2617(self,coord):

        return (-coord[0]+self.a)^4*(6*(-coord[1]+self.c)^2*(-coord[1]+self.d)+12*(-coord[1]+self.c)*(-coord[1]+self.d)^2+2*(-coord[1]+self.d)^3)+4*(-coord[0]+self.a)^3*(-coord[0]+self.b)*(6*(-coord[1]+self.c)^2*(-coord[1]+self.d)+12*(-coord[1]+self.c)*(-coord[1]+self.d)^2+2*(-coord[1]+self.d)^3)

    def partialGxy2618(self,coord):

        return (-coord[0]+self.a)^4*(6*(-coord[1]+self.c)^3*(-coord[1]+self.d)+18*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2+6*(-coord[1]+self.c)*(-coord[1]+self.d)^3)+4*(-coord[0]+self.a)^3*(-coord[0]+self.b)*(6*(-coord[1]+self.c)^3*(-coord[1]+self.d)+18*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2+6*(-coord[1]+self.c)*(-coord[1]+self.d)^3)

    def partialGxy2619(self,coord):

        return (-coord[0]+self.a)^4*(6*(-coord[1]+self.c)^4*(-coord[1]+self.d)+24*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2+12*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3)+4*(-coord[0]+self.a)^3*(-coord[0]+self.b)*(6*(-coord[1]+self.c)^4*(-coord[1]+self.d)+24*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2+12*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3)

    def partialGxy2622(self,coord):

        return (-coord[0]+self.a)^4*(12*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2+16*(-coord[1]+self.c)*(-coord[1]+self.d)^3+2*(-coord[1]+self.d)^4)+4*(-coord[0]+self.a)^3*(-coord[0]+self.b)*(12*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2+16*(-coord[1]+self.c)*(-coord[1]+self.d)^3+2*(-coord[1]+self.d)^4)

    def partialGxy2623(self,coord):

        return (-coord[0]+self.a)^4*(12*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2+24*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3+6*(-coord[1]+self.c)*(-coord[1]+self.d)^4)+4*(-coord[0]+self.a)^3*(-coord[0]+self.b)*(12*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2+24*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3+6*(-coord[1]+self.c)*(-coord[1]+self.d)^4)

    def partialGxy2624(self,coord):

        return (-coord[0]+self.a)^4*(12*(-coord[1]+self.c)^4*(-coord[1]+self.d)^2+32*(-coord[1]+self.c)^3*(-coord[1]+self.d)^3+12*(-coord[1]+self.c)^2*(-coord[1]+self.d)^4)+4*(-coord[0]+self.a)^3*(-coord[0]+self.b)*(12*(-coord[1]+self.c)^4*(-coord[1]+self.d)^2+32*(-coord[1]+self.c)^3*(-coord[1]+self.d)^3+12*(-coord[1]+self.c)^2*(-coord[1]+self.d)^4)

    def partialGxy2700(self,coord):

        return 2*(-coord[0]+self.a)*(-coord[0]+self.b)+(-coord[0]+self.b)^2

    def partialGxy2701(self,coord):

        return 2*(-coord[0]+self.a)*(-coord[0]+self.b)*(-coord[1]+self.c)+(-coord[0]+self.b)^2*(-coord[1]+self.c)

    def partialGxy2702(self,coord):

        return 2*(-coord[0]+self.a)*(-coord[0]+self.b)*(-coord[1]+self.c)^2+(-coord[0]+self.b)^2*(-coord[1]+self.c)^2

    def partialGxy2703(self,coord):

        return 2*(-coord[0]+self.a)*(-coord[0]+self.b)*(-coord[1]+self.c)^3+(-coord[0]+self.b)^2*(-coord[1]+self.c)^3

    def partialGxy2704(self,coord):

        return 2*(-coord[0]+self.a)*(-coord[0]+self.b)*(-coord[1]+self.c)^4+(-coord[0]+self.b)^2*(-coord[1]+self.c)^4

    def partialGxy2705(self,coord):

        return 2*(-coord[0]+self.a)*(-coord[0]+self.b)*(-coord[1]+self.d)+(-coord[0]+self.b)^2*(-coord[1]+self.d)

    def partialGxy2706(self,coord):

        return 2*(-coord[0]+self.a)*(-coord[0]+self.b)*(-coord[1]+self.c)*(-coord[1]+self.d)+(-coord[0]+self.b)^2*(-coord[1]+self.c)*(-coord[1]+self.d)

    def partialGxy2707(self,coord):

        return 2*(-coord[0]+self.a)*(-coord[0]+self.b)*(-coord[1]+self.c)^2*(-coord[1]+self.d)+(-coord[0]+self.b)^2*(-coord[1]+self.c)^2*(-coord[1]+self.d)

    def partialGxy2708(self,coord):

        return 2*(-coord[0]+self.a)*(-coord[0]+self.b)*(-coord[1]+self.c)^3*(-coord[1]+self.d)+(-coord[0]+self.b)^2*(-coord[1]+self.c)^3*(-coord[1]+self.d)

    def partialGxy2709(self,coord):

        return 2*(-coord[0]+self.a)*(-coord[0]+self.b)*(-coord[1]+self.c)^4*(-coord[1]+self.d)+(-coord[0]+self.b)^2*(-coord[1]+self.c)^4*(-coord[1]+self.d)

    def partialGxy2710(self,coord):

        return 2*(-coord[0]+self.a)*(-coord[0]+self.b)*(-coord[1]+self.d)^2+(-coord[0]+self.b)^2*(-coord[1]+self.d)^2

    def partialGxy2711(self,coord):

        return 2*(-coord[0]+self.a)*(-coord[0]+self.b)*(-coord[1]+self.c)*(-coord[1]+self.d)^2+(-coord[0]+self.b)^2*(-coord[1]+self.c)*(-coord[1]+self.d)^2

    def partialGxy2712(self,coord):

        return 2*(-coord[0]+self.a)*(-coord[0]+self.b)*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2+(-coord[0]+self.b)^2*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2

    def partialGxy2713(self,coord):

        return 2*(-coord[0]+self.a)*(-coord[0]+self.b)*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2+(-coord[0]+self.b)^2*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2

    def partialGxy2714(self,coord):

        return 2*(-coord[0]+self.a)*(-coord[0]+self.b)*(-coord[1]+self.c)^4*(-coord[1]+self.d)^2+(-coord[0]+self.b)^2*(-coord[1]+self.c)^4*(-coord[1]+self.d)^2

    def partialGxy2715(self,coord):

        return 2*(-coord[0]+self.a)*(-coord[0]+self.b)*(-coord[1]+self.d)^3+(-coord[0]+self.b)^2*(-coord[1]+self.d)^3

    def partialGxy2716(self,coord):

        return 2*(-coord[0]+self.a)*(-coord[0]+self.b)*(-coord[1]+self.c)*(-coord[1]+self.d)^3+(-coord[0]+self.b)^2*(-coord[1]+self.c)*(-coord[1]+self.d)^3

    def partialGxy2717(self,coord):

        return 2*(-coord[0]+self.a)*(-coord[0]+self.b)*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3+(-coord[0]+self.b)^2*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3

    def partialGxy2718(self,coord):

        return 2*(-coord[0]+self.a)*(-coord[0]+self.b)*(-coord[1]+self.c)^3*(-coord[1]+self.d)^3+(-coord[0]+self.b)^2*(-coord[1]+self.c)^3*(-coord[1]+self.d)^3

    def partialGxy2719(self,coord):

        return 2*(-coord[0]+self.a)*(-coord[0]+self.b)*(-coord[1]+self.c)^4*(-coord[1]+self.d)^3+(-coord[0]+self.b)^2*(-coord[1]+self.c)^4*(-coord[1]+self.d)^3

    def partialGxy2720(self,coord):

        return 2*(-coord[0]+self.a)*(-coord[0]+self.b)*(-coord[1]+self.d)^4+(-coord[0]+self.b)^2*(-coord[1]+self.d)^4

    def partialGxy2721(self,coord):

        return 2*(-coord[0]+self.a)*(-coord[0]+self.b)*(-coord[1]+self.c)*(-coord[1]+self.d)^4+(-coord[0]+self.b)^2*(-coord[1]+self.c)*(-coord[1]+self.d)^4

    def partialGxy2722(self,coord):

        return 2*(-coord[0]+self.a)*(-coord[0]+self.b)*(-coord[1]+self.c)^2*(-coord[1]+self.d)^4+(-coord[0]+self.b)^2*(-coord[1]+self.c)^2*(-coord[1]+self.d)^4

    def partialGxy2723(self,coord):

        return 2*(-coord[0]+self.a)*(-coord[0]+self.b)*(-coord[1]+self.c)^3*(-coord[1]+self.d)^4+(-coord[0]+self.b)^2*(-coord[1]+self.c)^3*(-coord[1]+self.d)^4

    def partialGxy2724(self,coord):

        return 2*(-coord[0]+self.a)*(-coord[0]+self.b)*(-coord[1]+self.c)^4*(-coord[1]+self.d)^4+(-coord[0]+self.b)^2*(-coord[1]+self.c)^4*(-coord[1]+self.d)^4

    def partialGxy2731(self,coord):

        return 2*(-coord[0]+self.a)*(-coord[0]+self.b)*(-coord[1]+self.c)+(-coord[0]+self.b)^2*(-coord[1]+self.c)+2*(-coord[0]+self.a)*(-coord[0]+self.b)*(-coord[1]+self.d)+(-coord[0]+self.b)^2*(-coord[1]+self.d)

    def partialGxy2732(self,coord):

        return 2*(-coord[0]+self.a)*(-coord[0]+self.b)*(-coord[1]+self.c)^2+(-coord[0]+self.b)^2*(-coord[1]+self.c)^2+4*(-coord[0]+self.a)*(-coord[0]+self.b)*(-coord[1]+self.c)*(-coord[1]+self.d)+2*(-coord[0]+self.b)^2*(-coord[1]+self.c)*(-coord[1]+self.d)

    def partialGxy2733(self,coord):

        return 2*(-coord[0]+self.a)*(-coord[0]+self.b)*(-coord[1]+self.c)^3+(-coord[0]+self.b)^2*(-coord[1]+self.c)^3+6*(-coord[0]+self.a)*(-coord[0]+self.b)*(-coord[1]+self.c)^2*(-coord[1]+self.d)+3*(-coord[0]+self.b)^2*(-coord[1]+self.c)^2*(-coord[1]+self.d)

    def partialGxy2734(self,coord):

        return 2*(-coord[0]+self.a)*(-coord[0]+self.b)*(-coord[1]+self.c)^4+(-coord[0]+self.b)^2*(-coord[1]+self.c)^4+8*(-coord[0]+self.a)*(-coord[0]+self.b)*(-coord[1]+self.c)^3*(-coord[1]+self.d)+4*(-coord[0]+self.b)^2*(-coord[1]+self.c)^3*(-coord[1]+self.d)

    def partialGxy2736(self,coord):

        return 4*(-coord[0]+self.a)*(-coord[0]+self.b)*(-coord[1]+self.c)*(-coord[1]+self.d)+2*(-coord[0]+self.b)^2*(-coord[1]+self.c)*(-coord[1]+self.d)+2*(-coord[0]+self.a)*(-coord[0]+self.b)*(-coord[1]+self.d)^2+(-coord[0]+self.b)^2*(-coord[1]+self.d)^2

    def partialGxy2737(self,coord):

        return 4*(-coord[0]+self.a)*(-coord[0]+self.b)*(-coord[1]+self.c)^2*(-coord[1]+self.d)+2*(-coord[0]+self.b)^2*(-coord[1]+self.c)^2*(-coord[1]+self.d)+4*(-coord[0]+self.a)*(-coord[0]+self.b)*(-coord[1]+self.c)*(-coord[1]+self.d)^2+2*(-coord[0]+self.b)^2*(-coord[1]+self.c)*(-coord[1]+self.d)^2

    def partialGxy2738(self,coord):

        return 4*(-coord[0]+self.a)*(-coord[0]+self.b)*(-coord[1]+self.c)^3*(-coord[1]+self.d)+2*(-coord[0]+self.b)^2*(-coord[1]+self.c)^3*(-coord[1]+self.d)+6*(-coord[0]+self.a)*(-coord[0]+self.b)*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2+3*(-coord[0]+self.b)^2*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2

    def partialGxy2739(self,coord):

        return 4*(-coord[0]+self.a)*(-coord[0]+self.b)*(-coord[1]+self.c)^4*(-coord[1]+self.d)+2*(-coord[0]+self.b)^2*(-coord[1]+self.c)^4*(-coord[1]+self.d)+8*(-coord[0]+self.a)*(-coord[0]+self.b)*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2+4*(-coord[0]+self.b)^2*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2

    def partialGxy2741(self,coord):

        return 6*(-coord[0]+self.a)*(-coord[0]+self.b)*(-coord[1]+self.c)*(-coord[1]+self.d)^2+3*(-coord[0]+self.b)^2*(-coord[1]+self.c)*(-coord[1]+self.d)^2+2*(-coord[0]+self.a)*(-coord[0]+self.b)*(-coord[1]+self.d)^3+(-coord[0]+self.b)^2*(-coord[1]+self.d)^3

    def partialGxy2742(self,coord):

        return 6*(-coord[0]+self.a)*(-coord[0]+self.b)*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2+3*(-coord[0]+self.b)^2*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2+4*(-coord[0]+self.a)*(-coord[0]+self.b)*(-coord[1]+self.c)*(-coord[1]+self.d)^3+2*(-coord[0]+self.b)^2*(-coord[1]+self.c)*(-coord[1]+self.d)^3

    def partialGxy2743(self,coord):

        return 6*(-coord[0]+self.a)*(-coord[0]+self.b)*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2+3*(-coord[0]+self.b)^2*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2+6*(-coord[0]+self.a)*(-coord[0]+self.b)*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3+3*(-coord[0]+self.b)^2*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3

    def partialGxy2744(self,coord):

        return 6*(-coord[0]+self.a)*(-coord[0]+self.b)*(-coord[1]+self.c)^4*(-coord[1]+self.d)^2+3*(-coord[0]+self.b)^2*(-coord[1]+self.c)^4*(-coord[1]+self.d)^2+8*(-coord[0]+self.a)*(-coord[0]+self.b)*(-coord[1]+self.c)^3*(-coord[1]+self.d)^3+4*(-coord[0]+self.b)^2*(-coord[1]+self.c)^3*(-coord[1]+self.d)^3

    def partialGxy2746(self,coord):

        return 8*(-coord[0]+self.a)*(-coord[0]+self.b)*(-coord[1]+self.c)*(-coord[1]+self.d)^3+4*(-coord[0]+self.b)^2*(-coord[1]+self.c)*(-coord[1]+self.d)^3+2*(-coord[0]+self.a)*(-coord[0]+self.b)*(-coord[1]+self.d)^4+(-coord[0]+self.b)^2*(-coord[1]+self.d)^4

    def partialGxy2747(self,coord):

        return 8*(-coord[0]+self.a)*(-coord[0]+self.b)*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3+4*(-coord[0]+self.b)^2*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3+4*(-coord[0]+self.a)*(-coord[0]+self.b)*(-coord[1]+self.c)*(-coord[1]+self.d)^4+2*(-coord[0]+self.b)^2*(-coord[1]+self.c)*(-coord[1]+self.d)^4

    def partialGxy2748(self,coord):

        return 8*(-coord[0]+self.a)*(-coord[0]+self.b)*(-coord[1]+self.c)^3*(-coord[1]+self.d)^3+4*(-coord[0]+self.b)^2*(-coord[1]+self.c)^3*(-coord[1]+self.d)^3+6*(-coord[0]+self.a)*(-coord[0]+self.b)*(-coord[1]+self.c)^2*(-coord[1]+self.d)^4+3*(-coord[0]+self.b)^2*(-coord[1]+self.c)^2*(-coord[1]+self.d)^4

    def partialGxy2749(self,coord):

        return 8*(-coord[0]+self.a)*(-coord[0]+self.b)*(-coord[1]+self.c)^4*(-coord[1]+self.d)^3+4*(-coord[0]+self.b)^2*(-coord[1]+self.c)^4*(-coord[1]+self.d)^3+8*(-coord[0]+self.a)*(-coord[0]+self.b)*(-coord[1]+self.c)^3*(-coord[1]+self.d)^4+4*(-coord[0]+self.b)^2*(-coord[1]+self.c)^3*(-coord[1]+self.d)^4

    def partialGxy2762(self,coord):

        return 2*(-coord[0]+self.a)*(-coord[0]+self.b)*(2*(-coord[1]+self.c)^2+8*(-coord[1]+self.c)*(-coord[1]+self.d)+2*(-coord[1]+self.d)^2)+(-coord[0]+self.b)^2*(2*(-coord[1]+self.c)^2+8*(-coord[1]+self.c)*(-coord[1]+self.d)+2*(-coord[1]+self.d)^2)

    def partialGxy2763(self,coord):

        return 2*(-coord[0]+self.a)*(-coord[0]+self.b)*(2*(-coord[1]+self.c)^3+12*(-coord[1]+self.c)^2*(-coord[1]+self.d)+6*(-coord[1]+self.c)*(-coord[1]+self.d)^2)+(-coord[0]+self.b)^2*(2*(-coord[1]+self.c)^3+12*(-coord[1]+self.c)^2*(-coord[1]+self.d)+6*(-coord[1]+self.c)*(-coord[1]+self.d)^2)

    def partialGxy2764(self,coord):

        return 2*(-coord[0]+self.a)*(-coord[0]+self.b)*(2*(-coord[1]+self.c)^4+16*(-coord[1]+self.c)^3*(-coord[1]+self.d)+12*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2)+(-coord[0]+self.b)^2*(2*(-coord[1]+self.c)^4+16*(-coord[1]+self.c)^3*(-coord[1]+self.d)+12*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2)

    def partialGxy2767(self,coord):

        return 2*(-coord[0]+self.a)*(-coord[0]+self.b)*(6*(-coord[1]+self.c)^2*(-coord[1]+self.d)+12*(-coord[1]+self.c)*(-coord[1]+self.d)^2+2*(-coord[1]+self.d)^3)+(-coord[0]+self.b)^2*(6*(-coord[1]+self.c)^2*(-coord[1]+self.d)+12*(-coord[1]+self.c)*(-coord[1]+self.d)^2+2*(-coord[1]+self.d)^3)

    def partialGxy2768(self,coord):

        return 2*(-coord[0]+self.a)*(-coord[0]+self.b)*(6*(-coord[1]+self.c)^3*(-coord[1]+self.d)+18*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2+6*(-coord[1]+self.c)*(-coord[1]+self.d)^3)+(-coord[0]+self.b)^2*(6*(-coord[1]+self.c)^3*(-coord[1]+self.d)+18*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2+6*(-coord[1]+self.c)*(-coord[1]+self.d)^3)

    def partialGxy2769(self,coord):

        return 2*(-coord[0]+self.a)*(-coord[0]+self.b)*(6*(-coord[1]+self.c)^4*(-coord[1]+self.d)+24*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2+12*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3)+(-coord[0]+self.b)^2*(6*(-coord[1]+self.c)^4*(-coord[1]+self.d)+24*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2+12*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3)

    def partialGxy2772(self,coord):

        return 2*(-coord[0]+self.a)*(-coord[0]+self.b)*(12*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2+16*(-coord[1]+self.c)*(-coord[1]+self.d)^3+2*(-coord[1]+self.d)^4)+(-coord[0]+self.b)^2*(12*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2+16*(-coord[1]+self.c)*(-coord[1]+self.d)^3+2*(-coord[1]+self.d)^4)

    def partialGxy2773(self,coord):

        return 2*(-coord[0]+self.a)*(-coord[0]+self.b)*(12*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2+24*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3+6*(-coord[1]+self.c)*(-coord[1]+self.d)^4)+(-coord[0]+self.b)^2*(12*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2+24*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3+6*(-coord[1]+self.c)*(-coord[1]+self.d)^4)

    def partialGxy2774(self,coord):

        return 2*(-coord[0]+self.a)*(-coord[0]+self.b)*(12*(-coord[1]+self.c)^4*(-coord[1]+self.d)^2+32*(-coord[1]+self.c)^3*(-coord[1]+self.d)^3+12*(-coord[1]+self.c)^2*(-coord[1]+self.d)^4)+(-coord[0]+self.b)^2*(12*(-coord[1]+self.c)^4*(-coord[1]+self.d)^2+32*(-coord[1]+self.c)^3*(-coord[1]+self.d)^3+12*(-coord[1]+self.c)^2*(-coord[1]+self.d)^4)

    def partialGxy2775(self,coord):

        return 2*(-coord[0]+self.a)^2*(-coord[0]+self.b)+2*(-coord[0]+self.a)*(-coord[0]+self.b)^2

    def partialGxy2776(self,coord):

        return 2*(-coord[0]+self.a)^2*(-coord[0]+self.b)*(-coord[1]+self.c)+2*(-coord[0]+self.a)*(-coord[0]+self.b)^2*(-coord[1]+self.c)

    def partialGxy2777(self,coord):

        return 2*(-coord[0]+self.a)^2*(-coord[0]+self.b)*(-coord[1]+self.c)^2+2*(-coord[0]+self.a)*(-coord[0]+self.b)^2*(-coord[1]+self.c)^2

    def partialGxy2778(self,coord):

        return 2*(-coord[0]+self.a)^2*(-coord[0]+self.b)*(-coord[1]+self.c)^3+2*(-coord[0]+self.a)*(-coord[0]+self.b)^2*(-coord[1]+self.c)^3

    def partialGxy2779(self,coord):

        return 2*(-coord[0]+self.a)^2*(-coord[0]+self.b)*(-coord[1]+self.c)^4+2*(-coord[0]+self.a)*(-coord[0]+self.b)^2*(-coord[1]+self.c)^4

    def partialGxy2780(self,coord):

        return 2*(-coord[0]+self.a)^2*(-coord[0]+self.b)*(-coord[1]+self.d)+2*(-coord[0]+self.a)*(-coord[0]+self.b)^2*(-coord[1]+self.d)

    def partialGxy2781(self,coord):

        return 2*(-coord[0]+self.a)^2*(-coord[0]+self.b)*(-coord[1]+self.c)*(-coord[1]+self.d)+2*(-coord[0]+self.a)*(-coord[0]+self.b)^2*(-coord[1]+self.c)*(-coord[1]+self.d)

    def partialGxy2782(self,coord):

        return 2*(-coord[0]+self.a)^2*(-coord[0]+self.b)*(-coord[1]+self.c)^2*(-coord[1]+self.d)+2*(-coord[0]+self.a)*(-coord[0]+self.b)^2*(-coord[1]+self.c)^2*(-coord[1]+self.d)

    def partialGxy2783(self,coord):

        return 2*(-coord[0]+self.a)^2*(-coord[0]+self.b)*(-coord[1]+self.c)^3*(-coord[1]+self.d)+2*(-coord[0]+self.a)*(-coord[0]+self.b)^2*(-coord[1]+self.c)^3*(-coord[1]+self.d)

    def partialGxy2784(self,coord):

        return 2*(-coord[0]+self.a)^2*(-coord[0]+self.b)*(-coord[1]+self.c)^4*(-coord[1]+self.d)+2*(-coord[0]+self.a)*(-coord[0]+self.b)^2*(-coord[1]+self.c)^4*(-coord[1]+self.d)

    def partialGxy2785(self,coord):

        return 2*(-coord[0]+self.a)^2*(-coord[0]+self.b)*(-coord[1]+self.d)^2+2*(-coord[0]+self.a)*(-coord[0]+self.b)^2*(-coord[1]+self.d)^2

    def partialGxy2786(self,coord):

        return 2*(-coord[0]+self.a)^2*(-coord[0]+self.b)*(-coord[1]+self.c)*(-coord[1]+self.d)^2+2*(-coord[0]+self.a)*(-coord[0]+self.b)^2*(-coord[1]+self.c)*(-coord[1]+self.d)^2

    def partialGxy2787(self,coord):

        return 2*(-coord[0]+self.a)^2*(-coord[0]+self.b)*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2+2*(-coord[0]+self.a)*(-coord[0]+self.b)^2*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2

    def partialGxy2788(self,coord):

        return 2*(-coord[0]+self.a)^2*(-coord[0]+self.b)*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2+2*(-coord[0]+self.a)*(-coord[0]+self.b)^2*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2

    def partialGxy2789(self,coord):

        return 2*(-coord[0]+self.a)^2*(-coord[0]+self.b)*(-coord[1]+self.c)^4*(-coord[1]+self.d)^2+2*(-coord[0]+self.a)*(-coord[0]+self.b)^2*(-coord[1]+self.c)^4*(-coord[1]+self.d)^2

    def partialGxy2790(self,coord):

        return 2*(-coord[0]+self.a)^2*(-coord[0]+self.b)*(-coord[1]+self.d)^3+2*(-coord[0]+self.a)*(-coord[0]+self.b)^2*(-coord[1]+self.d)^3

    def partialGxy2791(self,coord):

        return 2*(-coord[0]+self.a)^2*(-coord[0]+self.b)*(-coord[1]+self.c)*(-coord[1]+self.d)^3+2*(-coord[0]+self.a)*(-coord[0]+self.b)^2*(-coord[1]+self.c)*(-coord[1]+self.d)^3

    def partialGxy2792(self,coord):

        return 2*(-coord[0]+self.a)^2*(-coord[0]+self.b)*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3+2*(-coord[0]+self.a)*(-coord[0]+self.b)^2*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3

    def partialGxy2793(self,coord):

        return 2*(-coord[0]+self.a)^2*(-coord[0]+self.b)*(-coord[1]+self.c)^3*(-coord[1]+self.d)^3+2*(-coord[0]+self.a)*(-coord[0]+self.b)^2*(-coord[1]+self.c)^3*(-coord[1]+self.d)^3

    def partialGxy2794(self,coord):

        return 2*(-coord[0]+self.a)^2*(-coord[0]+self.b)*(-coord[1]+self.c)^4*(-coord[1]+self.d)^3+2*(-coord[0]+self.a)*(-coord[0]+self.b)^2*(-coord[1]+self.c)^4*(-coord[1]+self.d)^3

    def partialGxy2795(self,coord):

        return 2*(-coord[0]+self.a)^2*(-coord[0]+self.b)*(-coord[1]+self.d)^4+2*(-coord[0]+self.a)*(-coord[0]+self.b)^2*(-coord[1]+self.d)^4

    def partialGxy2796(self,coord):

        return 2*(-coord[0]+self.a)^2*(-coord[0]+self.b)*(-coord[1]+self.c)*(-coord[1]+self.d)^4+2*(-coord[0]+self.a)*(-coord[0]+self.b)^2*(-coord[1]+self.c)*(-coord[1]+self.d)^4

    def partialGxy2797(self,coord):

        return 2*(-coord[0]+self.a)^2*(-coord[0]+self.b)*(-coord[1]+self.c)^2*(-coord[1]+self.d)^4+2*(-coord[0]+self.a)*(-coord[0]+self.b)^2*(-coord[1]+self.c)^2*(-coord[1]+self.d)^4

    def partialGxy2798(self,coord):

        return 2*(-coord[0]+self.a)^2*(-coord[0]+self.b)*(-coord[1]+self.c)^3*(-coord[1]+self.d)^4+2*(-coord[0]+self.a)*(-coord[0]+self.b)^2*(-coord[1]+self.c)^3*(-coord[1]+self.d)^4

    def partialGxy2799(self,coord):

        return 2*(-coord[0]+self.a)^2*(-coord[0]+self.b)*(-coord[1]+self.c)^4*(-coord[1]+self.d)^4+2*(-coord[0]+self.a)*(-coord[0]+self.b)^2*(-coord[1]+self.c)^4*(-coord[1]+self.d)^4

    def partialGxy2806(self,coord):

        return 2*(-coord[0]+self.a)^2*(-coord[0]+self.b)*(-coord[1]+self.c)+2*(-coord[0]+self.a)*(-coord[0]+self.b)^2*(-coord[1]+self.c)+2*(-coord[0]+self.a)^2*(-coord[0]+self.b)*(-coord[1]+self.d)+2*(-coord[0]+self.a)*(-coord[0]+self.b)^2*(-coord[1]+self.d)

    def partialGxy2807(self,coord):

        return 2*(-coord[0]+self.a)^2*(-coord[0]+self.b)*(-coord[1]+self.c)^2+2*(-coord[0]+self.a)*(-coord[0]+self.b)^2*(-coord[1]+self.c)^2+4*(-coord[0]+self.a)^2*(-coord[0]+self.b)*(-coord[1]+self.c)*(-coord[1]+self.d)+4*(-coord[0]+self.a)*(-coord[0]+self.b)^2*(-coord[1]+self.c)*(-coord[1]+self.d)

    def partialGxy2808(self,coord):

        return 2*(-coord[0]+self.a)^2*(-coord[0]+self.b)*(-coord[1]+self.c)^3+2*(-coord[0]+self.a)*(-coord[0]+self.b)^2*(-coord[1]+self.c)^3+6*(-coord[0]+self.a)^2*(-coord[0]+self.b)*(-coord[1]+self.c)^2*(-coord[1]+self.d)+6*(-coord[0]+self.a)*(-coord[0]+self.b)^2*(-coord[1]+self.c)^2*(-coord[1]+self.d)

    def partialGxy2809(self,coord):

        return 2*(-coord[0]+self.a)^2*(-coord[0]+self.b)*(-coord[1]+self.c)^4+2*(-coord[0]+self.a)*(-coord[0]+self.b)^2*(-coord[1]+self.c)^4+8*(-coord[0]+self.a)^2*(-coord[0]+self.b)*(-coord[1]+self.c)^3*(-coord[1]+self.d)+8*(-coord[0]+self.a)*(-coord[0]+self.b)^2*(-coord[1]+self.c)^3*(-coord[1]+self.d)

    def partialGxy2811(self,coord):

        return 4*(-coord[0]+self.a)^2*(-coord[0]+self.b)*(-coord[1]+self.c)*(-coord[1]+self.d)+4*(-coord[0]+self.a)*(-coord[0]+self.b)^2*(-coord[1]+self.c)*(-coord[1]+self.d)+2*(-coord[0]+self.a)^2*(-coord[0]+self.b)*(-coord[1]+self.d)^2+2*(-coord[0]+self.a)*(-coord[0]+self.b)^2*(-coord[1]+self.d)^2

    def partialGxy2812(self,coord):

        return 4*(-coord[0]+self.a)^2*(-coord[0]+self.b)*(-coord[1]+self.c)^2*(-coord[1]+self.d)+4*(-coord[0]+self.a)*(-coord[0]+self.b)^2*(-coord[1]+self.c)^2*(-coord[1]+self.d)+4*(-coord[0]+self.a)^2*(-coord[0]+self.b)*(-coord[1]+self.c)*(-coord[1]+self.d)^2+4*(-coord[0]+self.a)*(-coord[0]+self.b)^2*(-coord[1]+self.c)*(-coord[1]+self.d)^2

    def partialGxy2813(self,coord):

        return 4*(-coord[0]+self.a)^2*(-coord[0]+self.b)*(-coord[1]+self.c)^3*(-coord[1]+self.d)+4*(-coord[0]+self.a)*(-coord[0]+self.b)^2*(-coord[1]+self.c)^3*(-coord[1]+self.d)+6*(-coord[0]+self.a)^2*(-coord[0]+self.b)*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2+6*(-coord[0]+self.a)*(-coord[0]+self.b)^2*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2

    def partialGxy2814(self,coord):

        return 4*(-coord[0]+self.a)^2*(-coord[0]+self.b)*(-coord[1]+self.c)^4*(-coord[1]+self.d)+4*(-coord[0]+self.a)*(-coord[0]+self.b)^2*(-coord[1]+self.c)^4*(-coord[1]+self.d)+8*(-coord[0]+self.a)^2*(-coord[0]+self.b)*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2+8*(-coord[0]+self.a)*(-coord[0]+self.b)^2*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2

    def partialGxy2816(self,coord):

        return 6*(-coord[0]+self.a)^2*(-coord[0]+self.b)*(-coord[1]+self.c)*(-coord[1]+self.d)^2+6*(-coord[0]+self.a)*(-coord[0]+self.b)^2*(-coord[1]+self.c)*(-coord[1]+self.d)^2+2*(-coord[0]+self.a)^2*(-coord[0]+self.b)*(-coord[1]+self.d)^3+2*(-coord[0]+self.a)*(-coord[0]+self.b)^2*(-coord[1]+self.d)^3

    def partialGxy2817(self,coord):

        return 6*(-coord[0]+self.a)^2*(-coord[0]+self.b)*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2+6*(-coord[0]+self.a)*(-coord[0]+self.b)^2*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2+4*(-coord[0]+self.a)^2*(-coord[0]+self.b)*(-coord[1]+self.c)*(-coord[1]+self.d)^3+4*(-coord[0]+self.a)*(-coord[0]+self.b)^2*(-coord[1]+self.c)*(-coord[1]+self.d)^3

    def partialGxy2818(self,coord):

        return 6*(-coord[0]+self.a)^2*(-coord[0]+self.b)*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2+6*(-coord[0]+self.a)*(-coord[0]+self.b)^2*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2+6*(-coord[0]+self.a)^2*(-coord[0]+self.b)*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3+6*(-coord[0]+self.a)*(-coord[0]+self.b)^2*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3

    def partialGxy2819(self,coord):

        return 6*(-coord[0]+self.a)^2*(-coord[0]+self.b)*(-coord[1]+self.c)^4*(-coord[1]+self.d)^2+6*(-coord[0]+self.a)*(-coord[0]+self.b)^2*(-coord[1]+self.c)^4*(-coord[1]+self.d)^2+8*(-coord[0]+self.a)^2*(-coord[0]+self.b)*(-coord[1]+self.c)^3*(-coord[1]+self.d)^3+8*(-coord[0]+self.a)*(-coord[0]+self.b)^2*(-coord[1]+self.c)^3*(-coord[1]+self.d)^3

    def partialGxy2821(self,coord):

        return 8*(-coord[0]+self.a)^2*(-coord[0]+self.b)*(-coord[1]+self.c)*(-coord[1]+self.d)^3+8*(-coord[0]+self.a)*(-coord[0]+self.b)^2*(-coord[1]+self.c)*(-coord[1]+self.d)^3+2*(-coord[0]+self.a)^2*(-coord[0]+self.b)*(-coord[1]+self.d)^4+2*(-coord[0]+self.a)*(-coord[0]+self.b)^2*(-coord[1]+self.d)^4

    def partialGxy2822(self,coord):

        return 8*(-coord[0]+self.a)^2*(-coord[0]+self.b)*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3+8*(-coord[0]+self.a)*(-coord[0]+self.b)^2*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3+4*(-coord[0]+self.a)^2*(-coord[0]+self.b)*(-coord[1]+self.c)*(-coord[1]+self.d)^4+4*(-coord[0]+self.a)*(-coord[0]+self.b)^2*(-coord[1]+self.c)*(-coord[1]+self.d)^4

    def partialGxy2823(self,coord):

        return 8*(-coord[0]+self.a)^2*(-coord[0]+self.b)*(-coord[1]+self.c)^3*(-coord[1]+self.d)^3+8*(-coord[0]+self.a)*(-coord[0]+self.b)^2*(-coord[1]+self.c)^3*(-coord[1]+self.d)^3+6*(-coord[0]+self.a)^2*(-coord[0]+self.b)*(-coord[1]+self.c)^2*(-coord[1]+self.d)^4+6*(-coord[0]+self.a)*(-coord[0]+self.b)^2*(-coord[1]+self.c)^2*(-coord[1]+self.d)^4

    def partialGxy2824(self,coord):

        return 8*(-coord[0]+self.a)^2*(-coord[0]+self.b)*(-coord[1]+self.c)^4*(-coord[1]+self.d)^3+8*(-coord[0]+self.a)*(-coord[0]+self.b)^2*(-coord[1]+self.c)^4*(-coord[1]+self.d)^3+8*(-coord[0]+self.a)^2*(-coord[0]+self.b)*(-coord[1]+self.c)^3*(-coord[1]+self.d)^4+8*(-coord[0]+self.a)*(-coord[0]+self.b)^2*(-coord[1]+self.c)^3*(-coord[1]+self.d)^4

    def partialGxy2837(self,coord):

        return 2*(-coord[0]+self.a)^2*(-coord[0]+self.b)*(2*(-coord[1]+self.c)^2+8*(-coord[1]+self.c)*(-coord[1]+self.d)+2*(-coord[1]+self.d)^2)+2*(-coord[0]+self.a)*(-coord[0]+self.b)^2*(2*(-coord[1]+self.c)^2+8*(-coord[1]+self.c)*(-coord[1]+self.d)+2*(-coord[1]+self.d)^2)

    def partialGxy2838(self,coord):

        return 2*(-coord[0]+self.a)^2*(-coord[0]+self.b)*(2*(-coord[1]+self.c)^3+12*(-coord[1]+self.c)^2*(-coord[1]+self.d)+6*(-coord[1]+self.c)*(-coord[1]+self.d)^2)+2*(-coord[0]+self.a)*(-coord[0]+self.b)^2*(2*(-coord[1]+self.c)^3+12*(-coord[1]+self.c)^2*(-coord[1]+self.d)+6*(-coord[1]+self.c)*(-coord[1]+self.d)^2)

    def partialGxy2839(self,coord):

        return 2*(-coord[0]+self.a)^2*(-coord[0]+self.b)*(2*(-coord[1]+self.c)^4+16*(-coord[1]+self.c)^3*(-coord[1]+self.d)+12*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2)+2*(-coord[0]+self.a)*(-coord[0]+self.b)^2*(2*(-coord[1]+self.c)^4+16*(-coord[1]+self.c)^3*(-coord[1]+self.d)+12*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2)

    def partialGxy2842(self,coord):

        return 2*(-coord[0]+self.a)^2*(-coord[0]+self.b)*(6*(-coord[1]+self.c)^2*(-coord[1]+self.d)+12*(-coord[1]+self.c)*(-coord[1]+self.d)^2+2*(-coord[1]+self.d)^3)+2*(-coord[0]+self.a)*(-coord[0]+self.b)^2*(6*(-coord[1]+self.c)^2*(-coord[1]+self.d)+12*(-coord[1]+self.c)*(-coord[1]+self.d)^2+2*(-coord[1]+self.d)^3)

    def partialGxy2843(self,coord):

        return 2*(-coord[0]+self.a)^2*(-coord[0]+self.b)*(6*(-coord[1]+self.c)^3*(-coord[1]+self.d)+18*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2+6*(-coord[1]+self.c)*(-coord[1]+self.d)^3)+2*(-coord[0]+self.a)*(-coord[0]+self.b)^2*(6*(-coord[1]+self.c)^3*(-coord[1]+self.d)+18*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2+6*(-coord[1]+self.c)*(-coord[1]+self.d)^3)

    def partialGxy2844(self,coord):

        return 2*(-coord[0]+self.a)^2*(-coord[0]+self.b)*(6*(-coord[1]+self.c)^4*(-coord[1]+self.d)+24*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2+12*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3)+2*(-coord[0]+self.a)*(-coord[0]+self.b)^2*(6*(-coord[1]+self.c)^4*(-coord[1]+self.d)+24*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2+12*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3)

    def partialGxy2847(self,coord):

        return 2*(-coord[0]+self.a)^2*(-coord[0]+self.b)*(12*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2+16*(-coord[1]+self.c)*(-coord[1]+self.d)^3+2*(-coord[1]+self.d)^4)+2*(-coord[0]+self.a)*(-coord[0]+self.b)^2*(12*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2+16*(-coord[1]+self.c)*(-coord[1]+self.d)^3+2*(-coord[1]+self.d)^4)

    def partialGxy2848(self,coord):

        return 2*(-coord[0]+self.a)^2*(-coord[0]+self.b)*(12*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2+24*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3+6*(-coord[1]+self.c)*(-coord[1]+self.d)^4)+2*(-coord[0]+self.a)*(-coord[0]+self.b)^2*(12*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2+24*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3+6*(-coord[1]+self.c)*(-coord[1]+self.d)^4)

    def partialGxy2849(self,coord):

        return 2*(-coord[0]+self.a)^2*(-coord[0]+self.b)*(12*(-coord[1]+self.c)^4*(-coord[1]+self.d)^2+32*(-coord[1]+self.c)^3*(-coord[1]+self.d)^3+12*(-coord[1]+self.c)^2*(-coord[1]+self.d)^4)+2*(-coord[0]+self.a)*(-coord[0]+self.b)^2*(12*(-coord[1]+self.c)^4*(-coord[1]+self.d)^2+32*(-coord[1]+self.c)^3*(-coord[1]+self.d)^3+12*(-coord[1]+self.c)^2*(-coord[1]+self.d)^4)

    def partialGxy2850(self,coord):

        return 2*(-coord[0]+self.a)^3*(-coord[0]+self.b)+3*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2

    def partialGxy2851(self,coord):

        return 2*(-coord[0]+self.a)^3*(-coord[0]+self.b)*(-coord[1]+self.c)+3*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2*(-coord[1]+self.c)

    def partialGxy2852(self,coord):

        return 2*(-coord[0]+self.a)^3*(-coord[0]+self.b)*(-coord[1]+self.c)^2+3*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2*(-coord[1]+self.c)^2

    def partialGxy2853(self,coord):

        return 2*(-coord[0]+self.a)^3*(-coord[0]+self.b)*(-coord[1]+self.c)^3+3*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2*(-coord[1]+self.c)^3

    def partialGxy2854(self,coord):

        return 2*(-coord[0]+self.a)^3*(-coord[0]+self.b)*(-coord[1]+self.c)^4+3*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2*(-coord[1]+self.c)^4

    def partialGxy2855(self,coord):

        return 2*(-coord[0]+self.a)^3*(-coord[0]+self.b)*(-coord[1]+self.d)+3*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2*(-coord[1]+self.d)

    def partialGxy2856(self,coord):

        return 2*(-coord[0]+self.a)^3*(-coord[0]+self.b)*(-coord[1]+self.c)*(-coord[1]+self.d)+3*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2*(-coord[1]+self.c)*(-coord[1]+self.d)

    def partialGxy2857(self,coord):

        return 2*(-coord[0]+self.a)^3*(-coord[0]+self.b)*(-coord[1]+self.c)^2*(-coord[1]+self.d)+3*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2*(-coord[1]+self.c)^2*(-coord[1]+self.d)

    def partialGxy2858(self,coord):

        return 2*(-coord[0]+self.a)^3*(-coord[0]+self.b)*(-coord[1]+self.c)^3*(-coord[1]+self.d)+3*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2*(-coord[1]+self.c)^3*(-coord[1]+self.d)

    def partialGxy2859(self,coord):

        return 2*(-coord[0]+self.a)^3*(-coord[0]+self.b)*(-coord[1]+self.c)^4*(-coord[1]+self.d)+3*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2*(-coord[1]+self.c)^4*(-coord[1]+self.d)

    def partialGxy2860(self,coord):

        return 2*(-coord[0]+self.a)^3*(-coord[0]+self.b)*(-coord[1]+self.d)^2+3*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2*(-coord[1]+self.d)^2

    def partialGxy2861(self,coord):

        return 2*(-coord[0]+self.a)^3*(-coord[0]+self.b)*(-coord[1]+self.c)*(-coord[1]+self.d)^2+3*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2*(-coord[1]+self.c)*(-coord[1]+self.d)^2

    def partialGxy2862(self,coord):

        return 2*(-coord[0]+self.a)^3*(-coord[0]+self.b)*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2+3*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2

    def partialGxy2863(self,coord):

        return 2*(-coord[0]+self.a)^3*(-coord[0]+self.b)*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2+3*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2

    def partialGxy2864(self,coord):

        return 2*(-coord[0]+self.a)^3*(-coord[0]+self.b)*(-coord[1]+self.c)^4*(-coord[1]+self.d)^2+3*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2*(-coord[1]+self.c)^4*(-coord[1]+self.d)^2

    def partialGxy2865(self,coord):

        return 2*(-coord[0]+self.a)^3*(-coord[0]+self.b)*(-coord[1]+self.d)^3+3*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2*(-coord[1]+self.d)^3

    def partialGxy2866(self,coord):

        return 2*(-coord[0]+self.a)^3*(-coord[0]+self.b)*(-coord[1]+self.c)*(-coord[1]+self.d)^3+3*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2*(-coord[1]+self.c)*(-coord[1]+self.d)^3

    def partialGxy2867(self,coord):

        return 2*(-coord[0]+self.a)^3*(-coord[0]+self.b)*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3+3*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3

    def partialGxy2868(self,coord):

        return 2*(-coord[0]+self.a)^3*(-coord[0]+self.b)*(-coord[1]+self.c)^3*(-coord[1]+self.d)^3+3*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2*(-coord[1]+self.c)^3*(-coord[1]+self.d)^3

    def partialGxy2869(self,coord):

        return 2*(-coord[0]+self.a)^3*(-coord[0]+self.b)*(-coord[1]+self.c)^4*(-coord[1]+self.d)^3+3*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2*(-coord[1]+self.c)^4*(-coord[1]+self.d)^3

    def partialGxy2870(self,coord):

        return 2*(-coord[0]+self.a)^3*(-coord[0]+self.b)*(-coord[1]+self.d)^4+3*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2*(-coord[1]+self.d)^4

    def partialGxy2871(self,coord):

        return 2*(-coord[0]+self.a)^3*(-coord[0]+self.b)*(-coord[1]+self.c)*(-coord[1]+self.d)^4+3*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2*(-coord[1]+self.c)*(-coord[1]+self.d)^4

    def partialGxy2872(self,coord):

        return 2*(-coord[0]+self.a)^3*(-coord[0]+self.b)*(-coord[1]+self.c)^2*(-coord[1]+self.d)^4+3*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2*(-coord[1]+self.c)^2*(-coord[1]+self.d)^4

    def partialGxy2873(self,coord):

        return 2*(-coord[0]+self.a)^3*(-coord[0]+self.b)*(-coord[1]+self.c)^3*(-coord[1]+self.d)^4+3*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2*(-coord[1]+self.c)^3*(-coord[1]+self.d)^4

    def partialGxy2874(self,coord):

        return 2*(-coord[0]+self.a)^3*(-coord[0]+self.b)*(-coord[1]+self.c)^4*(-coord[1]+self.d)^4+3*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2*(-coord[1]+self.c)^4*(-coord[1]+self.d)^4

    def partialGxy2881(self,coord):

        return 2*(-coord[0]+self.a)^3*(-coord[0]+self.b)*(-coord[1]+self.c)+3*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2*(-coord[1]+self.c)+2*(-coord[0]+self.a)^3*(-coord[0]+self.b)*(-coord[1]+self.d)+3*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2*(-coord[1]+self.d)

    def partialGxy2882(self,coord):

        return 2*(-coord[0]+self.a)^3*(-coord[0]+self.b)*(-coord[1]+self.c)^2+3*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2*(-coord[1]+self.c)^2+4*(-coord[0]+self.a)^3*(-coord[0]+self.b)*(-coord[1]+self.c)*(-coord[1]+self.d)+6*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2*(-coord[1]+self.c)*(-coord[1]+self.d)

    def partialGxy2883(self,coord):

        return 2*(-coord[0]+self.a)^3*(-coord[0]+self.b)*(-coord[1]+self.c)^3+3*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2*(-coord[1]+self.c)^3+6*(-coord[0]+self.a)^3*(-coord[0]+self.b)*(-coord[1]+self.c)^2*(-coord[1]+self.d)+9*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2*(-coord[1]+self.c)^2*(-coord[1]+self.d)

    def partialGxy2884(self,coord):

        return 2*(-coord[0]+self.a)^3*(-coord[0]+self.b)*(-coord[1]+self.c)^4+3*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2*(-coord[1]+self.c)^4+8*(-coord[0]+self.a)^3*(-coord[0]+self.b)*(-coord[1]+self.c)^3*(-coord[1]+self.d)+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2*(-coord[1]+self.c)^3*(-coord[1]+self.d)

    def partialGxy2886(self,coord):

        return 4*(-coord[0]+self.a)^3*(-coord[0]+self.b)*(-coord[1]+self.c)*(-coord[1]+self.d)+6*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2*(-coord[1]+self.c)*(-coord[1]+self.d)+2*(-coord[0]+self.a)^3*(-coord[0]+self.b)*(-coord[1]+self.d)^2+3*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2*(-coord[1]+self.d)^2

    def partialGxy2887(self,coord):

        return 4*(-coord[0]+self.a)^3*(-coord[0]+self.b)*(-coord[1]+self.c)^2*(-coord[1]+self.d)+6*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2*(-coord[1]+self.c)^2*(-coord[1]+self.d)+4*(-coord[0]+self.a)^3*(-coord[0]+self.b)*(-coord[1]+self.c)*(-coord[1]+self.d)^2+6*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2*(-coord[1]+self.c)*(-coord[1]+self.d)^2

    def partialGxy2888(self,coord):

        return 4*(-coord[0]+self.a)^3*(-coord[0]+self.b)*(-coord[1]+self.c)^3*(-coord[1]+self.d)+6*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2*(-coord[1]+self.c)^3*(-coord[1]+self.d)+6*(-coord[0]+self.a)^3*(-coord[0]+self.b)*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2+9*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2

    def partialGxy2889(self,coord):

        return 4*(-coord[0]+self.a)^3*(-coord[0]+self.b)*(-coord[1]+self.c)^4*(-coord[1]+self.d)+6*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2*(-coord[1]+self.c)^4*(-coord[1]+self.d)+8*(-coord[0]+self.a)^3*(-coord[0]+self.b)*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2

    def partialGxy2891(self,coord):

        return 6*(-coord[0]+self.a)^3*(-coord[0]+self.b)*(-coord[1]+self.c)*(-coord[1]+self.d)^2+9*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2*(-coord[1]+self.c)*(-coord[1]+self.d)^2+2*(-coord[0]+self.a)^3*(-coord[0]+self.b)*(-coord[1]+self.d)^3+3*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2*(-coord[1]+self.d)^3

    def partialGxy2892(self,coord):

        return 6*(-coord[0]+self.a)^3*(-coord[0]+self.b)*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2+9*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2+4*(-coord[0]+self.a)^3*(-coord[0]+self.b)*(-coord[1]+self.c)*(-coord[1]+self.d)^3+6*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2*(-coord[1]+self.c)*(-coord[1]+self.d)^3

    def partialGxy2893(self,coord):

        return 6*(-coord[0]+self.a)^3*(-coord[0]+self.b)*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2+9*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2+6*(-coord[0]+self.a)^3*(-coord[0]+self.b)*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3+9*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3

    def partialGxy2894(self,coord):

        return 6*(-coord[0]+self.a)^3*(-coord[0]+self.b)*(-coord[1]+self.c)^4*(-coord[1]+self.d)^2+9*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2*(-coord[1]+self.c)^4*(-coord[1]+self.d)^2+8*(-coord[0]+self.a)^3*(-coord[0]+self.b)*(-coord[1]+self.c)^3*(-coord[1]+self.d)^3+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2*(-coord[1]+self.c)^3*(-coord[1]+self.d)^3

    def partialGxy2896(self,coord):

        return 8*(-coord[0]+self.a)^3*(-coord[0]+self.b)*(-coord[1]+self.c)*(-coord[1]+self.d)^3+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2*(-coord[1]+self.c)*(-coord[1]+self.d)^3+2*(-coord[0]+self.a)^3*(-coord[0]+self.b)*(-coord[1]+self.d)^4+3*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2*(-coord[1]+self.d)^4

    def partialGxy2897(self,coord):

        return 8*(-coord[0]+self.a)^3*(-coord[0]+self.b)*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3+4*(-coord[0]+self.a)^3*(-coord[0]+self.b)*(-coord[1]+self.c)*(-coord[1]+self.d)^4+6*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2*(-coord[1]+self.c)*(-coord[1]+self.d)^4

    def partialGxy2898(self,coord):

        return 8*(-coord[0]+self.a)^3*(-coord[0]+self.b)*(-coord[1]+self.c)^3*(-coord[1]+self.d)^3+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2*(-coord[1]+self.c)^3*(-coord[1]+self.d)^3+6*(-coord[0]+self.a)^3*(-coord[0]+self.b)*(-coord[1]+self.c)^2*(-coord[1]+self.d)^4+9*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2*(-coord[1]+self.c)^2*(-coord[1]+self.d)^4

    def partialGxy2899(self,coord):

        return 8*(-coord[0]+self.a)^3*(-coord[0]+self.b)*(-coord[1]+self.c)^4*(-coord[1]+self.d)^3+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2*(-coord[1]+self.c)^4*(-coord[1]+self.d)^3+8*(-coord[0]+self.a)^3*(-coord[0]+self.b)*(-coord[1]+self.c)^3*(-coord[1]+self.d)^4+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2*(-coord[1]+self.c)^3*(-coord[1]+self.d)^4

    def partialGxy2912(self,coord):

        return 2*(-coord[0]+self.a)^3*(-coord[0]+self.b)*(2*(-coord[1]+self.c)^2+8*(-coord[1]+self.c)*(-coord[1]+self.d)+2*(-coord[1]+self.d)^2)+3*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2*(2*(-coord[1]+self.c)^2+8*(-coord[1]+self.c)*(-coord[1]+self.d)+2*(-coord[1]+self.d)^2)

    def partialGxy2913(self,coord):

        return 2*(-coord[0]+self.a)^3*(-coord[0]+self.b)*(2*(-coord[1]+self.c)^3+12*(-coord[1]+self.c)^2*(-coord[1]+self.d)+6*(-coord[1]+self.c)*(-coord[1]+self.d)^2)+3*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2*(2*(-coord[1]+self.c)^3+12*(-coord[1]+self.c)^2*(-coord[1]+self.d)+6*(-coord[1]+self.c)*(-coord[1]+self.d)^2)

    def partialGxy2914(self,coord):

        return 2*(-coord[0]+self.a)^3*(-coord[0]+self.b)*(2*(-coord[1]+self.c)^4+16*(-coord[1]+self.c)^3*(-coord[1]+self.d)+12*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2)+3*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2*(2*(-coord[1]+self.c)^4+16*(-coord[1]+self.c)^3*(-coord[1]+self.d)+12*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2)

    def partialGxy2917(self,coord):

        return 2*(-coord[0]+self.a)^3*(-coord[0]+self.b)*(6*(-coord[1]+self.c)^2*(-coord[1]+self.d)+12*(-coord[1]+self.c)*(-coord[1]+self.d)^2+2*(-coord[1]+self.d)^3)+3*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2*(6*(-coord[1]+self.c)^2*(-coord[1]+self.d)+12*(-coord[1]+self.c)*(-coord[1]+self.d)^2+2*(-coord[1]+self.d)^3)

    def partialGxy2918(self,coord):

        return 2*(-coord[0]+self.a)^3*(-coord[0]+self.b)*(6*(-coord[1]+self.c)^3*(-coord[1]+self.d)+18*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2+6*(-coord[1]+self.c)*(-coord[1]+self.d)^3)+3*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2*(6*(-coord[1]+self.c)^3*(-coord[1]+self.d)+18*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2+6*(-coord[1]+self.c)*(-coord[1]+self.d)^3)

    def partialGxy2919(self,coord):

        return 2*(-coord[0]+self.a)^3*(-coord[0]+self.b)*(6*(-coord[1]+self.c)^4*(-coord[1]+self.d)+24*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2+12*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3)+3*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2*(6*(-coord[1]+self.c)^4*(-coord[1]+self.d)+24*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2+12*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3)

    def partialGxy2922(self,coord):

        return 2*(-coord[0]+self.a)^3*(-coord[0]+self.b)*(12*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2+16*(-coord[1]+self.c)*(-coord[1]+self.d)^3+2*(-coord[1]+self.d)^4)+3*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2*(12*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2+16*(-coord[1]+self.c)*(-coord[1]+self.d)^3+2*(-coord[1]+self.d)^4)

    def partialGxy2923(self,coord):

        return 2*(-coord[0]+self.a)^3*(-coord[0]+self.b)*(12*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2+24*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3+6*(-coord[1]+self.c)*(-coord[1]+self.d)^4)+3*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2*(12*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2+24*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3+6*(-coord[1]+self.c)*(-coord[1]+self.d)^4)

    def partialGxy2924(self,coord):

        return 2*(-coord[0]+self.a)^3*(-coord[0]+self.b)*(12*(-coord[1]+self.c)^4*(-coord[1]+self.d)^2+32*(-coord[1]+self.c)^3*(-coord[1]+self.d)^3+12*(-coord[1]+self.c)^2*(-coord[1]+self.d)^4)+3*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2*(12*(-coord[1]+self.c)^4*(-coord[1]+self.d)^2+32*(-coord[1]+self.c)^3*(-coord[1]+self.d)^3+12*(-coord[1]+self.c)^2*(-coord[1]+self.d)^4)

    def partialGxy2925(self,coord):

        return 2*(-coord[0]+self.a)^4*(-coord[0]+self.b)+4*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2

    def partialGxy2926(self,coord):

        return 2*(-coord[0]+self.a)^4*(-coord[0]+self.b)*(-coord[1]+self.c)+4*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2*(-coord[1]+self.c)

    def partialGxy2927(self,coord):

        return 2*(-coord[0]+self.a)^4*(-coord[0]+self.b)*(-coord[1]+self.c)^2+4*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2*(-coord[1]+self.c)^2

    def partialGxy2928(self,coord):

        return 2*(-coord[0]+self.a)^4*(-coord[0]+self.b)*(-coord[1]+self.c)^3+4*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2*(-coord[1]+self.c)^3

    def partialGxy2929(self,coord):

        return 2*(-coord[0]+self.a)^4*(-coord[0]+self.b)*(-coord[1]+self.c)^4+4*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2*(-coord[1]+self.c)^4

    def partialGxy2930(self,coord):

        return 2*(-coord[0]+self.a)^4*(-coord[0]+self.b)*(-coord[1]+self.d)+4*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2*(-coord[1]+self.d)

    def partialGxy2931(self,coord):

        return 2*(-coord[0]+self.a)^4*(-coord[0]+self.b)*(-coord[1]+self.c)*(-coord[1]+self.d)+4*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2*(-coord[1]+self.c)*(-coord[1]+self.d)

    def partialGxy2932(self,coord):

        return 2*(-coord[0]+self.a)^4*(-coord[0]+self.b)*(-coord[1]+self.c)^2*(-coord[1]+self.d)+4*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2*(-coord[1]+self.c)^2*(-coord[1]+self.d)

    def partialGxy2933(self,coord):

        return 2*(-coord[0]+self.a)^4*(-coord[0]+self.b)*(-coord[1]+self.c)^3*(-coord[1]+self.d)+4*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2*(-coord[1]+self.c)^3*(-coord[1]+self.d)

    def partialGxy2934(self,coord):

        return 2*(-coord[0]+self.a)^4*(-coord[0]+self.b)*(-coord[1]+self.c)^4*(-coord[1]+self.d)+4*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2*(-coord[1]+self.c)^4*(-coord[1]+self.d)

    def partialGxy2935(self,coord):

        return 2*(-coord[0]+self.a)^4*(-coord[0]+self.b)*(-coord[1]+self.d)^2+4*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2*(-coord[1]+self.d)^2

    def partialGxy2936(self,coord):

        return 2*(-coord[0]+self.a)^4*(-coord[0]+self.b)*(-coord[1]+self.c)*(-coord[1]+self.d)^2+4*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2*(-coord[1]+self.c)*(-coord[1]+self.d)^2

    def partialGxy2937(self,coord):

        return 2*(-coord[0]+self.a)^4*(-coord[0]+self.b)*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2+4*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2

    def partialGxy2938(self,coord):

        return 2*(-coord[0]+self.a)^4*(-coord[0]+self.b)*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2+4*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2

    def partialGxy2939(self,coord):

        return 2*(-coord[0]+self.a)^4*(-coord[0]+self.b)*(-coord[1]+self.c)^4*(-coord[1]+self.d)^2+4*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2*(-coord[1]+self.c)^4*(-coord[1]+self.d)^2

    def partialGxy2940(self,coord):

        return 2*(-coord[0]+self.a)^4*(-coord[0]+self.b)*(-coord[1]+self.d)^3+4*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2*(-coord[1]+self.d)^3

    def partialGxy2941(self,coord):

        return 2*(-coord[0]+self.a)^4*(-coord[0]+self.b)*(-coord[1]+self.c)*(-coord[1]+self.d)^3+4*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2*(-coord[1]+self.c)*(-coord[1]+self.d)^3

    def partialGxy2942(self,coord):

        return 2*(-coord[0]+self.a)^4*(-coord[0]+self.b)*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3+4*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3

    def partialGxy2943(self,coord):

        return 2*(-coord[0]+self.a)^4*(-coord[0]+self.b)*(-coord[1]+self.c)^3*(-coord[1]+self.d)^3+4*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2*(-coord[1]+self.c)^3*(-coord[1]+self.d)^3

    def partialGxy2944(self,coord):

        return 2*(-coord[0]+self.a)^4*(-coord[0]+self.b)*(-coord[1]+self.c)^4*(-coord[1]+self.d)^3+4*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2*(-coord[1]+self.c)^4*(-coord[1]+self.d)^3

    def partialGxy2945(self,coord):

        return 2*(-coord[0]+self.a)^4*(-coord[0]+self.b)*(-coord[1]+self.d)^4+4*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2*(-coord[1]+self.d)^4

    def partialGxy2946(self,coord):

        return 2*(-coord[0]+self.a)^4*(-coord[0]+self.b)*(-coord[1]+self.c)*(-coord[1]+self.d)^4+4*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2*(-coord[1]+self.c)*(-coord[1]+self.d)^4

    def partialGxy2947(self,coord):

        return 2*(-coord[0]+self.a)^4*(-coord[0]+self.b)*(-coord[1]+self.c)^2*(-coord[1]+self.d)^4+4*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2*(-coord[1]+self.c)^2*(-coord[1]+self.d)^4

    def partialGxy2948(self,coord):

        return 2*(-coord[0]+self.a)^4*(-coord[0]+self.b)*(-coord[1]+self.c)^3*(-coord[1]+self.d)^4+4*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2*(-coord[1]+self.c)^3*(-coord[1]+self.d)^4

    def partialGxy2949(self,coord):

        return 2*(-coord[0]+self.a)^4*(-coord[0]+self.b)*(-coord[1]+self.c)^4*(-coord[1]+self.d)^4+4*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2*(-coord[1]+self.c)^4*(-coord[1]+self.d)^4

    def partialGxy2956(self,coord):

        return 2*(-coord[0]+self.a)^4*(-coord[0]+self.b)*(-coord[1]+self.c)+4*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2*(-coord[1]+self.c)+2*(-coord[0]+self.a)^4*(-coord[0]+self.b)*(-coord[1]+self.d)+4*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2*(-coord[1]+self.d)

    def partialGxy2957(self,coord):

        return 2*(-coord[0]+self.a)^4*(-coord[0]+self.b)*(-coord[1]+self.c)^2+4*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2*(-coord[1]+self.c)^2+4*(-coord[0]+self.a)^4*(-coord[0]+self.b)*(-coord[1]+self.c)*(-coord[1]+self.d)+8*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2*(-coord[1]+self.c)*(-coord[1]+self.d)

    def partialGxy2958(self,coord):

        return 2*(-coord[0]+self.a)^4*(-coord[0]+self.b)*(-coord[1]+self.c)^3+4*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2*(-coord[1]+self.c)^3+6*(-coord[0]+self.a)^4*(-coord[0]+self.b)*(-coord[1]+self.c)^2*(-coord[1]+self.d)+12*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2*(-coord[1]+self.c)^2*(-coord[1]+self.d)

    def partialGxy2959(self,coord):

        return 2*(-coord[0]+self.a)^4*(-coord[0]+self.b)*(-coord[1]+self.c)^4+4*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2*(-coord[1]+self.c)^4+8*(-coord[0]+self.a)^4*(-coord[0]+self.b)*(-coord[1]+self.c)^3*(-coord[1]+self.d)+16*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2*(-coord[1]+self.c)^3*(-coord[1]+self.d)

    def partialGxy2961(self,coord):

        return 4*(-coord[0]+self.a)^4*(-coord[0]+self.b)*(-coord[1]+self.c)*(-coord[1]+self.d)+8*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2*(-coord[1]+self.c)*(-coord[1]+self.d)+2*(-coord[0]+self.a)^4*(-coord[0]+self.b)*(-coord[1]+self.d)^2+4*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2*(-coord[1]+self.d)^2

    def partialGxy2962(self,coord):

        return 4*(-coord[0]+self.a)^4*(-coord[0]+self.b)*(-coord[1]+self.c)^2*(-coord[1]+self.d)+8*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2*(-coord[1]+self.c)^2*(-coord[1]+self.d)+4*(-coord[0]+self.a)^4*(-coord[0]+self.b)*(-coord[1]+self.c)*(-coord[1]+self.d)^2+8*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2*(-coord[1]+self.c)*(-coord[1]+self.d)^2

    def partialGxy2963(self,coord):

        return 4*(-coord[0]+self.a)^4*(-coord[0]+self.b)*(-coord[1]+self.c)^3*(-coord[1]+self.d)+8*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2*(-coord[1]+self.c)^3*(-coord[1]+self.d)+6*(-coord[0]+self.a)^4*(-coord[0]+self.b)*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2+12*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2

    def partialGxy2964(self,coord):

        return 4*(-coord[0]+self.a)^4*(-coord[0]+self.b)*(-coord[1]+self.c)^4*(-coord[1]+self.d)+8*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2*(-coord[1]+self.c)^4*(-coord[1]+self.d)+8*(-coord[0]+self.a)^4*(-coord[0]+self.b)*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2+16*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2

    def partialGxy2966(self,coord):

        return 6*(-coord[0]+self.a)^4*(-coord[0]+self.b)*(-coord[1]+self.c)*(-coord[1]+self.d)^2+12*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2*(-coord[1]+self.c)*(-coord[1]+self.d)^2+2*(-coord[0]+self.a)^4*(-coord[0]+self.b)*(-coord[1]+self.d)^3+4*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2*(-coord[1]+self.d)^3

    def partialGxy2967(self,coord):

        return 6*(-coord[0]+self.a)^4*(-coord[0]+self.b)*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2+12*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2+4*(-coord[0]+self.a)^4*(-coord[0]+self.b)*(-coord[1]+self.c)*(-coord[1]+self.d)^3+8*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2*(-coord[1]+self.c)*(-coord[1]+self.d)^3

    def partialGxy2968(self,coord):

        return 6*(-coord[0]+self.a)^4*(-coord[0]+self.b)*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2+12*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2+6*(-coord[0]+self.a)^4*(-coord[0]+self.b)*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3+12*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3

    def partialGxy2969(self,coord):

        return 6*(-coord[0]+self.a)^4*(-coord[0]+self.b)*(-coord[1]+self.c)^4*(-coord[1]+self.d)^2+12*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2*(-coord[1]+self.c)^4*(-coord[1]+self.d)^2+8*(-coord[0]+self.a)^4*(-coord[0]+self.b)*(-coord[1]+self.c)^3*(-coord[1]+self.d)^3+16*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2*(-coord[1]+self.c)^3*(-coord[1]+self.d)^3

    def partialGxy2971(self,coord):

        return 8*(-coord[0]+self.a)^4*(-coord[0]+self.b)*(-coord[1]+self.c)*(-coord[1]+self.d)^3+16*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2*(-coord[1]+self.c)*(-coord[1]+self.d)^3+2*(-coord[0]+self.a)^4*(-coord[0]+self.b)*(-coord[1]+self.d)^4+4*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2*(-coord[1]+self.d)^4

    def partialGxy2972(self,coord):

        return 8*(-coord[0]+self.a)^4*(-coord[0]+self.b)*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3+16*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3+4*(-coord[0]+self.a)^4*(-coord[0]+self.b)*(-coord[1]+self.c)*(-coord[1]+self.d)^4+8*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2*(-coord[1]+self.c)*(-coord[1]+self.d)^4

    def partialGxy2973(self,coord):

        return 8*(-coord[0]+self.a)^4*(-coord[0]+self.b)*(-coord[1]+self.c)^3*(-coord[1]+self.d)^3+16*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2*(-coord[1]+self.c)^3*(-coord[1]+self.d)^3+6*(-coord[0]+self.a)^4*(-coord[0]+self.b)*(-coord[1]+self.c)^2*(-coord[1]+self.d)^4+12*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2*(-coord[1]+self.c)^2*(-coord[1]+self.d)^4

    def partialGxy2974(self,coord):

        return 8*(-coord[0]+self.a)^4*(-coord[0]+self.b)*(-coord[1]+self.c)^4*(-coord[1]+self.d)^3+16*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2*(-coord[1]+self.c)^4*(-coord[1]+self.d)^3+8*(-coord[0]+self.a)^4*(-coord[0]+self.b)*(-coord[1]+self.c)^3*(-coord[1]+self.d)^4+16*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2*(-coord[1]+self.c)^3*(-coord[1]+self.d)^4

    def partialGxy2987(self,coord):

        return 2*(-coord[0]+self.a)^4*(-coord[0]+self.b)*(2*(-coord[1]+self.c)^2+8*(-coord[1]+self.c)*(-coord[1]+self.d)+2*(-coord[1]+self.d)^2)+4*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2*(2*(-coord[1]+self.c)^2+8*(-coord[1]+self.c)*(-coord[1]+self.d)+2*(-coord[1]+self.d)^2)

    def partialGxy2988(self,coord):

        return 2*(-coord[0]+self.a)^4*(-coord[0]+self.b)*(2*(-coord[1]+self.c)^3+12*(-coord[1]+self.c)^2*(-coord[1]+self.d)+6*(-coord[1]+self.c)*(-coord[1]+self.d)^2)+4*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2*(2*(-coord[1]+self.c)^3+12*(-coord[1]+self.c)^2*(-coord[1]+self.d)+6*(-coord[1]+self.c)*(-coord[1]+self.d)^2)

    def partialGxy2989(self,coord):

        return 2*(-coord[0]+self.a)^4*(-coord[0]+self.b)*(2*(-coord[1]+self.c)^4+16*(-coord[1]+self.c)^3*(-coord[1]+self.d)+12*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2)+4*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2*(2*(-coord[1]+self.c)^4+16*(-coord[1]+self.c)^3*(-coord[1]+self.d)+12*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2)

    def partialGxy2992(self,coord):

        return 2*(-coord[0]+self.a)^4*(-coord[0]+self.b)*(6*(-coord[1]+self.c)^2*(-coord[1]+self.d)+12*(-coord[1]+self.c)*(-coord[1]+self.d)^2+2*(-coord[1]+self.d)^3)+4*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2*(6*(-coord[1]+self.c)^2*(-coord[1]+self.d)+12*(-coord[1]+self.c)*(-coord[1]+self.d)^2+2*(-coord[1]+self.d)^3)

    def partialGxy2993(self,coord):

        return 2*(-coord[0]+self.a)^4*(-coord[0]+self.b)*(6*(-coord[1]+self.c)^3*(-coord[1]+self.d)+18*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2+6*(-coord[1]+self.c)*(-coord[1]+self.d)^3)+4*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2*(6*(-coord[1]+self.c)^3*(-coord[1]+self.d)+18*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2+6*(-coord[1]+self.c)*(-coord[1]+self.d)^3)

    def partialGxy2994(self,coord):

        return 2*(-coord[0]+self.a)^4*(-coord[0]+self.b)*(6*(-coord[1]+self.c)^4*(-coord[1]+self.d)+24*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2+12*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3)+4*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2*(6*(-coord[1]+self.c)^4*(-coord[1]+self.d)+24*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2+12*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3)

    def partialGxy2997(self,coord):

        return 2*(-coord[0]+self.a)^4*(-coord[0]+self.b)*(12*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2+16*(-coord[1]+self.c)*(-coord[1]+self.d)^3+2*(-coord[1]+self.d)^4)+4*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2*(12*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2+16*(-coord[1]+self.c)*(-coord[1]+self.d)^3+2*(-coord[1]+self.d)^4)

    def partialGxy2998(self,coord):

        return 2*(-coord[0]+self.a)^4*(-coord[0]+self.b)*(12*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2+24*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3+6*(-coord[1]+self.c)*(-coord[1]+self.d)^4)+4*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2*(12*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2+24*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3+6*(-coord[1]+self.c)*(-coord[1]+self.d)^4)

    def partialGxy2999(self,coord):

        return 2*(-coord[0]+self.a)^4*(-coord[0]+self.b)*(12*(-coord[1]+self.c)^4*(-coord[1]+self.d)^2+32*(-coord[1]+self.c)^3*(-coord[1]+self.d)^3+12*(-coord[1]+self.c)^2*(-coord[1]+self.d)^4)+4*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2*(12*(-coord[1]+self.c)^4*(-coord[1]+self.d)^2+32*(-coord[1]+self.c)^3*(-coord[1]+self.d)^3+12*(-coord[1]+self.c)^2*(-coord[1]+self.d)^4)

    def partialGxy3075(self,coord):

        return 3*(-coord[0]+self.a)*(-coord[0]+self.b)^2+(-coord[0]+self.b)^3

    def partialGxy3076(self,coord):

        return 3*(-coord[0]+self.a)*(-coord[0]+self.b)^2*(-coord[1]+self.c)+(-coord[0]+self.b)^3*(-coord[1]+self.c)

    def partialGxy3077(self,coord):

        return 3*(-coord[0]+self.a)*(-coord[0]+self.b)^2*(-coord[1]+self.c)^2+(-coord[0]+self.b)^3*(-coord[1]+self.c)^2

    def partialGxy3078(self,coord):

        return 3*(-coord[0]+self.a)*(-coord[0]+self.b)^2*(-coord[1]+self.c)^3+(-coord[0]+self.b)^3*(-coord[1]+self.c)^3

    def partialGxy3079(self,coord):

        return 3*(-coord[0]+self.a)*(-coord[0]+self.b)^2*(-coord[1]+self.c)^4+(-coord[0]+self.b)^3*(-coord[1]+self.c)^4

    def partialGxy3080(self,coord):

        return 3*(-coord[0]+self.a)*(-coord[0]+self.b)^2*(-coord[1]+self.d)+(-coord[0]+self.b)^3*(-coord[1]+self.d)

    def partialGxy3081(self,coord):

        return 3*(-coord[0]+self.a)*(-coord[0]+self.b)^2*(-coord[1]+self.c)*(-coord[1]+self.d)+(-coord[0]+self.b)^3*(-coord[1]+self.c)*(-coord[1]+self.d)

    def partialGxy3082(self,coord):

        return 3*(-coord[0]+self.a)*(-coord[0]+self.b)^2*(-coord[1]+self.c)^2*(-coord[1]+self.d)+(-coord[0]+self.b)^3*(-coord[1]+self.c)^2*(-coord[1]+self.d)

    def partialGxy3083(self,coord):

        return 3*(-coord[0]+self.a)*(-coord[0]+self.b)^2*(-coord[1]+self.c)^3*(-coord[1]+self.d)+(-coord[0]+self.b)^3*(-coord[1]+self.c)^3*(-coord[1]+self.d)

    def partialGxy3084(self,coord):

        return 3*(-coord[0]+self.a)*(-coord[0]+self.b)^2*(-coord[1]+self.c)^4*(-coord[1]+self.d)+(-coord[0]+self.b)^3*(-coord[1]+self.c)^4*(-coord[1]+self.d)

    def partialGxy3085(self,coord):

        return 3*(-coord[0]+self.a)*(-coord[0]+self.b)^2*(-coord[1]+self.d)^2+(-coord[0]+self.b)^3*(-coord[1]+self.d)^2

    def partialGxy3086(self,coord):

        return 3*(-coord[0]+self.a)*(-coord[0]+self.b)^2*(-coord[1]+self.c)*(-coord[1]+self.d)^2+(-coord[0]+self.b)^3*(-coord[1]+self.c)*(-coord[1]+self.d)^2

    def partialGxy3087(self,coord):

        return 3*(-coord[0]+self.a)*(-coord[0]+self.b)^2*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2+(-coord[0]+self.b)^3*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2

    def partialGxy3088(self,coord):

        return 3*(-coord[0]+self.a)*(-coord[0]+self.b)^2*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2+(-coord[0]+self.b)^3*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2

    def partialGxy3089(self,coord):

        return 3*(-coord[0]+self.a)*(-coord[0]+self.b)^2*(-coord[1]+self.c)^4*(-coord[1]+self.d)^2+(-coord[0]+self.b)^3*(-coord[1]+self.c)^4*(-coord[1]+self.d)^2

    def partialGxy3090(self,coord):

        return 3*(-coord[0]+self.a)*(-coord[0]+self.b)^2*(-coord[1]+self.d)^3+(-coord[0]+self.b)^3*(-coord[1]+self.d)^3

    def partialGxy3091(self,coord):

        return 3*(-coord[0]+self.a)*(-coord[0]+self.b)^2*(-coord[1]+self.c)*(-coord[1]+self.d)^3+(-coord[0]+self.b)^3*(-coord[1]+self.c)*(-coord[1]+self.d)^3

    def partialGxy3092(self,coord):

        return 3*(-coord[0]+self.a)*(-coord[0]+self.b)^2*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3+(-coord[0]+self.b)^3*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3

    def partialGxy3093(self,coord):

        return 3*(-coord[0]+self.a)*(-coord[0]+self.b)^2*(-coord[1]+self.c)^3*(-coord[1]+self.d)^3+(-coord[0]+self.b)^3*(-coord[1]+self.c)^3*(-coord[1]+self.d)^3

    def partialGxy3094(self,coord):

        return 3*(-coord[0]+self.a)*(-coord[0]+self.b)^2*(-coord[1]+self.c)^4*(-coord[1]+self.d)^3+(-coord[0]+self.b)^3*(-coord[1]+self.c)^4*(-coord[1]+self.d)^3

    def partialGxy3095(self,coord):

        return 3*(-coord[0]+self.a)*(-coord[0]+self.b)^2*(-coord[1]+self.d)^4+(-coord[0]+self.b)^3*(-coord[1]+self.d)^4

    def partialGxy3096(self,coord):

        return 3*(-coord[0]+self.a)*(-coord[0]+self.b)^2*(-coord[1]+self.c)*(-coord[1]+self.d)^4+(-coord[0]+self.b)^3*(-coord[1]+self.c)*(-coord[1]+self.d)^4

    def partialGxy3097(self,coord):

        return 3*(-coord[0]+self.a)*(-coord[0]+self.b)^2*(-coord[1]+self.c)^2*(-coord[1]+self.d)^4+(-coord[0]+self.b)^3*(-coord[1]+self.c)^2*(-coord[1]+self.d)^4

    def partialGxy3098(self,coord):

        return 3*(-coord[0]+self.a)*(-coord[0]+self.b)^2*(-coord[1]+self.c)^3*(-coord[1]+self.d)^4+(-coord[0]+self.b)^3*(-coord[1]+self.c)^3*(-coord[1]+self.d)^4

    def partialGxy3099(self,coord):

        return 3*(-coord[0]+self.a)*(-coord[0]+self.b)^2*(-coord[1]+self.c)^4*(-coord[1]+self.d)^4+(-coord[0]+self.b)^3*(-coord[1]+self.c)^4*(-coord[1]+self.d)^4

    def partialGxy3106(self,coord):

        return 3*(-coord[0]+self.a)*(-coord[0]+self.b)^2*(-coord[1]+self.c)+(-coord[0]+self.b)^3*(-coord[1]+self.c)+3*(-coord[0]+self.a)*(-coord[0]+self.b)^2*(-coord[1]+self.d)+(-coord[0]+self.b)^3*(-coord[1]+self.d)

    def partialGxy3107(self,coord):

        return 3*(-coord[0]+self.a)*(-coord[0]+self.b)^2*(-coord[1]+self.c)^2+(-coord[0]+self.b)^3*(-coord[1]+self.c)^2+6*(-coord[0]+self.a)*(-coord[0]+self.b)^2*(-coord[1]+self.c)*(-coord[1]+self.d)+2*(-coord[0]+self.b)^3*(-coord[1]+self.c)*(-coord[1]+self.d)

    def partialGxy3108(self,coord):

        return 3*(-coord[0]+self.a)*(-coord[0]+self.b)^2*(-coord[1]+self.c)^3+(-coord[0]+self.b)^3*(-coord[1]+self.c)^3+9*(-coord[0]+self.a)*(-coord[0]+self.b)^2*(-coord[1]+self.c)^2*(-coord[1]+self.d)+3*(-coord[0]+self.b)^3*(-coord[1]+self.c)^2*(-coord[1]+self.d)

    def partialGxy3109(self,coord):

        return 3*(-coord[0]+self.a)*(-coord[0]+self.b)^2*(-coord[1]+self.c)^4+(-coord[0]+self.b)^3*(-coord[1]+self.c)^4+12*(-coord[0]+self.a)*(-coord[0]+self.b)^2*(-coord[1]+self.c)^3*(-coord[1]+self.d)+4*(-coord[0]+self.b)^3*(-coord[1]+self.c)^3*(-coord[1]+self.d)

    def partialGxy3111(self,coord):

        return 6*(-coord[0]+self.a)*(-coord[0]+self.b)^2*(-coord[1]+self.c)*(-coord[1]+self.d)+2*(-coord[0]+self.b)^3*(-coord[1]+self.c)*(-coord[1]+self.d)+3*(-coord[0]+self.a)*(-coord[0]+self.b)^2*(-coord[1]+self.d)^2+(-coord[0]+self.b)^3*(-coord[1]+self.d)^2

    def partialGxy3112(self,coord):

        return 6*(-coord[0]+self.a)*(-coord[0]+self.b)^2*(-coord[1]+self.c)^2*(-coord[1]+self.d)+2*(-coord[0]+self.b)^3*(-coord[1]+self.c)^2*(-coord[1]+self.d)+6*(-coord[0]+self.a)*(-coord[0]+self.b)^2*(-coord[1]+self.c)*(-coord[1]+self.d)^2+2*(-coord[0]+self.b)^3*(-coord[1]+self.c)*(-coord[1]+self.d)^2

    def partialGxy3113(self,coord):

        return 6*(-coord[0]+self.a)*(-coord[0]+self.b)^2*(-coord[1]+self.c)^3*(-coord[1]+self.d)+2*(-coord[0]+self.b)^3*(-coord[1]+self.c)^3*(-coord[1]+self.d)+9*(-coord[0]+self.a)*(-coord[0]+self.b)^2*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2+3*(-coord[0]+self.b)^3*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2

    def partialGxy3114(self,coord):

        return 6*(-coord[0]+self.a)*(-coord[0]+self.b)^2*(-coord[1]+self.c)^4*(-coord[1]+self.d)+2*(-coord[0]+self.b)^3*(-coord[1]+self.c)^4*(-coord[1]+self.d)+12*(-coord[0]+self.a)*(-coord[0]+self.b)^2*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2+4*(-coord[0]+self.b)^3*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2

    def partialGxy3116(self,coord):

        return 9*(-coord[0]+self.a)*(-coord[0]+self.b)^2*(-coord[1]+self.c)*(-coord[1]+self.d)^2+3*(-coord[0]+self.b)^3*(-coord[1]+self.c)*(-coord[1]+self.d)^2+3*(-coord[0]+self.a)*(-coord[0]+self.b)^2*(-coord[1]+self.d)^3+(-coord[0]+self.b)^3*(-coord[1]+self.d)^3

    def partialGxy3117(self,coord):

        return 9*(-coord[0]+self.a)*(-coord[0]+self.b)^2*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2+3*(-coord[0]+self.b)^3*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2+6*(-coord[0]+self.a)*(-coord[0]+self.b)^2*(-coord[1]+self.c)*(-coord[1]+self.d)^3+2*(-coord[0]+self.b)^3*(-coord[1]+self.c)*(-coord[1]+self.d)^3

    def partialGxy3118(self,coord):

        return 9*(-coord[0]+self.a)*(-coord[0]+self.b)^2*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2+3*(-coord[0]+self.b)^3*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2+9*(-coord[0]+self.a)*(-coord[0]+self.b)^2*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3+3*(-coord[0]+self.b)^3*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3

    def partialGxy3119(self,coord):

        return 9*(-coord[0]+self.a)*(-coord[0]+self.b)^2*(-coord[1]+self.c)^4*(-coord[1]+self.d)^2+3*(-coord[0]+self.b)^3*(-coord[1]+self.c)^4*(-coord[1]+self.d)^2+12*(-coord[0]+self.a)*(-coord[0]+self.b)^2*(-coord[1]+self.c)^3*(-coord[1]+self.d)^3+4*(-coord[0]+self.b)^3*(-coord[1]+self.c)^3*(-coord[1]+self.d)^3

    def partialGxy3121(self,coord):

        return 12*(-coord[0]+self.a)*(-coord[0]+self.b)^2*(-coord[1]+self.c)*(-coord[1]+self.d)^3+4*(-coord[0]+self.b)^3*(-coord[1]+self.c)*(-coord[1]+self.d)^3+3*(-coord[0]+self.a)*(-coord[0]+self.b)^2*(-coord[1]+self.d)^4+(-coord[0]+self.b)^3*(-coord[1]+self.d)^4

    def partialGxy3122(self,coord):

        return 12*(-coord[0]+self.a)*(-coord[0]+self.b)^2*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3+4*(-coord[0]+self.b)^3*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3+6*(-coord[0]+self.a)*(-coord[0]+self.b)^2*(-coord[1]+self.c)*(-coord[1]+self.d)^4+2*(-coord[0]+self.b)^3*(-coord[1]+self.c)*(-coord[1]+self.d)^4

    def partialGxy3123(self,coord):

        return 12*(-coord[0]+self.a)*(-coord[0]+self.b)^2*(-coord[1]+self.c)^3*(-coord[1]+self.d)^3+4*(-coord[0]+self.b)^3*(-coord[1]+self.c)^3*(-coord[1]+self.d)^3+9*(-coord[0]+self.a)*(-coord[0]+self.b)^2*(-coord[1]+self.c)^2*(-coord[1]+self.d)^4+3*(-coord[0]+self.b)^3*(-coord[1]+self.c)^2*(-coord[1]+self.d)^4

    def partialGxy3124(self,coord):

        return 12*(-coord[0]+self.a)*(-coord[0]+self.b)^2*(-coord[1]+self.c)^4*(-coord[1]+self.d)^3+4*(-coord[0]+self.b)^3*(-coord[1]+self.c)^4*(-coord[1]+self.d)^3+12*(-coord[0]+self.a)*(-coord[0]+self.b)^2*(-coord[1]+self.c)^3*(-coord[1]+self.d)^4+4*(-coord[0]+self.b)^3*(-coord[1]+self.c)^3*(-coord[1]+self.d)^4

    def partialGxy3137(self,coord):

        return 3*(-coord[0]+self.a)*(-coord[0]+self.b)^2*(2*(-coord[1]+self.c)^2+8*(-coord[1]+self.c)*(-coord[1]+self.d)+2*(-coord[1]+self.d)^2)+(-coord[0]+self.b)^3*(2*(-coord[1]+self.c)^2+8*(-coord[1]+self.c)*(-coord[1]+self.d)+2*(-coord[1]+self.d)^2)

    def partialGxy3138(self,coord):

        return 3*(-coord[0]+self.a)*(-coord[0]+self.b)^2*(2*(-coord[1]+self.c)^3+12*(-coord[1]+self.c)^2*(-coord[1]+self.d)+6*(-coord[1]+self.c)*(-coord[1]+self.d)^2)+(-coord[0]+self.b)^3*(2*(-coord[1]+self.c)^3+12*(-coord[1]+self.c)^2*(-coord[1]+self.d)+6*(-coord[1]+self.c)*(-coord[1]+self.d)^2)

    def partialGxy3139(self,coord):

        return 3*(-coord[0]+self.a)*(-coord[0]+self.b)^2*(2*(-coord[1]+self.c)^4+16*(-coord[1]+self.c)^3*(-coord[1]+self.d)+12*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2)+(-coord[0]+self.b)^3*(2*(-coord[1]+self.c)^4+16*(-coord[1]+self.c)^3*(-coord[1]+self.d)+12*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2)

    def partialGxy3142(self,coord):

        return 3*(-coord[0]+self.a)*(-coord[0]+self.b)^2*(6*(-coord[1]+self.c)^2*(-coord[1]+self.d)+12*(-coord[1]+self.c)*(-coord[1]+self.d)^2+2*(-coord[1]+self.d)^3)+(-coord[0]+self.b)^3*(6*(-coord[1]+self.c)^2*(-coord[1]+self.d)+12*(-coord[1]+self.c)*(-coord[1]+self.d)^2+2*(-coord[1]+self.d)^3)

    def partialGxy3143(self,coord):

        return 3*(-coord[0]+self.a)*(-coord[0]+self.b)^2*(6*(-coord[1]+self.c)^3*(-coord[1]+self.d)+18*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2+6*(-coord[1]+self.c)*(-coord[1]+self.d)^3)+(-coord[0]+self.b)^3*(6*(-coord[1]+self.c)^3*(-coord[1]+self.d)+18*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2+6*(-coord[1]+self.c)*(-coord[1]+self.d)^3)

    def partialGxy3144(self,coord):

        return 3*(-coord[0]+self.a)*(-coord[0]+self.b)^2*(6*(-coord[1]+self.c)^4*(-coord[1]+self.d)+24*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2+12*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3)+(-coord[0]+self.b)^3*(6*(-coord[1]+self.c)^4*(-coord[1]+self.d)+24*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2+12*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3)

    def partialGxy3147(self,coord):

        return 3*(-coord[0]+self.a)*(-coord[0]+self.b)^2*(12*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2+16*(-coord[1]+self.c)*(-coord[1]+self.d)^3+2*(-coord[1]+self.d)^4)+(-coord[0]+self.b)^3*(12*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2+16*(-coord[1]+self.c)*(-coord[1]+self.d)^3+2*(-coord[1]+self.d)^4)

    def partialGxy3148(self,coord):

        return 3*(-coord[0]+self.a)*(-coord[0]+self.b)^2*(12*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2+24*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3+6*(-coord[1]+self.c)*(-coord[1]+self.d)^4)+(-coord[0]+self.b)^3*(12*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2+24*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3+6*(-coord[1]+self.c)*(-coord[1]+self.d)^4)

    def partialGxy3149(self,coord):

        return 3*(-coord[0]+self.a)*(-coord[0]+self.b)^2*(12*(-coord[1]+self.c)^4*(-coord[1]+self.d)^2+32*(-coord[1]+self.c)^3*(-coord[1]+self.d)^3+12*(-coord[1]+self.c)^2*(-coord[1]+self.d)^4)+(-coord[0]+self.b)^3*(12*(-coord[1]+self.c)^4*(-coord[1]+self.d)^2+32*(-coord[1]+self.c)^3*(-coord[1]+self.d)^3+12*(-coord[1]+self.c)^2*(-coord[1]+self.d)^4)

    def partialGxy3150(self,coord):

        return 3*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2+2*(-coord[0]+self.a)*(-coord[0]+self.b)^3

    def partialGxy3151(self,coord):

        return 3*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2*(-coord[1]+self.c)+2*(-coord[0]+self.a)*(-coord[0]+self.b)^3*(-coord[1]+self.c)

    def partialGxy3152(self,coord):

        return 3*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2*(-coord[1]+self.c)^2+2*(-coord[0]+self.a)*(-coord[0]+self.b)^3*(-coord[1]+self.c)^2

    def partialGxy3153(self,coord):

        return 3*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2*(-coord[1]+self.c)^3+2*(-coord[0]+self.a)*(-coord[0]+self.b)^3*(-coord[1]+self.c)^3

    def partialGxy3154(self,coord):

        return 3*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2*(-coord[1]+self.c)^4+2*(-coord[0]+self.a)*(-coord[0]+self.b)^3*(-coord[1]+self.c)^4

    def partialGxy3155(self,coord):

        return 3*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2*(-coord[1]+self.d)+2*(-coord[0]+self.a)*(-coord[0]+self.b)^3*(-coord[1]+self.d)

    def partialGxy3156(self,coord):

        return 3*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2*(-coord[1]+self.c)*(-coord[1]+self.d)+2*(-coord[0]+self.a)*(-coord[0]+self.b)^3*(-coord[1]+self.c)*(-coord[1]+self.d)

    def partialGxy3157(self,coord):

        return 3*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2*(-coord[1]+self.c)^2*(-coord[1]+self.d)+2*(-coord[0]+self.a)*(-coord[0]+self.b)^3*(-coord[1]+self.c)^2*(-coord[1]+self.d)

    def partialGxy3158(self,coord):

        return 3*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2*(-coord[1]+self.c)^3*(-coord[1]+self.d)+2*(-coord[0]+self.a)*(-coord[0]+self.b)^3*(-coord[1]+self.c)^3*(-coord[1]+self.d)

    def partialGxy3159(self,coord):

        return 3*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2*(-coord[1]+self.c)^4*(-coord[1]+self.d)+2*(-coord[0]+self.a)*(-coord[0]+self.b)^3*(-coord[1]+self.c)^4*(-coord[1]+self.d)

    def partialGxy3160(self,coord):

        return 3*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2*(-coord[1]+self.d)^2+2*(-coord[0]+self.a)*(-coord[0]+self.b)^3*(-coord[1]+self.d)^2

    def partialGxy3161(self,coord):

        return 3*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2*(-coord[1]+self.c)*(-coord[1]+self.d)^2+2*(-coord[0]+self.a)*(-coord[0]+self.b)^3*(-coord[1]+self.c)*(-coord[1]+self.d)^2

    def partialGxy3162(self,coord):

        return 3*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2+2*(-coord[0]+self.a)*(-coord[0]+self.b)^3*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2

    def partialGxy3163(self,coord):

        return 3*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2+2*(-coord[0]+self.a)*(-coord[0]+self.b)^3*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2

    def partialGxy3164(self,coord):

        return 3*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2*(-coord[1]+self.c)^4*(-coord[1]+self.d)^2+2*(-coord[0]+self.a)*(-coord[0]+self.b)^3*(-coord[1]+self.c)^4*(-coord[1]+self.d)^2

    def partialGxy3165(self,coord):

        return 3*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2*(-coord[1]+self.d)^3+2*(-coord[0]+self.a)*(-coord[0]+self.b)^3*(-coord[1]+self.d)^3

    def partialGxy3166(self,coord):

        return 3*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2*(-coord[1]+self.c)*(-coord[1]+self.d)^3+2*(-coord[0]+self.a)*(-coord[0]+self.b)^3*(-coord[1]+self.c)*(-coord[1]+self.d)^3

    def partialGxy3167(self,coord):

        return 3*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3+2*(-coord[0]+self.a)*(-coord[0]+self.b)^3*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3

    def partialGxy3168(self,coord):

        return 3*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2*(-coord[1]+self.c)^3*(-coord[1]+self.d)^3+2*(-coord[0]+self.a)*(-coord[0]+self.b)^3*(-coord[1]+self.c)^3*(-coord[1]+self.d)^3

    def partialGxy3169(self,coord):

        return 3*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2*(-coord[1]+self.c)^4*(-coord[1]+self.d)^3+2*(-coord[0]+self.a)*(-coord[0]+self.b)^3*(-coord[1]+self.c)^4*(-coord[1]+self.d)^3

    def partialGxy3170(self,coord):

        return 3*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2*(-coord[1]+self.d)^4+2*(-coord[0]+self.a)*(-coord[0]+self.b)^3*(-coord[1]+self.d)^4

    def partialGxy3171(self,coord):

        return 3*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2*(-coord[1]+self.c)*(-coord[1]+self.d)^4+2*(-coord[0]+self.a)*(-coord[0]+self.b)^3*(-coord[1]+self.c)*(-coord[1]+self.d)^4

    def partialGxy3172(self,coord):

        return 3*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2*(-coord[1]+self.c)^2*(-coord[1]+self.d)^4+2*(-coord[0]+self.a)*(-coord[0]+self.b)^3*(-coord[1]+self.c)^2*(-coord[1]+self.d)^4

    def partialGxy3173(self,coord):

        return 3*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2*(-coord[1]+self.c)^3*(-coord[1]+self.d)^4+2*(-coord[0]+self.a)*(-coord[0]+self.b)^3*(-coord[1]+self.c)^3*(-coord[1]+self.d)^4

    def partialGxy3174(self,coord):

        return 3*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2*(-coord[1]+self.c)^4*(-coord[1]+self.d)^4+2*(-coord[0]+self.a)*(-coord[0]+self.b)^3*(-coord[1]+self.c)^4*(-coord[1]+self.d)^4

    def partialGxy3181(self,coord):

        return 3*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2*(-coord[1]+self.c)+2*(-coord[0]+self.a)*(-coord[0]+self.b)^3*(-coord[1]+self.c)+3*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2*(-coord[1]+self.d)+2*(-coord[0]+self.a)*(-coord[0]+self.b)^3*(-coord[1]+self.d)

    def partialGxy3182(self,coord):

        return 3*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2*(-coord[1]+self.c)^2+2*(-coord[0]+self.a)*(-coord[0]+self.b)^3*(-coord[1]+self.c)^2+6*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2*(-coord[1]+self.c)*(-coord[1]+self.d)+4*(-coord[0]+self.a)*(-coord[0]+self.b)^3*(-coord[1]+self.c)*(-coord[1]+self.d)

    def partialGxy3183(self,coord):

        return 3*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2*(-coord[1]+self.c)^3+2*(-coord[0]+self.a)*(-coord[0]+self.b)^3*(-coord[1]+self.c)^3+9*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2*(-coord[1]+self.c)^2*(-coord[1]+self.d)+6*(-coord[0]+self.a)*(-coord[0]+self.b)^3*(-coord[1]+self.c)^2*(-coord[1]+self.d)

    def partialGxy3184(self,coord):

        return 3*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2*(-coord[1]+self.c)^4+2*(-coord[0]+self.a)*(-coord[0]+self.b)^3*(-coord[1]+self.c)^4+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2*(-coord[1]+self.c)^3*(-coord[1]+self.d)+8*(-coord[0]+self.a)*(-coord[0]+self.b)^3*(-coord[1]+self.c)^3*(-coord[1]+self.d)

    def partialGxy3186(self,coord):

        return 6*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2*(-coord[1]+self.c)*(-coord[1]+self.d)+4*(-coord[0]+self.a)*(-coord[0]+self.b)^3*(-coord[1]+self.c)*(-coord[1]+self.d)+3*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2*(-coord[1]+self.d)^2+2*(-coord[0]+self.a)*(-coord[0]+self.b)^3*(-coord[1]+self.d)^2

    def partialGxy3187(self,coord):

        return 6*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2*(-coord[1]+self.c)^2*(-coord[1]+self.d)+4*(-coord[0]+self.a)*(-coord[0]+self.b)^3*(-coord[1]+self.c)^2*(-coord[1]+self.d)+6*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2*(-coord[1]+self.c)*(-coord[1]+self.d)^2+4*(-coord[0]+self.a)*(-coord[0]+self.b)^3*(-coord[1]+self.c)*(-coord[1]+self.d)^2

    def partialGxy3188(self,coord):

        return 6*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2*(-coord[1]+self.c)^3*(-coord[1]+self.d)+4*(-coord[0]+self.a)*(-coord[0]+self.b)^3*(-coord[1]+self.c)^3*(-coord[1]+self.d)+9*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2+6*(-coord[0]+self.a)*(-coord[0]+self.b)^3*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2

    def partialGxy3189(self,coord):

        return 6*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2*(-coord[1]+self.c)^4*(-coord[1]+self.d)+4*(-coord[0]+self.a)*(-coord[0]+self.b)^3*(-coord[1]+self.c)^4*(-coord[1]+self.d)+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2+8*(-coord[0]+self.a)*(-coord[0]+self.b)^3*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2

    def partialGxy3191(self,coord):

        return 9*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2*(-coord[1]+self.c)*(-coord[1]+self.d)^2+6*(-coord[0]+self.a)*(-coord[0]+self.b)^3*(-coord[1]+self.c)*(-coord[1]+self.d)^2+3*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2*(-coord[1]+self.d)^3+2*(-coord[0]+self.a)*(-coord[0]+self.b)^3*(-coord[1]+self.d)^3

    def partialGxy3192(self,coord):

        return 9*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2+6*(-coord[0]+self.a)*(-coord[0]+self.b)^3*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2+6*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2*(-coord[1]+self.c)*(-coord[1]+self.d)^3+4*(-coord[0]+self.a)*(-coord[0]+self.b)^3*(-coord[1]+self.c)*(-coord[1]+self.d)^3

    def partialGxy3193(self,coord):

        return 9*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2+6*(-coord[0]+self.a)*(-coord[0]+self.b)^3*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2+9*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3+6*(-coord[0]+self.a)*(-coord[0]+self.b)^3*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3

    def partialGxy3194(self,coord):

        return 9*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2*(-coord[1]+self.c)^4*(-coord[1]+self.d)^2+6*(-coord[0]+self.a)*(-coord[0]+self.b)^3*(-coord[1]+self.c)^4*(-coord[1]+self.d)^2+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2*(-coord[1]+self.c)^3*(-coord[1]+self.d)^3+8*(-coord[0]+self.a)*(-coord[0]+self.b)^3*(-coord[1]+self.c)^3*(-coord[1]+self.d)^3

    def partialGxy3196(self,coord):

        return 12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2*(-coord[1]+self.c)*(-coord[1]+self.d)^3+8*(-coord[0]+self.a)*(-coord[0]+self.b)^3*(-coord[1]+self.c)*(-coord[1]+self.d)^3+3*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2*(-coord[1]+self.d)^4+2*(-coord[0]+self.a)*(-coord[0]+self.b)^3*(-coord[1]+self.d)^4

    def partialGxy3197(self,coord):

        return 12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3+8*(-coord[0]+self.a)*(-coord[0]+self.b)^3*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3+6*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2*(-coord[1]+self.c)*(-coord[1]+self.d)^4+4*(-coord[0]+self.a)*(-coord[0]+self.b)^3*(-coord[1]+self.c)*(-coord[1]+self.d)^4

    def partialGxy3198(self,coord):

        return 12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2*(-coord[1]+self.c)^3*(-coord[1]+self.d)^3+8*(-coord[0]+self.a)*(-coord[0]+self.b)^3*(-coord[1]+self.c)^3*(-coord[1]+self.d)^3+9*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2*(-coord[1]+self.c)^2*(-coord[1]+self.d)^4+6*(-coord[0]+self.a)*(-coord[0]+self.b)^3*(-coord[1]+self.c)^2*(-coord[1]+self.d)^4

    def partialGxy3199(self,coord):

        return 12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2*(-coord[1]+self.c)^4*(-coord[1]+self.d)^3+8*(-coord[0]+self.a)*(-coord[0]+self.b)^3*(-coord[1]+self.c)^4*(-coord[1]+self.d)^3+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2*(-coord[1]+self.c)^3*(-coord[1]+self.d)^4+8*(-coord[0]+self.a)*(-coord[0]+self.b)^3*(-coord[1]+self.c)^3*(-coord[1]+self.d)^4

    def partialGxy3212(self,coord):

        return 3*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2*(2*(-coord[1]+self.c)^2+8*(-coord[1]+self.c)*(-coord[1]+self.d)+2*(-coord[1]+self.d)^2)+2*(-coord[0]+self.a)*(-coord[0]+self.b)^3*(2*(-coord[1]+self.c)^2+8*(-coord[1]+self.c)*(-coord[1]+self.d)+2*(-coord[1]+self.d)^2)

    def partialGxy3213(self,coord):

        return 3*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2*(2*(-coord[1]+self.c)^3+12*(-coord[1]+self.c)^2*(-coord[1]+self.d)+6*(-coord[1]+self.c)*(-coord[1]+self.d)^2)+2*(-coord[0]+self.a)*(-coord[0]+self.b)^3*(2*(-coord[1]+self.c)^3+12*(-coord[1]+self.c)^2*(-coord[1]+self.d)+6*(-coord[1]+self.c)*(-coord[1]+self.d)^2)

    def partialGxy3214(self,coord):

        return 3*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2*(2*(-coord[1]+self.c)^4+16*(-coord[1]+self.c)^3*(-coord[1]+self.d)+12*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2)+2*(-coord[0]+self.a)*(-coord[0]+self.b)^3*(2*(-coord[1]+self.c)^4+16*(-coord[1]+self.c)^3*(-coord[1]+self.d)+12*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2)

    def partialGxy3217(self,coord):

        return 3*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2*(6*(-coord[1]+self.c)^2*(-coord[1]+self.d)+12*(-coord[1]+self.c)*(-coord[1]+self.d)^2+2*(-coord[1]+self.d)^3)+2*(-coord[0]+self.a)*(-coord[0]+self.b)^3*(6*(-coord[1]+self.c)^2*(-coord[1]+self.d)+12*(-coord[1]+self.c)*(-coord[1]+self.d)^2+2*(-coord[1]+self.d)^3)

    def partialGxy3218(self,coord):

        return 3*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2*(6*(-coord[1]+self.c)^3*(-coord[1]+self.d)+18*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2+6*(-coord[1]+self.c)*(-coord[1]+self.d)^3)+2*(-coord[0]+self.a)*(-coord[0]+self.b)^3*(6*(-coord[1]+self.c)^3*(-coord[1]+self.d)+18*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2+6*(-coord[1]+self.c)*(-coord[1]+self.d)^3)

    def partialGxy3219(self,coord):

        return 3*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2*(6*(-coord[1]+self.c)^4*(-coord[1]+self.d)+24*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2+12*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3)+2*(-coord[0]+self.a)*(-coord[0]+self.b)^3*(6*(-coord[1]+self.c)^4*(-coord[1]+self.d)+24*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2+12*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3)

    def partialGxy3222(self,coord):

        return 3*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2*(12*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2+16*(-coord[1]+self.c)*(-coord[1]+self.d)^3+2*(-coord[1]+self.d)^4)+2*(-coord[0]+self.a)*(-coord[0]+self.b)^3*(12*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2+16*(-coord[1]+self.c)*(-coord[1]+self.d)^3+2*(-coord[1]+self.d)^4)

    def partialGxy3223(self,coord):

        return 3*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2*(12*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2+24*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3+6*(-coord[1]+self.c)*(-coord[1]+self.d)^4)+2*(-coord[0]+self.a)*(-coord[0]+self.b)^3*(12*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2+24*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3+6*(-coord[1]+self.c)*(-coord[1]+self.d)^4)

    def partialGxy3224(self,coord):

        return 3*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2*(12*(-coord[1]+self.c)^4*(-coord[1]+self.d)^2+32*(-coord[1]+self.c)^3*(-coord[1]+self.d)^3+12*(-coord[1]+self.c)^2*(-coord[1]+self.d)^4)+2*(-coord[0]+self.a)*(-coord[0]+self.b)^3*(12*(-coord[1]+self.c)^4*(-coord[1]+self.d)^2+32*(-coord[1]+self.c)^3*(-coord[1]+self.d)^3+12*(-coord[1]+self.c)^2*(-coord[1]+self.d)^4)

    def partialGxy3225(self,coord):

        return 3*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2+3*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3

    def partialGxy3226(self,coord):

        return 3*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2*(-coord[1]+self.c)+3*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3*(-coord[1]+self.c)

    def partialGxy3227(self,coord):

        return 3*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2*(-coord[1]+self.c)^2+3*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3*(-coord[1]+self.c)^2

    def partialGxy3228(self,coord):

        return 3*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2*(-coord[1]+self.c)^3+3*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3*(-coord[1]+self.c)^3

    def partialGxy3229(self,coord):

        return 3*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2*(-coord[1]+self.c)^4+3*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3*(-coord[1]+self.c)^4

    def partialGxy3230(self,coord):

        return 3*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2*(-coord[1]+self.d)+3*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3*(-coord[1]+self.d)

    def partialGxy3231(self,coord):

        return 3*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2*(-coord[1]+self.c)*(-coord[1]+self.d)+3*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3*(-coord[1]+self.c)*(-coord[1]+self.d)

    def partialGxy3232(self,coord):

        return 3*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2*(-coord[1]+self.c)^2*(-coord[1]+self.d)+3*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3*(-coord[1]+self.c)^2*(-coord[1]+self.d)

    def partialGxy3233(self,coord):

        return 3*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2*(-coord[1]+self.c)^3*(-coord[1]+self.d)+3*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3*(-coord[1]+self.c)^3*(-coord[1]+self.d)

    def partialGxy3234(self,coord):

        return 3*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2*(-coord[1]+self.c)^4*(-coord[1]+self.d)+3*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3*(-coord[1]+self.c)^4*(-coord[1]+self.d)

    def partialGxy3235(self,coord):

        return 3*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2*(-coord[1]+self.d)^2+3*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3*(-coord[1]+self.d)^2

    def partialGxy3236(self,coord):

        return 3*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2*(-coord[1]+self.c)*(-coord[1]+self.d)^2+3*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3*(-coord[1]+self.c)*(-coord[1]+self.d)^2

    def partialGxy3237(self,coord):

        return 3*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2+3*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2

    def partialGxy3238(self,coord):

        return 3*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2+3*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2

    def partialGxy3239(self,coord):

        return 3*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2*(-coord[1]+self.c)^4*(-coord[1]+self.d)^2+3*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3*(-coord[1]+self.c)^4*(-coord[1]+self.d)^2

    def partialGxy3240(self,coord):

        return 3*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2*(-coord[1]+self.d)^3+3*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3*(-coord[1]+self.d)^3

    def partialGxy3241(self,coord):

        return 3*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2*(-coord[1]+self.c)*(-coord[1]+self.d)^3+3*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3*(-coord[1]+self.c)*(-coord[1]+self.d)^3

    def partialGxy3242(self,coord):

        return 3*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3+3*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3

    def partialGxy3243(self,coord):

        return 3*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2*(-coord[1]+self.c)^3*(-coord[1]+self.d)^3+3*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3*(-coord[1]+self.c)^3*(-coord[1]+self.d)^3

    def partialGxy3244(self,coord):

        return 3*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2*(-coord[1]+self.c)^4*(-coord[1]+self.d)^3+3*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3*(-coord[1]+self.c)^4*(-coord[1]+self.d)^3

    def partialGxy3245(self,coord):

        return 3*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2*(-coord[1]+self.d)^4+3*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3*(-coord[1]+self.d)^4

    def partialGxy3246(self,coord):

        return 3*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2*(-coord[1]+self.c)*(-coord[1]+self.d)^4+3*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3*(-coord[1]+self.c)*(-coord[1]+self.d)^4

    def partialGxy3247(self,coord):

        return 3*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2*(-coord[1]+self.c)^2*(-coord[1]+self.d)^4+3*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3*(-coord[1]+self.c)^2*(-coord[1]+self.d)^4

    def partialGxy3248(self,coord):

        return 3*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2*(-coord[1]+self.c)^3*(-coord[1]+self.d)^4+3*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3*(-coord[1]+self.c)^3*(-coord[1]+self.d)^4

    def partialGxy3249(self,coord):

        return 3*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2*(-coord[1]+self.c)^4*(-coord[1]+self.d)^4+3*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3*(-coord[1]+self.c)^4*(-coord[1]+self.d)^4

    def partialGxy3256(self,coord):

        return 3*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2*(-coord[1]+self.c)+3*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3*(-coord[1]+self.c)+3*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2*(-coord[1]+self.d)+3*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3*(-coord[1]+self.d)

    def partialGxy3257(self,coord):

        return 3*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2*(-coord[1]+self.c)^2+3*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3*(-coord[1]+self.c)^2+6*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2*(-coord[1]+self.c)*(-coord[1]+self.d)+6*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3*(-coord[1]+self.c)*(-coord[1]+self.d)

    def partialGxy3258(self,coord):

        return 3*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2*(-coord[1]+self.c)^3+3*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3*(-coord[1]+self.c)^3+9*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2*(-coord[1]+self.c)^2*(-coord[1]+self.d)+9*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3*(-coord[1]+self.c)^2*(-coord[1]+self.d)

    def partialGxy3259(self,coord):

        return 3*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2*(-coord[1]+self.c)^4+3*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3*(-coord[1]+self.c)^4+12*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2*(-coord[1]+self.c)^3*(-coord[1]+self.d)+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3*(-coord[1]+self.c)^3*(-coord[1]+self.d)

    def partialGxy3261(self,coord):

        return 6*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2*(-coord[1]+self.c)*(-coord[1]+self.d)+6*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3*(-coord[1]+self.c)*(-coord[1]+self.d)+3*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2*(-coord[1]+self.d)^2+3*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3*(-coord[1]+self.d)^2

    def partialGxy3262(self,coord):

        return 6*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2*(-coord[1]+self.c)^2*(-coord[1]+self.d)+6*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3*(-coord[1]+self.c)^2*(-coord[1]+self.d)+6*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2*(-coord[1]+self.c)*(-coord[1]+self.d)^2+6*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3*(-coord[1]+self.c)*(-coord[1]+self.d)^2

    def partialGxy3263(self,coord):

        return 6*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2*(-coord[1]+self.c)^3*(-coord[1]+self.d)+6*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3*(-coord[1]+self.c)^3*(-coord[1]+self.d)+9*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2+9*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2

    def partialGxy3264(self,coord):

        return 6*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2*(-coord[1]+self.c)^4*(-coord[1]+self.d)+6*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3*(-coord[1]+self.c)^4*(-coord[1]+self.d)+12*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2

    def partialGxy3266(self,coord):

        return 9*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2*(-coord[1]+self.c)*(-coord[1]+self.d)^2+9*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3*(-coord[1]+self.c)*(-coord[1]+self.d)^2+3*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2*(-coord[1]+self.d)^3+3*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3*(-coord[1]+self.d)^3

    def partialGxy3267(self,coord):

        return 9*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2+9*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2+6*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2*(-coord[1]+self.c)*(-coord[1]+self.d)^3+6*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3*(-coord[1]+self.c)*(-coord[1]+self.d)^3

    def partialGxy3268(self,coord):

        return 9*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2+9*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2+9*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3+9*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3

    def partialGxy3269(self,coord):

        return 9*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2*(-coord[1]+self.c)^4*(-coord[1]+self.d)^2+9*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3*(-coord[1]+self.c)^4*(-coord[1]+self.d)^2+12*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2*(-coord[1]+self.c)^3*(-coord[1]+self.d)^3+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3*(-coord[1]+self.c)^3*(-coord[1]+self.d)^3

    def partialGxy3271(self,coord):

        return 12*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2*(-coord[1]+self.c)*(-coord[1]+self.d)^3+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3*(-coord[1]+self.c)*(-coord[1]+self.d)^3+3*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2*(-coord[1]+self.d)^4+3*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3*(-coord[1]+self.d)^4

    def partialGxy3272(self,coord):

        return 12*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3+6*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2*(-coord[1]+self.c)*(-coord[1]+self.d)^4+6*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3*(-coord[1]+self.c)*(-coord[1]+self.d)^4

    def partialGxy3273(self,coord):

        return 12*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2*(-coord[1]+self.c)^3*(-coord[1]+self.d)^3+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3*(-coord[1]+self.c)^3*(-coord[1]+self.d)^3+9*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2*(-coord[1]+self.c)^2*(-coord[1]+self.d)^4+9*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3*(-coord[1]+self.c)^2*(-coord[1]+self.d)^4

    def partialGxy3274(self,coord):

        return 12*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2*(-coord[1]+self.c)^4*(-coord[1]+self.d)^3+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3*(-coord[1]+self.c)^4*(-coord[1]+self.d)^3+12*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2*(-coord[1]+self.c)^3*(-coord[1]+self.d)^4+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3*(-coord[1]+self.c)^3*(-coord[1]+self.d)^4

    def partialGxy3287(self,coord):

        return 3*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2*(2*(-coord[1]+self.c)^2+8*(-coord[1]+self.c)*(-coord[1]+self.d)+2*(-coord[1]+self.d)^2)+3*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3*(2*(-coord[1]+self.c)^2+8*(-coord[1]+self.c)*(-coord[1]+self.d)+2*(-coord[1]+self.d)^2)

    def partialGxy3288(self,coord):

        return 3*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2*(2*(-coord[1]+self.c)^3+12*(-coord[1]+self.c)^2*(-coord[1]+self.d)+6*(-coord[1]+self.c)*(-coord[1]+self.d)^2)+3*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3*(2*(-coord[1]+self.c)^3+12*(-coord[1]+self.c)^2*(-coord[1]+self.d)+6*(-coord[1]+self.c)*(-coord[1]+self.d)^2)

    def partialGxy3289(self,coord):

        return 3*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2*(2*(-coord[1]+self.c)^4+16*(-coord[1]+self.c)^3*(-coord[1]+self.d)+12*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2)+3*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3*(2*(-coord[1]+self.c)^4+16*(-coord[1]+self.c)^3*(-coord[1]+self.d)+12*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2)

    def partialGxy3292(self,coord):

        return 3*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2*(6*(-coord[1]+self.c)^2*(-coord[1]+self.d)+12*(-coord[1]+self.c)*(-coord[1]+self.d)^2+2*(-coord[1]+self.d)^3)+3*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3*(6*(-coord[1]+self.c)^2*(-coord[1]+self.d)+12*(-coord[1]+self.c)*(-coord[1]+self.d)^2+2*(-coord[1]+self.d)^3)

    def partialGxy3293(self,coord):

        return 3*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2*(6*(-coord[1]+self.c)^3*(-coord[1]+self.d)+18*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2+6*(-coord[1]+self.c)*(-coord[1]+self.d)^3)+3*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3*(6*(-coord[1]+self.c)^3*(-coord[1]+self.d)+18*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2+6*(-coord[1]+self.c)*(-coord[1]+self.d)^3)

    def partialGxy3294(self,coord):

        return 3*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2*(6*(-coord[1]+self.c)^4*(-coord[1]+self.d)+24*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2+12*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3)+3*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3*(6*(-coord[1]+self.c)^4*(-coord[1]+self.d)+24*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2+12*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3)

    def partialGxy3297(self,coord):

        return 3*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2*(12*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2+16*(-coord[1]+self.c)*(-coord[1]+self.d)^3+2*(-coord[1]+self.d)^4)+3*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3*(12*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2+16*(-coord[1]+self.c)*(-coord[1]+self.d)^3+2*(-coord[1]+self.d)^4)

    def partialGxy3298(self,coord):

        return 3*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2*(12*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2+24*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3+6*(-coord[1]+self.c)*(-coord[1]+self.d)^4)+3*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3*(12*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2+24*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3+6*(-coord[1]+self.c)*(-coord[1]+self.d)^4)

    def partialGxy3299(self,coord):

        return 3*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2*(12*(-coord[1]+self.c)^4*(-coord[1]+self.d)^2+32*(-coord[1]+self.c)^3*(-coord[1]+self.d)^3+12*(-coord[1]+self.c)^2*(-coord[1]+self.d)^4)+3*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3*(12*(-coord[1]+self.c)^4*(-coord[1]+self.d)^2+32*(-coord[1]+self.c)^3*(-coord[1]+self.d)^3+12*(-coord[1]+self.c)^2*(-coord[1]+self.d)^4)

    def partialGxy3300(self,coord):

        return 3*(-coord[0]+self.a)^4*(-coord[0]+self.b)^2+4*(-coord[0]+self.a)^3*(-coord[0]+self.b)^3

    def partialGxy3301(self,coord):

        return 3*(-coord[0]+self.a)^4*(-coord[0]+self.b)^2*(-coord[1]+self.c)+4*(-coord[0]+self.a)^3*(-coord[0]+self.b)^3*(-coord[1]+self.c)

    def partialGxy3302(self,coord):

        return 3*(-coord[0]+self.a)^4*(-coord[0]+self.b)^2*(-coord[1]+self.c)^2+4*(-coord[0]+self.a)^3*(-coord[0]+self.b)^3*(-coord[1]+self.c)^2

    def partialGxy3303(self,coord):

        return 3*(-coord[0]+self.a)^4*(-coord[0]+self.b)^2*(-coord[1]+self.c)^3+4*(-coord[0]+self.a)^3*(-coord[0]+self.b)^3*(-coord[1]+self.c)^3

    def partialGxy3304(self,coord):

        return 3*(-coord[0]+self.a)^4*(-coord[0]+self.b)^2*(-coord[1]+self.c)^4+4*(-coord[0]+self.a)^3*(-coord[0]+self.b)^3*(-coord[1]+self.c)^4

    def partialGxy3305(self,coord):

        return 3*(-coord[0]+self.a)^4*(-coord[0]+self.b)^2*(-coord[1]+self.d)+4*(-coord[0]+self.a)^3*(-coord[0]+self.b)^3*(-coord[1]+self.d)

    def partialGxy3306(self,coord):

        return 3*(-coord[0]+self.a)^4*(-coord[0]+self.b)^2*(-coord[1]+self.c)*(-coord[1]+self.d)+4*(-coord[0]+self.a)^3*(-coord[0]+self.b)^3*(-coord[1]+self.c)*(-coord[1]+self.d)

    def partialGxy3307(self,coord):

        return 3*(-coord[0]+self.a)^4*(-coord[0]+self.b)^2*(-coord[1]+self.c)^2*(-coord[1]+self.d)+4*(-coord[0]+self.a)^3*(-coord[0]+self.b)^3*(-coord[1]+self.c)^2*(-coord[1]+self.d)

    def partialGxy3308(self,coord):

        return 3*(-coord[0]+self.a)^4*(-coord[0]+self.b)^2*(-coord[1]+self.c)^3*(-coord[1]+self.d)+4*(-coord[0]+self.a)^3*(-coord[0]+self.b)^3*(-coord[1]+self.c)^3*(-coord[1]+self.d)

    def partialGxy3309(self,coord):

        return 3*(-coord[0]+self.a)^4*(-coord[0]+self.b)^2*(-coord[1]+self.c)^4*(-coord[1]+self.d)+4*(-coord[0]+self.a)^3*(-coord[0]+self.b)^3*(-coord[1]+self.c)^4*(-coord[1]+self.d)

    def partialGxy3310(self,coord):

        return 3*(-coord[0]+self.a)^4*(-coord[0]+self.b)^2*(-coord[1]+self.d)^2+4*(-coord[0]+self.a)^3*(-coord[0]+self.b)^3*(-coord[1]+self.d)^2

    def partialGxy3311(self,coord):

        return 3*(-coord[0]+self.a)^4*(-coord[0]+self.b)^2*(-coord[1]+self.c)*(-coord[1]+self.d)^2+4*(-coord[0]+self.a)^3*(-coord[0]+self.b)^3*(-coord[1]+self.c)*(-coord[1]+self.d)^2

    def partialGxy3312(self,coord):

        return 3*(-coord[0]+self.a)^4*(-coord[0]+self.b)^2*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2+4*(-coord[0]+self.a)^3*(-coord[0]+self.b)^3*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2

    def partialGxy3313(self,coord):

        return 3*(-coord[0]+self.a)^4*(-coord[0]+self.b)^2*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2+4*(-coord[0]+self.a)^3*(-coord[0]+self.b)^3*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2

    def partialGxy3314(self,coord):

        return 3*(-coord[0]+self.a)^4*(-coord[0]+self.b)^2*(-coord[1]+self.c)^4*(-coord[1]+self.d)^2+4*(-coord[0]+self.a)^3*(-coord[0]+self.b)^3*(-coord[1]+self.c)^4*(-coord[1]+self.d)^2

    def partialGxy3315(self,coord):

        return 3*(-coord[0]+self.a)^4*(-coord[0]+self.b)^2*(-coord[1]+self.d)^3+4*(-coord[0]+self.a)^3*(-coord[0]+self.b)^3*(-coord[1]+self.d)^3

    def partialGxy3316(self,coord):

        return 3*(-coord[0]+self.a)^4*(-coord[0]+self.b)^2*(-coord[1]+self.c)*(-coord[1]+self.d)^3+4*(-coord[0]+self.a)^3*(-coord[0]+self.b)^3*(-coord[1]+self.c)*(-coord[1]+self.d)^3

    def partialGxy3317(self,coord):

        return 3*(-coord[0]+self.a)^4*(-coord[0]+self.b)^2*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3+4*(-coord[0]+self.a)^3*(-coord[0]+self.b)^3*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3

    def partialGxy3318(self,coord):

        return 3*(-coord[0]+self.a)^4*(-coord[0]+self.b)^2*(-coord[1]+self.c)^3*(-coord[1]+self.d)^3+4*(-coord[0]+self.a)^3*(-coord[0]+self.b)^3*(-coord[1]+self.c)^3*(-coord[1]+self.d)^3

    def partialGxy3319(self,coord):

        return 3*(-coord[0]+self.a)^4*(-coord[0]+self.b)^2*(-coord[1]+self.c)^4*(-coord[1]+self.d)^3+4*(-coord[0]+self.a)^3*(-coord[0]+self.b)^3*(-coord[1]+self.c)^4*(-coord[1]+self.d)^3

    def partialGxy3320(self,coord):

        return 3*(-coord[0]+self.a)^4*(-coord[0]+self.b)^2*(-coord[1]+self.d)^4+4*(-coord[0]+self.a)^3*(-coord[0]+self.b)^3*(-coord[1]+self.d)^4

    def partialGxy3321(self,coord):

        return 3*(-coord[0]+self.a)^4*(-coord[0]+self.b)^2*(-coord[1]+self.c)*(-coord[1]+self.d)^4+4*(-coord[0]+self.a)^3*(-coord[0]+self.b)^3*(-coord[1]+self.c)*(-coord[1]+self.d)^4

    def partialGxy3322(self,coord):

        return 3*(-coord[0]+self.a)^4*(-coord[0]+self.b)^2*(-coord[1]+self.c)^2*(-coord[1]+self.d)^4+4*(-coord[0]+self.a)^3*(-coord[0]+self.b)^3*(-coord[1]+self.c)^2*(-coord[1]+self.d)^4

    def partialGxy3323(self,coord):

        return 3*(-coord[0]+self.a)^4*(-coord[0]+self.b)^2*(-coord[1]+self.c)^3*(-coord[1]+self.d)^4+4*(-coord[0]+self.a)^3*(-coord[0]+self.b)^3*(-coord[1]+self.c)^3*(-coord[1]+self.d)^4

    def partialGxy3324(self,coord):

        return 3*(-coord[0]+self.a)^4*(-coord[0]+self.b)^2*(-coord[1]+self.c)^4*(-coord[1]+self.d)^4+4*(-coord[0]+self.a)^3*(-coord[0]+self.b)^3*(-coord[1]+self.c)^4*(-coord[1]+self.d)^4

    def partialGxy3331(self,coord):

        return 3*(-coord[0]+self.a)^4*(-coord[0]+self.b)^2*(-coord[1]+self.c)+4*(-coord[0]+self.a)^3*(-coord[0]+self.b)^3*(-coord[1]+self.c)+3*(-coord[0]+self.a)^4*(-coord[0]+self.b)^2*(-coord[1]+self.d)+4*(-coord[0]+self.a)^3*(-coord[0]+self.b)^3*(-coord[1]+self.d)

    def partialGxy3332(self,coord):

        return 3*(-coord[0]+self.a)^4*(-coord[0]+self.b)^2*(-coord[1]+self.c)^2+4*(-coord[0]+self.a)^3*(-coord[0]+self.b)^3*(-coord[1]+self.c)^2+6*(-coord[0]+self.a)^4*(-coord[0]+self.b)^2*(-coord[1]+self.c)*(-coord[1]+self.d)+8*(-coord[0]+self.a)^3*(-coord[0]+self.b)^3*(-coord[1]+self.c)*(-coord[1]+self.d)

    def partialGxy3333(self,coord):

        return 3*(-coord[0]+self.a)^4*(-coord[0]+self.b)^2*(-coord[1]+self.c)^3+4*(-coord[0]+self.a)^3*(-coord[0]+self.b)^3*(-coord[1]+self.c)^3+9*(-coord[0]+self.a)^4*(-coord[0]+self.b)^2*(-coord[1]+self.c)^2*(-coord[1]+self.d)+12*(-coord[0]+self.a)^3*(-coord[0]+self.b)^3*(-coord[1]+self.c)^2*(-coord[1]+self.d)

    def partialGxy3334(self,coord):

        return 3*(-coord[0]+self.a)^4*(-coord[0]+self.b)^2*(-coord[1]+self.c)^4+4*(-coord[0]+self.a)^3*(-coord[0]+self.b)^3*(-coord[1]+self.c)^4+12*(-coord[0]+self.a)^4*(-coord[0]+self.b)^2*(-coord[1]+self.c)^3*(-coord[1]+self.d)+16*(-coord[0]+self.a)^3*(-coord[0]+self.b)^3*(-coord[1]+self.c)^3*(-coord[1]+self.d)

    def partialGxy3336(self,coord):

        return 6*(-coord[0]+self.a)^4*(-coord[0]+self.b)^2*(-coord[1]+self.c)*(-coord[1]+self.d)+8*(-coord[0]+self.a)^3*(-coord[0]+self.b)^3*(-coord[1]+self.c)*(-coord[1]+self.d)+3*(-coord[0]+self.a)^4*(-coord[0]+self.b)^2*(-coord[1]+self.d)^2+4*(-coord[0]+self.a)^3*(-coord[0]+self.b)^3*(-coord[1]+self.d)^2

    def partialGxy3337(self,coord):

        return 6*(-coord[0]+self.a)^4*(-coord[0]+self.b)^2*(-coord[1]+self.c)^2*(-coord[1]+self.d)+8*(-coord[0]+self.a)^3*(-coord[0]+self.b)^3*(-coord[1]+self.c)^2*(-coord[1]+self.d)+6*(-coord[0]+self.a)^4*(-coord[0]+self.b)^2*(-coord[1]+self.c)*(-coord[1]+self.d)^2+8*(-coord[0]+self.a)^3*(-coord[0]+self.b)^3*(-coord[1]+self.c)*(-coord[1]+self.d)^2

    def partialGxy3338(self,coord):

        return 6*(-coord[0]+self.a)^4*(-coord[0]+self.b)^2*(-coord[1]+self.c)^3*(-coord[1]+self.d)+8*(-coord[0]+self.a)^3*(-coord[0]+self.b)^3*(-coord[1]+self.c)^3*(-coord[1]+self.d)+9*(-coord[0]+self.a)^4*(-coord[0]+self.b)^2*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2+12*(-coord[0]+self.a)^3*(-coord[0]+self.b)^3*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2

    def partialGxy3339(self,coord):

        return 6*(-coord[0]+self.a)^4*(-coord[0]+self.b)^2*(-coord[1]+self.c)^4*(-coord[1]+self.d)+8*(-coord[0]+self.a)^3*(-coord[0]+self.b)^3*(-coord[1]+self.c)^4*(-coord[1]+self.d)+12*(-coord[0]+self.a)^4*(-coord[0]+self.b)^2*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2+16*(-coord[0]+self.a)^3*(-coord[0]+self.b)^3*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2

    def partialGxy3341(self,coord):

        return 9*(-coord[0]+self.a)^4*(-coord[0]+self.b)^2*(-coord[1]+self.c)*(-coord[1]+self.d)^2+12*(-coord[0]+self.a)^3*(-coord[0]+self.b)^3*(-coord[1]+self.c)*(-coord[1]+self.d)^2+3*(-coord[0]+self.a)^4*(-coord[0]+self.b)^2*(-coord[1]+self.d)^3+4*(-coord[0]+self.a)^3*(-coord[0]+self.b)^3*(-coord[1]+self.d)^3

    def partialGxy3342(self,coord):

        return 9*(-coord[0]+self.a)^4*(-coord[0]+self.b)^2*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2+12*(-coord[0]+self.a)^3*(-coord[0]+self.b)^3*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2+6*(-coord[0]+self.a)^4*(-coord[0]+self.b)^2*(-coord[1]+self.c)*(-coord[1]+self.d)^3+8*(-coord[0]+self.a)^3*(-coord[0]+self.b)^3*(-coord[1]+self.c)*(-coord[1]+self.d)^3

    def partialGxy3343(self,coord):

        return 9*(-coord[0]+self.a)^4*(-coord[0]+self.b)^2*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2+12*(-coord[0]+self.a)^3*(-coord[0]+self.b)^3*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2+9*(-coord[0]+self.a)^4*(-coord[0]+self.b)^2*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3+12*(-coord[0]+self.a)^3*(-coord[0]+self.b)^3*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3

    def partialGxy3344(self,coord):

        return 9*(-coord[0]+self.a)^4*(-coord[0]+self.b)^2*(-coord[1]+self.c)^4*(-coord[1]+self.d)^2+12*(-coord[0]+self.a)^3*(-coord[0]+self.b)^3*(-coord[1]+self.c)^4*(-coord[1]+self.d)^2+12*(-coord[0]+self.a)^4*(-coord[0]+self.b)^2*(-coord[1]+self.c)^3*(-coord[1]+self.d)^3+16*(-coord[0]+self.a)^3*(-coord[0]+self.b)^3*(-coord[1]+self.c)^3*(-coord[1]+self.d)^3

    def partialGxy3346(self,coord):

        return 12*(-coord[0]+self.a)^4*(-coord[0]+self.b)^2*(-coord[1]+self.c)*(-coord[1]+self.d)^3+16*(-coord[0]+self.a)^3*(-coord[0]+self.b)^3*(-coord[1]+self.c)*(-coord[1]+self.d)^3+3*(-coord[0]+self.a)^4*(-coord[0]+self.b)^2*(-coord[1]+self.d)^4+4*(-coord[0]+self.a)^3*(-coord[0]+self.b)^3*(-coord[1]+self.d)^4

    def partialGxy3347(self,coord):

        return 12*(-coord[0]+self.a)^4*(-coord[0]+self.b)^2*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3+16*(-coord[0]+self.a)^3*(-coord[0]+self.b)^3*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3+6*(-coord[0]+self.a)^4*(-coord[0]+self.b)^2*(-coord[1]+self.c)*(-coord[1]+self.d)^4+8*(-coord[0]+self.a)^3*(-coord[0]+self.b)^3*(-coord[1]+self.c)*(-coord[1]+self.d)^4

    def partialGxy3348(self,coord):

        return 12*(-coord[0]+self.a)^4*(-coord[0]+self.b)^2*(-coord[1]+self.c)^3*(-coord[1]+self.d)^3+16*(-coord[0]+self.a)^3*(-coord[0]+self.b)^3*(-coord[1]+self.c)^3*(-coord[1]+self.d)^3+9*(-coord[0]+self.a)^4*(-coord[0]+self.b)^2*(-coord[1]+self.c)^2*(-coord[1]+self.d)^4+12*(-coord[0]+self.a)^3*(-coord[0]+self.b)^3*(-coord[1]+self.c)^2*(-coord[1]+self.d)^4

    def partialGxy3349(self,coord):

        return 12*(-coord[0]+self.a)^4*(-coord[0]+self.b)^2*(-coord[1]+self.c)^4*(-coord[1]+self.d)^3+16*(-coord[0]+self.a)^3*(-coord[0]+self.b)^3*(-coord[1]+self.c)^4*(-coord[1]+self.d)^3+12*(-coord[0]+self.a)^4*(-coord[0]+self.b)^2*(-coord[1]+self.c)^3*(-coord[1]+self.d)^4+16*(-coord[0]+self.a)^3*(-coord[0]+self.b)^3*(-coord[1]+self.c)^3*(-coord[1]+self.d)^4

    def partialGxy3362(self,coord):

        return 3*(-coord[0]+self.a)^4*(-coord[0]+self.b)^2*(2*(-coord[1]+self.c)^2+8*(-coord[1]+self.c)*(-coord[1]+self.d)+2*(-coord[1]+self.d)^2)+4*(-coord[0]+self.a)^3*(-coord[0]+self.b)^3*(2*(-coord[1]+self.c)^2+8*(-coord[1]+self.c)*(-coord[1]+self.d)+2*(-coord[1]+self.d)^2)

    def partialGxy3363(self,coord):

        return 3*(-coord[0]+self.a)^4*(-coord[0]+self.b)^2*(2*(-coord[1]+self.c)^3+12*(-coord[1]+self.c)^2*(-coord[1]+self.d)+6*(-coord[1]+self.c)*(-coord[1]+self.d)^2)+4*(-coord[0]+self.a)^3*(-coord[0]+self.b)^3*(2*(-coord[1]+self.c)^3+12*(-coord[1]+self.c)^2*(-coord[1]+self.d)+6*(-coord[1]+self.c)*(-coord[1]+self.d)^2)

    def partialGxy3364(self,coord):

        return 3*(-coord[0]+self.a)^4*(-coord[0]+self.b)^2*(2*(-coord[1]+self.c)^4+16*(-coord[1]+self.c)^3*(-coord[1]+self.d)+12*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2)+4*(-coord[0]+self.a)^3*(-coord[0]+self.b)^3*(2*(-coord[1]+self.c)^4+16*(-coord[1]+self.c)^3*(-coord[1]+self.d)+12*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2)

    def partialGxy3367(self,coord):

        return 3*(-coord[0]+self.a)^4*(-coord[0]+self.b)^2*(6*(-coord[1]+self.c)^2*(-coord[1]+self.d)+12*(-coord[1]+self.c)*(-coord[1]+self.d)^2+2*(-coord[1]+self.d)^3)+4*(-coord[0]+self.a)^3*(-coord[0]+self.b)^3*(6*(-coord[1]+self.c)^2*(-coord[1]+self.d)+12*(-coord[1]+self.c)*(-coord[1]+self.d)^2+2*(-coord[1]+self.d)^3)

    def partialGxy3368(self,coord):

        return 3*(-coord[0]+self.a)^4*(-coord[0]+self.b)^2*(6*(-coord[1]+self.c)^3*(-coord[1]+self.d)+18*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2+6*(-coord[1]+self.c)*(-coord[1]+self.d)^3)+4*(-coord[0]+self.a)^3*(-coord[0]+self.b)^3*(6*(-coord[1]+self.c)^3*(-coord[1]+self.d)+18*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2+6*(-coord[1]+self.c)*(-coord[1]+self.d)^3)

    def partialGxy3369(self,coord):

        return 3*(-coord[0]+self.a)^4*(-coord[0]+self.b)^2*(6*(-coord[1]+self.c)^4*(-coord[1]+self.d)+24*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2+12*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3)+4*(-coord[0]+self.a)^3*(-coord[0]+self.b)^3*(6*(-coord[1]+self.c)^4*(-coord[1]+self.d)+24*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2+12*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3)

    def partialGxy3372(self,coord):

        return 3*(-coord[0]+self.a)^4*(-coord[0]+self.b)^2*(12*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2+16*(-coord[1]+self.c)*(-coord[1]+self.d)^3+2*(-coord[1]+self.d)^4)+4*(-coord[0]+self.a)^3*(-coord[0]+self.b)^3*(12*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2+16*(-coord[1]+self.c)*(-coord[1]+self.d)^3+2*(-coord[1]+self.d)^4)

    def partialGxy3373(self,coord):

        return 3*(-coord[0]+self.a)^4*(-coord[0]+self.b)^2*(12*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2+24*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3+6*(-coord[1]+self.c)*(-coord[1]+self.d)^4)+4*(-coord[0]+self.a)^3*(-coord[0]+self.b)^3*(12*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2+24*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3+6*(-coord[1]+self.c)*(-coord[1]+self.d)^4)

    def partialGxy3374(self,coord):

        return 3*(-coord[0]+self.a)^4*(-coord[0]+self.b)^2*(12*(-coord[1]+self.c)^4*(-coord[1]+self.d)^2+32*(-coord[1]+self.c)^3*(-coord[1]+self.d)^3+12*(-coord[1]+self.c)^2*(-coord[1]+self.d)^4)+4*(-coord[0]+self.a)^3*(-coord[0]+self.b)^3*(12*(-coord[1]+self.c)^4*(-coord[1]+self.d)^2+32*(-coord[1]+self.c)^3*(-coord[1]+self.d)^3+12*(-coord[1]+self.c)^2*(-coord[1]+self.d)^4)

    def partialGxy3450(self,coord):

        return 4*(-coord[0]+self.a)*(-coord[0]+self.b)^3+(-coord[0]+self.b)^4

    def partialGxy3451(self,coord):

        return 4*(-coord[0]+self.a)*(-coord[0]+self.b)^3*(-coord[1]+self.c)+(-coord[0]+self.b)^4*(-coord[1]+self.c)

    def partialGxy3452(self,coord):

        return 4*(-coord[0]+self.a)*(-coord[0]+self.b)^3*(-coord[1]+self.c)^2+(-coord[0]+self.b)^4*(-coord[1]+self.c)^2

    def partialGxy3453(self,coord):

        return 4*(-coord[0]+self.a)*(-coord[0]+self.b)^3*(-coord[1]+self.c)^3+(-coord[0]+self.b)^4*(-coord[1]+self.c)^3

    def partialGxy3454(self,coord):

        return 4*(-coord[0]+self.a)*(-coord[0]+self.b)^3*(-coord[1]+self.c)^4+(-coord[0]+self.b)^4*(-coord[1]+self.c)^4

    def partialGxy3455(self,coord):

        return 4*(-coord[0]+self.a)*(-coord[0]+self.b)^3*(-coord[1]+self.d)+(-coord[0]+self.b)^4*(-coord[1]+self.d)

    def partialGxy3456(self,coord):

        return 4*(-coord[0]+self.a)*(-coord[0]+self.b)^3*(-coord[1]+self.c)*(-coord[1]+self.d)+(-coord[0]+self.b)^4*(-coord[1]+self.c)*(-coord[1]+self.d)

    def partialGxy3457(self,coord):

        return 4*(-coord[0]+self.a)*(-coord[0]+self.b)^3*(-coord[1]+self.c)^2*(-coord[1]+self.d)+(-coord[0]+self.b)^4*(-coord[1]+self.c)^2*(-coord[1]+self.d)

    def partialGxy3458(self,coord):

        return 4*(-coord[0]+self.a)*(-coord[0]+self.b)^3*(-coord[1]+self.c)^3*(-coord[1]+self.d)+(-coord[0]+self.b)^4*(-coord[1]+self.c)^3*(-coord[1]+self.d)

    def partialGxy3459(self,coord):

        return 4*(-coord[0]+self.a)*(-coord[0]+self.b)^3*(-coord[1]+self.c)^4*(-coord[1]+self.d)+(-coord[0]+self.b)^4*(-coord[1]+self.c)^4*(-coord[1]+self.d)

    def partialGxy3460(self,coord):

        return 4*(-coord[0]+self.a)*(-coord[0]+self.b)^3*(-coord[1]+self.d)^2+(-coord[0]+self.b)^4*(-coord[1]+self.d)^2

    def partialGxy3461(self,coord):

        return 4*(-coord[0]+self.a)*(-coord[0]+self.b)^3*(-coord[1]+self.c)*(-coord[1]+self.d)^2+(-coord[0]+self.b)^4*(-coord[1]+self.c)*(-coord[1]+self.d)^2

    def partialGxy3462(self,coord):

        return 4*(-coord[0]+self.a)*(-coord[0]+self.b)^3*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2+(-coord[0]+self.b)^4*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2

    def partialGxy3463(self,coord):

        return 4*(-coord[0]+self.a)*(-coord[0]+self.b)^3*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2+(-coord[0]+self.b)^4*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2

    def partialGxy3464(self,coord):

        return 4*(-coord[0]+self.a)*(-coord[0]+self.b)^3*(-coord[1]+self.c)^4*(-coord[1]+self.d)^2+(-coord[0]+self.b)^4*(-coord[1]+self.c)^4*(-coord[1]+self.d)^2

    def partialGxy3465(self,coord):

        return 4*(-coord[0]+self.a)*(-coord[0]+self.b)^3*(-coord[1]+self.d)^3+(-coord[0]+self.b)^4*(-coord[1]+self.d)^3

    def partialGxy3466(self,coord):

        return 4*(-coord[0]+self.a)*(-coord[0]+self.b)^3*(-coord[1]+self.c)*(-coord[1]+self.d)^3+(-coord[0]+self.b)^4*(-coord[1]+self.c)*(-coord[1]+self.d)^3

    def partialGxy3467(self,coord):

        return 4*(-coord[0]+self.a)*(-coord[0]+self.b)^3*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3+(-coord[0]+self.b)^4*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3

    def partialGxy3468(self,coord):

        return 4*(-coord[0]+self.a)*(-coord[0]+self.b)^3*(-coord[1]+self.c)^3*(-coord[1]+self.d)^3+(-coord[0]+self.b)^4*(-coord[1]+self.c)^3*(-coord[1]+self.d)^3

    def partialGxy3469(self,coord):

        return 4*(-coord[0]+self.a)*(-coord[0]+self.b)^3*(-coord[1]+self.c)^4*(-coord[1]+self.d)^3+(-coord[0]+self.b)^4*(-coord[1]+self.c)^4*(-coord[1]+self.d)^3

    def partialGxy3470(self,coord):

        return 4*(-coord[0]+self.a)*(-coord[0]+self.b)^3*(-coord[1]+self.d)^4+(-coord[0]+self.b)^4*(-coord[1]+self.d)^4

    def partialGxy3471(self,coord):

        return 4*(-coord[0]+self.a)*(-coord[0]+self.b)^3*(-coord[1]+self.c)*(-coord[1]+self.d)^4+(-coord[0]+self.b)^4*(-coord[1]+self.c)*(-coord[1]+self.d)^4

    def partialGxy3472(self,coord):

        return 4*(-coord[0]+self.a)*(-coord[0]+self.b)^3*(-coord[1]+self.c)^2*(-coord[1]+self.d)^4+(-coord[0]+self.b)^4*(-coord[1]+self.c)^2*(-coord[1]+self.d)^4

    def partialGxy3473(self,coord):

        return 4*(-coord[0]+self.a)*(-coord[0]+self.b)^3*(-coord[1]+self.c)^3*(-coord[1]+self.d)^4+(-coord[0]+self.b)^4*(-coord[1]+self.c)^3*(-coord[1]+self.d)^4

    def partialGxy3474(self,coord):

        return 4*(-coord[0]+self.a)*(-coord[0]+self.b)^3*(-coord[1]+self.c)^4*(-coord[1]+self.d)^4+(-coord[0]+self.b)^4*(-coord[1]+self.c)^4*(-coord[1]+self.d)^4

    def partialGxy3481(self,coord):

        return 4*(-coord[0]+self.a)*(-coord[0]+self.b)^3*(-coord[1]+self.c)+(-coord[0]+self.b)^4*(-coord[1]+self.c)+4*(-coord[0]+self.a)*(-coord[0]+self.b)^3*(-coord[1]+self.d)+(-coord[0]+self.b)^4*(-coord[1]+self.d)

    def partialGxy3482(self,coord):

        return 4*(-coord[0]+self.a)*(-coord[0]+self.b)^3*(-coord[1]+self.c)^2+(-coord[0]+self.b)^4*(-coord[1]+self.c)^2+8*(-coord[0]+self.a)*(-coord[0]+self.b)^3*(-coord[1]+self.c)*(-coord[1]+self.d)+2*(-coord[0]+self.b)^4*(-coord[1]+self.c)*(-coord[1]+self.d)

    def partialGxy3483(self,coord):

        return 4*(-coord[0]+self.a)*(-coord[0]+self.b)^3*(-coord[1]+self.c)^3+(-coord[0]+self.b)^4*(-coord[1]+self.c)^3+12*(-coord[0]+self.a)*(-coord[0]+self.b)^3*(-coord[1]+self.c)^2*(-coord[1]+self.d)+3*(-coord[0]+self.b)^4*(-coord[1]+self.c)^2*(-coord[1]+self.d)

    def partialGxy3484(self,coord):

        return 4*(-coord[0]+self.a)*(-coord[0]+self.b)^3*(-coord[1]+self.c)^4+(-coord[0]+self.b)^4*(-coord[1]+self.c)^4+16*(-coord[0]+self.a)*(-coord[0]+self.b)^3*(-coord[1]+self.c)^3*(-coord[1]+self.d)+4*(-coord[0]+self.b)^4*(-coord[1]+self.c)^3*(-coord[1]+self.d)

    def partialGxy3486(self,coord):

        return 8*(-coord[0]+self.a)*(-coord[0]+self.b)^3*(-coord[1]+self.c)*(-coord[1]+self.d)+2*(-coord[0]+self.b)^4*(-coord[1]+self.c)*(-coord[1]+self.d)+4*(-coord[0]+self.a)*(-coord[0]+self.b)^3*(-coord[1]+self.d)^2+(-coord[0]+self.b)^4*(-coord[1]+self.d)^2

    def partialGxy3487(self,coord):

        return 8*(-coord[0]+self.a)*(-coord[0]+self.b)^3*(-coord[1]+self.c)^2*(-coord[1]+self.d)+2*(-coord[0]+self.b)^4*(-coord[1]+self.c)^2*(-coord[1]+self.d)+8*(-coord[0]+self.a)*(-coord[0]+self.b)^3*(-coord[1]+self.c)*(-coord[1]+self.d)^2+2*(-coord[0]+self.b)^4*(-coord[1]+self.c)*(-coord[1]+self.d)^2

    def partialGxy3488(self,coord):

        return 8*(-coord[0]+self.a)*(-coord[0]+self.b)^3*(-coord[1]+self.c)^3*(-coord[1]+self.d)+2*(-coord[0]+self.b)^4*(-coord[1]+self.c)^3*(-coord[1]+self.d)+12*(-coord[0]+self.a)*(-coord[0]+self.b)^3*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2+3*(-coord[0]+self.b)^4*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2

    def partialGxy3489(self,coord):

        return 8*(-coord[0]+self.a)*(-coord[0]+self.b)^3*(-coord[1]+self.c)^4*(-coord[1]+self.d)+2*(-coord[0]+self.b)^4*(-coord[1]+self.c)^4*(-coord[1]+self.d)+16*(-coord[0]+self.a)*(-coord[0]+self.b)^3*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2+4*(-coord[0]+self.b)^4*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2

    def partialGxy3491(self,coord):

        return 12*(-coord[0]+self.a)*(-coord[0]+self.b)^3*(-coord[1]+self.c)*(-coord[1]+self.d)^2+3*(-coord[0]+self.b)^4*(-coord[1]+self.c)*(-coord[1]+self.d)^2+4*(-coord[0]+self.a)*(-coord[0]+self.b)^3*(-coord[1]+self.d)^3+(-coord[0]+self.b)^4*(-coord[1]+self.d)^3

    def partialGxy3492(self,coord):

        return 12*(-coord[0]+self.a)*(-coord[0]+self.b)^3*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2+3*(-coord[0]+self.b)^4*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2+8*(-coord[0]+self.a)*(-coord[0]+self.b)^3*(-coord[1]+self.c)*(-coord[1]+self.d)^3+2*(-coord[0]+self.b)^4*(-coord[1]+self.c)*(-coord[1]+self.d)^3

    def partialGxy3493(self,coord):

        return 12*(-coord[0]+self.a)*(-coord[0]+self.b)^3*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2+3*(-coord[0]+self.b)^4*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2+12*(-coord[0]+self.a)*(-coord[0]+self.b)^3*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3+3*(-coord[0]+self.b)^4*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3

    def partialGxy3494(self,coord):

        return 12*(-coord[0]+self.a)*(-coord[0]+self.b)^3*(-coord[1]+self.c)^4*(-coord[1]+self.d)^2+3*(-coord[0]+self.b)^4*(-coord[1]+self.c)^4*(-coord[1]+self.d)^2+16*(-coord[0]+self.a)*(-coord[0]+self.b)^3*(-coord[1]+self.c)^3*(-coord[1]+self.d)^3+4*(-coord[0]+self.b)^4*(-coord[1]+self.c)^3*(-coord[1]+self.d)^3

    def partialGxy3496(self,coord):

        return 16*(-coord[0]+self.a)*(-coord[0]+self.b)^3*(-coord[1]+self.c)*(-coord[1]+self.d)^3+4*(-coord[0]+self.b)^4*(-coord[1]+self.c)*(-coord[1]+self.d)^3+4*(-coord[0]+self.a)*(-coord[0]+self.b)^3*(-coord[1]+self.d)^4+(-coord[0]+self.b)^4*(-coord[1]+self.d)^4

    def partialGxy3497(self,coord):

        return 16*(-coord[0]+self.a)*(-coord[0]+self.b)^3*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3+4*(-coord[0]+self.b)^4*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3+8*(-coord[0]+self.a)*(-coord[0]+self.b)^3*(-coord[1]+self.c)*(-coord[1]+self.d)^4+2*(-coord[0]+self.b)^4*(-coord[1]+self.c)*(-coord[1]+self.d)^4

    def partialGxy3498(self,coord):

        return 16*(-coord[0]+self.a)*(-coord[0]+self.b)^3*(-coord[1]+self.c)^3*(-coord[1]+self.d)^3+4*(-coord[0]+self.b)^4*(-coord[1]+self.c)^3*(-coord[1]+self.d)^3+12*(-coord[0]+self.a)*(-coord[0]+self.b)^3*(-coord[1]+self.c)^2*(-coord[1]+self.d)^4+3*(-coord[0]+self.b)^4*(-coord[1]+self.c)^2*(-coord[1]+self.d)^4

    def partialGxy3499(self,coord):

        return 16*(-coord[0]+self.a)*(-coord[0]+self.b)^3*(-coord[1]+self.c)^4*(-coord[1]+self.d)^3+4*(-coord[0]+self.b)^4*(-coord[1]+self.c)^4*(-coord[1]+self.d)^3+16*(-coord[0]+self.a)*(-coord[0]+self.b)^3*(-coord[1]+self.c)^3*(-coord[1]+self.d)^4+4*(-coord[0]+self.b)^4*(-coord[1]+self.c)^3*(-coord[1]+self.d)^4

    def partialGxy3512(self,coord):

        return 4*(-coord[0]+self.a)*(-coord[0]+self.b)^3*(2*(-coord[1]+self.c)^2+8*(-coord[1]+self.c)*(-coord[1]+self.d)+2*(-coord[1]+self.d)^2)+(-coord[0]+self.b)^4*(2*(-coord[1]+self.c)^2+8*(-coord[1]+self.c)*(-coord[1]+self.d)+2*(-coord[1]+self.d)^2)

    def partialGxy3513(self,coord):

        return 4*(-coord[0]+self.a)*(-coord[0]+self.b)^3*(2*(-coord[1]+self.c)^3+12*(-coord[1]+self.c)^2*(-coord[1]+self.d)+6*(-coord[1]+self.c)*(-coord[1]+self.d)^2)+(-coord[0]+self.b)^4*(2*(-coord[1]+self.c)^3+12*(-coord[1]+self.c)^2*(-coord[1]+self.d)+6*(-coord[1]+self.c)*(-coord[1]+self.d)^2)

    def partialGxy3514(self,coord):

        return 4*(-coord[0]+self.a)*(-coord[0]+self.b)^3*(2*(-coord[1]+self.c)^4+16*(-coord[1]+self.c)^3*(-coord[1]+self.d)+12*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2)+(-coord[0]+self.b)^4*(2*(-coord[1]+self.c)^4+16*(-coord[1]+self.c)^3*(-coord[1]+self.d)+12*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2)

    def partialGxy3517(self,coord):

        return 4*(-coord[0]+self.a)*(-coord[0]+self.b)^3*(6*(-coord[1]+self.c)^2*(-coord[1]+self.d)+12*(-coord[1]+self.c)*(-coord[1]+self.d)^2+2*(-coord[1]+self.d)^3)+(-coord[0]+self.b)^4*(6*(-coord[1]+self.c)^2*(-coord[1]+self.d)+12*(-coord[1]+self.c)*(-coord[1]+self.d)^2+2*(-coord[1]+self.d)^3)

    def partialGxy3518(self,coord):

        return 4*(-coord[0]+self.a)*(-coord[0]+self.b)^3*(6*(-coord[1]+self.c)^3*(-coord[1]+self.d)+18*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2+6*(-coord[1]+self.c)*(-coord[1]+self.d)^3)+(-coord[0]+self.b)^4*(6*(-coord[1]+self.c)^3*(-coord[1]+self.d)+18*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2+6*(-coord[1]+self.c)*(-coord[1]+self.d)^3)

    def partialGxy3519(self,coord):

        return 4*(-coord[0]+self.a)*(-coord[0]+self.b)^3*(6*(-coord[1]+self.c)^4*(-coord[1]+self.d)+24*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2+12*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3)+(-coord[0]+self.b)^4*(6*(-coord[1]+self.c)^4*(-coord[1]+self.d)+24*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2+12*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3)

    def partialGxy3522(self,coord):

        return 4*(-coord[0]+self.a)*(-coord[0]+self.b)^3*(12*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2+16*(-coord[1]+self.c)*(-coord[1]+self.d)^3+2*(-coord[1]+self.d)^4)+(-coord[0]+self.b)^4*(12*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2+16*(-coord[1]+self.c)*(-coord[1]+self.d)^3+2*(-coord[1]+self.d)^4)

    def partialGxy3523(self,coord):

        return 4*(-coord[0]+self.a)*(-coord[0]+self.b)^3*(12*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2+24*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3+6*(-coord[1]+self.c)*(-coord[1]+self.d)^4)+(-coord[0]+self.b)^4*(12*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2+24*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3+6*(-coord[1]+self.c)*(-coord[1]+self.d)^4)

    def partialGxy3524(self,coord):

        return 4*(-coord[0]+self.a)*(-coord[0]+self.b)^3*(12*(-coord[1]+self.c)^4*(-coord[1]+self.d)^2+32*(-coord[1]+self.c)^3*(-coord[1]+self.d)^3+12*(-coord[1]+self.c)^2*(-coord[1]+self.d)^4)+(-coord[0]+self.b)^4*(12*(-coord[1]+self.c)^4*(-coord[1]+self.d)^2+32*(-coord[1]+self.c)^3*(-coord[1]+self.d)^3+12*(-coord[1]+self.c)^2*(-coord[1]+self.d)^4)

    def partialGxy3525(self,coord):

        return 4*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3+2*(-coord[0]+self.a)*(-coord[0]+self.b)^4

    def partialGxy3526(self,coord):

        return 4*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3*(-coord[1]+self.c)+2*(-coord[0]+self.a)*(-coord[0]+self.b)^4*(-coord[1]+self.c)

    def partialGxy3527(self,coord):

        return 4*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3*(-coord[1]+self.c)^2+2*(-coord[0]+self.a)*(-coord[0]+self.b)^4*(-coord[1]+self.c)^2

    def partialGxy3528(self,coord):

        return 4*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3*(-coord[1]+self.c)^3+2*(-coord[0]+self.a)*(-coord[0]+self.b)^4*(-coord[1]+self.c)^3

    def partialGxy3529(self,coord):

        return 4*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3*(-coord[1]+self.c)^4+2*(-coord[0]+self.a)*(-coord[0]+self.b)^4*(-coord[1]+self.c)^4

    def partialGxy3530(self,coord):

        return 4*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3*(-coord[1]+self.d)+2*(-coord[0]+self.a)*(-coord[0]+self.b)^4*(-coord[1]+self.d)

    def partialGxy3531(self,coord):

        return 4*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3*(-coord[1]+self.c)*(-coord[1]+self.d)+2*(-coord[0]+self.a)*(-coord[0]+self.b)^4*(-coord[1]+self.c)*(-coord[1]+self.d)

    def partialGxy3532(self,coord):

        return 4*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3*(-coord[1]+self.c)^2*(-coord[1]+self.d)+2*(-coord[0]+self.a)*(-coord[0]+self.b)^4*(-coord[1]+self.c)^2*(-coord[1]+self.d)

    def partialGxy3533(self,coord):

        return 4*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3*(-coord[1]+self.c)^3*(-coord[1]+self.d)+2*(-coord[0]+self.a)*(-coord[0]+self.b)^4*(-coord[1]+self.c)^3*(-coord[1]+self.d)

    def partialGxy3534(self,coord):

        return 4*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3*(-coord[1]+self.c)^4*(-coord[1]+self.d)+2*(-coord[0]+self.a)*(-coord[0]+self.b)^4*(-coord[1]+self.c)^4*(-coord[1]+self.d)

    def partialGxy3535(self,coord):

        return 4*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3*(-coord[1]+self.d)^2+2*(-coord[0]+self.a)*(-coord[0]+self.b)^4*(-coord[1]+self.d)^2

    def partialGxy3536(self,coord):

        return 4*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3*(-coord[1]+self.c)*(-coord[1]+self.d)^2+2*(-coord[0]+self.a)*(-coord[0]+self.b)^4*(-coord[1]+self.c)*(-coord[1]+self.d)^2

    def partialGxy3537(self,coord):

        return 4*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2+2*(-coord[0]+self.a)*(-coord[0]+self.b)^4*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2

    def partialGxy3538(self,coord):

        return 4*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2+2*(-coord[0]+self.a)*(-coord[0]+self.b)^4*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2

    def partialGxy3539(self,coord):

        return 4*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3*(-coord[1]+self.c)^4*(-coord[1]+self.d)^2+2*(-coord[0]+self.a)*(-coord[0]+self.b)^4*(-coord[1]+self.c)^4*(-coord[1]+self.d)^2

    def partialGxy3540(self,coord):

        return 4*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3*(-coord[1]+self.d)^3+2*(-coord[0]+self.a)*(-coord[0]+self.b)^4*(-coord[1]+self.d)^3

    def partialGxy3541(self,coord):

        return 4*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3*(-coord[1]+self.c)*(-coord[1]+self.d)^3+2*(-coord[0]+self.a)*(-coord[0]+self.b)^4*(-coord[1]+self.c)*(-coord[1]+self.d)^3

    def partialGxy3542(self,coord):

        return 4*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3+2*(-coord[0]+self.a)*(-coord[0]+self.b)^4*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3

    def partialGxy3543(self,coord):

        return 4*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3*(-coord[1]+self.c)^3*(-coord[1]+self.d)^3+2*(-coord[0]+self.a)*(-coord[0]+self.b)^4*(-coord[1]+self.c)^3*(-coord[1]+self.d)^3

    def partialGxy3544(self,coord):

        return 4*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3*(-coord[1]+self.c)^4*(-coord[1]+self.d)^3+2*(-coord[0]+self.a)*(-coord[0]+self.b)^4*(-coord[1]+self.c)^4*(-coord[1]+self.d)^3

    def partialGxy3545(self,coord):

        return 4*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3*(-coord[1]+self.d)^4+2*(-coord[0]+self.a)*(-coord[0]+self.b)^4*(-coord[1]+self.d)^4

    def partialGxy3546(self,coord):

        return 4*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3*(-coord[1]+self.c)*(-coord[1]+self.d)^4+2*(-coord[0]+self.a)*(-coord[0]+self.b)^4*(-coord[1]+self.c)*(-coord[1]+self.d)^4

    def partialGxy3547(self,coord):

        return 4*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3*(-coord[1]+self.c)^2*(-coord[1]+self.d)^4+2*(-coord[0]+self.a)*(-coord[0]+self.b)^4*(-coord[1]+self.c)^2*(-coord[1]+self.d)^4

    def partialGxy3548(self,coord):

        return 4*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3*(-coord[1]+self.c)^3*(-coord[1]+self.d)^4+2*(-coord[0]+self.a)*(-coord[0]+self.b)^4*(-coord[1]+self.c)^3*(-coord[1]+self.d)^4

    def partialGxy3549(self,coord):

        return 4*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3*(-coord[1]+self.c)^4*(-coord[1]+self.d)^4+2*(-coord[0]+self.a)*(-coord[0]+self.b)^4*(-coord[1]+self.c)^4*(-coord[1]+self.d)^4

    def partialGxy3556(self,coord):

        return 4*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3*(-coord[1]+self.c)+2*(-coord[0]+self.a)*(-coord[0]+self.b)^4*(-coord[1]+self.c)+4*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3*(-coord[1]+self.d)+2*(-coord[0]+self.a)*(-coord[0]+self.b)^4*(-coord[1]+self.d)

    def partialGxy3557(self,coord):

        return 4*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3*(-coord[1]+self.c)^2+2*(-coord[0]+self.a)*(-coord[0]+self.b)^4*(-coord[1]+self.c)^2+8*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3*(-coord[1]+self.c)*(-coord[1]+self.d)+4*(-coord[0]+self.a)*(-coord[0]+self.b)^4*(-coord[1]+self.c)*(-coord[1]+self.d)

    def partialGxy3558(self,coord):

        return 4*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3*(-coord[1]+self.c)^3+2*(-coord[0]+self.a)*(-coord[0]+self.b)^4*(-coord[1]+self.c)^3+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3*(-coord[1]+self.c)^2*(-coord[1]+self.d)+6*(-coord[0]+self.a)*(-coord[0]+self.b)^4*(-coord[1]+self.c)^2*(-coord[1]+self.d)

    def partialGxy3559(self,coord):

        return 4*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3*(-coord[1]+self.c)^4+2*(-coord[0]+self.a)*(-coord[0]+self.b)^4*(-coord[1]+self.c)^4+16*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3*(-coord[1]+self.c)^3*(-coord[1]+self.d)+8*(-coord[0]+self.a)*(-coord[0]+self.b)^4*(-coord[1]+self.c)^3*(-coord[1]+self.d)

    def partialGxy3561(self,coord):

        return 8*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3*(-coord[1]+self.c)*(-coord[1]+self.d)+4*(-coord[0]+self.a)*(-coord[0]+self.b)^4*(-coord[1]+self.c)*(-coord[1]+self.d)+4*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3*(-coord[1]+self.d)^2+2*(-coord[0]+self.a)*(-coord[0]+self.b)^4*(-coord[1]+self.d)^2

    def partialGxy3562(self,coord):

        return 8*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3*(-coord[1]+self.c)^2*(-coord[1]+self.d)+4*(-coord[0]+self.a)*(-coord[0]+self.b)^4*(-coord[1]+self.c)^2*(-coord[1]+self.d)+8*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3*(-coord[1]+self.c)*(-coord[1]+self.d)^2+4*(-coord[0]+self.a)*(-coord[0]+self.b)^4*(-coord[1]+self.c)*(-coord[1]+self.d)^2

    def partialGxy3563(self,coord):

        return 8*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3*(-coord[1]+self.c)^3*(-coord[1]+self.d)+4*(-coord[0]+self.a)*(-coord[0]+self.b)^4*(-coord[1]+self.c)^3*(-coord[1]+self.d)+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2+6*(-coord[0]+self.a)*(-coord[0]+self.b)^4*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2

    def partialGxy3564(self,coord):

        return 8*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3*(-coord[1]+self.c)^4*(-coord[1]+self.d)+4*(-coord[0]+self.a)*(-coord[0]+self.b)^4*(-coord[1]+self.c)^4*(-coord[1]+self.d)+16*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2+8*(-coord[0]+self.a)*(-coord[0]+self.b)^4*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2

    def partialGxy3566(self,coord):

        return 12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3*(-coord[1]+self.c)*(-coord[1]+self.d)^2+6*(-coord[0]+self.a)*(-coord[0]+self.b)^4*(-coord[1]+self.c)*(-coord[1]+self.d)^2+4*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3*(-coord[1]+self.d)^3+2*(-coord[0]+self.a)*(-coord[0]+self.b)^4*(-coord[1]+self.d)^3

    def partialGxy3567(self,coord):

        return 12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2+6*(-coord[0]+self.a)*(-coord[0]+self.b)^4*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2+8*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3*(-coord[1]+self.c)*(-coord[1]+self.d)^3+4*(-coord[0]+self.a)*(-coord[0]+self.b)^4*(-coord[1]+self.c)*(-coord[1]+self.d)^3

    def partialGxy3568(self,coord):

        return 12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2+6*(-coord[0]+self.a)*(-coord[0]+self.b)^4*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3+6*(-coord[0]+self.a)*(-coord[0]+self.b)^4*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3

    def partialGxy3569(self,coord):

        return 12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3*(-coord[1]+self.c)^4*(-coord[1]+self.d)^2+6*(-coord[0]+self.a)*(-coord[0]+self.b)^4*(-coord[1]+self.c)^4*(-coord[1]+self.d)^2+16*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3*(-coord[1]+self.c)^3*(-coord[1]+self.d)^3+8*(-coord[0]+self.a)*(-coord[0]+self.b)^4*(-coord[1]+self.c)^3*(-coord[1]+self.d)^3

    def partialGxy3571(self,coord):

        return 16*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3*(-coord[1]+self.c)*(-coord[1]+self.d)^3+8*(-coord[0]+self.a)*(-coord[0]+self.b)^4*(-coord[1]+self.c)*(-coord[1]+self.d)^3+4*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3*(-coord[1]+self.d)^4+2*(-coord[0]+self.a)*(-coord[0]+self.b)^4*(-coord[1]+self.d)^4

    def partialGxy3572(self,coord):

        return 16*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3+8*(-coord[0]+self.a)*(-coord[0]+self.b)^4*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3+8*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3*(-coord[1]+self.c)*(-coord[1]+self.d)^4+4*(-coord[0]+self.a)*(-coord[0]+self.b)^4*(-coord[1]+self.c)*(-coord[1]+self.d)^4

    def partialGxy3573(self,coord):

        return 16*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3*(-coord[1]+self.c)^3*(-coord[1]+self.d)^3+8*(-coord[0]+self.a)*(-coord[0]+self.b)^4*(-coord[1]+self.c)^3*(-coord[1]+self.d)^3+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3*(-coord[1]+self.c)^2*(-coord[1]+self.d)^4+6*(-coord[0]+self.a)*(-coord[0]+self.b)^4*(-coord[1]+self.c)^2*(-coord[1]+self.d)^4

    def partialGxy3574(self,coord):

        return 16*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3*(-coord[1]+self.c)^4*(-coord[1]+self.d)^3+8*(-coord[0]+self.a)*(-coord[0]+self.b)^4*(-coord[1]+self.c)^4*(-coord[1]+self.d)^3+16*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3*(-coord[1]+self.c)^3*(-coord[1]+self.d)^4+8*(-coord[0]+self.a)*(-coord[0]+self.b)^4*(-coord[1]+self.c)^3*(-coord[1]+self.d)^4

    def partialGxy3587(self,coord):

        return 4*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3*(2*(-coord[1]+self.c)^2+8*(-coord[1]+self.c)*(-coord[1]+self.d)+2*(-coord[1]+self.d)^2)+2*(-coord[0]+self.a)*(-coord[0]+self.b)^4*(2*(-coord[1]+self.c)^2+8*(-coord[1]+self.c)*(-coord[1]+self.d)+2*(-coord[1]+self.d)^2)

    def partialGxy3588(self,coord):

        return 4*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3*(2*(-coord[1]+self.c)^3+12*(-coord[1]+self.c)^2*(-coord[1]+self.d)+6*(-coord[1]+self.c)*(-coord[1]+self.d)^2)+2*(-coord[0]+self.a)*(-coord[0]+self.b)^4*(2*(-coord[1]+self.c)^3+12*(-coord[1]+self.c)^2*(-coord[1]+self.d)+6*(-coord[1]+self.c)*(-coord[1]+self.d)^2)

    def partialGxy3589(self,coord):

        return 4*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3*(2*(-coord[1]+self.c)^4+16*(-coord[1]+self.c)^3*(-coord[1]+self.d)+12*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2)+2*(-coord[0]+self.a)*(-coord[0]+self.b)^4*(2*(-coord[1]+self.c)^4+16*(-coord[1]+self.c)^3*(-coord[1]+self.d)+12*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2)

    def partialGxy3592(self,coord):

        return 4*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3*(6*(-coord[1]+self.c)^2*(-coord[1]+self.d)+12*(-coord[1]+self.c)*(-coord[1]+self.d)^2+2*(-coord[1]+self.d)^3)+2*(-coord[0]+self.a)*(-coord[0]+self.b)^4*(6*(-coord[1]+self.c)^2*(-coord[1]+self.d)+12*(-coord[1]+self.c)*(-coord[1]+self.d)^2+2*(-coord[1]+self.d)^3)

    def partialGxy3593(self,coord):

        return 4*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3*(6*(-coord[1]+self.c)^3*(-coord[1]+self.d)+18*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2+6*(-coord[1]+self.c)*(-coord[1]+self.d)^3)+2*(-coord[0]+self.a)*(-coord[0]+self.b)^4*(6*(-coord[1]+self.c)^3*(-coord[1]+self.d)+18*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2+6*(-coord[1]+self.c)*(-coord[1]+self.d)^3)

    def partialGxy3594(self,coord):

        return 4*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3*(6*(-coord[1]+self.c)^4*(-coord[1]+self.d)+24*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2+12*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3)+2*(-coord[0]+self.a)*(-coord[0]+self.b)^4*(6*(-coord[1]+self.c)^4*(-coord[1]+self.d)+24*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2+12*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3)

    def partialGxy3597(self,coord):

        return 4*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3*(12*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2+16*(-coord[1]+self.c)*(-coord[1]+self.d)^3+2*(-coord[1]+self.d)^4)+2*(-coord[0]+self.a)*(-coord[0]+self.b)^4*(12*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2+16*(-coord[1]+self.c)*(-coord[1]+self.d)^3+2*(-coord[1]+self.d)^4)

    def partialGxy3598(self,coord):

        return 4*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3*(12*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2+24*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3+6*(-coord[1]+self.c)*(-coord[1]+self.d)^4)+2*(-coord[0]+self.a)*(-coord[0]+self.b)^4*(12*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2+24*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3+6*(-coord[1]+self.c)*(-coord[1]+self.d)^4)

    def partialGxy3599(self,coord):

        return 4*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3*(12*(-coord[1]+self.c)^4*(-coord[1]+self.d)^2+32*(-coord[1]+self.c)^3*(-coord[1]+self.d)^3+12*(-coord[1]+self.c)^2*(-coord[1]+self.d)^4)+2*(-coord[0]+self.a)*(-coord[0]+self.b)^4*(12*(-coord[1]+self.c)^4*(-coord[1]+self.d)^2+32*(-coord[1]+self.c)^3*(-coord[1]+self.d)^3+12*(-coord[1]+self.c)^2*(-coord[1]+self.d)^4)

    def partialGxy3600(self,coord):

        return 4*(-coord[0]+self.a)^3*(-coord[0]+self.b)^3+3*(-coord[0]+self.a)^2*(-coord[0]+self.b)^4

    def partialGxy3601(self,coord):

        return 4*(-coord[0]+self.a)^3*(-coord[0]+self.b)^3*(-coord[1]+self.c)+3*(-coord[0]+self.a)^2*(-coord[0]+self.b)^4*(-coord[1]+self.c)

    def partialGxy3602(self,coord):

        return 4*(-coord[0]+self.a)^3*(-coord[0]+self.b)^3*(-coord[1]+self.c)^2+3*(-coord[0]+self.a)^2*(-coord[0]+self.b)^4*(-coord[1]+self.c)^2

    def partialGxy3603(self,coord):

        return 4*(-coord[0]+self.a)^3*(-coord[0]+self.b)^3*(-coord[1]+self.c)^3+3*(-coord[0]+self.a)^2*(-coord[0]+self.b)^4*(-coord[1]+self.c)^3

    def partialGxy3604(self,coord):

        return 4*(-coord[0]+self.a)^3*(-coord[0]+self.b)^3*(-coord[1]+self.c)^4+3*(-coord[0]+self.a)^2*(-coord[0]+self.b)^4*(-coord[1]+self.c)^4

    def partialGxy3605(self,coord):

        return 4*(-coord[0]+self.a)^3*(-coord[0]+self.b)^3*(-coord[1]+self.d)+3*(-coord[0]+self.a)^2*(-coord[0]+self.b)^4*(-coord[1]+self.d)

    def partialGxy3606(self,coord):

        return 4*(-coord[0]+self.a)^3*(-coord[0]+self.b)^3*(-coord[1]+self.c)*(-coord[1]+self.d)+3*(-coord[0]+self.a)^2*(-coord[0]+self.b)^4*(-coord[1]+self.c)*(-coord[1]+self.d)

    def partialGxy3607(self,coord):

        return 4*(-coord[0]+self.a)^3*(-coord[0]+self.b)^3*(-coord[1]+self.c)^2*(-coord[1]+self.d)+3*(-coord[0]+self.a)^2*(-coord[0]+self.b)^4*(-coord[1]+self.c)^2*(-coord[1]+self.d)

    def partialGxy3608(self,coord):

        return 4*(-coord[0]+self.a)^3*(-coord[0]+self.b)^3*(-coord[1]+self.c)^3*(-coord[1]+self.d)+3*(-coord[0]+self.a)^2*(-coord[0]+self.b)^4*(-coord[1]+self.c)^3*(-coord[1]+self.d)

    def partialGxy3609(self,coord):

        return 4*(-coord[0]+self.a)^3*(-coord[0]+self.b)^3*(-coord[1]+self.c)^4*(-coord[1]+self.d)+3*(-coord[0]+self.a)^2*(-coord[0]+self.b)^4*(-coord[1]+self.c)^4*(-coord[1]+self.d)

    def partialGxy3610(self,coord):

        return 4*(-coord[0]+self.a)^3*(-coord[0]+self.b)^3*(-coord[1]+self.d)^2+3*(-coord[0]+self.a)^2*(-coord[0]+self.b)^4*(-coord[1]+self.d)^2

    def partialGxy3611(self,coord):

        return 4*(-coord[0]+self.a)^3*(-coord[0]+self.b)^3*(-coord[1]+self.c)*(-coord[1]+self.d)^2+3*(-coord[0]+self.a)^2*(-coord[0]+self.b)^4*(-coord[1]+self.c)*(-coord[1]+self.d)^2

    def partialGxy3612(self,coord):

        return 4*(-coord[0]+self.a)^3*(-coord[0]+self.b)^3*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2+3*(-coord[0]+self.a)^2*(-coord[0]+self.b)^4*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2

    def partialGxy3613(self,coord):

        return 4*(-coord[0]+self.a)^3*(-coord[0]+self.b)^3*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2+3*(-coord[0]+self.a)^2*(-coord[0]+self.b)^4*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2

    def partialGxy3614(self,coord):

        return 4*(-coord[0]+self.a)^3*(-coord[0]+self.b)^3*(-coord[1]+self.c)^4*(-coord[1]+self.d)^2+3*(-coord[0]+self.a)^2*(-coord[0]+self.b)^4*(-coord[1]+self.c)^4*(-coord[1]+self.d)^2

    def partialGxy3615(self,coord):

        return 4*(-coord[0]+self.a)^3*(-coord[0]+self.b)^3*(-coord[1]+self.d)^3+3*(-coord[0]+self.a)^2*(-coord[0]+self.b)^4*(-coord[1]+self.d)^3

    def partialGxy3616(self,coord):

        return 4*(-coord[0]+self.a)^3*(-coord[0]+self.b)^3*(-coord[1]+self.c)*(-coord[1]+self.d)^3+3*(-coord[0]+self.a)^2*(-coord[0]+self.b)^4*(-coord[1]+self.c)*(-coord[1]+self.d)^3

    def partialGxy3617(self,coord):

        return 4*(-coord[0]+self.a)^3*(-coord[0]+self.b)^3*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3+3*(-coord[0]+self.a)^2*(-coord[0]+self.b)^4*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3

    def partialGxy3618(self,coord):

        return 4*(-coord[0]+self.a)^3*(-coord[0]+self.b)^3*(-coord[1]+self.c)^3*(-coord[1]+self.d)^3+3*(-coord[0]+self.a)^2*(-coord[0]+self.b)^4*(-coord[1]+self.c)^3*(-coord[1]+self.d)^3

    def partialGxy3619(self,coord):

        return 4*(-coord[0]+self.a)^3*(-coord[0]+self.b)^3*(-coord[1]+self.c)^4*(-coord[1]+self.d)^3+3*(-coord[0]+self.a)^2*(-coord[0]+self.b)^4*(-coord[1]+self.c)^4*(-coord[1]+self.d)^3

    def partialGxy3620(self,coord):

        return 4*(-coord[0]+self.a)^3*(-coord[0]+self.b)^3*(-coord[1]+self.d)^4+3*(-coord[0]+self.a)^2*(-coord[0]+self.b)^4*(-coord[1]+self.d)^4

    def partialGxy3621(self,coord):

        return 4*(-coord[0]+self.a)^3*(-coord[0]+self.b)^3*(-coord[1]+self.c)*(-coord[1]+self.d)^4+3*(-coord[0]+self.a)^2*(-coord[0]+self.b)^4*(-coord[1]+self.c)*(-coord[1]+self.d)^4

    def partialGxy3622(self,coord):

        return 4*(-coord[0]+self.a)^3*(-coord[0]+self.b)^3*(-coord[1]+self.c)^2*(-coord[1]+self.d)^4+3*(-coord[0]+self.a)^2*(-coord[0]+self.b)^4*(-coord[1]+self.c)^2*(-coord[1]+self.d)^4

    def partialGxy3623(self,coord):

        return 4*(-coord[0]+self.a)^3*(-coord[0]+self.b)^3*(-coord[1]+self.c)^3*(-coord[1]+self.d)^4+3*(-coord[0]+self.a)^2*(-coord[0]+self.b)^4*(-coord[1]+self.c)^3*(-coord[1]+self.d)^4

    def partialGxy3624(self,coord):

        return 4*(-coord[0]+self.a)^3*(-coord[0]+self.b)^3*(-coord[1]+self.c)^4*(-coord[1]+self.d)^4+3*(-coord[0]+self.a)^2*(-coord[0]+self.b)^4*(-coord[1]+self.c)^4*(-coord[1]+self.d)^4

    def partialGxy3631(self,coord):

        return 4*(-coord[0]+self.a)^3*(-coord[0]+self.b)^3*(-coord[1]+self.c)+3*(-coord[0]+self.a)^2*(-coord[0]+self.b)^4*(-coord[1]+self.c)+4*(-coord[0]+self.a)^3*(-coord[0]+self.b)^3*(-coord[1]+self.d)+3*(-coord[0]+self.a)^2*(-coord[0]+self.b)^4*(-coord[1]+self.d)

    def partialGxy3632(self,coord):

        return 4*(-coord[0]+self.a)^3*(-coord[0]+self.b)^3*(-coord[1]+self.c)^2+3*(-coord[0]+self.a)^2*(-coord[0]+self.b)^4*(-coord[1]+self.c)^2+8*(-coord[0]+self.a)^3*(-coord[0]+self.b)^3*(-coord[1]+self.c)*(-coord[1]+self.d)+6*(-coord[0]+self.a)^2*(-coord[0]+self.b)^4*(-coord[1]+self.c)*(-coord[1]+self.d)

    def partialGxy3633(self,coord):

        return 4*(-coord[0]+self.a)^3*(-coord[0]+self.b)^3*(-coord[1]+self.c)^3+3*(-coord[0]+self.a)^2*(-coord[0]+self.b)^4*(-coord[1]+self.c)^3+12*(-coord[0]+self.a)^3*(-coord[0]+self.b)^3*(-coord[1]+self.c)^2*(-coord[1]+self.d)+9*(-coord[0]+self.a)^2*(-coord[0]+self.b)^4*(-coord[1]+self.c)^2*(-coord[1]+self.d)

    def partialGxy3634(self,coord):

        return 4*(-coord[0]+self.a)^3*(-coord[0]+self.b)^3*(-coord[1]+self.c)^4+3*(-coord[0]+self.a)^2*(-coord[0]+self.b)^4*(-coord[1]+self.c)^4+16*(-coord[0]+self.a)^3*(-coord[0]+self.b)^3*(-coord[1]+self.c)^3*(-coord[1]+self.d)+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^4*(-coord[1]+self.c)^3*(-coord[1]+self.d)

    def partialGxy3636(self,coord):

        return 8*(-coord[0]+self.a)^3*(-coord[0]+self.b)^3*(-coord[1]+self.c)*(-coord[1]+self.d)+6*(-coord[0]+self.a)^2*(-coord[0]+self.b)^4*(-coord[1]+self.c)*(-coord[1]+self.d)+4*(-coord[0]+self.a)^3*(-coord[0]+self.b)^3*(-coord[1]+self.d)^2+3*(-coord[0]+self.a)^2*(-coord[0]+self.b)^4*(-coord[1]+self.d)^2

    def partialGxy3637(self,coord):

        return 8*(-coord[0]+self.a)^3*(-coord[0]+self.b)^3*(-coord[1]+self.c)^2*(-coord[1]+self.d)+6*(-coord[0]+self.a)^2*(-coord[0]+self.b)^4*(-coord[1]+self.c)^2*(-coord[1]+self.d)+8*(-coord[0]+self.a)^3*(-coord[0]+self.b)^3*(-coord[1]+self.c)*(-coord[1]+self.d)^2+6*(-coord[0]+self.a)^2*(-coord[0]+self.b)^4*(-coord[1]+self.c)*(-coord[1]+self.d)^2

    def partialGxy3638(self,coord):

        return 8*(-coord[0]+self.a)^3*(-coord[0]+self.b)^3*(-coord[1]+self.c)^3*(-coord[1]+self.d)+6*(-coord[0]+self.a)^2*(-coord[0]+self.b)^4*(-coord[1]+self.c)^3*(-coord[1]+self.d)+12*(-coord[0]+self.a)^3*(-coord[0]+self.b)^3*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2+9*(-coord[0]+self.a)^2*(-coord[0]+self.b)^4*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2

    def partialGxy3639(self,coord):

        return 8*(-coord[0]+self.a)^3*(-coord[0]+self.b)^3*(-coord[1]+self.c)^4*(-coord[1]+self.d)+6*(-coord[0]+self.a)^2*(-coord[0]+self.b)^4*(-coord[1]+self.c)^4*(-coord[1]+self.d)+16*(-coord[0]+self.a)^3*(-coord[0]+self.b)^3*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^4*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2

    def partialGxy3641(self,coord):

        return 12*(-coord[0]+self.a)^3*(-coord[0]+self.b)^3*(-coord[1]+self.c)*(-coord[1]+self.d)^2+9*(-coord[0]+self.a)^2*(-coord[0]+self.b)^4*(-coord[1]+self.c)*(-coord[1]+self.d)^2+4*(-coord[0]+self.a)^3*(-coord[0]+self.b)^3*(-coord[1]+self.d)^3+3*(-coord[0]+self.a)^2*(-coord[0]+self.b)^4*(-coord[1]+self.d)^3

    def partialGxy3642(self,coord):

        return 12*(-coord[0]+self.a)^3*(-coord[0]+self.b)^3*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2+9*(-coord[0]+self.a)^2*(-coord[0]+self.b)^4*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2+8*(-coord[0]+self.a)^3*(-coord[0]+self.b)^3*(-coord[1]+self.c)*(-coord[1]+self.d)^3+6*(-coord[0]+self.a)^2*(-coord[0]+self.b)^4*(-coord[1]+self.c)*(-coord[1]+self.d)^3

    def partialGxy3643(self,coord):

        return 12*(-coord[0]+self.a)^3*(-coord[0]+self.b)^3*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2+9*(-coord[0]+self.a)^2*(-coord[0]+self.b)^4*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2+12*(-coord[0]+self.a)^3*(-coord[0]+self.b)^3*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3+9*(-coord[0]+self.a)^2*(-coord[0]+self.b)^4*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3

    def partialGxy3644(self,coord):

        return 12*(-coord[0]+self.a)^3*(-coord[0]+self.b)^3*(-coord[1]+self.c)^4*(-coord[1]+self.d)^2+9*(-coord[0]+self.a)^2*(-coord[0]+self.b)^4*(-coord[1]+self.c)^4*(-coord[1]+self.d)^2+16*(-coord[0]+self.a)^3*(-coord[0]+self.b)^3*(-coord[1]+self.c)^3*(-coord[1]+self.d)^3+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^4*(-coord[1]+self.c)^3*(-coord[1]+self.d)^3

    def partialGxy3646(self,coord):

        return 16*(-coord[0]+self.a)^3*(-coord[0]+self.b)^3*(-coord[1]+self.c)*(-coord[1]+self.d)^3+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^4*(-coord[1]+self.c)*(-coord[1]+self.d)^3+4*(-coord[0]+self.a)^3*(-coord[0]+self.b)^3*(-coord[1]+self.d)^4+3*(-coord[0]+self.a)^2*(-coord[0]+self.b)^4*(-coord[1]+self.d)^4

    def partialGxy3647(self,coord):

        return 16*(-coord[0]+self.a)^3*(-coord[0]+self.b)^3*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^4*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3+8*(-coord[0]+self.a)^3*(-coord[0]+self.b)^3*(-coord[1]+self.c)*(-coord[1]+self.d)^4+6*(-coord[0]+self.a)^2*(-coord[0]+self.b)^4*(-coord[1]+self.c)*(-coord[1]+self.d)^4

    def partialGxy3648(self,coord):

        return 16*(-coord[0]+self.a)^3*(-coord[0]+self.b)^3*(-coord[1]+self.c)^3*(-coord[1]+self.d)^3+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^4*(-coord[1]+self.c)^3*(-coord[1]+self.d)^3+12*(-coord[0]+self.a)^3*(-coord[0]+self.b)^3*(-coord[1]+self.c)^2*(-coord[1]+self.d)^4+9*(-coord[0]+self.a)^2*(-coord[0]+self.b)^4*(-coord[1]+self.c)^2*(-coord[1]+self.d)^4

    def partialGxy3649(self,coord):

        return 16*(-coord[0]+self.a)^3*(-coord[0]+self.b)^3*(-coord[1]+self.c)^4*(-coord[1]+self.d)^3+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^4*(-coord[1]+self.c)^4*(-coord[1]+self.d)^3+16*(-coord[0]+self.a)^3*(-coord[0]+self.b)^3*(-coord[1]+self.c)^3*(-coord[1]+self.d)^4+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^4*(-coord[1]+self.c)^3*(-coord[1]+self.d)^4

    def partialGxy3662(self,coord):

        return 4*(-coord[0]+self.a)^3*(-coord[0]+self.b)^3*(2*(-coord[1]+self.c)^2+8*(-coord[1]+self.c)*(-coord[1]+self.d)+2*(-coord[1]+self.d)^2)+3*(-coord[0]+self.a)^2*(-coord[0]+self.b)^4*(2*(-coord[1]+self.c)^2+8*(-coord[1]+self.c)*(-coord[1]+self.d)+2*(-coord[1]+self.d)^2)

    def partialGxy3663(self,coord):

        return 4*(-coord[0]+self.a)^3*(-coord[0]+self.b)^3*(2*(-coord[1]+self.c)^3+12*(-coord[1]+self.c)^2*(-coord[1]+self.d)+6*(-coord[1]+self.c)*(-coord[1]+self.d)^2)+3*(-coord[0]+self.a)^2*(-coord[0]+self.b)^4*(2*(-coord[1]+self.c)^3+12*(-coord[1]+self.c)^2*(-coord[1]+self.d)+6*(-coord[1]+self.c)*(-coord[1]+self.d)^2)

    def partialGxy3664(self,coord):

        return 4*(-coord[0]+self.a)^3*(-coord[0]+self.b)^3*(2*(-coord[1]+self.c)^4+16*(-coord[1]+self.c)^3*(-coord[1]+self.d)+12*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2)+3*(-coord[0]+self.a)^2*(-coord[0]+self.b)^4*(2*(-coord[1]+self.c)^4+16*(-coord[1]+self.c)^3*(-coord[1]+self.d)+12*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2)

    def partialGxy3667(self,coord):

        return 4*(-coord[0]+self.a)^3*(-coord[0]+self.b)^3*(6*(-coord[1]+self.c)^2*(-coord[1]+self.d)+12*(-coord[1]+self.c)*(-coord[1]+self.d)^2+2*(-coord[1]+self.d)^3)+3*(-coord[0]+self.a)^2*(-coord[0]+self.b)^4*(6*(-coord[1]+self.c)^2*(-coord[1]+self.d)+12*(-coord[1]+self.c)*(-coord[1]+self.d)^2+2*(-coord[1]+self.d)^3)

    def partialGxy3668(self,coord):

        return 4*(-coord[0]+self.a)^3*(-coord[0]+self.b)^3*(6*(-coord[1]+self.c)^3*(-coord[1]+self.d)+18*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2+6*(-coord[1]+self.c)*(-coord[1]+self.d)^3)+3*(-coord[0]+self.a)^2*(-coord[0]+self.b)^4*(6*(-coord[1]+self.c)^3*(-coord[1]+self.d)+18*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2+6*(-coord[1]+self.c)*(-coord[1]+self.d)^3)

    def partialGxy3669(self,coord):

        return 4*(-coord[0]+self.a)^3*(-coord[0]+self.b)^3*(6*(-coord[1]+self.c)^4*(-coord[1]+self.d)+24*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2+12*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3)+3*(-coord[0]+self.a)^2*(-coord[0]+self.b)^4*(6*(-coord[1]+self.c)^4*(-coord[1]+self.d)+24*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2+12*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3)

    def partialGxy3672(self,coord):

        return 4*(-coord[0]+self.a)^3*(-coord[0]+self.b)^3*(12*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2+16*(-coord[1]+self.c)*(-coord[1]+self.d)^3+2*(-coord[1]+self.d)^4)+3*(-coord[0]+self.a)^2*(-coord[0]+self.b)^4*(12*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2+16*(-coord[1]+self.c)*(-coord[1]+self.d)^3+2*(-coord[1]+self.d)^4)

    def partialGxy3673(self,coord):

        return 4*(-coord[0]+self.a)^3*(-coord[0]+self.b)^3*(12*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2+24*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3+6*(-coord[1]+self.c)*(-coord[1]+self.d)^4)+3*(-coord[0]+self.a)^2*(-coord[0]+self.b)^4*(12*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2+24*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3+6*(-coord[1]+self.c)*(-coord[1]+self.d)^4)

    def partialGxy3674(self,coord):

        return 4*(-coord[0]+self.a)^3*(-coord[0]+self.b)^3*(12*(-coord[1]+self.c)^4*(-coord[1]+self.d)^2+32*(-coord[1]+self.c)^3*(-coord[1]+self.d)^3+12*(-coord[1]+self.c)^2*(-coord[1]+self.d)^4)+3*(-coord[0]+self.a)^2*(-coord[0]+self.b)^4*(12*(-coord[1]+self.c)^4*(-coord[1]+self.d)^2+32*(-coord[1]+self.c)^3*(-coord[1]+self.d)^3+12*(-coord[1]+self.c)^2*(-coord[1]+self.d)^4)

    def partialGxy3675(self,coord):

        return 4*(-coord[0]+self.a)^4*(-coord[0]+self.b)^3+4*(-coord[0]+self.a)^3*(-coord[0]+self.b)^4

    def partialGxy3676(self,coord):

        return 4*(-coord[0]+self.a)^4*(-coord[0]+self.b)^3*(-coord[1]+self.c)+4*(-coord[0]+self.a)^3*(-coord[0]+self.b)^4*(-coord[1]+self.c)

    def partialGxy3677(self,coord):

        return 4*(-coord[0]+self.a)^4*(-coord[0]+self.b)^3*(-coord[1]+self.c)^2+4*(-coord[0]+self.a)^3*(-coord[0]+self.b)^4*(-coord[1]+self.c)^2

    def partialGxy3678(self,coord):

        return 4*(-coord[0]+self.a)^4*(-coord[0]+self.b)^3*(-coord[1]+self.c)^3+4*(-coord[0]+self.a)^3*(-coord[0]+self.b)^4*(-coord[1]+self.c)^3

    def partialGxy3679(self,coord):

        return 4*(-coord[0]+self.a)^4*(-coord[0]+self.b)^3*(-coord[1]+self.c)^4+4*(-coord[0]+self.a)^3*(-coord[0]+self.b)^4*(-coord[1]+self.c)^4

    def partialGxy3680(self,coord):

        return 4*(-coord[0]+self.a)^4*(-coord[0]+self.b)^3*(-coord[1]+self.d)+4*(-coord[0]+self.a)^3*(-coord[0]+self.b)^4*(-coord[1]+self.d)

    def partialGxy3681(self,coord):

        return 4*(-coord[0]+self.a)^4*(-coord[0]+self.b)^3*(-coord[1]+self.c)*(-coord[1]+self.d)+4*(-coord[0]+self.a)^3*(-coord[0]+self.b)^4*(-coord[1]+self.c)*(-coord[1]+self.d)

    def partialGxy3682(self,coord):

        return 4*(-coord[0]+self.a)^4*(-coord[0]+self.b)^3*(-coord[1]+self.c)^2*(-coord[1]+self.d)+4*(-coord[0]+self.a)^3*(-coord[0]+self.b)^4*(-coord[1]+self.c)^2*(-coord[1]+self.d)

    def partialGxy3683(self,coord):

        return 4*(-coord[0]+self.a)^4*(-coord[0]+self.b)^3*(-coord[1]+self.c)^3*(-coord[1]+self.d)+4*(-coord[0]+self.a)^3*(-coord[0]+self.b)^4*(-coord[1]+self.c)^3*(-coord[1]+self.d)

    def partialGxy3684(self,coord):

        return 4*(-coord[0]+self.a)^4*(-coord[0]+self.b)^3*(-coord[1]+self.c)^4*(-coord[1]+self.d)+4*(-coord[0]+self.a)^3*(-coord[0]+self.b)^4*(-coord[1]+self.c)^4*(-coord[1]+self.d)

    def partialGxy3685(self,coord):

        return 4*(-coord[0]+self.a)^4*(-coord[0]+self.b)^3*(-coord[1]+self.d)^2+4*(-coord[0]+self.a)^3*(-coord[0]+self.b)^4*(-coord[1]+self.d)^2

    def partialGxy3686(self,coord):

        return 4*(-coord[0]+self.a)^4*(-coord[0]+self.b)^3*(-coord[1]+self.c)*(-coord[1]+self.d)^2+4*(-coord[0]+self.a)^3*(-coord[0]+self.b)^4*(-coord[1]+self.c)*(-coord[1]+self.d)^2

    def partialGxy3687(self,coord):

        return 4*(-coord[0]+self.a)^4*(-coord[0]+self.b)^3*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2+4*(-coord[0]+self.a)^3*(-coord[0]+self.b)^4*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2

    def partialGxy3688(self,coord):

        return 4*(-coord[0]+self.a)^4*(-coord[0]+self.b)^3*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2+4*(-coord[0]+self.a)^3*(-coord[0]+self.b)^4*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2

    def partialGxy3689(self,coord):

        return 4*(-coord[0]+self.a)^4*(-coord[0]+self.b)^3*(-coord[1]+self.c)^4*(-coord[1]+self.d)^2+4*(-coord[0]+self.a)^3*(-coord[0]+self.b)^4*(-coord[1]+self.c)^4*(-coord[1]+self.d)^2

    def partialGxy3690(self,coord):

        return 4*(-coord[0]+self.a)^4*(-coord[0]+self.b)^3*(-coord[1]+self.d)^3+4*(-coord[0]+self.a)^3*(-coord[0]+self.b)^4*(-coord[1]+self.d)^3

    def partialGxy3691(self,coord):

        return 4*(-coord[0]+self.a)^4*(-coord[0]+self.b)^3*(-coord[1]+self.c)*(-coord[1]+self.d)^3+4*(-coord[0]+self.a)^3*(-coord[0]+self.b)^4*(-coord[1]+self.c)*(-coord[1]+self.d)^3

    def partialGxy3692(self,coord):

        return 4*(-coord[0]+self.a)^4*(-coord[0]+self.b)^3*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3+4*(-coord[0]+self.a)^3*(-coord[0]+self.b)^4*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3

    def partialGxy3693(self,coord):

        return 4*(-coord[0]+self.a)^4*(-coord[0]+self.b)^3*(-coord[1]+self.c)^3*(-coord[1]+self.d)^3+4*(-coord[0]+self.a)^3*(-coord[0]+self.b)^4*(-coord[1]+self.c)^3*(-coord[1]+self.d)^3

    def partialGxy3694(self,coord):

        return 4*(-coord[0]+self.a)^4*(-coord[0]+self.b)^3*(-coord[1]+self.c)^4*(-coord[1]+self.d)^3+4*(-coord[0]+self.a)^3*(-coord[0]+self.b)^4*(-coord[1]+self.c)^4*(-coord[1]+self.d)^3

    def partialGxy3695(self,coord):

        return 4*(-coord[0]+self.a)^4*(-coord[0]+self.b)^3*(-coord[1]+self.d)^4+4*(-coord[0]+self.a)^3*(-coord[0]+self.b)^4*(-coord[1]+self.d)^4

    def partialGxy3696(self,coord):

        return 4*(-coord[0]+self.a)^4*(-coord[0]+self.b)^3*(-coord[1]+self.c)*(-coord[1]+self.d)^4+4*(-coord[0]+self.a)^3*(-coord[0]+self.b)^4*(-coord[1]+self.c)*(-coord[1]+self.d)^4

    def partialGxy3697(self,coord):

        return 4*(-coord[0]+self.a)^4*(-coord[0]+self.b)^3*(-coord[1]+self.c)^2*(-coord[1]+self.d)^4+4*(-coord[0]+self.a)^3*(-coord[0]+self.b)^4*(-coord[1]+self.c)^2*(-coord[1]+self.d)^4

    def partialGxy3698(self,coord):

        return 4*(-coord[0]+self.a)^4*(-coord[0]+self.b)^3*(-coord[1]+self.c)^3*(-coord[1]+self.d)^4+4*(-coord[0]+self.a)^3*(-coord[0]+self.b)^4*(-coord[1]+self.c)^3*(-coord[1]+self.d)^4

    def partialGxy3699(self,coord):

        return 4*(-coord[0]+self.a)^4*(-coord[0]+self.b)^3*(-coord[1]+self.c)^4*(-coord[1]+self.d)^4+4*(-coord[0]+self.a)^3*(-coord[0]+self.b)^4*(-coord[1]+self.c)^4*(-coord[1]+self.d)^4

    def partialGxy3706(self,coord):

        return 4*(-coord[0]+self.a)^4*(-coord[0]+self.b)^3*(-coord[1]+self.c)+4*(-coord[0]+self.a)^3*(-coord[0]+self.b)^4*(-coord[1]+self.c)+4*(-coord[0]+self.a)^4*(-coord[0]+self.b)^3*(-coord[1]+self.d)+4*(-coord[0]+self.a)^3*(-coord[0]+self.b)^4*(-coord[1]+self.d)

    def partialGxy3707(self,coord):

        return 4*(-coord[0]+self.a)^4*(-coord[0]+self.b)^3*(-coord[1]+self.c)^2+4*(-coord[0]+self.a)^3*(-coord[0]+self.b)^4*(-coord[1]+self.c)^2+8*(-coord[0]+self.a)^4*(-coord[0]+self.b)^3*(-coord[1]+self.c)*(-coord[1]+self.d)+8*(-coord[0]+self.a)^3*(-coord[0]+self.b)^4*(-coord[1]+self.c)*(-coord[1]+self.d)

    def partialGxy3708(self,coord):

        return 4*(-coord[0]+self.a)^4*(-coord[0]+self.b)^3*(-coord[1]+self.c)^3+4*(-coord[0]+self.a)^3*(-coord[0]+self.b)^4*(-coord[1]+self.c)^3+12*(-coord[0]+self.a)^4*(-coord[0]+self.b)^3*(-coord[1]+self.c)^2*(-coord[1]+self.d)+12*(-coord[0]+self.a)^3*(-coord[0]+self.b)^4*(-coord[1]+self.c)^2*(-coord[1]+self.d)

    def partialGxy3709(self,coord):

        return 4*(-coord[0]+self.a)^4*(-coord[0]+self.b)^3*(-coord[1]+self.c)^4+4*(-coord[0]+self.a)^3*(-coord[0]+self.b)^4*(-coord[1]+self.c)^4+16*(-coord[0]+self.a)^4*(-coord[0]+self.b)^3*(-coord[1]+self.c)^3*(-coord[1]+self.d)+16*(-coord[0]+self.a)^3*(-coord[0]+self.b)^4*(-coord[1]+self.c)^3*(-coord[1]+self.d)

    def partialGxy3711(self,coord):

        return 8*(-coord[0]+self.a)^4*(-coord[0]+self.b)^3*(-coord[1]+self.c)*(-coord[1]+self.d)+8*(-coord[0]+self.a)^3*(-coord[0]+self.b)^4*(-coord[1]+self.c)*(-coord[1]+self.d)+4*(-coord[0]+self.a)^4*(-coord[0]+self.b)^3*(-coord[1]+self.d)^2+4*(-coord[0]+self.a)^3*(-coord[0]+self.b)^4*(-coord[1]+self.d)^2

    def partialGxy3712(self,coord):

        return 8*(-coord[0]+self.a)^4*(-coord[0]+self.b)^3*(-coord[1]+self.c)^2*(-coord[1]+self.d)+8*(-coord[0]+self.a)^3*(-coord[0]+self.b)^4*(-coord[1]+self.c)^2*(-coord[1]+self.d)+8*(-coord[0]+self.a)^4*(-coord[0]+self.b)^3*(-coord[1]+self.c)*(-coord[1]+self.d)^2+8*(-coord[0]+self.a)^3*(-coord[0]+self.b)^4*(-coord[1]+self.c)*(-coord[1]+self.d)^2

    def partialGxy3713(self,coord):

        return 8*(-coord[0]+self.a)^4*(-coord[0]+self.b)^3*(-coord[1]+self.c)^3*(-coord[1]+self.d)+8*(-coord[0]+self.a)^3*(-coord[0]+self.b)^4*(-coord[1]+self.c)^3*(-coord[1]+self.d)+12*(-coord[0]+self.a)^4*(-coord[0]+self.b)^3*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2+12*(-coord[0]+self.a)^3*(-coord[0]+self.b)^4*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2

    def partialGxy3714(self,coord):

        return 8*(-coord[0]+self.a)^4*(-coord[0]+self.b)^3*(-coord[1]+self.c)^4*(-coord[1]+self.d)+8*(-coord[0]+self.a)^3*(-coord[0]+self.b)^4*(-coord[1]+self.c)^4*(-coord[1]+self.d)+16*(-coord[0]+self.a)^4*(-coord[0]+self.b)^3*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2+16*(-coord[0]+self.a)^3*(-coord[0]+self.b)^4*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2

    def partialGxy3716(self,coord):

        return 12*(-coord[0]+self.a)^4*(-coord[0]+self.b)^3*(-coord[1]+self.c)*(-coord[1]+self.d)^2+12*(-coord[0]+self.a)^3*(-coord[0]+self.b)^4*(-coord[1]+self.c)*(-coord[1]+self.d)^2+4*(-coord[0]+self.a)^4*(-coord[0]+self.b)^3*(-coord[1]+self.d)^3+4*(-coord[0]+self.a)^3*(-coord[0]+self.b)^4*(-coord[1]+self.d)^3

    def partialGxy3717(self,coord):

        return 12*(-coord[0]+self.a)^4*(-coord[0]+self.b)^3*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2+12*(-coord[0]+self.a)^3*(-coord[0]+self.b)^4*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2+8*(-coord[0]+self.a)^4*(-coord[0]+self.b)^3*(-coord[1]+self.c)*(-coord[1]+self.d)^3+8*(-coord[0]+self.a)^3*(-coord[0]+self.b)^4*(-coord[1]+self.c)*(-coord[1]+self.d)^3

    def partialGxy3718(self,coord):

        return 12*(-coord[0]+self.a)^4*(-coord[0]+self.b)^3*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2+12*(-coord[0]+self.a)^3*(-coord[0]+self.b)^4*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2+12*(-coord[0]+self.a)^4*(-coord[0]+self.b)^3*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3+12*(-coord[0]+self.a)^3*(-coord[0]+self.b)^4*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3

    def partialGxy3719(self,coord):

        return 12*(-coord[0]+self.a)^4*(-coord[0]+self.b)^3*(-coord[1]+self.c)^4*(-coord[1]+self.d)^2+12*(-coord[0]+self.a)^3*(-coord[0]+self.b)^4*(-coord[1]+self.c)^4*(-coord[1]+self.d)^2+16*(-coord[0]+self.a)^4*(-coord[0]+self.b)^3*(-coord[1]+self.c)^3*(-coord[1]+self.d)^3+16*(-coord[0]+self.a)^3*(-coord[0]+self.b)^4*(-coord[1]+self.c)^3*(-coord[1]+self.d)^3

    def partialGxy3721(self,coord):

        return 16*(-coord[0]+self.a)^4*(-coord[0]+self.b)^3*(-coord[1]+self.c)*(-coord[1]+self.d)^3+16*(-coord[0]+self.a)^3*(-coord[0]+self.b)^4*(-coord[1]+self.c)*(-coord[1]+self.d)^3+4*(-coord[0]+self.a)^4*(-coord[0]+self.b)^3*(-coord[1]+self.d)^4+4*(-coord[0]+self.a)^3*(-coord[0]+self.b)^4*(-coord[1]+self.d)^4

    def partialGxy3722(self,coord):

        return 16*(-coord[0]+self.a)^4*(-coord[0]+self.b)^3*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3+16*(-coord[0]+self.a)^3*(-coord[0]+self.b)^4*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3+8*(-coord[0]+self.a)^4*(-coord[0]+self.b)^3*(-coord[1]+self.c)*(-coord[1]+self.d)^4+8*(-coord[0]+self.a)^3*(-coord[0]+self.b)^4*(-coord[1]+self.c)*(-coord[1]+self.d)^4

    def partialGxy3723(self,coord):

        return 16*(-coord[0]+self.a)^4*(-coord[0]+self.b)^3*(-coord[1]+self.c)^3*(-coord[1]+self.d)^3+16*(-coord[0]+self.a)^3*(-coord[0]+self.b)^4*(-coord[1]+self.c)^3*(-coord[1]+self.d)^3+12*(-coord[0]+self.a)^4*(-coord[0]+self.b)^3*(-coord[1]+self.c)^2*(-coord[1]+self.d)^4+12*(-coord[0]+self.a)^3*(-coord[0]+self.b)^4*(-coord[1]+self.c)^2*(-coord[1]+self.d)^4

    def partialGxy3724(self,coord):

        return 16*(-coord[0]+self.a)^4*(-coord[0]+self.b)^3*(-coord[1]+self.c)^4*(-coord[1]+self.d)^3+16*(-coord[0]+self.a)^3*(-coord[0]+self.b)^4*(-coord[1]+self.c)^4*(-coord[1]+self.d)^3+16*(-coord[0]+self.a)^4*(-coord[0]+self.b)^3*(-coord[1]+self.c)^3*(-coord[1]+self.d)^4+16*(-coord[0]+self.a)^3*(-coord[0]+self.b)^4*(-coord[1]+self.c)^3*(-coord[1]+self.d)^4

    def partialGxy3737(self,coord):

        return 4*(-coord[0]+self.a)^4*(-coord[0]+self.b)^3*(2*(-coord[1]+self.c)^2+8*(-coord[1]+self.c)*(-coord[1]+self.d)+2*(-coord[1]+self.d)^2)+4*(-coord[0]+self.a)^3*(-coord[0]+self.b)^4*(2*(-coord[1]+self.c)^2+8*(-coord[1]+self.c)*(-coord[1]+self.d)+2*(-coord[1]+self.d)^2)

    def partialGxy3738(self,coord):

        return 4*(-coord[0]+self.a)^4*(-coord[0]+self.b)^3*(2*(-coord[1]+self.c)^3+12*(-coord[1]+self.c)^2*(-coord[1]+self.d)+6*(-coord[1]+self.c)*(-coord[1]+self.d)^2)+4*(-coord[0]+self.a)^3*(-coord[0]+self.b)^4*(2*(-coord[1]+self.c)^3+12*(-coord[1]+self.c)^2*(-coord[1]+self.d)+6*(-coord[1]+self.c)*(-coord[1]+self.d)^2)

    def partialGxy3739(self,coord):

        return 4*(-coord[0]+self.a)^4*(-coord[0]+self.b)^3*(2*(-coord[1]+self.c)^4+16*(-coord[1]+self.c)^3*(-coord[1]+self.d)+12*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2)+4*(-coord[0]+self.a)^3*(-coord[0]+self.b)^4*(2*(-coord[1]+self.c)^4+16*(-coord[1]+self.c)^3*(-coord[1]+self.d)+12*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2)

    def partialGxy3742(self,coord):

        return 4*(-coord[0]+self.a)^4*(-coord[0]+self.b)^3*(6*(-coord[1]+self.c)^2*(-coord[1]+self.d)+12*(-coord[1]+self.c)*(-coord[1]+self.d)^2+2*(-coord[1]+self.d)^3)+4*(-coord[0]+self.a)^3*(-coord[0]+self.b)^4*(6*(-coord[1]+self.c)^2*(-coord[1]+self.d)+12*(-coord[1]+self.c)*(-coord[1]+self.d)^2+2*(-coord[1]+self.d)^3)

    def partialGxy3743(self,coord):

        return 4*(-coord[0]+self.a)^4*(-coord[0]+self.b)^3*(6*(-coord[1]+self.c)^3*(-coord[1]+self.d)+18*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2+6*(-coord[1]+self.c)*(-coord[1]+self.d)^3)+4*(-coord[0]+self.a)^3*(-coord[0]+self.b)^4*(6*(-coord[1]+self.c)^3*(-coord[1]+self.d)+18*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2+6*(-coord[1]+self.c)*(-coord[1]+self.d)^3)

    def partialGxy3744(self,coord):

        return 4*(-coord[0]+self.a)^4*(-coord[0]+self.b)^3*(6*(-coord[1]+self.c)^4*(-coord[1]+self.d)+24*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2+12*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3)+4*(-coord[0]+self.a)^3*(-coord[0]+self.b)^4*(6*(-coord[1]+self.c)^4*(-coord[1]+self.d)+24*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2+12*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3)

    def partialGxy3747(self,coord):

        return 4*(-coord[0]+self.a)^4*(-coord[0]+self.b)^3*(12*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2+16*(-coord[1]+self.c)*(-coord[1]+self.d)^3+2*(-coord[1]+self.d)^4)+4*(-coord[0]+self.a)^3*(-coord[0]+self.b)^4*(12*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2+16*(-coord[1]+self.c)*(-coord[1]+self.d)^3+2*(-coord[1]+self.d)^4)

    def partialGxy3748(self,coord):

        return 4*(-coord[0]+self.a)^4*(-coord[0]+self.b)^3*(12*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2+24*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3+6*(-coord[1]+self.c)*(-coord[1]+self.d)^4)+4*(-coord[0]+self.a)^3*(-coord[0]+self.b)^4*(12*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2+24*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3+6*(-coord[1]+self.c)*(-coord[1]+self.d)^4)

    def partialGxy3749(self,coord):

        return 4*(-coord[0]+self.a)^4*(-coord[0]+self.b)^3*(12*(-coord[1]+self.c)^4*(-coord[1]+self.d)^2+32*(-coord[1]+self.c)^3*(-coord[1]+self.d)^3+12*(-coord[1]+self.c)^2*(-coord[1]+self.d)^4)+4*(-coord[0]+self.a)^3*(-coord[0]+self.b)^4*(12*(-coord[1]+self.c)^4*(-coord[1]+self.d)^2+32*(-coord[1]+self.c)^3*(-coord[1]+self.d)^3+12*(-coord[1]+self.c)^2*(-coord[1]+self.d)^4)

    def partialGxy4650(self,coord):

        return 2*(-coord[0]+self.a)^2+8*(-coord[0]+self.a)*(-coord[0]+self.b)+2*(-coord[0]+self.b)^2

    def partialGxy4651(self,coord):

        return (2*(-coord[0]+self.a)^2+8*(-coord[0]+self.a)*(-coord[0]+self.b)+2*(-coord[0]+self.b)^2)*(-coord[1]+self.c)

    def partialGxy4652(self,coord):

        return (2*(-coord[0]+self.a)^2+8*(-coord[0]+self.a)*(-coord[0]+self.b)+2*(-coord[0]+self.b)^2)*(-coord[1]+self.c)^2

    def partialGxy4653(self,coord):

        return (2*(-coord[0]+self.a)^2+8*(-coord[0]+self.a)*(-coord[0]+self.b)+2*(-coord[0]+self.b)^2)*(-coord[1]+self.c)^3

    def partialGxy4654(self,coord):

        return (2*(-coord[0]+self.a)^2+8*(-coord[0]+self.a)*(-coord[0]+self.b)+2*(-coord[0]+self.b)^2)*(-coord[1]+self.c)^4

    def partialGxy4655(self,coord):

        return (2*(-coord[0]+self.a)^2+8*(-coord[0]+self.a)*(-coord[0]+self.b)+2*(-coord[0]+self.b)^2)*(-coord[1]+self.d)

    def partialGxy4656(self,coord):

        return (2*(-coord[0]+self.a)^2+8*(-coord[0]+self.a)*(-coord[0]+self.b)+2*(-coord[0]+self.b)^2)*(-coord[1]+self.c)*(-coord[1]+self.d)

    def partialGxy4657(self,coord):

        return (2*(-coord[0]+self.a)^2+8*(-coord[0]+self.a)*(-coord[0]+self.b)+2*(-coord[0]+self.b)^2)*(-coord[1]+self.c)^2*(-coord[1]+self.d)

    def partialGxy4658(self,coord):

        return (2*(-coord[0]+self.a)^2+8*(-coord[0]+self.a)*(-coord[0]+self.b)+2*(-coord[0]+self.b)^2)*(-coord[1]+self.c)^3*(-coord[1]+self.d)

    def partialGxy4659(self,coord):

        return (2*(-coord[0]+self.a)^2+8*(-coord[0]+self.a)*(-coord[0]+self.b)+2*(-coord[0]+self.b)^2)*(-coord[1]+self.c)^4*(-coord[1]+self.d)

    def partialGxy4660(self,coord):

        return (2*(-coord[0]+self.a)^2+8*(-coord[0]+self.a)*(-coord[0]+self.b)+2*(-coord[0]+self.b)^2)*(-coord[1]+self.d)^2

    def partialGxy4661(self,coord):

        return (2*(-coord[0]+self.a)^2+8*(-coord[0]+self.a)*(-coord[0]+self.b)+2*(-coord[0]+self.b)^2)*(-coord[1]+self.c)*(-coord[1]+self.d)^2

    def partialGxy4662(self,coord):

        return (2*(-coord[0]+self.a)^2+8*(-coord[0]+self.a)*(-coord[0]+self.b)+2*(-coord[0]+self.b)^2)*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2

    def partialGxy4663(self,coord):

        return (2*(-coord[0]+self.a)^2+8*(-coord[0]+self.a)*(-coord[0]+self.b)+2*(-coord[0]+self.b)^2)*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2

    def partialGxy4664(self,coord):

        return (2*(-coord[0]+self.a)^2+8*(-coord[0]+self.a)*(-coord[0]+self.b)+2*(-coord[0]+self.b)^2)*(-coord[1]+self.c)^4*(-coord[1]+self.d)^2

    def partialGxy4665(self,coord):

        return (2*(-coord[0]+self.a)^2+8*(-coord[0]+self.a)*(-coord[0]+self.b)+2*(-coord[0]+self.b)^2)*(-coord[1]+self.d)^3

    def partialGxy4666(self,coord):

        return (2*(-coord[0]+self.a)^2+8*(-coord[0]+self.a)*(-coord[0]+self.b)+2*(-coord[0]+self.b)^2)*(-coord[1]+self.c)*(-coord[1]+self.d)^3

    def partialGxy4667(self,coord):

        return (2*(-coord[0]+self.a)^2+8*(-coord[0]+self.a)*(-coord[0]+self.b)+2*(-coord[0]+self.b)^2)*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3

    def partialGxy4668(self,coord):

        return (2*(-coord[0]+self.a)^2+8*(-coord[0]+self.a)*(-coord[0]+self.b)+2*(-coord[0]+self.b)^2)*(-coord[1]+self.c)^3*(-coord[1]+self.d)^3

    def partialGxy4669(self,coord):

        return (2*(-coord[0]+self.a)^2+8*(-coord[0]+self.a)*(-coord[0]+self.b)+2*(-coord[0]+self.b)^2)*(-coord[1]+self.c)^4*(-coord[1]+self.d)^3

    def partialGxy4670(self,coord):

        return (2*(-coord[0]+self.a)^2+8*(-coord[0]+self.a)*(-coord[0]+self.b)+2*(-coord[0]+self.b)^2)*(-coord[1]+self.d)^4

    def partialGxy4671(self,coord):

        return (2*(-coord[0]+self.a)^2+8*(-coord[0]+self.a)*(-coord[0]+self.b)+2*(-coord[0]+self.b)^2)*(-coord[1]+self.c)*(-coord[1]+self.d)^4

    def partialGxy4672(self,coord):

        return (2*(-coord[0]+self.a)^2+8*(-coord[0]+self.a)*(-coord[0]+self.b)+2*(-coord[0]+self.b)^2)*(-coord[1]+self.c)^2*(-coord[1]+self.d)^4

    def partialGxy4673(self,coord):

        return (2*(-coord[0]+self.a)^2+8*(-coord[0]+self.a)*(-coord[0]+self.b)+2*(-coord[0]+self.b)^2)*(-coord[1]+self.c)^3*(-coord[1]+self.d)^4

    def partialGxy4674(self,coord):

        return (2*(-coord[0]+self.a)^2+8*(-coord[0]+self.a)*(-coord[0]+self.b)+2*(-coord[0]+self.b)^2)*(-coord[1]+self.c)^4*(-coord[1]+self.d)^4

    def partialGxy4681(self,coord):

        return (2*(-coord[0]+self.a)^2+8*(-coord[0]+self.a)*(-coord[0]+self.b)+2*(-coord[0]+self.b)^2)*(-coord[1]+self.c)+(2*(-coord[0]+self.a)^2+8*(-coord[0]+self.a)*(-coord[0]+self.b)+2*(-coord[0]+self.b)^2)*(-coord[1]+self.d)

    def partialGxy4682(self,coord):

        return (2*(-coord[0]+self.a)^2+8*(-coord[0]+self.a)*(-coord[0]+self.b)+2*(-coord[0]+self.b)^2)*(-coord[1]+self.c)^2+2*(2*(-coord[0]+self.a)^2+8*(-coord[0]+self.a)*(-coord[0]+self.b)+2*(-coord[0]+self.b)^2)*(-coord[1]+self.c)*(-coord[1]+self.d)

    def partialGxy4683(self,coord):

        return (2*(-coord[0]+self.a)^2+8*(-coord[0]+self.a)*(-coord[0]+self.b)+2*(-coord[0]+self.b)^2)*(-coord[1]+self.c)^3+3*(2*(-coord[0]+self.a)^2+8*(-coord[0]+self.a)*(-coord[0]+self.b)+2*(-coord[0]+self.b)^2)*(-coord[1]+self.c)^2*(-coord[1]+self.d)

    def partialGxy4684(self,coord):

        return (2*(-coord[0]+self.a)^2+8*(-coord[0]+self.a)*(-coord[0]+self.b)+2*(-coord[0]+self.b)^2)*(-coord[1]+self.c)^4+4*(2*(-coord[0]+self.a)^2+8*(-coord[0]+self.a)*(-coord[0]+self.b)+2*(-coord[0]+self.b)^2)*(-coord[1]+self.c)^3*(-coord[1]+self.d)

    def partialGxy4686(self,coord):

        return 2*(2*(-coord[0]+self.a)^2+8*(-coord[0]+self.a)*(-coord[0]+self.b)+2*(-coord[0]+self.b)^2)*(-coord[1]+self.c)*(-coord[1]+self.d)+(2*(-coord[0]+self.a)^2+8*(-coord[0]+self.a)*(-coord[0]+self.b)+2*(-coord[0]+self.b)^2)*(-coord[1]+self.d)^2

    def partialGxy4687(self,coord):

        return 2*(2*(-coord[0]+self.a)^2+8*(-coord[0]+self.a)*(-coord[0]+self.b)+2*(-coord[0]+self.b)^2)*(-coord[1]+self.c)^2*(-coord[1]+self.d)+2*(2*(-coord[0]+self.a)^2+8*(-coord[0]+self.a)*(-coord[0]+self.b)+2*(-coord[0]+self.b)^2)*(-coord[1]+self.c)*(-coord[1]+self.d)^2

    def partialGxy4688(self,coord):

        return 2*(2*(-coord[0]+self.a)^2+8*(-coord[0]+self.a)*(-coord[0]+self.b)+2*(-coord[0]+self.b)^2)*(-coord[1]+self.c)^3*(-coord[1]+self.d)+3*(2*(-coord[0]+self.a)^2+8*(-coord[0]+self.a)*(-coord[0]+self.b)+2*(-coord[0]+self.b)^2)*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2

    def partialGxy4689(self,coord):

        return 2*(2*(-coord[0]+self.a)^2+8*(-coord[0]+self.a)*(-coord[0]+self.b)+2*(-coord[0]+self.b)^2)*(-coord[1]+self.c)^4*(-coord[1]+self.d)+4*(2*(-coord[0]+self.a)^2+8*(-coord[0]+self.a)*(-coord[0]+self.b)+2*(-coord[0]+self.b)^2)*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2

    def partialGxy4691(self,coord):

        return 3*(2*(-coord[0]+self.a)^2+8*(-coord[0]+self.a)*(-coord[0]+self.b)+2*(-coord[0]+self.b)^2)*(-coord[1]+self.c)*(-coord[1]+self.d)^2+(2*(-coord[0]+self.a)^2+8*(-coord[0]+self.a)*(-coord[0]+self.b)+2*(-coord[0]+self.b)^2)*(-coord[1]+self.d)^3

    def partialGxy4692(self,coord):

        return 3*(2*(-coord[0]+self.a)^2+8*(-coord[0]+self.a)*(-coord[0]+self.b)+2*(-coord[0]+self.b)^2)*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2+2*(2*(-coord[0]+self.a)^2+8*(-coord[0]+self.a)*(-coord[0]+self.b)+2*(-coord[0]+self.b)^2)*(-coord[1]+self.c)*(-coord[1]+self.d)^3

    def partialGxy4693(self,coord):

        return 3*(2*(-coord[0]+self.a)^2+8*(-coord[0]+self.a)*(-coord[0]+self.b)+2*(-coord[0]+self.b)^2)*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2+3*(2*(-coord[0]+self.a)^2+8*(-coord[0]+self.a)*(-coord[0]+self.b)+2*(-coord[0]+self.b)^2)*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3

    def partialGxy4694(self,coord):

        return 3*(2*(-coord[0]+self.a)^2+8*(-coord[0]+self.a)*(-coord[0]+self.b)+2*(-coord[0]+self.b)^2)*(-coord[1]+self.c)^4*(-coord[1]+self.d)^2+4*(2*(-coord[0]+self.a)^2+8*(-coord[0]+self.a)*(-coord[0]+self.b)+2*(-coord[0]+self.b)^2)*(-coord[1]+self.c)^3*(-coord[1]+self.d)^3

    def partialGxy4696(self,coord):

        return 4*(2*(-coord[0]+self.a)^2+8*(-coord[0]+self.a)*(-coord[0]+self.b)+2*(-coord[0]+self.b)^2)*(-coord[1]+self.c)*(-coord[1]+self.d)^3+(2*(-coord[0]+self.a)^2+8*(-coord[0]+self.a)*(-coord[0]+self.b)+2*(-coord[0]+self.b)^2)*(-coord[1]+self.d)^4

    def partialGxy4697(self,coord):

        return 4*(2*(-coord[0]+self.a)^2+8*(-coord[0]+self.a)*(-coord[0]+self.b)+2*(-coord[0]+self.b)^2)*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3+2*(2*(-coord[0]+self.a)^2+8*(-coord[0]+self.a)*(-coord[0]+self.b)+2*(-coord[0]+self.b)^2)*(-coord[1]+self.c)*(-coord[1]+self.d)^4

    def partialGxy4698(self,coord):

        return 4*(2*(-coord[0]+self.a)^2+8*(-coord[0]+self.a)*(-coord[0]+self.b)+2*(-coord[0]+self.b)^2)*(-coord[1]+self.c)^3*(-coord[1]+self.d)^3+3*(2*(-coord[0]+self.a)^2+8*(-coord[0]+self.a)*(-coord[0]+self.b)+2*(-coord[0]+self.b)^2)*(-coord[1]+self.c)^2*(-coord[1]+self.d)^4

    def partialGxy4699(self,coord):

        return 4*(2*(-coord[0]+self.a)^2+8*(-coord[0]+self.a)*(-coord[0]+self.b)+2*(-coord[0]+self.b)^2)*(-coord[1]+self.c)^4*(-coord[1]+self.d)^3+4*(2*(-coord[0]+self.a)^2+8*(-coord[0]+self.a)*(-coord[0]+self.b)+2*(-coord[0]+self.b)^2)*(-coord[1]+self.c)^3*(-coord[1]+self.d)^4

    def partialGxy4712(self,coord):

        return 2*(2*(-coord[0]+self.a)^2+8*(-coord[0]+self.a)*(-coord[0]+self.b)+2*(-coord[0]+self.b)^2)*(-coord[1]+self.c)^2+8*(2*(-coord[0]+self.a)^2+8*(-coord[0]+self.a)*(-coord[0]+self.b)+2*(-coord[0]+self.b)^2)*(-coord[1]+self.c)*(-coord[1]+self.d)+2*(2*(-coord[0]+self.a)^2+8*(-coord[0]+self.a)*(-coord[0]+self.b)+2*(-coord[0]+self.b)^2)*(-coord[1]+self.d)^2

    def partialGxy4713(self,coord):

        return 2*(2*(-coord[0]+self.a)^2+8*(-coord[0]+self.a)*(-coord[0]+self.b)+2*(-coord[0]+self.b)^2)*(-coord[1]+self.c)^3+12*(2*(-coord[0]+self.a)^2+8*(-coord[0]+self.a)*(-coord[0]+self.b)+2*(-coord[0]+self.b)^2)*(-coord[1]+self.c)^2*(-coord[1]+self.d)+6*(2*(-coord[0]+self.a)^2+8*(-coord[0]+self.a)*(-coord[0]+self.b)+2*(-coord[0]+self.b)^2)*(-coord[1]+self.c)*(-coord[1]+self.d)^2

    def partialGxy4714(self,coord):

        return 2*(2*(-coord[0]+self.a)^2+8*(-coord[0]+self.a)*(-coord[0]+self.b)+2*(-coord[0]+self.b)^2)*(-coord[1]+self.c)^4+16*(2*(-coord[0]+self.a)^2+8*(-coord[0]+self.a)*(-coord[0]+self.b)+2*(-coord[0]+self.b)^2)*(-coord[1]+self.c)^3*(-coord[1]+self.d)+12*(2*(-coord[0]+self.a)^2+8*(-coord[0]+self.a)*(-coord[0]+self.b)+2*(-coord[0]+self.b)^2)*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2

    def partialGxy4717(self,coord):

        return 6*(2*(-coord[0]+self.a)^2+8*(-coord[0]+self.a)*(-coord[0]+self.b)+2*(-coord[0]+self.b)^2)*(-coord[1]+self.c)^2*(-coord[1]+self.d)+12*(2*(-coord[0]+self.a)^2+8*(-coord[0]+self.a)*(-coord[0]+self.b)+2*(-coord[0]+self.b)^2)*(-coord[1]+self.c)*(-coord[1]+self.d)^2+2*(2*(-coord[0]+self.a)^2+8*(-coord[0]+self.a)*(-coord[0]+self.b)+2*(-coord[0]+self.b)^2)*(-coord[1]+self.d)^3

    def partialGxy4718(self,coord):

        return 6*(2*(-coord[0]+self.a)^2+8*(-coord[0]+self.a)*(-coord[0]+self.b)+2*(-coord[0]+self.b)^2)*(-coord[1]+self.c)^3*(-coord[1]+self.d)+18*(2*(-coord[0]+self.a)^2+8*(-coord[0]+self.a)*(-coord[0]+self.b)+2*(-coord[0]+self.b)^2)*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2+6*(2*(-coord[0]+self.a)^2+8*(-coord[0]+self.a)*(-coord[0]+self.b)+2*(-coord[0]+self.b)^2)*(-coord[1]+self.c)*(-coord[1]+self.d)^3

    def partialGxy4719(self,coord):

        return 6*(2*(-coord[0]+self.a)^2+8*(-coord[0]+self.a)*(-coord[0]+self.b)+2*(-coord[0]+self.b)^2)*(-coord[1]+self.c)^4*(-coord[1]+self.d)+24*(2*(-coord[0]+self.a)^2+8*(-coord[0]+self.a)*(-coord[0]+self.b)+2*(-coord[0]+self.b)^2)*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2+12*(2*(-coord[0]+self.a)^2+8*(-coord[0]+self.a)*(-coord[0]+self.b)+2*(-coord[0]+self.b)^2)*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3

    def partialGxy4722(self,coord):

        return 12*(2*(-coord[0]+self.a)^2+8*(-coord[0]+self.a)*(-coord[0]+self.b)+2*(-coord[0]+self.b)^2)*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2+16*(2*(-coord[0]+self.a)^2+8*(-coord[0]+self.a)*(-coord[0]+self.b)+2*(-coord[0]+self.b)^2)*(-coord[1]+self.c)*(-coord[1]+self.d)^3+2*(2*(-coord[0]+self.a)^2+8*(-coord[0]+self.a)*(-coord[0]+self.b)+2*(-coord[0]+self.b)^2)*(-coord[1]+self.d)^4

    def partialGxy4723(self,coord):

        return 12*(2*(-coord[0]+self.a)^2+8*(-coord[0]+self.a)*(-coord[0]+self.b)+2*(-coord[0]+self.b)^2)*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2+24*(2*(-coord[0]+self.a)^2+8*(-coord[0]+self.a)*(-coord[0]+self.b)+2*(-coord[0]+self.b)^2)*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3+6*(2*(-coord[0]+self.a)^2+8*(-coord[0]+self.a)*(-coord[0]+self.b)+2*(-coord[0]+self.b)^2)*(-coord[1]+self.c)*(-coord[1]+self.d)^4

    def partialGxy4724(self,coord):

        return 12*(2*(-coord[0]+self.a)^2+8*(-coord[0]+self.a)*(-coord[0]+self.b)+2*(-coord[0]+self.b)^2)*(-coord[1]+self.c)^4*(-coord[1]+self.d)^2+32*(2*(-coord[0]+self.a)^2+8*(-coord[0]+self.a)*(-coord[0]+self.b)+2*(-coord[0]+self.b)^2)*(-coord[1]+self.c)^3*(-coord[1]+self.d)^3+12*(2*(-coord[0]+self.a)^2+8*(-coord[0]+self.a)*(-coord[0]+self.b)+2*(-coord[0]+self.b)^2)*(-coord[1]+self.c)^2*(-coord[1]+self.d)^4

    def partialGxy4725(self,coord):

        return 2*(-coord[0]+self.a)^3+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)+6*(-coord[0]+self.a)*(-coord[0]+self.b)^2

    def partialGxy4726(self,coord):

        return (2*(-coord[0]+self.a)^3+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)+6*(-coord[0]+self.a)*(-coord[0]+self.b)^2)*(-coord[1]+self.c)

    def partialGxy4727(self,coord):

        return (2*(-coord[0]+self.a)^3+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)+6*(-coord[0]+self.a)*(-coord[0]+self.b)^2)*(-coord[1]+self.c)^2

    def partialGxy4728(self,coord):

        return (2*(-coord[0]+self.a)^3+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)+6*(-coord[0]+self.a)*(-coord[0]+self.b)^2)*(-coord[1]+self.c)^3

    def partialGxy4729(self,coord):

        return (2*(-coord[0]+self.a)^3+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)+6*(-coord[0]+self.a)*(-coord[0]+self.b)^2)*(-coord[1]+self.c)^4

    def partialGxy4730(self,coord):

        return (2*(-coord[0]+self.a)^3+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)+6*(-coord[0]+self.a)*(-coord[0]+self.b)^2)*(-coord[1]+self.d)

    def partialGxy4731(self,coord):

        return (2*(-coord[0]+self.a)^3+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)+6*(-coord[0]+self.a)*(-coord[0]+self.b)^2)*(-coord[1]+self.c)*(-coord[1]+self.d)

    def partialGxy4732(self,coord):

        return (2*(-coord[0]+self.a)^3+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)+6*(-coord[0]+self.a)*(-coord[0]+self.b)^2)*(-coord[1]+self.c)^2*(-coord[1]+self.d)

    def partialGxy4733(self,coord):

        return (2*(-coord[0]+self.a)^3+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)+6*(-coord[0]+self.a)*(-coord[0]+self.b)^2)*(-coord[1]+self.c)^3*(-coord[1]+self.d)

    def partialGxy4734(self,coord):

        return (2*(-coord[0]+self.a)^3+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)+6*(-coord[0]+self.a)*(-coord[0]+self.b)^2)*(-coord[1]+self.c)^4*(-coord[1]+self.d)

    def partialGxy4735(self,coord):

        return (2*(-coord[0]+self.a)^3+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)+6*(-coord[0]+self.a)*(-coord[0]+self.b)^2)*(-coord[1]+self.d)^2

    def partialGxy4736(self,coord):

        return (2*(-coord[0]+self.a)^3+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)+6*(-coord[0]+self.a)*(-coord[0]+self.b)^2)*(-coord[1]+self.c)*(-coord[1]+self.d)^2

    def partialGxy4737(self,coord):

        return (2*(-coord[0]+self.a)^3+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)+6*(-coord[0]+self.a)*(-coord[0]+self.b)^2)*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2

    def partialGxy4738(self,coord):

        return (2*(-coord[0]+self.a)^3+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)+6*(-coord[0]+self.a)*(-coord[0]+self.b)^2)*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2

    def partialGxy4739(self,coord):

        return (2*(-coord[0]+self.a)^3+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)+6*(-coord[0]+self.a)*(-coord[0]+self.b)^2)*(-coord[1]+self.c)^4*(-coord[1]+self.d)^2

    def partialGxy4740(self,coord):

        return (2*(-coord[0]+self.a)^3+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)+6*(-coord[0]+self.a)*(-coord[0]+self.b)^2)*(-coord[1]+self.d)^3

    def partialGxy4741(self,coord):

        return (2*(-coord[0]+self.a)^3+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)+6*(-coord[0]+self.a)*(-coord[0]+self.b)^2)*(-coord[1]+self.c)*(-coord[1]+self.d)^3

    def partialGxy4742(self,coord):

        return (2*(-coord[0]+self.a)^3+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)+6*(-coord[0]+self.a)*(-coord[0]+self.b)^2)*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3

    def partialGxy4743(self,coord):

        return (2*(-coord[0]+self.a)^3+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)+6*(-coord[0]+self.a)*(-coord[0]+self.b)^2)*(-coord[1]+self.c)^3*(-coord[1]+self.d)^3

    def partialGxy4744(self,coord):

        return (2*(-coord[0]+self.a)^3+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)+6*(-coord[0]+self.a)*(-coord[0]+self.b)^2)*(-coord[1]+self.c)^4*(-coord[1]+self.d)^3

    def partialGxy4745(self,coord):

        return (2*(-coord[0]+self.a)^3+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)+6*(-coord[0]+self.a)*(-coord[0]+self.b)^2)*(-coord[1]+self.d)^4

    def partialGxy4746(self,coord):

        return (2*(-coord[0]+self.a)^3+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)+6*(-coord[0]+self.a)*(-coord[0]+self.b)^2)*(-coord[1]+self.c)*(-coord[1]+self.d)^4

    def partialGxy4747(self,coord):

        return (2*(-coord[0]+self.a)^3+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)+6*(-coord[0]+self.a)*(-coord[0]+self.b)^2)*(-coord[1]+self.c)^2*(-coord[1]+self.d)^4

    def partialGxy4748(self,coord):

        return (2*(-coord[0]+self.a)^3+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)+6*(-coord[0]+self.a)*(-coord[0]+self.b)^2)*(-coord[1]+self.c)^3*(-coord[1]+self.d)^4

    def partialGxy4749(self,coord):

        return (2*(-coord[0]+self.a)^3+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)+6*(-coord[0]+self.a)*(-coord[0]+self.b)^2)*(-coord[1]+self.c)^4*(-coord[1]+self.d)^4

    def partialGxy4756(self,coord):

        return (2*(-coord[0]+self.a)^3+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)+6*(-coord[0]+self.a)*(-coord[0]+self.b)^2)*(-coord[1]+self.c)+(2*(-coord[0]+self.a)^3+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)+6*(-coord[0]+self.a)*(-coord[0]+self.b)^2)*(-coord[1]+self.d)

    def partialGxy4757(self,coord):

        return (2*(-coord[0]+self.a)^3+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)+6*(-coord[0]+self.a)*(-coord[0]+self.b)^2)*(-coord[1]+self.c)^2+2*(2*(-coord[0]+self.a)^3+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)+6*(-coord[0]+self.a)*(-coord[0]+self.b)^2)*(-coord[1]+self.c)*(-coord[1]+self.d)

    def partialGxy4758(self,coord):

        return (2*(-coord[0]+self.a)^3+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)+6*(-coord[0]+self.a)*(-coord[0]+self.b)^2)*(-coord[1]+self.c)^3+3*(2*(-coord[0]+self.a)^3+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)+6*(-coord[0]+self.a)*(-coord[0]+self.b)^2)*(-coord[1]+self.c)^2*(-coord[1]+self.d)

    def partialGxy4759(self,coord):

        return (2*(-coord[0]+self.a)^3+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)+6*(-coord[0]+self.a)*(-coord[0]+self.b)^2)*(-coord[1]+self.c)^4+4*(2*(-coord[0]+self.a)^3+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)+6*(-coord[0]+self.a)*(-coord[0]+self.b)^2)*(-coord[1]+self.c)^3*(-coord[1]+self.d)

    def partialGxy4761(self,coord):

        return 2*(2*(-coord[0]+self.a)^3+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)+6*(-coord[0]+self.a)*(-coord[0]+self.b)^2)*(-coord[1]+self.c)*(-coord[1]+self.d)+(2*(-coord[0]+self.a)^3+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)+6*(-coord[0]+self.a)*(-coord[0]+self.b)^2)*(-coord[1]+self.d)^2

    def partialGxy4762(self,coord):

        return 2*(2*(-coord[0]+self.a)^3+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)+6*(-coord[0]+self.a)*(-coord[0]+self.b)^2)*(-coord[1]+self.c)^2*(-coord[1]+self.d)+2*(2*(-coord[0]+self.a)^3+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)+6*(-coord[0]+self.a)*(-coord[0]+self.b)^2)*(-coord[1]+self.c)*(-coord[1]+self.d)^2

    def partialGxy4763(self,coord):

        return 2*(2*(-coord[0]+self.a)^3+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)+6*(-coord[0]+self.a)*(-coord[0]+self.b)^2)*(-coord[1]+self.c)^3*(-coord[1]+self.d)+3*(2*(-coord[0]+self.a)^3+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)+6*(-coord[0]+self.a)*(-coord[0]+self.b)^2)*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2

    def partialGxy4764(self,coord):

        return 2*(2*(-coord[0]+self.a)^3+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)+6*(-coord[0]+self.a)*(-coord[0]+self.b)^2)*(-coord[1]+self.c)^4*(-coord[1]+self.d)+4*(2*(-coord[0]+self.a)^3+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)+6*(-coord[0]+self.a)*(-coord[0]+self.b)^2)*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2

    def partialGxy4766(self,coord):

        return 3*(2*(-coord[0]+self.a)^3+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)+6*(-coord[0]+self.a)*(-coord[0]+self.b)^2)*(-coord[1]+self.c)*(-coord[1]+self.d)^2+(2*(-coord[0]+self.a)^3+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)+6*(-coord[0]+self.a)*(-coord[0]+self.b)^2)*(-coord[1]+self.d)^3

    def partialGxy4767(self,coord):

        return 3*(2*(-coord[0]+self.a)^3+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)+6*(-coord[0]+self.a)*(-coord[0]+self.b)^2)*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2+2*(2*(-coord[0]+self.a)^3+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)+6*(-coord[0]+self.a)*(-coord[0]+self.b)^2)*(-coord[1]+self.c)*(-coord[1]+self.d)^3

    def partialGxy4768(self,coord):

        return 3*(2*(-coord[0]+self.a)^3+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)+6*(-coord[0]+self.a)*(-coord[0]+self.b)^2)*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2+3*(2*(-coord[0]+self.a)^3+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)+6*(-coord[0]+self.a)*(-coord[0]+self.b)^2)*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3

    def partialGxy4769(self,coord):

        return 3*(2*(-coord[0]+self.a)^3+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)+6*(-coord[0]+self.a)*(-coord[0]+self.b)^2)*(-coord[1]+self.c)^4*(-coord[1]+self.d)^2+4*(2*(-coord[0]+self.a)^3+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)+6*(-coord[0]+self.a)*(-coord[0]+self.b)^2)*(-coord[1]+self.c)^3*(-coord[1]+self.d)^3

    def partialGxy4771(self,coord):

        return 4*(2*(-coord[0]+self.a)^3+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)+6*(-coord[0]+self.a)*(-coord[0]+self.b)^2)*(-coord[1]+self.c)*(-coord[1]+self.d)^3+(2*(-coord[0]+self.a)^3+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)+6*(-coord[0]+self.a)*(-coord[0]+self.b)^2)*(-coord[1]+self.d)^4

    def partialGxy4772(self,coord):

        return 4*(2*(-coord[0]+self.a)^3+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)+6*(-coord[0]+self.a)*(-coord[0]+self.b)^2)*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3+2*(2*(-coord[0]+self.a)^3+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)+6*(-coord[0]+self.a)*(-coord[0]+self.b)^2)*(-coord[1]+self.c)*(-coord[1]+self.d)^4

    def partialGxy4773(self,coord):

        return 4*(2*(-coord[0]+self.a)^3+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)+6*(-coord[0]+self.a)*(-coord[0]+self.b)^2)*(-coord[1]+self.c)^3*(-coord[1]+self.d)^3+3*(2*(-coord[0]+self.a)^3+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)+6*(-coord[0]+self.a)*(-coord[0]+self.b)^2)*(-coord[1]+self.c)^2*(-coord[1]+self.d)^4

    def partialGxy4774(self,coord):

        return 4*(2*(-coord[0]+self.a)^3+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)+6*(-coord[0]+self.a)*(-coord[0]+self.b)^2)*(-coord[1]+self.c)^4*(-coord[1]+self.d)^3+4*(2*(-coord[0]+self.a)^3+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)+6*(-coord[0]+self.a)*(-coord[0]+self.b)^2)*(-coord[1]+self.c)^3*(-coord[1]+self.d)^4

    def partialGxy4787(self,coord):

        return 2*(2*(-coord[0]+self.a)^3+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)+6*(-coord[0]+self.a)*(-coord[0]+self.b)^2)*(-coord[1]+self.c)^2+8*(2*(-coord[0]+self.a)^3+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)+6*(-coord[0]+self.a)*(-coord[0]+self.b)^2)*(-coord[1]+self.c)*(-coord[1]+self.d)+2*(2*(-coord[0]+self.a)^3+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)+6*(-coord[0]+self.a)*(-coord[0]+self.b)^2)*(-coord[1]+self.d)^2

    def partialGxy4788(self,coord):

        return 2*(2*(-coord[0]+self.a)^3+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)+6*(-coord[0]+self.a)*(-coord[0]+self.b)^2)*(-coord[1]+self.c)^3+12*(2*(-coord[0]+self.a)^3+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)+6*(-coord[0]+self.a)*(-coord[0]+self.b)^2)*(-coord[1]+self.c)^2*(-coord[1]+self.d)+6*(2*(-coord[0]+self.a)^3+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)+6*(-coord[0]+self.a)*(-coord[0]+self.b)^2)*(-coord[1]+self.c)*(-coord[1]+self.d)^2

    def partialGxy4789(self,coord):

        return 2*(2*(-coord[0]+self.a)^3+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)+6*(-coord[0]+self.a)*(-coord[0]+self.b)^2)*(-coord[1]+self.c)^4+16*(2*(-coord[0]+self.a)^3+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)+6*(-coord[0]+self.a)*(-coord[0]+self.b)^2)*(-coord[1]+self.c)^3*(-coord[1]+self.d)+12*(2*(-coord[0]+self.a)^3+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)+6*(-coord[0]+self.a)*(-coord[0]+self.b)^2)*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2

    def partialGxy4792(self,coord):

        return 6*(2*(-coord[0]+self.a)^3+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)+6*(-coord[0]+self.a)*(-coord[0]+self.b)^2)*(-coord[1]+self.c)^2*(-coord[1]+self.d)+12*(2*(-coord[0]+self.a)^3+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)+6*(-coord[0]+self.a)*(-coord[0]+self.b)^2)*(-coord[1]+self.c)*(-coord[1]+self.d)^2+2*(2*(-coord[0]+self.a)^3+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)+6*(-coord[0]+self.a)*(-coord[0]+self.b)^2)*(-coord[1]+self.d)^3

    def partialGxy4793(self,coord):

        return 6*(2*(-coord[0]+self.a)^3+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)+6*(-coord[0]+self.a)*(-coord[0]+self.b)^2)*(-coord[1]+self.c)^3*(-coord[1]+self.d)+18*(2*(-coord[0]+self.a)^3+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)+6*(-coord[0]+self.a)*(-coord[0]+self.b)^2)*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2+6*(2*(-coord[0]+self.a)^3+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)+6*(-coord[0]+self.a)*(-coord[0]+self.b)^2)*(-coord[1]+self.c)*(-coord[1]+self.d)^3

    def partialGxy4794(self,coord):

        return 6*(2*(-coord[0]+self.a)^3+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)+6*(-coord[0]+self.a)*(-coord[0]+self.b)^2)*(-coord[1]+self.c)^4*(-coord[1]+self.d)+24*(2*(-coord[0]+self.a)^3+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)+6*(-coord[0]+self.a)*(-coord[0]+self.b)^2)*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2+12*(2*(-coord[0]+self.a)^3+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)+6*(-coord[0]+self.a)*(-coord[0]+self.b)^2)*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3

    def partialGxy4797(self,coord):

        return 12*(2*(-coord[0]+self.a)^3+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)+6*(-coord[0]+self.a)*(-coord[0]+self.b)^2)*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2+16*(2*(-coord[0]+self.a)^3+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)+6*(-coord[0]+self.a)*(-coord[0]+self.b)^2)*(-coord[1]+self.c)*(-coord[1]+self.d)^3+2*(2*(-coord[0]+self.a)^3+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)+6*(-coord[0]+self.a)*(-coord[0]+self.b)^2)*(-coord[1]+self.d)^4

    def partialGxy4798(self,coord):

        return 12*(2*(-coord[0]+self.a)^3+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)+6*(-coord[0]+self.a)*(-coord[0]+self.b)^2)*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2+24*(2*(-coord[0]+self.a)^3+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)+6*(-coord[0]+self.a)*(-coord[0]+self.b)^2)*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3+6*(2*(-coord[0]+self.a)^3+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)+6*(-coord[0]+self.a)*(-coord[0]+self.b)^2)*(-coord[1]+self.c)*(-coord[1]+self.d)^4

    def partialGxy4799(self,coord):

        return 12*(2*(-coord[0]+self.a)^3+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)+6*(-coord[0]+self.a)*(-coord[0]+self.b)^2)*(-coord[1]+self.c)^4*(-coord[1]+self.d)^2+32*(2*(-coord[0]+self.a)^3+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)+6*(-coord[0]+self.a)*(-coord[0]+self.b)^2)*(-coord[1]+self.c)^3*(-coord[1]+self.d)^3+12*(2*(-coord[0]+self.a)^3+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)+6*(-coord[0]+self.a)*(-coord[0]+self.b)^2)*(-coord[1]+self.c)^2*(-coord[1]+self.d)^4

    def partialGxy4800(self,coord):

        return 2*(-coord[0]+self.a)^4+16*(-coord[0]+self.a)^3*(-coord[0]+self.b)+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2

    def partialGxy4801(self,coord):

        return (2*(-coord[0]+self.a)^4+16*(-coord[0]+self.a)^3*(-coord[0]+self.b)+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2)*(-coord[1]+self.c)

    def partialGxy4802(self,coord):

        return (2*(-coord[0]+self.a)^4+16*(-coord[0]+self.a)^3*(-coord[0]+self.b)+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2)*(-coord[1]+self.c)^2

    def partialGxy4803(self,coord):

        return (2*(-coord[0]+self.a)^4+16*(-coord[0]+self.a)^3*(-coord[0]+self.b)+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2)*(-coord[1]+self.c)^3

    def partialGxy4804(self,coord):

        return (2*(-coord[0]+self.a)^4+16*(-coord[0]+self.a)^3*(-coord[0]+self.b)+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2)*(-coord[1]+self.c)^4

    def partialGxy4805(self,coord):

        return (2*(-coord[0]+self.a)^4+16*(-coord[0]+self.a)^3*(-coord[0]+self.b)+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2)*(-coord[1]+self.d)

    def partialGxy4806(self,coord):

        return (2*(-coord[0]+self.a)^4+16*(-coord[0]+self.a)^3*(-coord[0]+self.b)+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2)*(-coord[1]+self.c)*(-coord[1]+self.d)

    def partialGxy4807(self,coord):

        return (2*(-coord[0]+self.a)^4+16*(-coord[0]+self.a)^3*(-coord[0]+self.b)+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2)*(-coord[1]+self.c)^2*(-coord[1]+self.d)

    def partialGxy4808(self,coord):

        return (2*(-coord[0]+self.a)^4+16*(-coord[0]+self.a)^3*(-coord[0]+self.b)+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2)*(-coord[1]+self.c)^3*(-coord[1]+self.d)

    def partialGxy4809(self,coord):

        return (2*(-coord[0]+self.a)^4+16*(-coord[0]+self.a)^3*(-coord[0]+self.b)+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2)*(-coord[1]+self.c)^4*(-coord[1]+self.d)

    def partialGxy4810(self,coord):

        return (2*(-coord[0]+self.a)^4+16*(-coord[0]+self.a)^3*(-coord[0]+self.b)+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2)*(-coord[1]+self.d)^2

    def partialGxy4811(self,coord):

        return (2*(-coord[0]+self.a)^4+16*(-coord[0]+self.a)^3*(-coord[0]+self.b)+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2)*(-coord[1]+self.c)*(-coord[1]+self.d)^2

    def partialGxy4812(self,coord):

        return (2*(-coord[0]+self.a)^4+16*(-coord[0]+self.a)^3*(-coord[0]+self.b)+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2)*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2

    def partialGxy4813(self,coord):

        return (2*(-coord[0]+self.a)^4+16*(-coord[0]+self.a)^3*(-coord[0]+self.b)+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2)*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2

    def partialGxy4814(self,coord):

        return (2*(-coord[0]+self.a)^4+16*(-coord[0]+self.a)^3*(-coord[0]+self.b)+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2)*(-coord[1]+self.c)^4*(-coord[1]+self.d)^2

    def partialGxy4815(self,coord):

        return (2*(-coord[0]+self.a)^4+16*(-coord[0]+self.a)^3*(-coord[0]+self.b)+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2)*(-coord[1]+self.d)^3

    def partialGxy4816(self,coord):

        return (2*(-coord[0]+self.a)^4+16*(-coord[0]+self.a)^3*(-coord[0]+self.b)+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2)*(-coord[1]+self.c)*(-coord[1]+self.d)^3

    def partialGxy4817(self,coord):

        return (2*(-coord[0]+self.a)^4+16*(-coord[0]+self.a)^3*(-coord[0]+self.b)+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2)*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3

    def partialGxy4818(self,coord):

        return (2*(-coord[0]+self.a)^4+16*(-coord[0]+self.a)^3*(-coord[0]+self.b)+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2)*(-coord[1]+self.c)^3*(-coord[1]+self.d)^3

    def partialGxy4819(self,coord):

        return (2*(-coord[0]+self.a)^4+16*(-coord[0]+self.a)^3*(-coord[0]+self.b)+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2)*(-coord[1]+self.c)^4*(-coord[1]+self.d)^3

    def partialGxy4820(self,coord):

        return (2*(-coord[0]+self.a)^4+16*(-coord[0]+self.a)^3*(-coord[0]+self.b)+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2)*(-coord[1]+self.d)^4

    def partialGxy4821(self,coord):

        return (2*(-coord[0]+self.a)^4+16*(-coord[0]+self.a)^3*(-coord[0]+self.b)+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2)*(-coord[1]+self.c)*(-coord[1]+self.d)^4

    def partialGxy4822(self,coord):

        return (2*(-coord[0]+self.a)^4+16*(-coord[0]+self.a)^3*(-coord[0]+self.b)+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2)*(-coord[1]+self.c)^2*(-coord[1]+self.d)^4

    def partialGxy4823(self,coord):

        return (2*(-coord[0]+self.a)^4+16*(-coord[0]+self.a)^3*(-coord[0]+self.b)+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2)*(-coord[1]+self.c)^3*(-coord[1]+self.d)^4

    def partialGxy4824(self,coord):

        return (2*(-coord[0]+self.a)^4+16*(-coord[0]+self.a)^3*(-coord[0]+self.b)+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2)*(-coord[1]+self.c)^4*(-coord[1]+self.d)^4

    def partialGxy4831(self,coord):

        return (2*(-coord[0]+self.a)^4+16*(-coord[0]+self.a)^3*(-coord[0]+self.b)+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2)*(-coord[1]+self.c)+(2*(-coord[0]+self.a)^4+16*(-coord[0]+self.a)^3*(-coord[0]+self.b)+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2)*(-coord[1]+self.d)

    def partialGxy4832(self,coord):

        return (2*(-coord[0]+self.a)^4+16*(-coord[0]+self.a)^3*(-coord[0]+self.b)+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2)*(-coord[1]+self.c)^2+2*(2*(-coord[0]+self.a)^4+16*(-coord[0]+self.a)^3*(-coord[0]+self.b)+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2)*(-coord[1]+self.c)*(-coord[1]+self.d)

    def partialGxy4833(self,coord):

        return (2*(-coord[0]+self.a)^4+16*(-coord[0]+self.a)^3*(-coord[0]+self.b)+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2)*(-coord[1]+self.c)^3+3*(2*(-coord[0]+self.a)^4+16*(-coord[0]+self.a)^3*(-coord[0]+self.b)+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2)*(-coord[1]+self.c)^2*(-coord[1]+self.d)

    def partialGxy4834(self,coord):

        return (2*(-coord[0]+self.a)^4+16*(-coord[0]+self.a)^3*(-coord[0]+self.b)+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2)*(-coord[1]+self.c)^4+4*(2*(-coord[0]+self.a)^4+16*(-coord[0]+self.a)^3*(-coord[0]+self.b)+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2)*(-coord[1]+self.c)^3*(-coord[1]+self.d)

    def partialGxy4836(self,coord):

        return 2*(2*(-coord[0]+self.a)^4+16*(-coord[0]+self.a)^3*(-coord[0]+self.b)+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2)*(-coord[1]+self.c)*(-coord[1]+self.d)+(2*(-coord[0]+self.a)^4+16*(-coord[0]+self.a)^3*(-coord[0]+self.b)+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2)*(-coord[1]+self.d)^2

    def partialGxy4837(self,coord):

        return 2*(2*(-coord[0]+self.a)^4+16*(-coord[0]+self.a)^3*(-coord[0]+self.b)+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2)*(-coord[1]+self.c)^2*(-coord[1]+self.d)+2*(2*(-coord[0]+self.a)^4+16*(-coord[0]+self.a)^3*(-coord[0]+self.b)+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2)*(-coord[1]+self.c)*(-coord[1]+self.d)^2

    def partialGxy4838(self,coord):

        return 2*(2*(-coord[0]+self.a)^4+16*(-coord[0]+self.a)^3*(-coord[0]+self.b)+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2)*(-coord[1]+self.c)^3*(-coord[1]+self.d)+3*(2*(-coord[0]+self.a)^4+16*(-coord[0]+self.a)^3*(-coord[0]+self.b)+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2)*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2

    def partialGxy4839(self,coord):

        return 2*(2*(-coord[0]+self.a)^4+16*(-coord[0]+self.a)^3*(-coord[0]+self.b)+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2)*(-coord[1]+self.c)^4*(-coord[1]+self.d)+4*(2*(-coord[0]+self.a)^4+16*(-coord[0]+self.a)^3*(-coord[0]+self.b)+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2)*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2

    def partialGxy4841(self,coord):

        return 3*(2*(-coord[0]+self.a)^4+16*(-coord[0]+self.a)^3*(-coord[0]+self.b)+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2)*(-coord[1]+self.c)*(-coord[1]+self.d)^2+(2*(-coord[0]+self.a)^4+16*(-coord[0]+self.a)^3*(-coord[0]+self.b)+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2)*(-coord[1]+self.d)^3

    def partialGxy4842(self,coord):

        return 3*(2*(-coord[0]+self.a)^4+16*(-coord[0]+self.a)^3*(-coord[0]+self.b)+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2)*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2+2*(2*(-coord[0]+self.a)^4+16*(-coord[0]+self.a)^3*(-coord[0]+self.b)+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2)*(-coord[1]+self.c)*(-coord[1]+self.d)^3

    def partialGxy4843(self,coord):

        return 3*(2*(-coord[0]+self.a)^4+16*(-coord[0]+self.a)^3*(-coord[0]+self.b)+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2)*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2+3*(2*(-coord[0]+self.a)^4+16*(-coord[0]+self.a)^3*(-coord[0]+self.b)+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2)*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3

    def partialGxy4844(self,coord):

        return 3*(2*(-coord[0]+self.a)^4+16*(-coord[0]+self.a)^3*(-coord[0]+self.b)+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2)*(-coord[1]+self.c)^4*(-coord[1]+self.d)^2+4*(2*(-coord[0]+self.a)^4+16*(-coord[0]+self.a)^3*(-coord[0]+self.b)+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2)*(-coord[1]+self.c)^3*(-coord[1]+self.d)^3

    def partialGxy4846(self,coord):

        return 4*(2*(-coord[0]+self.a)^4+16*(-coord[0]+self.a)^3*(-coord[0]+self.b)+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2)*(-coord[1]+self.c)*(-coord[1]+self.d)^3+(2*(-coord[0]+self.a)^4+16*(-coord[0]+self.a)^3*(-coord[0]+self.b)+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2)*(-coord[1]+self.d)^4

    def partialGxy4847(self,coord):

        return 4*(2*(-coord[0]+self.a)^4+16*(-coord[0]+self.a)^3*(-coord[0]+self.b)+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2)*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3+2*(2*(-coord[0]+self.a)^4+16*(-coord[0]+self.a)^3*(-coord[0]+self.b)+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2)*(-coord[1]+self.c)*(-coord[1]+self.d)^4

    def partialGxy4848(self,coord):

        return 4*(2*(-coord[0]+self.a)^4+16*(-coord[0]+self.a)^3*(-coord[0]+self.b)+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2)*(-coord[1]+self.c)^3*(-coord[1]+self.d)^3+3*(2*(-coord[0]+self.a)^4+16*(-coord[0]+self.a)^3*(-coord[0]+self.b)+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2)*(-coord[1]+self.c)^2*(-coord[1]+self.d)^4

    def partialGxy4849(self,coord):

        return 4*(2*(-coord[0]+self.a)^4+16*(-coord[0]+self.a)^3*(-coord[0]+self.b)+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2)*(-coord[1]+self.c)^4*(-coord[1]+self.d)^3+4*(2*(-coord[0]+self.a)^4+16*(-coord[0]+self.a)^3*(-coord[0]+self.b)+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2)*(-coord[1]+self.c)^3*(-coord[1]+self.d)^4

    def partialGxy4862(self,coord):

        return 2*(2*(-coord[0]+self.a)^4+16*(-coord[0]+self.a)^3*(-coord[0]+self.b)+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2)*(-coord[1]+self.c)^2+8*(2*(-coord[0]+self.a)^4+16*(-coord[0]+self.a)^3*(-coord[0]+self.b)+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2)*(-coord[1]+self.c)*(-coord[1]+self.d)+2*(2*(-coord[0]+self.a)^4+16*(-coord[0]+self.a)^3*(-coord[0]+self.b)+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2)*(-coord[1]+self.d)^2

    def partialGxy4863(self,coord):

        return 2*(2*(-coord[0]+self.a)^4+16*(-coord[0]+self.a)^3*(-coord[0]+self.b)+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2)*(-coord[1]+self.c)^3+12*(2*(-coord[0]+self.a)^4+16*(-coord[0]+self.a)^3*(-coord[0]+self.b)+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2)*(-coord[1]+self.c)^2*(-coord[1]+self.d)+6*(2*(-coord[0]+self.a)^4+16*(-coord[0]+self.a)^3*(-coord[0]+self.b)+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2)*(-coord[1]+self.c)*(-coord[1]+self.d)^2

    def partialGxy4864(self,coord):

        return 2*(2*(-coord[0]+self.a)^4+16*(-coord[0]+self.a)^3*(-coord[0]+self.b)+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2)*(-coord[1]+self.c)^4+16*(2*(-coord[0]+self.a)^4+16*(-coord[0]+self.a)^3*(-coord[0]+self.b)+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2)*(-coord[1]+self.c)^3*(-coord[1]+self.d)+12*(2*(-coord[0]+self.a)^4+16*(-coord[0]+self.a)^3*(-coord[0]+self.b)+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2)*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2

    def partialGxy4867(self,coord):

        return 6*(2*(-coord[0]+self.a)^4+16*(-coord[0]+self.a)^3*(-coord[0]+self.b)+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2)*(-coord[1]+self.c)^2*(-coord[1]+self.d)+12*(2*(-coord[0]+self.a)^4+16*(-coord[0]+self.a)^3*(-coord[0]+self.b)+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2)*(-coord[1]+self.c)*(-coord[1]+self.d)^2+2*(2*(-coord[0]+self.a)^4+16*(-coord[0]+self.a)^3*(-coord[0]+self.b)+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2)*(-coord[1]+self.d)^3

    def partialGxy4868(self,coord):

        return 6*(2*(-coord[0]+self.a)^4+16*(-coord[0]+self.a)^3*(-coord[0]+self.b)+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2)*(-coord[1]+self.c)^3*(-coord[1]+self.d)+18*(2*(-coord[0]+self.a)^4+16*(-coord[0]+self.a)^3*(-coord[0]+self.b)+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2)*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2+6*(2*(-coord[0]+self.a)^4+16*(-coord[0]+self.a)^3*(-coord[0]+self.b)+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2)*(-coord[1]+self.c)*(-coord[1]+self.d)^3

    def partialGxy4869(self,coord):

        return 6*(2*(-coord[0]+self.a)^4+16*(-coord[0]+self.a)^3*(-coord[0]+self.b)+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2)*(-coord[1]+self.c)^4*(-coord[1]+self.d)+24*(2*(-coord[0]+self.a)^4+16*(-coord[0]+self.a)^3*(-coord[0]+self.b)+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2)*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2+12*(2*(-coord[0]+self.a)^4+16*(-coord[0]+self.a)^3*(-coord[0]+self.b)+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2)*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3

    def partialGxy4872(self,coord):

        return 12*(2*(-coord[0]+self.a)^4+16*(-coord[0]+self.a)^3*(-coord[0]+self.b)+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2)*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2+16*(2*(-coord[0]+self.a)^4+16*(-coord[0]+self.a)^3*(-coord[0]+self.b)+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2)*(-coord[1]+self.c)*(-coord[1]+self.d)^3+2*(2*(-coord[0]+self.a)^4+16*(-coord[0]+self.a)^3*(-coord[0]+self.b)+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2)*(-coord[1]+self.d)^4

    def partialGxy4873(self,coord):

        return 12*(2*(-coord[0]+self.a)^4+16*(-coord[0]+self.a)^3*(-coord[0]+self.b)+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2)*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2+24*(2*(-coord[0]+self.a)^4+16*(-coord[0]+self.a)^3*(-coord[0]+self.b)+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2)*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3+6*(2*(-coord[0]+self.a)^4+16*(-coord[0]+self.a)^3*(-coord[0]+self.b)+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2)*(-coord[1]+self.c)*(-coord[1]+self.d)^4

    def partialGxy4874(self,coord):

        return 12*(2*(-coord[0]+self.a)^4+16*(-coord[0]+self.a)^3*(-coord[0]+self.b)+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2)*(-coord[1]+self.c)^4*(-coord[1]+self.d)^2+32*(2*(-coord[0]+self.a)^4+16*(-coord[0]+self.a)^3*(-coord[0]+self.b)+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2)*(-coord[1]+self.c)^3*(-coord[1]+self.d)^3+12*(2*(-coord[0]+self.a)^4+16*(-coord[0]+self.a)^3*(-coord[0]+self.b)+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2)*(-coord[1]+self.c)^2*(-coord[1]+self.d)^4

    def partialGxy5025(self,coord):

        return 6*(-coord[0]+self.a)^2*(-coord[0]+self.b)+12*(-coord[0]+self.a)*(-coord[0]+self.b)^2+2*(-coord[0]+self.b)^3

    def partialGxy5026(self,coord):

        return (6*(-coord[0]+self.a)^2*(-coord[0]+self.b)+12*(-coord[0]+self.a)*(-coord[0]+self.b)^2+2*(-coord[0]+self.b)^3)*(-coord[1]+self.c)

    def partialGxy5027(self,coord):

        return (6*(-coord[0]+self.a)^2*(-coord[0]+self.b)+12*(-coord[0]+self.a)*(-coord[0]+self.b)^2+2*(-coord[0]+self.b)^3)*(-coord[1]+self.c)^2

    def partialGxy5028(self,coord):

        return (6*(-coord[0]+self.a)^2*(-coord[0]+self.b)+12*(-coord[0]+self.a)*(-coord[0]+self.b)^2+2*(-coord[0]+self.b)^3)*(-coord[1]+self.c)^3

    def partialGxy5029(self,coord):

        return (6*(-coord[0]+self.a)^2*(-coord[0]+self.b)+12*(-coord[0]+self.a)*(-coord[0]+self.b)^2+2*(-coord[0]+self.b)^3)*(-coord[1]+self.c)^4

    def partialGxy5030(self,coord):

        return (6*(-coord[0]+self.a)^2*(-coord[0]+self.b)+12*(-coord[0]+self.a)*(-coord[0]+self.b)^2+2*(-coord[0]+self.b)^3)*(-coord[1]+self.d)

    def partialGxy5031(self,coord):

        return (6*(-coord[0]+self.a)^2*(-coord[0]+self.b)+12*(-coord[0]+self.a)*(-coord[0]+self.b)^2+2*(-coord[0]+self.b)^3)*(-coord[1]+self.c)*(-coord[1]+self.d)

    def partialGxy5032(self,coord):

        return (6*(-coord[0]+self.a)^2*(-coord[0]+self.b)+12*(-coord[0]+self.a)*(-coord[0]+self.b)^2+2*(-coord[0]+self.b)^3)*(-coord[1]+self.c)^2*(-coord[1]+self.d)

    def partialGxy5033(self,coord):

        return (6*(-coord[0]+self.a)^2*(-coord[0]+self.b)+12*(-coord[0]+self.a)*(-coord[0]+self.b)^2+2*(-coord[0]+self.b)^3)*(-coord[1]+self.c)^3*(-coord[1]+self.d)

    def partialGxy5034(self,coord):

        return (6*(-coord[0]+self.a)^2*(-coord[0]+self.b)+12*(-coord[0]+self.a)*(-coord[0]+self.b)^2+2*(-coord[0]+self.b)^3)*(-coord[1]+self.c)^4*(-coord[1]+self.d)

    def partialGxy5035(self,coord):

        return (6*(-coord[0]+self.a)^2*(-coord[0]+self.b)+12*(-coord[0]+self.a)*(-coord[0]+self.b)^2+2*(-coord[0]+self.b)^3)*(-coord[1]+self.d)^2

    def partialGxy5036(self,coord):

        return (6*(-coord[0]+self.a)^2*(-coord[0]+self.b)+12*(-coord[0]+self.a)*(-coord[0]+self.b)^2+2*(-coord[0]+self.b)^3)*(-coord[1]+self.c)*(-coord[1]+self.d)^2

    def partialGxy5037(self,coord):

        return (6*(-coord[0]+self.a)^2*(-coord[0]+self.b)+12*(-coord[0]+self.a)*(-coord[0]+self.b)^2+2*(-coord[0]+self.b)^3)*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2

    def partialGxy5038(self,coord):

        return (6*(-coord[0]+self.a)^2*(-coord[0]+self.b)+12*(-coord[0]+self.a)*(-coord[0]+self.b)^2+2*(-coord[0]+self.b)^3)*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2

    def partialGxy5039(self,coord):

        return (6*(-coord[0]+self.a)^2*(-coord[0]+self.b)+12*(-coord[0]+self.a)*(-coord[0]+self.b)^2+2*(-coord[0]+self.b)^3)*(-coord[1]+self.c)^4*(-coord[1]+self.d)^2

    def partialGxy5040(self,coord):

        return (6*(-coord[0]+self.a)^2*(-coord[0]+self.b)+12*(-coord[0]+self.a)*(-coord[0]+self.b)^2+2*(-coord[0]+self.b)^3)*(-coord[1]+self.d)^3

    def partialGxy5041(self,coord):

        return (6*(-coord[0]+self.a)^2*(-coord[0]+self.b)+12*(-coord[0]+self.a)*(-coord[0]+self.b)^2+2*(-coord[0]+self.b)^3)*(-coord[1]+self.c)*(-coord[1]+self.d)^3

    def partialGxy5042(self,coord):

        return (6*(-coord[0]+self.a)^2*(-coord[0]+self.b)+12*(-coord[0]+self.a)*(-coord[0]+self.b)^2+2*(-coord[0]+self.b)^3)*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3

    def partialGxy5043(self,coord):

        return (6*(-coord[0]+self.a)^2*(-coord[0]+self.b)+12*(-coord[0]+self.a)*(-coord[0]+self.b)^2+2*(-coord[0]+self.b)^3)*(-coord[1]+self.c)^3*(-coord[1]+self.d)^3

    def partialGxy5044(self,coord):

        return (6*(-coord[0]+self.a)^2*(-coord[0]+self.b)+12*(-coord[0]+self.a)*(-coord[0]+self.b)^2+2*(-coord[0]+self.b)^3)*(-coord[1]+self.c)^4*(-coord[1]+self.d)^3

    def partialGxy5045(self,coord):

        return (6*(-coord[0]+self.a)^2*(-coord[0]+self.b)+12*(-coord[0]+self.a)*(-coord[0]+self.b)^2+2*(-coord[0]+self.b)^3)*(-coord[1]+self.d)^4

    def partialGxy5046(self,coord):

        return (6*(-coord[0]+self.a)^2*(-coord[0]+self.b)+12*(-coord[0]+self.a)*(-coord[0]+self.b)^2+2*(-coord[0]+self.b)^3)*(-coord[1]+self.c)*(-coord[1]+self.d)^4

    def partialGxy5047(self,coord):

        return (6*(-coord[0]+self.a)^2*(-coord[0]+self.b)+12*(-coord[0]+self.a)*(-coord[0]+self.b)^2+2*(-coord[0]+self.b)^3)*(-coord[1]+self.c)^2*(-coord[1]+self.d)^4

    def partialGxy5048(self,coord):

        return (6*(-coord[0]+self.a)^2*(-coord[0]+self.b)+12*(-coord[0]+self.a)*(-coord[0]+self.b)^2+2*(-coord[0]+self.b)^3)*(-coord[1]+self.c)^3*(-coord[1]+self.d)^4

    def partialGxy5049(self,coord):

        return (6*(-coord[0]+self.a)^2*(-coord[0]+self.b)+12*(-coord[0]+self.a)*(-coord[0]+self.b)^2+2*(-coord[0]+self.b)^3)*(-coord[1]+self.c)^4*(-coord[1]+self.d)^4

    def partialGxy5056(self,coord):

        return (6*(-coord[0]+self.a)^2*(-coord[0]+self.b)+12*(-coord[0]+self.a)*(-coord[0]+self.b)^2+2*(-coord[0]+self.b)^3)*(-coord[1]+self.c)+(6*(-coord[0]+self.a)^2*(-coord[0]+self.b)+12*(-coord[0]+self.a)*(-coord[0]+self.b)^2+2*(-coord[0]+self.b)^3)*(-coord[1]+self.d)

    def partialGxy5057(self,coord):

        return (6*(-coord[0]+self.a)^2*(-coord[0]+self.b)+12*(-coord[0]+self.a)*(-coord[0]+self.b)^2+2*(-coord[0]+self.b)^3)*(-coord[1]+self.c)^2+2*(6*(-coord[0]+self.a)^2*(-coord[0]+self.b)+12*(-coord[0]+self.a)*(-coord[0]+self.b)^2+2*(-coord[0]+self.b)^3)*(-coord[1]+self.c)*(-coord[1]+self.d)

    def partialGxy5058(self,coord):

        return (6*(-coord[0]+self.a)^2*(-coord[0]+self.b)+12*(-coord[0]+self.a)*(-coord[0]+self.b)^2+2*(-coord[0]+self.b)^3)*(-coord[1]+self.c)^3+3*(6*(-coord[0]+self.a)^2*(-coord[0]+self.b)+12*(-coord[0]+self.a)*(-coord[0]+self.b)^2+2*(-coord[0]+self.b)^3)*(-coord[1]+self.c)^2*(-coord[1]+self.d)

    def partialGxy5059(self,coord):

        return (6*(-coord[0]+self.a)^2*(-coord[0]+self.b)+12*(-coord[0]+self.a)*(-coord[0]+self.b)^2+2*(-coord[0]+self.b)^3)*(-coord[1]+self.c)^4+4*(6*(-coord[0]+self.a)^2*(-coord[0]+self.b)+12*(-coord[0]+self.a)*(-coord[0]+self.b)^2+2*(-coord[0]+self.b)^3)*(-coord[1]+self.c)^3*(-coord[1]+self.d)

    def partialGxy5061(self,coord):

        return 2*(6*(-coord[0]+self.a)^2*(-coord[0]+self.b)+12*(-coord[0]+self.a)*(-coord[0]+self.b)^2+2*(-coord[0]+self.b)^3)*(-coord[1]+self.c)*(-coord[1]+self.d)+(6*(-coord[0]+self.a)^2*(-coord[0]+self.b)+12*(-coord[0]+self.a)*(-coord[0]+self.b)^2+2*(-coord[0]+self.b)^3)*(-coord[1]+self.d)^2

    def partialGxy5062(self,coord):

        return 2*(6*(-coord[0]+self.a)^2*(-coord[0]+self.b)+12*(-coord[0]+self.a)*(-coord[0]+self.b)^2+2*(-coord[0]+self.b)^3)*(-coord[1]+self.c)^2*(-coord[1]+self.d)+2*(6*(-coord[0]+self.a)^2*(-coord[0]+self.b)+12*(-coord[0]+self.a)*(-coord[0]+self.b)^2+2*(-coord[0]+self.b)^3)*(-coord[1]+self.c)*(-coord[1]+self.d)^2

    def partialGxy5063(self,coord):

        return 2*(6*(-coord[0]+self.a)^2*(-coord[0]+self.b)+12*(-coord[0]+self.a)*(-coord[0]+self.b)^2+2*(-coord[0]+self.b)^3)*(-coord[1]+self.c)^3*(-coord[1]+self.d)+3*(6*(-coord[0]+self.a)^2*(-coord[0]+self.b)+12*(-coord[0]+self.a)*(-coord[0]+self.b)^2+2*(-coord[0]+self.b)^3)*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2

    def partialGxy5064(self,coord):

        return 2*(6*(-coord[0]+self.a)^2*(-coord[0]+self.b)+12*(-coord[0]+self.a)*(-coord[0]+self.b)^2+2*(-coord[0]+self.b)^3)*(-coord[1]+self.c)^4*(-coord[1]+self.d)+4*(6*(-coord[0]+self.a)^2*(-coord[0]+self.b)+12*(-coord[0]+self.a)*(-coord[0]+self.b)^2+2*(-coord[0]+self.b)^3)*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2

    def partialGxy5066(self,coord):

        return 3*(6*(-coord[0]+self.a)^2*(-coord[0]+self.b)+12*(-coord[0]+self.a)*(-coord[0]+self.b)^2+2*(-coord[0]+self.b)^3)*(-coord[1]+self.c)*(-coord[1]+self.d)^2+(6*(-coord[0]+self.a)^2*(-coord[0]+self.b)+12*(-coord[0]+self.a)*(-coord[0]+self.b)^2+2*(-coord[0]+self.b)^3)*(-coord[1]+self.d)^3

    def partialGxy5067(self,coord):

        return 3*(6*(-coord[0]+self.a)^2*(-coord[0]+self.b)+12*(-coord[0]+self.a)*(-coord[0]+self.b)^2+2*(-coord[0]+self.b)^3)*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2+2*(6*(-coord[0]+self.a)^2*(-coord[0]+self.b)+12*(-coord[0]+self.a)*(-coord[0]+self.b)^2+2*(-coord[0]+self.b)^3)*(-coord[1]+self.c)*(-coord[1]+self.d)^3

    def partialGxy5068(self,coord):

        return 3*(6*(-coord[0]+self.a)^2*(-coord[0]+self.b)+12*(-coord[0]+self.a)*(-coord[0]+self.b)^2+2*(-coord[0]+self.b)^3)*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2+3*(6*(-coord[0]+self.a)^2*(-coord[0]+self.b)+12*(-coord[0]+self.a)*(-coord[0]+self.b)^2+2*(-coord[0]+self.b)^3)*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3

    def partialGxy5069(self,coord):

        return 3*(6*(-coord[0]+self.a)^2*(-coord[0]+self.b)+12*(-coord[0]+self.a)*(-coord[0]+self.b)^2+2*(-coord[0]+self.b)^3)*(-coord[1]+self.c)^4*(-coord[1]+self.d)^2+4*(6*(-coord[0]+self.a)^2*(-coord[0]+self.b)+12*(-coord[0]+self.a)*(-coord[0]+self.b)^2+2*(-coord[0]+self.b)^3)*(-coord[1]+self.c)^3*(-coord[1]+self.d)^3

    def partialGxy5071(self,coord):

        return 4*(6*(-coord[0]+self.a)^2*(-coord[0]+self.b)+12*(-coord[0]+self.a)*(-coord[0]+self.b)^2+2*(-coord[0]+self.b)^3)*(-coord[1]+self.c)*(-coord[1]+self.d)^3+(6*(-coord[0]+self.a)^2*(-coord[0]+self.b)+12*(-coord[0]+self.a)*(-coord[0]+self.b)^2+2*(-coord[0]+self.b)^3)*(-coord[1]+self.d)^4

    def partialGxy5072(self,coord):

        return 4*(6*(-coord[0]+self.a)^2*(-coord[0]+self.b)+12*(-coord[0]+self.a)*(-coord[0]+self.b)^2+2*(-coord[0]+self.b)^3)*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3+2*(6*(-coord[0]+self.a)^2*(-coord[0]+self.b)+12*(-coord[0]+self.a)*(-coord[0]+self.b)^2+2*(-coord[0]+self.b)^3)*(-coord[1]+self.c)*(-coord[1]+self.d)^4

    def partialGxy5073(self,coord):

        return 4*(6*(-coord[0]+self.a)^2*(-coord[0]+self.b)+12*(-coord[0]+self.a)*(-coord[0]+self.b)^2+2*(-coord[0]+self.b)^3)*(-coord[1]+self.c)^3*(-coord[1]+self.d)^3+3*(6*(-coord[0]+self.a)^2*(-coord[0]+self.b)+12*(-coord[0]+self.a)*(-coord[0]+self.b)^2+2*(-coord[0]+self.b)^3)*(-coord[1]+self.c)^2*(-coord[1]+self.d)^4

    def partialGxy5074(self,coord):

        return 4*(6*(-coord[0]+self.a)^2*(-coord[0]+self.b)+12*(-coord[0]+self.a)*(-coord[0]+self.b)^2+2*(-coord[0]+self.b)^3)*(-coord[1]+self.c)^4*(-coord[1]+self.d)^3+4*(6*(-coord[0]+self.a)^2*(-coord[0]+self.b)+12*(-coord[0]+self.a)*(-coord[0]+self.b)^2+2*(-coord[0]+self.b)^3)*(-coord[1]+self.c)^3*(-coord[1]+self.d)^4

    def partialGxy5087(self,coord):

        return 2*(6*(-coord[0]+self.a)^2*(-coord[0]+self.b)+12*(-coord[0]+self.a)*(-coord[0]+self.b)^2+2*(-coord[0]+self.b)^3)*(-coord[1]+self.c)^2+8*(6*(-coord[0]+self.a)^2*(-coord[0]+self.b)+12*(-coord[0]+self.a)*(-coord[0]+self.b)^2+2*(-coord[0]+self.b)^3)*(-coord[1]+self.c)*(-coord[1]+self.d)+2*(6*(-coord[0]+self.a)^2*(-coord[0]+self.b)+12*(-coord[0]+self.a)*(-coord[0]+self.b)^2+2*(-coord[0]+self.b)^3)*(-coord[1]+self.d)^2

    def partialGxy5088(self,coord):

        return 2*(6*(-coord[0]+self.a)^2*(-coord[0]+self.b)+12*(-coord[0]+self.a)*(-coord[0]+self.b)^2+2*(-coord[0]+self.b)^3)*(-coord[1]+self.c)^3+12*(6*(-coord[0]+self.a)^2*(-coord[0]+self.b)+12*(-coord[0]+self.a)*(-coord[0]+self.b)^2+2*(-coord[0]+self.b)^3)*(-coord[1]+self.c)^2*(-coord[1]+self.d)+6*(6*(-coord[0]+self.a)^2*(-coord[0]+self.b)+12*(-coord[0]+self.a)*(-coord[0]+self.b)^2+2*(-coord[0]+self.b)^3)*(-coord[1]+self.c)*(-coord[1]+self.d)^2

    def partialGxy5089(self,coord):

        return 2*(6*(-coord[0]+self.a)^2*(-coord[0]+self.b)+12*(-coord[0]+self.a)*(-coord[0]+self.b)^2+2*(-coord[0]+self.b)^3)*(-coord[1]+self.c)^4+16*(6*(-coord[0]+self.a)^2*(-coord[0]+self.b)+12*(-coord[0]+self.a)*(-coord[0]+self.b)^2+2*(-coord[0]+self.b)^3)*(-coord[1]+self.c)^3*(-coord[1]+self.d)+12*(6*(-coord[0]+self.a)^2*(-coord[0]+self.b)+12*(-coord[0]+self.a)*(-coord[0]+self.b)^2+2*(-coord[0]+self.b)^3)*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2

    def partialGxy5092(self,coord):

        return 6*(6*(-coord[0]+self.a)^2*(-coord[0]+self.b)+12*(-coord[0]+self.a)*(-coord[0]+self.b)^2+2*(-coord[0]+self.b)^3)*(-coord[1]+self.c)^2*(-coord[1]+self.d)+12*(6*(-coord[0]+self.a)^2*(-coord[0]+self.b)+12*(-coord[0]+self.a)*(-coord[0]+self.b)^2+2*(-coord[0]+self.b)^3)*(-coord[1]+self.c)*(-coord[1]+self.d)^2+2*(6*(-coord[0]+self.a)^2*(-coord[0]+self.b)+12*(-coord[0]+self.a)*(-coord[0]+self.b)^2+2*(-coord[0]+self.b)^3)*(-coord[1]+self.d)^3

    def partialGxy5093(self,coord):

        return 6*(6*(-coord[0]+self.a)^2*(-coord[0]+self.b)+12*(-coord[0]+self.a)*(-coord[0]+self.b)^2+2*(-coord[0]+self.b)^3)*(-coord[1]+self.c)^3*(-coord[1]+self.d)+18*(6*(-coord[0]+self.a)^2*(-coord[0]+self.b)+12*(-coord[0]+self.a)*(-coord[0]+self.b)^2+2*(-coord[0]+self.b)^3)*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2+6*(6*(-coord[0]+self.a)^2*(-coord[0]+self.b)+12*(-coord[0]+self.a)*(-coord[0]+self.b)^2+2*(-coord[0]+self.b)^3)*(-coord[1]+self.c)*(-coord[1]+self.d)^3

    def partialGxy5094(self,coord):

        return 6*(6*(-coord[0]+self.a)^2*(-coord[0]+self.b)+12*(-coord[0]+self.a)*(-coord[0]+self.b)^2+2*(-coord[0]+self.b)^3)*(-coord[1]+self.c)^4*(-coord[1]+self.d)+24*(6*(-coord[0]+self.a)^2*(-coord[0]+self.b)+12*(-coord[0]+self.a)*(-coord[0]+self.b)^2+2*(-coord[0]+self.b)^3)*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2+12*(6*(-coord[0]+self.a)^2*(-coord[0]+self.b)+12*(-coord[0]+self.a)*(-coord[0]+self.b)^2+2*(-coord[0]+self.b)^3)*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3

    def partialGxy5097(self,coord):

        return 12*(6*(-coord[0]+self.a)^2*(-coord[0]+self.b)+12*(-coord[0]+self.a)*(-coord[0]+self.b)^2+2*(-coord[0]+self.b)^3)*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2+16*(6*(-coord[0]+self.a)^2*(-coord[0]+self.b)+12*(-coord[0]+self.a)*(-coord[0]+self.b)^2+2*(-coord[0]+self.b)^3)*(-coord[1]+self.c)*(-coord[1]+self.d)^3+2*(6*(-coord[0]+self.a)^2*(-coord[0]+self.b)+12*(-coord[0]+self.a)*(-coord[0]+self.b)^2+2*(-coord[0]+self.b)^3)*(-coord[1]+self.d)^4

    def partialGxy5098(self,coord):

        return 12*(6*(-coord[0]+self.a)^2*(-coord[0]+self.b)+12*(-coord[0]+self.a)*(-coord[0]+self.b)^2+2*(-coord[0]+self.b)^3)*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2+24*(6*(-coord[0]+self.a)^2*(-coord[0]+self.b)+12*(-coord[0]+self.a)*(-coord[0]+self.b)^2+2*(-coord[0]+self.b)^3)*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3+6*(6*(-coord[0]+self.a)^2*(-coord[0]+self.b)+12*(-coord[0]+self.a)*(-coord[0]+self.b)^2+2*(-coord[0]+self.b)^3)*(-coord[1]+self.c)*(-coord[1]+self.d)^4

    def partialGxy5099(self,coord):

        return 12*(6*(-coord[0]+self.a)^2*(-coord[0]+self.b)+12*(-coord[0]+self.a)*(-coord[0]+self.b)^2+2*(-coord[0]+self.b)^3)*(-coord[1]+self.c)^4*(-coord[1]+self.d)^2+32*(6*(-coord[0]+self.a)^2*(-coord[0]+self.b)+12*(-coord[0]+self.a)*(-coord[0]+self.b)^2+2*(-coord[0]+self.b)^3)*(-coord[1]+self.c)^3*(-coord[1]+self.d)^3+12*(6*(-coord[0]+self.a)^2*(-coord[0]+self.b)+12*(-coord[0]+self.a)*(-coord[0]+self.b)^2+2*(-coord[0]+self.b)^3)*(-coord[1]+self.c)^2*(-coord[1]+self.d)^4

    def partialGxy5100(self,coord):

        return 6*(-coord[0]+self.a)^3*(-coord[0]+self.b)+18*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2+6*(-coord[0]+self.a)*(-coord[0]+self.b)^3

    def partialGxy5101(self,coord):

        return (6*(-coord[0]+self.a)^3*(-coord[0]+self.b)+18*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2+6*(-coord[0]+self.a)*(-coord[0]+self.b)^3)*(-coord[1]+self.c)

    def partialGxy5102(self,coord):

        return (6*(-coord[0]+self.a)^3*(-coord[0]+self.b)+18*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2+6*(-coord[0]+self.a)*(-coord[0]+self.b)^3)*(-coord[1]+self.c)^2

    def partialGxy5103(self,coord):

        return (6*(-coord[0]+self.a)^3*(-coord[0]+self.b)+18*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2+6*(-coord[0]+self.a)*(-coord[0]+self.b)^3)*(-coord[1]+self.c)^3

    def partialGxy5104(self,coord):

        return (6*(-coord[0]+self.a)^3*(-coord[0]+self.b)+18*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2+6*(-coord[0]+self.a)*(-coord[0]+self.b)^3)*(-coord[1]+self.c)^4

    def partialGxy5105(self,coord):

        return (6*(-coord[0]+self.a)^3*(-coord[0]+self.b)+18*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2+6*(-coord[0]+self.a)*(-coord[0]+self.b)^3)*(-coord[1]+self.d)

    def partialGxy5106(self,coord):

        return (6*(-coord[0]+self.a)^3*(-coord[0]+self.b)+18*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2+6*(-coord[0]+self.a)*(-coord[0]+self.b)^3)*(-coord[1]+self.c)*(-coord[1]+self.d)

    def partialGxy5107(self,coord):

        return (6*(-coord[0]+self.a)^3*(-coord[0]+self.b)+18*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2+6*(-coord[0]+self.a)*(-coord[0]+self.b)^3)*(-coord[1]+self.c)^2*(-coord[1]+self.d)

    def partialGxy5108(self,coord):

        return (6*(-coord[0]+self.a)^3*(-coord[0]+self.b)+18*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2+6*(-coord[0]+self.a)*(-coord[0]+self.b)^3)*(-coord[1]+self.c)^3*(-coord[1]+self.d)

    def partialGxy5109(self,coord):

        return (6*(-coord[0]+self.a)^3*(-coord[0]+self.b)+18*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2+6*(-coord[0]+self.a)*(-coord[0]+self.b)^3)*(-coord[1]+self.c)^4*(-coord[1]+self.d)

    def partialGxy5110(self,coord):

        return (6*(-coord[0]+self.a)^3*(-coord[0]+self.b)+18*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2+6*(-coord[0]+self.a)*(-coord[0]+self.b)^3)*(-coord[1]+self.d)^2

    def partialGxy5111(self,coord):

        return (6*(-coord[0]+self.a)^3*(-coord[0]+self.b)+18*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2+6*(-coord[0]+self.a)*(-coord[0]+self.b)^3)*(-coord[1]+self.c)*(-coord[1]+self.d)^2

    def partialGxy5112(self,coord):

        return (6*(-coord[0]+self.a)^3*(-coord[0]+self.b)+18*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2+6*(-coord[0]+self.a)*(-coord[0]+self.b)^3)*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2

    def partialGxy5113(self,coord):

        return (6*(-coord[0]+self.a)^3*(-coord[0]+self.b)+18*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2+6*(-coord[0]+self.a)*(-coord[0]+self.b)^3)*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2

    def partialGxy5114(self,coord):

        return (6*(-coord[0]+self.a)^3*(-coord[0]+self.b)+18*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2+6*(-coord[0]+self.a)*(-coord[0]+self.b)^3)*(-coord[1]+self.c)^4*(-coord[1]+self.d)^2

    def partialGxy5115(self,coord):

        return (6*(-coord[0]+self.a)^3*(-coord[0]+self.b)+18*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2+6*(-coord[0]+self.a)*(-coord[0]+self.b)^3)*(-coord[1]+self.d)^3

    def partialGxy5116(self,coord):

        return (6*(-coord[0]+self.a)^3*(-coord[0]+self.b)+18*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2+6*(-coord[0]+self.a)*(-coord[0]+self.b)^3)*(-coord[1]+self.c)*(-coord[1]+self.d)^3

    def partialGxy5117(self,coord):

        return (6*(-coord[0]+self.a)^3*(-coord[0]+self.b)+18*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2+6*(-coord[0]+self.a)*(-coord[0]+self.b)^3)*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3

    def partialGxy5118(self,coord):

        return (6*(-coord[0]+self.a)^3*(-coord[0]+self.b)+18*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2+6*(-coord[0]+self.a)*(-coord[0]+self.b)^3)*(-coord[1]+self.c)^3*(-coord[1]+self.d)^3

    def partialGxy5119(self,coord):

        return (6*(-coord[0]+self.a)^3*(-coord[0]+self.b)+18*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2+6*(-coord[0]+self.a)*(-coord[0]+self.b)^3)*(-coord[1]+self.c)^4*(-coord[1]+self.d)^3

    def partialGxy5120(self,coord):

        return (6*(-coord[0]+self.a)^3*(-coord[0]+self.b)+18*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2+6*(-coord[0]+self.a)*(-coord[0]+self.b)^3)*(-coord[1]+self.d)^4

    def partialGxy5121(self,coord):

        return (6*(-coord[0]+self.a)^3*(-coord[0]+self.b)+18*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2+6*(-coord[0]+self.a)*(-coord[0]+self.b)^3)*(-coord[1]+self.c)*(-coord[1]+self.d)^4

    def partialGxy5122(self,coord):

        return (6*(-coord[0]+self.a)^3*(-coord[0]+self.b)+18*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2+6*(-coord[0]+self.a)*(-coord[0]+self.b)^3)*(-coord[1]+self.c)^2*(-coord[1]+self.d)^4

    def partialGxy5123(self,coord):

        return (6*(-coord[0]+self.a)^3*(-coord[0]+self.b)+18*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2+6*(-coord[0]+self.a)*(-coord[0]+self.b)^3)*(-coord[1]+self.c)^3*(-coord[1]+self.d)^4

    def partialGxy5124(self,coord):

        return (6*(-coord[0]+self.a)^3*(-coord[0]+self.b)+18*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2+6*(-coord[0]+self.a)*(-coord[0]+self.b)^3)*(-coord[1]+self.c)^4*(-coord[1]+self.d)^4

    def partialGxy5131(self,coord):

        return (6*(-coord[0]+self.a)^3*(-coord[0]+self.b)+18*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2+6*(-coord[0]+self.a)*(-coord[0]+self.b)^3)*(-coord[1]+self.c)+(6*(-coord[0]+self.a)^3*(-coord[0]+self.b)+18*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2+6*(-coord[0]+self.a)*(-coord[0]+self.b)^3)*(-coord[1]+self.d)

    def partialGxy5132(self,coord):

        return (6*(-coord[0]+self.a)^3*(-coord[0]+self.b)+18*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2+6*(-coord[0]+self.a)*(-coord[0]+self.b)^3)*(-coord[1]+self.c)^2+2*(6*(-coord[0]+self.a)^3*(-coord[0]+self.b)+18*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2+6*(-coord[0]+self.a)*(-coord[0]+self.b)^3)*(-coord[1]+self.c)*(-coord[1]+self.d)

    def partialGxy5133(self,coord):

        return (6*(-coord[0]+self.a)^3*(-coord[0]+self.b)+18*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2+6*(-coord[0]+self.a)*(-coord[0]+self.b)^3)*(-coord[1]+self.c)^3+3*(6*(-coord[0]+self.a)^3*(-coord[0]+self.b)+18*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2+6*(-coord[0]+self.a)*(-coord[0]+self.b)^3)*(-coord[1]+self.c)^2*(-coord[1]+self.d)

    def partialGxy5134(self,coord):

        return (6*(-coord[0]+self.a)^3*(-coord[0]+self.b)+18*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2+6*(-coord[0]+self.a)*(-coord[0]+self.b)^3)*(-coord[1]+self.c)^4+4*(6*(-coord[0]+self.a)^3*(-coord[0]+self.b)+18*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2+6*(-coord[0]+self.a)*(-coord[0]+self.b)^3)*(-coord[1]+self.c)^3*(-coord[1]+self.d)

    def partialGxy5136(self,coord):

        return 2*(6*(-coord[0]+self.a)^3*(-coord[0]+self.b)+18*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2+6*(-coord[0]+self.a)*(-coord[0]+self.b)^3)*(-coord[1]+self.c)*(-coord[1]+self.d)+(6*(-coord[0]+self.a)^3*(-coord[0]+self.b)+18*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2+6*(-coord[0]+self.a)*(-coord[0]+self.b)^3)*(-coord[1]+self.d)^2

    def partialGxy5137(self,coord):

        return 2*(6*(-coord[0]+self.a)^3*(-coord[0]+self.b)+18*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2+6*(-coord[0]+self.a)*(-coord[0]+self.b)^3)*(-coord[1]+self.c)^2*(-coord[1]+self.d)+2*(6*(-coord[0]+self.a)^3*(-coord[0]+self.b)+18*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2+6*(-coord[0]+self.a)*(-coord[0]+self.b)^3)*(-coord[1]+self.c)*(-coord[1]+self.d)^2

    def partialGxy5138(self,coord):

        return 2*(6*(-coord[0]+self.a)^3*(-coord[0]+self.b)+18*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2+6*(-coord[0]+self.a)*(-coord[0]+self.b)^3)*(-coord[1]+self.c)^3*(-coord[1]+self.d)+3*(6*(-coord[0]+self.a)^3*(-coord[0]+self.b)+18*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2+6*(-coord[0]+self.a)*(-coord[0]+self.b)^3)*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2

    def partialGxy5139(self,coord):

        return 2*(6*(-coord[0]+self.a)^3*(-coord[0]+self.b)+18*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2+6*(-coord[0]+self.a)*(-coord[0]+self.b)^3)*(-coord[1]+self.c)^4*(-coord[1]+self.d)+4*(6*(-coord[0]+self.a)^3*(-coord[0]+self.b)+18*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2+6*(-coord[0]+self.a)*(-coord[0]+self.b)^3)*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2

    def partialGxy5141(self,coord):

        return 3*(6*(-coord[0]+self.a)^3*(-coord[0]+self.b)+18*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2+6*(-coord[0]+self.a)*(-coord[0]+self.b)^3)*(-coord[1]+self.c)*(-coord[1]+self.d)^2+(6*(-coord[0]+self.a)^3*(-coord[0]+self.b)+18*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2+6*(-coord[0]+self.a)*(-coord[0]+self.b)^3)*(-coord[1]+self.d)^3

    def partialGxy5142(self,coord):

        return 3*(6*(-coord[0]+self.a)^3*(-coord[0]+self.b)+18*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2+6*(-coord[0]+self.a)*(-coord[0]+self.b)^3)*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2+2*(6*(-coord[0]+self.a)^3*(-coord[0]+self.b)+18*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2+6*(-coord[0]+self.a)*(-coord[0]+self.b)^3)*(-coord[1]+self.c)*(-coord[1]+self.d)^3

    def partialGxy5143(self,coord):

        return 3*(6*(-coord[0]+self.a)^3*(-coord[0]+self.b)+18*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2+6*(-coord[0]+self.a)*(-coord[0]+self.b)^3)*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2+3*(6*(-coord[0]+self.a)^3*(-coord[0]+self.b)+18*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2+6*(-coord[0]+self.a)*(-coord[0]+self.b)^3)*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3

    def partialGxy5144(self,coord):

        return 3*(6*(-coord[0]+self.a)^3*(-coord[0]+self.b)+18*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2+6*(-coord[0]+self.a)*(-coord[0]+self.b)^3)*(-coord[1]+self.c)^4*(-coord[1]+self.d)^2+4*(6*(-coord[0]+self.a)^3*(-coord[0]+self.b)+18*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2+6*(-coord[0]+self.a)*(-coord[0]+self.b)^3)*(-coord[1]+self.c)^3*(-coord[1]+self.d)^3

    def partialGxy5146(self,coord):

        return 4*(6*(-coord[0]+self.a)^3*(-coord[0]+self.b)+18*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2+6*(-coord[0]+self.a)*(-coord[0]+self.b)^3)*(-coord[1]+self.c)*(-coord[1]+self.d)^3+(6*(-coord[0]+self.a)^3*(-coord[0]+self.b)+18*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2+6*(-coord[0]+self.a)*(-coord[0]+self.b)^3)*(-coord[1]+self.d)^4

    def partialGxy5147(self,coord):

        return 4*(6*(-coord[0]+self.a)^3*(-coord[0]+self.b)+18*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2+6*(-coord[0]+self.a)*(-coord[0]+self.b)^3)*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3+2*(6*(-coord[0]+self.a)^3*(-coord[0]+self.b)+18*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2+6*(-coord[0]+self.a)*(-coord[0]+self.b)^3)*(-coord[1]+self.c)*(-coord[1]+self.d)^4

    def partialGxy5148(self,coord):

        return 4*(6*(-coord[0]+self.a)^3*(-coord[0]+self.b)+18*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2+6*(-coord[0]+self.a)*(-coord[0]+self.b)^3)*(-coord[1]+self.c)^3*(-coord[1]+self.d)^3+3*(6*(-coord[0]+self.a)^3*(-coord[0]+self.b)+18*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2+6*(-coord[0]+self.a)*(-coord[0]+self.b)^3)*(-coord[1]+self.c)^2*(-coord[1]+self.d)^4

    def partialGxy5149(self,coord):

        return 4*(6*(-coord[0]+self.a)^3*(-coord[0]+self.b)+18*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2+6*(-coord[0]+self.a)*(-coord[0]+self.b)^3)*(-coord[1]+self.c)^4*(-coord[1]+self.d)^3+4*(6*(-coord[0]+self.a)^3*(-coord[0]+self.b)+18*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2+6*(-coord[0]+self.a)*(-coord[0]+self.b)^3)*(-coord[1]+self.c)^3*(-coord[1]+self.d)^4

    def partialGxy5162(self,coord):

        return 2*(6*(-coord[0]+self.a)^3*(-coord[0]+self.b)+18*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2+6*(-coord[0]+self.a)*(-coord[0]+self.b)^3)*(-coord[1]+self.c)^2+8*(6*(-coord[0]+self.a)^3*(-coord[0]+self.b)+18*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2+6*(-coord[0]+self.a)*(-coord[0]+self.b)^3)*(-coord[1]+self.c)*(-coord[1]+self.d)+2*(6*(-coord[0]+self.a)^3*(-coord[0]+self.b)+18*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2+6*(-coord[0]+self.a)*(-coord[0]+self.b)^3)*(-coord[1]+self.d)^2

    def partialGxy5163(self,coord):

        return 2*(6*(-coord[0]+self.a)^3*(-coord[0]+self.b)+18*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2+6*(-coord[0]+self.a)*(-coord[0]+self.b)^3)*(-coord[1]+self.c)^3+12*(6*(-coord[0]+self.a)^3*(-coord[0]+self.b)+18*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2+6*(-coord[0]+self.a)*(-coord[0]+self.b)^3)*(-coord[1]+self.c)^2*(-coord[1]+self.d)+6*(6*(-coord[0]+self.a)^3*(-coord[0]+self.b)+18*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2+6*(-coord[0]+self.a)*(-coord[0]+self.b)^3)*(-coord[1]+self.c)*(-coord[1]+self.d)^2

    def partialGxy5164(self,coord):

        return 2*(6*(-coord[0]+self.a)^3*(-coord[0]+self.b)+18*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2+6*(-coord[0]+self.a)*(-coord[0]+self.b)^3)*(-coord[1]+self.c)^4+16*(6*(-coord[0]+self.a)^3*(-coord[0]+self.b)+18*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2+6*(-coord[0]+self.a)*(-coord[0]+self.b)^3)*(-coord[1]+self.c)^3*(-coord[1]+self.d)+12*(6*(-coord[0]+self.a)^3*(-coord[0]+self.b)+18*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2+6*(-coord[0]+self.a)*(-coord[0]+self.b)^3)*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2

    def partialGxy5167(self,coord):

        return 6*(6*(-coord[0]+self.a)^3*(-coord[0]+self.b)+18*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2+6*(-coord[0]+self.a)*(-coord[0]+self.b)^3)*(-coord[1]+self.c)^2*(-coord[1]+self.d)+12*(6*(-coord[0]+self.a)^3*(-coord[0]+self.b)+18*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2+6*(-coord[0]+self.a)*(-coord[0]+self.b)^3)*(-coord[1]+self.c)*(-coord[1]+self.d)^2+2*(6*(-coord[0]+self.a)^3*(-coord[0]+self.b)+18*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2+6*(-coord[0]+self.a)*(-coord[0]+self.b)^3)*(-coord[1]+self.d)^3

    def partialGxy5168(self,coord):

        return 6*(6*(-coord[0]+self.a)^3*(-coord[0]+self.b)+18*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2+6*(-coord[0]+self.a)*(-coord[0]+self.b)^3)*(-coord[1]+self.c)^3*(-coord[1]+self.d)+18*(6*(-coord[0]+self.a)^3*(-coord[0]+self.b)+18*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2+6*(-coord[0]+self.a)*(-coord[0]+self.b)^3)*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2+6*(6*(-coord[0]+self.a)^3*(-coord[0]+self.b)+18*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2+6*(-coord[0]+self.a)*(-coord[0]+self.b)^3)*(-coord[1]+self.c)*(-coord[1]+self.d)^3

    def partialGxy5169(self,coord):

        return 6*(6*(-coord[0]+self.a)^3*(-coord[0]+self.b)+18*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2+6*(-coord[0]+self.a)*(-coord[0]+self.b)^3)*(-coord[1]+self.c)^4*(-coord[1]+self.d)+24*(6*(-coord[0]+self.a)^3*(-coord[0]+self.b)+18*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2+6*(-coord[0]+self.a)*(-coord[0]+self.b)^3)*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2+12*(6*(-coord[0]+self.a)^3*(-coord[0]+self.b)+18*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2+6*(-coord[0]+self.a)*(-coord[0]+self.b)^3)*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3

    def partialGxy5172(self,coord):

        return 12*(6*(-coord[0]+self.a)^3*(-coord[0]+self.b)+18*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2+6*(-coord[0]+self.a)*(-coord[0]+self.b)^3)*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2+16*(6*(-coord[0]+self.a)^3*(-coord[0]+self.b)+18*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2+6*(-coord[0]+self.a)*(-coord[0]+self.b)^3)*(-coord[1]+self.c)*(-coord[1]+self.d)^3+2*(6*(-coord[0]+self.a)^3*(-coord[0]+self.b)+18*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2+6*(-coord[0]+self.a)*(-coord[0]+self.b)^3)*(-coord[1]+self.d)^4

    def partialGxy5173(self,coord):

        return 12*(6*(-coord[0]+self.a)^3*(-coord[0]+self.b)+18*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2+6*(-coord[0]+self.a)*(-coord[0]+self.b)^3)*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2+24*(6*(-coord[0]+self.a)^3*(-coord[0]+self.b)+18*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2+6*(-coord[0]+self.a)*(-coord[0]+self.b)^3)*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3+6*(6*(-coord[0]+self.a)^3*(-coord[0]+self.b)+18*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2+6*(-coord[0]+self.a)*(-coord[0]+self.b)^3)*(-coord[1]+self.c)*(-coord[1]+self.d)^4

    def partialGxy5174(self,coord):

        return 12*(6*(-coord[0]+self.a)^3*(-coord[0]+self.b)+18*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2+6*(-coord[0]+self.a)*(-coord[0]+self.b)^3)*(-coord[1]+self.c)^4*(-coord[1]+self.d)^2+32*(6*(-coord[0]+self.a)^3*(-coord[0]+self.b)+18*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2+6*(-coord[0]+self.a)*(-coord[0]+self.b)^3)*(-coord[1]+self.c)^3*(-coord[1]+self.d)^3+12*(6*(-coord[0]+self.a)^3*(-coord[0]+self.b)+18*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2+6*(-coord[0]+self.a)*(-coord[0]+self.b)^3)*(-coord[1]+self.c)^2*(-coord[1]+self.d)^4

    def partialGxy5175(self,coord):

        return 6*(-coord[0]+self.a)^4*(-coord[0]+self.b)+24*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3

    def partialGxy5176(self,coord):

        return (6*(-coord[0]+self.a)^4*(-coord[0]+self.b)+24*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3)*(-coord[1]+self.c)

    def partialGxy5177(self,coord):

        return (6*(-coord[0]+self.a)^4*(-coord[0]+self.b)+24*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3)*(-coord[1]+self.c)^2

    def partialGxy5178(self,coord):

        return (6*(-coord[0]+self.a)^4*(-coord[0]+self.b)+24*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3)*(-coord[1]+self.c)^3

    def partialGxy5179(self,coord):

        return (6*(-coord[0]+self.a)^4*(-coord[0]+self.b)+24*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3)*(-coord[1]+self.c)^4

    def partialGxy5180(self,coord):

        return (6*(-coord[0]+self.a)^4*(-coord[0]+self.b)+24*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3)*(-coord[1]+self.d)

    def partialGxy5181(self,coord):

        return (6*(-coord[0]+self.a)^4*(-coord[0]+self.b)+24*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3)*(-coord[1]+self.c)*(-coord[1]+self.d)

    def partialGxy5182(self,coord):

        return (6*(-coord[0]+self.a)^4*(-coord[0]+self.b)+24*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3)*(-coord[1]+self.c)^2*(-coord[1]+self.d)

    def partialGxy5183(self,coord):

        return (6*(-coord[0]+self.a)^4*(-coord[0]+self.b)+24*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3)*(-coord[1]+self.c)^3*(-coord[1]+self.d)

    def partialGxy5184(self,coord):

        return (6*(-coord[0]+self.a)^4*(-coord[0]+self.b)+24*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3)*(-coord[1]+self.c)^4*(-coord[1]+self.d)

    def partialGxy5185(self,coord):

        return (6*(-coord[0]+self.a)^4*(-coord[0]+self.b)+24*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3)*(-coord[1]+self.d)^2

    def partialGxy5186(self,coord):

        return (6*(-coord[0]+self.a)^4*(-coord[0]+self.b)+24*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3)*(-coord[1]+self.c)*(-coord[1]+self.d)^2

    def partialGxy5187(self,coord):

        return (6*(-coord[0]+self.a)^4*(-coord[0]+self.b)+24*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3)*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2

    def partialGxy5188(self,coord):

        return (6*(-coord[0]+self.a)^4*(-coord[0]+self.b)+24*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3)*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2

    def partialGxy5189(self,coord):

        return (6*(-coord[0]+self.a)^4*(-coord[0]+self.b)+24*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3)*(-coord[1]+self.c)^4*(-coord[1]+self.d)^2

    def partialGxy5190(self,coord):

        return (6*(-coord[0]+self.a)^4*(-coord[0]+self.b)+24*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3)*(-coord[1]+self.d)^3

    def partialGxy5191(self,coord):

        return (6*(-coord[0]+self.a)^4*(-coord[0]+self.b)+24*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3)*(-coord[1]+self.c)*(-coord[1]+self.d)^3

    def partialGxy5192(self,coord):

        return (6*(-coord[0]+self.a)^4*(-coord[0]+self.b)+24*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3)*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3

    def partialGxy5193(self,coord):

        return (6*(-coord[0]+self.a)^4*(-coord[0]+self.b)+24*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3)*(-coord[1]+self.c)^3*(-coord[1]+self.d)^3

    def partialGxy5194(self,coord):

        return (6*(-coord[0]+self.a)^4*(-coord[0]+self.b)+24*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3)*(-coord[1]+self.c)^4*(-coord[1]+self.d)^3

    def partialGxy5195(self,coord):

        return (6*(-coord[0]+self.a)^4*(-coord[0]+self.b)+24*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3)*(-coord[1]+self.d)^4

    def partialGxy5196(self,coord):

        return (6*(-coord[0]+self.a)^4*(-coord[0]+self.b)+24*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3)*(-coord[1]+self.c)*(-coord[1]+self.d)^4

    def partialGxy5197(self,coord):

        return (6*(-coord[0]+self.a)^4*(-coord[0]+self.b)+24*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3)*(-coord[1]+self.c)^2*(-coord[1]+self.d)^4

    def partialGxy5198(self,coord):

        return (6*(-coord[0]+self.a)^4*(-coord[0]+self.b)+24*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3)*(-coord[1]+self.c)^3*(-coord[1]+self.d)^4

    def partialGxy5199(self,coord):

        return (6*(-coord[0]+self.a)^4*(-coord[0]+self.b)+24*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3)*(-coord[1]+self.c)^4*(-coord[1]+self.d)^4

    def partialGxy5206(self,coord):

        return (6*(-coord[0]+self.a)^4*(-coord[0]+self.b)+24*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3)*(-coord[1]+self.c)+(6*(-coord[0]+self.a)^4*(-coord[0]+self.b)+24*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3)*(-coord[1]+self.d)

    def partialGxy5207(self,coord):

        return (6*(-coord[0]+self.a)^4*(-coord[0]+self.b)+24*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3)*(-coord[1]+self.c)^2+2*(6*(-coord[0]+self.a)^4*(-coord[0]+self.b)+24*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3)*(-coord[1]+self.c)*(-coord[1]+self.d)

    def partialGxy5208(self,coord):

        return (6*(-coord[0]+self.a)^4*(-coord[0]+self.b)+24*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3)*(-coord[1]+self.c)^3+3*(6*(-coord[0]+self.a)^4*(-coord[0]+self.b)+24*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3)*(-coord[1]+self.c)^2*(-coord[1]+self.d)

    def partialGxy5209(self,coord):

        return (6*(-coord[0]+self.a)^4*(-coord[0]+self.b)+24*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3)*(-coord[1]+self.c)^4+4*(6*(-coord[0]+self.a)^4*(-coord[0]+self.b)+24*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3)*(-coord[1]+self.c)^3*(-coord[1]+self.d)

    def partialGxy5211(self,coord):

        return 2*(6*(-coord[0]+self.a)^4*(-coord[0]+self.b)+24*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3)*(-coord[1]+self.c)*(-coord[1]+self.d)+(6*(-coord[0]+self.a)^4*(-coord[0]+self.b)+24*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3)*(-coord[1]+self.d)^2

    def partialGxy5212(self,coord):

        return 2*(6*(-coord[0]+self.a)^4*(-coord[0]+self.b)+24*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3)*(-coord[1]+self.c)^2*(-coord[1]+self.d)+2*(6*(-coord[0]+self.a)^4*(-coord[0]+self.b)+24*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3)*(-coord[1]+self.c)*(-coord[1]+self.d)^2

    def partialGxy5213(self,coord):

        return 2*(6*(-coord[0]+self.a)^4*(-coord[0]+self.b)+24*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3)*(-coord[1]+self.c)^3*(-coord[1]+self.d)+3*(6*(-coord[0]+self.a)^4*(-coord[0]+self.b)+24*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3)*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2

    def partialGxy5214(self,coord):

        return 2*(6*(-coord[0]+self.a)^4*(-coord[0]+self.b)+24*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3)*(-coord[1]+self.c)^4*(-coord[1]+self.d)+4*(6*(-coord[0]+self.a)^4*(-coord[0]+self.b)+24*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3)*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2

    def partialGxy5216(self,coord):

        return 3*(6*(-coord[0]+self.a)^4*(-coord[0]+self.b)+24*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3)*(-coord[1]+self.c)*(-coord[1]+self.d)^2+(6*(-coord[0]+self.a)^4*(-coord[0]+self.b)+24*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3)*(-coord[1]+self.d)^3

    def partialGxy5217(self,coord):

        return 3*(6*(-coord[0]+self.a)^4*(-coord[0]+self.b)+24*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3)*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2+2*(6*(-coord[0]+self.a)^4*(-coord[0]+self.b)+24*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3)*(-coord[1]+self.c)*(-coord[1]+self.d)^3

    def partialGxy5218(self,coord):

        return 3*(6*(-coord[0]+self.a)^4*(-coord[0]+self.b)+24*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3)*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2+3*(6*(-coord[0]+self.a)^4*(-coord[0]+self.b)+24*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3)*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3

    def partialGxy5219(self,coord):

        return 3*(6*(-coord[0]+self.a)^4*(-coord[0]+self.b)+24*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3)*(-coord[1]+self.c)^4*(-coord[1]+self.d)^2+4*(6*(-coord[0]+self.a)^4*(-coord[0]+self.b)+24*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3)*(-coord[1]+self.c)^3*(-coord[1]+self.d)^3

    def partialGxy5221(self,coord):

        return 4*(6*(-coord[0]+self.a)^4*(-coord[0]+self.b)+24*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3)*(-coord[1]+self.c)*(-coord[1]+self.d)^3+(6*(-coord[0]+self.a)^4*(-coord[0]+self.b)+24*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3)*(-coord[1]+self.d)^4

    def partialGxy5222(self,coord):

        return 4*(6*(-coord[0]+self.a)^4*(-coord[0]+self.b)+24*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3)*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3+2*(6*(-coord[0]+self.a)^4*(-coord[0]+self.b)+24*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3)*(-coord[1]+self.c)*(-coord[1]+self.d)^4

    def partialGxy5223(self,coord):

        return 4*(6*(-coord[0]+self.a)^4*(-coord[0]+self.b)+24*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3)*(-coord[1]+self.c)^3*(-coord[1]+self.d)^3+3*(6*(-coord[0]+self.a)^4*(-coord[0]+self.b)+24*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3)*(-coord[1]+self.c)^2*(-coord[1]+self.d)^4

    def partialGxy5224(self,coord):

        return 4*(6*(-coord[0]+self.a)^4*(-coord[0]+self.b)+24*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3)*(-coord[1]+self.c)^4*(-coord[1]+self.d)^3+4*(6*(-coord[0]+self.a)^4*(-coord[0]+self.b)+24*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3)*(-coord[1]+self.c)^3*(-coord[1]+self.d)^4

    def partialGxy5237(self,coord):

        return 2*(6*(-coord[0]+self.a)^4*(-coord[0]+self.b)+24*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3)*(-coord[1]+self.c)^2+8*(6*(-coord[0]+self.a)^4*(-coord[0]+self.b)+24*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3)*(-coord[1]+self.c)*(-coord[1]+self.d)+2*(6*(-coord[0]+self.a)^4*(-coord[0]+self.b)+24*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3)*(-coord[1]+self.d)^2

    def partialGxy5238(self,coord):

        return 2*(6*(-coord[0]+self.a)^4*(-coord[0]+self.b)+24*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3)*(-coord[1]+self.c)^3+12*(6*(-coord[0]+self.a)^4*(-coord[0]+self.b)+24*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3)*(-coord[1]+self.c)^2*(-coord[1]+self.d)+6*(6*(-coord[0]+self.a)^4*(-coord[0]+self.b)+24*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3)*(-coord[1]+self.c)*(-coord[1]+self.d)^2

    def partialGxy5239(self,coord):

        return 2*(6*(-coord[0]+self.a)^4*(-coord[0]+self.b)+24*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3)*(-coord[1]+self.c)^4+16*(6*(-coord[0]+self.a)^4*(-coord[0]+self.b)+24*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3)*(-coord[1]+self.c)^3*(-coord[1]+self.d)+12*(6*(-coord[0]+self.a)^4*(-coord[0]+self.b)+24*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3)*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2

    def partialGxy5242(self,coord):

        return 6*(6*(-coord[0]+self.a)^4*(-coord[0]+self.b)+24*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3)*(-coord[1]+self.c)^2*(-coord[1]+self.d)+12*(6*(-coord[0]+self.a)^4*(-coord[0]+self.b)+24*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3)*(-coord[1]+self.c)*(-coord[1]+self.d)^2+2*(6*(-coord[0]+self.a)^4*(-coord[0]+self.b)+24*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3)*(-coord[1]+self.d)^3

    def partialGxy5243(self,coord):

        return 6*(6*(-coord[0]+self.a)^4*(-coord[0]+self.b)+24*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3)*(-coord[1]+self.c)^3*(-coord[1]+self.d)+18*(6*(-coord[0]+self.a)^4*(-coord[0]+self.b)+24*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3)*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2+6*(6*(-coord[0]+self.a)^4*(-coord[0]+self.b)+24*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3)*(-coord[1]+self.c)*(-coord[1]+self.d)^3

    def partialGxy5244(self,coord):

        return 6*(6*(-coord[0]+self.a)^4*(-coord[0]+self.b)+24*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3)*(-coord[1]+self.c)^4*(-coord[1]+self.d)+24*(6*(-coord[0]+self.a)^4*(-coord[0]+self.b)+24*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3)*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2+12*(6*(-coord[0]+self.a)^4*(-coord[0]+self.b)+24*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3)*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3

    def partialGxy5247(self,coord):

        return 12*(6*(-coord[0]+self.a)^4*(-coord[0]+self.b)+24*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3)*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2+16*(6*(-coord[0]+self.a)^4*(-coord[0]+self.b)+24*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3)*(-coord[1]+self.c)*(-coord[1]+self.d)^3+2*(6*(-coord[0]+self.a)^4*(-coord[0]+self.b)+24*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3)*(-coord[1]+self.d)^4

    def partialGxy5248(self,coord):

        return 12*(6*(-coord[0]+self.a)^4*(-coord[0]+self.b)+24*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3)*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2+24*(6*(-coord[0]+self.a)^4*(-coord[0]+self.b)+24*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3)*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3+6*(6*(-coord[0]+self.a)^4*(-coord[0]+self.b)+24*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3)*(-coord[1]+self.c)*(-coord[1]+self.d)^4

    def partialGxy5249(self,coord):

        return 12*(6*(-coord[0]+self.a)^4*(-coord[0]+self.b)+24*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3)*(-coord[1]+self.c)^4*(-coord[1]+self.d)^2+32*(6*(-coord[0]+self.a)^4*(-coord[0]+self.b)+24*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3)*(-coord[1]+self.c)^3*(-coord[1]+self.d)^3+12*(6*(-coord[0]+self.a)^4*(-coord[0]+self.b)+24*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3)*(-coord[1]+self.c)^2*(-coord[1]+self.d)^4

    def partialGxy5400(self,coord):

        return 12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2+16*(-coord[0]+self.a)*(-coord[0]+self.b)^3+2*(-coord[0]+self.b)^4

    def partialGxy5401(self,coord):

        return (12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2+16*(-coord[0]+self.a)*(-coord[0]+self.b)^3+2*(-coord[0]+self.b)^4)*(-coord[1]+self.c)

    def partialGxy5402(self,coord):

        return (12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2+16*(-coord[0]+self.a)*(-coord[0]+self.b)^3+2*(-coord[0]+self.b)^4)*(-coord[1]+self.c)^2

    def partialGxy5403(self,coord):

        return (12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2+16*(-coord[0]+self.a)*(-coord[0]+self.b)^3+2*(-coord[0]+self.b)^4)*(-coord[1]+self.c)^3

    def partialGxy5404(self,coord):

        return (12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2+16*(-coord[0]+self.a)*(-coord[0]+self.b)^3+2*(-coord[0]+self.b)^4)*(-coord[1]+self.c)^4

    def partialGxy5405(self,coord):

        return (12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2+16*(-coord[0]+self.a)*(-coord[0]+self.b)^3+2*(-coord[0]+self.b)^4)*(-coord[1]+self.d)

    def partialGxy5406(self,coord):

        return (12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2+16*(-coord[0]+self.a)*(-coord[0]+self.b)^3+2*(-coord[0]+self.b)^4)*(-coord[1]+self.c)*(-coord[1]+self.d)

    def partialGxy5407(self,coord):

        return (12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2+16*(-coord[0]+self.a)*(-coord[0]+self.b)^3+2*(-coord[0]+self.b)^4)*(-coord[1]+self.c)^2*(-coord[1]+self.d)

    def partialGxy5408(self,coord):

        return (12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2+16*(-coord[0]+self.a)*(-coord[0]+self.b)^3+2*(-coord[0]+self.b)^4)*(-coord[1]+self.c)^3*(-coord[1]+self.d)

    def partialGxy5409(self,coord):

        return (12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2+16*(-coord[0]+self.a)*(-coord[0]+self.b)^3+2*(-coord[0]+self.b)^4)*(-coord[1]+self.c)^4*(-coord[1]+self.d)

    def partialGxy5410(self,coord):

        return (12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2+16*(-coord[0]+self.a)*(-coord[0]+self.b)^3+2*(-coord[0]+self.b)^4)*(-coord[1]+self.d)^2

    def partialGxy5411(self,coord):

        return (12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2+16*(-coord[0]+self.a)*(-coord[0]+self.b)^3+2*(-coord[0]+self.b)^4)*(-coord[1]+self.c)*(-coord[1]+self.d)^2

    def partialGxy5412(self,coord):

        return (12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2+16*(-coord[0]+self.a)*(-coord[0]+self.b)^3+2*(-coord[0]+self.b)^4)*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2

    def partialGxy5413(self,coord):

        return (12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2+16*(-coord[0]+self.a)*(-coord[0]+self.b)^3+2*(-coord[0]+self.b)^4)*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2

    def partialGxy5414(self,coord):

        return (12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2+16*(-coord[0]+self.a)*(-coord[0]+self.b)^3+2*(-coord[0]+self.b)^4)*(-coord[1]+self.c)^4*(-coord[1]+self.d)^2

    def partialGxy5415(self,coord):

        return (12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2+16*(-coord[0]+self.a)*(-coord[0]+self.b)^3+2*(-coord[0]+self.b)^4)*(-coord[1]+self.d)^3

    def partialGxy5416(self,coord):

        return (12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2+16*(-coord[0]+self.a)*(-coord[0]+self.b)^3+2*(-coord[0]+self.b)^4)*(-coord[1]+self.c)*(-coord[1]+self.d)^3

    def partialGxy5417(self,coord):

        return (12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2+16*(-coord[0]+self.a)*(-coord[0]+self.b)^3+2*(-coord[0]+self.b)^4)*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3

    def partialGxy5418(self,coord):

        return (12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2+16*(-coord[0]+self.a)*(-coord[0]+self.b)^3+2*(-coord[0]+self.b)^4)*(-coord[1]+self.c)^3*(-coord[1]+self.d)^3

    def partialGxy5419(self,coord):

        return (12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2+16*(-coord[0]+self.a)*(-coord[0]+self.b)^3+2*(-coord[0]+self.b)^4)*(-coord[1]+self.c)^4*(-coord[1]+self.d)^3

    def partialGxy5420(self,coord):

        return (12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2+16*(-coord[0]+self.a)*(-coord[0]+self.b)^3+2*(-coord[0]+self.b)^4)*(-coord[1]+self.d)^4

    def partialGxy5421(self,coord):

        return (12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2+16*(-coord[0]+self.a)*(-coord[0]+self.b)^3+2*(-coord[0]+self.b)^4)*(-coord[1]+self.c)*(-coord[1]+self.d)^4

    def partialGxy5422(self,coord):

        return (12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2+16*(-coord[0]+self.a)*(-coord[0]+self.b)^3+2*(-coord[0]+self.b)^4)*(-coord[1]+self.c)^2*(-coord[1]+self.d)^4

    def partialGxy5423(self,coord):

        return (12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2+16*(-coord[0]+self.a)*(-coord[0]+self.b)^3+2*(-coord[0]+self.b)^4)*(-coord[1]+self.c)^3*(-coord[1]+self.d)^4

    def partialGxy5424(self,coord):

        return (12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2+16*(-coord[0]+self.a)*(-coord[0]+self.b)^3+2*(-coord[0]+self.b)^4)*(-coord[1]+self.c)^4*(-coord[1]+self.d)^4

    def partialGxy5431(self,coord):

        return (12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2+16*(-coord[0]+self.a)*(-coord[0]+self.b)^3+2*(-coord[0]+self.b)^4)*(-coord[1]+self.c)+(12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2+16*(-coord[0]+self.a)*(-coord[0]+self.b)^3+2*(-coord[0]+self.b)^4)*(-coord[1]+self.d)

    def partialGxy5432(self,coord):

        return (12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2+16*(-coord[0]+self.a)*(-coord[0]+self.b)^3+2*(-coord[0]+self.b)^4)*(-coord[1]+self.c)^2+2*(12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2+16*(-coord[0]+self.a)*(-coord[0]+self.b)^3+2*(-coord[0]+self.b)^4)*(-coord[1]+self.c)*(-coord[1]+self.d)

    def partialGxy5433(self,coord):

        return (12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2+16*(-coord[0]+self.a)*(-coord[0]+self.b)^3+2*(-coord[0]+self.b)^4)*(-coord[1]+self.c)^3+3*(12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2+16*(-coord[0]+self.a)*(-coord[0]+self.b)^3+2*(-coord[0]+self.b)^4)*(-coord[1]+self.c)^2*(-coord[1]+self.d)

    def partialGxy5434(self,coord):

        return (12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2+16*(-coord[0]+self.a)*(-coord[0]+self.b)^3+2*(-coord[0]+self.b)^4)*(-coord[1]+self.c)^4+4*(12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2+16*(-coord[0]+self.a)*(-coord[0]+self.b)^3+2*(-coord[0]+self.b)^4)*(-coord[1]+self.c)^3*(-coord[1]+self.d)

    def partialGxy5436(self,coord):

        return 2*(12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2+16*(-coord[0]+self.a)*(-coord[0]+self.b)^3+2*(-coord[0]+self.b)^4)*(-coord[1]+self.c)*(-coord[1]+self.d)+(12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2+16*(-coord[0]+self.a)*(-coord[0]+self.b)^3+2*(-coord[0]+self.b)^4)*(-coord[1]+self.d)^2

    def partialGxy5437(self,coord):

        return 2*(12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2+16*(-coord[0]+self.a)*(-coord[0]+self.b)^3+2*(-coord[0]+self.b)^4)*(-coord[1]+self.c)^2*(-coord[1]+self.d)+2*(12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2+16*(-coord[0]+self.a)*(-coord[0]+self.b)^3+2*(-coord[0]+self.b)^4)*(-coord[1]+self.c)*(-coord[1]+self.d)^2

    def partialGxy5438(self,coord):

        return 2*(12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2+16*(-coord[0]+self.a)*(-coord[0]+self.b)^3+2*(-coord[0]+self.b)^4)*(-coord[1]+self.c)^3*(-coord[1]+self.d)+3*(12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2+16*(-coord[0]+self.a)*(-coord[0]+self.b)^3+2*(-coord[0]+self.b)^4)*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2

    def partialGxy5439(self,coord):

        return 2*(12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2+16*(-coord[0]+self.a)*(-coord[0]+self.b)^3+2*(-coord[0]+self.b)^4)*(-coord[1]+self.c)^4*(-coord[1]+self.d)+4*(12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2+16*(-coord[0]+self.a)*(-coord[0]+self.b)^3+2*(-coord[0]+self.b)^4)*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2

    def partialGxy5441(self,coord):

        return 3*(12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2+16*(-coord[0]+self.a)*(-coord[0]+self.b)^3+2*(-coord[0]+self.b)^4)*(-coord[1]+self.c)*(-coord[1]+self.d)^2+(12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2+16*(-coord[0]+self.a)*(-coord[0]+self.b)^3+2*(-coord[0]+self.b)^4)*(-coord[1]+self.d)^3

    def partialGxy5442(self,coord):

        return 3*(12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2+16*(-coord[0]+self.a)*(-coord[0]+self.b)^3+2*(-coord[0]+self.b)^4)*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2+2*(12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2+16*(-coord[0]+self.a)*(-coord[0]+self.b)^3+2*(-coord[0]+self.b)^4)*(-coord[1]+self.c)*(-coord[1]+self.d)^3

    def partialGxy5443(self,coord):

        return 3*(12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2+16*(-coord[0]+self.a)*(-coord[0]+self.b)^3+2*(-coord[0]+self.b)^4)*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2+3*(12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2+16*(-coord[0]+self.a)*(-coord[0]+self.b)^3+2*(-coord[0]+self.b)^4)*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3

    def partialGxy5444(self,coord):

        return 3*(12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2+16*(-coord[0]+self.a)*(-coord[0]+self.b)^3+2*(-coord[0]+self.b)^4)*(-coord[1]+self.c)^4*(-coord[1]+self.d)^2+4*(12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2+16*(-coord[0]+self.a)*(-coord[0]+self.b)^3+2*(-coord[0]+self.b)^4)*(-coord[1]+self.c)^3*(-coord[1]+self.d)^3

    def partialGxy5446(self,coord):

        return 4*(12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2+16*(-coord[0]+self.a)*(-coord[0]+self.b)^3+2*(-coord[0]+self.b)^4)*(-coord[1]+self.c)*(-coord[1]+self.d)^3+(12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2+16*(-coord[0]+self.a)*(-coord[0]+self.b)^3+2*(-coord[0]+self.b)^4)*(-coord[1]+self.d)^4

    def partialGxy5447(self,coord):

        return 4*(12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2+16*(-coord[0]+self.a)*(-coord[0]+self.b)^3+2*(-coord[0]+self.b)^4)*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3+2*(12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2+16*(-coord[0]+self.a)*(-coord[0]+self.b)^3+2*(-coord[0]+self.b)^4)*(-coord[1]+self.c)*(-coord[1]+self.d)^4

    def partialGxy5448(self,coord):

        return 4*(12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2+16*(-coord[0]+self.a)*(-coord[0]+self.b)^3+2*(-coord[0]+self.b)^4)*(-coord[1]+self.c)^3*(-coord[1]+self.d)^3+3*(12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2+16*(-coord[0]+self.a)*(-coord[0]+self.b)^3+2*(-coord[0]+self.b)^4)*(-coord[1]+self.c)^2*(-coord[1]+self.d)^4

    def partialGxy5449(self,coord):

        return 4*(12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2+16*(-coord[0]+self.a)*(-coord[0]+self.b)^3+2*(-coord[0]+self.b)^4)*(-coord[1]+self.c)^4*(-coord[1]+self.d)^3+4*(12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2+16*(-coord[0]+self.a)*(-coord[0]+self.b)^3+2*(-coord[0]+self.b)^4)*(-coord[1]+self.c)^3*(-coord[1]+self.d)^4

    def partialGxy5462(self,coord):

        return 2*(12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2+16*(-coord[0]+self.a)*(-coord[0]+self.b)^3+2*(-coord[0]+self.b)^4)*(-coord[1]+self.c)^2+8*(12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2+16*(-coord[0]+self.a)*(-coord[0]+self.b)^3+2*(-coord[0]+self.b)^4)*(-coord[1]+self.c)*(-coord[1]+self.d)+2*(12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2+16*(-coord[0]+self.a)*(-coord[0]+self.b)^3+2*(-coord[0]+self.b)^4)*(-coord[1]+self.d)^2

    def partialGxy5463(self,coord):

        return 2*(12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2+16*(-coord[0]+self.a)*(-coord[0]+self.b)^3+2*(-coord[0]+self.b)^4)*(-coord[1]+self.c)^3+12*(12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2+16*(-coord[0]+self.a)*(-coord[0]+self.b)^3+2*(-coord[0]+self.b)^4)*(-coord[1]+self.c)^2*(-coord[1]+self.d)+6*(12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2+16*(-coord[0]+self.a)*(-coord[0]+self.b)^3+2*(-coord[0]+self.b)^4)*(-coord[1]+self.c)*(-coord[1]+self.d)^2

    def partialGxy5464(self,coord):

        return 2*(12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2+16*(-coord[0]+self.a)*(-coord[0]+self.b)^3+2*(-coord[0]+self.b)^4)*(-coord[1]+self.c)^4+16*(12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2+16*(-coord[0]+self.a)*(-coord[0]+self.b)^3+2*(-coord[0]+self.b)^4)*(-coord[1]+self.c)^3*(-coord[1]+self.d)+12*(12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2+16*(-coord[0]+self.a)*(-coord[0]+self.b)^3+2*(-coord[0]+self.b)^4)*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2

    def partialGxy5467(self,coord):

        return 6*(12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2+16*(-coord[0]+self.a)*(-coord[0]+self.b)^3+2*(-coord[0]+self.b)^4)*(-coord[1]+self.c)^2*(-coord[1]+self.d)+12*(12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2+16*(-coord[0]+self.a)*(-coord[0]+self.b)^3+2*(-coord[0]+self.b)^4)*(-coord[1]+self.c)*(-coord[1]+self.d)^2+2*(12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2+16*(-coord[0]+self.a)*(-coord[0]+self.b)^3+2*(-coord[0]+self.b)^4)*(-coord[1]+self.d)^3

    def partialGxy5468(self,coord):

        return 6*(12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2+16*(-coord[0]+self.a)*(-coord[0]+self.b)^3+2*(-coord[0]+self.b)^4)*(-coord[1]+self.c)^3*(-coord[1]+self.d)+18*(12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2+16*(-coord[0]+self.a)*(-coord[0]+self.b)^3+2*(-coord[0]+self.b)^4)*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2+6*(12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2+16*(-coord[0]+self.a)*(-coord[0]+self.b)^3+2*(-coord[0]+self.b)^4)*(-coord[1]+self.c)*(-coord[1]+self.d)^3

    def partialGxy5469(self,coord):

        return 6*(12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2+16*(-coord[0]+self.a)*(-coord[0]+self.b)^3+2*(-coord[0]+self.b)^4)*(-coord[1]+self.c)^4*(-coord[1]+self.d)+24*(12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2+16*(-coord[0]+self.a)*(-coord[0]+self.b)^3+2*(-coord[0]+self.b)^4)*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2+12*(12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2+16*(-coord[0]+self.a)*(-coord[0]+self.b)^3+2*(-coord[0]+self.b)^4)*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3

    def partialGxy5472(self,coord):

        return 12*(12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2+16*(-coord[0]+self.a)*(-coord[0]+self.b)^3+2*(-coord[0]+self.b)^4)*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2+16*(12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2+16*(-coord[0]+self.a)*(-coord[0]+self.b)^3+2*(-coord[0]+self.b)^4)*(-coord[1]+self.c)*(-coord[1]+self.d)^3+2*(12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2+16*(-coord[0]+self.a)*(-coord[0]+self.b)^3+2*(-coord[0]+self.b)^4)*(-coord[1]+self.d)^4

    def partialGxy5473(self,coord):

        return 12*(12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2+16*(-coord[0]+self.a)*(-coord[0]+self.b)^3+2*(-coord[0]+self.b)^4)*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2+24*(12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2+16*(-coord[0]+self.a)*(-coord[0]+self.b)^3+2*(-coord[0]+self.b)^4)*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3+6*(12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2+16*(-coord[0]+self.a)*(-coord[0]+self.b)^3+2*(-coord[0]+self.b)^4)*(-coord[1]+self.c)*(-coord[1]+self.d)^4

    def partialGxy5474(self,coord):

        return 12*(12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2+16*(-coord[0]+self.a)*(-coord[0]+self.b)^3+2*(-coord[0]+self.b)^4)*(-coord[1]+self.c)^4*(-coord[1]+self.d)^2+32*(12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2+16*(-coord[0]+self.a)*(-coord[0]+self.b)^3+2*(-coord[0]+self.b)^4)*(-coord[1]+self.c)^3*(-coord[1]+self.d)^3+12*(12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^2+16*(-coord[0]+self.a)*(-coord[0]+self.b)^3+2*(-coord[0]+self.b)^4)*(-coord[1]+self.c)^2*(-coord[1]+self.d)^4

    def partialGxy5475(self,coord):

        return 12*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2+24*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3+6*(-coord[0]+self.a)*(-coord[0]+self.b)^4

    def partialGxy5476(self,coord):

        return (12*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2+24*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3+6*(-coord[0]+self.a)*(-coord[0]+self.b)^4)*(-coord[1]+self.c)

    def partialGxy5477(self,coord):

        return (12*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2+24*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3+6*(-coord[0]+self.a)*(-coord[0]+self.b)^4)*(-coord[1]+self.c)^2

    def partialGxy5478(self,coord):

        return (12*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2+24*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3+6*(-coord[0]+self.a)*(-coord[0]+self.b)^4)*(-coord[1]+self.c)^3

    def partialGxy5479(self,coord):

        return (12*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2+24*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3+6*(-coord[0]+self.a)*(-coord[0]+self.b)^4)*(-coord[1]+self.c)^4

    def partialGxy5480(self,coord):

        return (12*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2+24*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3+6*(-coord[0]+self.a)*(-coord[0]+self.b)^4)*(-coord[1]+self.d)

    def partialGxy5481(self,coord):

        return (12*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2+24*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3+6*(-coord[0]+self.a)*(-coord[0]+self.b)^4)*(-coord[1]+self.c)*(-coord[1]+self.d)

    def partialGxy5482(self,coord):

        return (12*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2+24*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3+6*(-coord[0]+self.a)*(-coord[0]+self.b)^4)*(-coord[1]+self.c)^2*(-coord[1]+self.d)

    def partialGxy5483(self,coord):

        return (12*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2+24*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3+6*(-coord[0]+self.a)*(-coord[0]+self.b)^4)*(-coord[1]+self.c)^3*(-coord[1]+self.d)

    def partialGxy5484(self,coord):

        return (12*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2+24*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3+6*(-coord[0]+self.a)*(-coord[0]+self.b)^4)*(-coord[1]+self.c)^4*(-coord[1]+self.d)

    def partialGxy5485(self,coord):

        return (12*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2+24*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3+6*(-coord[0]+self.a)*(-coord[0]+self.b)^4)*(-coord[1]+self.d)^2

    def partialGxy5486(self,coord):

        return (12*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2+24*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3+6*(-coord[0]+self.a)*(-coord[0]+self.b)^4)*(-coord[1]+self.c)*(-coord[1]+self.d)^2

    def partialGxy5487(self,coord):

        return (12*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2+24*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3+6*(-coord[0]+self.a)*(-coord[0]+self.b)^4)*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2

    def partialGxy5488(self,coord):

        return (12*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2+24*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3+6*(-coord[0]+self.a)*(-coord[0]+self.b)^4)*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2

    def partialGxy5489(self,coord):

        return (12*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2+24*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3+6*(-coord[0]+self.a)*(-coord[0]+self.b)^4)*(-coord[1]+self.c)^4*(-coord[1]+self.d)^2

    def partialGxy5490(self,coord):

        return (12*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2+24*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3+6*(-coord[0]+self.a)*(-coord[0]+self.b)^4)*(-coord[1]+self.d)^3

    def partialGxy5491(self,coord):

        return (12*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2+24*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3+6*(-coord[0]+self.a)*(-coord[0]+self.b)^4)*(-coord[1]+self.c)*(-coord[1]+self.d)^3

    def partialGxy5492(self,coord):

        return (12*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2+24*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3+6*(-coord[0]+self.a)*(-coord[0]+self.b)^4)*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3

    def partialGxy5493(self,coord):

        return (12*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2+24*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3+6*(-coord[0]+self.a)*(-coord[0]+self.b)^4)*(-coord[1]+self.c)^3*(-coord[1]+self.d)^3

    def partialGxy5494(self,coord):

        return (12*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2+24*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3+6*(-coord[0]+self.a)*(-coord[0]+self.b)^4)*(-coord[1]+self.c)^4*(-coord[1]+self.d)^3

    def partialGxy5495(self,coord):

        return (12*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2+24*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3+6*(-coord[0]+self.a)*(-coord[0]+self.b)^4)*(-coord[1]+self.d)^4

    def partialGxy5496(self,coord):

        return (12*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2+24*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3+6*(-coord[0]+self.a)*(-coord[0]+self.b)^4)*(-coord[1]+self.c)*(-coord[1]+self.d)^4

    def partialGxy5497(self,coord):

        return (12*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2+24*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3+6*(-coord[0]+self.a)*(-coord[0]+self.b)^4)*(-coord[1]+self.c)^2*(-coord[1]+self.d)^4

    def partialGxy5498(self,coord):

        return (12*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2+24*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3+6*(-coord[0]+self.a)*(-coord[0]+self.b)^4)*(-coord[1]+self.c)^3*(-coord[1]+self.d)^4

    def partialGxy5499(self,coord):

        return (12*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2+24*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3+6*(-coord[0]+self.a)*(-coord[0]+self.b)^4)*(-coord[1]+self.c)^4*(-coord[1]+self.d)^4

    def partialGxy5506(self,coord):

        return (12*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2+24*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3+6*(-coord[0]+self.a)*(-coord[0]+self.b)^4)*(-coord[1]+self.c)+(12*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2+24*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3+6*(-coord[0]+self.a)*(-coord[0]+self.b)^4)*(-coord[1]+self.d)

    def partialGxy5507(self,coord):

        return (12*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2+24*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3+6*(-coord[0]+self.a)*(-coord[0]+self.b)^4)*(-coord[1]+self.c)^2+2*(12*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2+24*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3+6*(-coord[0]+self.a)*(-coord[0]+self.b)^4)*(-coord[1]+self.c)*(-coord[1]+self.d)

    def partialGxy5508(self,coord):

        return (12*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2+24*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3+6*(-coord[0]+self.a)*(-coord[0]+self.b)^4)*(-coord[1]+self.c)^3+3*(12*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2+24*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3+6*(-coord[0]+self.a)*(-coord[0]+self.b)^4)*(-coord[1]+self.c)^2*(-coord[1]+self.d)

    def partialGxy5509(self,coord):

        return (12*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2+24*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3+6*(-coord[0]+self.a)*(-coord[0]+self.b)^4)*(-coord[1]+self.c)^4+4*(12*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2+24*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3+6*(-coord[0]+self.a)*(-coord[0]+self.b)^4)*(-coord[1]+self.c)^3*(-coord[1]+self.d)

    def partialGxy5511(self,coord):

        return 2*(12*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2+24*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3+6*(-coord[0]+self.a)*(-coord[0]+self.b)^4)*(-coord[1]+self.c)*(-coord[1]+self.d)+(12*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2+24*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3+6*(-coord[0]+self.a)*(-coord[0]+self.b)^4)*(-coord[1]+self.d)^2

    def partialGxy5512(self,coord):

        return 2*(12*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2+24*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3+6*(-coord[0]+self.a)*(-coord[0]+self.b)^4)*(-coord[1]+self.c)^2*(-coord[1]+self.d)+2*(12*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2+24*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3+6*(-coord[0]+self.a)*(-coord[0]+self.b)^4)*(-coord[1]+self.c)*(-coord[1]+self.d)^2

    def partialGxy5513(self,coord):

        return 2*(12*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2+24*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3+6*(-coord[0]+self.a)*(-coord[0]+self.b)^4)*(-coord[1]+self.c)^3*(-coord[1]+self.d)+3*(12*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2+24*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3+6*(-coord[0]+self.a)*(-coord[0]+self.b)^4)*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2

    def partialGxy5514(self,coord):

        return 2*(12*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2+24*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3+6*(-coord[0]+self.a)*(-coord[0]+self.b)^4)*(-coord[1]+self.c)^4*(-coord[1]+self.d)+4*(12*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2+24*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3+6*(-coord[0]+self.a)*(-coord[0]+self.b)^4)*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2

    def partialGxy5516(self,coord):

        return 3*(12*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2+24*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3+6*(-coord[0]+self.a)*(-coord[0]+self.b)^4)*(-coord[1]+self.c)*(-coord[1]+self.d)^2+(12*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2+24*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3+6*(-coord[0]+self.a)*(-coord[0]+self.b)^4)*(-coord[1]+self.d)^3

    def partialGxy5517(self,coord):

        return 3*(12*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2+24*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3+6*(-coord[0]+self.a)*(-coord[0]+self.b)^4)*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2+2*(12*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2+24*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3+6*(-coord[0]+self.a)*(-coord[0]+self.b)^4)*(-coord[1]+self.c)*(-coord[1]+self.d)^3

    def partialGxy5518(self,coord):

        return 3*(12*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2+24*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3+6*(-coord[0]+self.a)*(-coord[0]+self.b)^4)*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2+3*(12*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2+24*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3+6*(-coord[0]+self.a)*(-coord[0]+self.b)^4)*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3

    def partialGxy5519(self,coord):

        return 3*(12*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2+24*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3+6*(-coord[0]+self.a)*(-coord[0]+self.b)^4)*(-coord[1]+self.c)^4*(-coord[1]+self.d)^2+4*(12*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2+24*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3+6*(-coord[0]+self.a)*(-coord[0]+self.b)^4)*(-coord[1]+self.c)^3*(-coord[1]+self.d)^3

    def partialGxy5521(self,coord):

        return 4*(12*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2+24*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3+6*(-coord[0]+self.a)*(-coord[0]+self.b)^4)*(-coord[1]+self.c)*(-coord[1]+self.d)^3+(12*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2+24*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3+6*(-coord[0]+self.a)*(-coord[0]+self.b)^4)*(-coord[1]+self.d)^4

    def partialGxy5522(self,coord):

        return 4*(12*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2+24*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3+6*(-coord[0]+self.a)*(-coord[0]+self.b)^4)*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3+2*(12*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2+24*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3+6*(-coord[0]+self.a)*(-coord[0]+self.b)^4)*(-coord[1]+self.c)*(-coord[1]+self.d)^4

    def partialGxy5523(self,coord):

        return 4*(12*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2+24*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3+6*(-coord[0]+self.a)*(-coord[0]+self.b)^4)*(-coord[1]+self.c)^3*(-coord[1]+self.d)^3+3*(12*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2+24*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3+6*(-coord[0]+self.a)*(-coord[0]+self.b)^4)*(-coord[1]+self.c)^2*(-coord[1]+self.d)^4

    def partialGxy5524(self,coord):

        return 4*(12*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2+24*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3+6*(-coord[0]+self.a)*(-coord[0]+self.b)^4)*(-coord[1]+self.c)^4*(-coord[1]+self.d)^3+4*(12*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2+24*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3+6*(-coord[0]+self.a)*(-coord[0]+self.b)^4)*(-coord[1]+self.c)^3*(-coord[1]+self.d)^4

    def partialGxy5537(self,coord):

        return 2*(12*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2+24*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3+6*(-coord[0]+self.a)*(-coord[0]+self.b)^4)*(-coord[1]+self.c)^2+8*(12*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2+24*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3+6*(-coord[0]+self.a)*(-coord[0]+self.b)^4)*(-coord[1]+self.c)*(-coord[1]+self.d)+2*(12*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2+24*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3+6*(-coord[0]+self.a)*(-coord[0]+self.b)^4)*(-coord[1]+self.d)^2

    def partialGxy5538(self,coord):

        return 2*(12*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2+24*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3+6*(-coord[0]+self.a)*(-coord[0]+self.b)^4)*(-coord[1]+self.c)^3+12*(12*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2+24*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3+6*(-coord[0]+self.a)*(-coord[0]+self.b)^4)*(-coord[1]+self.c)^2*(-coord[1]+self.d)+6*(12*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2+24*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3+6*(-coord[0]+self.a)*(-coord[0]+self.b)^4)*(-coord[1]+self.c)*(-coord[1]+self.d)^2

    def partialGxy5539(self,coord):

        return 2*(12*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2+24*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3+6*(-coord[0]+self.a)*(-coord[0]+self.b)^4)*(-coord[1]+self.c)^4+16*(12*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2+24*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3+6*(-coord[0]+self.a)*(-coord[0]+self.b)^4)*(-coord[1]+self.c)^3*(-coord[1]+self.d)+12*(12*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2+24*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3+6*(-coord[0]+self.a)*(-coord[0]+self.b)^4)*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2

    def partialGxy5542(self,coord):

        return 6*(12*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2+24*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3+6*(-coord[0]+self.a)*(-coord[0]+self.b)^4)*(-coord[1]+self.c)^2*(-coord[1]+self.d)+12*(12*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2+24*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3+6*(-coord[0]+self.a)*(-coord[0]+self.b)^4)*(-coord[1]+self.c)*(-coord[1]+self.d)^2+2*(12*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2+24*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3+6*(-coord[0]+self.a)*(-coord[0]+self.b)^4)*(-coord[1]+self.d)^3

    def partialGxy5543(self,coord):

        return 6*(12*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2+24*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3+6*(-coord[0]+self.a)*(-coord[0]+self.b)^4)*(-coord[1]+self.c)^3*(-coord[1]+self.d)+18*(12*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2+24*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3+6*(-coord[0]+self.a)*(-coord[0]+self.b)^4)*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2+6*(12*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2+24*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3+6*(-coord[0]+self.a)*(-coord[0]+self.b)^4)*(-coord[1]+self.c)*(-coord[1]+self.d)^3

    def partialGxy5544(self,coord):

        return 6*(12*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2+24*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3+6*(-coord[0]+self.a)*(-coord[0]+self.b)^4)*(-coord[1]+self.c)^4*(-coord[1]+self.d)+24*(12*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2+24*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3+6*(-coord[0]+self.a)*(-coord[0]+self.b)^4)*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2+12*(12*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2+24*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3+6*(-coord[0]+self.a)*(-coord[0]+self.b)^4)*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3

    def partialGxy5547(self,coord):

        return 12*(12*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2+24*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3+6*(-coord[0]+self.a)*(-coord[0]+self.b)^4)*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2+16*(12*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2+24*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3+6*(-coord[0]+self.a)*(-coord[0]+self.b)^4)*(-coord[1]+self.c)*(-coord[1]+self.d)^3+2*(12*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2+24*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3+6*(-coord[0]+self.a)*(-coord[0]+self.b)^4)*(-coord[1]+self.d)^4

    def partialGxy5548(self,coord):

        return 12*(12*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2+24*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3+6*(-coord[0]+self.a)*(-coord[0]+self.b)^4)*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2+24*(12*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2+24*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3+6*(-coord[0]+self.a)*(-coord[0]+self.b)^4)*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3+6*(12*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2+24*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3+6*(-coord[0]+self.a)*(-coord[0]+self.b)^4)*(-coord[1]+self.c)*(-coord[1]+self.d)^4

    def partialGxy5549(self,coord):

        return 12*(12*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2+24*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3+6*(-coord[0]+self.a)*(-coord[0]+self.b)^4)*(-coord[1]+self.c)^4*(-coord[1]+self.d)^2+32*(12*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2+24*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3+6*(-coord[0]+self.a)*(-coord[0]+self.b)^4)*(-coord[1]+self.c)^3*(-coord[1]+self.d)^3+12*(12*(-coord[0]+self.a)^3*(-coord[0]+self.b)^2+24*(-coord[0]+self.a)^2*(-coord[0]+self.b)^3+6*(-coord[0]+self.a)*(-coord[0]+self.b)^4)*(-coord[1]+self.c)^2*(-coord[1]+self.d)^4

    def partialGxy5550(self,coord):

        return 12*(-coord[0]+self.a)^4*(-coord[0]+self.b)^2+32*(-coord[0]+self.a)^3*(-coord[0]+self.b)^3+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^4

    def partialGxy5551(self,coord):

        return (12*(-coord[0]+self.a)^4*(-coord[0]+self.b)^2+32*(-coord[0]+self.a)^3*(-coord[0]+self.b)^3+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^4)*(-coord[1]+self.c)

    def partialGxy5552(self,coord):

        return (12*(-coord[0]+self.a)^4*(-coord[0]+self.b)^2+32*(-coord[0]+self.a)^3*(-coord[0]+self.b)^3+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^4)*(-coord[1]+self.c)^2

    def partialGxy5553(self,coord):

        return (12*(-coord[0]+self.a)^4*(-coord[0]+self.b)^2+32*(-coord[0]+self.a)^3*(-coord[0]+self.b)^3+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^4)*(-coord[1]+self.c)^3

    def partialGxy5554(self,coord):

        return (12*(-coord[0]+self.a)^4*(-coord[0]+self.b)^2+32*(-coord[0]+self.a)^3*(-coord[0]+self.b)^3+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^4)*(-coord[1]+self.c)^4

    def partialGxy5555(self,coord):

        return (12*(-coord[0]+self.a)^4*(-coord[0]+self.b)^2+32*(-coord[0]+self.a)^3*(-coord[0]+self.b)^3+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^4)*(-coord[1]+self.d)

    def partialGxy5556(self,coord):

        return (12*(-coord[0]+self.a)^4*(-coord[0]+self.b)^2+32*(-coord[0]+self.a)^3*(-coord[0]+self.b)^3+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^4)*(-coord[1]+self.c)*(-coord[1]+self.d)

    def partialGxy5557(self,coord):

        return (12*(-coord[0]+self.a)^4*(-coord[0]+self.b)^2+32*(-coord[0]+self.a)^3*(-coord[0]+self.b)^3+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^4)*(-coord[1]+self.c)^2*(-coord[1]+self.d)

    def partialGxy5558(self,coord):

        return (12*(-coord[0]+self.a)^4*(-coord[0]+self.b)^2+32*(-coord[0]+self.a)^3*(-coord[0]+self.b)^3+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^4)*(-coord[1]+self.c)^3*(-coord[1]+self.d)

    def partialGxy5559(self,coord):

        return (12*(-coord[0]+self.a)^4*(-coord[0]+self.b)^2+32*(-coord[0]+self.a)^3*(-coord[0]+self.b)^3+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^4)*(-coord[1]+self.c)^4*(-coord[1]+self.d)

    def partialGxy5560(self,coord):

        return (12*(-coord[0]+self.a)^4*(-coord[0]+self.b)^2+32*(-coord[0]+self.a)^3*(-coord[0]+self.b)^3+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^4)*(-coord[1]+self.d)^2

    def partialGxy5561(self,coord):

        return (12*(-coord[0]+self.a)^4*(-coord[0]+self.b)^2+32*(-coord[0]+self.a)^3*(-coord[0]+self.b)^3+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^4)*(-coord[1]+self.c)*(-coord[1]+self.d)^2

    def partialGxy5562(self,coord):

        return (12*(-coord[0]+self.a)^4*(-coord[0]+self.b)^2+32*(-coord[0]+self.a)^3*(-coord[0]+self.b)^3+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^4)*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2

    def partialGxy5563(self,coord):

        return (12*(-coord[0]+self.a)^4*(-coord[0]+self.b)^2+32*(-coord[0]+self.a)^3*(-coord[0]+self.b)^3+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^4)*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2

    def partialGxy5564(self,coord):

        return (12*(-coord[0]+self.a)^4*(-coord[0]+self.b)^2+32*(-coord[0]+self.a)^3*(-coord[0]+self.b)^3+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^4)*(-coord[1]+self.c)^4*(-coord[1]+self.d)^2

    def partialGxy5565(self,coord):

        return (12*(-coord[0]+self.a)^4*(-coord[0]+self.b)^2+32*(-coord[0]+self.a)^3*(-coord[0]+self.b)^3+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^4)*(-coord[1]+self.d)^3

    def partialGxy5566(self,coord):

        return (12*(-coord[0]+self.a)^4*(-coord[0]+self.b)^2+32*(-coord[0]+self.a)^3*(-coord[0]+self.b)^3+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^4)*(-coord[1]+self.c)*(-coord[1]+self.d)^3

    def partialGxy5567(self,coord):

        return (12*(-coord[0]+self.a)^4*(-coord[0]+self.b)^2+32*(-coord[0]+self.a)^3*(-coord[0]+self.b)^3+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^4)*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3

    def partialGxy5568(self,coord):

        return (12*(-coord[0]+self.a)^4*(-coord[0]+self.b)^2+32*(-coord[0]+self.a)^3*(-coord[0]+self.b)^3+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^4)*(-coord[1]+self.c)^3*(-coord[1]+self.d)^3

    def partialGxy5569(self,coord):

        return (12*(-coord[0]+self.a)^4*(-coord[0]+self.b)^2+32*(-coord[0]+self.a)^3*(-coord[0]+self.b)^3+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^4)*(-coord[1]+self.c)^4*(-coord[1]+self.d)^3

    def partialGxy5570(self,coord):

        return (12*(-coord[0]+self.a)^4*(-coord[0]+self.b)^2+32*(-coord[0]+self.a)^3*(-coord[0]+self.b)^3+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^4)*(-coord[1]+self.d)^4

    def partialGxy5571(self,coord):

        return (12*(-coord[0]+self.a)^4*(-coord[0]+self.b)^2+32*(-coord[0]+self.a)^3*(-coord[0]+self.b)^3+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^4)*(-coord[1]+self.c)*(-coord[1]+self.d)^4

    def partialGxy5572(self,coord):

        return (12*(-coord[0]+self.a)^4*(-coord[0]+self.b)^2+32*(-coord[0]+self.a)^3*(-coord[0]+self.b)^3+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^4)*(-coord[1]+self.c)^2*(-coord[1]+self.d)^4

    def partialGxy5573(self,coord):

        return (12*(-coord[0]+self.a)^4*(-coord[0]+self.b)^2+32*(-coord[0]+self.a)^3*(-coord[0]+self.b)^3+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^4)*(-coord[1]+self.c)^3*(-coord[1]+self.d)^4

    def partialGxy5574(self,coord):

        return (12*(-coord[0]+self.a)^4*(-coord[0]+self.b)^2+32*(-coord[0]+self.a)^3*(-coord[0]+self.b)^3+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^4)*(-coord[1]+self.c)^4*(-coord[1]+self.d)^4

    def partialGxy5581(self,coord):

        return (12*(-coord[0]+self.a)^4*(-coord[0]+self.b)^2+32*(-coord[0]+self.a)^3*(-coord[0]+self.b)^3+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^4)*(-coord[1]+self.c)+(12*(-coord[0]+self.a)^4*(-coord[0]+self.b)^2+32*(-coord[0]+self.a)^3*(-coord[0]+self.b)^3+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^4)*(-coord[1]+self.d)

    def partialGxy5582(self,coord):

        return (12*(-coord[0]+self.a)^4*(-coord[0]+self.b)^2+32*(-coord[0]+self.a)^3*(-coord[0]+self.b)^3+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^4)*(-coord[1]+self.c)^2+2*(12*(-coord[0]+self.a)^4*(-coord[0]+self.b)^2+32*(-coord[0]+self.a)^3*(-coord[0]+self.b)^3+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^4)*(-coord[1]+self.c)*(-coord[1]+self.d)

    def partialGxy5583(self,coord):

        return (12*(-coord[0]+self.a)^4*(-coord[0]+self.b)^2+32*(-coord[0]+self.a)^3*(-coord[0]+self.b)^3+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^4)*(-coord[1]+self.c)^3+3*(12*(-coord[0]+self.a)^4*(-coord[0]+self.b)^2+32*(-coord[0]+self.a)^3*(-coord[0]+self.b)^3+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^4)*(-coord[1]+self.c)^2*(-coord[1]+self.d)

    def partialGxy5584(self,coord):

        return (12*(-coord[0]+self.a)^4*(-coord[0]+self.b)^2+32*(-coord[0]+self.a)^3*(-coord[0]+self.b)^3+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^4)*(-coord[1]+self.c)^4+4*(12*(-coord[0]+self.a)^4*(-coord[0]+self.b)^2+32*(-coord[0]+self.a)^3*(-coord[0]+self.b)^3+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^4)*(-coord[1]+self.c)^3*(-coord[1]+self.d)

    def partialGxy5586(self,coord):

        return 2*(12*(-coord[0]+self.a)^4*(-coord[0]+self.b)^2+32*(-coord[0]+self.a)^3*(-coord[0]+self.b)^3+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^4)*(-coord[1]+self.c)*(-coord[1]+self.d)+(12*(-coord[0]+self.a)^4*(-coord[0]+self.b)^2+32*(-coord[0]+self.a)^3*(-coord[0]+self.b)^3+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^4)*(-coord[1]+self.d)^2

    def partialGxy5587(self,coord):

        return 2*(12*(-coord[0]+self.a)^4*(-coord[0]+self.b)^2+32*(-coord[0]+self.a)^3*(-coord[0]+self.b)^3+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^4)*(-coord[1]+self.c)^2*(-coord[1]+self.d)+2*(12*(-coord[0]+self.a)^4*(-coord[0]+self.b)^2+32*(-coord[0]+self.a)^3*(-coord[0]+self.b)^3+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^4)*(-coord[1]+self.c)*(-coord[1]+self.d)^2

    def partialGxy5588(self,coord):

        return 2*(12*(-coord[0]+self.a)^4*(-coord[0]+self.b)^2+32*(-coord[0]+self.a)^3*(-coord[0]+self.b)^3+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^4)*(-coord[1]+self.c)^3*(-coord[1]+self.d)+3*(12*(-coord[0]+self.a)^4*(-coord[0]+self.b)^2+32*(-coord[0]+self.a)^3*(-coord[0]+self.b)^3+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^4)*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2

    def partialGxy5589(self,coord):

        return 2*(12*(-coord[0]+self.a)^4*(-coord[0]+self.b)^2+32*(-coord[0]+self.a)^3*(-coord[0]+self.b)^3+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^4)*(-coord[1]+self.c)^4*(-coord[1]+self.d)+4*(12*(-coord[0]+self.a)^4*(-coord[0]+self.b)^2+32*(-coord[0]+self.a)^3*(-coord[0]+self.b)^3+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^4)*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2

    def partialGxy5591(self,coord):

        return 3*(12*(-coord[0]+self.a)^4*(-coord[0]+self.b)^2+32*(-coord[0]+self.a)^3*(-coord[0]+self.b)^3+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^4)*(-coord[1]+self.c)*(-coord[1]+self.d)^2+(12*(-coord[0]+self.a)^4*(-coord[0]+self.b)^2+32*(-coord[0]+self.a)^3*(-coord[0]+self.b)^3+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^4)*(-coord[1]+self.d)^3

    def partialGxy5592(self,coord):

        return 3*(12*(-coord[0]+self.a)^4*(-coord[0]+self.b)^2+32*(-coord[0]+self.a)^3*(-coord[0]+self.b)^3+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^4)*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2+2*(12*(-coord[0]+self.a)^4*(-coord[0]+self.b)^2+32*(-coord[0]+self.a)^3*(-coord[0]+self.b)^3+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^4)*(-coord[1]+self.c)*(-coord[1]+self.d)^3

    def partialGxy5593(self,coord):

        return 3*(12*(-coord[0]+self.a)^4*(-coord[0]+self.b)^2+32*(-coord[0]+self.a)^3*(-coord[0]+self.b)^3+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^4)*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2+3*(12*(-coord[0]+self.a)^4*(-coord[0]+self.b)^2+32*(-coord[0]+self.a)^3*(-coord[0]+self.b)^3+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^4)*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3

    def partialGxy5594(self,coord):

        return 3*(12*(-coord[0]+self.a)^4*(-coord[0]+self.b)^2+32*(-coord[0]+self.a)^3*(-coord[0]+self.b)^3+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^4)*(-coord[1]+self.c)^4*(-coord[1]+self.d)^2+4*(12*(-coord[0]+self.a)^4*(-coord[0]+self.b)^2+32*(-coord[0]+self.a)^3*(-coord[0]+self.b)^3+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^4)*(-coord[1]+self.c)^3*(-coord[1]+self.d)^3

    def partialGxy5596(self,coord):

        return 4*(12*(-coord[0]+self.a)^4*(-coord[0]+self.b)^2+32*(-coord[0]+self.a)^3*(-coord[0]+self.b)^3+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^4)*(-coord[1]+self.c)*(-coord[1]+self.d)^3+(12*(-coord[0]+self.a)^4*(-coord[0]+self.b)^2+32*(-coord[0]+self.a)^3*(-coord[0]+self.b)^3+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^4)*(-coord[1]+self.d)^4

    def partialGxy5597(self,coord):

        return 4*(12*(-coord[0]+self.a)^4*(-coord[0]+self.b)^2+32*(-coord[0]+self.a)^3*(-coord[0]+self.b)^3+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^4)*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3+2*(12*(-coord[0]+self.a)^4*(-coord[0]+self.b)^2+32*(-coord[0]+self.a)^3*(-coord[0]+self.b)^3+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^4)*(-coord[1]+self.c)*(-coord[1]+self.d)^4

    def partialGxy5598(self,coord):

        return 4*(12*(-coord[0]+self.a)^4*(-coord[0]+self.b)^2+32*(-coord[0]+self.a)^3*(-coord[0]+self.b)^3+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^4)*(-coord[1]+self.c)^3*(-coord[1]+self.d)^3+3*(12*(-coord[0]+self.a)^4*(-coord[0]+self.b)^2+32*(-coord[0]+self.a)^3*(-coord[0]+self.b)^3+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^4)*(-coord[1]+self.c)^2*(-coord[1]+self.d)^4

    def partialGxy5599(self,coord):

        return 4*(12*(-coord[0]+self.a)^4*(-coord[0]+self.b)^2+32*(-coord[0]+self.a)^3*(-coord[0]+self.b)^3+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^4)*(-coord[1]+self.c)^4*(-coord[1]+self.d)^3+4*(12*(-coord[0]+self.a)^4*(-coord[0]+self.b)^2+32*(-coord[0]+self.a)^3*(-coord[0]+self.b)^3+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^4)*(-coord[1]+self.c)^3*(-coord[1]+self.d)^4

    def partialGxy5612(self,coord):

        return 2*(12*(-coord[0]+self.a)^4*(-coord[0]+self.b)^2+32*(-coord[0]+self.a)^3*(-coord[0]+self.b)^3+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^4)*(-coord[1]+self.c)^2+8*(12*(-coord[0]+self.a)^4*(-coord[0]+self.b)^2+32*(-coord[0]+self.a)^3*(-coord[0]+self.b)^3+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^4)*(-coord[1]+self.c)*(-coord[1]+self.d)+2*(12*(-coord[0]+self.a)^4*(-coord[0]+self.b)^2+32*(-coord[0]+self.a)^3*(-coord[0]+self.b)^3+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^4)*(-coord[1]+self.d)^2

    def partialGxy5613(self,coord):

        return 2*(12*(-coord[0]+self.a)^4*(-coord[0]+self.b)^2+32*(-coord[0]+self.a)^3*(-coord[0]+self.b)^3+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^4)*(-coord[1]+self.c)^3+12*(12*(-coord[0]+self.a)^4*(-coord[0]+self.b)^2+32*(-coord[0]+self.a)^3*(-coord[0]+self.b)^3+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^4)*(-coord[1]+self.c)^2*(-coord[1]+self.d)+6*(12*(-coord[0]+self.a)^4*(-coord[0]+self.b)^2+32*(-coord[0]+self.a)^3*(-coord[0]+self.b)^3+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^4)*(-coord[1]+self.c)*(-coord[1]+self.d)^2

    def partialGxy5614(self,coord):

        return 2*(12*(-coord[0]+self.a)^4*(-coord[0]+self.b)^2+32*(-coord[0]+self.a)^3*(-coord[0]+self.b)^3+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^4)*(-coord[1]+self.c)^4+16*(12*(-coord[0]+self.a)^4*(-coord[0]+self.b)^2+32*(-coord[0]+self.a)^3*(-coord[0]+self.b)^3+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^4)*(-coord[1]+self.c)^3*(-coord[1]+self.d)+12*(12*(-coord[0]+self.a)^4*(-coord[0]+self.b)^2+32*(-coord[0]+self.a)^3*(-coord[0]+self.b)^3+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^4)*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2

    def partialGxy5617(self,coord):

        return 6*(12*(-coord[0]+self.a)^4*(-coord[0]+self.b)^2+32*(-coord[0]+self.a)^3*(-coord[0]+self.b)^3+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^4)*(-coord[1]+self.c)^2*(-coord[1]+self.d)+12*(12*(-coord[0]+self.a)^4*(-coord[0]+self.b)^2+32*(-coord[0]+self.a)^3*(-coord[0]+self.b)^3+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^4)*(-coord[1]+self.c)*(-coord[1]+self.d)^2+2*(12*(-coord[0]+self.a)^4*(-coord[0]+self.b)^2+32*(-coord[0]+self.a)^3*(-coord[0]+self.b)^3+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^4)*(-coord[1]+self.d)^3

    def partialGxy5618(self,coord):

        return 6*(12*(-coord[0]+self.a)^4*(-coord[0]+self.b)^2+32*(-coord[0]+self.a)^3*(-coord[0]+self.b)^3+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^4)*(-coord[1]+self.c)^3*(-coord[1]+self.d)+18*(12*(-coord[0]+self.a)^4*(-coord[0]+self.b)^2+32*(-coord[0]+self.a)^3*(-coord[0]+self.b)^3+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^4)*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2+6*(12*(-coord[0]+self.a)^4*(-coord[0]+self.b)^2+32*(-coord[0]+self.a)^3*(-coord[0]+self.b)^3+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^4)*(-coord[1]+self.c)*(-coord[1]+self.d)^3

    def partialGxy5619(self,coord):

        return 6*(12*(-coord[0]+self.a)^4*(-coord[0]+self.b)^2+32*(-coord[0]+self.a)^3*(-coord[0]+self.b)^3+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^4)*(-coord[1]+self.c)^4*(-coord[1]+self.d)+24*(12*(-coord[0]+self.a)^4*(-coord[0]+self.b)^2+32*(-coord[0]+self.a)^3*(-coord[0]+self.b)^3+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^4)*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2+12*(12*(-coord[0]+self.a)^4*(-coord[0]+self.b)^2+32*(-coord[0]+self.a)^3*(-coord[0]+self.b)^3+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^4)*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3

    def partialGxy5622(self,coord):

        return 12*(12*(-coord[0]+self.a)^4*(-coord[0]+self.b)^2+32*(-coord[0]+self.a)^3*(-coord[0]+self.b)^3+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^4)*(-coord[1]+self.c)^2*(-coord[1]+self.d)^2+16*(12*(-coord[0]+self.a)^4*(-coord[0]+self.b)^2+32*(-coord[0]+self.a)^3*(-coord[0]+self.b)^3+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^4)*(-coord[1]+self.c)*(-coord[1]+self.d)^3+2*(12*(-coord[0]+self.a)^4*(-coord[0]+self.b)^2+32*(-coord[0]+self.a)^3*(-coord[0]+self.b)^3+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^4)*(-coord[1]+self.d)^4

    def partialGxy5623(self,coord):

        return 12*(12*(-coord[0]+self.a)^4*(-coord[0]+self.b)^2+32*(-coord[0]+self.a)^3*(-coord[0]+self.b)^3+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^4)*(-coord[1]+self.c)^3*(-coord[1]+self.d)^2+24*(12*(-coord[0]+self.a)^4*(-coord[0]+self.b)^2+32*(-coord[0]+self.a)^3*(-coord[0]+self.b)^3+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^4)*(-coord[1]+self.c)^2*(-coord[1]+self.d)^3+6*(12*(-coord[0]+self.a)^4*(-coord[0]+self.b)^2+32*(-coord[0]+self.a)^3*(-coord[0]+self.b)^3+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^4)*(-coord[1]+self.c)*(-coord[1]+self.d)^4

    def partialGxy5624(self,coord):

        return 12*(12*(-coord[0]+self.a)^4*(-coord[0]+self.b)^2+32*(-coord[0]+self.a)^3*(-coord[0]+self.b)^3+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^4)*(-coord[1]+self.c)^4*(-coord[1]+self.d)^2+32*(12*(-coord[0]+self.a)^4*(-coord[0]+self.b)^2+32*(-coord[0]+self.a)^3*(-coord[0]+self.b)^3+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^4)*(-coord[1]+self.c)^3*(-coord[1]+self.d)^3+12*(12*(-coord[0]+self.a)^4*(-coord[0]+self.b)^2+32*(-coord[0]+self.a)^3*(-coord[0]+self.b)^3+12*(-coord[0]+self.a)^2*(-coord[0]+self.b)^4)*(-coord[1]+self.c)^2*(-coord[1]+self.d)^4
