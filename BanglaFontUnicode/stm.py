#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  stm.py
#  
#  Copyright 2014-17 Sayan "Riju" Chakrabarti <s26c.sayan@gmail.com>
#
#  License: MIT 
#  
#  Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
# 
#  The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
# 
#  THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

def convert(txt):
  import re
  
  ## Ensure unicode input text
  #~ txt = txt.decode('utf-8')
  
  ## Block 0 : The Deletables!
  txt = txt.replace(u'\u0020',u' ') # space
  
  txt = txt.replace(u'\u00e9',u'')
  txt = txt.replace(u'\u00f9',u'')
  txt = txt.replace(u'\u00fe',u'')
  
  txt = txt.replace(u'\u00ec',u'')
  
  ## Block 1 : Single character of OP formed using two partial INPUT characters
  #~ txt = txt.replace(u'\u00ee\u00fb\u002a',u'রূ') ## added on 15/01/2015
  txt = txt.replace(u'\u00dd\u00c6',u'ট্র') ## added on 15/01/2015
  txt = txt.replace(u'\u00c1\u00b1',u'ম্প্র') ## added on 15/01/2015
  #~ txt = txt.replace(u'\u00c1\u00b1',u'X') ## added on 15/01/2015
  
  txt = txt.replace(u'\u00ee\u00fb',u'র')
  txt = txt.replace(u'\u00eb\u00fb',u'য়')
  txt = txt.replace(u'\u0078\u0079',u'আ')
  txt = txt.replace(u'\u0076\u007a',u'উ')
  txt = txt.replace(u'\u00a3\u007a',u'ই')
  txt = txt.replace(u'\u007e\u0152',u'ঞ')
  txt = txt.replace(u'\u0065\u00ab',u'ক্র')
  txt = txt.replace(u'\u005f\u00ab',u'ক্ত')
  txt = txt.replace(u'\u00a3\u00ab',u'হ্ন')
  
    ## SPECIALS (HACKS)!!!
  #~ txt = txt.replace(u'\u0073\u0069',u'ন্থ')
  txt = txt.replace(u'\u0073 \u0069',u'ন্থ')
  txt = txt.replace(u'\u00c1\u00ac',u'ম্ন')
  txt = txt.replace(u'\u00a7\u00ac',u'ন্ন') # added on 15/01/2015
  txt = txt.replace(u'\u0046\u0160',u'চ্ছ') # added on 15/01/2015
  txt = txt.replace(u'\u00b2\u00cc\u0026',u'প্রু')
  
  ## Added 15/01/2015
  txt = txt.replace(u'\u0021\u00df\u0066',u'স্ত্রি')
  txt = txt.replace(u'\u00df\u0066',u'স্ত্র')
  
  txt = txt.replace(u'\u0021\u00df\u00ac',u'স্নি')
  txt = txt.replace(u'\u00df\u00ac',u'স্ন')
  #~ txt = txt.replace(u'\u00df\u00f1',u'স্ক')
  txt = txt.replace(u'\u00df\u0025\u00f1',u'স্কু')
  txt = txt.replace(u'\u00df\u00f1\u0025',u'স্কু')
  txt = txt.replace(u'\u0073\u0066',u'ন্ত্র')
  
  txt = txt.replace(u'\u201e\u00cf',u'ক্ল') # added on 15/01/2015
  txt = txt.replace(u'\u0161\u00cf',u'ফ্ল')
  #~ txt = txt.replace(u'\u00de\u0069',u'স্থ')
  #~ txt = txt.replace(u'\u00df\u0069',u'স্থ')
  
  txt = txt.replace(u'\u0021\u00df\u0054\u00c9',u'স্ট্রি')
  txt = txt.replace(u'\u0021\u00df\u0054\u00c9',u'স্ট্রে')
  txt = txt.replace(u'\u0021\u00df\u0054\u00c9',u'স্ট্রৈ')
    
  txt = re.compile(ur'(.)\u0069').sub(ur'\1থ',txt)

  txt = txt.replace(u'\u2039\u00b5',u'জ্ব') # added on 15/01/2015    
  txt = re.compile(ur'\u0067(.)').sub(ur'\1ত্ব',txt)
  txt = re.compile(ur'\u0068(.)').sub(ur'\1ত',txt)
  #~ ‌‌added on 15/01/2015
  txt = re.compile(ur'\u006c(.)').sub(ur'\1তু',txt) 
  
  
  ## Block 2A : OP formed from single INPUT character : SWARABARNAS
  txt = txt.replace(u'\u0078',u'অ')
  txt = txt.replace(u'\u007B',u'ঈ')
  txt = txt.replace(u'\u007C',u'ঊ')
  txt = txt.replace(u'\u007D',u'ঋ')
  txt = txt.replace(u'\u007E',u'এ')
  txt = txt.replace(u'\u00fa',u'ঐ')
  txt = txt.replace(u'\u00E7',u'ও')
  txt = txt.replace(u'\u00E8',u'ঔ')
  txt = txt.replace(u'\u007F',u'৺')
  
  ## Block 2B : OP formed from single INPUT character : BYANJANS with MATRA/KAAR
  txt = txt.replace(u'\u00fd',u'হু')
  txt = txt.replace(u'\u003d',u'গু')
  
  ## Block 2C : OP formed from single INPUT character : BYANJANBARNAS
  txt = txt.replace(u'\u2018\u00fc',u'ঢ়') ## added on 16/01/2015
  txt = txt.replace(u'\u0076\u00fc',u'ড়')
  txt = txt.replace(u'\u0047',u'ঝ')
  txt = txt.replace(u'\u0048',u'ছ')  ##???
  txt = txt.replace(u'\u0057',u'ঢ')  ## ???
  txt = txt.replace(u'\u0076',u'ড')
  txt = txt.replace(u'\u00a1',u'ষ')
  txt = txt.replace(u'\u00a2',u'স')
  txt = txt.replace(u'\u00a3',u'হ')
  txt = txt.replace(u'\u00a6',u'ভ')
  txt = txt.replace(u'\u00dd',u'ট')
  txt = txt.replace(u'\u00e0',u'ঠ')
  txt = txt.replace(u'\u00ea',u'ৎ')
  txt = txt.replace(u'\u00eb',u'য')
  txt = txt.replace(u'\u00ed',u'থ')
  txt = txt.replace(u'\u00ee',u'ব')
  txt = txt.replace(u'\u00b9',u'ব')
  txt = txt.replace(u'\u0153',u'ল')
  txt = txt.replace(u'\u0160',u'ছ')
  txt = txt.replace(u'\u0161',u'ফ')
  txt = txt.replace(u'\u0178',u'শ')
  txt = txt.replace(u'\u0192',u'ঃ')
  txt = txt.replace(u'\u02c6',u'ঙ')
  txt = txt.replace(u'\u02dc',u'ন')
  txt = txt.replace(u'\u2018',u'ঢ')
  txt = txt.replace(u'\u2019',u'ণ')
  txt = txt.replace(u'\u201a',u'ং')
  txt = txt.replace(u'\u201c',u'ত')
  txt = txt.replace(u'\u201d',u'দ')
  txt = txt.replace(u'\u201e',u'ক')
  txt = txt.replace(u'\u2020',u'গ')
  txt = txt.replace(u'\u2021',u'ঘ')
  txt = txt.replace(u'\u2022',u'ধ')
  txt = txt.replace(u'\u2026',u'খ')
  txt = txt.replace(u'\u2030',u'চ')
  txt = txt.replace(u'\u2039',u'জ')
  txt = txt.replace(u'\u203a',u'ম')
  txt = txt.replace(u'\u2122',u'প')
  
  
  ## Block 2D : OP formed from single INPUT character : JUKTAKHYORS
  txt = txt.replace(u'\u0022',u'ক্ষ্ম')
  txt = txt.replace(u'\u002d',u'ঙ্ম')
  txt = txt.replace(u'\u003a',u'ক্স')
  txt = txt.replace(u'\u00c7',u'ক্ষ')
  txt = txt.replace(u'\u003e',u'গ্গ')
  txt = txt.replace(u'\u003f',u'গ্ধ')
  txt = txt.replace(u'\u0042',u'ঙ্ক')
  txt = txt.replace(u'\u0043',u'ঙ্খ')
  txt = txt.replace(u'\u0044',u'ঙ্গ')
  txt = txt.replace(u'\u0045',u'ক্ক')
  txt = txt.replace(u'\u0049',u'জ্জ')
  txt = txt.replace(u'\u004a',u'জ্ঝ')
  txt = txt.replace(u'\u004b',u'জ্ঞ')
  txt = txt.replace(u'\u004c',u'জ্র')
  txt = txt.replace(u'\u004d',u'ঞ্চ')
  txt = txt.replace(u'\u004e',u'ঞ্ছ')
  txt = txt.replace(u'\u004f',u'ঞ্জ')  
  txt = txt.replace(u'\u0050',u'ঞ্ঝ')
  txt = txt.replace(u'\u0051',u'ক্ট')
  txt = txt.replace(u'\u0052',u'ট্ট')
  txt = txt.replace(u'\u0055',u'ড্ড')
  txt = txt.replace(u'\u005a',u'ণ্ঠ')
  txt = txt.replace(u'\u005b',u'ণ্ড')
  txt = txt.replace(u'\u005c',u'ণ্ড্র')
  txt = txt.replace(u'\u005d',u'ণ্ন')
  txt = txt.replace(u'\u005f',u'ত্ত')  
  txt = txt.replace(u'\u0060',u'ক্ত্র') ## ???? 
  txt = txt.replace(u'\u0061',u'ত্থ')
  txt = txt.replace(u'\u0062',u'ত্ন')
  txt = txt.replace(u'\u0063',u'ত্ব')
  txt = txt.replace(u'\u0064',u'ত্ম')
  txt = txt.replace(u'\u0065',u'ত্র')
  txt = txt.replace(u'\u006a',u'দ্দ')
  txt = txt.replace(u'\u006b',u'দ্ধ')
  txt = txt.replace(u'\u006d',u'দ্ব')
  txt = txt.replace(u'\u006f',u'দ্র')
  txt = txt.replace(u'\u0070',u'দ্ম')
  txt = txt.replace(u'\u0071',u'দ্ভ')
  txt = txt.replace(u'\u0074',u'ন্ঠ')
  txt = txt.replace(u'\u0075',u'ন্ড')
  txt = txt.replace(u'\u0077',u'ন্দ্র')  
  txt = txt.replace(u'\u00a8',u'ন্দ')
  txt = txt.replace(u'\u00a9',u'ক্ম')
  txt = txt.replace(u'\u00aa',u'ন্স')  
  txt = txt.replace(u'\u00ae',u'প্ত')
  txt = txt.replace(u'\u00af',u'প্প')
  txt = txt.replace(u'\u00b0',u'প্স')
  txt = txt.replace(u'\u00b1',u'প্র')
  txt = txt.replace(u'\u00b6',u'ব্জ')
  txt = txt.replace(u'\u00b7',u'ব্দ')
  txt = txt.replace(u'\u00b8',u'ব্ধ')
  txt = txt.replace(u'\u00bc',u'ভ্র')
  txt = txt.replace(u'\u00bd',u'ম্ভ')
  txt = txt.replace(u'\u00be',u'ম্ভ্র')  
  txt = txt.replace(u'\u00d1',u'ল্গ')
  txt = txt.replace(u'\u00d2',u'ল্প')
  txt = txt.replace(u'\u00d3',u'ল্ড')
  txt = txt.replace(u'\u00d6',u'শু')
  txt = txt.replace(u'\u00d7',u'শ্র')
  txt = txt.replace(u'\u00d8',u'শ্চ')
  txt = txt.replace(u'\u00db',u'ষ্ঠ')
  txt = txt.replace(u'\u00e1',u'হ্ম')
  txt = txt.replace(u'\u00e2',u'হ্ল')
  txt = txt.replace(u'\u00e3',u'হ্ণ')
  txt = txt.replace(u'\u00f5',u'ন্ধ')
  txt = txt.replace(u'\u20ac',u'ল্গু')
  
  
  ## Block 3A : Partial OP character from single partial INPUT character : LEFT appear (to be ligature-d on OP) 
  txt = txt.replace(u'\u0040',u'গ্')
  txt = txt.replace(u'\u0041',u'ঙ্')
  txt = txt.replace(u'\u0046',u'চ্')  
  txt = txt.replace(u'\u0058',u'ড়্‌')
  txt = txt.replace(u'\u005e',u'ণ্‌')
  txt = txt.replace(u'\u0072',u'ন্')
  txt = txt.replace(u'\u00a7',u'ন্')
  txt = txt.replace(u'\u0073 ',u'ন্') #####
  txt = txt.replace(u'\u0073',u'ন্') 
  txt = txt.replace(u'\u00b2',u'প্')
  txt = txt.replace(u'\u00c1',u'ম্')
  txt = txt.replace(u'\u00cd',u'ল্')
  txt = txt.replace(u'\u00ce',u'ল্')
  txt = txt.replace(u'\u00d9',u'শ্')
  txt = txt.replace(u'\u00dc',u'ষ্')
  txt = txt.replace(u'\u00de',u'স্')
  txt = txt.replace(u'\u00df',u'স্')
  txt = txt.replace(u'\u00e5',u'দ্')
  
  ## Block 3A : Partial OP character from single partial INPUT character : RIGHT appear (to be ligature-d on OP) 
  txt = re.compile(ur'(.)\u00').sub(ur'\1',txt)
  txt = re.compile(ur'(.)\u003b').sub(ur'\1ক্র',txt)
  txt = re.compile(ur'(.)\u003c').sub(ur'\1‌খ',txt)
  txt = re.compile(ur'(.)\u0054').sub(ur'\1ট',txt)
  txt = re.compile(ur'(.)\u0066').sub(ur'‌\1ত্র',txt)
  txt = re.compile(ur'(.)\u006c').sub(ur'\1‌ত্ত',txt)
  txt = re.compile(ur'(.)\u00ac').sub(ur'\1‌ন',txt)
  txt = re.compile(ur'(.)\u00b3').sub(ur'\1ফ',txt)
  txt = re.compile(ur'(.)\u00b4').sub(ur'\1ব',txt)
  txt = re.compile(ur'(.)\u00b5').sub(ur'\1ব',txt)
  txt = re.compile(ur'(.)\u00ba').sub(ur'\1ব',txt)
  txt = re.compile(ur'(.)\u00bb').sub(ur'\1ব',txt)
  txt = re.compile(ur'(.)\u00bf').sub(ur'\1ম',txt)
  txt = re.compile(ur'(.)\u00c0').sub(ur'\1ণ',txt)
  txt = re.compile(ur'(.)\u00c2').sub(ur'ম',txt)
  txt = re.compile(ur'(.)\u00c3').sub(ur'\1ম',txt)
  txt = re.compile(ur'(.)\u00cf').sub(ur'\1ল',txt)
  txt = re.compile(ur'(.)\u00d4').sub(ur'\1ল',txt)
  txt = re.compile(ur'(.)\u00d5').sub(ur'\1ল',txt)
  txt = re.compile(ur'(.)\u00f1').sub(ur'\1ক',txt)
  txt = re.compile(ur'(.)\u00f8').sub(ur'\1ন',txt)
  
   
  ## Block 4 : Ref, fola-s, matra-s
  #~ txt =  txt.replace(u'\u00a4',u'ঁ')
  #~ txt =  txt.replace(u'\u00a5',u'ঁ')
  
  ## Chandrabindu (added here on 15/01/2015)
  txt = re.compile(ur'(.)\u00a4\u00c4\u0079').sub(ur'\1্যাঁ',txt) 
  txt = re.compile(ur'(.)\u00a5\u00c4\u0079').sub(ur'\1্যাঁ',txt) 
  #ঁ  া  ্য ্ঁ 
  txt = re.compile(ur'(.)\u00a4\u0079').sub(ur'\1াঁ',txt)
  txt = re.compile(ur'(.)\u00a5\u0079').sub(ur'\1াঁ',txt)
  txt = re.compile(ur'\u00f6(.)\u00a4\u00ef').sub(ur'\1ৌঁ',txt)
  txt = re.compile(ur'\u00f6(.)\u00a5\u00ef').sub(ur'\1ৌঁ',txt)
  
  txt = re.compile(ur'(.)\u00c5').sub(ur'র্\1',txt) ## Ref
 
  txt = re.compile(ur'(.)\u00cc').sub(ur'\1র‌',txt) ## ro-fola-s
  txt = re.compile(ur'(.)\u00cb').sub(ur'\1র‌',txt)
  txt = re.compile(ur'(.)\u00ca').sub(ur'\1র‌',txt)
  txt = re.compile(ur'(.)\u00c9').sub(ur'\1র‌',txt)
  txt = re.compile(ur'(.)\u00c8').sub(ur'\1র‌',txt)
  txt = re.compile(ur'(.)\u00c6').sub(ur'\1র‌',txt)

  ## jaw-fola (addded on 15/01/2015)
  txt = re.compile(ur'(.)\u0025\u00c4').sub(ur'\1্যু',txt)
  txt = re.compile(ur'(.)\u00c4').sub(ur'\1্য',txt)
  #~ txt = txt.replace(u'\u00c4',u'্য') ## jaw-fola
  
  ## Block 5A : kaar-s (left appears)
  txt = re.compile(ur'\u00f6(.)\u0079').sub(ur'\1ো',txt)
  txt = re.compile(ur'\u00f6(.)\u00ef').sub(ur'\1ৌ',txt)
  #~ txt = re.compile(ur'\u00f6(.*)\u0079\u007a').sub(ur'\1ৌ',txt)

  txt = re.compile(ur'\u0021(.্‌?.?)').sub(ur'\1ি',txt) ## For juktakhyors
  txt = re.compile(ur'\u0021(.)').sub(ur'\1ি',txt)

  txt = re.compile(ur'\u00f6(.্‌?.?)').sub(ur'\1ে',txt) ## For juktakhyors
  txt = re.compile(ur'\u00f6(.)').sub(ur'\1ে',txt)
  
  txt = re.compile(ur'\u00f7(.্‌?.?)').sub(ur'\1ৈ',txt)  ## For juktakhyors
  txt = re.compile(ur'\u00f7(.)').sub(ur'\1ৈ',txt)
  
 
  ## Block 5B : Kaar-s (Right Appears)
  txt = txt.replace(u'\u0079',u'া')
  txt = txt.replace(u'\u0023',u'ী')
  txt = txt.replace(u'\u0024',u'ু')
  txt = txt.replace(u'\u0025',u'ু')
  txt = txt.replace(u'\u0026',u'ু')
  txt = txt.replace(u'\u0028',u'ূ') 
  txt = txt.replace(u'\u0029',u'ূ')
  txt = txt.replace(u'\u002a',u'ূ') # added on 15/01/2015
  txt = txt.replace(u'\u002b',u'ৃ')
  txt = txt.replace(u'\u002c',u'ৃ')
  
 
  ## Block 6 : OP formed from single INPUT character : NUMERALS & PUNCTUATIONS
  txt = txt.replace(u'\u0030',u'০')
  txt = txt.replace(u'\u0031',u'১')
  txt = txt.replace(u'\u0032',u'২')
  txt = txt.replace(u'\u0033',u'৩')
  txt = txt.replace(u'\u0034',u'৪')
  txt = txt.replace(u'\u0035',u'৫')
  txt = txt.replace(u'\u0036',u'৬')
  txt = txt.replace(u'\u0037',u'৭')
  txt = txt.replace(u'\u0038',u'৮')
  txt = txt.replace(u'\u0039',u'৯')
  
  txt = txt.replace(u'\u002f',u'/')
  txt = txt.replace(u'\u0053',u'(')  
  txt = txt.replace(u'\u0056',u')')  
  txt = txt.replace(u'\u00a0',u'*')  
  txt = txt.replace(u'\u00ad',u':')  
  txt = txt.replace(u'\u00d0',u'।')  
  txt = txt.replace(u'\u00da',u'?')  
  txt = txt.replace(u'\u00e6',u'!')  
  txt = txt.replace(u'\u00f2',u'‘')  
  txt = txt.replace(u'\u00f3',u'’')  
  txt = txt.replace(u'\u00f4',u'-')  
  txt = txt.replace(u'\u2013',u',')  
  txt = txt.replace(u'\u2014',u';')  
  
  txt = txt.replace(u'\u00e4',u'্‌')  ## added on 16/01/2015
  
  ## Chandrabindu
  txt =  txt.replace(u'\u00a4',u'ঁ')
  txt =  txt.replace(u'\u00a5',u'ঁ')


  
  return txt
