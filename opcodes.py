
by_value = {
        0x00: 'STOP',
        0x01: 'ADD', 
        0x02: 'MUL', 
        0x03: 'SUB', 
        0x04: 'DIV', 
        0x05: 'SDIV', 
        0x06: 'MOD', 
        0x07: 'SMOD', 
        0x08: 'ADDMOD', 
        0x09: 'MULMOD', 
        0x0a: 'EXP', 
        0x0b: 'SIGNEXTEND', 
        0x0c: '0x0c',
        0x0d: '0x0d',
        0x0e: '0x0e',
        0x0f: '0x0f',
        0x10: 'LT',
        0x11: 'GT',
        0x12: 'SLT',
        0x13: 'SGT',
        0x14: 'EQ',
        0x15: 'ISZERO',
        0x16: 'AND',
        0x17: 'OR',
        0x18: 'XOR',
        0x19: 'NOT',
        0x1a: 'BYTE',
        0x1b: 'SHL',
        0x1c: 'SHR',
        0x1d: 'SAR',
        0x1e: '0x1e',
        0x1f: '0x1f',
        0x20: 'KECCAK256',
        0x21: '0x21',
        0x22: '0x22',
        0x23: '0x23',
        0x24: '0x24',
        0x25: '0x25',
        0x26: '0x26',
        0x27: '0x27',
        0x28: '0x28',
        0x29: '0x29',
        0x2a: '0x2a',
        0x2b: '0x2b',
        0x2c: '0x2c',
        0x2d: '0x2d',
        0x2e: '0x2e',
        0x2f: '0x2f',
        0x30: 'ADDRESS',
        0x31: 'BALANCE',
        0x32: 'ORIGIN',
        0x33: 'CALLER',
        0x34: 'CALLVALUE',
        0x35: 'CALLDATALOAD',
        0x36: 'CALLDATASIZE',
        0x37: 'CALLDATACOPY',
        0x38: 'CODESIZE',
        0x39: 'CODECOPY',
        0x3a: 'GASPRICE',
        0x3b: 'EXTCODESIZE',
        0x3c: 'EXTCODECOPY',
        0x3d: 'RETURNDATASIZE',
        0x3e: 'RETURNDATACOPY',
        0x3f: 'EXTCODEHASH',
        0x40: 'BLOCKHASH',
        0x41: 'COINBASE',
        0x42: 'TIMESTAMP',
        0x43: 'NUMBER',
        0x44: 'DIFFICULTY',
        0x45: 'GASLIMIT',
        0x46: 'CHAINID',
        0x47: 'SELFBALANCE',
        0x48: '0x48',
        0x49: '0x49',
        0x4a: '0x4a',
        0x4b: '0x4b',
        0x4c: '0x4c',
        0x4d: '0x4d',
        0x4e: '0x4e',
        0x4f: '0x4f',
        0x50: 'POP',
        0x51: 'MLOAD',
        0x52: 'MSTORE',
        0x53: 'MSTORE8',
        0x54: 'SLOAD',
        0x55: 'SSTORE',
        0x56: 'JUMP',
        0x57: 'JUMPI',
        0x58: 'PC',
        0x59: 'MSIZE',
        0x5a: 'GAS',
        0x5b: 'JUMPDEST',
        0x5c: '0x5c',
        0x5d: '0x5d',
        0x5e: '0x5e',
        0x5f: '0x5f',
        0x60: 'PUSH1',
        0x61: 'PUSH2',
        0x62: 'PUSH3',
        0x63: 'PUSH4',
        0x64: 'PUSH5',
        0x65: 'PUSH6',
        0x66: 'PUSH7',
        0x67: 'PUSH8',
        0x68: 'PUSH9',
        0x69: 'PUSH10',
        0x6a: 'PUSH11',
        0x6b: 'PUSH12',
        0x6c: 'PUSH13',
        0x6d: 'PUSH14',
        0x6e: 'PUSH15',
        0x6f: 'PUSH16',
        0x70: 'PUSH17',
        0x71: 'PUSH18',
        0x72: 'PUSH19',
        0x73: 'PUSH20',
        0x74: 'PUSH21',
        0x75: 'PUSH22',
        0x76: 'PUSH23',
        0x77: 'PUSH24',
        0x78: 'PUSH25',
        0x79: 'PUSH26',
        0x7a: 'PUSH27',
        0x7b: 'PUSH28',
        0x7c: 'PUSH29',
        0x7d: 'PUSH30',
        0x7e: 'PUSH31',
        0x7f: 'PUSH32',
        0x80: 'DUP1',
        0x81: 'DUP2',
        0x82: 'DUP3',
        0x83: 'DUP4',
        0x84: 'DUP5',
        0x85: 'DUP6',
        0x86: 'DUP7',
        0x87: 'DUP8',
        0x88: 'DUP9',
        0x89: 'DUP10',
        0x8a: 'DUP11',
        0x8b: 'DUP12',
        0x8c: 'DUP13',
        0x8d: 'DUP14',
        0x8e: 'DUP15',
        0x8f: 'DUP16',
        0x90: 'SWAP1',
        0x91: 'SWAP2',
        0x92: 'SWAP3',
        0x93: 'SWAP4',
        0x94: 'SWAP5',
        0x95: 'SWAP6',
        0x96: 'SWAP7',
        0x97: 'SWAP8',
        0x98: 'SWAP9',
        0x99: 'SWAP10',
        0x9a: 'SWAP11',
        0x9b: 'SWAP12',
        0x9c: 'SWAP13',
        0x9d: 'SWAP14',
        0x9e: 'SWAP15',
        0x9f: 'SWAP16',
        0xa0: 'LOG0',
        0xa1: 'LOG1',
        0xa2: 'LOG2',
        0xa3: 'LOG3',
        0xa4: 'LOG4',
        0xa5: '0xa5',
        0xa6: '0xa6',
        0xa7: '0xa7',
        0xa8: '0xa8',
        0xa9: '0xa9',
        0xaa: '0xaa',
        0xab: '0xab',
        0xac: '0xac',
        0xad: '0xad',
        0xae: '0xae',
        0xaf: '0xaf',
        0xb0: '0xb0',
        0xb1: '0xb1',
        0xb2: '0xb2',
        0xb3: '0xb3',
        0xb4: '0xb4',
        0xb5: '0xb5',
        0xb6: '0xb6',
        0xb7: '0xb7',
        0xb8: '0xb8',
        0xb9: '0xb9',
        0xba: '0xba',
        0xbb: '0xbb',
        0xbc: '0xbc',
        0xbd: '0xbd',
        0xbe: '0xbe',
        0xbf: '0xbf',
        0xc0: '0xc0',
        0xc1: '0xc1',
        0xc2: '0xc2',
        0xc3: '0xc3',
        0xc4: '0xc4',
        0xc5: '0xc5',
        0xc6: '0xc6',
        0xc7: '0xc7',
        0xc8: '0xc8',
        0xc9: '0xc9',
        0xca: '0xca',
        0xcb: '0xcb',
        0xcc: '0xcc',
        0xcd: '0xcd',
        0xce: '0xce',
        0xcf: '0xcf',
        0xd0: '0xd0',
        0xd1: '0xd1',
        0xd2: '0xd2',
        0xd3: '0xd3',
        0xd4: '0xd4',
        0xd5: '0xd5',
        0xd6: '0xd6',
        0xd7: '0xd7',
        0xd8: '0xd8',
        0xd9: '0xd9',
        0xda: '0xda',
        0xdb: '0xdb',
        0xdc: '0xdc',
        0xdd: '0xdd',
        0xde: '0xde',
        0xdf: '0xdf',
        0xe0: '0xe0',
        0xe1: '0xe1',
        0xe2: '0xe2',
        0xe3: '0xe3',
        0xe4: '0xe4',
        0xe5: '0xe5',
        0xe6: '0xe6',
        0xe7: '0xe7',
        0xe8: '0xe8',
        0xe9: '0xe9',
        0xea: '0xea',
        0xeb: '0xeb',
        0xec: '0xec',
        0xed: '0xed',
        0xee: '0xee',
        0xef: '0xef',
        0xf0: 'CREATE',
        0xf1: 'CALL',
        0xf2: 'CALLCODE',
        0xf3: 'RETURN',
        0xf4: 'DELEGATECALL',
        0xf5: 'CREATE2',
        0xf6: '0xf6',
        0xf7: '0xf7',
        0xf8: '0xf8',
        0xf9: '0xf9',
        0xfa: 'STATICCALL',
        0xfb: '0xfb',
        0xfc: '0xfc',
        0xfd: 'REVERT',
        0xfe: 'INVALID',
        0xff: 'SELFDESTRUCT',
    }

