'''
Authors:    
    Justin Wu

Date:       
    12 May 2021
'''

import pytest
from src.name_gen import firstLetter_lastName, firstName_lastName, \
    add_number, add_specialChar

# --------------------------------------------------------------------------------------- # 
# ----------------------------- Fixture Set Up ------------------------------------------ #
# --------------------------------------------------------------------------------------- #

@pytest.fixture
def create_users():
    '''
    Fixture sets up a mix of full names.
    '''
    return {
        'normal': [
            'Kanye East',
            'Michael Scott',
            'Justin Wu',
            'Je Suis'
        ],
        'special': [
            'FirstNameOnly ',
            ' LastNameOnly'
            'fa rt',
            'Rat Man123',
            'a b'
            ' '
        ]
    }

# --------------------------------------------------------------------------------------- # 
# ----------------------------- FirstL_LastName Tests------------------------------------ #
# --------------------------------------------------------------------------------------- #
def test_normal_firstL_lastName(create_users):
    '''
    Tests for correct firstL_lastName output for normal full names.
    '''
    names = create_users['normal']

    name1 = names[0].split(" ")
    username = firstLetter_lastName(name1)
    assert username == 'keas'

    name2 = names[1].split(" ")
    username = firstLetter_lastName(name2)
    assert username == 'msco'

    name3 = names[2].split(" ")
    username = firstLetter_lastName(name3)
    assert username == 'jwu'

    name4 = names[3].split(" ")
    username = firstLetter_lastName(name4)
    assert username == 'jsui'

def test_normal_firstL_lastName(create_users):
    '''
    Tests for correct firstL_lastName output for special full names.
    '''
    names = create_users['special']



