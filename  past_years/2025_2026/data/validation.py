def valid_sequence(sequence, valid_characters):
    for c in sequence:
        if c.upper() not in valid_characters:
            return False

    return True

def validate_dna(sequence):
    return valid_sequence(sequence, ['A', 'T', 'G', 'C'])

def validate_rna(sequence):
    return valid_sequence(sequence, ['A', 'U', 'G', 'C'])

def validate_protein(sequence):
    return valid_sequence(
        sequence,
        [
            'A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L',
            'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'Y'
        ]
    )
