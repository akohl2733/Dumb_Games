def check(dict, s):        
    if dict['UL'] == s and dict['UM'] == s and dict['UR'] == s:
        return f'Winner ({s})'
    if dict['ML'] == s and dict['MM'] == s and dict['MR'] == s:
        return f'Winner ({s})'
    if dict['BL'] == s and dict['BM'] == s and dict['BR'] == s:
        return f'Winner ({s})'
    if dict['UL'] == s and dict['ML'] == s and dict['BL'] == s:
        return f'Winner ({s})'
    if dict['UM'] == s and dict['MM'] == s and dict['BM'] == s:
        return f'Winner ({s})'
    if dict['UR'] == s and dict['MR'] == s and dict['BR'] == s:
        return f'Winner ({s})'
    if dict['UL'] == s and dict['MM'] == s and dict['BR'] == s:
        return f'Winner ({s})'
    if dict['UR'] == s and dict['MM'] == s and dict['BL'] == s:
        return f'Winner ({s})'