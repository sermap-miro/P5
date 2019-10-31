# -*- coding: utf-8 -*-
'''
Gestion de la mémoire non volatile (NVS)
'''
# Relecture des paramètres de bases
import pycom
# #pycom.nvs_set('ARM', int(m.arm_id, 16))


def memory_get(name='MIR', default_value=1):
    ''' Retourne une valeur par défaut si la mémoire NVS
    ne contient pas l'élément recherché '''
    try:
        _value = pycom.nvs_get(name)
    except Exception:
        _value = None
    if _value is None:
        _value = default_value
    return _value
    # try:
    #     #Memory_Value = pycom.nvs_get(Name)
    #     return pycom.nvs_get(name)
    # except Exception:
    #     return default_value
    # except BaseException:
    #     return default_value


def memory_set(name='MIR', value=0):
    ''' Enregistre une valeur dans la mémoire NVS '''
    try:
        pycom.nvs_set(name, value)
    except Exception:
        print("Erreur lors de la Memory Set")
        # pass


# def Set_ARM_ID(arm_id=_arm_id):
#     m.arm_id = arm_id
#     pycom.nvs_set('ARM', int(m.arm_id, 16))
#
#
# def Set_MIR_ID(mir_id=_mir_id):
#     m.mir_id = mir_id
#     pycom.nvs_set('MIR', m.mir_id)

# Set_ARM_ID()
#
# Set_MIR_ID()
