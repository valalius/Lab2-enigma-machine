def enigma(op_type, shift_n, r1, r2, r3, msg):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    rotors = [r1, r2, r3]

    if op_type == "ENCODE":
        # Зсув Цезаря з інкрементом
        shifted_chars = []
        for i, char in enumerate(msg.upper()):
            current_shift = shift_n + i
            orig_idx = alphabet.index(char)
            new_idx = (orig_idx + current_shift) % 26
            shifted_chars.append(alphabet[new_idx])

        # Проходження через ротори
        current_chars = shifted_chars
        for rotor in rotors:
            output = []
            for char in current_chars:
                idx = alphabet.index(char)
                output.append(rotor[idx])
            current_chars = output

        return "".join(current_chars)

    elif op_type == "DECODE":
        # Зворотне проходження через ротори
        current_chars = list(msg.upper())
        for rotor in reversed(rotors):
            output = []
            for char in current_chars:
                idx = rotor.index(char)
                output.append(alphabet[idx])
            current_chars = output

        # Зворотний зсув Цезаря з інкрементом
        decoded_chars = []
        for i, char in enumerate(current_chars):
            current_shift = shift_n + i
            orig_idx = alphabet.index(char)
            new_idx = (orig_idx - current_shift) % 26
            decoded_chars.append(alphabet[new_idx])

        return "".join(decoded_chars)
    else:
        return ""

if __name__ == "__main__":
    operation = input().strip()
    start_num = int(input())
    rotor1 = input().strip()
    rotor2 = input().strip()
    rotor3 = input().strip()
    text = input().strip()

    result = enigma(operation, start_num, rotor1, rotor2, rotor3, text)
    print(result)