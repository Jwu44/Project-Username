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
            ' LastNameOnly',
            'fa rt',
            'Rat Man123',
            'Hubert Blaine Wolfeschlegelsteinhausenbergerdorff Sr',
            '',
            'a b',
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

    name2 = names[0].split(" ")
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

    name1 = names[0].split(" ")
    username = firstLetter_lastName(name1)
    assert username == 'f'

    name2 = names[1].split(" ")
    name6 = names[5].split(" ")
    name8 = names[7].split(" ")
    with pytest.raises(IndexError):
        firstLetter_lastName(name2)
        firstLetter_lastName(name6)
        firstLetter_lastName(name8)


    name3 = names[2].split(" ")
    username = firstLetter_lastName(name3)
    assert username == 'frt'

    name4 = names[3].split(" ")
    username = firstLetter_lastName(name4)
    assert username == 'rman'

    name5 = names[4].split(" ")
    username = firstLetter_lastName(name5)
    assert username == 'hsr'

    name7 = names[6].split(" ")
    username = firstLetter_lastName(name7)
    assert username == 'ab'