aliases = {
        'SHA3': 'KECCAK256'
        }

def get_opcodes_by_name():
    ops_by_name = {}
    for k in by_value.keys():
        if by_value[k] == '-':
            ops_by_name[hex(k)] = k
        else:
            val = by_value[k]
            ops_by_name[val] = k

    return ops_by_name

by_name = get_opcodes_by_name()

def get_op_counter():
    opcounter = {}
    for key in by_value:
        opcounter[key] = 0
    return opcounter

def get_opnumber(opname):
    if opname in by_name.keys():
        return by_name[opname]
    elif opname in aliases.keys():
        opname = aliases[opname]
        return get_opnumber(opname)
    elif opname[:6] == 'opcode': # opcode ?? not defined
        err_msg = opname.split(' ')
        opvalue = int(err_msg[1], 16) # extract opcode number from error message
        opname = by_value[opvalue]
        return get_opnumber(opname)
    else:
        opvalue = int('0x' + opname, 16)
        opname = by_value[opvalue]
        return get_opnumber(opname)
    print('ERROR: ', '`' + opname + '`', 'not found!')
    print(by_name)
    raise ValueError(opname)

def update_op_counter(opcounter, opname, opvalue):
    value = int(opvalue)
    op_key = get_opnumber(opname)

    opcounter[op_key] = value
    #print(op_key, ':', opcounter[op_key])

    return opcounter


