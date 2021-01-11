from typing import List

from test_framework import generic_test, test_utils

# DG ~O(3^n) time and space
def phone_mnemonic(phone_number: str) -> List[str]:
    m = {'1': '1', '2': 'ABC', '3':'DEF', '4':'GHI', '5':'JKL',
         '6':'MNO', '7':'PQRS', '8':'TUV', '9':'WXYZ', '0':'0'}
    
    def phone_mnemonic_helper(L:list, ph:str, soFar:str=""):
        if not ph:
            L.append(soFar)
            return
        for ch in m[ph[0]]:
            phone_mnemonic_helper(L, ph[1:], soFar+(ch))
    
    if not phone_number: return []
    L = []
    phone_mnemonic_helper(L, phone_number)
    return L


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'phone_number_mnemonic.py',
            'phone_number_mnemonic.tsv',
            phone_mnemonic,
            comparator=test_utils.unordered_compare))
